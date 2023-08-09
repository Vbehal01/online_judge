#Solver

post route: /solver/
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
"email": string
},{
submission: {"id": int,
"body": string,
"solver_id": int,
"language_id": int,
"test_case_id": int}}]

get by id route: /solver/{solver_id}
method: get

request body:
{}

reponse body:
{"id": int,
"name": string,
"email": string
}



#Setter

post route: /setter/
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
"email": string
},
{question: {"id": int,
"title": string,
"body": string,
"author_id": int,
"level_id": int}}]

get by id route: /setter/{setter_id}
method: get

request body:
{}

reponse body:
{"id": int,
"name": string,
"email": string
}




#admin

post route: /admin/
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

get by id route: /admin/{admin_id}
method: get

request body:
{}

reponse body:
{"id": int,
"name": string,
"email": string
}


#question

post route: /question/
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
"level_id": int
},
{solver:
{"id": int,
"name": string,
"email": string}},
{submission:
{"id": int,
"body": string,
"solver_id": int,
"language_id": int,
"test_case_id": int}},
{level: 
{"id": int,
"body": string}},
{test_case:
{ "id": int,
"input": string,
"output": string,
"ques_id": int}},
{tag: 
{"id": int,
"body": string}}]

get by id route: /question/{question_id}
method: get

request body:
{}

reponse body:
{"id": int,
"title": string,
"body": string,
"author_id": int,
"level_id": int
}


#language

post route: /language/
method: post

request body:
{"body": string
}

reponse body:
{"id": int,
"body": string
}

get all route: /languages/
method: get

request body:
{}

reponse body:
[{"id": int,
"body": string
},
{submission:
{"id": int,
"body": string,
"solver_id": int,
"language_id": int,
"test_case_id": int}}]

get by id route: /language/{language_id}
method: get

request body:
{}

reponse body:
{"id": int,
"body": string
}


#tag

post route: /tag/
method: post

request body:
{"body": string
}

reponse body:
{"id": int,
"body": string
}

get all route: /tags/
method: get

request body:
{}

reponse body:
[{"id": int,
"body": string
},
{question: {"id": int,
"title": string,
"body": string,
"author_id": int,
"level_id": int}}]

get by id route: /tag/{tag_id}
method: get

request body:
{}

reponse body:
{"id": int,
"body": string
}



#ques_tag

post route: /ques_tag/
method: post

request body:
{"ques_id": int,
"tag_id": int
}

reponse body:
{"ques_id": int,
"tag_id": int
}

get all route: /ques_tags/
method: get

request body:
{}

reponse body:
[{"ques_id": int,
"tag_id": int
}]



#test_case

post route: /test_case/
method: post

request body:
{"input": string,
"output": string,
"ques_id": int
}

reponse body:
{"id": int,
"input": string,
"output": string,
"ques_id": int
}

get all route: /test_cases/
method: get

request body:
{}

reponse body:
[{"id": int,
"input": string,
"output": string,
"ques_id": int
},
{question:
{"id": int,
"title": string,
"body": string,
"author_id": int,
"level_id": int}}]

get by id route: /test_case/{test_case_id}
method: get

request body:
{}

reponse body:
{"id": int,
"input": string,
"output": string,
"ques_id": int
}



#submission

post route: /submission/
method: post

request body:
{"body": string,
"solver_id": int,
"language_id": int,
"test_case_id": int
}

reponse body:
{"id": int,
"body": string,
"solver_id": int,
"language_id": int,
"test_case_id": int
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
"test_case_id": int
},
{question: 
{"id": int,
"title": string,
"body": string,
"author_id": int,
"level_id": int}},
{language: 
{"id": int,
"body": string}},
{solver: {"id": int,
"name": string,
"email": string
}}]

get by id route: /submission/{submission_id}
method: get

request body:
{}

reponse body:
{"id": int,
"body": string,
"solver_id": int,
"language_id": int,
"test_case_id": int
}



#level

post route: /level/
method: post

request body:
{"body": string
}

reponse body:
{"id": int,
"body": string
}

get all route: /levels/
method: get

request body:
{}

reponse body:
[{"id": int,
"body": string
},
{question: 
{"id": int,
"title": string,
"body": string,
"author_id": int,
"level_id": int}},]

get by id route: /level/{level_id}
method: get

request body:
{}

reponse body:
{"id": int,
"body": string
}