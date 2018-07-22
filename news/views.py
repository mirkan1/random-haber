from django.shortcuts import render
import random
from .models import NewsItem
from faker import Faker

def index(request):
	fk = Faker()
	name = [fk.name() for i in range(1000)]
	job = [fk.job() for i in range(1000)]
	city = [fk.city() for i in range(1000)]
	currency_name = [fk.currency_name() for i in range(1000)]

	my_dict = {
		'sentences': [1,2,3,4,5],
		'sentence_one' : "%s got arrested in %s " % (random.choice(name), random.choice(city)),
		'sentence_two' : "%s have %d %s and did nothing wrong" % (random.choice(name), random.randint(1, 100000000), random.choice(currency_name)),
		'sentence_three' : "Acording to Swedish scientists the people in %s lives at least %d more years than the people in %s" % (random.choice(city), random.randint(2,100), random.choice(city)),
		'sentence_four': "Old person %s was working so hard as %s to keep living his magnificant life but died on %d in %s" % (random.choice(name), random.choice(job), random.randint(70,150), random.choice(city)),
		'sentence_five': '%s killed %s because for lunch money' % (random.choice(name), random.choice(name)),
		'random' : random.randint(0,4)
	}

	return render(request, "news/index.html", context=(my_dict))
