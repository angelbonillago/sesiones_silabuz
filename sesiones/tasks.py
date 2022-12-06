from time import sleep
from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_book(nombre, mail):
    sleep(20)  # Simula operaciones muy pesadas que congelan a Django
    print(
        nombre + " " + mail
    )



@shared_task
def enviar_correo(nombre, mail):
    
    send_mail(
        'Subject here',
        'Here is the message.',
        'from@example.com',
        [mail],
        fail_silently=False,
    )

    return "correo enviado"