let count = 1;


function render(q, t) {
    questions = JSON.parse(q);
    test = JSON.parse(t)[0];


    base = $('#test');

    base.append(`<h1>Score: ${test['fields']['score'].toFixed(2)}%</h1>`)

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
            html += `<input class="custom-control-input" type="radio" id="${id}" name="${question['pk']}" disabled>`;
            html += `<label class="custom-control-label" for="${id}">${choices[i]}</label>`;
            html += `</div>`;
        }
    }
    return html;
}