document.addEventListener("DOMContentLoaded", function() {
    document.getElementById('updateButton').addEventListener('click', function() {
        fetch('/update-currency-rates/')
            .then(response => {
                if (response.ok) {
                    alert('Currency rates updated successfully!');
                    console.log('Currency rates updated successfully');
                } else {
                    alert('Failed to update currency rates. Please try again later.');
                    console.error('Failed to update currency rates:', response.statusText);
                }
            })
            .catch(error => {
                alert('Error updating currency rates. Please check your internet connection.');
                console.error('Error updating currency rates:', error);
            });
    });
});