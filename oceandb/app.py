import oceandb
import oceandb.config
from oceandb.server.fastapi import FastAPI

settings = oceandb.config.Settings()
server = FastAPI(settings)
app = server.app()
