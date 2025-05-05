terraform {
    required_providers {
        aws = {
            source  = "hashicorp/aws"
            version = "~> 4.0"
        }
    }

    required_version = ">= 1.3.0"
}
    

# s3 resources
resource "aws_s3_bucket" "mlops_bucket" {
    bucket = var.bucket_name

    tags = {
        Name        = "mlops_project"
        Environment = "prod"
    }
}


# ec2 resources
data "aws_ami" "ubuntu" {
  most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["099720109477"] # Canonical
}

# server instance
resource "aws_instance" "mlfloe_server" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"

  tags = {
    Name = "mlflow"
  }
}

# processsing instance
resource "aws_instance" "processing_data" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"

  tags = {
    Name = "data_processing"
  }
}