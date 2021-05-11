#!/usr/bin/env python

import json
import logging

import azure.functions as func

from weasyprint import HTML, CSS


def main(req: func.HttpRequest) -> func.HttpResponse:
    name = req.params.get('filename', 'unnamed.pdf')

    logging.info('POST  /pdf?filename=%s' % name)

    if req.headers['Content-Type'] == 'application/json':
        data = json.loads(req.get_body().decode('utf-8'))
        html = HTML(string=data['html'])
        css = [CSS(string=sheet) for sheet in data['css']]
        pdf = html.write_pdf(stylesheets=css)
    else:
        html = HTML(string=req.get_body().decode('utf-8'))
        pdf = html.write_pdf()

    response = func.HttpResponse(body=pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline;filename=%s' % name
    logging.info(' ==> POST  /pdf?filename=%s ok' % name)
    return response
