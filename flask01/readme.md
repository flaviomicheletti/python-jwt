# flask-jwt-extended

https://flask-jwt-extended.readthedocs.io/en/stable/

    curl --request POST \
      --url http://localhost:5000/login \
      --header 'content-type: application/json' \
      --data '{"username": "john", "password": "1234"}'


    curl --request GET \
      --url http://localhost:5000/protected \
      --header 'authorization: Bearer <access_token>'



