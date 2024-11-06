---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
---


<link rel="stylesheet" href="{{ "/assets/css/carousel.css" | relative_url }}">
![Beschreibung](/bettenhaus/assets/images/homepage/banner.JPG){: .full-width }

Willkommen in Götzerberge! Der malerische Flecken liegt an der Havel, zwischen Werder und Brandenburg.
Hier entsteht ein generationenübergreifendes und zukunftsfähiges Wohnen in Stadtnähe.
Das Wohnprojekt wird von einer kleinen, neu gegründeten Genossenschaft realisiert. Damit soll allen Bewohner*innen und Beteiligten eine langfristige Wohnperspektive in einem toleranten, respektvollen und gemeinwohlorientierten Umfeld ermöglicht werden. 
Das Bettenhaus liegt wunderschön zwischen den Götzer Bergen, der Havel und den Deetzer Erdelöchern. Nach Berlin ist es eine Stunde Fahrzeit per Bahn (RE1) oder Auto. Zum Bahnhof Götz, unserm Link in die Großstadt, sind es 5km.



<div id="carousel" class="carousel">
  <div class="carousel-item">
    <img src="/bettenhaus/assets/images/homepage/entrance.jpg">
    <div class="caption">Blick von der Straße auf das Ensembe</div>
  </div>
  <div class="carousel-item active">
    <img src="/bettenhaus/assets/images/homepage/DSCF1308.jpg">
    <div class="caption">Eines der Deetzer Erdelöcher, unser Badesee. Foto: Susanne Beyer</div>
  </div>
  <div class="carousel-item">
    <img src="/bettenhaus/assets/images/homepage/DSCF1347.jpg">
    <div class="caption">Blick vom Nahegelegenen Aussichtsturm. Foto: Susanne Beyer</div>
  </div>
  <div class="carousel-item">
    <img src="/bettenhaus/assets/images/homepage/westende.jpg">
    <div class="caption">Der Westflügel des Plattenbaus mit angrenzendem Landschaftspark</div>
  </div>

  <!-- Steuerungselemente -->
  <button class="carousel-control prev" onclick="moveSlide(-1)">&#10094;</button>
  <button class="carousel-control next" onclick="moveSlide(1)">&#10095;</button>
</div>
</div>

Es wird individuelle, barrierefreie Wohnungen und gemeinschaftlich genutzte Bereiche geben. Das ehemaliges FDGB-Schulungsheim wird dazu umgebaut. Neben der sozialen Nachhaltigkeit streben wir eine ökologisch durchdachte, ästhetisch und ökonomisch überzeugende Modernisierung des Baubestands an. Wenn ihr Interesse an dem Projekt habt, meldet euch gern!
</div>
___

<script>
let currentSlide = 0;
const slides = document.querySelectorAll('.carousel-item');

function showSlide(index) {
  slides.forEach((slide, i) => {
    slide.classList.remove('active');
    if (i === index) {
      slide.classList.add('active');
    }
  });
}

function moveSlide(step) {
  currentSlide = (currentSlide + step + slides.length) % slides.length;
  showSlide(currentSlide);
}

// Zeige den ersten Slide beim Laden
showSlide(currentSlide);
</script>
