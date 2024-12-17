from django import forms
from food.models import Item
from food.models import Trending
from food.models import AllCategories
from food.models import Designing
from food.models import Desserts

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['rest_owner', 'prod_code', 'item_name', 'item_desc', 'item_price', 'item_image']

class TrendingForms(forms.ModelForm):
    class Meta:
        model = Trending
        fields = ['trend_code', 'trend_name', 'trend_image', 'trend_type']

class AllCategoriesForm(forms.ModelForm):
    class Meta:
        model = AllCategories
        fields = ['ac_code', 'ac_name', 'ac_desc', 'ac_price', 'ac_image']

class DesigningForms(forms.ModelForm):
    class Meta:
        model = Designing
        fields = ['design_code', 'design_name', 'design_image', 'design_type']

class DessertsForms(forms.ModelForm):
    class Meta:
        model = Desserts
        fields = ['dessert_code', 'dessert_name', 'dessert_image', 'dessert_type']

