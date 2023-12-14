provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "intro" {
  ami                    = "ami-0230bd60aa48260c6"
  instance_type          = "t2.micro"
  availability_zone      = "us-east-1a"
  key_name               = "terraform-key"
  vpc_security_group_ids = ["sg-0c6da1c6f07044d54"]
  tags = {
    Name    = "Terraform-Instance"
    Project = "Terra"
  }
}