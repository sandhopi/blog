from django.shortcuts import render
from django.http import HttpResponse
from blog.models import ContentBlog
from django.db.models import OuterRef, Subquery


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    
    artikel_terbaru = ContentBlog.objects.order_by('-created').first()
    artikel_2 = ContentBlog.objects.order_by('-created')[:2]
    artikel_kedua = artikel_2[1] if len(artikel_2) > 1 else None
    
    artikel_3 = ContentBlog.objects.order_by('-created')[:3]
    artikel_ketiga = artikel_3[2] if len(artikel_3) > 1 else None

    artikel_4 = ContentBlog.objects.order_by('-created')[:4]
    artikel_keempat = artikel_4[3] if len(artikel_4) > 1 else None

    artikel_5 = ContentBlog.objects.order_by('-created')[:5]
    artikel_kelima = artikel_5[4] if len(artikel_5) > 1 else None
    
    late_post = ContentBlog.objects.order_by('-created')

    subquery = ContentBlog.objects.filter( category=OuterRef('category')).order_by('-created')
    per_kategori_3 = ContentBlog.objects.filter( id=Subquery(subquery.values('id')[:1])).order_by('-created')[:3]
    per_kategori_4all = ContentBlog.objects.filter( id=Subquery(subquery.values('id')[:1])).order_by('-created')[3:5]

    context = {
        'new_content' : artikel_terbaru,
        'second_content' : artikel_kedua,
        'content_3' : artikel_ketiga,
        'content_4' : artikel_keempat,
        'content_5' : artikel_kelima,
        'late_post' : late_post[:6],
        'kategori_post' : per_kategori_3,
        'kategori_post_4all' : per_kategori_4all,
    }

    return render(request, 'beranda/index.html', context)


def kategori(request):
    
    artikel_terbaru = ContentBlog.objects.order_by('-created').first()
    artikel_2 = ContentBlog.objects.order_by('-created')[:2]
    artikel_kedua = artikel_2[1] if len(artikel_2) > 1 else None
    
    artikel_3 = ContentBlog.objects.order_by('-created')[:3]
    artikel_ketiga = artikel_3[2] if len(artikel_3) > 1 else None

    artikel_4 = ContentBlog.objects.order_by('-created')[:4]
    artikel_keempat = artikel_4[3] if len(artikel_4) > 1 else None

    artikel_5 = ContentBlog.objects.order_by('-created')[:5]
    artikel_kelima = artikel_5[4] if len(artikel_5) > 1 else None
    
    late_post = ContentBlog.objects.order_by('-created')

    context = {
        'new_content' : artikel_terbaru,
        'second_content' : artikel_kedua,
        'content_3' : artikel_ketiga,
        'content_4' : artikel_keempat,
        'content_5' : artikel_kelima,
        'late_post' : late_post[:6]
    }

    return render(request, 'beranda/index.html', context)