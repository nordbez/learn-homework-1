from pprint import pprint
"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
xxx = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
def main(xxx):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    sum_phone,avg_phone = [],[]
    tmp1 = 0
    tmp2 = 0
    summa_all = 0
    avg_all = 0
    len_element = 0

    for i in xxx:
        tmp1 = sum(i['items_sold'])
        sum_phone.append(tmp1)
        tmp2 = (sum(i['items_sold']) / len(i['items_sold']))
        avg_phone.append(tmp2)
        len_element += len(i['items_sold'])

    summa_all = sum(sum_phone) 
    avg_all = summa_all / len_element
    print("Суммарное количесво продаж для каждого товара")  
    pprint(sum_phone)
    print("Среднее количество продаж для каждого товара")
    pprint(avg_phone)
    print(f'Общее количество телефонов {summa_all}')
    print(f'Среднее количество продаж всех товаров: {avg_all}')







    
if __name__ == "__main__":
    main(xxx)
