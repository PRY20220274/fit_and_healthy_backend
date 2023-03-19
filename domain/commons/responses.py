from flask import request, make_response


def user_not_found():
    return make_response(
        {
            'message': 'No user found with that email'
        }, 
        401
    )


def get_token(token):
    return make_response(
        {
            'token': token
        }, 
        200
    )


def wrong_credentials():
    return make_response(
        {
            'message': 'The credentials are wrong'
        }, 
        401
    )


def user_exists():
    return make_response(
        {
            'message': 'User already exists. Please Log in'
        }, 
        202
    )


def access_saved():
    return make_response(
        {
            'message': 'Access of the google account of the user were saved'
        }, 
        201
    )


def access_denied():
    return make_response(
        {
            'message': 'Access of the google account couldn t save'
        }, 
        400
    )


def existing_access():
    return make_response(
        {
            'message': 'The user already has access credentials'
        }, 
        200
    )


def blocked_information():
    return make_response(
        {
            'message': 'Google Fit information could not be accessed'
        }, 
        200
    )


def iot_data_saved():
    return make_response(
        {
            'message': 'Google Fit Data of the user were saved'
        }, 
        201
    )
