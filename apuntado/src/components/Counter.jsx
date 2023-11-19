import React, { useState } from 'react'
import './Counter.css'

const Counter = () => {
    const [contador, setContador] = useState(0)

    const incrementar = () => {
        setContador(contador + 1)
    }

    const restar = () => {
        setContador(contador - 1)
    }

    return (
        <>
            <h1>{contador}</h1>
            <button onClick={incrementar}>Incrementar</button>
            <button onClick={restar}>Restar</button>
        </>
    )
}

export default Counter