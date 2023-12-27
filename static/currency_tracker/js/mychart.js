document.addEventListener("DOMContentLoaded", function() {
    fetch('/currency-data/')
    .then(response => response.json())
    .then(data => {
        var ctx = document.getElementById('currencyChart').getContext('2d');
        var chart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: data.data_labels,
                datasets: [{
                    label: 'Курс RUB',
                    backgroundColor: 'rgb(255, 99, 132)',
                    borderColor: 'rgb(255, 99, 132)',
                    data: data.data_rates
                }]
            },
            options: {}
        });
    });
});
