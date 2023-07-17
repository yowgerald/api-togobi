""" The code is importing necessary modules and classes for the code to work properly."""
from fastapi import APIRouter, Body
from gpt4all import GPT4All

router = APIRouter()


async def startup_event():
    """
    The function "startup_event" prints a message indicating that the startup event has occurred.
    """
    print("Version 1: Startup event")


@router.post("/askGPT")
async def ask_gpt(prompt: str = Body(..., embed=True)):
    """
    It uses a GPT model to generate a response based on the prompt and
    returns the generated output as a response.
    """
    # https://observablehq.com/@simonw/gpt4all-models
    # gpt4all: orca-mini-3b - Orca (Small), 1.80GB download, needs 4GB RAM
    # gpt4all: ggml-gpt4all-j-v1 - Groovy, 3.53GB download, needs 8GB RAM
    # gpt4all: nous-hermes-13b - Hermes, 7.58GB download, needs 16GB RAM
    # gpt4all: orca-mini-7b - Orca, 3.53GB download, needs 8GB RAM
    # gpt4all: ggml-model-gpt4all-falcon-q4_0 - GPT4All Falcon, 3.78GB download, needs 8GB RAM
    # gpt4all: ggml-vicuna-7b-1 - Vicuna, 3.92GB download, needs 8GB RAM
    # gpt4all: ggml-wizardLM-7B - Wizard, 3.92GB download, needs 8GB RAM
    # gpt4all: ggml-mpt-7b-base - MPT Base, 4.52GB download, needs 8GB RAM
    # gpt4all: ggml-mpt-7b-instruct - MPT Instruct, 4.52GB download, needs 8GB RAM
    # gpt4all: ggml-mpt-7b-chat - MPT Chat, 4.52GB download, needs 8GB RAM
    # gpt4all: ggml-replit-code-v1-3b - Replit, 4.84GB download, needs 4GB RAM
    # gpt4all: orca-mini-13b - Orca (Large), 6.82GB download, needs 16GB RAM
    # gpt4all: GPT4All-13B-snoozy - Snoozy, 7.58GB download, needs 16GB RAM
    # gpt4all: ggml-vicuna-13b-1 - Vicuna (large), 7.58GB download, needs 16GB RAM
    # gpt4all: ggml-nous-gpt4-vicuna-13b - Nous Vicuna, 7.58GB download, needs 16GB RAM
    # gpt4all: ggml-stable-vicuna-13B - Stable Vicuna, 7.58GB download, needs 16GB RAM
    # gpt4all: wizardLM-13B-Uncensored - Wizard Uncensored, 7.58GB download, needs 16GB RAM

    # TODO: specify what model to use in body
    model = GPT4All("ggml-model-gpt4all-falcon-q4_0.bin")
    output = model.generate(prompt + " ")

    return {"message": "File uploaded successfully", "output": output}


async def shutdown_event():
    """
    The function `shutdown_event` prints a message indicating that a shutdown event has occurred.
    """
    print("Version 1: Shutdown event")


on_startup = [startup_event]
on_shutdown = [shutdown_event]

routes = [router]
