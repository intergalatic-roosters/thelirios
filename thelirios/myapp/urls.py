from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # Ingredients urls
    path("new-ingredient/", views.ingredient_registration, name="new-ingredient"),
    path("ingredients-list/", views.list_all_ingredients, name="ingredients-list"),
    path("ingredient-delete/<int:id>/", views.ingredient_delete, name="ingredient-delete"),
    path("ingredient-update/<int:id>/", views.ingredient_update, name="ingredient-update"),
    path("inventory/ingredients-list/", views.ingredient_inventory_list, name="inventory-ingredients-list"),
    path("inventory/add-ingredients", views.add_ingredients_to_inventory, name="add-ingredients"),
    path("inventory/ingredients-stock/", views.ingredient_stock, name="ingredients-stock"),

    # Recipes urls
    path("new-recipe", views.recipe_registration, name="new-recipe"),
    path("recipes-list", views.recipes_list, name="recipes-list"),
    path("recipe-delete/<int:id>", views.recipe_delete, name="recipe-delete"),
    path("recipe-update/<int:id>", views.recipe_update, name="recipe-update"),
    path('recipe/<recipe_id>', views.recipe_details, name='recipe-details'),
    path("inventory/recipes-list/", views.recipe_inventory_list, name="inventory-recipes-list"),
    path("inventory/add-recipes", views.add_recipes_to_inventory, name="add-recipes"),
    path("inventory/recipes-stock/", views.recipe_stock, name="recipes-stock"),   

    # Products urls
    path("new-product", views.product_registration, name="new-product"),
    path("products-list", views.list_all_products, name="products-list"),
    path("product-delete/<int:id>", views.product_delete, name="product-delete"),
    path("product-update/<int:id>", views.product_update, name="product-update"),
    path('product/<product_id>', views.product_details, name='product-details'),
    path("inventory/products-list/", views.product_inventory_list, name="inventory-products-list"),
    path("inventory/add-products", views.add_products_to_inventory, name="add-products"),
    path("inventory/sold-products", views.remove_products, name="remove-products"),
    path("inventory/products-stock/", views.product_stock, name="products-stock"),  
]
