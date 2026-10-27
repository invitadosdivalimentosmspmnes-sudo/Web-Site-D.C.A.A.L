# Portal de Información — División de Calidad de Alimentos, Agua y Laboratorio

Sitio estático de 8 páginas, generado a partir de `PROMPT_PORTAL_DE_INFORMACION.pdf` y los
archivos de `PORTAL DE INFORMACION.zip`.

## Cómo verlo
Abrí `index.html` en el navegador (doble clic), o serví la carpeta con cualquier servidor
estático, por ejemplo:

```
cd site
python3 -m http.server 8080
```

y visitá `http://localhost:8080`.

## Estructura
```
index.html                     Página de inicio
ubicacion-y-contactos.html     Contacto, mapa (LACEPMI), áreas, sectores, residencia
rne-y-rnpa.html                Registro Nacional (RNE / RNPA) + descargas
registro-de-artesanales.html   Registro Provincial (RPEA / RPAA) + descargas
capacitaciones.html            Alta de capacitador + ciclo 2026
links-de-interes.html          Enlaces externos oficiales (SIFeGA, CAA, Boletín, Digesto)
buscadores.html                Buscadores oficiales (SIFeGA / ANMAT)
noticias-y-avisos.html         Noticias

style.css                      Sistema de diseño completo (variables, componentes)
main.js                        Header con scroll y animaciones reveal
logo.png                       Isologo Misiones Gobierno + Ministerio de Salud Pública
<trámite>-<archivo>            Los 40 archivos descargables en la raíz, con prefijo
                                de trámite para evitar nombres duplicados.

build.py, generate*.py         Scripts Python que generan las 8 páginas HTML.
                                Volvé a correr `python3 generate.py && python3 generate2.py
                                && python3 generate3.py` desde /site si necesitás
                                regenerar el sitio tras editar contenido.
```

## Qué se corrigió en esta revisión
1. **Descargas**: se detectó que las carpetas y archivos originales tenían espacios,
   acentos y paréntesis en sus nombres, lo cual provoca el error "Este archivo no se
   encontró aquí" en la mayoría de los hostings estáticos (problemas de normalización
   Unicode NFC/NFD y de percent-encoding entre sistemas operativos). Los 40 archivos
   usan nombres ASCII con prefijo de trámite y se encuentran en la raíz; los enlaces
   conservan el atributo `download` sin forzar la apertura de otra pestaña.
2. **Enlaces de interés y buscadores**: ya no son placeholders. Apuntan a las páginas
   oficiales reales (verificadas por búsqueda web): Plataforma SIFeGA de Misiones,
   Código Alimentario Argentino (ANMAT), Boletín Oficial de Misiones, Digesto Jurídico
   de Misiones, y los 6 buscadores oficiales de SIFeGA/ANMAT (RNE, RNPA, ALG,
   Directores Técnicos, Capacitadores/Manipuladores, Registros Provinciales). Todos
   con `target="_blank"` y `rel="noopener noreferrer"`.
3. **Correos**: los 10 enlaces `mailto:` están verificados y funcionando.
4. **Ubicación**: el texto y el mapa embebido ahora apuntan puntualmente al
   **Laboratorio Central de la Provincia de Misiones (LACEPMI)**, con su nombre
   destacado como encabezado de la sección y como primera línea de la dirección.
5. **Header**: los títulos del menú de navegación ahora son blancos y uniformes
   (antes tenían un color distinto por sección).

Todo el resto del diseño visual (paleta oscura, tarjetas, banners por color de
sección, animaciones) se mantuvo intacto.

