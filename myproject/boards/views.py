from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.models import User
# from django.http import HttpResponse
# from django.http import Http404
from django.http import HttpResponseRedirect
from .models import Board, Topic, Post
from .forms import NewTopicForm


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
    return render(request, 'topics.html', context={'board': board})


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
            return HttpResponseRedirect(reverse('board_topics', args=(pk,)))
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', context={'board': board, 'form': form})

