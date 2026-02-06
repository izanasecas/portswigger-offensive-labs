# Weak Brute Force Protection – Counter Reset Bypass

## 📌 Descripción

Este PoC explota una **protección débil contra ataques de fuerza bruta** en el sistema de autenticación.

La aplicación implementa un contador de intentos fallidos y bloquea temporalmente el acceso tras varios errores consecutivos.  
Sin embargo, este contador puede **resetearse iniciando sesión correctamente con otra cuenta**, permitiendo realizar un ataque de fuerza bruta de forma indefinida.

🎯 Objetivo: obtener la contraseña del usuario víctima y acceder a su cuenta.

---

## 🔑 Credenciales conocidas

- Usuario controlado: `wiener`
- Contraseña: `peter`
- Usuario objetivo: `carlos`

---

## 🔍 Análisis del mecanismo de protección

Tras varios intentos de inicio de sesión fallidos:
- La aplicación bloquea temporalmente el formulario
- El bloqueo dura aproximadamente 1 minuto

Este comportamiento parece correcto a primera vista.

---

## ⚠️ Bypass del contador de intentos

Analizando la lógica del sistema se observa que:
- El contador de intentos fallidos **se asocia a la sesión actual**
- Al iniciar sesión correctamente y cerrar sesión, el contador se reinicia

Esto permite el siguiente flujo:

1. Realizar varios intentos fallidos contra el usuario objetivo
2. Iniciar sesión correctamente con una cuenta válida
3. Cerrar sesión
4. Repetir el proceso indefinidamente

---

## 💥 Fuerza bruta de contraseña

Usando este bypass:
- No existe un límite real de intentos
- El bloqueo nunca se mantiene de forma persistente
- Es posible probar contraseñas del diccionario hasta encontrar la correcta

Finalmente se obtiene la contraseña del usuario `carlos` y se accede a su cuenta.

---

## 🧠 Impacto

Este fallo permite:
- Eludir protecciones anti–fuerza bruta aparentemente correctas
- Comprometer cuentas sin necesidad de exploits complejos
- Realizar ataques persistentes sin levantar alertas inmediatas

Es un ejemplo claro de cómo **una mala implementación lógica invalida un control de seguridad**.

---

## 📚 Referencias

- PortSwigger Web Security Academy  
- OWASP Top 10 – Identification and Authentication Failures
