def validate_hello(greetings):
    hellos = [
        "hello",
        "ciao",
        "salut",
        "hallo",
        "hola",
        "ahoj",
        "czesc",
    ]
    res = [ele for ele in hellos if (ele in greetings.casefold())]
    return bool(res)


print(validate_hello("Hallo, wie geht's dir?"))
