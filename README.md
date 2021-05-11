# WeasyPrint Azure Function

Forked from [aquavitae/docker-weasyprint](https://github.com/aquavitae/docker-weasyprint)

[Weasyprint](http://weasyprint.org/) as a microservice in an Azure Function using a docker image.

## Usage

To run locally you need:

- [Weasyprint](http://weasyprint.org/) and all prerequisites
- [Azure Functions Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local#v2)

Run the function (without docker):

```
func host start
```

A `POST` to `/api/pdf` with an html body will give a response containing a PDF. The filename may be set using a query parameter, e.g.:

```
curl -X POST -d @source.html http://127.0.0.1:7071/api/pdf?filename=result.pdf
```

This will use the file `source.html` and return a response with `Content-Type: application/pdf` and `Content-Disposition: inline; filename=result.pdf` headers.  The body of the response will be the PDF.
