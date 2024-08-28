import React,{useEffect} from 'react'

function unmount() {
    useEffect (()=>{
        // function mount
        return()=>{
            // function unmount
        }
    },[])
  return (
    <div>
        <h1>hello world</h1>
    </div>
  )
}

export default unmount