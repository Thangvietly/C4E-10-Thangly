
def extract_even(l):
    even_list=[x for x in l if x%2==0]
    return(even_list)
####7
l=[1, 4, 5, -1, 10]
print("even list",extract_even(l))


###8

even_list = extract_even([1, 2, 5, -10, 9, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
