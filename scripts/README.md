# Hybrid Auto Scaling Project

## Project Objective
This project monitors CPU and memory usage in a local VM. When usage exceeds 75%, the system simulates scaling to Google Cloud Platform (GCP) by creating a new VM instance.

## Files Included

- autoscale.py → Python monitoring script
- prometheus.yml → Prometheus configuration
- install_dependencies.sh → Installs required packages
- install_nginx.sh → Installs NGINX web server
- gcp_vm_create.sh → Creates a GCP VM instance

## Tools Used

- Linux Mint VM
- Python
- Prometheus
- Node Exporter
- GCP VM
- NGINX

## Threshold
CPU Threshold = 75%
Memory Threshold = 75%

## Sample Output

When CPU or memory usage crosses 75%, the script prints:

Threshold exceeded! Trigger scaling to GCP.
Creating new GCP VM...
