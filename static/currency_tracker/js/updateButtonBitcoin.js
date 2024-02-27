document.addEventListener("DOMContentLoaded", function() {
    document.getElementById('updateBitcoinButton').addEventListener('click', function() {
        fetch('/update-bitcoin-rates/')
            .then(response => {
                // Обработка ответа, например, сообщение об успехе
                console.log('Bitcoin rates updated successfully');
            })
            .catch(error => {
                // Обработка ошибки
                console.error('Error updating Bitcoin rates:', error);
            });
    });
});
