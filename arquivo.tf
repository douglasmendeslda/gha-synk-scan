provider "aws" {
  region = "us-west-2" # Substitua pela região desejada
}

resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0" # AMI do Amazon Linux 2 (substitua conforme necessário)
  instance_type = "t2.micro"              # Tipo de instância (substitua conforme necessário)

  tags = {
    Name = "Terraform-EC2-Instance"
  }
}
