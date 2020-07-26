function update_game(data){
    
    n_players = data.slice(0,1)
    document.getElementById('test').innerHTML = " "
    for (i = 5; i < n_players*33 + 5; i+= 33){
        document.getElementById('test').innerHTML += " "
        
        character = data.slice(i,i+1)
        id = data.slice(i+1,i+3)
        y  = data.slice(i+9,i+13)
        x  = data.slice(i+13,i+17)
        width = data.slice(i+17,i+21)
        height = data.slice(i+21,i+25)
        
        test = document.getElementById("t"+id)//this element is used to show random informaiton about the player 
        p1 = document.getElementById(id)
        
        test.innerHTML = data
        p1.style.color = "blue"
        p1.style.top = y + "px"
        p1.style.left = x + "px"
        p1.style.width = width + "px"
        p1.style.height = height + "px"
        /*
        */
        
        

    }
}
function update_player(player_data){

}
document.write("Hello world")


var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        data = xhttp.responseText

        update_game(data)

        xhttp.open("GET", "http://localhost:5000/loc", true);
        xhttp.send();
        
    }
}
xhttp.open("GET", "http://localhost:5000/loc", true);
xhttp.send();
/* 
while (true){
    
    
}
};
*/

