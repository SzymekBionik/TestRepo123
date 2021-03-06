class SlumberBaseException(Exception): ...

class SlumberHttpBaseException(SlumberBaseException):
    def __init__(self, *args, **kwargs) -> None: ...

class HttpClientError(SlumberHttpBaseException): ...
class HttpNotFoundError(HttpClientError): ...
class HttpServerError(SlumberHttpBaseException): ...
class SerializerNoAvailable(SlumberBaseException): ...
class SerializerNotAvailable(SlumberBaseException): ...
class ImproperlyConfigured(SlumberBaseException): ...
