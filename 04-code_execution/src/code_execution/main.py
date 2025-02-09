#!/usr/bin/env python
import sys
import warnings
from pathlib import Path

from crew import CodeExecutionCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """

    file_path = 'County_Health_Rankings.csv'

    inputs = {
        'file_path': file_path
    }

    result = CodeExecutionCrew().crew().kickoff(inputs=inputs)
    print(result)

if __name__ == "__main__":
    run()
