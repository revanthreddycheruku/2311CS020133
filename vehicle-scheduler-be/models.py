from pydantic import BaseModel

class Result(BaseModel):

    DepotID: int

    MechanicHours: int

    TotalImpact: int

    TotalDuration: int

    SelectedTaskIDs: list[str]