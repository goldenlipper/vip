from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Vip2, Vip1, Vip3, Vip4, GlUser, Selling


@login_required
def index(request):
    args = {'user': request.user}
    return render(request, 'vips/index.html', args)


@login_required
def clients(request, client_id, level_number):
    if level_number == '1':
        gluser_vip1 = GlUser.objects.get(id=client_id)
        vip1 = Vip1.objects.get(customer=gluser_vip1)
        lower_vips = vip1.lower_vip.vip_group
        args = {
            'vip1': vip1,
            'lower_vips': lower_vips,
        }
    elif level_number == '2':
        gluser_vip2 = GlUser.objects.get(id=client_id)
        vip2 = Vip2.objects.get(customer=gluser_vip2)
        lower_vips = vip2.lower_vip.vip_group
        args = {
            'vip2': vip2,
            'lower_vips': lower_vips,
        }
    elif level_number == '3':
        gluser_vip3 = GlUser.objects.get(id=client_id)
        vip3 = Vip3.objects.get(customer=gluser_vip3)
        lower_vips = vip3.lower_vip.vip_group
        args = {
            'vip3': vip3,
            'lower_vips': lower_vips,
        }
    else:
        gluser_vip4 = GlUser.objects.get(id=client_id)
        vip4 = Vip4.objects.get(customer=gluser_vip4)
        args = {
            'vip4': vip4,
        }
    return render(request, 'vips/clients.html', args)

@login_required
def dashboard(request, client_id, level_number):
    if level_number == '1':
        gluser_vip1 = GlUser.objects.get(id=client_id)
        vip1 = Vip1.objects.get(customer=gluser_vip1)
        lower_vips = vip1.lower_vip.vip_group
        if lower_vips is None:
            sellings = []
        else:
            sellings = Selling.objects.filter(seller__in=lower_vips.all())
        args = {
            'sellings': sellings,
            'lower_vips': lower_vips,
        }
    elif level_number == '2':
        gluser_vip2 = GlUser.objects.get(id=client_id)
        vip2 = Vip2.objects.get(customer=gluser_vip2)
        lower_vips = vip2.lower_vip.vip_group
        if lower_vips is None:
            sellings = []
        else:
            sellings = Selling.objects.filter(seller__in=lower_vips.all())
        args = {
            'sellings': sellings,
            'lower_vips': lower_vips,
        }
    elif level_number == '3':
        gluser_vip3 = GlUser.objects.get(id=client_id)
        vip3 = Vip3.objects.get(customer=gluser_vip3)
        lower_vips = vip3.lower_vip.vip_group
        if lower_vips is None:
            sellings = []
        else:
            sellings = Selling.objects.filter(seller__in=lower_vips.all())
        args = {
            'sellings': sellings,
            'lower_vips': lower_vips,
        }
    else:
        gluser_vip4 = GlUser.objects.get(id=client_id)
        vip4 = Vip4.objects.get(customer=gluser_vip4)
        lower_vips = vip4.lower_vip.vip_group
        if lower_vips is None:
            sellings = []
        else:
            sellings = Selling.objects.filter(seller__in=lower_vips.all())
        args = {
            'sellings': sellings,
            'lower_vips': lower_vips,
        }
    return render(request, 'vips/dashboard.html', args)


@login_required
def profile(request, client_id, level_number):
    if level_number == '1':
        vip1 = Vip1.objects.get(id=client_id)
        total = vip1.getAllTotal()
        args = {
            'total': total,
            'user': request.user
        }
    elif level_number == '2':
        vip2 = Vip2.objects.get(id=client_id)
        total = vip2.getAllTotal()
        args = {
            'total': total,
            'user': request.user
        }
    elif level_number == '3':
        vip3 = Vip3.objects.get(id=client_id)
        total = vip3.getAllTotal()
        args = {
            'total': total,
            'user': request.user
        }

        print(total)

    else:
        vip4 = Vip4.objects.get(id=client_id)
        total = vip4.getAllTotal()
        args = {
            'total': total,
            'user': request.user
        }
    return render(request, 'vips/profile.html', args)


@login_required
def vip1(request):
    vip1s = Vip1.objects.all()
    args = {
        'vip1s': vip1s
    }
    return render(request, 'accounts/vip1.html', args)

@login_required
def vip2(request, vip1_name):
    vip1 = Vip1.objects.get(customer_level_name=vip1_name)
    vip2s = Vip2.objects.filter(higher_vip1=vip1)
    args = {
        'vip2s': vip2s
    }
    return render(request, 'accounts/vip2.html', args)
