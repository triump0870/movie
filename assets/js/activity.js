$("movieClick").click(function(){
    $.get("http://localhost:8000/movies/1", function(data, status){
        alert("Data: " + data + "\nStatus: " + status);
        console.log(data);
    });
});