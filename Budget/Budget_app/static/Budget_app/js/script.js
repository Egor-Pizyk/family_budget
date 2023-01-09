const element_income = document.getElementById("Income");
if (element_income) {
    element_income.addEventListener("click", function() {
        document.getElementById('income_form').style.display = "flex";
        document.getElementById('pop_up_form').style.display = "block";
        document.getElementById('expense_form').style.display = "none";
        });
}

const element_expense = document.getElementById("Expense");
if (element_expense) {
element_expense.addEventListener("click", function() {
    document.getElementById('income_form').style.display = "none";
    document.getElementById('pop_up_form_1').style.display = "block";
    document.getElementById('expense_form').style.display = "flex";
    });
}

const new_category_hide = document.getElementById("hide_cat_form");
const new_count_form = document.getElementById("hide_count_form");
const new_transfer_hide = document.getElementById("hide_transfer_form");
const new_transaction_income_hide = document.getElementById("hide_transaction_income_form");
const new_transaction_expense_hide = document.getElementById("hide_transaction_expense_form_1");

if (new_category_hide) {
    new_category_hide.addEventListener("click", function(evt) {
        document.getElementById('create_category').style.display = "none";
        document.getElementById('pop_up_form_3').style.display = "none";
        });
}
if (new_count_form) {
    new_count_form.addEventListener("click", function(evt) {
        document.getElementById('create_count').style.display = "none";
        document.getElementById('pop_up_form_2').style.display = "none";
        });
}
if (new_transfer_hide) {
    new_transfer_hide.addEventListener("click", function(evt) {
        document.getElementById('set_transfer_to_card').style.display = "none";
        });
}
if (new_transfer_hide) {
    new_transaction_income_hide.addEventListener("click", function(evt) {
        document.getElementById('income_form').style.display = "none";
        document.getElementById('pop_up_form').style.display = "none";
        });
}
if (new_transfer_hide) {
    new_transaction_expense_hide.addEventListener("click", function(evt) {
        document.getElementById('expense_form').style.display = "none";
        document.getElementById('pop_up_form_1').style.display = "none";
        });
}

const new_category = document.getElementById("new_category");
if (new_category) {
new_category.addEventListener("click", function() {
    document.getElementById('create_count').style.display = "none";
    document.getElementById('create_category').style.display = "flex";
    document.getElementById('pop_up_form_3').style.display = "block";
    document.getElementById('set_transfer_to_card').style.display = "none";
    });
}



const new_count = document.getElementById("new_count");
if (new_count) {
new_count.addEventListener("click", function() {
    document.getElementById('create_category').style.display = "none";
    document.getElementById('create_count').style.display = "flex";
    document.getElementById('pop_up_form_2').style.display = "block";
    document.getElementById('set_transfer_to_card').style.display = "none";
    });
}

//const new_transfer = document.getElementById("new_transfer");
//if (new_transfer) {
//new_transfer.addEventListener("click", function() {
//    document.getElementById('create_category').style.display = "none";
//    document.getElementById('create_count').style.display = "none";
//    document.getElementById('set_transfer_to_card').style.display = "block";
//    });
//}
