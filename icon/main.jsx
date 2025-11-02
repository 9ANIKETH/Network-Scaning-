// src/Main.jsx or src/App.jsx
import React from 'react';
import Item from './components/Item';

const Main = () => {
  return (
    <div>
      <h2>Items List</h2>
      <Item name="Shirt" price={500} />
      <Item name="Shoes" price={1200} />
    </div>
  );
};

export default Main;
