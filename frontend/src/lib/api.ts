const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export interface Prestazione {
  id: number;
  nome: string;
  codice: string;
  branca: string;
  descrizione: string;
  prezzo_solvente: number | null;
  strutture: string[];
  medici: string[];
  fondi: string[];
}

export interface SearchResult {
  count: number;
  results: Prestazione[];
}

export interface Struttura {
  id: number;
  nome: string;
  citta: string;
  tipo: string;
}

export async function searchPrestazioni(
  query: string,
  struttura?: string,
  fondo?: string
): Promise<SearchResult> {
  const params = new URLSearchParams({ q: query });
  if (struttura) params.append("struttura", struttura);
  if (fondo) params.append("fondo", fondo);

  const res = await fetch(`${API_URL}/api/prestazioni/search/?${params}`);
  if (!res.ok) return { count: 0, results: [] };
  return res.json();
}

export async function getSuggestions(query: string): Promise<string[]> {
  if (query.length < 2) return [];
  const res = await fetch(`${API_URL}/api/prestazioni/suggestions/?q=${encodeURIComponent(query)}`);
  if (!res.ok) return [];
  const data = await res.json();
  return data.suggestions;
}

export interface PrestazioneDetail {
  id: number;
  nome: string;
  codice: string;
  branca: string;
  descrizione: string;
  prezzo_solvente: number | null;
  strutture: { id: number; nome: string; citta: string; indirizzo: string; telefono: string }[];
  medici: { nome: string; specializzazione: string; scheda_cms_id: number | null }[];
  fondi: { nome: string; codice: string }[];
}

export async function getPrestazioneDetail(id: number): Promise<PrestazioneDetail | null> {
  const res = await fetch(`${API_URL}/api/prestazioni/${id}/`);
  if (!res.ok) return null;
  return res.json();
}

export async function getStrutture(): Promise<Struttura[]> {
  const res = await fetch(`${API_URL}/api/strutture/`);
  if (!res.ok) return [];
  const data = await res.json();
  return data.results;
}

export interface Sede {
  id: number;
  nome: string;
  tipo: string;
  indirizzo: string;
  cap: string;
  citta: string;
  provincia: string;
  telefono: string;
  email: string;
  lat: number | null;
  lng: number | null;
  foto_url: string;
  orari: Record<string, string>;
}

export interface SedeDetail extends Sede {
  descrizione: string;
  servizi: string[];
}

const SERVER_API = process.env.API_URL ?? API_URL;

export async function getSedi(): Promise<Sede[]> {
  try {
    const res = await fetch(`${SERVER_API}/api/strutture/`, { next: { revalidate: 300 } });
    if (!res.ok) return [];
    const data = await res.json();
    return data.results;
  } catch { return []; }
}

export async function getSedeDetail(id: number): Promise<SedeDetail | null> {
  try {
    const res = await fetch(`${SERVER_API}/api/strutture/${id}/`, { next: { revalidate: 300 } });
    if (!res.ok) return null;
    return res.json();
  } catch { return null; }
}
