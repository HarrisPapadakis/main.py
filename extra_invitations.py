#List of guest
guests = ["Michael Jordan" ,"Lebron James" ,"Scottie Pipen" ,"Steph Curry"]

#Adding new guests
guests.insert(0,"Mel Gibson")
guests.insert(2,"Lana Rhodes")
guests.append("Mia Khalifa")

#Notify all guests for adding  new guests
print("Great news!I found i bigger dinner table.Here 's the updated guest list:")
for guest in guests:
        print(f"{guest}, you are invited to dinner!")
