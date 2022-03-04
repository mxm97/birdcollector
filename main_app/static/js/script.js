console.log('js file is loaded')
console.log(M);

// Variables
const dateEl = document.getElementById('id_date');
const selectEl = document.getElementById('id_meal');

// Date Picket Animations
M.Datepicker.init(dateEl, {
    format: 'yyyy-mm-dd',
    defaultDate: new Date(),
    setDefaultDate: true,
    autoClose: true
});

// Select Widget Animations
M.FormSelect.init(selectEl)

