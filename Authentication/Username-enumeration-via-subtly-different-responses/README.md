# Authentication Bruteforce via User Enumeration

## 📌 Descripción

Este PoC explota una vulnerabilidad de **enumeración de usuarios combinada con fuerza bruta de credenciales** en una aplicación web vulnerable de PortSwigger.

El sistema de autenticación devuelve mensajes de error aparentemente idénticos para usuarios válidos e inválidos.  
Sin embargo, un análisis más detallado de la respuesta permite identificar **pequeñas diferencias** que revelan cuándo un nombre de usuario existe en el sistema.

Una vez identificado un usuario válido, es posible realizar un ataque de fuerza bruta sobre su contraseña.

🎯 Objetivo: enumerar un usuario válido y obtener su contraseña para acceder a la cuenta.

---

## 🔍 Enumeración de usuarios

La aplicación dispone de un formulario de inicio de sesión que, a primera vista, parece correctamente protegido.

Durante un ataque inicial de fuerza bruta:
- Todas las respuestas parecen iguales
- No hay cambios evidentes en el contenido
- No existen códigos de error diferenciados

Al analizar el **mensaje de error completo**, se detecta una **ligera variación textual** cuando el usuario existe, lo que permite confirmar la validez del nombre de usuario.

Este tipo de fallo es común cuando:
- Se reutilizan mensajes genéricos
- No se normalizan correctamente las respuestas del backend

---

## 💥 Fuerza bruta de contraseña

Una vez identificado el usuario válido, se lanza un segundo ataque de fuerza bruta únicamente contra ese usuario.

Dado que:
- No existe limitación de intentos
- No hay bloqueo de cuenta
- No se implementan delays

Es posible obtener la contraseña mediante un diccionario en un tiempo reducido.

---

## 🧠 Impacto

Este tipo de vulnerabilidad permite:
- Enumerar usuarios válidos
- Comprometer cuentas con credenciales débiles
- Facilitar ataques posteriores (account takeover)

Incluso cuando los mensajes de error parecen genéricos, **pequeñas diferencias pueden filtrar información crítica**.

---

## 📚 Referencias

- PortSwigger Web Security Academy
- OWASP Top 10 – Identification and Authentication Failures
