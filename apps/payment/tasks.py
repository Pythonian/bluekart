from io import BytesIO
from celery import shared_task
import weasyprint
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from apps.orders.models import Order


@shared_task
def payment_completed(order_id):
    """Send an email notification when an order is successfully paid."""
    order = Order.objects.get(id=order_id)
    # create invoice email
    subject = f'Bluekart - Invoice no. {order.id}'
    message = 'Please, find attached the invoice of your recent purchase.'
    email = EmailMessage(subject, message, 'admin@bluekart.com', [order.email])
    # generate PDF
    html = render_to_string('orders/order_pdf.html', {'order': order})
    out = BytesIO()
    stylesheets = [weasyprint.CSS(settings.STATIC_ROOT + '/' + 'css/ui.css')]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)
    # attach PDF file
    email.attach(f'order_{order.id}.pdf', out.getvalue(), 'application/pdf')
    # send email
    email.send()