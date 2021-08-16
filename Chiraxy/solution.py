class ExceptionProxy:
    def __init__(self, msg, func):
        self.msg = msg
        self.function = func


def transform_exceptions(funcs):
    classes = list()

    for func in funcs:
        try:
            func()
            classes.append(ExceptionProxy('ok!', func))
        except Exception as e:
            classes.append(ExceptionProxy(str(e), func))

    return classes
