# Account Lockout User Enumeration & Bypass

## 📌 Descripción

Este PoC explota una **vulnerabilidad de enumeración de usuarios** causada por una **implementación defectuosa del bloqueo de cuentas**.

La aplicación bloquea cuentas tras múltiples intentos fallidos, pero presenta un fallo de lógica que permite:
- Identificar usuarios válidos
- Realizar fuerza bruta de contraseñas incluso cuando la cuenta está bloqueada

🎯 Objetivo: enumerar un usuario válido, obtener su contraseña y acceder a su página de cuenta.

---

## 🔍 Enumeración de usuarios

La aplicación dispone de:
- Un blog público
- Un panel de inicio de sesión sin credenciales iniciales

Se inicia un ataque de fuerza bruta usando una wordlist proporcionada.

Inicialmente:
- Las respuestas parecen idénticas para todos los usuarios
- No se observa enumeración directa por mensajes de error

---

## ⚠️ Detección del fallo lógico

Probando múltiples contraseñas incorrectas **para el mismo usuario**, se observa que:
- Solo algunos usuarios activan el bloqueo de cuenta tras varios intentos
- Esto permite identificar usuarios válidos por su comportamiento distinto

De esta forma se identifica el usuario válido


---

## 💥 Fuerza bruta con cuenta bloqueada

Analizando el flujo de autenticación se detecta que:
- El sistema **permite validar la contraseña incluso cuando la cuenta está bloqueada**
- Si la contraseña es correcta, no se devuelve ningún mensaje de error

Esto permite realizar fuerza bruta sobre el usuario bloqueado hasta encontrar la contraseña válida.

---

## 🧠 Impacto

Este fallo permite:
- Enumerar usuarios válidos sin mensajes explícitos
- Eludir mecanismos de bloqueo de cuentas
- Comprometer cuentas protegidas por controles aparentemente robustos

Es un ejemplo claro de **fallo de lógica en autenticación**, no de falta de controles.

---

## 📚 Referencias

- PortSwigger Web Security Academy  
- OWASP Top 10 – Identification and Authentication Failures

