import maintenance_utils
import json
from maintenance_task_class import MaintenanceTask

maintenance_tasks = [
    MaintenanceTask(
        "N101G",
        "left landing gear will not engage",
        "HIGH",
        "OPEN"
    ),
    MaintenanceTask(
        "N202G",
        "coffee maker inop",
        "LOW",
        "OPEN"
    ),
    MaintenanceTask(
        "N303G",
        "de-ice inop",
        "HIGH",
        "CLOSED"
    ),
    MaintenanceTask(
        "N404G",
        "right anti-collision light dim",
        "MEDIUM",
        "OPEN"
    ),
    MaintenanceTask(
        "N505G",
        "co-pilot seat smells funny",
        "LOW",
        "CLOSED"
    )
]

with open("maintenance_tasks.json", "w") as maintenance_tasks_json:
    json.dump(
        [task.to_dict() for task in maintenance_tasks],
        maintenance_tasks_json,
        indent=4
    )

def format_task(aircraft_id, discrepancy, priority, status):
    clean_aircraft = aircraft_id.strip().upper()
    clean_discrepancy = discrepancy.strip().lower()
    clean_priority = priority.strip().upper()
    clean_status = status.strip().upper()
    decision = maintenance_utils.check_priority(clean_priority)
    return 'Aircraft: {aircraft} \nDiscrepancy: {discrepancy} \nPriority: {priority} \nStatus: {status} \nDecision: {decision} \n'.format(aircraft=clean_aircraft, discrepancy=clean_discrepancy, priority=clean_priority, status=clean_status, decision=decision)

assert maintenance_utils.check_priority('HIGH') == "Immediate action required"
assert maintenance_utils.check_priority('meDium   ') == 'Schedule maintenance soon'
assert maintenance_utils.check_priority('  LoW  ') == 'Routine maintenance'

print('ALL MAINTENANCE TASKS\n')

for task in maintenance_tasks:
    print(format_task(
        task.aircraft,
        task.discrepancy,
        task.priority,
        task.status
    ))

print('HIGH PRIORITY TASKS\n')

for task in maintenance_tasks:
    if task.priority == 'HIGH':
       print(format_task(
           task.aircraft,
           task.discrepancy,
           task.priority,
           task.status
        ))


open_count = 0
closed_count = 0

for task in maintenance_tasks:
    if task.status == 'OPEN':
        open_count += 1
    elif task.status == 'CLOSED':
        closed_count += 1

print('TASK STATUS TOTALS')
print('OPEN: ' + str(open_count))
print('CLOSED: ' + str(closed_count))


try:
    with open('maintenance_tasks.json', 'r') as maintenance_json:
        maintenance_data = json.load(maintenance_json)
        print(maintenance_data)
except FileNotFoundError:
    print('Maintenance data file not found')