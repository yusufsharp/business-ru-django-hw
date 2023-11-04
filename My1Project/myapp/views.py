from django.shortcuts import render, redirect
from myapp.forms import MyProfileForm
from myapp.models import User

#def index(request):
#    return render(request, 'myapp/index.html')


def index(request):
    if request.method == 'POST':
        form = MyProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('study')
        else:
            errors = form.errors
            for field, error_list in errors.items():
                for error in error_list:
                    print(f"Ошибка в поле '{field}': {error}")

    context = {'form': MyProfileForm()}
    return render(request, 'myapp/index.html', context)


def study(request):
    last_user = User.objects.latest('id')
    age = last_user.calculate_age()
    return render(request, 'myapp/study.html', {'last_user': last_user, 'age': age})
