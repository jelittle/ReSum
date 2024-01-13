import React from 'react';
import Ratings from './Ratings';
import './Popup.css';

function Popup() {
  return (
    <div className='popup-container'>
      <div className='ratings-container'>
        <Ratings ratings={[["Good Mileage", "98%"], ["Comfortable Ride", "30%"], ["Spacious Interior", "78%"], ["Smooth Handling", "75%"], ["Advanced Features", "90%"]]} />
      </div>
    </div>
  );
}

export default Popup;