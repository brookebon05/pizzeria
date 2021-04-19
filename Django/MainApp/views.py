from django.shortcuts import render
from .models import Topic
from .forms import TopicForm

# Create your views here.


def index(request):
    # The home page for LEarning Log
    return render(request, "MainApp/index.html")


def topics(request):
    topics = Topic.objects.order_by("date_added")
    context = {"topics": topics}
    return render(request, "MainApp/topics.html", context)


def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by("-date_added")
    context = {"topic": topic, "entries": entries}
    return render(request, "MainApp/topic.html", context)


# GET AND POST ARE TWO WAYS USER CAN INTERACT
def new_topic(request):
    if request.method != "POST":  # is a get request
        form = TopicForm()
    else:
        form = TopicForm(data=request)
        if form.is_valid():
            form.save()

            return redirect("MainApp:topics")
    context = {"form": form}
    return render(request, "MainApp/new_topic.html", context)
