# Set does not support indexing/slicing
#insertion order is not preserved
#duplicates are not allowed (no failure)
#mathematical set operations can be performed
s1 =set([1,2,3,4,5])
s2 = set((1,2,3))
s3 = set({1: "a", 2 : "b"})
s1.add(100)
s1.add(1)  #no failure will be ignored
print(s1)
print(s2)
print(s3)
print(s1&s2&s3)
print(s1.union(s2).union(s3))
print(s1.symmetric_difference(s2))