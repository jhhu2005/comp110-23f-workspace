"""Practice with Dictionaries."""

#Constructing a dictionary
ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
print(ice_cream)

#Adding a key, value pair to a dictionary
ice_cream["mint"] = 3
print("After adding mint:")
print(ice_cream)

#Removing a key, value pair from a dictionary
ice_cream.pop("mint")
print("After removing mint:")
print(ice_cream)

#Accessing a value
print(f"There are {ice_cream['chocolate']} orders of chocolate")

#Adjusting a value
ice_cream["vanilla"] = 10
#ice_cream["vanilla"] += 2
print("After adjusting amount of vanilla:")
print(ice_cream)

#Getting the length of a dictionary
print(f"The number of key value pairs: {len(ice_cream)} in the dictionary")

#Checking if certain keys are in a dictionary
print("Is chocolate in ice_cream?")
print("chocolate" in ice_cream)
print("Is mint in ice_cream?")
print("mint" in ice_cream)

if "mint" in ice_cream:
    print(f"There are {ice_cream['mint']} orders of mint")
else: 
    print("There are no orders of mint")

if "chocolate" in ice_cream:
    print(f"There are {ice_cream['chocolate']} orders of chocolate")
else:
    print("There are no orders of chocolate")

#Iterating over keys in a dictionary with for loops
for key in ice_cream:
    # "<flavor> has <num_orders> orders"
    print(f"{key} has {ice_cream[key]} orders.")
    
