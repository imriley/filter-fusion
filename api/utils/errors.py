class ApiBaseError(Exception):
    """
    Base class for API exceptions.
    """

class NoImageProvided(ApiBaseError):
    def __init__(self):
        super().__init__("No image was provided, you can either pass the image as a URL or a file.")

class InvalidImageUrl(ApiBaseError):
    def __init__(self):
        super().__init__("Provided URL is not a valid image URL.")