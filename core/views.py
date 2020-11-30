from django.shortcuts import render

def index(request):
    user = request.user
    context = {}
    if not user.is_anonymous:
        context = {
            'name': user.first_name + ' ' + user.last_name,
            'customer_type': user.customer_set.last().customer_type if user.customer_set.last() else 'Nothing',
        }
    return render(request, 'core/index.html', context)

def contact(request):
    if request.method == 'POST':
        return render(request, 'core/index.html', {'name': "name"})
    return render(request, 'core/contact.html')