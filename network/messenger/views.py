from django.shortcuts import render


def index(request):
    return render(request, "index.html", {'title': 'Главная страница'})


def about(request):
    return render(request, "about.html", {'title': 'О нас'})


# errors

def page_not_found_view(request, exception):
    return render(request, 'messenger/errs/404.html', status=404)

# def page_bad_request(request, exception):
#     return render(request, 'messenger/errs/400.html', status=400)
#
# def page_forbidden(request, exception):
#     return render(request, 'messenger/errs/403.html', status=403)
#
# def page_internal_server(request, exception):
#     return render(request, 'messenger/errs/500.html', status=500)
