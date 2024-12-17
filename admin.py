from django.contrib import admin
from food.models import Item
from food.models import Trending
from food.models import Designing
from food.models import Desserts
from food.models import Category
from food.models import Flavour
from food.models import Kids
from food.models import Trend
from food.models import Occasional
from food.models import Design
from food.models import Birthday
from food.models import Anniversary
from food.models import Dessert_Cake
from food.models import AllCategories

# Register your models here.

admin.site.register(Item)
admin.site.register(Trending)
admin.site.register(Designing)
admin.site.register(Desserts)
admin.site.register(Category)
admin.site.register(Flavour)
admin.site.register(Kids)
admin.site.register(Trend)
admin.site.register(Occasional)
admin.site.register(Design)
admin.site.register(Birthday)
admin.site.register(Anniversary)
admin.site.register(Dessert_Cake)
admin.site.register(AllCategories)