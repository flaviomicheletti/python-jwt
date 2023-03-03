# JWT with two micro services

To complete the testing process, it is necessary to launch two microservices, 
specifically the ones located in the flask01 and flask02 folders. Following 
this, it is advised to initiate a request to the /login endpoint and record the 
resulting token. Finally, to confirm the functionality of the secure-data 
endpoint, it is recommended to execute a request to the aforementioned endpoint 
using the previously obtained token via the curl command. Additionally, a 
recommended test to perform is to modify the token, rendering it invalid, and 
assess the security of the endpoint.


## step by step

1. You need to start the two microservices, both the one in the `flask01` folder 
   and the one in the `flask02` folder.

2. Then you make a request to `/login` and make a note of the token.

3. The final test is to make a request (as curl below) to the `/secure-data` 
   endpoint using the token obtained earlier.

    curl --request GET \
      --url http://localhost:5001/secure-data \
      --header 'authorization: Bearer <your-token>'

4. Another interesting test is to change the token (so that it becomes invalid)
   and test if the endpoint is indeed secure.

