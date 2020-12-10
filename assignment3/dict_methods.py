#different functions of dictionary in python.
vehicles_list={"car":500000,"bike":100000,"truck":1500000,"lorry":200000};
get=vehicles_list.get('car');
print(f"getting vehicles_list:{get}"); #getting the value.
update=vehicles_list.update({"jcp":600000});
print(f"updating vehicles_list:{vehicles_list}"); #append the value at last position.
items=vehicles_list.items();
print(f"items of vehicles_list:{items}"); #It gives tuple representation.
values=vehicles_list.values();
print(f"values of vehicle_list:{values}"); #it gives the values of the vehicles_list.
popitems=vehicles_list.popitem();
print(f"popitems of vehicles_list:{vehicles_list}"); #it deletes the last value.