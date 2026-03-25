import { getSedi } from "@/lib/api";
import SediPageClient from "./SediPageClient";
import styles from "./page.module.css";

export const revalidate = 300;

const PROVINCE: Record<string, string> = {
  MI: "Milano",
  MB: "Monza-Brianza",
  BG: "Bergamo",
  BS: "Brescia",
  VA: "Varese",
  PV: "Pavia",
};

const TIPO_LABEL: Record<string, string> = {
  poliambulatorio: "Poliambulatorio",
  altro: "Punto Prelievi",
  studio: "Studio Specialistico",
  clinica: "Clinica",
  ospedale: "Ospedale",
};

export default async function SediPage() {
  const sedi = await getSedi();

  const citta = Array.from(new Set(sedi.map((s) => s.citta)));
  const province = Array.from(new Set(sedi.map((s) => s.provincia).filter(Boolean)));
  const poliambulatori = sedi.filter((s) => s.tipo === "poliambulatorio" || s.tipo === "studio");
  const puntiPrelievi = sedi.filter((s) => s.tipo === "altro");

  return (
    <>
      {/* ── HERO ─────────────────────────────────────────── */}
      <section className={styles.hero}>
        <div className={styles.heroOverlay} />
        <div className={styles.heroContent}>
          <span className={styles.heroBadge}>I NOSTRI CENTRI</span>
          <h1 className={styles.heroTitle}>
            Oltre 80 centri<br />in Lombardia
          </h1>
          <p className={styles.heroSub}>
            Poliambulatori, diagnostica per immagini e laboratori analisi a Milano,
            Monza, Bergamo, Brescia e nella provincia.
          </p>
          <div className={styles.heroStats}>
            <div className={styles.heroStat}>
              <span className={styles.heroStatNum}>{sedi.length}</span>
              <span className={styles.heroStatLabel}>Centri totali</span>
            </div>
            <div className={styles.heroStatDiv} />
            <div className={styles.heroStat}>
              <span className={styles.heroStatNum}>{poliambulatori.length}</span>
              <span className={styles.heroStatLabel}>Poliambulatori</span>
            </div>
            <div className={styles.heroStatDiv} />
            <div className={styles.heroStat}>
              <span className={styles.heroStatNum}>{citta.length}</span>
              <span className={styles.heroStatLabel}>Città</span>
            </div>
            <div className={styles.heroStatDiv} />
            <div className={styles.heroStat}>
              <span className={styles.heroStatNum}>2000+</span>
              <span className={styles.heroStatLabel}>Specialisti</span>
            </div>
          </div>
        </div>
      </section>

      {/* ── PROVINCE TAG ─────────────────────────────────── */}
      <div className={styles.provinceBand}>
        <div className={styles.provinceInner}>
          <span className={styles.provinceLabel}>Presenti in:</span>
          {province.map((p) => (
            <span key={p} className={styles.provinceTag}>
              {PROVINCE[p] ?? p}
            </span>
          ))}
        </div>
      </div>

      {/* ── CARD GRID ────────────────────────────────────── */}
      <section className={styles.gridSection}>
        <div className={styles.gridInner}>
          <div className={styles.gridHeader}>
            <h2 className={styles.gridTitle}>Poliambulatori e centri specialistici</h2>
            <p className={styles.gridSub}>
              Clicca su una sede per scoprire servizi, orari e come raggiungerla.
            </p>
          </div>

          <div className={styles.cardGrid}>
            {poliambulatori.map((s) => (
              <a key={s.id} href={`/sedi/${s.id}`} className={styles.sedeCard}>
                <div className={styles.sedeCardImgWrap}>
                  {s.foto_url
                    ? <img src={s.foto_url} alt={s.nome} className={styles.sedeCardImg} /> // eslint-disable-line @next/next/no-img-element
                    : <div className={styles.sedeCardImgPlaceholder} />
                  }
                  <span className={styles.sedeCardCitta}>{s.citta}</span>
                  <span className={styles.sedeCardTipoBadge}>{TIPO_LABEL[s.tipo] ?? s.tipo}</span>
                </div>
                <div className={styles.sedeCardBody}>
                  <h3 className={styles.sedeCardNome}>{s.nome}</h3>
                  <p className={styles.sedeCardAddr}>
                    <span className={styles.sedeCardAddrIcon}>📍</span>
                    {s.indirizzo}
                  </p>
                  {s.orari?.lun_ven && (
                    <p className={styles.sedeCardOrari}>
                      <span className={styles.sedeCardAddrIcon}>🕐</span>
                      Lun–Ven: {s.orari.lun_ven}
                    </p>
                  )}
                  {s.telefono && (
                    <p className={styles.sedeCardTel}>
                      <span className={styles.sedeCardAddrIcon}>📞</span>
                      {s.telefono}
                    </p>
                  )}
                  <span className={styles.sedeCardCta}>Scopri la sede →</span>
                </div>
              </a>
            ))}
          </div>

          {puntiPrelievi.length > 0 && (
            <>
              <div className={styles.gridHeader} style={{marginTop: "56px"}}>
                <h2 className={styles.gridTitle}>Punti Prelievi SSN</h2>
                <p className={styles.gridSub}>
                  Accesso diretto senza appuntamento nelle prime ore del mattino.
                </p>
              </div>
              <div className={styles.prelievoGrid}>
                {puntiPrelievi.map((s) => (
                  <a key={s.id} href={`/sedi/${s.id}`} className={styles.prelievoCard}>
                    <div className={styles.prelievoIcon}>🩸</div>
                    <div className={styles.prelievoBody}>
                      <h4 className={styles.prelievoNome}>{s.nome}</h4>
                      <p className={styles.prelievoAddr}>📍 {s.indirizzo}, {s.citta}</p>
                      {s.orari?.lun_ven && <p className={styles.prelievoOrari}>🕐 Lun–Ven: {s.orari.lun_ven}</p>}
                      {s.telefono && <p className={styles.prelievoTel}>📞 {s.telefono}</p>}
                    </div>
                    <span className={styles.prelievoArrow}>→</span>
                  </a>
                ))}
              </div>
            </>
          )}
        </div>
      </section>

      {/* ── STORE LOCATOR (mappa interattiva) ────────────── */}
      <section className={styles.locatorSection}>
        <div className={styles.locatorHeader}>
          <h2 className={styles.locatorTitle}>Trova la sede più vicina</h2>
          <p className={styles.locatorSub}>Esplora la mappa o cerca per città</p>
        </div>
        <SediPageClient sedi={sedi} />
      </section>

      {/* ── CTA ──────────────────────────────────────────── */}
      <section className={styles.ctaSection}>
        <div className={styles.ctaInner}>
          <h2 className={styles.ctaTitle}>Prenota in una delle nostre sedi</h2>
          <p className={styles.ctaSub}>
            Scegli la struttura più comoda per te e prenota online in pochi click.
          </p>
          <a href="/cerca" className={styles.ctaBtn}>Cerca una prestazione →</a>
        </div>
      </section>
    </>
  );
}
