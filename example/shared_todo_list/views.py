from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.template.response import TemplateResponse

from interactive.shortcuts import render_subview, render_pageview
from interactive import Layout

# Imports the Item class
from shared_todo_list.models import *
from django import template

register = template.Library()
layout_reg = Layout()


def render_list(request, context = {}):
    # id is required property that needs to be passed
    # so that render_X method can find the DOM element on 
    # the page later on.
    context['id'] = "todo-list"
    # el defaults to 'div'
    context['el'] = "ol"
    # optional value
    context['classname'] = "fancy-list"

    all_items = Item.objects.all()
    context['items']  = all_items

    return render_subview(request, 'shared-todo-list/list.html', context)

layout_reg.register_subview(render_list)

def render_item(request, item, context = {}):
    # item = Item.objects.get(pk=item_id)
    context['id'] = "todo-item-" + str(item.pk)
    context['el'] = "li"

    context['item'] = item

    return render_subview(request, 'shared-todo-list/item.html', context)

layout_reg.register_subview(render_item)


# Action for the default shared-todo-list/ route.
def home(request):
    # render takes: (1) the request,
    #               (2) the name of the view to generate, and
    #               (3) a dictionary of name-value pairs of data to be
    #                   available to the view.
    context = {}
    context['items'] = Item.objects.all()
    # context['render_list'] = render_list(request, context)[0]
    return render_pageview(request, 'shared-todo-list/index.html', context)



# Action for the shared-todo-list/add-item route.
def add_item(request):
    context = {}
    errors = []  # A list to record messages for any errors we encounter.

    # Adds the new item to the database if the request parameter is present
    if not 'item' in request.POST or not request.POST['item']:
	   errors.append('You must enter an item to add.')
    else:
	   new_item = Item(text=request.POST['item'])
	   new_item.save()

    context['errors'] = errors
    context['items'] = Item.objects.all()
    context['render_list'] = render_list(request, context)
    return render_pageview(request, 'shared-todo-list/index.html', context)
    
# Action for the shared-todo-list/delete-item route.
def delete_item(request, item_id):
    errors = []

    # Deletes the item if present in the todo-list database.
    try:
    	item_to_delete = Item.objects.get(id=item_id)
        item_to_delete.delete()
    except ObjectDoesNotExist:
	   errors.append('The item did not exist in the todo list.')

    items = Item.objects.all()
    context = {'items':items, 'errors':errors}
    context['render_list'] = render_list(request, context)
    return render(request, 'shared-todo-list/index.html', context)

