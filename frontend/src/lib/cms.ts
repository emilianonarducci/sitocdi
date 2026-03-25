// API_URL is server-only (Docker internal); NEXT_PUBLIC_API_URL is used on the client
const API = process.env.API_URL ?? process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

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

const isDev = process.env.NODE_ENV === "development";

async function fetchCMS<T>(path: string, tags?: string[]): Promise<T | null> {
  try {
    const res = await fetch(`${API}/api/cms/${path}`,
      isDev
        ? { cache: "no-store" }
        : { next: { revalidate: 300, tags } }
    );
    if (!res.ok) return null;
    return res.json();
  } catch {
    return null;
  }
}

export const getHeroSlides = () => fetchCMS<HeroSlide[]>("hero/", ["cms-hero"]);
export const getConsigliati = () => fetchCMS<ConsigliatiCard[]>("consigliati/", ["cms-consigliati"]);
export const getPercheSceglierci = () => fetchCMS<PercheSceglierciData>("perche-sceglierci/", ["cms-perche"]);
export const getSalutePerTe = () => fetchCMS<SalutePerTeArticolo[]>("salute-per-te/", ["cms-salute"]);

export interface TitoloAccademico {
  anno: string;
  titolo: string;
}

export interface EsperienzaProfessionale {
  anno: string;
  descrizione: string;
}

export interface SchedaMedico {
  id: number;
  nome_completo: string;
  specializzazione: string;
  ruolo: string;
  foto_url: string;
  bio: string;
  titoli_accademici: TitoloAccademico[];
  esperienze_professionali: EsperienzaProfessionale[];
  pubblicazioni: string;
  link_prenota: string;
}

export const getMedici = () => fetchCMS<SchedaMedico[]>("medici/", ["cms-medici"]);
export const getMedico = (id: number) => fetchCMS<SchedaMedico>(`medici/${id}/`, ["cms-medici", `cms-medico-${id}`]);
