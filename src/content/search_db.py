from .models import Ingredients, Dishes, DishType, Gallery, Reservation

query = Dishes.objects.all()
gallery = Gallery.objects.all()

dishes_ft = query.filter(featured=True)
count = [dishes_ft[x:x+3] for x in range(0, len(dishes_ft),3)] #Split array each n number
count_all = [query[x:x+2] for x in range(0, len(query),2)]

breakfast = query.filter(dish_type__name='breakfast')
count_breakfast = [breakfast[x:x+2] for x in range(0, len(breakfast),2)]

lunch = query.filter(dish_type__name='lunch')
count_lunch = [lunch[x:x+2] for x in range(0, len(lunch),2)]

dinner = query.filter(dish_type__name='dinner')
count_dinner = [dinner[x:x+2] for x in range(0, len(dinner),2)]

drink = query.filter(dish_type__name='drink')
count_drink = [drink[x:x+2] for x in range(0, len(drink),2)]

party = query.filter(dish_type__name='party')
count_party = [party[x:x+2] for x in range(0, len(party),2)]

coffee = query.filter(dish_type__name='coffee')
count_coffee = [coffee[x:x+2] for x in range(0, len(coffee),2)]

dessert = query.filter(dish_type__name='dessert')
juice = query.filter(dish_type__name='juice')
hard = query.filter(dish_type__name='hard')
soft = query.filter(dish_type__name='soft')