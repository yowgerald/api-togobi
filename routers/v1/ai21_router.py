""" The code is importing necessary modules and classes for the code to work properly."""
import json
from fastapi import APIRouter, Request

from ai21.task_specific import TaskSpecific

router = APIRouter()


async def startup_event():
    """
    The function "startup_event" prints a message indicating that the startup event has occurred.
    """
    print("Version 1: Startup event")


@router.post("/contextual_answer")
async def get_contextual_answer(request: Request):
    """
    The function `get_contextual_answer` takes a request, extracts the context and
    question from the request data, and uses a `TaskSpecific` object to generate a
    contextual answer based on the givencontext and question.
    """
    data = await request.json()
    context = data.get("context")
    question = data.get("question")

    task = TaskSpecific()
    response = task.contextual_answer(context=context, question=question)
    content_json = (response.content).decode("utf-8")

    return {"output": json.loads(content_json)}


async def shutdown_event():
    """
    The function `shutdown_event` prints a message indicating that a shutdown event has occurred.
    """
    print("Version 1: Shutdown event")


on_startup = [startup_event]
on_shutdown = [shutdown_event]

routes = [router]
