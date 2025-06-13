import React, { useState } from 'react';

function UserForm() {
  const [formData, setFormData] = useState({ name: '', email: '' });
  const [message, setMessage] = useState('');

  const handleChange = e => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      const response = await fetch('/submit', {  // <--- relative path
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData)
      });
      const data = await response.json();
      setMessage(data.message);
      setFormData({ name: '', email: '' });
    } catch (error) {
      setMessage("Error submitting data.");
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>User Info Form</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="name"
          placeholder="Enter name"
          value={formData.name}
          onChange={handleChange}
          required
        /><br /><br />
        <input
          type="text"
          name="msg"
          placeholder="Enter message"
          value={formData.email}
          onChange={handleChange}
          required
        /><br /><br />
        <button type="submit">Submit</button>
      </form>
      <p>{message}</p>
    </div>
  );
}

export default UserForm;
