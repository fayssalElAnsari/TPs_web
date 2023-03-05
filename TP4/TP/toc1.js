function toc() {
  var headings = document.getElementsByTagName("h1");
  var tocTable = document.createElement("table");
  var tocList = document.createElement("ul");
  var tocItem, tocLink;
  
  tocTable.appendChild(tocList);
  document.body.insertBefore(tocTable, document.body.firstChild);
  
  for (var i = 0; i < headings.length; i++) {
    tocItem = document.createElement("li");
    tocLink = document.createElement("a");
    tocLink.href = "#" + headings[i].id;
    tocLink.innerHTML = headings[i].innerHTML;
    tocItem.appendChild(tocLink);
    tocList.appendChild(tocItem);
  }
}
