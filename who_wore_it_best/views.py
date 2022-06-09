from django.views.generic import CreateView
from django.shortcuts import render

from who_wore_it_best.models import PeopleVote
from who_wore_it_best.forms import VoteForm

# Create your views here.
class VoteView(CreateView):
    model = PeopleVote
    form_class = VoteForm
    template_name = 'who_wore_it_best/vote.html'

class ThanksView(CreateView):
    model = PeopleVote
    form_class = VoteForm
    template_name = 'who_wore_it_best/thank_you.html'

def getvotes(request):
    people_and_votes = PeopleVote.objects.all()

    rajesh_votes = 0
    naresh_votes = 0

    for people_and_vote in people_and_votes:
        if people_and_vote.vote == "Rajesh" :
            rajesh_votes+=1  
        elif people_and_vote.vote == "Naresh" :
            naresh_votes+=1

    top_gun = "Rajesh" if rajesh_votes >= naresh_votes else "Naresh"

    election_result = {'rajesh_votes':rajesh_votes, 'naresh_votes':naresh_votes, 'top_gun':top_gun}

    return render(request, 'who_wore_it_best/getvotes.html', {'election_result': election_result, 'people_and_votes': people_and_votes})


# class GetVotesView(ListView):
#     model = PeopleVote
#     template_name = 'who_wore_it_best/getvotes.html'

# def vote(request):
#     people = PeopleVote.objects.all().values('name')

#     people_list = [person['name'] for person in people]
    
#     return render(request, 'who_wore_it_best/vote.html',{'people_list': people_list})


