import React,{useEffect,useState} from React;

function lifecycle(){

    const [count,setCount] = useState()

    // mount and unmount
    useEffect(()=>{
        console.log("component is mounted")
        return()=>{
            console.log("component is unmount")
        }
    },[])

    // update
    useEffect(()=>{
        console.log("component is updated")
    },[count])

    return(
        <div><h1>{count}</h1>
        <button onclick ={()=> setCount(count+1)}>increment</button>
        </div>
        
    )
}

export default lifecycle;
