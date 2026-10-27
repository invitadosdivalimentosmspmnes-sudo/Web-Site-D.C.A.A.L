#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from build import page, write, dl, dl_item, FORM_URL

CAP_CAT = "capacitaciones"

# =========================================================
# PAGE 5: CAPACITACIONES
# =========================================================
hero_cap = '''    <div class="hero hero-green reveal">
      <p class="hero-eyebrow line3">DIVISIÓN DE CALIDAD DE ALIMENTOS, AGUA Y LABORATORIO</p>
      <h1 class="hero-title">CAPACITADOR NACIONAL EN MANIPULACIÓN SEGURA DE ALIMENTOS</h1>
    </div>'''

cap_items = [
    ("1- Modelos de Notas Alta Capacitador", dl(CAP_CAT, "01-modelos-notas-alta-capacitador.docx")),
    ("2- NORMATIVA - Anexo II_Art21", dl(CAP_CAT, "02-normativa-anexo-ii-art21.pdf")),
]

body_cap = '''    <section class="section">
      <div class="card card-accent-green reveal" style="max-width:520px;">
        <p class="card-label green">Area de Capacitaciones</p>
        <a class="card-meta link-interactive" href="mailto:mspdivalimentoscapacitaciones@gmail.com" style="font-size:15px;">mspdivalimentoscapacitaciones@gmail.com</a>
        <p class="card-meta" style="margin-top:12px; font-style:italic;">Responsables:<br>Bioq. Mgter. Myriam García<br>Tec. Brom. Valeria Caruso</p>
      </div>
    </section>

    <section class="section" style="padding-top:0;">
      <a href="#descargas-cap" class="download-banner green reveal">
        <span>DESCARGUE LOS INSTRUCTIVOS DE SU INTERÉS</span>
        <span class="cloud-icon">&#9729;&#8681;</span>
      </a>
    </section>

    <section class="section" style="padding-top:0;">
      <div class="card card-accent-green reveal" style="max-width:520px;">
        <p class="card-label green">Trámite de Alta</p>
        <p class="card-body">CAPACITADOR NACIONAL DE MANIPULACIÓN SEGURA DE ALIMENTOS</p>
      </div>
    </section>

    <hr class="divider-soft">

    <section class="section" id="descargas-cap">
      <h2 class="section-title accent-green">CAPACITADOR NACIONAL EN MANIPULACIÓN SEGURA DE ALIMENTOS</h2>
      <p class="section-lead" style="font-style:italic;">DIVISIÓN DE CALIDAD DE ALIMENTOS, AGUA Y LABORATORIO</p>
      <div class="download-list">
{cap}
      </div>
      <p class="welcome-hint" style="margin-top:16px;">DESCARGUE EL INSTRUCTIVO DE SU INTERÉS</p>
    </section>

    <hr class="divider-soft">

    <section class="section">
      <div class="attention-box reveal">
        <p class="attention-title">ATENCIÓN:</p>
        <p>La documentación de este trámite debe ser presentada en forma PRESENCIAL en nuestras oficinas</p>
        <p style="margin-bottom:2px;">De no ser posible:</p>
        <ul>
          <li>a) Enviar con un Tercero , la Nota Original de SOLICITUD DE ACCESO AL SIFeGA y además la AUTORIZACIÓN PARA EL OTORGAMIENTO DE LA CLAVE A TERCEROS (Certificación ante Escribano, Juez de Paz).</li>
          <li>b) Envíar por Correo Argentino la Nota Original de SOLICITUD DE ACCESO AL SIFeGA. (Certificación ante Escribano, Juez de Paz).</li>
        </ul>
      </div>
    </section>

    <hr class="divider-soft">

    <section class="section">
      <h2 class="section-title accent-green">CAPACITACIONES PRESENCIALES Y VIRTUALES</h2>
      <p class="section-lead" style="font-style:italic;">DIVISIÓN DE CALIDAD DE ALIMENTOS, AGUA Y LABORATORIO</p>
      <p class="welcome-hint" style="margin:6px 0 24px;">PROGRAMA ANUAL DE CAPACITACIONES A PERSONAL RELACIONADO A LA PRODUCCION, ELABORACION Y CONTROL DE ALIMENTOS &mdash; CICLO 2026 &mdash; AREA DE CAPACITACIONES VIRTUALES Y PRESENCIALES</p>

      <div class="cards-grid cols-2">
        <div class="card card-accent-green reveal">
          <p class="card-label green">Consultas sobre esta sección</p>
          <a class="card-meta link-interactive" href="mailto:capacitaciones.divalimentosmsp@gmail.com" style="font-size:15px;">capacitaciones.divalimentosmsp@gmail.com</a>
          <p class="card-meta" style="margin-top:12px; font-style:italic;">Responsables:<br>Bioq. Mgter. Myriam García</p>
        </div>

        <div class="news-card reveal">
          <p class="news-date">13-05-2026</p>
          <p class="news-title">CAPACITACIONES ANUALES 2026</p>
          <p class="news-body">La División da inicio a su Ciclo de Capacitaciones, invitando a la participar de la primer capacitación gratuita:</p>
          <p class="news-course-name">&ldquo;GUÍA DE TRÁMITE PARA EL REGISTRO NACIONAL DE CAPACITADORES EN MANIPULACIÓN SEGURA DE ALIMENTOS, por Art. 21 mediante el uso del Sistema de Información Federal para la Gestión del Control de Alimentos (SIFeGA)&rdquo;</p>
          <a class="btn-primary" href="{form}" target="_blank" rel="noopener noreferrer">Más información e inscripción</a>
        </div>
      </div>
    </section>
'''.format(cap="\n".join(dl_item(l, h) for l, h in cap_items), form=FORM_URL)

