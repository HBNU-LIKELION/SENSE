import { useEffect } from "react";

function setScreenSize() {
  let vh = window.innerHeight * 0.01;
  document.documentElement.style.setProperty("--vh", `${vh}px`);
}

function App() {
  useEffect(() => {
    setScreenSize();
  }, []);

  return (
    <div>
      ㅎㅇㅎㅇ
    </div>
  );
}

export default App;
