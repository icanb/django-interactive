from django import template
from interactive.base import subviews


register = template.Library()

def tuple_without(original_tuple, ind_remove):
    new_tuple = []
    for i, s in enumerate(list(original_tuple)):
        if not i == ind_remove:
            new_tuple.append(s)
    return tuple(new_tuple)


@register.simple_tag(takes_context=True)
def subview(context, *args, **kwargs):

	# get subview_name
	subview_name = args[0]

	# remove subview_name from the args
	new_args = tuple_without(args, 0)


	# get and call f with the new arguments and current
	# context
	f = subviews[subview_name]
	return f("custom_tag", *new_args, context=context)
