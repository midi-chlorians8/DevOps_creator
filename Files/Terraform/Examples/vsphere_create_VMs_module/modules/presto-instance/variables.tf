variable "vsphere_user" {}
variable "vsphere_password" {
  sensitive = true
}
variable "vsphere_server" {}




variable "vsphere_datacenter" {
  type = string
}

variable "vsphere_datastore" {
  type = string
}

variable "vsphere_compute_cluster" {
  type = string
}

variable "vsphere_network" {
  type = string
}

variable "vsphere_resource_pool" {
  type = string
}




variable "vsphere_environment" {
  type = string
}

variable "vsphere_ipv4_gateway" {
  type = string
}

variable "dns_server_list" {
  type = list(string)
}

variable "domain" {
  default = "vn.local"
  type    = string
}

variable "clone_timeout_total" {
  description = "minutes"
  default     = "10"
  type        = string
}


variable "ipv4_netmask" {
  type = string
}

variable "disk_size_presto" {
  type = string
}

variable "memory_instance" {
  type = string
}

variable "num_cpus" {
  type = string
}

variable "presto_instances_count" {
  type = string
}

variable "ipv4_address_presto" {
  type = list(string)
}

variable "presto_cluster_template" {
  type = string
}

variable "presto_name" {
  type = string
}

variable "ssh_username" {
  type = string
}

variable "ssh_password" {
  type      = string
  sensitive = true
}
