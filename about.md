---
layout: page
title: Über das Bettenhaus
permalink: /about/
---

Wohnen in Genossenschaft im Grünen?

Zwischen Werder und Brandenburg planen wir ein gemeinsames Wohnprojekt.
Wir suchen noch Menschen, die Lust haben einzusteigen.

Wir sind eine kleine neu gegründete Genossenschaft und suchen neue Mitglieder, die Lust haben, sich ihren eigenen abgeschlossenen Wohnraum zu gestalten und gleichzeitig bestimmte gemeinschaftliche Räume zu teilen.

Es ist genossenschaftliches Eigentum an einem Plattenbau in einem historischen Landschaftspark. Der Grund und Boden wird in Erbbaurecht von einer Stiftung gepachtet. Das Haus wird so ökologisch und nachhaltig wie möglich zum Wohnen umgebaut. Es war mal ein altes FDGB Schulungsheim.

Das Grundstück befindet sich in unmittelbarer Nähe zur Havel und den Deetzer Erdlöchern und verfügt über einen wunderschönen Bestand an alten Bäumen.

Nach Berlin ist es ungefähr eine Stunde Fahrzeit per Bahn oder Auto. Der nächste Bahnhof in Götz ist 5 km entfernt.

Wir wünschen uns ein vielfältiges respektvolles Miteinander und freuen uns drauf, von Euch zu hören.

Bei Interesse könnt ihr an einem Info-Abend mit unseren Architektinnen teilnehmen. Schreibt dazu eine E-Mail an <a href="mailto:post@winterer-mohr.eu">post@winterer-mohr.eu</a>.

<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="leaflet-map" style="height: 400px; width: 100%;"></div>
<script>
    var map = L.map('leaflet-map').setView([52.443955, 12.731357], 12); // Center map on coordinates

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    L.marker([52.443955, 12.731357]).addTo(map)
        .bindPopup('Willkommen in Götzerberge!')
        .openPopup();
</script>

