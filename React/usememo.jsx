import React, {useMemo, useState} from 'react'

function usememo() {
    const [count,setCount] = useState('0')

    const memoval = useMemo(square,[count])

    const square = (x)=>{
        setCount(count=x*x)
    }
  return (
    <div>usememo</div>
  )
}

export default usememo