#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import build
from build import page, write, WHATSAPP_URL, MAPS_URL, MAPS_EMBED, FORM_URL, dl, dl_item


# =========================================================
# PAGE 1: INDEX
# =========================================================
hero_index = '''    <div class="hero hero-gold reveal">
      <p class="hero-eyebrow">Subsecretaría de Atención Primaria y Salud Ambiental</p>
      <p class="hero-eyebrow">Dirección de Saneamiento Ambiental</p>
      <p class="hero-eyebrow line3">Departamento de Saneamiento Básico</p>
      <h1 class="hero-title">DIVISIÓN DE CALIDAD DE ALIMENTOS, AGUA Y LABORATORIO</h1>
    </div>'''

body_index = '''    <section class="section">
      <div class="welcome-news-grid">
        <div class="card reveal">
          <p class="eyebrow-label">Bienvenido</p>
          <h2 class="welcome-title">BIENVENIDO</h2>
          <p class="welcome-sub">Portal de información y descarga de instructivos</p>
          <p class="welcome-hint">Haga click en la sección de su interés</p>
        </div>
        <div class="news-teaser reveal">
          <div class="info-icon">i</div>
          <p class="teaser-label">Noticias</p>
          <a href="noticias-y-avisos.html" class="arrow-link">Noticias y Avisos de la División <span class="arrow">&rarr;</span></a>
        </div>
      </div>
    </section>

    <hr class="divider-soft">

    <section class="section">
      <h2 class="section-title">Accesos directos y contacto</h2>
      <div class="cards-grid cols-3">
        <a href="ubicacion-y-contactos.html" class="card card-accent-teal reveal">
          <p class="card-label teal">Contacto</p>
          <p class="card-heading">&#9742; &#128205; CONTACTO Y UBICACIÓN DE NUESTRAS OFICINAS</p>
        </a>
        <a href="registro-de-artesanales.html" class="card card-accent-orange reveal">
          <p class="card-label orange">Instructivos</p>
          <p class="card-heading">Registro Provincial de Elaboradores(RPEA) y Alimentos Artesanales (RPAA)</p>
        </a>
        <a href="rne-y-rnpa.html" class="card card-accent-purple reveal">
          <p class="card-label purple">Instructivos</p>
          <p class="card-heading">Registro Nacional de Establecimientos (RNE) y Productos Alimenticios (RNPA)</p>
        </a>
        <a href="capacitaciones.html" class="card card-accent-green reveal">
          <p class="card-label green">Trámite</p>
          <p class="card-heading">Alta como Capacitador Nacional en Manipulación Segura de Alimentos</p>
        </a>
        <a href="ubicacion-y-contactos.html#residencia" class="card card-accent-gold reveal">
          <p class="card-label gold">Información</p>
          <p class="card-heading">Residencia en Bioquímica Bromatológica</p>
        </a>
        <a href="ubicacion-y-contactos.html#laboratorio" class="card card-accent-cyan reveal">
          <p class="card-label cyan">Información</p>
          <p class="card-heading">Laboratorio de Aguas y Alimentos</p>
        </a>
        <a href="capacitaciones.html" class="card card-accent-green reveal">
          <p class="card-label green">Información</p>
          <p class="card-heading">Capacitaciones presenciales y virtuales</p>
        </a>
      </div>
    </section>

    <hr class="divider-soft">

    <section class="section">
      <h2 class="section-title accent-cyan">Buscadores</h2>
      <div class="cards-grid cols-2">
        <a href="buscadores.html" class="card card-accent-cyan reveal">
          <p class="card-heading">Establecimientos Autorizados</p>
        </a>
        <a href="buscadores.html" class="card card-accent-cyan reveal">
          <p class="card-heading">Productos Alimenticios Autorizados</p>
        </a>
        <a href="buscadores.html" class="card card-accent-cyan reveal">
          <p class="card-heading">Alimentos Libre de Gluten</p>
        </a>
        <a href="buscadores.html" class="card card-accent-cyan reveal">
          <p class="card-heading">Buscador de Directores Técnicos</p>
        </a>
      </div>
    </section>

    <hr class="divider-soft">

    <section class="section">
      <h2 class="section-title accent-teal">Información / Links de Interés</h2>
      <div class="cards-grid cols-3">
        <a href="links-de-interes.html" class="card card-accent-teal reveal">
          <p class="card-heading">Plataforma SIFeGA</p>
        </a>
        <a href="links-de-interes.html" class="card card-accent-teal reveal">
          <p class="card-heading">Código Alimentario Argentino (Ley 18.284)</p>
        </a>
        <a href="links-de-interes.html" class="card card-accent-teal reveal">
          <p class="card-heading">Boletín oficial misiones</p>
        </a>
      </div>
    </section>
'''

