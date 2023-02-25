
var confirmationVal = 0;


function confirmDelete(){
	// let txt = {{ recipe }};	
	let confirmPopup = confirm(`Czy na pewno chcesz usunąć recepturę ${recipe_name}?`);
	if (confirmPopup == true){
		confirmationVal = 1;
	} else {
		confirmationVal = 0;
	}
	$('#confirmation').val(confirmationVal);
};

