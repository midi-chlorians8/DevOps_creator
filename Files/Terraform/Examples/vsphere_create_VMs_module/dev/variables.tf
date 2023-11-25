variable "vsphere_user" {}
variable "vsphere_password" {
  sensitive = true
}
variable "vsphere_server" {}

variable "vsphere_environment" {
  default = "dev"
  type    = string
}

variable "vsphere_common" {
  description = "vSphere configuration object"
  type = object({
    vsphere_datacenter      = string
    vsphere_compute_cluster = string
    vsphere_datastore       = string
    vsphere_resource_pool   = string
    vsphere_network         = string
  })
  default = {
    vsphere_datacenter      = "YOUR_DATA"
    vsphere_compute_cluster = "YOUR_DATA"
    vsphere_datastore       = "YOUR_DATA"
    vsphere_resource_pool   = "YOUR_DATA"
    vsphere_network         = "YOUR_DATA"
  }
}


variable "memory_instance" {
  default = "8192"
  type    = string
}

variable "disk_size" {
  default = "180"
  type    = string
}

variable "num_cpus_worker" {
  default = "4"
  type    = string
}



variable "ssh_username" {
  type = string
}

variable "ssh_password" {
  type      = string
  sensitive = true
}




variable "vsphere_ipv4_gateway" {
  default = "YOUR_DATA"
  type    = string
}
variable "dns_server_list" {
  default = ["YOUR_DATA", "YOUR_DATA"]
  type    = list(string)
}
variable "presto_cluster_template" {
  default = "prestodb-ubuntu-22-04-template-v2"
  type    = string
}

variable "ipv4_netmask" {
  default = "24"
  type    = string
}
