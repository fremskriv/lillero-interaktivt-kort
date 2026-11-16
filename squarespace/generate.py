"""Generate the paste-ready Squarespace block from the standalone map."""
from pathlib import Path
import re
base = Path(__file__).resolve().parent.parent
source = (base / 'index.html').read_text()
css = re.search(r'<style>(.*?)</style>', source, re.S)[1]
css = css.replace(':root {', ':host { display: block; width: 100%;')
css = css.replace('body {', '.lillero-map {').replace('      min-height: 100vh;\n', '')
section = re.search(r'(<section class="lillero-map".*?</section>)', source, re.S)[1]
image_url = 'https://raw.githubusercontent.com/fremskriv/lillero-interaktivt-kort/915927a12836f3b259d5d5ed6a412b71ddd46def/public/images/lillero-map-jonas.png'
section = section.replace('/public/images/lillero-map-jonas.png', image_url)
js = re.search(r'<script>(.*?)</script>', source, re.S)[1]
js = js.replace('ctaLabel:', 'href: null, ctaLabel:')
js = js.replace("document.querySelectorAll('[data-lillero-map]')", "root.querySelectorAll('[data-lillero-map]')")
js = js.replace('document.activeElement', 'root.activeElement')
js = js.replace("const hasLink = (item) => Boolean(item.ctaLabel) && !['petanque', 'legeplads', 'sauna'].includes(item.id);", "const hasLink = (item) => Boolean(item.ctaLabel && item.href && /^(https?:\\/\\/|\\/(?!\\/)|#)/i.test(item.href));")
js = js.replace('<a href="#">${escapeHtml(item.ctaLabel)}', '<a href="${escapeHtml(item.href)}">${escapeHtml(item.ctaLabel)}')
js = js.replace("cta.hidden = !hasLink(item);", "cta.hidden = !hasLink(item);\n        cta.href = hasLink(item) ? item.href : '#';")
# Listen inside the shadow root, and use the composed event path for external clicks.
js = js.replace("document.addEventListener('click', (event) => {", "root.addEventListener('click', (event) => {")
js = js.replace("      document.addEventListener('keydown',", "      document.addEventListener('click', (event) => {\n        if (activeId && !event.composedPath().includes(host)) closeInfo();\n      });\n\n      document.addEventListener('keydown',")
result = '''<!-- Lillero: Paste this entire file into ONE Squarespace HTML Code Block.
JavaScript support is required. Edit hotspot href values below to enable links.
The map image is already hosted; replace its src if you upload your own image. -->
<div data-lillero-embed>
<template>
<style>'''+css+'''</style>
'''+section+'''
</template>
</div>
<script>
(() => {
  const host = document.currentScript.previousElementSibling;
  if (!host || host.shadowRoot) return;
  const template = host.querySelector('template');
  const root = host.attachShadow({ mode: 'open' });
  root.appendChild(template.content.cloneNode(true));
  template.remove();
'''+js+'''
})();
</script>
'''
(base / 'squarespace' / 'lillero-kodeblok.html').write_text(result)
