import { useEffect, useState } from "react";
import { createRoot } from "react-dom/client";
import { obterEdicoes, type EdicaoFesta } from "./api";
import "./styles.css";

const moeda = new Intl.NumberFormat("pt-PT", { style: "currency", currency: "EUR" });
const data = new Intl.DateTimeFormat("pt-PT", { day: "numeric", month: "long", year: "numeric", timeZone: "UTC" });

function dataCivil(valor: string) {
  return data.format(new Date(valor + "T00:00:00Z"));
}

function App() {
  const [edicoes, setEdicoes] = useState<EdicaoFesta[] | null>(null);
  const [erro, setErro] = useState(false);
  const [tentativa, setTentativa] = useState(0);

  useEffect(() => {
    const pedido = new AbortController();
    setErro(false);
    setEdicoes(null);
    obterEdicoes(pedido.signal)
      .then(setEdicoes)
      .catch(() => { if (!pedido.signal.aborted) setErro(true); });
    return () => pedido.abort();
  }, [tentativa]);

  return (
    <>
      <header>Rota do Arraial</header>
      <main>
        <h1>Explorar festas</h1>
        {erro ? (
          <p role="alert">Não foi possível consultar as edições. <button onClick={() => setTentativa(n => n + 1)}>Tentar novamente</button></p>
        ) : edicoes === null ? (
          <p role="status">A carregar edições…</p>
        ) : edicoes.length === 0 ? (
          <p>Ainda não há edições aprovadas.</p>
        ) : (
          <ul>{edicoes.map(edicao => (
            <li key={edicao.id}>
              <time dateTime={edicao.data_inicio}>{dataCivil(edicao.data_inicio)}</time>
              <h2>{edicao.nome_festa}</h2>
              <p>{edicao.recinto}, {edicao.localidade}</p>
              <p>{Number(edicao.preco) === 0 ? "Entrada livre" : moeda.format(Number(edicao.preco))}</p>
            </li>
          ))}</ul>
        )}
      </main>
    </>
  );
}

createRoot(document.getElementById("root")!).render(<App />);
