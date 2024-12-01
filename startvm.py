from google.cloud import compute_v1

def sample_list():
    # Create a client
    client = compute_v1.InstancesClient()

    # Initialize request argument(s)
    request = compute_v1.ListInstancesRequest(
        project="",
        zone="asia-northeast1-b",
    )

    # Make the request
    page_result = client.list(request=request)
    for page in page_result:
        print(page.name)
        print("______________________________________________________________")
        if page.name == "instance-20241201-081720":
            print("Compute VM is Existed")
            if page.status == "RUNNING":
                print("Compute VM is already Running.....")
            else:
                # Initialize request argument(s)
                request = compute_v1.StartInstanceRequest(
                    instance="instance-20241201-081720",
                    project="pu-ecom-apollo-fed-dev-ap-0",
                    zone="asia-northeast1-b",
                )

                # Make the request
                response = client.start(request=request)
                print(response)
        else:
            print("Compute VM is Not Found")
            
                
     
sample_list()

