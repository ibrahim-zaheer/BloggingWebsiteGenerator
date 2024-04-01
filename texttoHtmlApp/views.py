from django.shortcuts import render
from .forms import MyForm
from django.http import HttpResponse

def convertor_view(request):
    form = MyForm()
    return render(request, 'index.html', {'form': form})


def generate_html(request):
    if request.method == 'POST':
        html_content = request.POST.get('html_content', '')

        # Ensure there is content to generate HTML file
        if html_content:
            response = HttpResponse(html_content, content_type='text/html')
            response['Content-Disposition'] = 'attachment; filename="generated_html.html"'
            return response
        else:
            return HttpResponse("No HTML content provided", status=400)
    else:
        return HttpResponse("Method not allowed", status=405)