write("index.html", page("index.html", "Inicio", hero_index, body_index))


# =========================================================
# PAGE 2: UBICACIÓN Y CONTACTOS
# =========================================================
hero_ubicacion = '''    <div class="hero hero-gold reveal">
      <p class="hero-eyebrow">Subsecretaría de Atención Primaria y Salud Ambiental</p>
      <p class="hero-eyebrow">Dirección de Saneamiento Ambiental</p>
      <p class="hero-eyebrow line3">Departamento de Saneamiento Básico</p>
      <h1 class="hero-title">DIVISIÓN DE CALIDAD DE ALIMENTOS,<br>AGUA Y LABORATORIO</h1>
    </div>'''

areas = [
    ("AREA DE GESTIÓN", "mspdivalimentos@gmail.com", "Bioq. Mgter. Federico Payés Monzón"),
    ("AREA DE EVALUACIÓN TÉCNICA", "mspdivalimentosnormas@gmail.com", "Bioq. Sandra Melnik"),
    ("AREA DE CAPACITACIONES", "mspdivalimentoscapacitaciones@gmail.com", "Bioq. Mgter. Myriam García"),
    ("LABORATORIO DE AGUAS Y ALIMENTOS", "labalimentosmnes@gmail.com", "Bioq. Mgter. Débora A. López"),
    ("AREA DE AUDITORÍAS", "alimentosauditorias@gmail.com", "Bioq. Mgter. Pablo Capaccio"),
]

sectores = [
    ("ÁREA DE ANÁLISIS MICROBIOLÓGICO", "microlabalimentosmspmnes@gmail.com", "Bioq. Gonzalo J. Alvarenga"),
    ("ÁREA DE RECEPCIÓN DE MUESTRAS", "mspdivalimentosmuestras@gmail.com", "Téc. Brom. Valeria Caruso"),
    ("ÁREA DE ANÁLISIS FISICOQUÍMICO", "fq.labalimentosmspmnes@gmail.com", "Bioq. Mgter. Sergio Parafieniuk"),
    ("ÁREA DE ANÁLISIS DE GLUTEN", "labalimentosmnes@gmail.com", "Bioq. Mgter. Pablo Capaccio"),
    ("AREA DE GENUINIDAD", "fq.labalimentosmspmnes@gmail.com", "Bioq. Candelaria Hein"),
]


def area_card(nombre, email, responsable):
    return '''        <div class="area-card reveal">
          <p class="area-name">{nombre}</p>
          <a class="area-email" href="mailto:{email}">{email}</a>
          <p class="area-resp-label">Responsable:</p>
          <p class="area-resp-name">{responsable}</p>
        </div>'''.format(nombre=nombre, email=email, responsable=responsable)


areas_html = "\n".join(area_card(*a) for a in areas)
sectores_html = "\n".join(area_card(*s) for s in sectores)

