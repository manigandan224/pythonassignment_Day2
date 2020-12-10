#different functions of the list object in python.
names_list=["manigandan","lokesh","yamini","uday","jagan"];
names_list.insert(1,'mani'); #using insert function.
print(f"insert function:{names_list}");
print(f"count function:{names_list.count('mani')}"); #count function.
pop=names_list.pop(0);
print(f"pop function:{names_list}"); #pop function.
append=names_list.append('mani');
print(f"append function:{names_list}"); #append function.
reverse=names_list.reverse();
print(f"reverse function:{names_list}"); #reverse function.
