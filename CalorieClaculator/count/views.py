from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import FoodItem
from django.contrib.auth.models import Group




def add_food(request):
    if request.method == 'POST':
        # Safely retrieve POST data
        name = request.POST.get('name', '').strip()
        calories = request.POST.get('calories', '').strip()

        # Check if fields are empty
        if not name or not calories:
            return render(request, 'add_food.html', {'error': 'Please fill in all fields.'})

        try:
            # Validate and convert calories to an integer
            calories = int(calories)
            if calories < 0:
                raise ValueError("Calories cannot be negative.")
        except ValueError:
            return render(request, 'add_food.html', {'error': 'Please enter a valid positive number for calories.'})

        # Create the new FoodItem if validation passes
        FoodItem.objects.create(name=name, calories=calories)
        return redirect('view_food')

    # If GET request, render the add_food template
    return render(request, 'add_food.html')

def view_food(request):
    # Get all food items
    food_items = FoodItem.objects.all()
    total_calories = sum(item.calories for item in food_items)

    return render(request, 'view_food.html', {
        'food_items': food_items,
        'total_calories': total_calories
    })


def remove_food(request, food_id):
    """
    Remove a specific food item by its ID.
    """
    food_item = get_object_or_404(FoodItem, id=food_id)
    food_item.delete()
    return redirect('view_food')

def reset_calories(request):
    """
    Remove all food items, resetting the calorie count.
    """
    FoodItem.objects.all().delete()
    return redirect('view_food')

def createfooditem(request):
    if request.method == 'POST':
            return redirect('/')
    return render(request,'createfooditem.html')
