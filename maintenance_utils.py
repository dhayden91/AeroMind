def check_priority(priority):
    clean_priority = priority.strip().upper()
    if clean_priority == 'HIGH':
        return 'Immediate action required'
    elif clean_priority == 'MEDIUM':
        return 'Schedule maintenance soon'
    else:
        return 'Routine maintenance'