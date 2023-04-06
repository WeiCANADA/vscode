'''
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

# make sure your solution is assigned to the answer variable so the tests can work!
answer =dict(zip(list1,list2))

print(answer)


person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
#answer = {thing[0]: thing[1] for thing in person}
answer = dict(person)
'''
#answer = { i:0 for i in 'aeiou'}
import charset_normalizer


answer = dict.fromkeys("aeiou", 0) 
answer = {i:chr(i) for i in range(65,91)}
print(answer)