from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def home(request):
#     return HttpResponse('<h1>App Home</h1>')

def home(request):
    test_title = "Home"
    if request.method == 'POST' and 'run_script' in request.POST:

        # import function to run
        from .updown import FileDownload
        from .updown import FileUpload
        from .updown import main
        from .updown import hello_title_change
        # from .updown import DriveAPI

        # call function
        test_title = main_function(1, 2)
        print(test_title)
        main()

    return render(request, 'app/home.html', {'title': test_title, 'test_param': 'debug test param...'})



    # return user to required page
    # return HttpResponseRedirect(reverse(app:app/home)
