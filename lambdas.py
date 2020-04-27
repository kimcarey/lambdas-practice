"""
Exercise #1: Given the function below, convert to lambda function
def f(x): return x + 5
print(f(2))
"""
f = lambda x: x + 5
print(f(2))


# Exercise #2: Given the function below, convert to lambda function
#
# def strip_spaces(str):
#   return ''.join(str.split(' '))

strip_spaces1 = lambda str: ''.join(str.split(' '))
print(strip_spaces1('Monty Pythons Flying Circus'))


# Exercise #3: Given the function below, convert to lambda function
# def join_list_no_duplicates(list_a,list_b):
#    return list(set(list_a + list_b))
list_a = [1,2,3,4]
list_b = [3,4,5,6,7]

join_list_no_duplicates = lambda list_a, list_b: list(set(list_a + list_b))
print(join_list_no_duplicates(list_a,list_b))


# Exercise #4: Complete the function so it returns a function
def create_quad_func(a,b,c):
    '''return function f(x) = ax^2 + bx + c'''
    return lambda x: a * x**2 + b * x + c
f = create_quad_func(2,4,6)
g = create_quad_func(1,2,3)
print(f(2))
print(g(2))


# Exercise 5: Sort by number, not lexicographically
signups = ['MPF104', 'MPF20', 'MPF2', 'MPF17', 'MPF3', 'MPF45']
print(sorted(signups, key= lambda id: int(id[3:])))


# Exercise 6: Sort by score using lambda
class Player:
   def __init__(self, name, score):
       self.name = name
       self.score =  score

Eric = Player('Eric', 116700)
John = Player('John', 24327)
Terry = Player('Terry', 150000)
player_list = [Eric, John, Terry]

# sort method, sort from highest to lowest score with reverse = True
player_list.sort(key= lambda player: player.score, reverse= True)
print([player.name for player in player_list])