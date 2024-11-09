
from django.http import Http404
from django.shortcuts import render
from todo.models import Todo


def todo_list(request):
    todo_list = Todo.objects.all().values('id', 'title')
    result = [{'id': todo['id'], 'title': todo['title']} for todo in todo_list]

    return render(request, 'todo_list.html', {'data': result})


def todo_info(request, todo_id):
    try:
        todo = Todo.objects.get(id=todo_id)
        info = {
            'title': todo.title,
            'description': todo.description,
            'start_date': todo.start_date,
            'end_date': todo.end_date,
            'is_completed': todo.is_completed,
        }
        return render(request, 'todo_info.html', {'data': info})
    except Todo.DoesNotExist:
        raise Http404("해당 Todo가 존재하지 않습니다.")

