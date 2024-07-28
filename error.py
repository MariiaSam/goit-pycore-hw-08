from functools import wraps

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return f"{str(e)}"
        except TypeError:
            return "Incorrect number of arguments"
        except KeyError:
            return "Contact not found"
        except Exception as e:
            return f"{str(e)}"

    return inner