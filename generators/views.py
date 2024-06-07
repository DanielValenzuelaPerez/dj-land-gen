from django.shortcuts import render

from .models import MyClass, Aspect, MyClassElement, AspectElement


def home(request):
    my_classes = MyClass.objects.all()
    aspects = Aspect.objects.all()

    context = {
        'my_classes': my_classes,
        'aspects': aspects,
    }

    if request.method == 'POST':
        selected_class_id = request.POST.get('classes')
        selected_class = MyClass.objects.get(id=selected_class_id)
        selected_aspect_id = request.POST.get('aspects')
        selected_aspect = Aspect.objects.get(id=selected_aspect_id)
        class_elements = list(MyClassElement.objects.filter(class_name=selected_class_id).order_by('?').values_list('name', flat=True)[:3])
        aspect_elements = list(AspectElement.objects.filter(aspect_name=selected_aspect_id).values_list('name', flat=True).order_by('?')[:3])
        context.update({
            'class_elements': class_elements, 
            'aspect_elements': aspect_elements,
            'selected_class': selected_class,
            'selected_aspect': selected_aspect,
        })

    return render(request, 'home.html', context)
