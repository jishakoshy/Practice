# how to mount, unmount,update in react?

# import React, { useState, useEffect } from "react";

# function Example() {
#   const [count, setCount] = useState(0);

#   // Mounting
#   useEffect(() => {
#     console.log("Component mounted");
#   }, []);

#   // Updating
#   useEffect(() => {
#     console.log("Component updated");
#   }, [count]);

#   // Unmounting
#   useEffect(() => {
#     return () => {
#       console.log("Component unmounted");
#     };
#   }, []);

#   return (
#     <div>
#       <h1>Count: {count}</h1>
#       <button onClick={() => setCount(count + 1)}>Increment</button>
#     </div>
#   );
# }

# export default Example;