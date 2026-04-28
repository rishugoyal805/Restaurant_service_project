from fastapi import FastAPI, HTTPException
import threading

from database import save_order, load_keys
from database import dlq_collection
from cache import exists, save, cache
from sqs_simulator import send_message
from worker import start_worker

app = FastAPI()


@app.get("/dlq")
def view_dlq():

    data = list(dlq_collection.find({}, {"_id": 0}))

    return {
        "failed_messages": data
    }
    
@app.on_event("startup")
def startup():

    keys = load_keys()

    for k in keys:

        cache.add(k)

    print("Cache rebuilt")

    threading.Thread(target=start_worker, daemon=True).start()


@app.post("/payment/webhook")

def webhook(order: dict):

    key = order["idempotency_key"]

    if exists(key):

        raise HTTPException(409, "Duplicate request")

    save_order(order)

    save(key)

    send_message(order)

    return {"status": "Order Accepted"}