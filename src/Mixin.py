class LoggingMixin:
    def __init__(self, *args, **kwargs):
        class_name = self.__class__.__name__
        params = ', '.join(repr(arg) for arg in args)
        params += ', ' + ', '.join(f"{k}={v!r}" for k, v in kwargs.items())
        print(f"Создан объект класса {class_name} с параметрами: {params}")