write("capacitaciones.html", page("capacitaciones.html", "Capacitaciones", hero_cap, body_cap))


# =========================================================
# PAGE 6: LINKS DE INTERÉS
# =========================================================
hero_links = '''    <div class="hero hero-teal reveal">
      <p class="hero-eyebrow line3">DIVISIÓN DE CALIDAD DE ALIMENTOS, AGUA Y LABORATORIO</p>
      <h1 class="hero-title">LINKS DE INTERÉS</h1>
    </div>'''

body_links = '''    <section class="section">
      <div class="buscadores-grid">
        <a href="https://salud.misiones.gob.ar/si-fe-ga/" target="_blank" rel="noopener noreferrer" class="plus-card teal reveal">
          <span class="plus-circle">+</span>
          <p class="plus-eyebrow">Acceso</p>
          <p class="plus-title">Plataforma SiFeGA</p>
          <p class="plus-sub">(Sistema de Información Federal para la Gestión del Control de los Alimentos)</p>
        </a>
        <a href="https://www.argentina.gob.ar/anmat/codigoalimentario" target="_blank" rel="noopener noreferrer" class="plus-card teal reveal">
          <span class="plus-circle">+</span>
          <p class="plus-eyebrow">Acceso</p>
          <p class="plus-title">Código Alimentario Argentino</p>
          <p class="plus-sub">(LEY 18.284)</p>
        </a>
        <a href="https://www.boletin.misiones.gov.ar/" target="_blank" rel="noopener noreferrer" class="plus-card teal reveal">
          <span class="plus-circle">+</span>
          <p class="plus-eyebrow">Acceso</p>
          <p class="plus-title">Boletín Oficial Misiones</p>
        </a>
        <a href="https://www.digestomisiones.gob.ar/" target="_blank" rel="noopener noreferrer" class="plus-card teal reveal">
          <span class="plus-circle">+</span>
          <p class="plus-eyebrow">Acceso</p>
          <p class="plus-title">Digesto Jurídico Misiones</p>
        </a>
      </div>
    </section>
'''

write("links-de-interes.html", page("links-de-interes.html", "Links de interés", hero_links, body_links))


# =========================================================
# PAGE 7: BUSCADORES
# =========================================================
hero_buscadores = '''    <div class="hero hero-teal reveal">
      <p class="hero-eyebrow line3">DIVISIÓN DE CALIDAD DE ALIMENTOS, AGUA Y LABORATORIO</p>
      <h1 class="hero-title">BUSCADORES</h1>
    </div>'''

