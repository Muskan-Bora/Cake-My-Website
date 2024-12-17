from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from users.forms import RegisterForm, ProfForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from users.models import Profile, Cart
from food.models import Category, Flavour, Kids, Trend, Occasional, Design, Birthday, Anniversary, AllCategories, Item

# Create your views here.

def register(request):

    if request.method == 'POST':
        print(f"Username length: {len(request.POST['username'])}")
        # print(f"Form Errors: {form.errors}")  # Debugging form validation errors
        form = RegisterForm(request.POST)
        username = request.POST['username']
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request,
                'Welcome {}, your account has been successfully created. Now you may Login below'.format(username)
            )
            return redirect('login')
        else:
            print(f"Form Errors: {form.errors}")  # Debugging form validation errors
    else:
        form = RegisterForm()

    context={
        'form':form
    }

    return render(request, 'users/register.html', context)

def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if (username is '') or (username is None):
            username = User.objects.get(email=email)

        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.success(
                request,
                'Invalid Login, Please Try Again'.format(user)
            )
            return redirect('login')
        
        elif user.is_superuser:
            login(request,user)
            messages.success(
                request,
                'Welcome, A Superuser {}, you have logged in successfully'.format(user)
            )
            return redirect('food:index')    
        
        elif user is not None:
            login(request, user)
            messages.success(
                request,
                'Welcome {}, you have logged in successfully'.format(user)
            )
        return redirect('food:index')

    return render(request, 'users/login.html')

def logout_view(request):

    if request.method == 'POST':
        user = request.user.username
        logout(request)
        messages.success(
            request,
            '{}, you have been logged out successfully'.format(user)
        )
        return redirect('food:index')
    
    return render(request, 'users/logout.html')

def ProfilePage(request):
    prof = Profile.objects.get(user=request.user.id)

    if not request.user.is_authenticated:
        return redirect('login')
    
    context = {
        'prof':prof
    }

    return render (request, 'users/profile.html', context)

def ProfileForm(request, prof_id):
    prof = Profile.objects.get(id=prof_id)
    form = ProfForm(request.POST or None, request.FILES or None, instance=prof)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('food:index')

    context = {
        'form':form
    }

    return render(request, 'users/profform.html', context)

@login_required(login_url='users:register')
def add_to_cart(request):
    if request.method == 'POST':
        # Extract form data
        cake_id = request.POST.get('cake_id')
        net_weight = int(request.POST.get('net_weight'))
        quantity = int(request.POST.get('quantity', 1))
        cake_category = request.POST.get('cake_category')

        # Debugging: Print the value of cake_category
        print(f"Selected cake category: {cake_category}")  # Debugging

        # Map categories to models
        category_to_model = {
            'category': Category,
            'flavour': Flavour,
            'kids': Kids,
            'trend': Trend,
            'occasional': Occasional,
            'design': Design,
            'birthday': Birthday,
            'anniversary': Anniversary,
            'allcategories': AllCategories,
            'item_item':Item,
        }
        cake_model = category_to_model.get(cake_category)

        if not cake_model:
            # Invalid category; show an error message and redirect back
            messages.error(request, "Invalid category selected. Please try again.")
            return redirect(request.META.get('HTTP_REFERER', 'food:index'))

        # Fetch the cake object
        cake = get_object_or_404(cake_model, id=cake_id)

        # Generalized price determination logic
        price_field_map = {
            250: 'price_250gm',
            500: 'price_500gm',
            1000: 'price_1kg',
        }
        price_field = price_field_map.get(net_weight)

        if not price_field or not hasattr(cake, price_field):
            # Invalid weight or missing price field
            messages.error(request, "Invalid net weight or pricing unavailable. Please try again.")
            return redirect(request.META.get('HTTP_REFERER', 'food:index'))

        price = getattr(cake, price_field, None)

        if price is None:
            # Price is not set for this weight
            messages.error(request, "Price for the selected weight is not available. Please try again.")
            return redirect(request.META.get('HTTP_REFERER', 'food:index'))

        # Create or update the cart item
        cart_item, created = Cart.objects.get_or_create(
            user=request.user,
            cake_id=cake_id,
            cake_category=cake_category,
            net_weight=net_weight,
            defaults={'quantity': quantity, 'price': price}
        )

        if not created:
            # If the item already exists, update the quantity
            cart_item.quantity += quantity
            cart_item.price = price  # Update price
            cart_item.save()
            
        # Calculate the total cart item count for the user
        cart_count = Cart.objects.filter(user=request.user).count()

        # Show success message and redirect to the cart view
        messages.success(request, "Item added to cart successfully!")
        return redirect('users:view_cart')

    # If not a POST request, redirect to the home page
    return redirect('food:index')

    
