vegetables = ["tomatoes","potatoes","onions"]
vegetables.remove("onions")
vegetables.append("carrots")
if "cucumber" not in vegetables:
    vegetables.append("cucumbers")
    vegetables.sort()
print("Updated Vegetable Inventory: ",vegetables)
if "carrots" in vegetables:
    print("Carrots are already in the list.")
if "cucumbers" in vegetables:
    print("Cucumbers are already in the list.")

