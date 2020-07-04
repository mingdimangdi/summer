from django.shortcuts import render, get_object_or_404, redirect
from .models import card
from django.urls import reverse 
from .forms import createForm
# Create your views here.

def main(request):
    cards = card.object.all
    return render(request, 'main.html',{'card':cards})

def create(request):
    form =createForm()
    if request.method == "POST":
        card_val = card()
        card_val.cardImage = request.FILES['photo']
        card_val.cardName = request.POST['cardName']
        card_val.cardExplain = request.POST['cardExplain']
        card_val.save()
        return redirect(reverse('main'))
    else:
        pass
    return render(request, 'create.html',{'form':form})





def update(request, change_id):
    change_obj = get_object_or_404(card, pk=change_id)
    
    if request.method == "POST":
        change_obj.cardName = request.POST['cardName']
        change_obj.cardExplain = request.POST['cardExplain']
        change_obj.save()
        return redirect(reverse('main'))
    else:
        pass
    return render(request, 'update.html',{'change_key':change_obj})

def delete(request, delete_id):
    delete_obj = get_object_or_404(card, pk=delete_id)
    delete_obj.delete()
    return redirect('main')