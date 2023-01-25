import peewee
from models import Category, Product

def post_category(category_name):
    try:
        category = Category(name=category_name)
        category.save()
        print('Saved!!!')
    except peewee.IntegrityError:
        print('такая катергория уже существует')

def get_category():
    categories = Category.select()
    for cat in categories:
        print(f'{cat.id}) {cat.name} -- {cat.created_at}')

def delete(category_id):
    try:
        category = Category.get(id=category_id)
        category.delete_instance()
        print('категория удалена')
        get_category()
    except peewee.DoesNotExist:
        print('категории с таким id нет')

def update_category(category_id, new_name):
    category = Category.get(id=category_id)
    category.name = new_name
    category.save()
    print('категория обновлена')
    get_category()
    

def detail_category(id_category):
    try:
        category = Category.get(id=id_category)
        print(f'{category.id}\n{category.name}\n{category.created_at}')
        for i in category.products:
            print(f'{i.name} -- {i.price} -- {i.amount}')
    except peewee.DoesNotExist:
        print('нет такой категории')

def post_product(name, price, amount, category):
    try:
        product = Product(name=name, price=price, amount=amount, category=category)
        product.save()
        print(f'{product.name} -- {product.price} -- {product.amount} -- {product.category}')
    except peewee.IntegrityError:
        print("такой категории не существует")

def get_products():
    product = Product.select()
    for prod in product:
        print(f'{prod.id} -- {prod.name} -- {prod.amount} -- {prod.category.name} -- {prod.category.created_at}')

def get_product_by_name(name):
    product = Product.select().where(Product.name==name)
    for i in product:
        print(i.name, i.price)