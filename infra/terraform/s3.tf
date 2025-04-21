
resource "aws_s3_bucket" "mlops_bucket" {
    bucket = "bucket-mlops-assets-prod"

    tags = {
        Name        = "mlops project"
        Environment = "prod"
    }
}