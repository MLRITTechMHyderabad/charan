li=[1,5,8,9,7,5,8,6,2,1,1,6,4]
frequency={}
for num in li:
    frequency[num]=frequency.get(num,0)+1
   #print(f"After processing {num}: {frequency}")  # Printing after each iteration 
print("frequency of numbers: ",frequency)