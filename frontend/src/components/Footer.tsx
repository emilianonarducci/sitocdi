import styles from "./Footer.module.css";

export default function Footer() {
  return (
    <footer className={styles.footer}>
      <div className="container">
        <div className={styles.grid}>
          <div>
            {/* eslint-disable-next-line @next/next/no-img-element */}
            <img
              src="https://www.cdi.it/wp-content/themes/CDI/static/loghi/logo_cdi_50_anni_neg.svg"
              alt="CDI"
              height={36}
              style={{ marginBottom: 12 }}
            />
            <p className={styles.desc}>Centro Diagnostico Italiano.<br />Dal 1975 al servizio della salute.</p>
          </div>
          <div className={styles.col}>
            <h4>Servizi</h4>
            <ul>
              <li><a href="#">Visite specialistiche</a></li>
              <li><a href="#">Diagnostica</a></li>
              <li><a href="#">Laboratorio</a></li>
              <li><a href="#">Chirurgia</a></li>
            </ul>
          </div>
          <div className={styles.col}>
            <h4>Chi siamo</h4>
            <ul>
              <li><a href="#">La nostra storia</a></li>
              <li><a href="#">I nostri centri</a></li>
              <li><a href="#">Lavora con noi</a></li>
            </ul>
          </div>
          <div className={styles.col}>
            <h4>I Nostri Medici</h4>
            <ul>
              <li><a href="/medici">Tutti i medici</a></li>
              <li><a href="/medici#cardiologia">Cardiologia</a></li>
              <li><a href="/medici#ortopedia-e-traumatologia">Ortopedia</a></li>
              <li><a href="/medici#radiologia">Radiologia</a></li>
              <li><a href="/medici#ginecologia">Ginecologia</a></li>
            </ul>
          </div>
          <div className={styles.col}>
            <h4>Supporto</h4>
            <ul>
              <li><a href="#">Contattaci</a></li>
              <li><a href="#">FAQ</a></li>
              <li><a href="#">Privacy Policy</a></li>
            </ul>
          </div>
        </div>
        <div className={styles.bottom}>
          <span>&copy; 2026 CDI - Centro Diagnostico Italiano S.p.A.</span>
          <span>P.IVA 00000000000</span>
        </div>
      </div>
    </footer>
  );
}
