Tested only with Ubuntu 22.04.


How to start:
0) set correct ip addresses in inventory/hosts.yaml

1)
```bash
ansible-playbook -i inventory 1_install_docker_docker_compose.playbook.yaml -K
```

2)
```bash
ansible-playbook -i inventory 2_copy_and_run_node_exporter.playbook.yaml -K
```