@login_required
def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)

    # Debugging: Print the cart items
    print(f"Cart items: {cart_items}")  # Debugging line

    # Fetch detailed info for each cart item
    detailed_cart_items = []
    for item in cart_items:
        # Determine the model based on the category
        category_to_model = {
            'category': Category,
            'flavour': Flavour,
            'kids': Kids,
            'trend': Trend,
            'occasional': Occasional,
            'design': Design,
            'birthday': Birthday,
            'anniversary': Anniversary,
            'allcategories': AllCategories,
            'item_item':Item,
        }
        model = category_to_model.get(item.cake_category)

        if model:
            cake = model.objects.filter(id=item.cake_id).first()
            if cake:
                detailed_cart_items.append({
                    'id': item.id,
                    'name': getattr(cake, 'name', 'Unknown Cake'),
                    'image': getattr(cake, 'image', None),
                    'category': item.cake_category,
                    'net_weight': item.net_weight,
                    'quantity': item.quantity,
                    'price': item.price,
                    'total_price': item.total_price,  # Ensure this field exists in your Cart model
                    # 'cart_count':item.cart_count,
                })
            else:
                print(f"Could not find cake with id {item.cake_id} in model {model.__name__}")  # Debugging line
        else:
            print(f"Invalid category {item.cake_category} for cart item {item.id}")  # Debugging line

    # Calculate total price
    total_price = sum(item['total_price'] for item in detailed_cart_items)
    
    # Get the total cart count
    cart_count = Cart.objects.filter(user=request.user).count()


    # Debugging: Print the detailed cart items
    print(f"Detailed cart items: {detailed_cart_items}")  # Debugging line

    return render(request, "users/cart.html", {"cart_items": detailed_cart_items, "total_price": total_price,  "cart_count": cart_count})

@login_required
def update_cart_item(request, item_id):
    if request.method == 'POST':
        cart_item = get_object_or_404(Cart, id=item_id, user=request.user)
        new_quantity = int(request.POST.get('quantity', 1))
        cart_item.quantity = new_quantity
        cart_item.save()
        messages.success(request, "Cart item updated successfully.")
    return redirect('users:view_cart')

@login_required
def remove_cart_item(request, item_id):
    if request.method == 'POST':
        cart_item = get_object_or_404(Cart, id=item_id, user=request.user)
        cart_item.delete()
        messages.success(request, "Item removed from cart.")
    return redirect('users:view_cart')


# def add_to_cart(request):
#     if not request.user.is_authenticated:
#         return redirect('login')  # Redirect to login if not authenticated

#     category_id = request.GET.get('cat_id')
#     category = get_object_or_404(AllCategories, id=category_id)

#     # Add the item to the cart, or update the quantity if it already exists
#     cart_item, created = Cart.objects.get_or_create(user=request.user, category=category)

#     if not created:
#         # If the item already exists in the cart, just increase the quantity
#         cart_item.quantity += 1
#         cart_item.save()

#     return redirect('show_cart')  # Redirect to the cart page after adding the item

# # views.py
# def show_cart(request):
#     if not request.user.is_authenticated:
#         return redirect('login')  # Redirect to login if not authenticated

#     # Fetch the cart items for the authenticated user
#     cart_items = Cart.objects.filter(user=request.user)

#     # Initialize total amount and shipping cost
#     total_amount = 0
#     subtotal = 0
#     shipping_cost = 10

#     for item in cart_items:
#         # Calculate the total price for each item (price * quantity)
#         item.total_price = item.category.ac_price * item.quantity
#         subtotal += item.total_price  # Accumulate the subtotal

#     total_amount = subtotal + shipping_cost  # Calculate the total amount including shipping

#     # Pass the cart items, subtotal, shipping cost, and total amount to the template
#     return render(request, 'users/cart.html', {
#         'cart_items': cart_items,
#         'subtotal': subtotal,
#         'shipping_cost': shipping_cost,
#         'total_amount': total_amount,
#     })

# def remove_from_cart(request, item_id):
#     if not request.user.is_authenticated:
#         return redirect("login")  # Redirect to login if not authenticated

#     cart_item = get_object_or_404(Cart, id=item_id, user=request.user)
#     cart_item.delete()

#     return redirect('show_cart')  # Redirect to the cart page after removing the item