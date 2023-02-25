

let table = document.getElementById('product_table');

// function (){
// 	if (!text){
// 		console.log('no text');
// 		return false;
// 	} else {
// 		for (i=0; i<table.rows.length; i++){
// 			if (table.rows[i].cells[0].innerHTML.includes(text)){
// 				console.log(table.rows[i].cells[0].innerHTML);
// 				console.log('spx');
// 			} else {
// 				table.deleteRow(i);
// 				console.log('ledete');
// 				};
// 			};
// 		};
// };


let textbox = document.getElementById('products_filter_text');

textbox.addEventListener('keyup', function (){
	let filtered_table = table;
	let text = this.value;
	if (!text){
		for (row of table.rows){
			$(row).show();
		}
	} else {
		for (row of table.rows){
			if ($(row).parent().is('thead')){
				continue;
			}
			else if (row.cells[0].innerHTML.toLowerCase().includes(text.toLowerCase())){
				$(row).show();
			} else {
				$(row).hide();
				}
			}
		}
	}
);
