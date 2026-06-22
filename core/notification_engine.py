import json
from datetime import datetime


def load_notifications():

    with open(
        "database/notifications.json",
        "r"
    ) as f:

        return json.load(f)


def save_notifications(notifications):

    with open(
        "database/notifications.json",
        "w"
    ) as f:

        json.dump(
            notifications,
            f,
            indent=4
        )


def send_notification(
    shipment_id,
    status
):

    notifications = load_notifications()

    notification = {

        "shipment_id": shipment_id,

        "message":
        f"Shipment {shipment_id} is currently {status}",

        "timestamp":
        datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    }

    notifications.append(notification)

    save_notifications(notifications)

    return notification