function toc() {
    // Find all the first-level headings in the document
    var headings = document.getElementsByTagName("h1");
  
    // Create a table to hold the table of contents
    var tocTable = document.createElement("table");
  
    // Add a caption to the table
    var caption = tocTable.createCaption();
    caption.innerHTML = "Table of Contents";
  
    // Add a row for each heading
    for (var i = 0; i < headings.length; i++) {
      var row = tocTable.insertRow();
  
      // Add a cell to the row
      var cell = row.insertCell();
  
      // Create a link to the heading
      var link = document.createElement("a");
      link.href = "#" + headings[i].id;
      link.innerHTML = headings[i].innerHTML;
  
      // Add the link to the cell
      cell.appendChild(link);
    }
  
    // Insert the table at the beginning of the document
    var body = document.getElementsByTagName("body")[0];
    body.insertBefore(tocTable, body.firstChild);
  }
  
window.onload = toc;