
var table = document.getElementById("pnl_table");



const get_table_width = function(){
    let row = table.rows[0];
    count = row.childElementCount;
    return count;
};



function widenRows(rows){
    let n_cols = get_table_width();
    for (row of rows) {
        let wide_cell = table.rows[row].cells[0];
        wide_cell.colSpan = n_cols;
        wide_cell.align = 'center';
        for (let i=1; table.rows[row].cells.length>1; i++){
            table.rows[row].deleteCell(1);
        };
    };
};



function boldenRows(rowNumbers){
    for (row of rowNumbers){
        let row2 = table.rows[row];
        for (cell of row2.cells){
            cell.innerHTML = '<b>' + cell.innerText + '</b>'
        };
    };
};



let boldRows = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 29, 30, 38, 39, 45, 46, 47, 48, 49];
let wideRows = [9, 30, 39];


boldenRows(boldRows);
widenRows(wideRows);





