"use client";
import { useState } from "react";
import styles from "./Hero.module.css";
import type { HeroSlide } from "@/lib/cms";

const FALLBACK: HeroSlide[] = [
  {
    id: 1,
    badge: "CDI — Dal 1975",
    titolo: "La tua salute,\nla nostra missione.",
    sottotitolo: "Oltre 80 centri in Lombardia. Prenota visite, esami e prestazioni mediche con i migliori specialisti.",
    cta_testo: "Prenota ora",
    cta_link: "/cerca",
    immagine_url: "https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=1600&q=80&auto=format&fit=crop",
  },
];

export default function Hero({ slides: initialSlides }: { slides?: HeroSlide[] | null }) {
  const slides = initialSlides?.length ? initialSlides : FALLBACK;
  const [current, setCurrent] = useState(0);
  const slide = slides[current];

  return (
    <section className={styles.hero}>
      {/* eslint-disable-next-line @next/next/no-img-element */}
      <img src={slide.immagine_url} alt="" className={styles.bgImage} />
      <div className={styles.overlay} />
      <div className={styles.content}>
        <span className={styles.badge}>{slide.badge}</span>
        <h1>{slide.titolo}</h1>
        <p>{slide.sottotitolo}</p>
        <a href={slide.cta_link} className={styles.cta}>{slide.cta_testo}</a>
      </div>
      <div className={styles.nav}>
        <button className={styles.arrow} onClick={() => setCurrent((c) => (c - 1 + slides.length) % slides.length)}>←</button>
        <div className={styles.dots}>
          {slides.map((_, i) => (
            <button key={i} className={`${styles.dot} ${i === current ? styles.dotActive : ""}`} onClick={() => setCurrent(i)} />
          ))}
        </div>
        <button className={styles.arrow} onClick={() => setCurrent((c) => (c + 1) % slides.length)}>→</button>
      </div>
    </section>
  );
}
