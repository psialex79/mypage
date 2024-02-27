document.addEventListener("DOMContentLoaded", function() {
    // Предполагается, что у вас есть endpoint `/bitcoin-data/` возвращающий данные для Bitcoin
    fetch('/bitcoin-data/')
    .then(response => response.json())
    .then(data => {
        var ctx = document.getElementById('bitcoinChart').getContext('2d');
        var chart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: data.data_labels, // Метки времени
                datasets: [{
                    label: 'Курс Bitcoin',
                    backgroundColor: 'rgb(60, 179, 113)', // Изменен цвет для различия графиков
                    borderColor: 'rgb(60, 179, 113)',
                    data: data.data_rates // Курсы Bitcoin
                }]
            },
            options: {}
        });
    });
});
