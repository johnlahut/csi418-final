// $(document).ready(function() {
//
// };
//

let count = 1;
let questions;

function render(questionsJSON, testJSON) {

    questions = JSON.parse(questionsJSON);
    test = JSON.parse(testJSON)[0];

    base = $('#test');

    console.log(questions);

    base.append(
        `<h1 class="m-4">${test['fields']['name']}</h1>`
    );

    for (question of questions) {
        base.append(getQuestion(question));
        count++;
    }
}

function getQuestion(question) {
    question_fields = question['fields'];

    choices = [
        question_fields['choice_1'],
        question_fields['choice_2'],
        question_fields['choice_3'],
        question_fields['choice_4'],
        question_fields['choice_5'],
        question_fields['choice_6']
    ];

    html =  `<hr>
            <h3 class="mt-3">Question: ${count}</h3>
            <h5>${question_fields['question']}</h5>
            `;

    for(i=0; i<choices.length; i++) {

        choice = choices[i];

        if (choice != null) {
            id = `${count}_id_${i}`;
            html += '<div class="custom-control custom-radio">';
            html += `<input class="custom-control-input" type="radio" id="${id}" name="${question['pk']}" required>`;
            html += `<label class="custom-control-label" for="${id}">${choices[i]}</label>`;
            html += `</div>`;
        }
    }
    return html;
}


function bindAnswers() {

    answers = {};

    for (question of questions) {
        selected_ans = $('input[name=' + question['pk'] + ']:checked').attr('id');
        selected_ans = parseInt(selected_ans.split('_')[2]) + 1;

        answers[question['pk']] = selected_ans;

    }
    data = JSON.stringify(answers);
    console.log(data);

    $('#answerData').val(JSON.stringify(answers));

    // $('#test').append(
    //     `<input type="text" value="${JSON.stringify(answers)}" id="mydat">`
    // );
}