#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from build import page, write, dl, dl_item

RNE_CAT = "rne"
RNPA_CAT = "rnpa"
SIFEGA_CAT = "sifega"

RPEA_CAT = "rpea"
RPAA_CAT = "rpaa"

# =========================================================
# PAGE 3: RNE Y RNPA
# =========================================================
hero_rne = '''    <div class="hero hero-purple reveal">
      <p class="hero-eyebrow line3">DIVISIÓN DE CALIDAD DE ALIMENTOS, AGUA Y LABORATORIO</p>
      <h1 class="hero-title">REGISTRO NACIONAL DE DE ESTABLECIMIENTOS Y PRODUCTOS ALIMENTICIOS</h1>
    </div>'''

sifega_items = [
    ("1-Nota de Solicitud Alta de Usuario", dl(SIFEGA_CAT, "01-nota-solicitud-alta-usuario.docx")),
    ("2-Autorización de Terceros retirar la clave", dl(SIFEGA_CAT, "02-autorizacion-terceros-retirar-clave.docx")),
]

rne_items = [
    ("1- Instructivo para usuarios externos", dl(RNE_CAT, "01-instructivo-usuarios-externos.pdf")),
    ("2 - Directrices para la Autorización Sanitaria de Establecimientos", dl(RNE_CAT, "02-directrices-autorizacion-sanitaria-establecimientos.pdf")),
    ("3- Contenidos mínimos para la Elaboración de manuales", dl(RNE_CAT, "03-contenidos-minimos-elaboracion-manuales.pdf")),
    ("4- Guía Manual de Retiro", dl(RNE_CAT, "04-guia-manual-retiro.pdf")),
    ("5- Lista de Chequeo", dl(RNE_CAT, "05-lista-de-chequeo.docx")),
    ("6 - Nota de Domicilio legal Misiones", dl(RNE_CAT, "06-nota-domicilio-legal-misiones.docx")),
    ("7- Informe de asistencia de Dirección Técnica", dl(RNE_CAT, "07-informe-asistencia-direccion-tecnica.docx")),
]

rnpa_items = [
    ("1- Instructivo RNPA", dl(RNPA_CAT, "01-instructivo-rnpa.pdf")),
    ("2-Directrices para la Autorización Sanitaria de Producto Alimenticio", dl(RNPA_CAT, "02-directrices-autorizacion-sanitaria-producto.pdf")),
    ("3 - Guía Rotulado", dl(RNPA_CAT, "03-guia-rotulado.pdf")),
    ("4 - Guía Rotulado Alérgenos", dl(RNPA_CAT, "04-guia-rotulado-alergenos.pdf")),
    ("5- Directrices Autorización de ALG (Alimentos libre de Gluten)", dl(RNPA_CAT, "05-directrices-autorizacion-alg.pdf")),
    ("6-Declaración jurada de uso de marcas", dl(RNPA_CAT, "06-declaracion-jurada-uso-marcas.docx")),
    ("7-Declaración Jurada de contenidos netos", dl(RNPA_CAT, "07-declaracion-jurada-contenidos-netos.docx")),
    ("8-Nota Modelo de Lotes", dl(RNPA_CAT, "08-nota-modelo-lote.docx")),
    ("9-Datos de las materias primas utilizadas", dl(RNPA_CAT, "09-datos-materias-primas-utilizadas.docx")),
    ("10-Nota modelo MISMO informe DISTINTOS productos", dl(RNPA_CAT, "10-nota-modelo-mismo-informe-distintos-productos.docx")),
    ("Alimentos Libre de Gluten (ALG)", dl(RNPA_CAT, "05-directrices-autorizacion-alg.pdf")),
    ("11-Declaración Jurada de BPM", dl(RNPA_CAT, "11-declaracion-jurada-bpm.docx")),
    ("12- Declaración de uso de Envases", dl(RNPA_CAT, "12-solicitud-autorizacion-uso-envases.docx")),
]

