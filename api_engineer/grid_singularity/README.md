# README


## REST API endpoints

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

The websocket can be reached at the URL `ws://127.0.0.1:8000/ws/simulations/`. For example, using `websocat` from console:

```sh
websocat ws://127.0.0.1:8000/ws/simulations/
```
