from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
def profile_list_view(request):
    obj_list = User.objects.filter(is_active=True)
    return render(request, 'profiles/list.html', {'obj_list': obj_list})

@login_required
def profile_detail_view(request, username=None, *args, **kwargs):
    user = request.user
    print(
        user.has_perm('subscriptions.free'),
        user.has_perm('subscriptions.basic'),
        user.has_perm('subscriptions.advance'),
        user.has_perm('subscriptions.pro')
    )

    user_obj = get_object_or_404(User, username=username)

    is_user = user_obj == user

    return render(request, 'profiles/detail.html', {"user_obj": user_obj, "owner":is_user})