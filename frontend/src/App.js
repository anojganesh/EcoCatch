import "./App.css";
import React, { useState } from "react";
import axios from "axios";
import pic from "./pic.jpg";
function App() {
  const [searchTerm, setSearchTerm] = useState("");
  const [result, setResult] = useState("");

  const handleSearch = async () => {
    try {
      console.log(searchTerm);
      const response = await axios.post(
        "http://localhost:5000/search",
        { waterbody: searchTerm },
        { responseType: "blob" } // Specify the response type as blob
      );

      const file = new Blob([response.data], { type: "text/html" });
      const fileURL = URL.createObjectURL(file);
      window.open(fileURL);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  return (
    <div className="App">
      <header
        style={{ backgroundImage: `url(${pic})`, backgroundSize: "cover" }}
        className="App-header"
      >
        <div></div>
        <div className="title">
          <h1>EcoCatch</h1>
          <p className="slogan">Where Sustainable Fishing Begins</p>
        </div>
        <div className="wrap">
          <div className="search">
            <input
              type="text"
              className="searchTerm"
              placeholder="Search for a waterbody..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
            />
            <button
              type="submit"
              className="searchButton"
              onClick={handleSearch}
            >
              Search
            </button>
          </div>
        </div>
        
      </header>
    </div>
  );
}

export default App;
