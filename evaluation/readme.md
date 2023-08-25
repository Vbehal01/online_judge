#evaluation

post route: /evaluation/
method post:

request body:
{
    "body": str,
    "test_case_id": int
}
response body:
{
    "output": str
}