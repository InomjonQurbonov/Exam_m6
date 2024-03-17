from django.shortcuts import render, get_object_or_404,redirect

from uno.models import News,Users,Members


def index(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'about_us/about_us.html')

def our_works(request):
    return render(request, 'our_works/our_works.html')

def law(request):
    return render(request, 'our_works/international_law.html')

def news_list(request):
    news = News.objects.all()
    return render(request,'news/news.html',{'news_list':news})

def news_detail(request, pk):
    new = News.objects.get(id=pk)
    return render(request, 'news/about_news.html', {'new_detail': new})

def add_news(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        news_date = request.POST.get('news_date')
        news = News(title=title,content=content,news_date=news_date)
        news.save()
        return redirect('news_detail',pk=news.id)
    else:
        return render(request, 'news/add_news.html')

def edit_news(request, pk):
    this_news = get_object_or_404(News,pk=pk)
    if request.method == 'POST':
        this_news.title = request.POST.get('title')
        this_news.content = request.POST.get('content')
        this_news.news_date = request.POST.get('news_date')
        this_news.save()
        return redirect('news_detail',pk=this_news.pk)
    else:
        return render(request, 'news/edit_news.html',{'news':this_news})

def delete_news(request, pk):
    this_news = get_object_or_404(News,pk=pk)
    this_news.delete()
    return redirect('news_list')

#register form
def new_user(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        password = request.POST['password']
        phone = request.POST['phone']
        new_user = Users(full_name=full_name,email=email,password=password,phone=phone)
        new_user.save()
        return redirect('add_news',pk=new_user.pk)
    else:
        return render(request,'login_form/register.html')

def members_list(request):
    members = Members.objects.all()
    return render(request,"about_us/our_members.html",{'members':members})

def members_details(request,pk):
    members = Members.objects.get(pk=pk)
    return render(request,'about_us/member_info.html',{'members':members})

def add_members(request):
    if request.method == 'POST':
        member_name = request.POST['member_name']
        add_date = request.POST['add_date']
        about_member = request.POST['about_member']
        members = Members(member_name=member_name,add_date=add_date,about_member=about_member)
        members.save()
        return redirect('members_details',pk=members.pk)
    else:
        return render(request,'about_us/add_members.html')

def edit_members(request,pk):
    this_member = Members.objects.get(pk=pk)
    if request.method == 'POST':
        this_member.member_name = request.POST['member_name']
        this_member.add_date = request.POST['add_date']
        this_member.about_member = request.POST['about_member']
        this_member.save()
        return redirect('members_details',pk=this_member.pk)
    else:
        return render(request,'about_us/edit_members.html',{'member':this_member})

def delete_members(request,pk):
    this_member = get_object_or_404(Members,pk=pk)
    this_member.delete()
    return redirect('members_list')