from .controllers.base import *

def page_not_found(request, exception):
    return render(request, 'error/404.html')