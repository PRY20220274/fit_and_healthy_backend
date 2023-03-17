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


def get_access():
    return make_response(
        {
            'message': 'Access of the google account of the user were saved'
        }, 
        201
    )
