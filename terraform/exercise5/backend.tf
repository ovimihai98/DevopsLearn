terraform {
  backend "s3" {
    bucket = "terra-state-dove-20"
    key    = "terraform/backend"
    region = "us-east-1"
  }
}