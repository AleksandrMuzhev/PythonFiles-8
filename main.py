def read_book(filename):
    copy_book = {}

    with open("recipes.txt", "r", encoding="utf-8") as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break
            copy_book[dish_name] = []
            ingredient_count = int(file.readline().strip())
            for _ in range(ingredient_count):
                ingredient_line = file.readline().strip().split(" | ")
                ingredient_name = ingredient_line[0]
                quantity = ingredient_line[1]
                measure = ingredient_line[2]
                copy_book[dish_name].append({
                    "ingredient_name": ingredient_name,
                    "quantity": quantity,
                    "measure": measure
                })
            file.readline()
        return copy_book


copy_book = read_book("recipes.txt")
print(f'Задание 1: \n copy_book = {copy_book}')


def get_shop_list_by_dishes(dishes, person_count):
    ingredients = {}
    for dish in dishes:
        if dish in copy_book:
            for ingredient in copy_book[dish]:
                ingredient_name = ingredient["ingredient_name"]
                quantity = int(ingredient["quantity"]) * person_count
                measure = ingredient["measure"]
                if ingredient_name in ingredients:
                    ingredients[ingredient_name]["quantity"] += quantity
                else:
                    ingredients[ingredient_name] = {"quantity": quantity, "measure": measure}
        else:
            print(f'Блюдо {dish} отсутствует в книге рецептов.')

    return ingredients


read_book("recipes.txt")
dishes = ['Запеченный картофель', 'Омлет']
person = 2
shop_list = get_shop_list_by_dishes(dishes, person)
print(f'Задание 2: \n {shop_list}')
