const tesseract = require("node-tesseract-ocr");
// Function to convert image to table
async function imageToTable(imagePath) {
  // Read the image using OpenCV
  const img = cv.imread(imagePath);

  // Convert the image to grayscale
  const gray = img.cvtColor(cv.COLOR_BGR2GRAY);

  // Save the grayscale image (optional, for visualization purposes)
  cv.imwrite('gray_image.png', gray);

  // Use Tesseract to do OCR on the image
  const { text } = await Tesseract.process(gray, {
    oem: 1, // Use LSTM OCR Engine
  });

  // Split the text into lines
  const lines = text.split('\n');

  // Create a list to store rows of the table
  return lines;
}

// Example usage
const imagePath = 'test2.png';
imageToTable(imagePath)
  .then(resultTable => {
    // Print the resulting table
    resultTable.forEach(row => {
      console.log(row);
    });
  })
  .catch(error => {
    console.error('Error:', error);
  });
