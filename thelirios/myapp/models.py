from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=60, null=False)
    amount_yield = models.FloatField(max_length=6)
    cooking_time = models.IntegerField(help_text="minutes")
    description = models.TextField(max_length=300, blank=True, null=True)
    cost = models.FloatField(max_length=6)
    ingredients = models.ManyToManyField('Ingredient', through='RecipeIngredient')

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=60, null=False)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return f"{self.recipe.name} - {self.ingredient.name} - {self.quantity}"


class Product(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(max_length=300, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    recipes = models.ManyToManyField("Recipe")

    def __str__(self):
        return self.name
