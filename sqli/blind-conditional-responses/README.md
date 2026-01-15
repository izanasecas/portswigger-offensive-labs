# Blind SQL Injection with Conditional Responses

Este laboratorio de **PortSwigger Web Security Academy** presenta una **inyección SQL a ciegas** donde el resultado de la consulta no se devuelve directamente ni se muestran errores SQL.

La única diferencia observable en la respuesta es la aparición del mensaje **"Welcome back"** cuando la consulta inyectada devuelve al menos una fila, lo que permite explotar la vulnerabilidad mediante **respuestas condicionales**.

El objetivo es extraer la contraseña del usuario `administrator` y autenticarse en la aplicación.

---

## 🎯 Descripción del escenario

- La aplicación utiliza una cookie `TrackingId` para analíticas.
- El valor de esta cookie se inserta directamente en una consulta SQL vulnerable.
- No se muestran errores ni resultados de la consulta.
- La aplicación responde con el mensaje **"Welcome back"** si la consulta retorna alguna fila.
- Existe una tabla `users` con las columnas:
  - `username`
  - `password`

Este comportamiento permite inferir valores **carácter a carácter** mediante condiciones booleanas.

---

## 🔍 Reconocimiento

Durante el análisis inicial:

- La funcionalidad principal (tienda online y filtros) no presenta inyección SQL directa.
- Al interceptar la petición con **Burp Suite**, se observa que la cookie `TrackingId` es procesada por el backend.
- Modificando su valor, es posible alterar el comportamiento de la respuesta del servidor.

Ejemplo de payload válido probado manualmente:

```sql
AND SUBSTRING((SELECT password FROM users WHERE username='administrator'),1,1)='b'
Si la condición es verdadera, el mensaje "Welcome back" aparece en la respuesta.

```

⚙️ Enfoque de explotación
Debido a la naturaleza ciega de la vulnerabilidad, se automatiza el proceso mediante un script en Python que:

Itera posición por posición sobre la contraseña.

Prueba caracteres alfanuméricos.

Infiere el valor correcto cuando la respuesta contiene el mensaje esperado.

Construye la contraseña completa carácter a carácter.

Este enfoque replica un ataque realista, similar al que podría ejecutarse contra una aplicación en producción con validaciones deficientes.

🧠 Conclusiones técnicas

Las inyecciones SQL a ciegas siguen siendo críticas incluso sin errores visibles.

Mensajes condicionales aparentemente inocuos pueden filtrar información sensible.

Este tipo de vulnerabilidad no siempre es detectada por herramientas automáticas.

La validación de entradas y el uso de consultas parametrizadas siguen siendo esenciales.

⚠️ Aviso legal

Este material ha sido desarrollado exclusivamente con fines educativos y para su uso en entornos de laboratorio controlados.

No debe utilizarse contra sistemas sin autorización expresa.

👤 Autor

Izan García
Pentester Freelance | Seguridad Ofensiva

Portfolio: https://izanasecas.github.io/izanasecas/

LinkedIn: https://www.linkedin.com/in/izanasecas/

Hack The Box: https://app.hackthebox.com/profile/1015013