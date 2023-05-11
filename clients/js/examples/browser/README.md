## Demo in browser

Update your settings to add `localhost:3000` to `ocean_server_cors_allow_origins`.

For example:

```
client = oceandb.Client(
    Settings(ocean_api_impl="rest", ocean_server_host="localhost", ocean_server_http_port="8000", ocean_server_cors_allow_origins=["http://localhost:3000"])
)

```

1. `yarn dev`
2. visit `localhost:3000`
