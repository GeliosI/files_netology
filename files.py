import os

def get_cook_book_by_file(file_path):
    cook_book = {}

    with open(file_path) as file:
        for cook in file:
            ingredient_count = int(file.readline())
            cook_book[cook.strip()] = []

            while ingredient_count:
                ingredient_name, quantity, measure = file.readline().strip().split(" | ")
                cook_book[cook.strip()].append({'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure})
                ingredient_count-= 1

            file.readline()

    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    file_path = os.path.join(os.getcwd(), 'recipes.txt')
    cook_book = get_cook_book_by_file(file_path)
    ingredients = {}

    for dish in dishes:
        for cook in cook_book[dish]:
            if cook['ingredient_name'] in ingredients:
                ingredients[cook['ingredient_name']]['quantity']+= cook['quantity'] * person_count
            else:
                ingredients[cook['ingredient_name']] = {'measure': cook['measure'], 'quantity': cook['quantity'] * person_count}

    return(ingredients)

def merge_files_into_one(*files):
    number_of_lines = []
    file_dict = {}

    for file in files:
        file_path = os.path.join(os.getcwd(), file)
        with open(file_path) as source_file:
            lines = source_file.readlines()
            number_of_lines.append(len(lines))
            file_dict[len(lines)] = [file, lines]

    number_of_lines.sort()

    with open('result.txt', 'at') as result:
        for i in number_of_lines:
            result.write(f'{file_dict[i][0]}\n{i}\n{"".join(file_dict[i][1])}\n')

def main():
    # задача №1
    print(get_cook_book_by_file(os.path.join(os.getcwd(), 'recipes.txt')))

    # задача №2
    print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 3))

    # задача №3
    merge_files_into_one('1.txt', '2.txt', '3.txt')

main()