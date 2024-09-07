fruit={'apples','carrot','banana','raddish','sweet potato','peas'}
vegi={'carrot','raddish','peas','wheat','cauliflower'}
grain={'wheat','peas','millet','oats'}

#s1 is items common to all three sets
s1=fruit.intersection(vegi)
s1=s1.intersection(grain)
print("Items common to all 3 sets: ",s1)

# s2 is items not common to any of the three sets
s2=fruit.symmetric_difference(vegi)
s2=s2.symmetric_difference(grain)
print("Items not common to any of the three sets: ",s2)

# s3 items unique to only fruit
s3 = fruit.difference(vegi)
s3 = s3.difference(grain)
print("Items unique in fruit set: ",s3)
# s4 items unique to only grain
s4 = grain.difference(vegi)
s4 = s4.difference(fruit)
print("Items unique in grain set: ",s4)
# s3 items unique to only fruit
s5 = vegi.difference(fruit)
s5 = s5.difference(grain)
print("Items unique in vegi set: ",s5)




