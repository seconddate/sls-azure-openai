import logging
import openai
import os
import json
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    req_body = req.get_json()
    messages = req_body["messages"]

    if messages:
        openai.api_key = os.getenv("OPENAI_API_KEY")
        openai.api_base = os.getenv("OPENAI_ENDPOINT")
        openai.api_type = "azure"
        openai.api_version = "2023-03-15-preview"

        response = openai.ChatCompletion.create(
            engine=os.getenv("OPENAI_MODEL_NAME"),
            messages=messages,
            temperature=0.5,
            max_tokens=800,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None,
        )

        # logging.info(response["choices"][0]["message"]["content"])
        result = {"content": "", "message": ""}
        if response and response["choices"] and len(response["choices"]) > 0:
            content = response["choices"][0]["message"]["content"]
            result["content"] = content
            messages.append({"role": "assistant", "content": content})
            result["message"] = messages
            return func.HttpResponse(json.dumps(result, ensure_ascii=False))
        else:
            func.HttpResponse("Bad Request Parameter", status_code=400)
    else:
        return func.HttpResponse("Please pass a messages on the query string or in the request body", status_code=400)
