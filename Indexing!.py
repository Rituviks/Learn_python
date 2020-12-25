Class_list = ["vikash","Divya","Ritu","Ragini","Anu","Anand","Swati"]
print(Class_list)
item_to_found = "Anu"
found_at = "None"

for index in range(len(Class_list)):
    if Class_list[index ] == "Anu":
        found_at = index
        break
print("item at {}".format(found_at))