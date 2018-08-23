"""Views for feedback app."""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import utilities
import bll


def index(request):
    """Json request for getting data into feedback form."""
    dictionary = {
        'fields': [
            {
                'type': 'single line text',
                'id': '5b46029bc20a6b25bbf51e74',
                'lbl': 'single line text',
                'placeholder': 'User name'
            },
            {
                'type': 'paragraph',
                'id': '5b471e70c20a6b5d789f560d',
                'lbl': 'paragraph',
                'placeholder': 'Feedback'
            },
            {
                'type': 'number',
                'id': '5b46029bc20a6b25bbf51e76',
                'lbl': 'Number',
                'placeholder': 'Ticket number'
            }
        ],
    }

    return render(
        request, 'feedback/index.html', {'data': dictionary['fields']})


@csrf_exempt
def send_feedback_mail(request):
    """For sending feedback email according to feedback.

    Input Params:
        ticket_number (int): Ticket Number for the feedback
        username (str): Username
        feedback (str): Feedback
        email (email): Email Id of the user.
    """
    request_dict = {}
    try:
        request_dict['received_data'] = request.POST
        request_dict['mandatory_params'] = [
            ('ticket_number', 'int'), ('username', 'str'),
            ('feedback', 'str'), ('email', 'email')]
        email_dict = utilities.fetch_request_params(request_dict)

        bll.send_feedback_mail(email_dict)
        data = render(request, 'feedback/success.html')
    except (KeyError, ValueError) as e:
        data = render(
            request, 'feedback/error_occured.html',
            {'data': e.message})
    return data
