users = {
    "admin": {
        "password": "admin123",
        "role": "admin"
    },

    "hr_user": {
        "password": "hr123",
        "role": "hr"
    },

    "finance_user": {
        "password": "finance123",
        "role": "finance"
    },

    "technical_user": {
        "password": "tech123",
        "role": "technical"
    },

    "employee": {
        "password": "emp123",
        "role": "employee"
    }
}

# AUTHENTICATION
def authenticate(username, password):

    user = users.get(username)

    if user and user["password"] == password:

        return user["role"]

    return None
