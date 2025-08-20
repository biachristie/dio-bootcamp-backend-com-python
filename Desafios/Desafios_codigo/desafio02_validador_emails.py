# Entrada do usuário
email = input().strip()

# TODO: Verifique as regras do e-mail:

if email != "" \
    and email.count(" ") == 0 \
    and email.count("@") == 1 \
    and not email.startswith("@") \
    and not email.endswith("@") \
    and not email.count("@") > 1 \
    and (email[-10:] == "@gmail.com" or email[-12:] == "@outlook.com"):
    print("E-mail válido")

else:
    print("E-mail inválido")