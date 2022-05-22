arr = [3,-4,7,2,23]
for i in range(len(arr)):
   mini = i
   for j in range(i+1, len(arr)):
      if arr[mini] > arr[j]:
         mini = j
   #swap
   arr[i], arr[mini] = arr[mini], arr[i]
# main
for i in range(len(arr)):
   print(arr[i])