from django.shortcuts import redirect, render
from .models import Order, Product
#from django.db.models import Count

def root(request):
    return redirect('/amadon')

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request, p_id):
    if request.method == 'POST':
        id_product = Product.objects.get(id=p_id)
        print(id_product.price)
        
        #### data from form ####
        quantity_from_form = int(request.POST["quantity"])
        price_from_form = id_product.price
        #price_from_form = float(request.POST["price"])
        total_charge = quantity_from_form * price_from_form
        print("Charging credit card...")

        ### add form data into database #######
        order = Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
        order.selected_items.add(id_product)
        return redirect('/amadon/checkout')
    else:
        return redirect('/amadon')

def bought(request):
    total_spent = 0
    total_orders = Order.objects.all()
    for one_order in total_orders:
        total_spent += one_order.total_price
    context = {
        'order': Order.objects.last(),
        'total_orders': total_orders,
        #'total_spent': Order.objects.annotate(Sum('total_price'))
        'total_spent': total_spent
    }

    return render(request, "store/checkout.html", context)