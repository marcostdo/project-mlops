terraform {
    required_providers {
        aws = {
            source  = "hashicorp/aws"
            version = "~> 4.0"
        }
    }

    required_version = ">= 1.3.0"
}
    


resource "aws_s3_bucket" "mlops_bucket" {
    bucket = var.bucket_name

    tags = {
        Name        = "mlops project"
        Environment = "prod"
    }
}