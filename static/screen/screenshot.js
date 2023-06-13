// Get the capture button element
const captureBtn = document.getElementById('captureBtn');
// Add a click event listener to the button
captureBtn.addEventListener('click', function () {
    // Capture the screenshot

    html2canvas(document.getElementById('full_body')).then(function (canvas) {
        // Convert the canvas to a blob
        canvas.toBlob(function (blob) {
            // Create a temporary anchor element
            const link = document.createElement('a');
            link.href = URL.createObjectURL(blob);
            link.download = 'patient.png';

            // Programmatically click the anchor element to trigger the download
            link.click();

            // Clean up the temporary anchor element
            URL.revokeObjectURL(link.href);
            link.remove();
        });
    });
});
