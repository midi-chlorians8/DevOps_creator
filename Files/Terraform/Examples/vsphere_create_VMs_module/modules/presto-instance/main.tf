terraform {
  required_version = "~> 1.6"
  required_providers {
    vsphere = {
      source  = "hashicorp/vsphere"
      version = "2.5.1"
    }
  }
}

provider "vsphere" {
  user                 = var.vsphere_user
  password             = var.vsphere_password
  vsphere_server       = var.vsphere_server
  allow_unverified_ssl = true
}


data "vsphere_datacenter" "datacenter" {
  name = var.vsphere_datacenter
}

data "vsphere_datastore" "datastore" {
  name          = var.vsphere_datastore
  datacenter_id = data.vsphere_datacenter.datacenter.id
}

data "vsphere_compute_cluster" "cluster" {
  name          = var.vsphere_compute_cluster
  datacenter_id = data.vsphere_datacenter.datacenter.id
}

data "vsphere_network" "network" {
  name          = var.vsphere_network
  datacenter_id = data.vsphere_datacenter.datacenter.id
}

data "vsphere_resource_pool" "pool" {
  name          = var.vsphere_resource_pool
  datacenter_id = data.vsphere_datacenter.datacenter.id
}

data "vsphere_virtual_machine" "presto_cluster_template" {
  name          = var.presto_cluster_template
  datacenter_id = data.vsphere_datacenter.datacenter.id
}


resource "vsphere_virtual_machine" "presto-instance" {
  count = var.presto_instances_count
  name  = "presto-${var.presto_name}${var.presto_instances_count > 1 ? "-${count.index}" : ""}-${var.vsphere_environment}"

  resource_pool_id = data.vsphere_resource_pool.pool.id
  datastore_id     = data.vsphere_datastore.datastore.id

  num_cpus = var.num_cpus
  memory   = var.memory_instance
  guest_id = data.vsphere_virtual_machine.presto_cluster_template.guest_id

  network_interface {
    network_id   = data.vsphere_network.network.id
    adapter_type = data.vsphere_virtual_machine.presto_cluster_template.network_interface_types[0]
  }

  disk {
    label            = "disk0"
    size             = var.disk_size_presto
    thin_provisioned = false
  }

  clone {
    template_uuid = data.vsphere_virtual_machine.presto_cluster_template.id
    timeout       = var.clone_timeout_total

    customize {
      linux_options {
        host_name = "presto-${var.presto_name}${var.presto_instances_count > 1 ? "-${count.index}" : ""}-${var.vsphere_environment}"
        domain    = var.domain
      }

      network_interface {
        ipv4_address = var.ipv4_address_presto[count.index]
        ipv4_netmask = var.ipv4_netmask
      }

      ipv4_gateway    = var.vsphere_ipv4_gateway
      dns_server_list = var.dns_server_list
    }
  }

}

resource "null_resource" "disk_resize_send_scrypt" {
  count      = var.presto_instances_count
  depends_on = [vsphere_virtual_machine.presto-instance]
  provisioner "file" {
    source      = "./disk_resize.sh"
    destination = "./disk_resize.sh"
  }
  triggers = {
    always_run = timestamp()
  }
  connection {
    host     = var.ipv4_address_presto[count.index]
    type     = "ssh"
    user     = var.ssh_username
    password = var.ssh_password
    agent    = "false"
  }
}

# It is very important on your template image do that commands:
# sudo su
# nano /etc/sudoers
# deepsage ALL=(ALL) NOPASSWD: /home/deepsage/disk_resize.sh

resource "null_resource" "exec_scrypt" {
  count      = var.presto_instances_count
  depends_on = [null_resource.disk_resize_send_scrypt]
  provisioner "remote-exec" {
    on_failure = continue
    inline = [
      "cd",
      "chmod +x disk_resize.sh",
      "sudo ./disk_resize.sh",
    ]
  }
  triggers = {
    always_run = timestamp()
  }
  connection {
    host     = var.ipv4_address_presto[count.index]
    type     = "ssh"
    user     = var.ssh_username
    password = var.ssh_password
    agent    = "false"
  }

}

resource "null_resource" "exec_scrypt2" {
  count      = var.presto_instances_count
  depends_on = [null_resource.exec_scrypt]
  provisioner "remote-exec" {
    on_failure = continue
    inline = [
      "sleep 15",
      "cd",
      "chmod +x disk_resize.sh",
      "sudo ./disk_resize.sh",
    ]
  }
  triggers = {
    always_run = timestamp()
  }
  connection {
    host     = var.ipv4_address_presto[count.index]
    type     = "ssh"
    user     = var.ssh_username
    password = var.ssh_password
    agent    = "false"
  }

}
