# Blind SQL Injection – Time-Based (PostgreSQL)

## 📌 Descripción

Este PoC explota una **inyección SQL a ciegas basada en tiempo** en una aplicación vulnerable de PortSwigger.

La aplicación utiliza una cookie de tracking (`TrackingId`) que es procesada dentro de una consulta SQL.  
El resultado de la consulta **no se devuelve**, no hay diferencias por condiciones verdaderas/falsas y **no se muestran errores**, lo que descarta técnicas clásicas de SQLi a ciegas.

Sin embargo, la consulta se ejecuta de forma síncrona, permitiendo **inferir información mediante retrasos en la respuesta**.

La base de datos es **PostgreSQL** y contiene una tabla `users` con los campos `username` y `password`.

🎯 Objetivo: obtener la contraseña del usuario `administrator`.

---

## 🔍 Técnica utilizada

- Blind SQL Injection
- Time-based inference
- Base de datos PostgreSQL
- Inyección vía cookies

Se utilizan funciones de delay (`pg_sleep`) para distinguir condiciones verdaderas y falsas en función del tiempo de respuesta.

---

🤖 Automatización

Se incluye un script en Python que:

Mide el tiempo de respuesta del servidor

Evalúa condiciones booleanas mediante delays

Extrae la contraseña carácter a carácter

⚠️ Aviso legal

Este material ha sido desarrollado exclusivamente con fines educativos y para su uso en entornos de laboratorio controlados.

No debe utilizarse contra sistemas sin autorización expresa.

👤 Autor

Izan García Pentester Freelance | Seguridad Ofensiva

Portfolio: https://izanasecas.github.io/izanasecas/

LinkedIn: https://www.linkedin.com/in/izanasecas/

Hack The Box: https://app.hackthebox.com/profile/1015013
