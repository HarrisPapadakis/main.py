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


#New list of guests
guests = ["Mel Gibson" ,"Michael Jordan" ,"Lebron James" ,"Lana Rhodes" ,"Scottie Pipen" ,"Steph Curry"]

#inform about th change
print ("Unfortunately, i can only invite two people to dinner.! ")

#Remove guests until only two remain
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry ,{removed_guest} i can't invite you to the dinner!")

#Notify the rest of the guests
for guest in guests:
    print(f"{guest} ,you are still invited to the dinner!")


#clear the list and confirm
guests.clear()
print(f"Final guest list: {guests}" )
