# Easy-Networking

NetPulse es una plataforma web avanzada de ciberseguridad diseñada para automatizar, gestionar y visualizar tareas de reconocimiento y auditoría de redes. La aplicación envuelve la potencia de la herramienta de consola **Nmap**, abstrayendo sus comandos y flags más avanzados detrás de una interfaz gráfica intuitiva, moderna y en tiempo real.

Gracias a una arquitectura asíncrona, NetPulse permite lanzar escaneos profundos de red sin bloquear la experiencia de usuario, transformando reportes de texto plano estructurados en dashboards visuales interactivos.

## 🎯 Objetivos del Proyecto

*   **Abstracción Visual de Nmap:** Traducir "flags ocultos" y complejos de la terminal (como técnicas de evasión de firewalls, scripts NSE de vulnerabilidades y escaneos sigilosos) a controles visuales (toggles, checkboxes).
*   **Procesamiento Asíncrono:** Gestionar escaneos concurrentes y de larga duración en segundo plano de manera eficiente, garantizando que la interfaz web siga respondiendo instantáneamente.
*   **Persistencia y Analítica:** Almacenar el histórico de auditorías en una base de datos relacional para analizar la evolución de la seguridad de los activos de red mediante gráficas.
*   **Interactividad en Tiempo Real:** Notificar al usuario el progreso del escaneo y la detección de hosts o puertos abiertos al momento, sin necesidad de refrescar la pantalla.

---

## 💻 Stack Tecnológico

El proyecto está diseñado combinando tecnologías de desarrollo web, bases de datos y redes a bajo nivel:

*   **Backend Core:** Python 3 + Flask (Application Factory & Blueprints)
*   **Gestión de Red:** Nmap (Motor nativo) + `python-nmap` (Wrapper)
*   **Arquitectura Asíncrona:** Celery (Task Queue) + Redis (Message Broker)
*   **Base de Datos:** PostgreSQL (Soporte para consultas relacionales y tipos de datos JSONB)
*   **Frontend:** HTML5, Tailwind CSS (Diseño Dark Mode enfocado a ciberseguridad) y Chart.js (Gráficas dinámicas)
*   **Comunicación en vivo:** Flask-SocketIO (WebSockets)

---

## 🔄 Flujo de Funcionamiento del Sistema

1.  **Configuración:** El usuario introduce un objetivo (IP o rango CIDR) en la interfaz web y activa los parámetros avanzados deseados (ej: Detección de OS, Scripts de Vulnerabilidad, Decoys).
2.  **Desencadenamiento:** Flask recibe la petición HTTP, registra la auditoría con estado "Pendiente" en PostgreSQL y delega la tarea pesada a la cola de **Celery**.
3.  **Ejecución:** El *Worker* de Celery (ejecutado con privilegios elevados) toma la tarea y arranca el escaneo binario de Nmap.
4.  **Actualización:** Conforme Nmap avanza o finaliza, el proceso actualiza la base de datos y envía señales mediante WebSockets para refrescar las gráficas del Dashboard del usuario en tiempo real.
5.  **Análisis:** El usuario inspecciona el reporte final filtrando por puertos abiertos, criticidad de servicios o vulnerabilidades encontradas.

---

## 🛠️ Próximos Pasos (Hoja de Ruta)

*   [ ] Fase 1: Configuración del entorno local (Instalación de Nmap nativo, Redis y Base de Datos).
*   [ ] Fase 2: Creación del Script de Prueba (PoC) en Python para validar la comunicación con Nmap.
*   [ ] Fase 3: Modelado de la base de datos en SQLAlchemy (Tablas de Escaneos, Hosts y Puertos).
*   [ ] Fase 4: Configuración e integración de Celery + Redis con Flask.
*   [ ] Fase 5: Desarrollo de las rutas de la API y las vistas del Frontend.
*   [ ] Fase 6: Implementación de la capa de tiempo real con WebSockets.
