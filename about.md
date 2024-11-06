---
layout: page
title: Über das Bettenhaus
permalink: /about/
---

Götzerberge ist ein besonderer Ort, ja, nahezu eine kleine Perle im sonst so dicht besiedelten Deutschland.
Der Ort liegt im Landschaftsschutzgebiet Brandenburger Osthavelniederung. Unweit der Havel und der Deetzer Erdlöcher ist am Nordhang der Bruchwald Götzer Berg als Geschützter Landschaftsbestandteil ausgewiesen.
Was auffällt, wenn man durch den Ort spaziert, ist die Ruhe und Entschleunigung.
In Götzerberge gibt es außerdem zwei Yoga- und Mediationszentren und weitere nette Gemeinschaften. Der Havelradwanderweg geht durch das Dorf, ansonsten ist es keine Durchfahrtsstraße sondern die Straße endet mit dem Dorfende.

Mitte des 19. Jahrhunderts entstanden im Gemeindeteil Götzer Berge drei Ziegeleien und eine weitere im Wohnplatz Havelufer, die Tonvorkommen zu Steinen für das aufstrebende Berlin brannten. Der Ziegeleibesitzer Hauptmann Daude baute eine Villa mit Park und Wasserturm. Diese war später Gästehaus des FDGB-Bezirksvorstandes Potsdam. Götzer Berge entstand als Siedlung der Ziegler. 
Unsere Genossenschaft hat das ehemaliges FDGB-Schulungsheim erstanden und wir freuen uns, dem geschichtsträchtigen Ort wieder neues Leben einzuhauchen. Unser Grundstück grenzt direkt an den denkmalgeschützten Park der Villa mit wunderschönem Bestand an alten Bäumen und dahinter ist nur noch der Wald.

Ihr wollt mehr erfahren?
Dann könnt ihr an einem Info-Abend mit unseren Architektinnen teilnehmen. Schreibt dazu eine E-Mail an <a href="mailto:{{ site.email }}">{{ site.email }}</a>.

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

