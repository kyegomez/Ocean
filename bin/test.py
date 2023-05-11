# Sanity check script to ensure that the Ocean client can connect
# and is capable of recieving data.
import oceandb

# run in in-memory mode
ocean_api = oceandb.Client()
print(ocean_api.heartbeat())
