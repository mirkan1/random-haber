from django import template
import random

register = template.Library()


@register.filter(name='sex') #ONE WAY TO DO IT
def sex(value):
	""" cuts if alkll valuues of arg from the string"""
	return random.choice(value)


#register.filter("sex", sex) #ONE WAY TO DO IT