body_rne = '''    <section class="section">
      <div class="cards-grid cols-2">
        <div class="card card-accent-purple reveal">
          <p class="card-label purple">Area de Evaluación Técnica</p>
          <a class="card-meta link-interactive" href="mailto:mspdivalimentosnormas@gmail.com" style="font-size:15px;">mspdivalimentosnormas@gmail.com</a>
          <p class="card-meta" style="margin-top:12px; font-style:italic;">Responsable:<br>Bioq. Sandra Melnik</p>
        </div>
        <div class="card card-accent-purple reveal">
          <p class="card-label purple">Solicitudes</p>
          <p class="card-body">Notas de acceso al SIFEGA</p>
          <div class="download-list">
{sifega}
          </div>
        </div>
      </div>
    </section>

    <hr class="divider-soft">

    <section class="section">
      <div class="cards-grid cols-2">
        <div class="card card-accent-purple reveal">
          <p class="card-label purple">RNE</p>
          <p class="card-body">Trámite de REGISTRO NACIONAL DE ESTABLECIMIENTOS</p>
        </div>
        <div class="card card-accent-purple reveal">
          <p class="card-label purple">RNPA</p>
          <p class="card-body">Trámite de REGISTRO NACIONAL DE PRODUCTOS ALIMENTICIOS</p>
        </div>
      </div>
    </section>

    <hr class="divider-soft">

    <section class="section">
      <h2 class="section-title accent-purple">REGISTRO NACIONAL DE DE ESTABLECIMIENTOS (RNE)</h2>
      <p class="section-lead" style="font-style:italic;">DIVISIÓN DE CALIDAD DE ALIMENTOS, AGUA Y LABORATORIO</p>
      <p class="welcome-hint" style="margin:10px 0 0;">DESCARGUE EL INSTRUCTIVO DE SU INTERÉS</p>
      <div class="download-list">
{rne}
      </div>
    </section>

    <hr class="divider-soft">

    <section class="section">
      <h2 class="section-title accent-purple">registro NACIONAL DE PRODUCTOS ALIMENTICIOS (RNPA)</h2>
      <p class="section-lead" style="font-style:italic;">DIVISIÓN DE CALIDAD DE ALIMENTOS, AGUA Y LABORATORIO</p>
      <div class="download-list">
{rnpa}
      </div>
      <p class="welcome-hint" style="margin-top:16px;">DESCARGUE EL INSTRUCTIVO DE SU INTERÉS</p>
    </section>
'''.format(
    sifega="\n".join(dl_item(l, h) for l, h in sifega_items),
    rne="\n".join(dl_item(l, h) for l, h in rne_items),
    rnpa="\n".join(dl_item(l, h) for l, h in rnpa_items),
)

write("rne-y-rnpa.html", page("rne-y-rnpa.html", "RNE y RNPA", hero_rne, body_rne))


# =========================================================
# PAGE 4: REGISTRO DE ARTESANALES
# =========================================================
hero_artesanales = '''    <div class="hero hero-orange reveal">
      <p class="hero-eyebrow line3">DIVISIÓN DE CALIDAD DE ALIMENTOS, AGUA Y LABORATORIO</p>
      <h1 class="hero-title">REGISTRO PROVINCIAL DE SALA DE ELABORACIÓN ARTESANAL</h1>
    </div>'''

rpea_items = [
    ("1- Guía de trámite para RPEA", dl(RPEA_CAT, "01-guia-tramite-rpea.pdf")),
    ("2- Formulario RPEA", dl(RPEA_CAT, "02-formulario-rpea.doc")),
    ("3- Nota Modelo de Solicitud de Inscripción de sala", dl(RPEA_CAT, "03-nota-modelo-solicitud-inscripcion-sala.docx")),
    ("4- Contenido Mínimo de Manuales para elaboradores", dl(RPEA_CAT, "04-contenido-minimo-manuales-elaboradores.pdf")),
    ("5- Autorización para terceros", dl(RPEA_CAT, "05-autorizacion-para-terceros.docx")),
    ("6- Modelo de Manual de BPM Artesanales", dl(RPEA_CAT, "06-modelo-manual-bpm-artesanales.docx")),
    ("7- Modelo de Manual de POES Artesanales", dl(RPEA_CAT, "07-modelo-manual-poes-artesanales.docx")),
    ("8 - Modelo de Manual de MIP Artesanales", dl(RPEA_CAT, "08-modelo-manual-mip-artesanales.docx")),
]

