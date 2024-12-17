from django.urls import path, include
from food import views

app_name = 'food'

urlpatterns = [

    # function based index view
    # ---------------------------------------------------
    path('home/', views.index, name='index'),

    # function based detail view
    # ---------------------------------------------------
    # path('detail/<int:item_id>/', views.detail, name='detail'),

    # class based index view
    # ---------------------------------------------------
    path('detail/<int:pk>/', views.FoodDetail.as_view(), name='detail'),

    # function based create_item view
    # ---------------------------------------------------
    # path('add/', views.create_item, name='create_item'),

    # class based create_item view
    # ---------------------------------------------------
    path('add/', views.CreateItem.as_view(), name='create_item'),

    # function based update_item view
    # ---------------------------------------------------
    path('update/<int:id>', views.update_item, name='update_item'),

    # function based delete_item view
    # ---------------------------------------------------
    path('delete/<int:id>', views.delete_item, name='delete_item'),

    # ------------------------------------------------------
    path('category/<slug:val>', views.CategoryView.as_view(), name='category'),

    # ------------------------------------------------------
    path('flavour/<slug:val>', views.flavourView.as_view(), name='flavour'),

    # ------------------------------------------------------
    path('kid/<slug:val>', views.kidView.as_view(), name='kid'),

    # ---------------------------------------------------------
    path('trend/<slug:val>', views.trendView.as_view(), name='trend'),

    # ----------------------------------------------------------
    path('occasion/<slug:val>', views.occasionView.as_view(), name='occasion'),

    # -----------------------------------------------------------
    path('design/<slug:val>', views.designView.as_view(), name='design'),

    # ------------------------------------------------------------
    path('birthday/<slug:val>', views.birthdayView.as_view(), name='birthday'),

    # ------------------------------------------------------------
    path('anniversary/<slug:val>', views.anniversaryView.as_view(), name='anniversary'),

    # -------------------------------------------------------------
    path('desserts/<slug:val>', views.dessertsView.as_view(), name='desserts'),

    # -------------------------------------------------------------
    path('detail_categories/<int:pk>/', views.detail_categories.as_view(), name='detail_categories'),

    # -------------------------------------------------------------
    path('detail_flavour/<int:pk>/', views.detail_flavour.as_view(), name='detail_flavour'),

    # --------------------------------------------------------------
    path('detail_kids/<int:pk>/', views.detail_kids.as_view(), name='detail_kids'),

    # ---------------------------------------------------------------
    path('detail_trend/<int:pk>/', views.detail_trend.as_view(), name='detail_trend'),

    # ---------------------------------------------------------------
    path('detail_occasion/<int:pk>/', views.detail_occasion.as_view(), name='detail_occasion'),

    # ---------------------------------------------------------------
    path('detail_design/<int:pk>/', views.detail_design.as_view(), name='detail_design'),

    # ----------------------------------------------------------------
    path('detail_birthday/<int:pk>/', views.detail_birthday.as_view(), name='detail_birthday'),

    # -----------------------------------------------------------------
    path('detail_dessert/<int:pk>/', views.detail_dessert.as_view(), name='detail_dessert'),

    # ------------------------------------------------------------------
    path('detail_anniversary/<int:pk>/', views.detail_anniversary.as_view(), name='detail_anniversary'),

    # -------------------------------------------------------------------
    path('detail_trending/<int:Trending_id>/', views.detail_trending, name='detail_trending'),

    # --------------------------------------------------------------------
    path('detail_designing/<int:Designing_id>/', views.detail_designing, name='detail_designing'),

    # --------------------------------------------------------------------
    path('detail_desserts/<int:Desserts_id>/', views.detail_desserts, name='detail_desserts'),

    # ---------------------------------------------------------------------
    path('allcategories/', views.allcategories, name='allcategories'),

    # ----------------------------------------------------------------------
    path('detail_allcategories/<int:AllCategories_id>/', views.detail_allcategories, name='detail_allcategories'),

    # -----------------------------------------------------------------------
    path('addtrending/', views.create_trending, name='create_trending'),

    # ------------------------------------------------------------------------
    path('deletetrending/<int:id>/', views.delete_trending, name='delete_trending'),

    # ------------------------------------------------------------------------
    path('addallcat/', views.create_allcat, name='create_allcat'),

    # ------------------------------------------------------------------------
    path('deleteallcat/<int:id>/', views.delete_allcat, name='delete_allcat'),

    # -------------------------------------------------------------------------
    path('updateallcat/<int:id>/', views.update_allcat, name='update_allcat'),

    # -------------------------------------------------------------------------
    path('adddesigning/', views.create_designing, name='create_designing'),

    # -------------------------------------------------------------------------
    path('deletedesigning/<int:id>/', views.delete_designing, name='delete_designing'),

    # -------------------------------------------------------------------------
    path('adddesserts/', views.create_desserts, name='create_desserts'),

    # --------------------------------------------------------------------------
    path('deletedesserts/<int:id>/', views.delete_desserts, name='delete_desserts'),
]