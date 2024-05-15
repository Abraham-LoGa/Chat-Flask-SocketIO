import React, { useRef } from "react";
import { useState, useEffect } from "react";

function App(){
  const [message, setMessage] = useState(" ")
  const [messages, setMessages] = useState([]);
  const inputRef = useRef(null)
  const handleSubmit = (e) =>{
    e.preventDefault();
    setMessages([...messages, message])
    setMessage("")
    if (inputRef.current){
      inputRef.current.value = "";
    }
  }
  useEffect(()=>{

  })
  return(
    <div className='h-screen  bg-zinc-800 text-white flex items-center justify-center'>
      <form onSubmit={handleSubmit} className="bg-zinc-900 p-10">
        <h1 className="text-2xl font-bold my-2"> Chat App</h1>
        <input type="text" placeholder="Escribe tu mensaje ..." onChange={(e) => setMessage(e.target.value)}  ref={inputRef} className="border-2 border-zinc-500 p-2 w-full text-black"/>
        <button>Send</button>
        <ul>
        {messages.map((message, i )=>(
          <li key={i} className="my-2 p-2 table text-sm rounded-md bg-sky-700">
            <span className="text-xs text-slate-300 block">
              from
            </span>
            <span className="text-md">
              {message}
            </span>
          </li>
        ))}
      </ul>
      </form>
    </div>
  )
}
export default App;
