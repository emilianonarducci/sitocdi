"use client";
import { useState, useEffect, useRef } from "react";
import { useRouter } from "next/navigation";
import { getStrutture, getSuggestions, type Struttura } from "@/lib/api";
import styles from "./SearchBar.module.css";

export default function SearchBar() {
  const router = useRouter();
  const [query, setQuery] = useState("");
  const [struttura, setStruttura] = useState("");
  const [data, setData] = useState("");
  const [strutture, setStrutture] = useState<Struttura[]>([]);
  const [suggestions, setSuggestions] = useState<string[]>([]);
  const [showSuggestions, setShowSuggestions] = useState(false);
  const debounceRef = useRef<ReturnType<typeof setTimeout> | null>(null);
  const wrapperRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    getStrutture().then(setStrutture);
  }, []);

  useEffect(() => {
    function handleClick(e: MouseEvent) {
      if (wrapperRef.current && !wrapperRef.current.contains(e.target as Node)) {
        setShowSuggestions(false);
      }
    }
    document.addEventListener("mousedown", handleClick);
    return () => document.removeEventListener("mousedown", handleClick);
  }, []);

  function handleQueryChange(value: string) {
    setQuery(value);
    if (debounceRef.current) clearTimeout(debounceRef.current);
    if (value.length < 2) {
      setSuggestions([]);
      setShowSuggestions(false);
      return;
    }
    debounceRef.current = setTimeout(async () => {
      const list = await getSuggestions(value);
      setSuggestions(list);
      setShowSuggestions(list.length > 0);
    }, 250);
  }

  function selectSuggestion(s: string) {
    setQuery(s);
    setSuggestions([]);
    setShowSuggestions(false);
  }

  function handleSearch(e: React.FormEvent) {
    e.preventDefault();
    if (!query.trim()) return;
    const params = new URLSearchParams({ q: query });
    if (struttura) params.append("struttura", struttura);
    if (data) params.append("data", data);
    router.push(`/cerca?${params.toString()}`);
  }

  return (
    <section className={styles.section}>
      <div className="container">
        <div className={styles.card}>
          <div className={styles.header}>
            <div className={styles.headerText}>
              <h2>Prenota una visita o un esame</h2>
              <p>Cerca l&apos;esame o la prestazione, indica il centro e la data in cui vuoi effettuarla</p>
            </div>
            <a href="#" className={styles.iniziaDaQui}>
              <span>Inizia da qui</span>
              <span className={styles.iniziaIcon}>◈</span>
            </a>
          </div>

          <form onSubmit={handleSearch}>
            <div className={styles.searchPill}>

              <div className={styles.pillField} ref={wrapperRef} style={{ position: "relative" }}>
                <svg className={styles.fieldIcon} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8">
                  <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/>
                  <circle cx="9" cy="7" r="4"/>
                  <path d="M23 21v-2a4 4 0 0 0-3-3.87"/>
                  <path d="M16 3.13a4 4 0 0 1 0 7.75"/>
                </svg>
                <div className={styles.fieldContent}>
                  <label>Visita o Esame</label>
                  <input
                    type="text"
                    value={query}
                    onChange={(e) => handleQueryChange(e.target.value)}
                    onFocus={() => suggestions.length > 0 && setShowSuggestions(true)}
                    placeholder="Es. visita cardiologica, ECG..."
                    autoComplete="off"
                  />
                </div>
                {showSuggestions && (
                  <ul className={styles.suggestions}>
                    {suggestions.map((s) => (
                      <li key={s} onMouseDown={() => selectSuggestion(s)}>
                        <span className={styles.suggIcon}>🔍</span> {s}
                      </li>
                    ))}
                  </ul>
                )}
              </div>

              <div className={styles.divider} />

              <div className={styles.pillField}>
                <svg className={styles.fieldIcon} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8">
                  <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>
                  <circle cx="12" cy="10" r="3"/>
                </svg>
                <div className={styles.fieldContent}>
                  <label>Sede o modalità di visita</label>
                  <select value={struttura} onChange={(e) => setStruttura(e.target.value)} className={styles.selectField}>
                    <option value="">Tutti i centri</option>
                    {strutture.map((s) => (
                      <option key={s.id} value={s.nome}>{s.nome} — {s.citta}</option>
                    ))}
                  </select>
                </div>
              </div>

              <div className={styles.divider} />

              <div className={styles.pillField}>
                <svg className={styles.fieldIcon} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8">
                  <rect x="3" y="4" width="18" height="18" rx="2" ry="2"/>
                  <line x1="16" y1="2" x2="16" y2="6"/>
                  <line x1="8" y1="2" x2="8" y2="6"/>
                  <line x1="3" y1="10" x2="21" y2="10"/>
                </svg>
                <div className={styles.fieldContent}>
                  <label>Data</label>
                  <input
                    type="date"
                    value={data}
                    onChange={(e) => setData(e.target.value)}
                    className={styles.dateField}
                    min={new Date().toISOString().split("T")[0]}
                  />
                </div>
              </div>

              <button type="submit" className={styles.cercaBtn}>
                Cerca →
              </button>
            </div>
          </form>
        </div>
      </div>
    </section>
  );
}
