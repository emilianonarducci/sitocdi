import styles from "./AppDownload.module.css";

export default function AppDownload() {
  return (
    <section className={styles.section}>
      <div className={styles.inner}>

        {/* Left */}
        <div className={styles.left}>
          <h2 className={styles.title}>
            La tua salute sempre con te,
            <br />scarica la nostra app.
          </h2>

          <div className={styles.appRow}>
            <div className={styles.appIcon}>
              <svg width="48" height="48" viewBox="0 0 48 48" fill="none">
                <path d="M24 4L4 16v16l20 12 20-12V16L24 4z" stroke="#003087" strokeWidth="2" strokeLinejoin="round"/>
                <path d="M24 4v24M4 16l20 9 20-9" stroke="#003087" strokeWidth="1.5" strokeLinejoin="round"/>
                <path d="M14 10l10 6 10-6" stroke="#003087" strokeWidth="1.2" strokeLinejoin="round"/>
                <path d="M14 32l10-6 10 6" stroke="#003087" strokeWidth="1.2" strokeLinejoin="round"/>
              </svg>
            </div>
            <div>
              <p className={styles.appName}>CDI Care</p>
              <ul className={styles.features}>
                <li>Gestisci le tue prenotazioni</li>
                <li>Visualizzi l&apos;agenda con gli appuntamenti</li>
                <li>Scegli e prenoti le tue visite</li>
                <li>Consulti i dettagli della tua polizza</li>
              </ul>
            </div>
          </div>

          {/* Store badges */}
          <div className={styles.storeButtons}>

            {/* Apple App Store */}
            <a href="#" className={styles.badge}>
              <svg className={styles.badgeIcon} viewBox="0 0 24 29" fill="white" xmlns="http://www.w3.org/2000/svg">
                <path d="M19.665 15.23c-.031-3.27 2.67-4.845 2.793-4.924-1.522-2.222-3.887-2.527-4.726-2.56-2.01-.204-3.928 1.185-4.944 1.185-1.02 0-2.588-1.156-4.257-1.124-2.186.033-4.21 1.27-5.335 3.21-2.285 3.955-.583 9.802 1.637 13.007 1.086 1.567 2.37 3.323 4.065 3.26 1.632-.065 2.244-1.055 4.214-1.055 1.966 0 2.53 1.055 4.254 1.02 1.755-.03 2.864-1.594 3.936-3.17 1.25-1.813 1.762-3.577 1.788-3.667-.038-.017-3.42-1.315-3.425-5.182z"/>
                <path d="M16.355 5.28c.894-1.088 1.5-2.594 1.334-4.1-1.29.052-2.87.862-3.797 1.928-.827.958-1.562 2.51-1.367 3.985 1.44.11 2.912-.732 3.83-1.813z"/>
              </svg>
              <div className={styles.badgeText}>
                <span className={styles.badgeSub}>Scarica su</span>
                <span className={styles.badgeMain}>App Store</span>
              </div>
            </a>

            {/* Google Play */}
            <a href="#" className={styles.badge}>
              {/* Official Google Play triangle icon with 4 colors */}
              <svg className={styles.badgeIcon} viewBox="0 0 24 27" xmlns="http://www.w3.org/2000/svg">
                <path d="M1.5 0.5C0.9 0.85 0.5 1.5 0.5 2.3v22.4c0 0.8 0.4 1.45 1 1.8l0.1 0.05 12.55-12.55v-0.3L1.5 0.5z" fill="#4285F4"/>
                <path d="M18.35 18.15l-4.2-4.2v-0.3l4.2-4.2 0.1 0.05 4.97 2.82c1.42 0.81 1.42 2.12 0 2.93l-4.97 2.82-0.1 0.08z" fill="#FBBC04"/>
                <path d="M18.45 18.07L14.15 13.77 1.5 26.5c0.47 0.5 1.24 0.56 2.1 0.07l14.85-8.5" fill="#EA4335"/>
                <path d="M18.45 9.47L3.6 0.97C2.74 0.48 1.97 0.54 1.5 1.04L14.15 13.77l4.3-4.3z" fill="#34A853"/>
              </svg>
              <div className={styles.badgeText}>
                <span className={styles.badgeSub}>DISPONIBILE SU</span>
                <span className={styles.badgeMain}>Google Play</span>
              </div>
            </a>

          </div>
        </div>

        {/* Right: iPhone mockup */}
        <div className={styles.right}>
          <div className={styles.phone}>
            <div className={styles.dynamicIsland} />
            <div className={styles.statusBar}>
              <span className={styles.time}>9:41</span>
              <div className={styles.statusIcons}>
                <svg width="17" height="11" viewBox="0 0 17 11" fill="white">
                  <rect x="0" y="5" width="3" height="6" rx="1"/>
                  <rect x="4.5" y="3.5" width="3" height="7.5" rx="1"/>
                  <rect x="9" y="2" width="3" height="9" rx="1"/>
                  <rect x="13.5" y="0" width="3" height="11" rx="1"/>
                </svg>
                <svg width="15" height="11" viewBox="0 0 15 11" fill="white">
                  <path d="M7.5 9a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3z"/>
                  <path d="M3 5.5C4.4 4.2 5.9 3.5 7.5 3.5s3.1.7 4.5 2" stroke="white" strokeWidth="1.4" fill="none" strokeLinecap="round"/>
                  <path d="M.5 3C2.5 1.1 4.9.1 7.5.1s5 1 7 2.9" stroke="white" strokeWidth="1.4" fill="none" strokeLinecap="round"/>
                </svg>
                <svg width="27" height="13" viewBox="0 0 27 13" fill="white">
                  <rect x="0.5" y="0.5" width="23" height="12" rx="3.5" stroke="white" strokeOpacity=".4" fill="none"/>
                  <rect x="2" y="2" width="19" height="9" rx="2"/>
                  <path d="M25 4.5v4a2.5 2.5 0 000-4z" fill="white" fillOpacity=".45"/>
                </svg>
              </div>
            </div>

            <div className={styles.screen}>
              <div className={styles.appHeader}>
                <div className={styles.headerLogo}>
                  <svg width="20" height="20" viewBox="0 0 22 22" fill="none">
                    <path d="M11 2L2 7v8l9 5 9-5V7L11 2z" stroke="#003087" strokeWidth="1.8" strokeLinejoin="round"/>
                    <path d="M11 2v13M2 7l9 4.5L20 7" stroke="#003087" strokeWidth="1.3" strokeLinejoin="round"/>
                  </svg>
                  <div className={styles.headerLogoText}>
                    <span className={styles.headerCDI}>CDI</span>
                    <span className={styles.headerSub}>LIFE FROM INSIDE</span>
                  </div>
                </div>
                <div className={styles.profileBtn}>
                  <svg width="15" height="15" viewBox="0 0 16 16" fill="none">
                    <circle cx="8" cy="5.5" r="2.5" stroke="#003087" strokeWidth="1.4"/>
                    <path d="M2.5 14c0-3 2.5-5 5.5-5s5.5 2 5.5 5" stroke="#003087" strokeWidth="1.4" strokeLinecap="round"/>
                  </svg>
                </div>
              </div>

              <div className={styles.welcomeRow}>
                <div className={styles.avatarCircle}>
                  <svg width="36" height="36" viewBox="0 0 36 36">
                    <circle cx="18" cy="18" r="18" fill="#dbeafe"/>
                    <circle cx="18" cy="13" r="6" fill="#93c5fd"/>
                    <ellipse cx="18" cy="30" rx="11" ry="8" fill="#93c5fd"/>
                  </svg>
                </div>
                <div>
                  <div className={styles.ciaoText}>Ciao</div>
                  <div className={styles.nameText}>Luca!</div>
                </div>
              </div>

              <div className={styles.blueCard}>
                <p className={styles.blueCardTitle}>Prenota una visita<br/>o un esame</p>
                <p className={styles.blueCardSub}>
                  Inizia la tua esplorazione: trova un esame, una prestazione medica o un medico specialista.
                </p>
                <div className={styles.searchBar}>
                  <span className={styles.searchPlaceholder}>Cerca per esame, prestazione o medico</span>
                  <div className={styles.searchBtn}>
                    <svg width="12" height="12" viewBox="0 0 13 13" fill="none">
                      <circle cx="5.5" cy="5.5" r="4" stroke="white" strokeWidth="1.5"/>
                      <path d="M8.5 8.5l3 3" stroke="white" strokeWidth="1.5" strokeLinecap="round"/>
                    </svg>
                  </div>
                </div>
              </div>

              <div className={styles.prenotazioniCard}>
                <span className={styles.prenotazioniTitle}>Le tue prenotazioni</span>
              </div>
            </div>
          </div>
        </div>

      </div>
    </section>
  );
}
