old


function copyValues(sourceRow, destinationRow){
    for (let i=1; i<n_cols; i++){
        table.rows[destinationRow].cells[i].innerHTML = table.rows[sourceRow].cells[i].innerHTML
    };
};


function fillCosts(copyMap){
    for (key in copyMap){
        copyValues(key, copyMap[key]);
    };
};


function addRows(){
    var rows = {"Koszty operacyjne": [9, 29],
                "Koszty surowca": [30, 38],
                "Koszty personelu": [39, 45]
                };

    for (let row in rows) {
        let row1 = table.insertRow(rows[row][0]);
        let cell1 = row1.insertCell(0);
        cell1.innerHTML = row;
        cell1.colSpan = n_cols;
        cell1.align = 'center'

        let row2 = table.insertRow(rows[row][1]);
        let cell2 = row2.insertCell(0);
        cell2.innerHTML = 'Suma';
        for (let n=1; n<n_cols; n++){
            let cell6 = row2.insertCell(n);
        };   
    };
};