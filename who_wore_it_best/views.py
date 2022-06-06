from django.shortcuts import render
from who_wore_it_best.models import PeopleVote

# Create your views here.
def vote(request):
    return render(request, 'who_wore_it_best/vote.html')

def getvotes(request):
    people_and_votes = PeopleVote.objects.all()

    rajesh_votes = 0
    naresh_votes = 0

    for people_and_vote in people_and_votes:
        if people_and_vote.vote == "Rajesh" :
            rajesh_votes+=1  
        elif people_and_vote.vote == "Naresh" :
            naresh_votes+=1

    election_result = {'rajesh_votes':rajesh_votes, 'naresh_votes':naresh_votes}

    return render(request, 'who_wore_it_best/getvotes.html', {'election_result': election_result, 'people_and_votes': people_and_votes})
