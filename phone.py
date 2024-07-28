from field import Field


class Phone(Field):
    def __init__(self, phone):
        self.value = self.validate_phone(phone)

    def validate_phone(self, phone):
        if not phone.isdigit():
            raise ValueError("Phone number must contain only numbers")
        
        if len(phone) != 10:
            raise ValueError("Phone number must contain 10 digits")

        return phone
