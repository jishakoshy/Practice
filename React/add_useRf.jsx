import React, { useState } from 'react'

function add_useRf() {
    const countRef = useRef(0);
    const [,forceUpdate] = useState();

    const increment = ()=>{
        countRef.current += 1
        forceUpdate({});
    }

    const decrement = ()=>{
        countRef.current -= 1
        forceUpdata({});
    }

  return (
    <div>
        <h1>Count:{countRef.current}</h1>
        <button onClick={increment}>+</button>
        <button onClick={decrement}>-</button>
    </div>
  )
}

export default add_useRf