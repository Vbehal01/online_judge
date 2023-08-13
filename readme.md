#Solver

post route: /solvers/
method: post

request body:
{"name": string,
"password": string,
"email": string
}

reponse body:
{"id": int,
"name": string,
"email": string
}

get all route: /solvers/
method: get

request body:
{}

reponse body:
[{"id": int,
"name": string,
"email": string,
submission: {"id": int,
"body": string,
"solver_id": int,
"language_id": int,
"failed_test_case_id": int}}]

get by id route: /solvers/{solver_id}
method: get

request body:
{}

reponse body:
{"id": int,
"name": string,
"email": string,
submission: {"id": int,
"body": string,
"solver_id": int,
"language_id": int,
"failed_test_case_id": int}
}

#Setter

post route: /setters/
method: post

request body:
{"name": string,
"password": string,
"email": string
}

reponse body:
{"id": int,
"name": string,
"email": string
}

get all route: /setters/
method: get

request body:
{}

reponse body:
[{"id": int,
"name": string,
"email": string,
question: {"id": int,
"title": string,
"body": string,
"author_id": int,
"level_id": int}}]

get by id route: /setters/{setter_id}
method: get

request body:
{}

reponse body:
{"id": int,
"name": string,
"email": string,
question: {"id": int,
"title": string,
"body": string,
"author_id": int,
"level_id": int}
}

#admin

post route: /admins/
method: post

request body:
{"name": string,
"password": string,
"email": string
}

reponse body:
{"id": int,
"name": string,
"email": string
}

get all route: /admins/
method: get

request body:
{}

reponse body:
[{"id": int,
"name": string,
"email": string
}]

get by id route: /admins/{admin_id}
method: get

request body:
{}

reponse body:
{"id": int,
"name": string,
"email": string
}

#question

post route: /questions/
method: post

request body:
{"title": string,
"body": string,
"author_id": int,
"level_id": int
}

reponse body:
{"id": int,
"title": string,
"body": string,
"author_id": int,
"level_id": int
}

get all route: /questions/
method: get

request body:
{}

reponse body:
[{"id": int,
"title": string,
"body": string,
"author_id": int,
"level_id": int,
solver:
{"id": int,
"name": string,
"email": string},
submission:
{"id": int,
"body": string,
"solver_id": int,
"language_id": int,
"failed_test_case_id": int},
level:
{"id": int,
"body": string},
test_case:
{ "id": int,
"input": string,
"output": string,
"ques_id": int},
tag:
{"id": int,
"body": string}}]

get by id route: /questions/{question_id}
method: get

request body:
{}

reponse body:
{"id": int,
"title": string,
"body": string,
"author_id": int,
"level_id": int,
solver:
{"id": int,
"name": string,
"email": string},
submission:
{"id": int,
"body": string,
"solver_id": int,
"language_id": int,
"failed_test_case_id": int},
level:
{"id": int,
"body": string},
test_case:
{ "id": int,
"input": string,
"output": string,
"ques_id": int},
tag:
{"id": int,
"body": string}
}

get testcase by question id route: /questions/{question_id}/test_case
method: get

request body:
{}

reponse body:
{"id": int,
"test_case_id": int
}

#language

post route: /languages/
method: post

request body:
{"title": string
}

reponse body:
{"id": int,
"title": string
}

get all route: /languages/
method: get

request body:
{}

reponse body:
[{"id": int,
"title": string,
submission:
{"id": int,
"body": string,
"solver_id": int,
"language_id": int,
"failed_test_case_id": int}}]

get by id route: /languages/{language_id}
method: get

request body:
{}

reponse body:
{"id": int,
"title": string,
submission:
{"id": int,
"body": string,
"solver_id": int,
"language_id": int,
"failed_test_case_id": int}
}

#tag

post route: /tags/
method: post

request body:
{"title": string
}

reponse body:
{"id": int,
"title": string
}

get all route: /tags/
method: get

request body:
{}

reponse body:
[{"id": int,
"title": string,
question: {"id": int,
"title": string,
"body": string,
"author_id": int,
"level_id": int}}]

get by id route: /tags/{tag_id}
method: get

request body:
{}

reponse body:
{"id": int,
"title": string,
question: {"id": int,
"title": string,
"body": string,
"author_id": int,
"level_id": int}
}

#question_tag

post route: /question_tags/{question_id}
method: post

request body:
{"tag_id": int
}

reponse body:
{"question_id": int,
"tag_id": int
}

#test_case

post route: /test_cases/{question_id}
method: post

request body:
{"input": string,
"output": string
}

reponse body:
{"id": int,
"input": string,
"output": string,
"question_id": int
}

get all route: /test_cases/
method: get

request body:
{}

reponse body:
[{"id": int,
"input": string,
"output": string,
"question_id": int,
question:
{"id": int,
"title": string,
"body": string,
"author_id": int,
"level_id": int}}]

get by id route: /test_cases/{test_case_id}
method: get

request body:
{}

reponse body:
{"id": int,
"input": string,
"output": string,
"question_id": int,
question:
{"id": int,
"title": string,
"body": string,
"author_id": int,
"level_id": int}
}

#submission

post route: /submissions/{question_id}
method: post

request body:
{"body": string,
"solver_id": int,
"language_id": int
}

reponse body:
{"id": int,
"body": string,
"solver_id": int,
"language_id": int,
"failed_test_case_id": int,
"question_id": int
}

get all route: /submissions/
method: get

request body:
{}

reponse body:
[{"id": int,
"body": string,
"solver_id": int,
"language_id": int,
"failed_test_case_id": int
question:
{"id": int,
"title": string,
"body": string,
"author_id": int,
"level_id": int},
language:
{"id": int,
"body": string},
solver: {"id": int,
"name": string,
"email": string}}]

get by id route: /submissions/{submission_id}
method: get

request body:
{}

reponse body:
{"id": int,
"body": string,
"solver_id": int,
"language_id": int,
"failed_test_case_id": int,
question:
{"id": int,
"title": string,
"body": string,
"author_id": int,
"level_id": int},
language:
{"id": int,
"body": string},
solver: {"id": int,
"name": string,
"email": string}}

#level

post route: /levels/
method: post

request body:
{"title": string
}

reponse body:
{"id": int,
"title": string
}

get all route: /levels/
method: get

request body:
{}

reponse body:
[{"id": int,
"title": string,
question:
{"id": int,
"title": string,
"body": string,
"author_id": int,
"level_id": int}}]

get by id route: /levels/{level_id}
method: get

request body:
{}

reponse body:
{"id": int,
"title": string,
question:
{"id": int,
"title": string,
"body": string,
"author_id": int,
"level_id": int}}