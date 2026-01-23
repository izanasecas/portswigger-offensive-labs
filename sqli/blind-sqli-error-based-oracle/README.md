# Blind SQL Injection –  Blind SQL injection with conditional errors  (Oracle)

## 📌 Descripción

Este PoC explota una **inyección SQL a ciegas basada en errores** en una aplicación vulnerable de PortSwigger.

La aplicación procesa el valor de la cookie `TrackingId` dentro de una consulta SQL.  
Aunque no devuelve el resultado de la consulta ni muestra diferencias entre condiciones verdaderas o falsas, **sí responde con un error cuando la consulta falla**, lo que permite explotar la vulnerabilidad.

La base de datos es **Oracle** y contiene una tabla `users` con los campos `username` y `password`.

🎯 Objetivo: obtener la contraseña del usuario `administrator`.

---

## 🔍 Técnica utilizada

- Blind SQL Injection
- Error-based inference
- Base de datos Oracle
- Inyección vía cookies

Se utiliza una condición `CASE WHEN` para provocar errores SQL (`TO_CHAR(1/0)`) únicamente cuando la condición evaluada es verdadera.

---

## 💥 Explotación

Mediante pruebas controladas, se puede extraer la contraseña carácter a carácter evaluando si la aplicación devuelve un error.

⚠️ Aviso legal

Este material ha sido desarrollado exclusivamente con fines educativos y para su uso en entornos de laboratorio controlados.

No debe utilizarse contra sistemas sin autorización expresa.

👤 Autor

Izan García Pentester Freelance | Seguridad Ofensiva

Portfolio: https://izanasecas.github.io/izanasecas/

LinkedIn: https://www.linkedin.com/in/izanasecas/

Hack The Box: https://app.hackthebox.com/profile/1015013
