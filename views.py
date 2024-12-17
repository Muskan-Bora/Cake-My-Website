from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from food.models import Item
from food.forms import ItemForm, TrendingForms, AllCategoriesForm, DesigningForms, DessertsForms
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from food.models import Trending, Designing, Desserts
from django.views import View
from food.models import Category, Flavour, Kids, Trend, Occasional, Design, Birthday, Anniversary, Dessert_Cake, AllCategories

# Create your views here.
# ---------------------------------------------------

# function based index view
# ---------------------------------------------------

def index(request):
    itemlist = Item.objects.all()
    trendings = Trending.objects.all()
    designing = Designing.objects.all()
    dessert = Desserts.objects.all()

    Context = {
        'itemlist':itemlist,
        'trendings':trendings,
        'designing':designing,
        'dessert':dessert
    }

    return render(request,'food/index.html', Context)

# def index(request):
#     trendings = Trending.objects.all()

#     Context = {
#         'trendings':trendings
#     }

#     return render(request,'food/index.html', Context)

# Class based index view
# ---------------------------------------------------

class IndexClassView(ListView):
    model=Item
    context_object_name = 'itemlist'
    template_name = 'food/index.html'

# function based detail view
# ---------------------------------------------------

def detail(request, item_id):

    item = Item.objects.get(id = item_id)

    context= {
        'item':item
    }

    return render (request, 'food/detail.html', context)

# Class based detail view
# ---------------------------------------------------

class FoodDetail(DetailView):
    model = Item
    context_object_name = 'item'
    template_name = 'food/detail.html'

# function based create_item view
# ---------------------------------------------------

def create_item(request):

    form = ItemForm(request.POST or None)

    if request.method == 'POST':
        form.instance.added_by = request.user.username
        form.save()
        return redirect('food:index')

    context = {
        'form':form
    }

    return render(request, 'food/item-form.html', context)

# class based create_item view
# ---------------------------------------------------

