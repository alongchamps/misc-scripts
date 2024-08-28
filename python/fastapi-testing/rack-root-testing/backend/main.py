# Import necessary modules and classes
from fastapi import FastAPI, APIRouter
from fastapi.responses import HTMLResponse
from .database import ItemResponse
from .item import create_item, read_all_items, read_item, delete_item

# FastAPI app instance
app = FastAPI()

# setup all the routes for / and /items
router = APIRouter()
router.add_api_route("/", read_all_items, methods=['GET'], response_class=HTMLResponse)
# router.add_api_route("/", read_all_items, methods=['GET'],response_model=list[ItemResponse])
router.add_api_route("/items/", read_all_items, methods=['GET'], response_model=list[ItemResponse])
router.add_api_route("/items/", create_item, methods=['POST'], response_model=ItemResponse)
router.add_api_route("/items/{item_id:int}", read_item, methods=['GET'], response_model=ItemResponse)
router.add_api_route("/items/{item_id:int}", delete_item, methods=['DELETE'])

app.include_router(router)
