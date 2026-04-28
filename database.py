import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))

db = client["order_system"]

orders = db["orders"]

dlq_collection = db["dead_letter_queue"]


def save_order(order):

    orders.insert_one(order)


def load_keys():

    keys = []

    for doc in orders.find({}, {"idempotency_key": 1}):

        keys.append(doc["idempotency_key"])

    return keys


def save_dlq(order):

    dlq_collection.insert_one(order)