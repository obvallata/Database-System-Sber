import json
import random

def generate_product(id):
    """Генерирует данные для одного продукта."""
    product_names = ["shampoo", "conditioner", "soap", "toothpaste", "body wash", "hand sanitizer", "lotion", "razor", "deodorant", "mouthwash"]
    cost = round(random.uniform(1, 10), 2)  # Стоимость случайным образом в диапазоне от 1 до 10
    amount = random.randint(10, 1000)       # Количество случайным образом в диапазоне от 10 до 1000
    return {
        "id": id,
        "product_name": random.choice(product_names),
        "cost": cost,
        "amount": amount
    }

def generate_products(num_products):
    """Генерирует данные для нескольких продуктов."""
    return [generate_product(i) for i in range(num_products)]

def save_to_json(data, filename):
    """Сохраняет данные в файл в формате JSON."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    num_products = int(input("Введите количество продуктов: "))
    products_data = generate_products(num_products)
    filename = 'products.json'
    save_to_json(products_data, filename)
    print(f"Файл {filename} успешно сохранен.")

if __name__ == "__main__":
    main()
