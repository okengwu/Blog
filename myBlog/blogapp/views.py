from django.shortcuts import render



def post_list(request):
   # face = request.POST['www.facebook.com']
    return render(request,'blogapp/post_list.html', {
      #  "facebook" : face

    })


# Create your views here.
