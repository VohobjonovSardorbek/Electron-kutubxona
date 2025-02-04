from django.shortcuts import render, get_object_or_404, redirect
from django.template.context_processors import request

from .models import *
from django.db.models import Q


def bosh_sahifa_view(reqest):
    return render(reqest, 'bosh_sahifa.html')


def bolimlar_view(request):
    bolimlar = Bolim.objects.all().order_by('nom')
    context = {
        "bolimlar": bolimlar
    }
    return render(request, 'bolimlar.html', context=context)


def mualliflar_view(request):
    mualliflar = Muallif.objects.all().order_by('ism')
    context = {
        "mualliflar": mualliflar
    }
    return render(request, 'mualliflar.html', context=context)


def kitoblar_view(request):
    kitoblar = Kitob.objects.all().order_by('nom')
    context = {
        "kitoblar": kitoblar
    }
    return render(request, 'kitoblar.html', context=context)


def yangi_asarlar_view(request):
    kitoblar = Kitob.objects.filter(muallif__tirik=True)
    context = {
        "kitoblar" : kitoblar
    }
    return render(request, 'yangi_asarlar.html', context=context)

def kitob_details_view(request, pk):
    kitob = get_object_or_404(Kitob, id=pk)
    context = {
        "kitob" : kitob
    }
    return render(request, 'kitob_details.html', context=context)

def kitob_qoshish_view(request):
    if request.method == 'POST':
        Kitob.objects.create(
            nom=request.POST.get('nom'),
            user=request.POST.get('user'),
            muallif=Muallif.objects.get(id=request.POST.get('muallif_id')),
            yil=request.POST.get('yil'),
            bolim=Bolim.objects.get(id=request.POST.get('bolim_id')),
        )
        return redirect('kitoblar')
    mualliflar = Muallif.objects.order_by('ism')
    bolimlar = Bolim.objects.order_by('nom')
    context = {
        "mualliflar" : mualliflar,
        "bolimlar" : bolimlar
    }
    return render(request, 'kitob_qoshish.html', context=context)


def kitob_detele_view(request, pk):
    kitob = get_object_or_404(Kitob, id=pk)
    kitob.delete()
    return redirect('kitoblar')


def kitob_update_view(request, pk):
    if request.method == 'POST':
        Kitob.objects.filter(id=pk).update(
            nom=request.POST.get('nom'),
            user=request.POST.get('user'),
            muallif=Muallif.objects.get(id=request.POST.get('muallif_id')),
            yil=request.POST.get('yil'),
            bolim=Bolim.objects.get(id=request.POST.get('bolim_id'))
        )
        return redirect('kitoblar')
    kitob = Kitob.objects.get(id=pk)
    mualliflar = Muallif.objects.exclude(ism=kitob.muallif.ism)
    bolimlar = Bolim.objects.exclude(nom=kitob.bolim.nom)
    context = {
        "kitob" : kitob,
        "mualliflar" : mualliflar,
        "bolimlar" : bolimlar
    }
    return render(request, 'kitob_update.html', context=context)