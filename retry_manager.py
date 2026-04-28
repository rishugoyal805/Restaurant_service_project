MAX_RETRY = 3


def should_retry(order):

    if "retry_count" not in order:

        order["retry_count"] = 0

    order["retry_count"] += 1

    return order["retry_count"] <= MAX_RETRY