import pytest

# Test web app home page
def test_swagger_page(test_client):
    """
    GIVEN Surfers API Web Service
    WHEN the '/docs' page is requested (GET)
    THEN check that the response is valid
    """
    _response = test_client.get('/docs')
    assert _response.status_code == 200, "Check Swagger site is responsive"
    assert b'Surfers FastAPI Accelerator' in _response.content, "Check Swagger site title"

# Test against the health check page to ensure ok response
def test_healthcheck_page(test_client):
    """
    GIVEN Service health check web page
    WHEN the '/api/v1/healthz' page is requested (GET)
    THEN check that all responses are valid and healthy
    """
    _response = test_client.get('/api/v1/healthz')
    assert _response.status_code == 200, "Check that health page is responsive"
    assert b'health' in _response.content, "Check that it is health page accessed"
    assert b'ok' in _response.content, "Check health page reporting status ok"

# Test that the 404 error condition is caught
def test_unknown_page(test_client):
    """
    GIVEN An unknown web page to ensure 404 caught
    WHEN the '/unknown' page is requested (GET)
    THEN check that the error is raised
    """
    
    _response = test_client.get('/unknown')
    assert _response.status_code == 404, "Check that 404 error raised when incorreect page accesed"
    assert b"Not Found" in _response.content, "Check that error message correct for 404"

# test that the API spec is valid
def test_api_spec(test_client):
    """
    GIVEN Swagger API definition
    WHEN the 'api/v1/api-docs' is requested
    THEN validate the API structure
    """

    _response = test_client.get('/api/v1/api-docs')
    assert _response.status_code == 200, "Check that openapi doc accessible"
    assert b"openapi" in _response.content, "Check that content of openapi doc readable"
