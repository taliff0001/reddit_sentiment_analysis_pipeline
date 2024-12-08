# Running Tests for the Reddit Sentiment Analysis Pipeline

## Prerequisites
Before running the tests, ensure you have:
1. Python 3.8 or higher installed.
2. All dependencies from `requirements.txt` installed.
   ```bash
   pip install -r requirements.txt
   ```
3. Proper configurations in `config/reddit_credentials.json` and `config/pipeline_config.json`.

---

## Running the Tests

### Using Python's `unittest` Framework
The tests are located in the `tests/` directory and are written using Python's `unittest` framework. Follow the steps below to execute them:

1. **Navigate to the Project Directory**:
   Open a terminal or command prompt and navigate to the root of the project:
   ```bash
   cd /path/to/reddit-sentiment-pipeline
   ```

2. **Run All Tests**:
   Use the `unittest` discovery mode to find and execute all test files:
   ```bash
   python -m unittest discover tests/
   ```

3. **Run a Specific Test File**:
   To run a specific test module, specify the file path:
   ```bash
   python -m unittest tests.test_data_collection
   ```

4. **Run a Specific Test Case**:
   To execute an individual test case, provide the module and test class:
   ```bash
   python -m unittest tests.test_data_collection.TestDataCollection
   ```

5. **Run a Specific Test Method**:
   To run an individual test method, provide the module, class, and method:
   ```bash
   python -m unittest tests.test_data_collection.TestDataCollection.test_authentication
   ```

---

## Output
When the tests are executed, you'll see the following:
- `.`: A dot for each passed test.
- `F`: An `F` for each failed test, followed by details about the failure.
- `E`: An `E` for each error, followed by traceback details.

Example Output:
```
....
----------------------------------------------------------------------
Ran 4 tests in 0.123s

OK
```

---

## Troubleshooting
- If tests fail due to incorrect API credentials, ensure that `config/reddit_credentials.json` is properly configured.
- If tests fail due to missing dependencies, re-install them using:
   ```bash
   pip install -r requirements.txt
   ```
- If database-related tests fail, verify your database connection settings in `config/pipeline_config.json`.

---

## Tips
- Use a virtual environment to manage dependencies for testing:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\\Scripts\\activate
   pip install -r requirements.txt
   ```
- Add a `--failfast` flag to stop the test suite after the first failure:
   ```bash
   python -m unittest discover tests/ --failfast
   ```

---

By following these instructions, you can validate the functionality and reliability of your Reddit Sentiment Analysis Pipeline.