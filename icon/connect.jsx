// src/components/Item.jsx
import React from 'react';

const Item = ({ name, price }) => {
  return (
    <div className="item">
      <h3>{name}</h3>
      <p>Price: ₹{price}</p>
    </div>
  );
};

export default Item;
