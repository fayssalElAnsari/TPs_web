function toc() {
  var headings = document.getElementsByTagName("h1");
  var tocTable = document.createElement("table");
  var tocList = document.createElement("ul");
  var tocItem, tocLink;
  
  tocTable.appendChild(tocList);
  document.head.innerHTML += "<style>.selected1 { background-color: yellow; } .selected2 { background-color: green; }</style>";
  document.body.insertBefore(tocTable, document.body.firstChild);
  
  for (var i = 0; i < headings.length; i++) {
    if (!headings[i].id) {
      headings[i].id = "section" + i;
    }
    tocItem = document.createElement("li");
    tocLink = document.createElement("a");
    tocLink.href =
