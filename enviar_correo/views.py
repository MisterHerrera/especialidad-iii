from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.shortcuts import render
from django.conf import settings  # Asegúrate de tener esto para acceder a settings.DEFAULT_FROM_EMAIL

def enviar_correo(request):
    if request.method == "POST":
        # Obtener el correo del destinatario desde el formulario
        recipient = request.POST.get('recipient')

        # Asunto del correo
        subject = 'Correo de Farmacia Jesús'

        # Correo desde el cual se enviará el email, obtenido de settings
        from_email = settings.DEFAULT_FROM_EMAIL  # Puedes cambiar esto por un correo específico

        # Lista de destinatarios con el correo del formulario
        recipient_list = [recipient]  # Destinatario ingresado por el usuario
        
        # Cargar plantilla HTML del correo
        html_content = render_to_string('email_template.html', {'nombre': 'Cliente'})  # Pasando contexto al template
        text_content = strip_tags(html_content)  # Generar una versión sin HTML
        
        # Crear el objeto de correo
        email = EmailMultiAlternatives(subject, text_content, from_email, recipient_list)
        email.attach_alternative(html_content, "text/html")
        
        # Intentar enviar el correo
        try:
            email.send()
            return HttpResponse('Correo enviado exitosamente.')
        except Exception as e:
            return HttpResponse(f'Error al enviar el correo: {str(e)}')

    # Renderizar el formulario si no es una solicitud POST
    return render(request, 'enviar_correo.html')
