provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_container_cluster" "primary" {
  name     = "echolite-cluster"
  location = var.region
  initial_node_count = 1

  node_config {
    machine_type = "e2-standard-2"
  }
}