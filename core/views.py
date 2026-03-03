from django.shortcuts import render
from django.contrib.auth.decorators import login_required 
from django.db import connection
from django.contrib.auth.models import User
from core.models import SecurityIncident



@login_required # Aquesta línia protegeix la vista. Sense sessió, no passes. 

def perfil_usuari(request):

	return render(request, 'perfil.html')




@login_required
def vulnerable_search(request):
    query = request.GET.get('q')
    results = []

    if query:

        # Control d'accés mantingut
        if request.user.is_superuser:
            incidents = SecurityIncident.objects.filter(title__icontains=query)
        else:
            incidents = SecurityIncident.objects.none()

        results = [(i.id, i.title, i.description) for i in incidents]

    return render(request, "search.html", {"results": results})


from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@login_required
@csrf_exempt
def update_email(request):

    if request.method == "POST":
        email = request.POST.get("email")

        # ÚS SEGUR DE L'ORM
        User.objects.filter(id=request.user.id).update(email=email)

        return HttpResponse("Email actualitzat")

    return render(request, "update_email.html")

from django.shortcuts import render, get_object_or_404
from .models import SecurityIncident

@login_required
def incident_detail(request, id):
    1/0
    incident = get_object_or_404(
        SecurityIncident,
        id=id,
        creator=request.user   # FILTRE PER USUARI PROPIETARI
    )

    return render(request, "incident_detail.html", {
        "incident": incident
    })
