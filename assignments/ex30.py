people = 30
cars = 40
trucks = 150
if cars > people:
    print("we should take the cars.")


elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")

elif trucks < cars:
    print("May be we could take the trucks.")

else:
    print("we still can't decide.")

if people > trucks:
    print("All right, let's just take the trucks.")

else:
    print("Fine, let's stay home then.")