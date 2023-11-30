import openai
import ast
class Obstacle_GPT:
    def __init__(self, api_key, init_prompt, model="gpt-4"):
        self.api_key = api_key
        self.model = model
        self.init_prompt = init_prompt
        self.dialogue_history = [{"role": "system", "content": self.init_prompt}]

    def add_message(self, role, content):
        self.dialogue_history.append({"role": role, "content": content})

    def get_response(self, user_input):
        self.add_message("user", user_input)
        openai.api_key = self.api_key

        response = openai.chat.completions.create(
            model=self.model,
            messages=self.dialogue_history
        )

        model_response = response.choices[0].message.content
        self.add_message("system", model_response)

        model_response = ast.literal_eval(model_response)

        return model_response

    def update_dialogue_history(self):
        first_message = self.dialogue_history[0]
        half_length = len(self.dialogue_history) // 2
        self.dialogue_history = [first_message] + self.dialogue_history[-half_length:]


# generator_ai = Obstacle_GPT(api_key="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", init_prompt=PROMPT)
#
# obstacle_list = generator_ai.get_response("start a generation task")
#
# obstacle_list = ast.literal_eval(obstacle_list)
#
# print(obstacle_list)
#
# print(type(obstacle_list))