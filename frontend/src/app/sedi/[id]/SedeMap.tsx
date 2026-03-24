"use client";
import dynamic from "next/dynamic";
import type { Sede } from "@/lib/api";
import styles from "./page.module.css";

const StoreMap = dynamic(() => import("@/components/StoreMap"), {
  ssr: false,
  loading: () => <div className={styles.mapLoading}>Caricamento mappa...</div>,
});

export default function SedeMap({ sede }: { sede: Sede }) {
  return (
    <div className={styles.mapBox}>
      <StoreMap sedi={[sede]} activeSedId={sede.id} onMarkerClick={() => {}} singleMode />
    </div>
  );
}
