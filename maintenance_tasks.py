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


print('ALL MAINTENANCE TASKS\n')

for i in range(len(aircraft)):
    print(
        'Aircraft: ' + aircraft[i] +
        '\nDiscrepancy: ' + discrepancies[i] +
        '\nPriority: ' + priorities[i] +
        '\nStatus: ' + statuses[i] +
        '\n'
    )


print('HIGH PRIORITY TASKS\n')

for i in range(len(aircraft)):
    if priorities[i] == 'HIGH':
        print(
            'Aircraft: ' + aircraft[i] +
            '\nDiscrepancy: ' + discrepancies[i] +
            '\nStatus: ' + statuses[i] +
            '\n'
        )


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