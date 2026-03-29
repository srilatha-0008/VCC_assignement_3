gcloud compute instances create auto-scale-vm \
  --zone=asia-south1-a \
  --machine-type=e2-micro \
  --image-family=ubuntu-2204-lts-minimal \
  --image-project=ubuntu-os-cloud \
  --tags=http-server,https-server
