import os
import replicate
#Set the REPLICATE_API_TOKEN environment variable
os.environ["REPLICATE_API_TOKEN"] = "r8_JQbNwBxILxCAD6ZvFnmIsQW4niGy0TD3fbQMI"
def get_text(text):
    return text

def get_Chat_response(text):
    output = replicate.run(
    "meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",
    input={
        "prompt": get_text(text)
    }
    )
    output_string = "" 
    for item in output:
        output_string += str(item)
    return output_string