terraform {
  backend "gcs" {
    bucket  = "husne_mybucket"
    prefix  = "qa/hello-world"
    project = "fuchicorp-project-315576"
  }
}
