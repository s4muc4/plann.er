my_dict = {
    "hello": "world",
    "im": "here"
}

other_dict = {
    **my_dict, 
    "id": "my_id",
    "here": "my_dict"
}

print(other_dict)