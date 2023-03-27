# SwapRouterAPI

### Enviroments
In `env.txt`:
- HTTP_NODE: HTTP Node URL (e.g. http://localhost:5000) or infura URL (e.g. https://mainnet.infura.io/v3/...)
- MONGO_URI: Mongo URI to connect in format mongodb://<user>:<password>@<host>:<port> (now host is docker network)

### Run for dev
Using Makefile:
```
make clean // clean all caches and venv
make setup // run and set up python venv
make dev   // run all linters and tests
```

### How to run?
From docker-compose:
```
docker-compose up -d
```
