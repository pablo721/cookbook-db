
var checked_ids;

function findChecked() {
    let checkboxes = document.getElementsByTagName("input");
    let checked = Array();
    for (item of checkboxes) {
        if (item.checked) {
        checked.push(item.id);
        }
    }
    return checked;
};

function updateChecked() {
    checked_ids = findChecked();
    $('#js_data_input').val(checked_ids);
};



