from .models import Menu, Contact


def menu_list(request):
    menu = Menu.objects.filter(active=True, is_staff=False)

    return {
        'menu': menu
    }

def menu_child_list(request):
    menu_child = Menu.objects.filter(active=True, is_staff=False, is_parent=False)

    return {
        'menu_child': menu_child
    }

def contact_list(request):
    contact = Contact.objects.all()

    return {
        'contact': contact
    }