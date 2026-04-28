from queue import Queue

order_queue = Queue()


def send_message(order):

    order_queue.put(order)


def receive_message():

    return order_queue.get()