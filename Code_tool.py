import json
import autogen

# Load config from config.json
with open("config.json") as f:
    config = json.load(f)
llm_config = config["llm_config"]

# Define Codegenerator Agent
codegenerator = autogen.AssistantAgent(
    name="Codegenerator",
    system_message=(
        "You are a code generator. Only generate code in response to programming language queries. "
        "Do not provide explanations, only output the code block. "
        "If the prompt is not code-related, reply with: 'This is only a code related tool.'"
    ),
    llm_config=llm_config,
    human_input_mode="NEVER"
)

# Define Codevalidator Agent
codevalidator = autogen.AssistantAgent(
    name="Codevalidator",
    system_message=(
        "You are a code validator. Check the given code for errors. "
        "If errors are found, explain each error clearly. "
        "If no errors, reply with exactly: 'No errors found.'"
    ),
    llm_config=llm_config,
    human_input_mode="NEVER"
)

def is_code_related(response):
    """Check if the response is the code tool rejection message."""
    return not (response.strip() == "This is only a code related tool.")

def agentive_code_tool():
    print("Welcome to the Agentive Code Tool!")
    print("Type your programming/code task, or 'q' to quit.\n")
    while True:
        user_prompt = input("Enter your programming task: ").strip()
        if user_prompt.lower() == "q":
            print("Exiting. Goodbye!")
            break
        if not user_prompt:
            print("Please enter a non-empty programming task.")
            continue

        # Step 1: Generate code
        code = codegenerator.generate_reply(messages=[{"role": "user", "content": user_prompt}])
        if not is_code_related(code):
            print("\n[Codegenerator]: I'm here to generate code.If you need any code-related assistance, let me know!\n")
            continue

        print(f"\n[Codegenerator] Generated code:\n{code}")

        iteration = 1
        while True:
            print(f"\n--- Iteration {iteration} ---")
            # Step 2: Validate code
            validation = codevalidator.generate_reply(messages=[{"role": "user", "content": code}]).strip()
            print(f"\n[Codevalidator] Validation result:\n{validation}")

            if validation.lower().strip() == "no errors found.":
                print("\n✅ Final Output (Code is valid):\n", code)
                break

            # Step 3: Send errors to code generator for fixing
            print("\n[Codevalidator] Errors found, sending back to Codegenerator for fixes.")
            fix_prompt = (
                f"The following errors were found in your code:\n{validation}\n"
                "Please fix these errors and return only the corrected code."
            )
            code = codegenerator.generate_reply(messages=[{"role": "user", "content": fix_prompt}])
            print(f"\n[Codegenerator] Corrected code:\n{code}")
            iteration += 1

if __name__ == "__main__":
    agentive_code_tool()
