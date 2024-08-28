import React, { useEffect } from 'react';

function MyComponent() {
  useEffect(() => {
    console.log("Component mounted");

    const handleMouseClick = () => {
      console.log("Mouse clicked");
    };

    window.addEventListener('click', handleMouseClick);

    return () => {
      console.log("Component unmounted");
      window.removeEventListener('click', handleMouseClick);
    };
  }, []);

  return (
    <div>
      <h1>Hello, world!</h1>
    </div>
  );
}

export default MyComponent;
