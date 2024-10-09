function toggleText(document) {
  var coll = document.getElementsByClassName("collapsible");
  var i;

  for (i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function() {
      this.classList.toggle("active");
      var content = this.nextElementSibling;
      if (content.style.maxHeight){
        content.style.maxHeight = null;
      } else {
        content.style.maxHeight = content.scrollHeight + "px";
      }
    });
  }
}

//   var x = document.getElementById("toggleDIV");
//   if (x.style.display === none) {
//     x.style.display = "block";
//   } else {
//     x.style.display = "none";
//   }
// }