class CreateItem(CreateView):
    model = Item
    fields = ['rest_owner', 'prod_code', 'item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'food/item-form.html'
    success_url = reverse_lazy('food:index')

    def form_valid(self, form):
        form.instance.added_by = self.request.user.username
        return super().form_valid(form)

# function based update_item view
# ---------------------------------------------------

def update_item(request, id):

    item = Item.objects.get(pk=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    context = {
        'form':form
    }
    
    return render(request, 'food/item-form.html', context)

# function based delete_item view
# ---------------------------------------------------

def delete_item(request,id):

    item = Item.objects.get(pk=id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')

    context={
        'item':item
    }

    return render(request, 'food/item-delete.html', context)

# ---------------------------------------------------------------
class CategoryView(View):
    def get(self, request, val):
        
        Categories = Category.objects.filter(categories=val)
        
        return render(request, 'food/category.html', locals())
    
# ------------------------------------------------------------------
class flavourView(View):
    def get(self, request, val):
        
        flavours = Flavour.objects.filter(flavour=val)
        
        return render(request, 'food/flavour.html', locals())
    
# ------------------------------------------------------------------
class kidView(View):
    def get(self, request, val):
        
        kids = Kids.objects.filter(kids=val)
        
        return render(request, 'food/kids.html', locals())
    
# --------------------------------------------------------------------
class trendView(View):
    def get(self, request, val):
        
        trending = Trend.objects.filter(trending=val)
        
        return render(request, 'food/trend.html', locals())
    
# ----------------------------------------------------------------------
class occasionView(View):
    def get(self, request, val):
        
        occasion = Occasional.objects.filter(occasion=val)
        
        return render(request, 'food/occasional.html', locals())
    
# ------------------------------------------------------------------------
class designView(View):
    def get(self, request, val):
        
        designing = Design.objects.filter(designing=val)
        
        return render(request, 'food/design.html', locals())
    

# -------------------------------------------------------------------------
class birthdayView(View):
    def get(self, request, val):
        
        birthday = Birthday.objects.filter(birthday=val)
        
        return render(request, 'food/birthday.html', locals())
    
# --------------------------------------------------------------------------
class anniversaryView(View):
    def get(self, request, val):
        
        anniversary = Anniversary.objects.filter(anniversary=val)
        
        return render(request, 'food/anniversary.html', locals())
    
# ---------------------------------------------------------------------------
class dessertsView(View):
    def get(self, request, val):
        
        desserts = Dessert_Cake.objects.filter(dessert_cake=val)
        
        return render(request, 'food/dessert_cake.html', locals())
    
# ----------------------------------------------------------------------------
class detail_categories(View):
    def get(self, request, pk):

        details = Category.objects.get(category_code = pk)

        return render(request, 'food/category-detail.html', locals())
    
# ----------------------------------------------------------------------------
class detail_flavour(View):
    def get(self, request, pk):

        detail_flavour = Flavour.objects.get(flavour_code = pk)

        return render(request, 'food/flavour-detail.html', locals())
    
# -----------------------------------------------------------------------------
class detail_kids(View):
    def get(self, request, pk):

        detail_kids = Kids.objects.get(kids_code = pk)

        return render(request, 'food/kids-detail.html', locals())
    
# -----------------------------------------------------------------------------
class detail_trend(View):
    def get(self, request, pk):

        detail_trend = Trend.objects.get(tending_code = pk)

        return render(request, 'food/trend-detail.html', locals())
    
# -------------------------------------------------------------------------------
class detail_occasion(View):
    def get(self, request, pk):

        detail_occasion = Occasional.objects.get(occasion_code = pk)

        return render(request, 'food/occasion-detail.html', locals())
    
# -------------------------------------------------------------------------------
class detail_design(View):
    def get(self, request, pk):

        detail_design = Design.objects.get(designing_code = pk)

        return render(request, 'food/design-detail.html', locals())
    
# --------------------------------------------------------------------------------
class detail_birthday(View):
    def get(self, request, pk):

        detail_birthday = Birthday.objects.get(birthday_code = pk)

        return render(request, 'food/birthday-detail.html', locals())
    
# --------------------------------------------------------------------------------
class detail_dessert(View):
    def get(self, request, pk):

        detail_dessert = Dessert_Cake.objects.get(dc_code = pk)

        return render(request, 'food/dessert_cake-detail.html', locals())
    
# ---------------------------------------------------------------------------------
class detail_anniversary(View):
    def get(self, request, pk):

        detail_anniversary = Anniversary.objects.get(anniversary_code = pk)

        return render(request, 'food/anniversary-detail.html', locals())
    
# --------------------------------------------------------------------------------
def detail_trending(request, Trending_id):

    detailtrending = Trending.objects.get(id=Trending_id)

    context = {
        'detailtrending':detailtrending
    }

    return render(request, 'food/detail_trending.html', context)

# ----------------------------------------------------------------------------------
def detail_designing(request, Designing_id):
    detaildesigning = Designing.objects.get(id=Designing_id)

    context = {
        'detaildesigning':detaildesigning
    }

    return render(request, 'food/detail_designing.html', context)

# ------------------------------------------------------------------------------------
def detail_desserts(request, Desserts_id):
    detaildesserts = Desserts.objects.get(id=Desserts_id)

    context = {
        'detaildesserts':detaildesserts
    }

    return render(request, 'food/detail_desserts.html', context)

# ------------------------------------------------------------------------------------
def allcategories(request):

    allcategories = AllCategories.objects.all()

    context = {
        'allcategories':allcategories
    }

    return render(request, 'food/allcategories.html', context)

# -----------------------------------------------------------------------------------
def detail_allcategories(request, AllCategories_id):
    detailallcategories = AllCategories.objects.get(id=AllCategories_id)

    context = {
        'detailallcategories':detailallcategories
    }

    return render(request, 'food/detail_allcategories.html', context)

# ------------------------------------------------------------------------------------
def create_trending(request):

    form = TrendingForms(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    context = {
        'form':form
    }

    return render (request, 'food/addtrending-form.html', context)

# ----------------------------------------------------------------------------------
def delete_trending(request, id):

    trending = Trending.objects.get(pk=id)

    if request.method == 'POST':
        trending.delete()
        return redirect('food:index')

    context = {
        'trending':trending
    }

    return render(request, 'food/delete-trending.html', context)

# ------------------------------------------------------------------------

def create_allcat(request):

    form = AllCategoriesForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    context = {
        'form':form
    }

    return render (request, 'food/addallcat-form.html', context)

# --------------------------------------------------------------------------
def delete_allcat(request, id):

    allcat = AllCategories.objects.get(pk=id)

    if request.method == 'POST':
        allcat.delete()
        return redirect('food:index')

    context = {
        'allcat':allcat
    }

    return render(request, 'food/delete-allcat.html', context)

# ----------------------------------------------------------------------------
def update_allcat(request, id):

    updallcat = AllCategories.objects.get(pk=id)
    form = AllCategoriesForm(request.POST or None, instance=AllCategories)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    context = {
        'form':form
    }

    return render(request, 'food/addallcat-form.html', context)

# ------------------------------------------------------------------------
def create_designing(request):

    form = DesigningForms(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    context = {
        'form':form
    }

    return render (request, 'food/adddesigning-form.html', context)

# ---------------------------------------------------------------------
def delete_designing(request, id):

    designing = Designing.objects.get(pk=id)

    if request.method == 'POST':
        designing.delete()
        return redirect('food:index')

    context = {
        'designing':designing
    }

    return render(request, 'food/delete-designing.html', context)

# ------------------------------------------------------------------------
def create_desserts(request):

    form = DessertsForms(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    context = {
        'form':form
    }

    return render (request, 'food/adddesserts-form.html', context)

# -------------------------------------------------------------------------
def delete_desserts(request, id):

    dessert = Desserts.objects.get(pk=id)

    if request.method == 'POST':
        dessert.delete()
        return redirect('food:index')

    context = {
        'dessert':dessert
    }

    return render(request, 'food/delete-desserts.html', context)