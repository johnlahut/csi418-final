let count = 1;
let questions = [];
let questionMap = {};

$(document).ready(function() {

    // init table, enable searching
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

    // get question ID from parent ID (table row ID)
    question_id = $(button).parent().attr('id').split('-')[1];

    // make a request to django, and handle the response in renderQuestion
    $.ajax({
        url: '../get_question/' + question_id + '/',
        type: 'GET',
        success: function f(data) {
            renderQuestion(data);
        }
    });
}

function renderQuestion(data) {

    // make sure question has not already been added
    if (questions.indexOf(data['id']) >= 0)
        return;

    parent = $('#test-preview');            // get main div to append to
    htmlId = `question_${data['id']}`;      // specific question div, log for removal

    html = `
    <div id="${htmlId}">
        <div class="col-12">
            <div class="row">
                <div class="col-auto mr-auto">
                    <p class="h5">Question ${count}:</p>
                </div>
                <div class="col-auto">
                    <button class="btn btn-danger" type="button" onclick="removeQuestion('${htmlId}')">Remove Question</button>
                </div>
            </div>
            
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
    </div>
    
    `;

    count++;                            // increment question count for display
    parent.append(html);                // add HTML to DOM
    questions.push(data['id']);         // keep track of question IDs for creating test later
    questionMap[htmlId] = html;         // map HTML tp question ID for deletion
}

function createTest(csrf) {

    // data = new FormData();
    // data.append('questions', questions);
    console.log(questions);
    $.ajax({
        url: '../make_test/',
        type: 'POST',
        data: {
            'csrfmiddlewaretoken': csrf,
            'questions': JSON.stringify(questions),
            'name': $('#test-name').val()
        },
        success: function f(data) {
            console.log(data);
        }
    });

}

function removeQuestion(htmlId) {

    id = parseInt(htmlId.split('_')[1]);            // get ID to remove from array
    questions = questions.filter(i => i !== id);    // filter from array
    delete questionMap[htmlId];                     // remove from HTML map
    $(`#${htmlId}`).remove();                       // remove from DOM
}
