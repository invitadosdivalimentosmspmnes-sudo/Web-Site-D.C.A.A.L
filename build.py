#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build script: generates the 8 static HTML pages for the
División de Calidad de Alimentos, Agua y Laboratorio portal."""

import os

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = ROOT

NAV = [
    ("index.html", "Inicio"),
    ("ubicacion-y-contactos.html", "Ubicación y Contactos"),
    ("rne-y-rnpa.html", "RNE y RNPA"),
    ("registro-de-artesanales.html", "Registro de Artesanales"),
    ("capacitaciones.html", "Capacitaciones"),
    ("links-de-interes.html", "Links de Interés"),
    ("buscadores.html", "Buscadores"),
    ("noticias-y-avisos.html", "Noticias y Avisos"),
]

WHATSAPP_URL = "https://wa.me/5493765193454?text=Hola%2C%20quisiera%20realizar%20una%20consulta."
MAPS_QUERY = "Laboratorio Central de la Provincia de Misiones LACEPMI, Calle 62 y Calle 229, Posadas, Misiones, Argentina"
MAPS_URL = "https://www.google.com/maps/search/?api=1&query=" + MAPS_QUERY.replace(" ", "+").replace(",", "%2C")
MAPS_EMBED = "https://maps.google.com/maps?q=" + MAPS_QUERY.replace(" ", "+") + "&output=embed"
FORM_URL = "https://forms.gle/FVoDsfe2Uya9L2PMA"


def nav_links(active_file):
    parts = []
    for href, label in NAV:
        current = ' aria-current="page"' if href == active_file else ""
        parts.append('<a href="{href}"{current}>{label}</a>'.format(
            href=href, current=current, label=label))
    return "\n        ".join(parts)


def breadcrumb(active_file, active_label):
    if active_file == "index.html":
        return ""
    return '''
  <div class="app-container">
    <nav class="breadcrumbs" aria-label="Breadcrumb">
      <a href="index.html">Inicio</a><span class="sep">/</span><span class="current">{label}</span>
    </nav>
  </div>'''.format(label=active_label)


def header(active_file):
    return '''  <header class="site-header">
    <div class="header-inner">
      <a href="index.html" class="logo-lockup" aria-label="Ir al inicio">
        <img src="logo.png" alt="Misiones Gobierno | Ministerio de Salud Pública">
      </a>
      <nav class="main-nav" aria-label="Navegación principal">
        {nav}
      </nav>
    </div>
  </header>'''.format(nav=nav_links(active_file))


def footer():
    return '''  <footer class="site-footer">
    <div class="app-container footer-links">
      <a href="#" class="link-interactive">Términos y ayuda</a>
      <span class="separator">|</span>
      <a href="#" class="link-interactive">Política de privacidad</a>
      <div class="footer-canva">División de Calidad de Alimentos, Agua y Laboratorio &mdash; Ministerio de Salud Pública de Misiones</div>
    </div>
  </footer>'''


def page(active_file, tab_title, hero_html, body_html, extra_head=""):
    return '''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{tab_title}</title>
<meta name="description" content="División de Calidad de Alimentos, Agua y Laboratorio - Ministerio de Salud Pública de Misiones. Portal de información y descarga de instructivos.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
{extra_head}
</head>
<body>
<div class="app-container">
</div>
{header}
<main>
{breadcrumb}
  <div class="app-container">
{hero}
{body}
  </div>
</main>
{footer}
<script src="main.js"></script>
</body>
</html>
'''.format(
        tab_title=tab_title,
        extra_head=extra_head,
        header=header(active_file),
        breadcrumb=breadcrumb(active_file, dict((h, l) for h, l in NAV)[active_file]),
        hero=hero_html,
        body=body_html,
        footer=footer(),
    )


def write(filename, content):
    with open(os.path.join(OUT, filename), "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", filename)


def dl(category, filename):
  return category + "-" + filename


def dl_item(label, href):
    fname = href.rsplit("/", 1)[-1]
  return '''      <a class="download-item reveal" href="{href}" download>
        <span>{label}</span>
        <span class="dl-icon">&#8681;</span>
      </a>'''.format(href=href, label=label)
