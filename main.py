import uuid
from typing import List


def define_env(env):
    @env.macro
    def quiz(question: str, answers: List[str]):
        return "<div class=\"admonition question\">" +\
               "<p class=\"admonition-title\">" + question + "</p>" +\
               "<div class=\"quiz__answers\">" + "".join(answers) + "</div>" +\
               "</div>"

    @env.macro
    def answer(text: str):
        id = str(uuid.uuid4())
        return "<div class=\"quiz__answer\">" +\
            "<input id=\"" + id + "\" type=\"checkbox\" />" +\
            "<label for=\"" + id + "\"> " + text + "</label>" +\
            "</div>"
