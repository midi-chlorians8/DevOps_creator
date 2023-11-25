module "presto-coordinator" {
  source           = ".././modules/presto-instance"
  vsphere_user     = var.vsphere_user
  vsphere_password = var.vsphere_password
  vsphere_server   = var.vsphere_server

  vsphere_datacenter      = var.vsphere_common.vsphere_datacenter
  vsphere_compute_cluster = var.vsphere_common.vsphere_compute_cluster
  vsphere_datastore       = var.vsphere_common.vsphere_datastore
  vsphere_resource_pool   = var.vsphere_common.vsphere_resource_pool
  vsphere_network         = var.vsphere_common.vsphere_network

  vsphere_environment = var.vsphere_environment

  presto_name = "coordinator"

  presto_instances_count = 1
  ipv4_address_presto    = ["10.123.66.103"]

  num_cpus         = "4"
  memory_instance  = var.memory_instance
  disk_size_presto = "21"

  ssh_username = var.ssh_username
  ssh_password = var.ssh_password

  vsphere_ipv4_gateway    = var.vsphere_ipv4_gateway
  dns_server_list         = var.dns_server_list
  ipv4_netmask            = var.ipv4_netmask
  presto_cluster_template = var.presto_cluster_template

}

module "presto-resource-manager" {
  source           = ".././modules/presto-instance"
  vsphere_user     = var.vsphere_user
  vsphere_password = var.vsphere_password
  vsphere_server   = var.vsphere_server

  vsphere_datacenter      = var.vsphere_common.vsphere_datacenter
  vsphere_compute_cluster = var.vsphere_common.vsphere_compute_cluster
  vsphere_datastore       = var.vsphere_common.vsphere_datastore
  vsphere_resource_pool   = var.vsphere_common.vsphere_resource_pool
  vsphere_network         = var.vsphere_common.vsphere_network

  vsphere_environment = var.vsphere_environment

  presto_name = "resource-manager"

  presto_instances_count = 1
  ipv4_address_presto    = ["10.123.66.104"]

  num_cpus         = "2"
  memory_instance  = "4096"
  disk_size_presto = "21"

  ssh_username = var.ssh_username
  ssh_password = var.ssh_password

  vsphere_ipv4_gateway = var.vsphere_ipv4_gateway
  dns_server_list      = var.dns_server_list
  ipv4_netmask         = var.ipv4_netmask

  presto_cluster_template = var.presto_cluster_template

}

module "presto-worker" {
  source           = ".././modules/presto-instance"
  vsphere_user     = var.vsphere_user
  vsphere_password = var.vsphere_password
  vsphere_server   = var.vsphere_server

  vsphere_datacenter      = var.vsphere_common.vsphere_datacenter
  vsphere_compute_cluster = var.vsphere_common.vsphere_compute_cluster
  vsphere_datastore       = var.vsphere_common.vsphere_datastore
  vsphere_resource_pool   = var.vsphere_common.vsphere_resource_pool
  vsphere_network         = var.vsphere_common.vsphere_network

  vsphere_environment = var.vsphere_environment

  presto_name = "worker"

  presto_instances_count = 4
  ipv4_address_presto    = ["10.123.66.105", "10.123.66.106", "10.123.66.107", "10.123.66.108"]

  num_cpus         = "4"
  memory_instance  = var.memory_instance
  disk_size_presto = var.disk_size

  ssh_username = var.ssh_username
  ssh_password = var.ssh_password

  vsphere_ipv4_gateway = var.vsphere_ipv4_gateway
  dns_server_list      = var.dns_server_list
  ipv4_netmask         = var.ipv4_netmask

  presto_cluster_template = var.presto_cluster_template

}
