from django.shortcuts import render
from blog.models import ContentBlog


def result(request):
    if request.method == 'POST':
        parm = request.POST['search_parm'] 
        result = ContentBlog.objects.filter(title__icontains=parm)
        print(result)
        context = {
            
            'result' : result
        }

        return render(request, "search_result/index.html", context )
    
def category_blog(request, cat):
    result = ContentBlog.objects.filter(category=cat)
    
    context = {    
        'result' : result
    }

    return render(request, "search_result/index.html", context )