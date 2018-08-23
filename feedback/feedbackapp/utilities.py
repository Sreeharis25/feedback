"""Utilities for feedback app."""
from django.core.validators import validate_email


def fetch_request_params(request_dict):
    """
    Function to collect the parameters in request.

    Input params:
        request_dict (obj): object which contains,
            mandatory_params (list): parameter list, which should be
                in the request.
            optional_params (list): parameters, which is optional
            media_params(list): media data.
            received_data (dict): json dictionary which contains the parameters
                in the parameter list.
    Return:
        param_dict (obj): object which has the collected parameters.
    """
    param_dict = {}
    if 'mandatory_params' in request_dict.keys():
        fetch_mandatory_params(request_dict, param_dict)

    return param_dict


def fetch_mandatory_params(request_dict, param_dict):
    """Function to fetch the mandatory parameters in request."""
    for item in request_dict['mandatory_params']:
        parameter = item[0]
        value = request_dict['received_data'].get(parameter)
        if not value:
            raise KeyError('%s is missing in request params' % (parameter))
        else:
            value_dict = {}
            value_dict['value'] = value
            value_dict['parameter'] = parameter
            value_dict['type'] = item[1]
            value = check_parameter_value(value_dict)

        param_dict[parameter] = value
    return param_dict


def check_parameter_value(value_dict):
    """
    Function to check the parameter vales and type.

    Input Params:
        value_dict (obj): collection obj with following data,
            value: value collected
            parameter: parameter name.
            type: value type
    """
    if value_dict['type'] == 'int':
        return(check_int_value(value_dict))
    elif value_dict['type'] == 'str':
        return(check_str_value(value_dict))
    elif value_dict['type'] == 'email':
        return(check_email_value(value_dict))
    else:
        raise ValueError('Invalid parameter type')


def check_int_value(value_dict):
    """Function to check the int value, and return the value."""
    try:
        return int(value_dict['value'])
    except:
        raise ValueError('%s must be int' % (value_dict['parameter']))


def check_str_value(value_dict):
    """Function to check the str value, and return the value."""
    try:
        return str(value_dict['value'])
    except:
        try:
            return str(value_dict['value'].encode("utf8"))
        except:
            raise ValueError('%s must be str' % (value_dict['parameter']))


def check_email_value(value_dict):
    """Function to check the email value, and return the value."""
    try:
        validate_email(value_dict['value'])
    except:
        raise ValueError(
            '%s is not in valid format.' % (value_dict['parameter']))
    return value_dict['value']
