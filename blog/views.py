from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import ContentBlog, Category, UrlPerfom
from django.db.models import Count
import base64
from django.contrib import messages
from .forms import BlogFrom
import json
from django.views.decorators.csrf import csrf_exempt


def detail(request, id):
    category_counts = Category.objects.annotate(cat_counts=Count('contentblog')).order_by('-cat_counts')
    if not id:
        return render(request, "blog/not_found.html")
    
    try:        
        decoded_data = base64.urlsafe_b64decode(id[1:])
        pk = decoded_data.decode('utf-8')

        blog_content = ContentBlog.objects.get(pk=pk)
        recent_content = ContentBlog.objects.all().order_by('-created')[:5]
        

        content ={
            'blog_detail' : blog_content,
            'category_counts' : category_counts,
            'recent' : recent_content
        }


        return render(request, "blog/index.html", content )
    
    except Exception as e:
        
        return render(request, "blog/not_found.html")
    

def add_blog(request):
    form = BlogFrom()

    if request.method == 'POST' and request.FILES['image']:
        form = BlogFrom(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            messages.success(request, 'Artikel sukses disimpan.')
            form = BlogFrom()
        else:
            messages.warning(request, 'Artikel gagal disimpan.')
    context = {
        'form' : form
    }

    return render(request, "blog/add_article.html", context)

@csrf_exempt
def add_perfom(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)

        UrlPerfom.objects.create( 
                                    url             = data['url'], 
                                    click_element   = data['el_click'],
                                    scroll_position = data['scroll_pos'],
                                    used_time       = data['used_time'],
                                    user_agent      = data['user_agent'],
                                    see_user_id     = data['user_id'],
                                )
        # pengguna = Pengguna(nama=data['nama'], email=data['email'])
        # pengguna.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

    
    