from django.http import HttpResponse
from django.shortcuts import render
import operator


def about(request):
	return render(request, 'about.html')

def home(request):
	return render(request, 'home.html')

def count(request):
	fulltext = request.GET['fulltext']
	wordlist = fulltext.split()

	worddict = {}

	for word in wordlist:
		if word in worddict:
			#Increase
			worddict[word] += 1
		else:
			#add to dict
			worddict[word] = 1

	# Sorts by words, alphabetically, ascending
	sortedwords = sorted(worddict.items(), key=operator.itemgetter(0))
	# Sorts by counts, descending
	# sortedwords = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)

	return render(request, 'count.html', {'fulltext':fulltext, 'wc':len(wordlist), 'sortedwords':sortedwords})