rpaa_items = [
    ("1- Guía de trámite para RPAA", dl(RPAA_CAT, "01-guia-tramite-rpaa.pdf")),
    ("2- Formulario RPAA", dl(RPAA_CAT, "02-formulario-rpaa.doc")),
    ("3- Nota Modelo de Solicitud de Inscripción de alimentos artesanales", dl(RPAA_CAT, "03-nota-modelo-solicitud-inscripcion-alimentos-artesanales.docx")),
    ("4- Declaración jurada de Contenidos Netos", dl(RPAA_CAT, "04-declaracion-jurada-contenidos-netos.docx")),
    ("5- Declaración Jurada de uso de marca", dl(RPAA_CAT, "05-declaracion-jurada-uso-marca.docx")),
    ("6- Declaración jurada de lugar de comercialización", dl(RPAA_CAT, "06-declaracion-jurada-lugar-comercializacion.docx")),
    ("7- Nota modelo de Lote", dl(RPAA_CAT, "07-nota-modelo-lote.docx")),
    ("POES Artesanales", dl(RPEA_CAT, "07-modelo-manual-poes-artesanales.docx")),
    ("8- Nota modelo de Reinscripción de alimentos artesanales", dl(RPAA_CAT, "08-nota-modelo-reinscripcion-alimentos-artesanales.docx")),
    ("9- Datos de materias primas utilizadas", dl(RPAA_CAT, "09-datos-materias-primas-utilizadas.docx")),
]

body_artesanales = '''    <section class="section">
      <div class="card card-accent-orange reveal" style="max-width:480px;">
        <p class="card-label orange">Area de Evaluación Técnica</p>
        <a class="card-meta link-interactive" href="mailto:mspdivalimentosnormas@gmail.com" style="font-size:15px;">mspdivalimentosnormas@gmail.com</a>
        <p class="card-meta" style="margin-top:12px; font-style:italic;">Responsable:<br>Bioq. Sandra Melnik</p>
      </div>
    </section>

    <section class="section" style="padding-top:0;">
      <a href="#descargas-rpea" class="download-banner orange reveal">
        <span>DESCARGUE LOS INSTRUCTIVOS DE SU INTERÉS</span>
        <span class="cloud-icon">&#9729;&#8681;</span>
      </a>
    </section>

    <section class="section" style="padding-top:0;">
      <div class="cards-grid cols-2">
        <div class="card card-accent-orange reveal">
          <p class="card-label orange">RPEA</p>
          <p class="card-body">Trámite de REGISTRO PROVINCIAL DE SALA DE ELABORACIÓN ARTESANAL</p>
        </div>
        <div class="card card-accent-orange reveal">
          <p class="card-label orange">RPAA</p>
          <p class="card-body">Trámite de REGISTRO PROVINCIAL DE ALIMENTO ARTESANAL</p>
        </div>
      </div>
    </section>

    <hr class="divider-soft">

    <section class="section" id="descargas-rpea">
      <h2 class="section-title accent-orange">REGISTRO PROVINCIAL DE SALA DE ELABORACIÓN ARTESANAL (RPEA)</h2>
      <p class="section-lead" style="font-style:italic;">DIVISIÓN DE CALIDAD DE ALIMENTOS, AGUA Y LABORATORIO</p>
      <p class="welcome-hint" style="margin:10px 0 0;">DESCARGUE EL INSTRUCTIVO DE SU INTERÉS</p>
      <div class="download-list">
{rpea}
      </div>
    </section>

    <hr class="divider-soft">

    <section class="section">
      <h2 class="section-title accent-orange">registro provincial DE ALIMENTO ARTESANAL (RPAA)</h2>
      <p class="section-lead" style="font-style:italic;">DIVISIÓN DE CALIDAD DE ALIMENTOS, AGUA Y LABORATORIO</p>
      <p class="welcome-hint" style="margin:10px 0 0;">DESCARGUE EL INSTRUCTIVO DE SU INTERÉS</p>
      <div class="download-list">
{rpaa}
      </div>
    </section>
'''.format(
    rpea="\n".join(dl_item(l, h) for l, h in rpea_items),
    rpaa="\n".join(dl_item(l, h) for l, h in rpaa_items),
)

write("registro-de-artesanales.html", page("registro-de-artesanales.html", "Registro de Artesanales", hero_artesanales, body_artesanales))

print("Part 2 done: rne-y-rnpa + registro-de-artesanales")
