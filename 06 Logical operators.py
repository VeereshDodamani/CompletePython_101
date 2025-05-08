## Logical opertator : evaluate multiple comditions(or, and, not)
#                      or = atleast 1 condition must be true
#                      and = both the conditions must be true
#                      not = invert the condition (not True, not False)

temp = 25
is_raining = False

if temp>35 or temp<0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("Outdoor event not cancelled")


is_sunny = True
if temp>=28 and is_sunny:
    print("IT IS SUNNY OUT")
else:
        print("IT IS NOT SUNNY OUT")


is_sunny = True
if temp>=28 and not is_sunny:
    print("IT IS CLOUDY")
else:
        print("IT IS NOT CLOUDY")