body_ubicacion = '''    <section class="section">
      <div class="contact-card reveal">
        <svg class="whatsapp-icon" viewBox="0 0 32 32" fill="currentColor" aria-hidden="true"><path d="M16.001 3C9.373 3 4 8.373 4 15c0 2.362.687 4.564 1.872 6.417L4 29l7.762-1.837A11.94 11.94 0 0 0 16.001 27C22.63 27 28 21.627 28 15S22.63 3 16.001 3zm0 21.818c-2.02 0-3.9-.59-5.485-1.605l-.393-.242-4.605 1.09 1.114-4.487-.256-.412A9.77 9.77 0 0 1 5.182 15c0-5.964 4.855-10.818 10.819-10.818S26.818 9.036 26.818 15 21.965 24.818 16.001 24.818zm5.938-8.14c-.325-.163-1.925-.95-2.223-1.06-.298-.109-.515-.163-.732.163-.217.326-.84 1.06-1.03 1.278-.19.217-.38.244-.705.081-.325-.163-1.373-.506-2.615-1.612-.967-.862-1.62-1.927-1.81-2.253-.19-.326-.02-.502.143-.664.146-.146.325-.38.488-.57.163-.19.217-.326.325-.543.109-.217.054-.407-.027-.57-.081-.163-.732-1.764-1.003-2.416-.264-.634-.532-.548-.732-.558-.19-.008-.407-.01-.624-.01-.217 0-.57.081-.868.407-.298.326-1.138 1.113-1.138 2.715 0 1.602 1.165 3.15 1.328 3.368.163.217 2.293 3.503 5.557 4.912.777.335 1.383.535 1.856.685.78.248 1.49.213 2.052.13.626-.093 1.925-.787 2.196-1.547.271-.76.271-1.412.19-1.547-.081-.135-.298-.217-.623-.38z"/></svg>
        <p class="contact-title">Contacto</p>
        <p class="contact-sub">Whatsapp para consultas generales</p>
        <a class="contact-phone" href="{whatsapp}" target="_blank" rel="noopener noreferrer">376 5193454</a>
        <p class="contact-hours">Lunes a Viernes<br>De 8:00 a 12:30 H<br>Deje su nombre y consulta. Nos comunicaremos a la brevedad</p>
      </div>
    </section>

    <hr class="divider-soft">

    <section class="section" id="laboratorio">
      <h2 class="section-title accent-teal">Ubicación &mdash; Laboratorio LACEPMI</h2>
      <div class="location-block">
        <div class="reveal">
          <p class="location-address">
            <strong>Laboratorio Central de la Provincia de Misiones (LACEPMI)</strong><br>
            <em>Parque Industrial y de la Innovación Posadas (PIIP)</em><br>
            <strong>Calle 62 y Calle 229 (Paraje Nemesio Parma)</strong><br>
            Posadas<br>Misiones<br>Argentina<br>CP 3300
          </p>
          <p class="location-note">Nuestras oficinas están ubicadas dentro del edificio del Laboratorio Central de la Provincia de Misiones (LACEPMI)</p>
        </div>
        <div class="reveal">
          <div class="map-embed-wrap">
            <iframe src="{maps_embed}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Mapa de ubicación PIIP"></iframe>
          </div>
          <div class="maps-cta">
            <span class="maps-label">Google Maps</span>
            <a class="arrow-link link-interactive" href="{maps_url}" target="_blank" rel="noopener noreferrer">ver ubicación <span class="arrow">&rarr;</span></a>
          </div>
        </div>
      </div>
    </section>

    <hr class="divider-soft">

    <section class="section">
      <h2 class="section-title accent-teal">Contacto por Áreas</h2>
      <p class="section-lead">División de Calidad de Alimentos, Agua y Laboratorio</p>
      <div class="cards-grid cols-3" style="margin-top:20px;">
{areas}
      </div>
    </section>

    <hr class="divider-soft">

    <section class="section">
      <h2 class="section-title accent-teal">Contacto por Sectores</h2>
      <p class="section-lead">Contacto por sector &mdash; laboratorio de aguas y alimentos</p>
      <div class="cards-grid cols-3" style="margin-top:20px;">
{sectores}
      </div>
    </section>

    <hr class="divider-soft">

    <section class="section" id="residencia">
      <h2 class="section-title accent-gold">Residencia en Bioquímica Bromatológica</h2>
      <p class="section-lead">Laboratorio de aguas y alimentos</p>
      <div class="area-card reveal" style="max-width:480px; margin-top:20px;">
        <p class="area-name">RESIDENCIA EN BIOQUÍMICA BROMATOLÓGICA</p>
        <a class="area-email" href="mailto:residenciabqcabromatologica@gmail.com">residenciabqcabromatologica@gmail.com</a>
        <p class="area-resp-label">Responsable:</p>
        <p class="area-resp-name">Bioq. Ana Victoria Cerri</p>
        <p class="location-note" style="margin-top:14px;">@Resi.bioqbromato.mnes<br>(Instagram de Actividades y Anuncios)</p>
      </div>
    </section>
'''.format(whatsapp=WHATSAPP_URL, maps_embed=MAPS_EMBED, maps_url=MAPS_URL, areas=areas_html, sectores=sectores_html)

write("ubicacion-y-contactos.html", page("ubicacion-y-contactos.html", "Ubicación y contactos", hero_ubicacion, body_ubicacion))

print("Part 1 done: index + ubicacion")
