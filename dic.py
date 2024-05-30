# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# print(thisdict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# print(thisdict)



#Nasted Dic--------------------

course = {
  'php': {'duration':'3 months', 'fees': 15000},
 'Java': {'duration':'2 months', 'fees': 11000},
 'Python': {'duration':'4 months', 'fees': 15000},
 
}
print(course['php'] ['fees'])

for k,v in course.items():
  print(k,v['duration'], v['fees']) 




