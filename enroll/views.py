from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, TemplateView, FormView, RedirectView
from django.views import View
from .models import User
from .forms import StuReg  

# Create your views here.


class UserAddShow(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, *args, **kwargs):
        # print(kwargs)
        # print('userad')
        context = super().get_context_data(**kwargs)
        # print()
        # print()
        # print(context)
        # print()
        # print()
        # print()
        f = StuReg()
        stu = User.objects.all()
        context = { 'stu': stu , 'frm':f}
        return context

    def post(self, request):
        contri = request.POST.getlist('office')
        print()
        print()
        print(contri)
        for i in contri:
            print(i)

        print()
        print()
        f = StuReg(request.POST)
        if f.is_valid():
            nm = f.cleaned_data['name']
            em = f.cleaned_data['email']
            pwd = f.cleaned_data['passsword']
            print(nm, em, pwd)
             
        
            
            reg = User(name=nm, email=em, password=pwd)
            reg.save()
            return HttpResponseRedirect('/')
            

class UserDel(RedirectView):
    url = "/"
    def get_redirect_url(self, *args, **kwargs):
         
        print(kwargs['id'])
        print('kwarg')
        del_id = kwargs['id']

        User.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args,**kwargs)


class editDAt(View):
    def get(self, request,id):
        Ui = User.objects.get(pk=id)
        uId = Ui.id
        fm = StuReg(initial={
            'name': Ui.name,
            'email' : Ui.email,
            'passsword': Ui.password
        })
        return render(request, 'updateandShow.html',{'fm':fm, 'id':uId})

    def post(self, request, id):
        Ui = User.objects.get(pk=id)
        #create instance
        fm = StuReg(request.POST,initial={
            'name': Ui.name,
            'email': Ui.email,
            'passsword': Ui.password
        })

        if fm.is_valid():
            #get data from form
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pwd = fm.cleaned_data['passsword']
            print(nm, em, pwd)
            
            #Updating Data
            Ui.name = nm
            Ui.email = em
            Ui.password = pwd

            Ui.save()


        return HttpResponseRedirect('/')

 
