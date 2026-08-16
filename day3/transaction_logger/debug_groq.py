import os
import sys
import traceback
from groq import Groq

print("--- DIAGNOSTIC RUN ---")
print("Python Executable:", sys.executable)
print("GROQ_API_KEY set?:", bool(os.environ.get("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")))

try:
    client = Groq()
    print("Sending request to Groq...")
    
    response = client.chat.completions.create(
        model="groq/compound-mini",
        messages=[{"role": "user", "content": "Ping"}]
    )
    print("\nSUCCESS!")
    print("Response:", response.choices[0].message.content)

except Exception as err:
    print("\n--- DETAILED ERROR TRACEBACK ---")
    print("Error Type:", type(err).__name__)
    print("Error Details:", err)
    print("\nFull Stack Trace:")
    traceback.print_exc()