// using useState
// import React, { useState } from 'react'

// function add_sub() {
//     const [count,setCount] = useState('0')

//   return (
//     <div>
//         <h1>Count:{count}</h1>
//         <button onClick={()=>setCount(count+1)}>+</button>
//         <button onClick={()=>setCount(count-1)}>-</button>
//     </div>
//   )
// }

// export default add_sub


// using useReducer
import React, { useReducer } from 'react'

const initialState = {count:0};

function reducer(state,action){
    switch (action.type){
        case 'increment':
            return {count: state.count + 1}
        case 'decrement':
            return {count: state.count - 1}
    }
}

function add_subt() {
    const [state, dispatch] = useReducer(reducer,initialState);

  return (
    <div>
        <h1>Count:{}</h1>
        <button>+</button>
        <button>-</button>
    </div>
  )
}

export default add_subt
