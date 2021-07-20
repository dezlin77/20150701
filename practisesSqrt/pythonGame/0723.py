
# Python function to print permutations of a given list 
def permutation(list): 
  
    # If lst is empty then there are no permutations 
    if len(list) == 0: 
        return [] 
  
    # If there is only one element in lst then, only 
    # one permuatation is possible 
    if len(list) == 1: 
        return [list] 
  
    # Find the permutations for lst if there are 
    # more than 1 characters 
  
    l = [] # empty list that will store current permutation 
  
    # Iterate the input(lst) and calculate the permutation 
    for i in range(len(list)): 
       m = list[i] 
  
       # Extract lst[i] or m from the list.  remLst is 
       # remaining list 
       remLst = list[:i] + list[i+1:] 
  
       # Generating all permutations where m is first 
       # element 
       for p in permutation(remLst): 
           l.append([m] + p) 
    return l 
  
  
# Driver program to test above function 
#data = list('hiho')
data =["hi", "how", "are", "you"]
for p in permutation(data): 
    print(p)
