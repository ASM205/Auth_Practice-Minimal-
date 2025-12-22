import { useState } from 'react';



function BookInput({ value, onChange, placeholder }) {
  return (
    <input
      type="text"
      className='input-field'
      value={value}
      onChange={(e) => onChange(e.target.value)}
      placeholder={placeholder || "Enter text..."}
      />
  );
}


export default BookInput;