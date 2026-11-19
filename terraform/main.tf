
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 4.0"
    }
  }
}

provider "docker" {}

resource "docker_container" "portfolio" {
  name  = "portfolio-terraform"
  image = "cloud-portfolio:v1"

  ports {
    internal = 5000
    external = 5001
    ip       = "127.0.0.1"
  }
}
