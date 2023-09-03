// const article = document.querySelector("article");

// // `document.querySelector` may return null if the selector doesn't match anything.
// if (article) {
//   const text = article.textContent;
//   const wordMatchRegExp = /[^\s]+/g; // Regular expression
//   const words = text.matchAll(wordMatchRegExp);
//   // matchAll returns an iterator, convert to array to get word count
//   const wordCount = [...words].length;
//   const readingTime = Math.round(wordCount / 200);
//   const badge = document.createElement("p");
//   // Use the same styling as the publish information in an article's header
//   badge.classList.add("color-secondary-text", "type--caption");
//   badge.textContent = `⏱️ ${readingTime} min read`;

//   // Support for API reference docs
//   const heading = article.querySelector("h1");
//   // Support for article docs with date
//   const date = article.querySelector("time")?.parentNode;

//   (date ?? heading).insertAdjacentElement("afterend", badge);
// }

// get request to localhost:8001

function addRows(names, percentages) {
    // Create a table element
    var table = document.createElement("table");
    // Set the table border and width
    table.style.border = "1px solid black";
    table.style.width = "80%";
    // Loop through the names and percentages arrays
    for (var i = 0; i < names.length; i++) {
      // Create a row element
      var row = document.createElement("tr");
      // Create a cell element for the name
      var nameCell = document.createElement("td");
      // Set the name cell text content and alignment
      nameCell.textContent = names[i];
      nameCell.style.textAlign = "center";
      // Set the name cell border and padding
      nameCell.style.border = "1px solid black";
      nameCell.style.padding = "10px";
      // Set the name cell background color and border radius to make it a circle
      nameCell.style.backgroundColor = "lightblue";
      nameCell.style.borderRadius = "50%";
      // Create a cell element for the percentage
      var percentageCell = document.createElement("td");
      // Set the percentage cell text content and alignment
      percentageCell.textContent = percentages[i] + "%";
      percentageCell.style.textAlign = "center";
      // Set the percentage cell border and padding
      percentageCell.style.border = "1px solid black";
      percentageCell.style.padding = "10px";
      // Create a progress element for the percentage
      var progress = document.createElement("progress");
      // Set the progress value and max attributes
      progress.value = percentages[i];
      progress.max = 100;
      // Set the progress width and height
      progress.style.width = "80%";
      progress.style.height = "20px";
      // Append the progress element to the percentage cell
      percentageCell.appendChild(progress);
      // Append the name cell and the percentage cell to the row
      row.appendChild(nameCell);
      row.appendChild(percentageCell);
      // Append the row to the table
      table.appendChild(row);
    }
    // Append the table to the body of the document
    document.body.appendChild(table);
  }
  

buisnessUrl=window.location.href
fetch("http://localhost:8001/scrape/"+buisnessUrl).then(response => response.json())
console.log(respone)




