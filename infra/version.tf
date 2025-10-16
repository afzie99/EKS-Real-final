terraform {
  backend "remote" {
    organization = "iac-local-test"

    workspaces {
      name = "EKS-Real-final"
    }
  }
}
