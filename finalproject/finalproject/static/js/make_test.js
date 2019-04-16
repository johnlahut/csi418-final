let count = 1;
let questions = [];

$(document).ready(function() {
    $('#questionTable').DataTable({
        searching: true,
        columnsDefs: [{
            ordertable: false,
            className: 'select-checkbox',
            targets: 0
        }],
        ordering: false,
        select: {
            style: 'os',
            selector: 'td:first-child'
        }
    });
    $('.dataTables_length').addClass('bs-select');
});

function addQuestion(button) {
    question_id = $(button).parent().attr('id').split('-')[1];

    $.ajax({
        url: '../get_question/' + question_id + '/',
        type: 'GET',
        success: function f(data) {
            renderQuestion(data);
        }
    });
}

function renderQuestion(data) {

    if (questions.indexOf(data['id']) >= 0)
        return;

    parent = $('#test-preview');

    html = `
    <div class="col-2">
        <p class="h5">Question ${count}:</p>
    </div>

    <div class="col-10 ml-5">
        <p class="lead">${data['question']}</p>
    </div>

    <div class="text-center">
        <figure class="figure">
            <img src="#" class="figure-img img-fluid rounded" alt="Image not found!">
            <figcaption class="figure-caption text-center"></figcaption>
        </figure>
    </div>

    <div class="custom-control custom-radio">
        <div class="row">
            <div class="col-6">
                <input class="custom-control-input" type="radio" id="choice_1">
                <label class="custom-control-label" for="choice_1">${data['choice_1']}</label>
            </div>
            <div class="col-6">
                <input class="custom-control-input" type="radio" id="choice_2">
                <label class="custom-control-label" for="choice_2">${data['choice_2']}</label>
            </div>
        </div>
    
    
        <div class="row">
            <div class="col-6">
                <input class="custom-control-input" type="radio" id="choice_3">
                <label class="custom-control-label" for="choice_3">${data['choice_3']}</label>
            </div>
    
            <div class="col-6">
                <input class="custom-control-input" type="radio" id="choice_4">
                <label class="custom-control-label" for="choice_4">${data['choice_4']}</label>
            </div>
        </div>
    </div>
    <hr>
    `;

    count++;
    parent.append(html);
    questions.push(data['id']);
}

function createTest(csrf) {

}

