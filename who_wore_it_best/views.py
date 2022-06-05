from django.shortcuts import render

# Create your views here.
def vote(request):
    return render(request, 'who_wore_it_best/vote.html')

def getvotes(request):
    return render(request, 'who_wore_it_best/getvotes.html')
