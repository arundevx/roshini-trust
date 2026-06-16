const url = 'https://script.google.com/macros/s/AKfycbx3f_DXXzaffeMVRqrq8ZmYEHaZw4qKEvupvHlBfGQ14ZaH-OC0l-wpZ7nhhQpqkMY/exec';
const formData = new FormData();
formData.append('name', 'Test Volunteer');
formData.append('whatsapp', '9999999999');
formData.append('email', 'test@example.com');
formData.append('location', 'Test Location');
formData.append('interests', 'Donor Relationship Management');
formData.append('availability', 'Weekends only');

fetch(url, {
    method: 'POST',
    body: formData
}).then(r => r.json()).then(console.log).catch(console.error);
