
        // This script listens for changes on the image input and logs the selected file to the console.
        document.addEventListener('DOMContentLoaded', function() {
    const imageInput = document.getElementById('imageInput');
    const preview = document.getElementById('preview');

    imageInput.addEventListener('change', async function(event) {
        const file = event.target.files[0];

        if (!file) return;

        // ✅ Preview
        console.log('Selected file:', file);
        preview.src = URL.createObjectURL(file);
        preview.style.display = 'block';

        // UI before sending
        document.getElementById('result').querySelector('span').textContent = file.name;
        document.getElementById('confidence').querySelector('span').textContent = 'Uploading...';
        document.getElementById('conclusion').querySelector('span').textContent = 'Sending to server...';

        // ✅ Prepare form data
        const formData = new FormData();
        formData.append('image', file);

        try {
            // ✅ Send to Flask API
            const response = await fetch('http://127.0.0.1:5000/upload', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();
            console.log(data)
            // ✅ Handle success 


            if (response.ok) {
                document.getElementById('result').querySelector('span').textContent = data.prediction; //data.prediction.toFixed(2) data.confidence:.2f
                document.getElementById('confidence').querySelector('span').textContent = data.confidence.toString().slice(0, 5);;
                document.getElementById('conclusion').querySelector('span').textContent = data.message;
                console.log("input goten")
            } else {
                // API returned error (400, etc.)
                document.getElementById('confidence').querySelector('span').textContent = 'Error';
                document.getElementById('conclusion').querySelector('span').textContent = data.error;
            }

        } catch (error) {
            // ❌ Network / server error
            console.error('Error:', error);
            document.getElementById('confidence').querySelector('span').textContent = 'Failed';
            document.getElementById('conclusion').querySelector('span').textContent = 'Server not reachable';
        }
    });
});