const url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQ4LqWDC5VX3wfmviVHG0y1XonV8oY3iAlomsi-1V9Lv6PKhEjOta8YsCmMtzwpQS7TLYJcfhx4aJys/pub?gid=1239458077&single=true&output=csv';
fetch(url).then(r => r.text()).then(data => {
    console.log("Raw Data:", JSON.stringify(data));
    const rows = data.split('\n').map(row => row.split(','));
    console.log("Rows:", rows);
    const status = rows[1][0].trim().toLowerCase();
    const message = rows[1].slice(1).join(',').trim().replace(/^"|"$/g, '');
    console.log("Status:", status, status === 'on');
    console.log("Message:", message);
}).catch(console.error);
