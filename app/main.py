from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse
from app.database.mongo import client

app = FastAPI(
    title="horseAss",
    version="0.0.1",
    description="api for retrieving and posting horses to our database.",
)

@app.get('/')
def index():
    return RedirectResponse(app.docs_url)

@app.get('/testmongo')
def mongo_test():
    db = client.horseDatabase
    return db.list_collection_names()
