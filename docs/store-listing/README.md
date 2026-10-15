# Ficha de Atelier Tools — preparación del 15 de octubre de 2026

## Alcance y estado

Textos preparados para el candidato Atelier30, según el cierre comunicado por su responsable: `dd1e474fe0f3c356d1a4eaaae52b9bfc56f5a2ce`. No se ha accedido a ese worktree Windows desde esta revisión. La rama remota de la aplicación está en una revisión anterior (`c11d3978355eae5c3eaa9e93739239184cc3a157`, versión declarada 1.0.0+1); no sustituye a la auditoría del AAB que se vaya a subir.

Las descripciones de `listing.json` son borradores listos para copiar cuando se confirme que el AAB distribuido incluye las funciones descritas. No deben sustituir la ficha de una versión antigua que no las contenga. No se ha editado Play Console ni contratado publicidad.

La interfaz de la app en tres idiomas sigue pendiente del resultado de Atelier31. Las fichas están traducidas, pero no afirman que la interfaz ya lo esté. Tras comprobarla en el APK final se podrá añadir esa disponibilidad a las tres descripciones. La web sí incluye páginas estáticas en los tres idiomas.

## Dónde pegar cada dato

Play Console → Atelier Tools → Aumentar usuarios → Presencia en Google Play → Fichas de Play Store → Ficha principal (los nombres pueden variar).

1. Nombre: campo `title` del idioma correspondiente.
2. Descripción breve: campo `short_description`.
3. Descripción completa: campo `full_description`.
4. Gestionar traducciones → Seleccionar idiomas: Español (Latinoamérica), English (United States), Français (France).
5. Recursos gráficos: conservar los originales que representen la versión final. La web y este documento no contienen capturas finales recuperadas ni un video promocional nuevo.

Los límites comprobados son 30 caracteres para nombre, 80 para descripción breve y 4000 para descripción completa. `tools/check_site.py` informa de los recuentos.

## Configuración general propuesta

| Campo | Propuesta o dato |
| --- | --- |
| Tipo | Aplicación |
| Categoría | Productividad |
| Etiquetas | Elegir sólo etiquetas disponibles y pertinentes para PDF, documentos, escaneo y QR; no inventar etiquetas que no ofrezca la consola |
| Nombre del desarrollador | MT-Corp, si coincide con el perfil real verificado; no modifica la identidad legal exigida por Google |
| Correo de asistencia | mtcorp0505@gmail.com, conservado de la política existente |
| Sitio web | https://mt-corp.github.io/ |
| Política de privacidad | https://mt-corp.github.io/privacy.html |
| Contiene anuncios | Sí |
| Registro o inicio de sesión | No, según el candidato comunicado |
| Compras dentro de la app | No deducirlas de Founder/Premium; comprobar si existe Google Play Billing en el AAB final |
| Precio | Conservar el estado real de la app; un desbloqueo con anuncios no equivale por sí solo a una compra |
| Público objetivo, IARC y funciones especiales | Responder el cuestionario real; no inventar edades, calificaciones o certificaciones |
| Acceso para revisores | Explicar el acceso real a herramientas restringidas. No publicar códigos Founder ni fabricar recompensas |
| Países | Decisión independiente de los idiomas. Revisar privacidad/UMP antes de ampliar, especialmente a Francia y Estados Unidos |

## Recursos visuales

- Icono de Play: PNG 512 × 512, máximo 1024 KB; utilizar el maestro real de la app, no ampliar el pequeño icono web como sustituto de un maestro.
- Gráfico de funciones: 1024 × 500, JPEG o PNG de 24 bits sin alfa.
- Capturas: al menos dos en total; máximo ocho por tipo de dispositivo. JPEG o PNG de 24 bits sin alfa, lados entre 320 y 3840 px y relación máxima 2:1.
- Preparar capturas con la interfaz real del APK que se publicará: inicio, PDF, anotación de copia externa, firma, QR, escaneo y Office. No mostrar proyectos personales, anuncios reales pulsados ni funciones futuras.
- Video: enlace de un video de YouTube público o no listado, sin restricción de edad, con inserción permitida y anuncios desactivados. No se carga el MP4 directamente en la ficha. Usar mayoritariamente interfaz real; un montaje cinematográfico puede reservarse para redes.
- Capturas y video en español primero. Preparar equivalentes en inglés y francés después de comprobar esos idiomas en la app. No simularlos superponiendo botones que no existan.

## Seguridad de los datos: verificar, no copiar a ciegas

La declaración debe describir el AAB final y todos sus SDK, no sólo el procesamiento local de documentos. Las categorías previstas para AdMob son ubicación aproximada inferida de IP, interacciones, registros de fallos, diagnósticos e identificadores. Google también declara recopilación técnica de ML Kit para diagnóstico/análisis. Su recogida no se confunde con el contenido OCR.

No afirmar ausencia total de red, anonimato, tratamiento exclusivamente temporal, borrado automático a 90 días ni recogida opcional sin pruebas. El consentimiento para personalización no demuestra que todos los usuarios puedan detener toda transmisión. Comprobar la versión nativa exacta y la presencia de adaptadores de mediación.

La política contiene información sobre proveedores y controles, pero no crea un servicio de borrado de registros de Google por correo. No cambia por sí sola la respuesta del formulario sobre solicitudes de eliminación.

No hay una aprobación individual identificada para Data Safety en la información aportada. No registrar «aprobado» por inferencia. La revisión de Google no se sustituye por esta preparación técnica.

## Futuro: excluido de los textos de venta actuales

- Interfaz de la app en español, inglés y francés: en implementación, pendiente de cierre.
- IA propia generativa: investigación, no integrada ni validada.
- Generación educativa para MaClasse: otro producto; no anunciarla como función de Atelier.
- Intersticial con recompensa nuevo: deshabilitado.
- Animaciones y compatibilidad completa de presentaciones externas: no prometidas.

## Privacidad y obligaciones abiertas

La web conserva únicamente el correo público de soporte; no añade teléfono ni nombre personal. Esto no puede ocultar la identidad legal que Google Play deba mostrar por sus propias reglas.

Se han conservado `app-ads.txt` y sus datos sin cambios. El icono web es una copia del recurso original de launcher del repositorio privado de la app; no requiere que el visitante acceda a ese repositorio.

Antes de publicar el AAB, Codex debe cerrar las obligaciones pendientes de Liberation Sans y avisos transitivos nativos que figuran en la fase30. Añadir el nombre del proveedor en la política de privacidad no sustituye sus avisos de licencia. Este documento no certifica cumplimiento jurídico ni aprobación de la tienda.

## Fuentes de referencia

- https://support.google.com/googleplay/android-developer/answer/9859152?hl=es
- https://support.google.com/googleplay/android-developer/answer/9866151?hl=en
- https://support.google.com/googleplay/android-developer/answer/9844778?hl=es
- https://support.google.com/googleplay/android-developer/answer/7550024?hl=es
- https://developers.google.com/admob/android/privacy/play-data-disclosure
- https://developers.google.com/ml-kit/android-data-disclosure
- https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement

## Reproducción

Python 3, sin dependencias externas:

```sh
python tools/build_pages.py
python tools/check_site.py
python -m http.server 8765
```

Abrir `/`, `/privacy.html`, `/en/`, `/en/privacy.html`, `/fr/` y `/fr/privacy.html`. Las páginas se sirven desde la raíz de GitHub Pages. Cambiar el idioma no necesita guardar una preferencia ni enviar datos a un servicio de traducción.
