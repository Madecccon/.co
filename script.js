document.getElementById("menuIcon").addEventListener("click", function(){
    var menu = document.getElementById("menu");
    menu.classList.toggle("active");    
});

document.getElementById("searchButton").addEventListener("click", function(){
    var searchInput = document.getElementById("searchInput").Value;
    //perform search based on searchInput, you can replace this with your actual search logic
    alert("You searched for: " + searchInput);   
});