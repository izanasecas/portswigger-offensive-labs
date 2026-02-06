# User Enumeration via Response Time (Authentication)

## 📌 Descripción

Este PoC explota una vulnerabilidad de **enumeración de usuarios basada en tiempos de respuesta** en un sistema de autenticación vulnerable de PortSwigger.

La aplicación devuelve respuestas idénticas tanto para usuarios válidos como inválidos.  
Sin embargo, el **tiempo de procesamiento varía ligeramente** cuando el nombre de usuario existe, permitiendo inferir su validez mediante mediciones de tiempo.

Una vez identificado un usuario válido, es posible realizar un ataque de fuerza bruta sobre su contraseña y acceder a la cuenta.

🎯 Objetivo: enumerar un usuario válido mediante tiempos de respuesta y obtener su contraseña.

---

## 🔍 Enumeración de usuarios

El formulario de inicio de sesión no muestra diferencias visibles en:
- Mensajes de error
- Códigos de estado
- Contenido de la respuesta

No obstante, al medir el tiempo de respuesta:
- Las peticiones con usuarios inválidos responden de forma más rápida
- Las peticiones con usuarios válidos tardan ligeramente más, incluso con contraseñas incorrectas

Este retraso se vuelve más notable al utilizar contraseñas deliberadamente largas.

---

## 🚧 Bypass de protección contra fuerza bruta

Durante la enumeración, la aplicación implementa un mecanismo básico de protección frente a múltiples intentos.

Este control puede eludirse utilizando la cabecera HTTP:

`X-Forwarded-For`


Asignando una IP diferente en cada petición, el servidor trata cada intento como una nueva fuente, permitiendo continuar con el ataque.

---

## 💥 Fuerza bruta de contraseña

Tras identificar un usuario válido, se realiza un ataque de fuerza bruta sobre su contraseña.

Dado que:
- No existe bloqueo de cuenta efectivo
- El rate limiting es evitable
- No se aplican delays progresivos

La contraseña puede obtenerse mediante un diccionario en un tiempo razonable.

---

## 🧠 Impacto

Este tipo de vulnerabilidad permite:
- Enumerar usuarios sin diferencias visibles en la respuesta
- Eludir protecciones simples de rate limiting
- Facilitar ataques de account takeover

Incluso sin errores ni mensajes diferenciados, **el tiempo de respuesta puede filtrar información crítica**.

---

## 📚 Referencias

- PortSwigger Web Security Academy
- OWASP Top 10 – Identification and Authentication Failures

