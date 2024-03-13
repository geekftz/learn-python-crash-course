from django.shortcuts import render

from .models import Topic


# Create your views here.
def index(request):
    """the page that learn notes"""
    print("index index")
    return render(request, 'learning_logs/index.html')


def topics(request):
    """show all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """show single topic and its details"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
