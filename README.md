Simple example to try FastApi with Edgedb

To run the app first execute:
`docker-compose up` 

Then run migrations:
`docker-compose exec edgedb edgedb -I local_dev migration create` and `docker-compose exec edgedb edgedb -I local_dev migrate`

And open your browser http://localhost:8080/docs