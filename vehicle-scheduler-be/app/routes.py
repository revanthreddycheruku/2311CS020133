from fastapi import APIRouter

from app.api_service import get_depots, get_vehicles
from app.scheduler import knapsack

router = APIRouter()


@router.get("/schedule")
def schedule():

    depots = get_depots()
    vehicles = get_vehicles()

    results = []

    for depot in depots:

        capacity = depot["MechanicHours"]

        selected = knapsack(
            vehicles,
            capacity
        )

        results.append({

            "DepotID": depot["ID"],

            "MechanicHours": capacity,

            "TotalImpact": sum(x["Impact"] for x in selected),

            "TotalDuration": sum(x["Duration"] for x in selected),

            "SelectedTaskIDs": [
                x["TaskID"]
                for x in selected
            ]

        })

    return results