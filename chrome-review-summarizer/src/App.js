import React from "react";
import Ratings from "./Ratings";
import "./App.css";

const App = () => {
  return (
    <div className="app">
      <h1>Hello World</h1>
      <div className="small-area">
        <Ratings ratings={[["Good Mileage", "98%"], ["Comfortable Ride", "30%"], ["Spacious Interior", "78%"], ["Smooth Handling", "75%"], ["Advanced Features", "90%"]]} />
      </div>
      <div className="medium-area">
        <Ratings ratings={[["Good Mileage", "98%"], ["Comfortable Ride", "30%"], ["Spacious Interior", "78%"], ["Smooth Handling", "75%"], ["Advanced Features", "90%"]]} />
      </div>
      <div className="large-area">
        <Ratings ratings={[["Good Mileage", "98%"], ["Comfortable Ride", "30%"], ["Spacious Interior", "78%"], ["Smooth Handling", "75%"], ["Advanced Features", "90%"]]} />
      </div>
    </div>
  );
}

export default App;