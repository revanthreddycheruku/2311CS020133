from fastapi import FastAPI

from services.api_service import get_depots
from services.api_service import get_vehicles
from services.scheduler import knapsack

app = FastAPI()


@app.get("/schedule")
async def schedule():

    depots = await get_depots()

    vehicles = await get_vehicles()

    results = []

    for depot in depots:

        capacity = depot["MechanicHours"]

        solution = knapsack(
            vehicles,
            capacity
        )

        total_duration = sum(
            t["Duration"] for t in solution["SelectedTasks"]
        )

        results.append({

            "DepotID": depot["ID"],

            "MechanicHours": capacity,

            "TotalImpact": solution["TotalImpact"],

            "TotalDuration": total_duration,

            "SelectedTaskIDs": [
                x["TaskID"]
                for x in solution["SelectedTasks"]
            ]

        })

    return results