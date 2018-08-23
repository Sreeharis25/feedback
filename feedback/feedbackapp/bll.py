"""Bll for feedback app."""
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.template.loader import render_to_string


def send_feedback_mail(email_dict):
    """For sending email about feedback.

    Input Params:
        ticket_number (int): Ticket Number for the feedback
        username (str): Username
        feedback (str): Feedback
        email (email): Email Id of the user.
    """
    to = [email_dict['email']]
    from_email = 'hubbler@auditordesk.com'
    subject = 'Feedback Ticket ' + str(email_dict['ticket_number'])

    html_content = render_to_string(
        'feedback/email_template.html', {
            'single_line_text': email_dict['username'],
            'feedback': email_dict['feedback'],
            'ticket_number': email_dict['ticket_number']})
    text_content = strip_tags(html_content)

    try:
        msg = EmailMultiAlternatives(subject, text_content, from_email, to)
        msg.attach_alternative(html_content, "text/html")
        msg.send()
    except:
        pass

    return {'success': True}

