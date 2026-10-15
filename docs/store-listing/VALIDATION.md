# Validación de web y ficha — 15 de octubre de 2026

- Se generaron seis páginas estáticas, en español, inglés y francés, sin servicio de traducción remoto.
- Se verificaron idioma HTML, un título principal por página, iconos, alternativas de imágenes, enlaces locales, anclas y reproducción exacta del generador.
- Se comprobó el tamaño y formato del PNG original de launcher antes de incorporarlo al sitio. No se modificó la imagen.
- Se comprobaron los límites de los textos de Play:

| Idioma | Nombre /30 | Breve /80 | Completa /4000 |
| --- | --- | --- | --- |
| es-419 | 23 | 79 | 2544 |
| en-US | 23 | 73 | 2304 |
| fr-FR | 25 | 78 | 2879 |

- `git diff --check` pasó.
- La inspección visual en navegador local no pudo ejecutarse: Playwright estaba instalado, pero faltaba Chromium; la descarga del ejecutable devolvió archivos truncados. No se declara aprobada una auditoría visual responsive, Lighthouse ni QA física.
- Queda pendiente inspeccionar las páginas publicadas a 320 px, tablet y escritorio, el selector de idioma y los desplegables de preguntas. Los enlaces y la estructura sí fueron comprobados automáticamente.
- No se modificaron Play Console, AdMob, el repositorio de la aplicación, sus ramas ni su candidato. No se subieron capturas o videos ni se activaron campañas pagadas.
- El contenido de la próxima actualización procede del cierre de Atelier30 comunicado por el usuario. Antes de copiar la ficha a Play, debe contrastarse con el AAB concreto a publicar.
- Las traducciones han recibido revisión automática de consistencia, no revisión humana nativa.
- Los intentos iniciales de escritura devolvieron `403 Resource not accessible by integration`. Tras renovar la autorización, GitHub aceptó la creación del recurso de imagen original. La publicación utiliza un único commit sobre la revisión base `2dcb37c2b187a610831c04e05a58329fbde57853`, conservando `app-ads.txt` sin cambios. La disponibilidad de GitHub Pages se comprueba después de actualizar la rama; no sustituye la inspección visual pendiente.
