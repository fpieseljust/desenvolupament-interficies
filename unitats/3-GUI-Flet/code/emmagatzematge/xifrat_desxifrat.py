import os
import flet.security as ft_sec

contrasenya = os.getenv("MY_APP_SECRET_KEY")
text_sense_xifrar = "Este és un missatge secret!"
text_xifrat = ft_sec.encrypt(text_sense_xifrar, contrasenya)

print(f"\nMissatge xifrat: {text_xifrat}\n")

text_desxifrat = ft_sec.decrypt(text_xifrat, contrasenya)
print(f"Missatge desxifrat: {text_desxifrat}\n")

if text_sense_xifrar == text_desxifrat:
    print("El missatge s'ha desxifrat correctament!")