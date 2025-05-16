from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignIn, SignUp, forgotPass, resetPass
from django.contrib.auth.models import User 
from django.contrib import messages
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.sites.shortcuts import get_current_site
from django.template import loader
from django.core.mail import EmailMultiAlternatives
from .utils import token_generator
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required

def sign_up(request):
    form = SignUp()
    
    if request.method == 'POST':
        user = request.POST['username'] 
        mail = request.POST['email'] 
        passw = request.POST['password']

        exs_user = User.objects.filter(username = user)

        if exs_user.count() == 0 :
            user_signup = User.objects.create_user(
                username     = user,
                first_name   = '',
                last_name    = '',
                email        = mail, 
                password     = passw
            )
            user_signup.is_active = False
            user_signup.save()
            user_idb64  = urlsafe_base64_encode(force_bytes(user_signup.pk))
            url_domain = get_current_site(request).domain
            subject = 'Activate Your Account'
            templ = loader.get_template('account/email_verification.html')
            context = {
                    'domain': url_domain,
                    'uid': user_idb64,
                    'token': token_generator.make_token(user_signup),
                }
            msg = templ.render(context)

            email  = EmailMultiAlternatives(subject=subject,body=msg,to=[mail] )
            email.content_subtype = "html" 
            if email.send():
                messages.success(request, "Silahkan melakukan aktivasi. Link aktivasi dikirimkan melalui email yang sudah didaftarkan.")
                form = SignUp()
                # return HttpResponse(1)
        else:
            messages.warning(request, "Username sudah ada.")
            # return HttpResponse(0)
            form = SignUp()

    context = {
        'formUp' : SignUp()
    }        
    return render(request, "account/sign_up.html",context)

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and token_generator.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
        return render(request, "account/success_activation.html")
        # return redirect('account/success_activation.html')
    else:
        messages.error(request, 'Activation link is invalid!')

    return render(request, "not_found.html")

def sign_in(request):
    form = SignIn()
    if request.method == 'POST':
        user = request.POST['username']
        passw = request.POST['password']

        try:
            user = User.objects.get(username=user)
       
            # return HttpResponse(0)

            user_auth = authenticate(request, username=user, password=passw)
            
            if user_auth is not None and user.is_active is True:
                login(request, user_auth)
                # messages.success(request, "login sukses.")
                return redirect('/')
                
                # return HttpResponse(1)
            
            elif user_auth is not None:
                messages.warning(request, "Password tidak cocok.")
                form = SignIn()
                # return HttpResponse(2)
            
            elif user.is_active is False:
                messages.warning(request, "Silahkan melakukan aktivasi terlebih dahulu.")
                # return HttpResponse(3)
                form = SignIn()
            else:
                messages.warning(request, "Password tidak cocok.")
                form = SignIn()
                # return HttpResponse(0)
            
        except User.DoesNotExist:
            messages.error(request, "User tidak dikenali")
            form = SignIn()
    context = {
        'formIn' : SignIn()
    }

    return render(request, "account/sign_in.html",context)

@login_required
def log_out(request):
    messages.get_messages(request).used = True
    logout(request)
    return redirect('/')