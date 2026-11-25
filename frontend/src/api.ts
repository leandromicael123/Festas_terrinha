export interface EdicaoFesta {
  id: number;
  festa: number;
  nome_festa: string;
  localidade: string;
  organizador: number;
  ano: number;
  data_inicio: string;
  data_fim: string;
  recinto: string;
  latitude: number;
  longitude: number;
  preco: string;
  aprovada: boolean;
}

export async function obterEdicoes(signal: AbortSignal): Promise<EdicaoFesta[]> {
  const resposta = await fetch("/api/catalogo/edicoes/", { signal });
  if (!resposta.ok) throw new Error("Falha na consulta das edições.");
  return resposta.json();
}
