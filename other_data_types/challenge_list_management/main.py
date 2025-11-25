meat =["Ham", 3.99, 50, "Sliced"]
Cheese =["Cheddar",5.49,100,"Sharp"]
condiment =["Mustard",1.99,75,"Spicy"]

deli_dept= [meat,Cheese,condiment]
if "Ham" in meat and meat[2] < 100:
    meat[2] = 100

print("Initial Deli list: ",deli_dept)

seasonal_meat = ["Turkey",4.50,100,"Sliced"]
deli_dept.append(seasonal_meat)
deli_dept.remove(condiment)
deli_dept.sort()

print("Updated Deli list: ",deli_dept)



