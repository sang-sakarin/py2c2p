from functools import wraps
from .error import PaymentGatewayRedirectError


def check_in_kwargs(kwargs_names):
    """
    check if the wrapped function's class have the specified kwargs
    :param kwargs_names: array of kwargs names to check
    :return:
    """
    def layer(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            for kwarg in kwargs_names:
                if kwarg in kwargs and kwargs.get(kwarg) == '':
                    raise PaymentGatewayRedirectError("{0} must be defined and not empty".format(kwarg))
            return func(self, *args, **kwargs)
        return wrapper
    return layer
