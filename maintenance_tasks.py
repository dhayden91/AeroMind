aircraft = ['N101G', 'N202G', 'N303G', 'N404G', 'N505G']

discrepancies = [
    'left landing gear will not engage',
    'coffee maker inop',
    'de-ice inop',
    'right anti-collision light dim',
    'co-pilot seat smells funny'
]

priorities = ['HIGH', 'LOW', 'HIGH', 'MEDIUM', 'LOW']
statuses = ['OPEN', 'OPEN', 'CLOSED', 'OPEN', 'CLOSED']

def format_task(aircraft_id, discrepancy, priority, status):
    clean_aircraft = aircraft_id.strip().upper()
    clean_discrepancy = discrepancy.strip().lower()
    clean_priority = priority.strip().upper()
    clean_status = status.strip().upper()
    decision = check_priority(clean_priority)
    return 'Aircraft: {aircraft} \nDiscrepancy: {discrepancy} \nPriority: {priority} \nStatus: {status} \nDecision: {decision} \n'.format(aircraft=clean_aircraft, discrepancy=clean_discrepancy, priority=clean_priority, status=clean_status, decision=decision)

def check_priority(priority):
    clean_priority = priority.strip().upper()
    if clean_priority == 'HIGH':
        return 'Immediate action required'
    elif clean_priority == 'MEDIUM':
        return 'Schedule maintenance soon'
    else:
        return 'Routine maintenance'

assert check_priority('HIGH') == "Immediate action required"
assert check_priority('meDium   ') == 'Schedule maintenance soon'
assert check_priority('  LoW  ') == 'Routine maintenance'



print('ALL MAINTENANCE TASKS\n')

for i in range(len(aircraft)):
    print(format_task(aircraft[i], discrepancies[i], priorities[i], statuses[i]))

print('HIGH PRIORITY TASKS\n')

for i in range(len(aircraft)):
    if priorities[i] == 'HIGH':
       print(format_task(aircraft[i], discrepancies[i], priorities[i], statuses[i]))


open_count = 0
closed_count = 0

for status in statuses:
    if status == 'OPEN':
        open_count += 1
    elif status == 'CLOSED':
        closed_count += 1

print('TASK STATUS TOTALS')
print('OPEN: ' + str(open_count))
print('CLOSED: ' + str(closed_count))