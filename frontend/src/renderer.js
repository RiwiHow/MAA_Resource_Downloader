const axios = require('axios');
const API_BASE = 'http://localhost:5000/api';

document.getElementById('checkUpdate').addEventListener('click', async () => {
    try {
        const response = await axios.get(`${API_BASE}/update-check`);
        if (response.data.needs_update) {
            const statusDiv = document.getElementById('status');
            statusDiv.textContent = 'Updating resources...';
            
            await axios.post(`${API_BASE}/update`);
            statusDiv.textContent = 'Update completed!';
        } else {
            document.getElementById('status').textContent = 'No updates available';
        }
    } catch (error) {
        document.getElementById('status').textContent = `Error: ${error.message}`;
    }
});

document.getElementById('startMAA').addEventListener('click', async () => {
    try {
        await axios.post(`${API_BASE}/start-maa`);
    } catch (error) {
        document.getElementById('status').textContent = `Error: ${error.message}`;
    }
});
