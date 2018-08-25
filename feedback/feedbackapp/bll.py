# -*- coding: utf-8 -*-
"""Bll for feedback app."""
from __future__ import unicode_literals

from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags


def send_feedback_mail(email_dict):
    """For sending email about feedback.

    Input Params:
        ids (int): Corresponding value for each id for tags.
        email (email): Email Id of the user.
    """
    received_data = email_dict['received_data']
    subject = replace_subject_tags(received_data)
    email_body = replace_email_body_tags(received_data)

    to = [email_dict['email']]
    from_email = 'hubbler@cbsoft.co'
    text_content = strip_tags(email_body)

    try:
        msg = EmailMultiAlternatives(subject, text_content, from_email, to)
        msg.attach_alternative(email_body, "text/html")
        msg.send()
    except:
        pass

    return {'success': True}


def replace_email_tag(body_tags, string, received_data):
    """For replacing email tag.

    Input Params:
        body_tags (list): List of details of tags replacement .
        string (str): String to be replaced.
        received_data (dict): Data received.
    Output Params:
        string (str): Replaced string.
    """
    actual_string_length = len(string)
    string_diff = 0
    for tag in body_tags:
        if received_data.get(tag['id']):
            from_index = tag['from'] - string_diff
            to_index = tag['to'] - string_diff
            string = string[:from_index] + \
                received_data.get(tag['id']) + \
                string[to_index:]
            replaced_string_length = len(string)
            string_diff = actual_string_length - replaced_string_length

    return string


def replace_email_body_tags(received_data):
    """For replacing email body tags.

    Input Params:
        received_data (dict): Data received.
    Output Params:
        email_body (str): Replaced email body.
    """
    emailBodyTags = [
        {
            'text': '#single line text',
            'id': "5b46029bc20a6b25bbf51e74",
            'from': 119,
            'to': 136
        },
        {
            'text': '#Paragraph',
            'id': "5b471e70c20a6b5d789f560d",
            'from': 397,
            'to': 407
        },
        {
            'text': '#Number',
            'id': '5b46029bc20a6b25bbf51e76',
            'from': 577,
            'to': 584
        }
    ]

    email_body = \
        "<p>Hello <span class='atwho-inserted' data-atwho-at-query='#'>" + \
        "<span id='5b46029bc20a6b25bbf51e74' class='customFields'>" + \
        "#single line text</span></span>⁠,</p><p><br></p>" + \
        "<p>Greetings from hubbler. It has been privilege to serve you." + \
        "&nbsp;</p><p>Your below Feedback &nbsp;is received:</p><p>" + \
        "<span class='atwho-inserted' data-atwho-at-query='#'>" + \
        "<span id='5b471e70c20a6b5d789f560d' class='customFields'>" + \
        "#Paragraph</span></span>⁠&nbsp;</p><p><br></p><p>" + \
        "Your Ticket Number : " + \
        "<span class='atwho-inserted' data-atwho-at-query='#'>" + \
        "<span id='5b46029bc20a6b25bbf51e76' class='customFields'>" + \
        "#Number</span></span>⁠ is raised and will be responded to asap." + \
        "</p><p><br></p><p>Happy Hubblering!!</p><p>Team Hubbler</p>"

    email_body = replace_email_tag(emailBodyTags, email_body, received_data)

    return email_body


def replace_subject_tags(received_data):
    """For replacing subject tags of the email.

    Input Params:
        received_data (dict): Data received.
    Output Params:
        subject (str): Replaced Subject.
    """
    subjectTags = [
        {
            'text': '#Number',
            'id': '5b46029bc20a6b25bbf51e76',
            'from': 16,
            'to': 23
        }
    ]

    subject = 'Feedback Ticket #Number'
    subject = replace_email_tag(subjectTags, subject, received_data)

    return subject
