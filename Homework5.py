import os
import sys
current = os.getcwd()
file_name = 'recipes.txt'
full_path = os.path.join(current, file_name)
recipes = []
recipes2 = []
with open(full_path, 'rt', encoding='utf8') as file:
    for dish in file:
        dish_name = dish.strip()
        cook_book = {dish_name: []}
        persons = file.readline()
        for i in range(int(persons)):
            emp = file.readline()
            ingredient_name, quantity, measure = emp.strip().split(' | ')
            cook_book[dish_name].append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        blank_line = file.readline()
        recipes.append(cook_book)
        recipes2.extend(cook_book)
#print(recipes)
#print(recipes2)

shop_list = []
def get_shop_list_by_dishes(dishes, person_count):
  if dishes in recipes2:
    for loc in recipes:
      for key, value in loc.items():
        print(value)
        for ingredient in value:
          print
          if ingredient in shop_list:
            shop_list['ingredient_name']['quantity'] += ['quantity'] * person_count
          else:
            shop_list += {'measure': value[0:]['measure'],
                          'quantity': (value[0:]['quantity'] * person_count)}
  else:
    print('Ошибка')
  print(shop_list)

get_shop_list_by_dishes(dishes = 'Омлет', person_count= 2)

def sort_files():
    text1 = {}
    for file in os.listdir('test'):
        with open(os.path.join('test', file), encoding='utf-8') as f:
            text = f.readlines()
            text_ = "".join(text)
            len_ = len(text)
            text1[file] = (f'{len_} \n{text_} \n')
    text2 = {}
    for a in sorted(text1, key=text1.get):
        text2[a] = text1[a]
    text_dict = {}
    for key, value in text2.items():
        with open('home3.txt', 'a', encoding='utf-8') as f:
            f.writelines(f'{key} \n{value} \n')
#sort_files()