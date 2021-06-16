orig = [{
    "info": {
        "first_name": "John",
        "last_name": "M."
    },
    "code": "1"
},
    {
        "info": {
            "first_name": "Sara",
            "last_name": "B. R."
        },
        "code": "2"
    }]

new = [x["info"] for x in orig]

print(new)