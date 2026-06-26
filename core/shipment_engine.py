import json
from datetime import datetime

SHIPMENT_STAGES = [
    "Packed",
    "Dispatched",
    "In Transit",
    "Out For Delivery",
    "Delivered" 
]


def load_shipments():
    with open("database/shipments.json", "r") as f:
        return json.load(f)


def save_shipments(shipments):
    with open("database/shipments.json", "w") as f:
        json.dump(shipments, f, indent=4)


def create_shipment(
    shipment_id,
    customer,
    destination,
    agent
):
    shipments = load_shipments()

    shipment = {
        "shipment_id": shipment_id,
        "customer": customer,
        "destination": destination,
        "agent": agent,
        "status": "Packed",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    shipments.append(shipment)

    save_shipments(shipments)

    return shipment


def move_to_next_stage(shipment_id):

    shipments = load_shipments()

    for shipment in shipments:

        current_status = shipment["status"]

        if shipment["shipment_id"] == shipment_id:

            current_index = SHIPMENT_STAGES.index(current_status)

            if current_index < len(SHIPMENT_STAGES) - 1:

                shipment["status"] = SHIPMENT_STAGES[
                    current_index + 1
                ]

    save_shipments(shipments)


def get_shipment(shipment_id):

    shipments = load_shipments()

    for shipment in shipments:

        if shipment["shipment_id"] == shipment_id:
            return shipment

    return None
