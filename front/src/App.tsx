import { useRef, useState } from "react";

function createInitialTodos() {
  const initialTodos = [];
  for (let i = 0; i <= 50; i++) {
    initialTodos.push({
      id: i,
      text: "item: " + (i + 1)
    });
  }

  return initialTodos;
}

export default function App() {
  // const [value, setValue] = useState(0)
  // const [name, setName] = useState("Matheus")
  // const [names, setNames] = useState({ firstName: "Zeca", midName: "Roger", lastName: "Pesa" })
  const [todos, setTodos] = useState(createInitialTodos)
  const [text, setText] = useState("")
  const [count, setCount] = useState(0);
  const valor = useRef(0);

  function alertHandler() {
    valor.current = valor.current + 1;
    alert("Você clicou em mim " + valor.current + " vezes");
  }

  // function handleClick() {
  //   setValue(value + 1);
  // }

  // function handleName() {
  //   setName("Isabelle");
  // }

  return (
    <div className="flex h-screen items-center justify-center">
      {/* <h1 className="text-4xl font-bold text-gray-800">Hello, World!</h1>
      <button onClick={handleClick} className="border-2 rounded-sm">Você me clicou {value} vezes</button>
      <button onClick={handleName}>Oi eu sou {name}</button>
      <a className="pt-4">Também sou {names.firstName} e {names.midName}</a>
      <label className="pt-8">Meu primeiro Nome:
        <input value={names.firstName} onChange={e => { setNames({ ...names, firstName: e.target.value }) }} className="border"></input>
      </label>
      <label>Meu segundo nome:
        <input value={names.midName} onChange={e => { setNames({ ...names, midName: e.target.value }) }}></input>
      </label> */}

      <input value={text} onChange={e => setText(e.target.value)} className="border"></input>
      <button className="border" onClick={() => { setText(""); setTodos([{ id: todos.length, text: text }, ...todos]); }}>Adicionar</button>
      {/* <ul>
        {todos.map(item => (
          <li key={item.id}>
            {item.text}
          </li>
        ))}
      </ul> */}
      
      <button className="border m-8" onClick={() => setCount(count + 1)}>Aumentar</button>
      <button className="border" onClick={() => setCount(count - 1)}>Diminuir</button>
      <button className="border" onClick={alertHandler}>Clique aqui</button>
      <Count count={count} />
    </div >
  );
}

function Count({ count }) {
  const [prevCount, setPrevCount] = useState(count);
  const [trend, setTrend] = useState("");

  if (prevCount !== count) {
    setPrevCount(count);
    setTrend(count > prevCount ? "Aumentando" : "Descendo");
  }

  return (
    <>
      <h1>{count}</h1>
      {trend && <p>O contador está {trend}</p>}
    </>
  );
}