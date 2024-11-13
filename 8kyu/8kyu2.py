def enough(cap, on, wait):
    total_people = on + wait
    if total_people <= cap:
        return 0
    else:
        return total_people - cap

print(enough(10, 5, 5))
print(enough(100, 60, 50))
