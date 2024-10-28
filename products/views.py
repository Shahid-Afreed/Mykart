from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    featured_products=Product.objects.order_by('priority')[:4]
    latest_products=Product.objects.order_by('-pk')[:4]
    context={
        'featured_products':featured_products,
        'latest_products':latest_products
    }
    return render(request,'index.html',context)



def list_products(request):
    sort_option = request.GET.get('sort', 'default')   
    # Get the current page, default to 1
    page = request.GET.get('page', 1)
    # Retrieve the product list
    product_list = Product.objects.all()  # Get all products
    # Apply sorting based on the selected option
    if sort_option == 'Price low to high':
        product_list = product_list.order_by('price')
    elif sort_option== 'Price high to low':
        product_list = product_list.order_by('-price') 
    else:
        product_list = product_list.order_by('priority')  

    # Paginate the sorted product list
    product_paginator = Paginator(product_list, 6)
    product_list = product_paginator.get_page(page)

    context = {
        'products': product_list,
        'sort_option': sort_option,  # Pass the sort option to the template if needed
    }
    return render(request, 'products.html', context)

    #PREVIOUS CODE
    # page=1
    # if request.GET:
    #     page=request.GET.get('page',1)
    # product_list=Product.objects.order_by('priority')

    # product_paginator=Paginator(product_list,6)
    # product_list=product_paginator.get_page(page)

    # context={'products':product_list}
    # return render(request,'products.html',context)



def detail_products(request,pk):
    product=Product.objects.get(pk=pk)
    context={'product':product}
    return render(request,'products_detail.html',context)