# README

## Setup

To build and run the Docker image using docker compose:

```sh
cd api_engineer/grid_singularity/
docker-compose up

# Generate and run Django migrations
docker-compose exec web python manage.py makemigrations grid_api
docker-compose exec web python manage.py migrate
```


## REST API endpoints

The docker container exposes port 8000. API requests can be therefore executed as in the following examples:

```sh
# POST: run (create) a new simulation
curl -H 'Accept: application/json' -X POST http://127.0.0.1:8000/api/simulations/
# GET: retrieve the last simulation
curl -H 'Accept: application/json' http://127.0.0.1:8000/api/simulations/last
# GET: retrieve a specific simulation (by its ID)
curl -H 'Accept: application/json' http://127.0.0.1:8000/api/simulations/1
# GET: retrieve the active power of the last simulation
curl -H 'Accept: application/json' http://127.0.0.1:8000/api/simulations/last_active_power
# GET: retrieve the reactive power of the last simulation
curl -H 'Accept: application/json' http://127.0.0.1:8000/api/simulations/last_reactive_power
```

## Websocket endpoints

The websocket can be reached at the URL `ws://127.0.0.1:8000/ws/simulations/`. For example, using `websocat`:

```sh
websocat ws://127.0.0.1:8000/ws/simulations/
```




## Notes

- The database is currently using the default Django settings (just a sqlite database). In a production environment, this should be better implemented as a separate dockerized service using, for example, PostgreSQL.
- In order to avoid the manual creation of `.env` files, we are currently defining env variables directly in the `docker-compose.yml` file (under `environment`). In general, using `.env` files would be the recommended practice.