body_buscadores = '''    <section class="section">
      <div class="buscadores-grid">
        <a href="https://salud.misiones.gob.ar/si-fe-ga/" target="_blank" rel="noopener noreferrer" class="plus-card cyan reveal">
          <span class="badge-new">Nuevo!</span>
          <span class="plus-circle">+</span>
          <p class="plus-title">Buscador de Registros Provinciales (Salas y Alimentos)</p>
        </a>
        <a href="https://inal.sifega.anmat.gob.ar/consultadealimentos/" target="_blank" rel="noopener noreferrer" class="plus-card cyan reveal">
          <p class="plus-eyebrow">Acceso</p>
          <span class="plus-circle">+</span>
          <p class="plus-title">Buscador de Productos Autorizados (RNPA)</p>
        </a>
        <a href="https://www.argentina.gob.ar/anmat/regulados/alimentos/sifega/busqueda-publica/manipuladores-y-capacitadores-en-manipulacion" target="_blank" rel="noopener noreferrer" class="plus-card cyan reveal">
          <p class="plus-eyebrow">Acceso</p>
          <span class="plus-circle">+</span>
          <p class="plus-title">Listado de Capacitadores y Manipuladores en Alimentos</p>
        </a>
        <a href="http://inal.sifega.anmat.gov.ar/consultadeRegistro/" target="_blank" rel="noopener noreferrer" class="plus-card cyan reveal">
          <p class="plus-eyebrow">Acceso</p>
          <span class="plus-circle">+</span>
          <p class="plus-title">Buscador de Establecimientos Autorizados (RNE)</p>
        </a>
        <a href="https://listadoalg.anmat.gob.ar/Home" target="_blank" rel="noopener noreferrer" class="plus-card cyan reveal">
          <p class="plus-eyebrow">Acceso</p>
          <span class="plus-circle">+</span>
          <p class="plus-title">Listado Integrado de Alimentos Libres de Gluten ( ALG)</p>
        </a>
        <a href="https://www.argentina.gob.ar/anmat/regulados/alimentos/sifega/busqueda-publica/directores-tecnicos" target="_blank" rel="noopener noreferrer" class="plus-card cyan reveal">
          <p class="plus-eyebrow">Acceso</p>
          <span class="plus-circle">+</span>
          <p class="plus-title">Buscador de Directores Técnicos (DT)</p>
        </a>
      </div>
    </section>
'''

write("buscadores.html", page("buscadores.html", "Buscadores", hero_buscadores, body_buscadores))


# =========================================================
# PAGE 8: NOTICIAS Y AVISOS
# =========================================================
hero_noticias = '''    <div class="hero hero-gold reveal">
      <p class="hero-eyebrow">Subsecretaría de Atención Primaria y Salud Ambiental</p>
      <p class="hero-eyebrow">Dirección de Saneamiento Ambiental</p>
      <p class="hero-eyebrow line3">Departamento de Saneamiento Básico</p>
      <h1 class="hero-title">DIVISIÓN DE CALIDAD DE ALIMENTOS,<br>AGUA Y LABORATORIO</h1>
    </div>'''

body_noticias = '''    <section class="section">
      <h2 class="section-title accent-gold text-center" style="text-align:center;">NOTICIAS Y AVISOS</h2>

      <div class="news-card reveal" style="max-width:760px; margin:24px auto 0;">
        <p class="news-date">13-05-2026</p>
        <p class="news-title">CAPACITACIONES ANUALES 2026</p>
        <p class="news-body">La División da inicio a su Ciclo de Capacitaciones, invitando a la participar de la primer capacitación gratuita:</p>
        <p class="news-course-name">&ldquo;GUÍA DE TRÁMITE PARA EL REGISTRO NACIONAL DE CAPACITADORES EN MANIPULACIÓN SEGURA DE ALIMENTOS, por Art. 21 mediante el uso del Sistema de Información Federal para la Gestión del Control de Alimentos (SIFeGA)&rdquo;</p>
        <a class="link-interactive" href="{form}" target="_blank" rel="noopener noreferrer">Más información e inscripción: {form}</a>
      </div>
    </section>
'''.format(form=FORM_URL)

write("noticias-y-avisos.html", page("noticias-y-avisos.html", "Noticias y Avisos", hero_noticias, body_noticias))

print("Part 3 done: capacitaciones + links-de-interes + buscadores + noticias-y-avisos")
