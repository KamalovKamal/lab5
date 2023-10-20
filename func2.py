movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]


# task 1

# def top_film (name): 
#     for i in movies: 
#         if i['name'] == name: 
#             if float(i['imdb']) >  5.5: 
#                 print(i['name'],':',i['imdb']) 
#                 return True     
#     return False 
# print (top_film('We Two'))
# print (top_film('What is the name'))
# print (top_film('Exam'))


# task 2

# def topovie_filmi(name): 
#     for i in movies: 
#         if i['name'] == name: 
#             if float(i['imdb']) >  5.5: 
#                 print(i['name'],':',i['imdb']) 
#                 return True     
#     return False 
            
# def list(list):
#     list1 = []
#     for i in list: 
#         if topovie_filmi(i["name"]):
#             list1.append(i["name"])
#     return list1

# print(*list(movies))


# task 3

# def abs(category):
#     list1 = []
#     for i in movies: 
#         if i['category'] == category:
#             list1.append(i["name"])
#     return list1

# ashot=input()
# print(abs(ashot))


# task 4

# def averg(li):
#     sum = 0
#     for i in li:
#         sum += i['imdb']

#     return sum/li.__len__()
 
# print(averg(movies))


# task 5

# def cateaverg(category):
#     li2= []
#     for k in movies:
#         if k['name'] in cate(category):

#             li2.append(k)
    
#     return averg(li2)

# def cate(category):
#     li1 = []
#     for i in movies: 
#         if i['category'] == category:
#             li1.append(i["name"])
#     return li1

# def averg(li):
#     sum = 0
#     for i in li:
#         sum += i['imdb']

#     return sum/li.__len__()

# c= input()
# print(cateaverg(c))
    