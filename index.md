---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
---


<link rel="stylesheet" href="{{ "/assets/css/carousel.css" | relative_url }}">
![Beschreibung](/bettenhaus/assets/images/homepage/banner.JPG){: .full-width }

Willkommen in Götzerberge! Der malerische Flecken liegt an der Havel, zwischen Werder und Brandenburg. Zum Bahnhof Götz, unserm Link in die Großstadt, sind es 5km.

Lorem ipsum dolor sit amet, amici carissimi, in unione nostra robur invenimus. Coniunctis viribus, ultra difficultates scandimus, solidaritatem firmamus, et spem in animo tenemus. Amici, non sumus soli; una ascendimus, una cadimus, et rursus una surgimus. Nos adiuvamus, ut omnes in hoc itinere melius procedamus.

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

Quisque fides nostra in amicitia viget, atque voluntas succurrendi semper praesto est. Integer virtute et compassionis robore animati, firmiter stamus, auxilium ferentes et gaudium spargentes. Curabitur blandit et sustineamus invicem, ne quis cadat sine manu adiutrice. Amicitia nostra lucet ut stellae in tenebris.

Nam vitae motus incerti sunt, et iter sine certitudine procedit; tamen, societas cordium nostrorum lumen praebet. Unus pro omnibus, omnes pro uno, una virtute, una caritate, in posterum gradimur.

Vivamus laeti, propter quod in communione nostra vera fortitudo et audacia recondita est.

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