from django.shortcuts import render

class Custom404Middleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        
        if response.status_code == 404:
            return self.custom_404_page(request, response)
        
        return response
    
    def custom_404_page(self, request, exception):
        return render(request, 'home/404.html', status=404)
