total_hours = int(input("Enter total hours : "))
total_abs_hours = int(input("Enter the total absent hours : "))

total_attended_hours = total_hours - total_abs_hours

percent_attended = ((total_attended_hours / total_hours) * 100)

percent_attended = round(percent_attended, 2)

print("Percent Attented : " + str(percent_attended))

ans = round((100 - percent_attended), 2)

print("Percent Absent : " + str(ans))