"use client";
import dynamic from "next/dynamic";
import { useState } from "react";
import type { Sede } from "@/lib/api";
import styles from "./page.module.css";

const StoreMap = dynamic(() => import("@/components/StoreMap"), {
  ssr: false,
  loading: () => <div className={styles.mapLoading}>Caricamento mappa...</div>,
});

export default function SediPageClient({ sedi }: { sedi: Sede[] }) {
  const [activeSedId, setActiveSedId] = useState<number | null>(null);
  const [search, setSearch] = useState("");

  const validSedi = sedi.filter((s) => s.lat && s.lng);

  const filtered = validSedi.filter((s) =>
    search.trim() === "" ||
    s.nome.toLowerCase().includes(search.toLowerCase()) ||
    s.citta.toLowerCase().includes(search.toLowerCase())
  );

  const visibleIds = search.trim() === "" ? null : filtered.map((s) => s.id);

  return (
    <div className={styles.locatorStack}>
      <div className={styles.locatorSearchBar}>
        <input
          className={styles.searchInput}
          placeholder="Cerca per nome o città..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
        <span className={styles.count}>
          {filtered.length} {filtered.length === 1 ? "sede" : "sedi"}
        </span>
      </div>
      <div className={styles.mapWrap}>
        <StoreMap
          sedi={validSedi}
          activeSedId={activeSedId}
          onMarkerClick={setActiveSedId}
          visibleIds={visibleIds}
        />
      </div>
    </div>
  );
}
