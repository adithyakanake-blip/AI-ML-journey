#list &tuple

fruits =["apple","banana","mango","grapes","blue berry"]
print(fruits[1])

#kiwi is added at the end of the list

fruits.append("kiwi")
fruits.insert(2,"strawberry")
fruits.remove("blue berry")
print("list:")
print("fruits:",fruits)
#list slicing 
print("available fruits:",fruits[0:3])


#tuple
print("tuple:") 

sec_A =(12,23,34,45,56,67,78)
sec_B =(98,76,65,54,43,23,45)

print("SEc_A=",sec_A)
print("SEc_B=",sec_B)

combine =sec_A +sec_B
print(combine)

print("min&max of sec_A")

print(min(sec_A))
print(max(sec_A))

print("min&max of sec_B")

print(min(sec_B))
print(max(sec_B))

#avg of both sec_A & sec_B

print( "avg:",sum(combine)/len(combine))







