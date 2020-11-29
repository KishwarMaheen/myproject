from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.db.models import Count
from django.contrib.auth.models import User
# from django.http import HttpResponse
# from django.http import Http404
from django.http import HttpResponseRedirect
from .models import Board, Topic, Post
from .forms import NewTopicForm, PostForm


# Create your views here.
def home(request):
    board_list = Board.objects.all()
    # board_names = list()
    # for board in board_list:
    #     board_names.append(board.name)
    # http_response = "<br>".join(board_names)
    # return HttpResponse(http_response)
    return render(request, 'home.html', context={'boards': board_list})


def board_topics(request, pk):
    # try:
    #     board = Board.objects.get(pk=pk)
    # except Board.DoesNotExist:
    #     raise Http404
    board = get_object_or_404(Board, pk=pk)
    topics = board.topics.order_by('-last_updated').annotate(replies=Count('posts') - 1)
    return render(request, 'topics.html', {'board': board, 'topics': topics})


@login_required
def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    # user = User.objects.first()
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            # topic.starter = user
            topic.starter = request.user
            topic.save()
            post = Post.objects.create(message=form.cleaned_data.get('message'),
                                       topic=topic,
                                       created_by=request.user)
                                       # created_by=user)
        # subject = request.POST['subject']
        # message = request.POST['message']
        # user = User.objects.first()
        # topic = Topic.objects.create(subject=subject, board=board, starter=user)
        # return HttpResponseRedirect(reverse('board_topics'), pk=pk) This was stupid of me
        # return redirect(reverse('board_topics'), pk=board.pk) This doesn't work for some reason
            return redirect('topic_posts', pk=pk, topic_pk=topic.pk)
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', context={'board': board, 'form': form})


def topic_posts(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board_id=pk, id=topic_pk)
    topic.views += 1
    topic.save()
    return render(request, "topic_posts.html", context={'topic': topic})


@login_required
def reply_topic(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board_id=pk, id=topic_pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            return redirect('topic_posts', pk=pk, topic_pk=topic_pk)
    else:
        form = PostForm()
    return render(request, "reply_topic.html", context={'topic': topic, 'form': form})
