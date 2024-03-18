#dictionaries
#data is stored in key value pairs
#ie key:value
cardata={
    "model":"mercedes",
    "brand":"C200",
    "YOM":2022
}
print(cardata["brand"])#accessing values in a dictionary we use the key
cardata["sunroof"]="available"#adding data to a dictionary
print(cardata)

cardata["brand"]="s200" #modifying