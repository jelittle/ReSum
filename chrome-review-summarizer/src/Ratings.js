import React from "react";
import styles from "./Ratings.css";

const Ratings = ({ ratings }) => {
  return (
    <div className="ratings-div">
      <table className="ratings-table">
        <tbody>
          {ratings.map((rating, index) => (
            <tr key={index}>
              <td>
                <div className="ratings-bar">
                  <div className="ratings-bar-fill" style={{ width: `${rating[1]}` }}></div>
                  <div className="ratings-bar-unfilled" style={{ width: `${100 - rating[1]}` }}></div>
                </div>
              </td>
              <td>{rating[0]}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Ratings;