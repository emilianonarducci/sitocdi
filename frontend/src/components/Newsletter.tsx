"use client";
import { useState } from "react";
import styles from "./Newsletter.module.css";

export default function Newsletter() {
  const [form, setForm] = useState({ nome: "", cognome: "", email: "", privacy: false });
  const [sent, setSent] = useState(false);

  function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    if (!form.privacy || !form.email) return;
    setSent(true);
  }

  return (
    <section className={styles.section}>
      <div className={styles.card}>
        {/* Left: form */}
        <div className={styles.formSide}>
          <h2 className={styles.title}>La tua salute, inizia da qui.</h2>
          <p className={styles.subtitle}>
            Iscriviti alla newsletter e scopri i migliori consigli per la tua salute.
          </p>

          {sent ? (
            <p className={styles.success}>Grazie per l&apos;iscrizione!</p>
          ) : (
            <form className={styles.form} onSubmit={handleSubmit}>
              <div className={styles.row}>
                <input
                  className={styles.input}
                  type="text"
                  placeholder="Nome"
                  value={form.nome}
                  onChange={(e) => setForm({ ...form, nome: e.target.value })}
                />
                <input
                  className={styles.input}
                  type="text"
                  placeholder="Cognome"
                  value={form.cognome}
                  onChange={(e) => setForm({ ...form, cognome: e.target.value })}
                />
              </div>
              <input
                className={styles.input}
                type="email"
                placeholder="E-mail"
                required
                value={form.email}
                onChange={(e) => setForm({ ...form, email: e.target.value })}
              />
              <div className={styles.footer}>
                <label className={styles.checkLabel}>
                  <input
                    type="checkbox"
                    className={styles.checkbox}
                    checked={form.privacy}
                    onChange={(e) => setForm({ ...form, privacy: e.target.checked })}
                    required
                  />
                  <span>
                    Autorizzo al trattamento dei dati{" "}
                    <a href="#" className={styles.privacyLink}>(leggi l&apos;informativa)</a>
                  </span>
                </label>
                <button type="submit" className={styles.btn}>
                  Iscriviti ora →
                </button>
              </div>
            </form>
          )}
        </div>

        {/* Right: photo */}
        <div className={styles.imgSide}>
          {/* eslint-disable-next-line @next/next/no-img-element */}
          <img
            src="https://images.unsplash.com/photo-1563986768609-322da13575f3?w=800&q=80&auto=format&fit=crop&crop=center"
            alt=""
            className={styles.img}
          />
        </div>
      </div>
    </section>
  );
}
