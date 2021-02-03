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

    return render(request, 'app/home.html', {'title': test_title})


def upload(request):
    return render(request, 'app/upload_file.html', {'title': "Upload"})


def download(request):
    files_result = "null"
    result = {"name":"John", "age":30, "city":"New York"}
    if request.method == 'POST' and 'download_execute' in request.POST:
        from .updown import get_files
        import json
        files_result = get_files()
        result = json.dumps(files_result)

    return render(request, 'app/download_file.html', {'title': "Download", 'files_result': result})
