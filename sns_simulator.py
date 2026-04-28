def publish_notification(order):

    print("\n SNS Notification")

    print("Restaurant:", order["restaurant_id"])

    print("Order:", order["order_id"])

    print("Amount:", order["amount"])