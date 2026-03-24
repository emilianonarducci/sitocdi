"use client";
import { useEffect, useRef } from "react";
import type { Sede } from "@/lib/api";

interface Props {
  sedi: Sede[];
  activeSedId: number | null;
  onMarkerClick: (id: number) => void;
  singleMode?: boolean; // compact map for detail page
  visibleIds?: number[] | null; // when set, hide markers not in this list
}

export default function StoreMap({ sedi, activeSedId, onMarkerClick, singleMode, visibleIds }: Props) {
  const containerRef = useRef<HTMLDivElement>(null);
  const mapRef = useRef<ReturnType<typeof import("leaflet")["map"]> | null>(null);
  const markersRef = useRef<Map<number, ReturnType<typeof import("leaflet")["marker"]>>>(new Map());

  useEffect(() => {
    if (!containerRef.current || mapRef.current) return;

    (async () => {
      const L = await import("leaflet");

      // Fix broken default marker icons in bundlers
      L.Icon.Default.mergeOptions({
        iconUrl: "https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon.png",
        iconRetinaUrl: "https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon-2x.png",
        shadowUrl: "https://unpkg.com/leaflet@1.9.4/dist/images/marker-shadow.png",
      });

      const validSedi = sedi.filter((s) => s.lat && s.lng);
      if (!validSedi.length || !containerRef.current) return;

      const center: [number, number] = singleMode && validSedi[0]
        ? [validSedi[0].lat!, validSedi[0].lng!]
        : [45.52, 9.28];

      const map = L.map(containerRef.current, {
        center,
        zoom: singleMode ? 15 : 9,
        scrollWheelZoom: !singleMode,
      });

      L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
        maxZoom: 19,
      }).addTo(map);

      // Custom CDI marker icon
      const cdiIcon = L.divIcon({
        className: "",
        html: `<div style="
          width:36px;height:36px;border-radius:50% 50% 50% 0;
          background:#003087;border:3px solid white;
          box-shadow:0 2px 8px rgba(0,0,0,.35);
          transform:rotate(-45deg);
          display:flex;align-items:center;justify-content:center;
        "><span style="transform:rotate(45deg);color:white;font-size:14px;font-weight:700;display:block;text-align:center;line-height:30px;">+</span></div>`,
        iconSize: [36, 36],
        iconAnchor: [18, 36],
        popupAnchor: [0, -38],
      });

      validSedi.forEach((sede) => {
        const marker = L.marker([sede.lat!, sede.lng!], { icon: cdiIcon })
          .addTo(map)
          .bindPopup(
            `<div style="min-width:160px">
              <strong style="color:#003087">${sede.nome}</strong><br/>
              <span style="font-size:13px;color:#555">${sede.indirizzo}<br/>${sede.cap} ${sede.citta}</span><br/>
              ${sede.telefono ? `<a href="tel:${sede.telefono}" style="font-size:13px;color:#0052cc">${sede.telefono}</a><br/>` : ""}
              <a href="/sedi/${sede.id}" style="font-size:12px;color:#0052cc;margin-top:6px;display:inline-block">Vedi scheda →</a>
            </div>`
          );

        marker.on("click", () => onMarkerClick(sede.id));
        markersRef.current.set(sede.id, marker);
      });

      mapRef.current = map;

      if (!singleMode && validSedi.length > 1) {
        const group = L.featureGroup(Array.from(markersRef.current.values()));
        map.fitBounds(group.getBounds().pad(0.15));
      }
    })();

    return () => {
      mapRef.current?.remove();
      mapRef.current = null;
      markersRef.current.clear();
    };
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  // Open popup when activeSedId changes
  useEffect(() => {
    if (activeSedId === null) return;
    const marker = markersRef.current.get(activeSedId);
    if (marker && mapRef.current) {
      mapRef.current.setView((marker as unknown as { getLatLng(): { lat: number; lng: number } }).getLatLng(), 13, { animate: true });
      marker.openPopup();
    }
  }, [activeSedId]);

  // Show/hide markers based on visibleIds
  useEffect(() => {
    if (!visibleIds) {
      markersRef.current.forEach((m) => (m as unknown as { setOpacity(v: number): void }).setOpacity(1));
      return;
    }
    const set = new Set(visibleIds);
    markersRef.current.forEach((m, id) => {
      (m as unknown as { setOpacity(v: number): void }).setOpacity(set.has(id) ? 1 : 0.15);
    });
  }, [visibleIds]);

  return <div ref={containerRef} style={{ width: "100%", height: "100%" }} />;
}
