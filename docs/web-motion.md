# Atelier web — selector e interacción espacial

15 de octubre de 2026. Base: `738fef8ee1739821c7e3c7244f6857e3f9eea599`.

## Cambios

- Inicio y privacidad en español, inglés y francés comparten un selector de idiomas Glass. Muestra nombres nativos, selección actual y rutas reales. No usa banderas como sustitutos de idiomas.
- El selector conserva la página al cambiar de idioma; permite Tab, Enter, flecha abajo, Escape y cierre al tocar fuera. Sin JavaScript conserva sus enlaces y apertura nativa.
- React se utiliza en tres islas previamente renderizadas: idioma, control de movimiento y escena interactiva. La información documental y la política se entregan completas en HTML.
- La escena usa planos CSS con perspectiva 3D, el icono original, reflejos, partículas y motivos documentales. Se puede girar mediante arrastre o flechas y centrar de nuevo. Los botones Documentos/QR/Firma cambian la composición. No es WebGL ni una simulación funcional de la aplicación. Se identifica como ilustración, sin inventar capturas de pantalla.
- Privacidad mantiene su texto completo sin planos de texto giratorios. El índice, el indicador de lectura y los encabezados facilitan la navegación.
- Movimiento reducido del sistema y pausa manual detienen los efectos. No se capturan sensores, cámara ni datos personales. Las animaciones se pausan fuera de pantalla y en segundo plano; el desplazamiento vertical sigue siendo nativo.
- No se añaden analítica, cookies, almacenamiento local o peticiones a un CDN. React, su código y sus avisos MIT se sirven desde el propio sitio.
- `app-ads.txt`, el icono original y los textos preparados para Play permanecen intactos. No se modifica la app Android ni Play Console.

## Reproducción

```sh
npm ci
npm run build
python tools/check_site.py
git diff --check
```

El bundle usa React/React DOM 19.3.1 y esbuild 0.28.2, fijados en `package-lock.json`. Los archivos de `assets/` y las seis páginas generadas se versionan: GitHub Pages no necesita instalar Node para servirlos.

Pruebas reales de navegador: instala Playwright como herramienta de QA y su Chromium compatible, o indica un ejecutable local:

```sh
ATELIER_CHROMIUM=/ruta/a/chromium node tools/check_browser.cjs
```

`ATELIER_QA_DIR` permite elegir dónde guardar capturas e informe. El script levanta y cierra su propio servidor local. No requiere servicios remotos ni una cuenta de prueba.

## Referencias consultadas

Se consultaron ideas y opiniones; no se copió el código de componentes de terceros.

- Usuarios de r/webdev, agosto de 2026: [Why is everything a dropdown now?](https://www.reddit.com/r/webdev/comments/1vnmyqj/why_is_everything_a_dropdown_now/). Comentarios sobre visibilidad y claridad cuando hay pocas opciones; opiniones, no estudio representativo.
- Usuarios de r/web_design, septiembre de 2026: [Overly animated sites show a lack of design skill](https://www.reddit.com/r/web_design/comments/1wcj9yw/overly_animated_sites_show_a_lack_of_design_skill/). Comentarios sobre exceso de animación y lectura; opiniones, no medición de este sitio.
- [USWDS: selector de tres o más idiomas](https://designsystem.digital.gov/patterns/select-a-language/three-or-more-languages/).
- [React: efectos y limpieza](https://react.dev/reference/react/useEffect).
- [MDN: planos tridimensionales](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-style).

## Límites

Las comprobaciones de navegador son de Chromium en un host, con tamaños de pantalla y preferencias simulados. No acreditan rendimiento de GPU, compatibilidad de Safari/Firefox, auditoría WCAG completa ni QA física del Moto o del iPhone. No se atribuye revisión humana nativa a las traducciones.


## Validación final

- 54 casos de Chromium: las seis páginas a 320, 390, 768, 1440, 2560 y 844 × 390; enlaces de idioma, Escape y flecha abajo, giro por teclado, centrado, pausa, progreso, JavaScript deshabilitado, movimiento reducido y texto al 200 %.
- Dos recorridos táctiles simulados adicionales: abrir/cerrar el selector, girar horizontalmente el objeto y desplazar verticalmente la página desde la propia escena. No equivalen a pruebas físicas.
- Sin errores de consola/ejecución ni solicitudes a servicios externos en la matriz instrumentada.
- Capturas de inicio, privacidad y selector inspeccionadas en móvil y escritorio. Se corrigieron un desbordamiento francés a 320 px, el salto de la puntuación del título y el ajuste de texto grande. La ruta sin JavaScript entrega controles estáticos utilizables.
- Bundle y páginas reproducidos byte a byte. Comprobación estructural de seis páginas, límites de ficha y `git diff --check` correctos.
- Se verificó igualdad exacta de todo el diccionario de textos y políticas frente a la base, además del icono, `app-ads.txt` y `listing.json`.
- [Informe de navegador](qa/web-motion/browser-report.json) y [recorridos táctiles](qa/web-motion/touch-report.json).

Para repetir los recorridos táctiles con el mismo entorno de Playwright:

```sh
ATELIER_CHROMIUM=/ruta/a/chromium node tools/check_touch.cjs
```
