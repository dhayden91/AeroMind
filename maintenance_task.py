aircraft_identifier = "N666S"
discrepancy = "Left landing gear alert light inop"
priority = "LOW"
status_complete = True

if status_complete:
    decision = "Task complete"
elif priority == "HIGH":
    decision = "Immediate action required"
elif priority == "MEDIUM":
    decision = "Schedule maintenance soon"
else:
    decision = "Routine maintenance"

print("Aircraft: " + aircraft_identifier + "\n",
"Discrepancy: " + discrepancy + "\n",
"Priority: " + priority + "\n",
"Status Complete: " + str(status_complete) + "\n",
"Decision: " + decision)