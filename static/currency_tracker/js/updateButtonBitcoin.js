document.addEventListener("DOMContentLoaded", function() {
    document.getElementById('updateBitcoinButton').addEventListener('click', function() {
        fetch('/update-bitcoin-rates/')
            .then(response => {
                if (response.ok) {
                    alert('Bitcoin rates updated successfully!');
                    console.log('Bitcoin rates updated successfully');
                } else {
                    alert('Failed to update Bitcoin rates. Please try again later.');
                    console.error('Failed to update Bitcoin rates:', response.statusText);
                }
            })
            .catch(error => {
                alert('Error updating Bitcoin rates. Please check your internet connection.');
                console.error('Error updating Bitcoin rates:', error);
            });
    });
});