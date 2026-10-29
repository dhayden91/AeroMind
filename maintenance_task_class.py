class MaintenanceTask:
    def __init__(self, aircraft: str, discrepancy: str, priority: str, status: str):
        if aircraft == "":
            raise ValueError("Invalid aircraft")

        if discrepancy == "":
            raise ValueError("Discrepancy cannot be empty")

        if priority not in ("LOW", "MEDIUM", "HIGH"):
            raise ValueError("Invalid priority")

        if status not in ("OPEN", "IN PROGRESS", "CLOSED"):
            raise ValueError("Invalid status")

        self.aircraft: str = aircraft
        self.discrepancy: str = discrepancy
        self.priority: str = priority
        self.status: str = status

        
        
    def change_priority(self, new_priority: str) -> None:
        if new_priority not in ("LOW", "MEDIUM", "HIGH"):
            raise ValueError("Invalid priority")

        self.priority = new_priority



    def change_status(self, new_status: str) -> None:
        if new_status not in ("OPEN", "IN PROGRESS", "CLOSED"):
            raise ValueError("Invalid status")

        self.status = new_status



    def close_task(self) -> None:
        self.status = "CLOSED"



    def to_dict(self) -> dict:
        return {
    "aircraft": self.aircraft,
    "discrepancy": self.discrepancy,
    "priority": self.priority,
    "status": self.status
}