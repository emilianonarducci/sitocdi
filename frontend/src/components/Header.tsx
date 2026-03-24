"use client";
import styles from "./Header.module.css";

export default function Header() {
  return (
    <header className={styles.header}>
      <div className="container">
        <div className={styles.inner}>
          <a href="/" className={styles.logo}>
            {/* eslint-disable-next-line @next/next/no-img-element */}
            <img
              src="https://www.cdi.it/wp-content/themes/CDI/static/loghi/logo_cdi_50_anni.svg"
              alt="CDI - Centro Diagnostico Italiano"
              height={40}
            />
          </a>
          <nav>
            <ul className={styles.nav}>
              <li><a href="#">Servizi per te</a></li>
              <li><a href="#">Salute per te</a></li>
              <li><a href="#">Chi siamo</a></li>
              <li><a href="#">Supporto</a></li>
            </ul>
          </nav>
          <div className={styles.actions}>
            <button className={styles.iconBtn} aria-label="Cerca">&#128269;</button>
            <button className={styles.iconBtn} aria-label="Profilo">&#128100;</button>
            <button className={styles.langBtn}>ITA</button>
            <a href="#" className={styles.reservedBtn}>Prenota</a>
          </div>
        </div>
      </div>
    </header>
  );
}
