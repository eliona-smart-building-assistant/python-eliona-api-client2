docker run --rm ^
    -v "%cd%":/local ^
    openapitools/openapi-generator-cli:v7.13.0 ^
    generate ^
    -g python ^
    --git-user-id eliona-smart-building-assistant ^
    --git-repo-id python-eliona-api-client2 ^
    -i https://raw.githubusercontent.com/eliona-smart-building-assistant/eliona-api/main/openapi.yaml ^
    -o /local ^
    --additional-properties="packageName=eliona.api_client2,packageVersion=2.9.3,projectName=Python Eliona API client 2"
