# Assessment 0: sample project

This is a sample project to help you get started and verify your local setup.
Note that in this example we provide you with a sample structure for the code and tests; we are not suggesting that these are necessarily a good example.
In the real exercises, it will be your responsibility to design a good API and write suitable test cases.

However, we would generally expect that your submission contains a `README.md` file, a `Dockerfile`, and a `run.sh` script which builds and runs the Docker image.
See the [Submitting your code](#submitting-your-code) section for more details.


## Setup

For this assessment, you will need to install the following:

- Python 3.12+
- [Docker](https://docs.docker.com/get-docker/)


## Development

For local development, you will want to create a virtual environment and install the dependencies.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

You can run all tests with:

```bash
python -m unittest discover -v -s tests
```

You can check your types with:

```bash
mypy .
```


## Testing your submission

Your submission will be solely tested via the Docker image.
You can replicate our testing environment by running the `run.sh` script.
This will build the Docker image and run the tests inside it.
If you run this repository as is, you will see that some tests fail, as the implementation is intentionally left incomplete.

```bash
$ ./run.sh
[+] Building 1.5s (13/13)
[...]
test_blake2b_default_length (test_diggest.TestDigest.test_blake2b_default_length) ... ERROR
test_init_checks_for_too_large_output_length (test_diggest.TestDigest.test_init_checks_for_too_large_output_length) ... FAIL
test_sha256_custom_length (test_diggest.TestDigest.test_sha256_custom_length) ... FAIL
test_sha256_default_length (test_diggest.TestDigest.test_sha256_default_length) ... ok
[...]
```


## Submitting your code

Once you completed the exercise, you will create a .zip file with the contents of your project.
Make sure to exclude the `.venv` directory (and similar).
All submissions should contain a `README.md` file, a `Dockerfile`, and a `run.sh` script which builds and runs the Docker image.
It is a good idea to double check that your submission is self-contained by opening the zip file on a different machine and double checking that the `run.sh` script works.
Include your lab report as a PDF file named `{csrid}_submission{nr}_report.pdf`.

Name the file `{csrid}_submission{nr}.zip`.
For example, Daniel's submission for the first exercise would be named `dh623_submission1.zip`.
