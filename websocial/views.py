from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django import forms
from datetime import datetime
from .models import User, Status
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

# Create your views here.
def home(request):
    return HttpResponse(render(request, 'websocial/index.html'))

def _timeline_entries(user):
    followed_users = user.get_followees()
    followed_statuses = Status.objects.filter(user__in=followed_users)
    own_statuses = user.status_set.all()
    return (followed_statuses | own_statuses)[:100]

@login_required(login_url="/admin/login/")
def timeline(request, user_id):
    user = User.objects.get(pk=int(user_id))
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            status = user.status_set.create(text=text, pub_date=datetime.now())
            status.save()
            return HttpResponseRedirect(request.path)

    else:
        form = StatusForm()

    title = "%s: Home" % user.name
    entries = _timeline_entries(user)
    return HttpResponse(render(request, 'websocial/timeline.html', {
        'title': title, 
        'entries': entries, 
        'user_id': user.id, 
        'status_form': form,
        'poll_url': '/user/%d/timeline/json/' % user.id}))

@login_required(login_url="/admin/login/")
def timeline_json(request, user_id):
    user = User.objects.get(pk=int(user_id))
    entries = _timeline_entries(user)
    entries_dicts = [{
            'id': entry.id, 
            'text': entry.text, 
            'url': entry.url, 
            'user_name': entry.user.name, 
            'user_id': entry.user.id} 
        for entry in entries]
    return JsonResponse(entries_dicts, safe=False)


def user_statuses_json(request, user_id):
    user = User.objects.get(pk=int(user_id))
    entries = user.status_set.all()[:100]
    entries_dicts = [{
            'id': entry.id, 
            'text': entry.text, 
            'url': entry.url, 
            'user_name': entry.user.name, 
            'user_id': entry.user.id} 
        for entry in entries]
    return JsonResponse(entries_dicts, safe=False)

   

from django.views.decorators.csrf import csrf_exempt

@login_required(login_url="/admin/login/")
@require_http_methods(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def user_following_user(request, follower_user_id, followee_user_id):
    user = User.objects.get(pk=int(follower_user_id))
    followee = User.objects.get(pk=int(followee_user_id))
    status = 200
    if request.method == 'PUT':
        user.following.add(followee)
        user.save()
    elif request.method == 'DELETE':
        user.following.remove(followee)
        user.save()
    content = {"following": followee in user.following.all()}
    return JsonResponse(content, status=status)

def _logged_in_user(request):
    if not request.user.is_authenticated():
        return None
    return User.objects.get(local_user=request.user)

@login_required(login_url="/admin/login/")
def home(request):
    user = _logged_in_user(request)
    return timeline(request, user.id)

def user_statuses(request, user_id):
    user = User.objects.get(pk=int(user_id))
    title = "%s: Posts" % user.name
    entries = user.status_set.all()[:100]
    logged_in_user = _logged_in_user(request)
    if logged_in_user:
        logged_in_id = logged_in_user.id
    else:
        logged_in_id = None
    return HttpResponse(render(request, 'websocial/timeline.html', {
        'title': title, 
        'entries': entries,
        'user_id': logged_in_id,
        'poll_url': '/user/%d/status/json/' % user.id}))

class StatusForm(forms.Form):
    text = forms.CharField(max_length=140, widget=forms.TextInput(attrs={ 
        "id": "text_input",
        "class": "form-control", 
        "placeholder": "Sup?", 
        "aria-describedby": "basic-addon1"}))

class SearchForm(forms.Form):
    q = forms.CharField(max_length=256, required=False, widget=forms.TextInput(attrs={ 
        "id": "query_input",
        "class": "form-control", 
        "placeholder": "RSS/Atom URL or User", 
        "aria-describedby": "basic-addon2"}))

__validate = URLValidator()
def _valid_url(url):
    try:
        __validate(url)
        return True
    except ValidationError:
        return False

def _search_users(query):
    rss_users = User.objects.filter(url__icontains=query)
    local_users = User.objects.filter(nick__icontains=query)
    name_users = User.objects.filter(name__icontains=query)
    return (rss_users | local_users | name_users)[:10]
 

def search(request):
    query = request.GET.get('q', '')
    if query:
        search_form = SearchForm(request.GET)
    else:
        search_form = SearchForm()
    return render(request, 'websocial/search.html', {
        'query': query,
        'valid_url': _valid_url(query),
        'users': _search_users(query), 
        'search_form': search_form})

def search_json(request, query):
    return JsonResponse(_search_users(query), safe=False)

@login_required(login_url="/admin/login/")
@csrf_exempt
@require_http_methods(['POST'])
def following(request, user_id):
    if request.method == 'POST':
        url = request.POST['url']
        follower = User.objects.get(pk=user_id)
        followees = User.objects.filter(url=url)
        if followees:
            followee = followees[0]
        else:
            followee = User.objects.create(url=url, name="Feed", remote=True)
            followee.save()
        if not followee in follower.following.all():
            follower.following.add(followee)
            follower.save()
        return JsonResponse({'user_id': followee.id})
