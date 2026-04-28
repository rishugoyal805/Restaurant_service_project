from database import save_dlq


def send_to_dlq(order):

    print("Sending order to Dead Letter Queue")

    save_dlq(order)