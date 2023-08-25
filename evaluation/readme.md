#evaluation

post route: /evaluation/
method post:

request body:
{
    "code": str,
    "test_case_input": str
}

response body:
{
    "output": str
}