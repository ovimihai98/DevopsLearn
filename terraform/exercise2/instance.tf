resource "aws_instance" "terra-inst" {
  ami                    = var.AMIS[var.REGION]
  instance_type          = "t2.micro"
  availability_zone      = var.ZONE1
  key_name               = "terraform-key"
  vpc_security_group_ids = ["sg-0c6da1c6f07044d54"]
  tags = {
    Name    = "Terraform-Instance"
    Project = "Terra"
  }
}