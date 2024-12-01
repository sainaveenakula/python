from google.cloud import compute_v1

def sample_list():
    # Create a client
    client = compute_v1.InstancesClient()

    # Initialize request argument(s)
    request = compute_v1.ListInstancesRequest(
        project="pu-ecom-apollo-fed-prd-ap-0",
        zone="asia-northeast1-c",
    )

    # Make the request
    page_result = client.list(request=request)
    for page in page_result:
      print(page.name)
      print(page.shielded_instance_config.enable_integrity_monitoring)
      print("***************************")
    # Handle the response
#    for response in page_result:
 #       print(response)

sample_list()
