from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.shortcuts import render

def enviar_correo(request):
    if request.method == "POST":
        subject = 'Correo de Farmacia Jesús'
        from_email = 'henriquezurbinae0@gmail.com'  # Cambia por tu correo real
        recipient_list = ['correo_destinatario@dominio.com']  # Cambia al correo del destinatario real
        
        # Cargar plantilla HTML del correo
        html_content = render_to_string('email_template.html', {'nombre': 'Cliente'})
        text_content = strip_tags(html_content)  # Eliminar etiquetas HTML para la versión de texto
        
        # Crear el objeto de correo
        email = EmailMultiAlternatives(subject, text_content, from_email, recipient_list)
        email.attach_alternative(html_content, "text/html")
        
        try:
            email.send()
            return HttpResponse('Correo enviado exitosamente.')
        except Exception as e:
            return HttpResponse(f'Error al enviar el correo: {str(e)}')

    # Renderizar el formulario si no es una solicitud POST
    return render(request, 'enviar_correo.html')

