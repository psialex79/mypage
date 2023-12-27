document.addEventListener("DOMContentLoaded", function() {
    document.getElementById('updateButton').addEventListener('click', function() {
        fetch('/update-currency-rates/')
            .then(response => {
                // Обработка ответа, например, сообщение об успехе
            })
            .catch(error => {
                // Обработка ошибки
            });
    });
});
