const API = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

export interface HeroSlide {
  id: number;
  badge: string;
  titolo: string;
  sottotitolo: string;
  cta_testo: string;
  cta_link: string;
  immagine_url: string;
}

export interface ConsigliatiCard {
  id: number;
  titolo: string;
  immagine_url: string;
  link: string;
}

export interface PercheSceglierciCard {
  id: number;
  variante: "light" | "mid" | "dark";
  titolo: string;
  descrizione: string;
}

export interface PercheSceglierciData {
  titolo: string;
  descrizione: string;
  immagine_sfondo_url: string;
  cards: PercheSceglierciCard[];
}

export interface SalutePerTeArticolo {
  id: number;
  tab: string;
  titolo: string;
  descrizione: string;
  immagine_url: string;
  link: string;
}

async function fetchCMS<T>(path: string): Promise<T | null> {
  try {
    const res = await fetch(`${API}/api/cms/${path}`, {
      next: { revalidate: 60 },
    });
    if (!res.ok) return null;
    return res.json();
  } catch {
    return null;
  }
}

export const getHeroSlides = () => fetchCMS<HeroSlide[]>("hero/");
export const getConsigliati = () => fetchCMS<ConsigliatiCard[]>("consigliati/");
export const getPercheSceglierci = () => fetchCMS<PercheSceglierciData>("perche-sceglierci/");
export const getSalutePerTe = () => fetchCMS<SalutePerTeArticolo[]>("salute-per-te/");
