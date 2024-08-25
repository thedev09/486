import React, { useState } from 'react';

function App() {
  const [jsonData, setJsonData] = useState('');
  const [apiResponse, setApiResponse] = useState(null);
  const [selectedOptions, setSelectedOptions] = useState([]);

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      // Validate JSON input
      JSON.parse(jsonData);

      // Call API
      const response = await fetch('/bfhl', { // Adjust API endpoint as needed
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ data: jsonData }),
      });

      if (response.ok) {
        const data = await response.json();
        setApiResponse(data);
      } else {
        // Handle API errors
        console.error('API Error:', response.status, response.statusText);
      }
    } catch (error) {
      // Handle JSON parsing errors
      console.error('Invalid JSON:', error);
    }
  };

  const handleOptionChange = (event) => {
    const selected = Array.from(event.target.selectedOptions, (option) => option.value);
    setSelectedOptions(selected);
  };

  // Render filtered response based on selected options
  const renderFilteredResponse = () => {
    if (!apiResponse) return null;

    const filteredData = {};
    selectedOptions.forEach((option) => {
      filteredData[option] = apiResponse[option]; 
    });

    return <pre>{JSON.stringify(filteredData, null, 2)}</pre>;
  };

  return (
    <div>
      <h1>Your Roll Number</h1> {/* Set your roll number here */}

      <form onSubmit={handleSubmit}>
        <textarea 
          value={jsonData} 
          onChange={(e) => setJsonData(e.target.value)} 
          placeholder="Enter JSON data here..." 
        />
        <button type="submit">Submit</button>
      </form>

      {apiResponse && (
        <div>
          <select multiple value={selectedOptions} onChange={handleOptionChange}>
            <option value="alphabets">Alphabets</option>
            <option value="numbers">Numbers</option>
            <option value="highest_lowercase_alphabet">Highest Lowercase Alphabet</option>
          </select>

          {renderFilteredResponse()}
        </div>
      )}
    </div>
  );
}

export default App;
