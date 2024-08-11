from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse


weekly_challenges = {
    "monday" : "Eat no meat for the entire day!",
    "tuesday" : "Walk for at least 20!",
    "wednesday" : "Learn django for at least 6 hours!",
    "thursday" : "Eat no meat for the entire day!",
    "friday" : "Walk for at least 20 minutes!",
    "saturday" : "Learn django for at least 6 hours!",
    "sunday" : None,
}


def index(request):
    days = list(weekly_challenges.keys())
    return render(request, "challenges/index.html", {
        "days" : days
    })


def weekly_challenge(request, day):
    try:
        challenge_text = weekly_challenges[day]
        return render(request, "challenges/challenge.html", {
            "text" : challenge_text,
            "day_name" : day
        })
    except:
        raise Http404()