document.addEventListener("DOMContentLoaded", function() {
    var ctx = document.getElementById('currencyChart').getContext('2d');
    var chart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: dataLabels, // Массив дат, предоставляемый Django
            datasets: [{
                label: 'Курс RUB',
                backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                data: dataRates // Массив значений курса, предоставляемый Django
            }]
        },
        options: {}
    });
});
