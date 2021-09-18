from django.shortcuts import redirect, render
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from .serializers import RegisterSerializer,GetToDo,ToDo,GetUser
from .models import User,Todo
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.utils.dateparse import parse_date
from rest_framework.parsers import JSONParser 




class Register(APIView):
    permission_classes = (AllowAny,)
    def post(self,request):
        acc = RegisterSerializer(data=request.data)
        if not acc.is_valid():
            return Response('not valid')
        else:
            username = acc.data["username"]
            email = acc.data["email"]
            password = acc.data["password"]
            re_password = acc.data["re_password"]
            if password!=re_password:
                return HttpResponse('password not correspond!') 
            user=User.objects.filter(username=username)
            if user:
                return HttpResponse('account existing!')
            usr=User.objects.create(username=username,email=email,password=make_password(password))
            usr.save()
        return HttpResponse('signup successful!')


class ToDoAPI(APIView):
    def post(self,request):
        task = ToDo(data=request.data)
        if not task.is_valid():
            return Response('not valid')
        title = task.data["title"]
        description = task.data["description"]
        user_id = task.data["user_id"]
        date_complete = parse_date(task.data["date_complete"])
        status = task.data["status"]
        t = Todo(title=title,description=description,user_id=user_id,date_complete=date_complete,status=status)
        t.save()
        return HttpResponse('saved task!')


class UpdateToDoAPI(APIView):
    def patch(self,request,id):
        task = ToDo(data=request.data)
        query = Todo.objects.get(pk=id)
        if query.status == 'COMPLETE':
            return Response('cannot update!')
        else:
            if not task.is_valid():
                return Response('not valid')
            query.title = task.data["title"]
            query.description = task.data["description"]
            query.user_id = task.data["user_id"]
            query.status = task.data["status"]
            query.save()
            return Response('updated successfully!')
        return Response('Update side!')


class RemoveToDoAPI(APIView):
    def delete(self,request,id):
        query = Todo.objects.get(pk=id)
        if query.status == 'COMPLETE':
            return Response('cannot delete!')
        else:
            query.delete()
            return Response('deleted successfully!')
        return Response('delete side!')



class GetALLToDoAPI(APIView):
    def get(self,request):
        list_todo = Todo.objects.all()
        todo_all = GetToDo(list_todo,many=True)
        return Response(data=todo_all.data)

class GetOneToDOAPI(APIView):
    def get(self,request,id):
        one_todo = Todo.objects.get(pk=id)
        todo = GetToDo(one_todo)
        return Response(data=todo.data)


class GetAllUserAPI(APIView):
    def get(self,request):
        user = User.objects.values('id','username','email')
        getuser = GetUser(user,many=True)
        return Response(data=getuser.data)
        
        

            
