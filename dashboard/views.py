from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
# from base.helper import ImageGenerator
from base.helper import cnts


@login_required(login_url='sign-in')
def index(request):
    # l = ["Simptom (плюс) ёки Милап -10мг 1таб (уйку олдидан) 10кун",
    #      "Na тиосулфат-30% 10мл  + NaCl-0.9% 100 ml в/в капельно 7кун",
    #      "Комбинил (флоксодекс)-3-5том х 3мах 10кун қулоқга томчи 08:00-12:00-16:00да",
    #      "Флюзамед -> 3-5том х 3мах 10кун қулоқга томизиш 10:00-14:00-18:00да",
    #      "2,4 млн ЕД + вода для инекции в/м каж 21день (после пробы с пеннициллином)"
    #  ]
    # ImageGenerator("Eshmatjon Toshmatbekov", 2028, "Oyoqlardan ayrilding", l)

    ctx = {
        'cnts': cnts()
    }
    return render(request, 'dashboard/pages/index.html', ctx)


