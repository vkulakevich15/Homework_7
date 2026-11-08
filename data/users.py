import uuid

VALID_USER={
    "email":"123@org.org",
    "password":"!@#qweASD123 "
}

VALID_USER1={
    "email": "alexandra_test@test.com",
    "password": "!@#$%QWEASDzxc.123"
}


INVALID_USER={
    "email":"test@t.t",
    "password":"test"
}


REGISTER_USER = {
    "first_name": "Alexandra",
    "last_name": "Sidorovich",
    "dob": "1990-01-01",
    "country": "Armenia",
    "postal_code": "220000",
    "house_number": "42",
    "street": "Lenina",
    "city": "Minsk",
    "state": "Minsk",
    "phone": "291234567",
    "email": f"{uuid.uuid4().hex[:8]}@mail.com",
    "password": f"!1Qa_{uuid.uuid4().hex[:6]}"
}
