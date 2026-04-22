import {useState} from "react";
import Navbar from "./components/NavBar";
import UploadPanel from "./components/UploadPanel";
import ResultPanel from "./components/ResultPanel";
import Footer from "./components/Footer";
import "./styles.css";

function App(){

  const [data,setData] = useState(null);

  return(

    <div>

      <Navbar/>

      <div className="hero">
        <h1>AI Powered Resume Analyzer</h1>
        <p>Upload resume and discover best matching jobs</p>
      </div>

      <div className="dashboard">

        <UploadPanel setData={setData}/>

        <ResultPanel data={data}/>

      </div>

      <Footer/>

    </div>

  )

}

export default App;
