from sqs_simulator import receive_message
from sns_simulator import publish_notification
from retry_manager import should_retry
from dlq import send_to_dlq


def start_worker():

    print("Worker started")

    while True:

        order = receive_message()

        try:

            if order["amount"] < 0:

                raise Exception("Invalid order")

            publish_notification(order)

        except Exception as e:

            print("Processing failed:", e)

            if should_retry(order):

                print("Retrying order")

                from sqs_simulator import send_message
                send_message(order)

            else:

                send_to_dlq(order)