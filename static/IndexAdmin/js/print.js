function imprSelec(card) {
     var contenido= document.getElementById(card).innerHTML;
     var contenidoOriginal= document.body.innerHTML;

     document.body.innerHTML = contenido;
    
     window.print();

     document.body.innerHTML = contenidoOriginal;
}