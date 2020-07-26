//mostrar mensaje de confirmacion para eliminar dato
const btnDelete= document.querySelectorAll('.btn-delete');
if(btnDelete) {
  const btnArray = Array.from(btnDelete);
  btnArray.forEach((btn) => {
    btn.addEventListener('click', (e) => {
      if(!confirm('¿Estás seguro de que quieres eliminarlo?')){
        e.preventDefault();
      }
    });
  })
}

//cerrar mensaje flash en un determinado tiempo 
$(document).ready(function(){
  $(".alert").delay(4000).slideUp(200, function() {
    $(this).alert('close');
  });
});

//limpiamos los inputs para un nuevo registro
let btnLimpia = document.querySelector('.limpia');
let inputs = document.querySelectorAll('input');

btnLimpia.addEventListener('click', () => {
  inputs.forEach(input => input.value = '');
});





