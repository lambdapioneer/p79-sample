# Assignment 0: sample project

This is a sample project to help you get started and verify your local setup.
Note that in this example we provide you with a sample structure for the code and tests; we are not suggesting that these are necessarily a good example.
In the real assignments, it will be your responsibility to design a good API and write suitable test cases.

However, we would generally expect that your submission contains a `README.md` file, a `Dockerfile`, and a `run.sh` script which builds and runs the Docker image.
See the [Submitting your code](#submitting-your-code) section for more details.


## Setup

You will need to install the following:

- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- [Docker](https://docs.docker.com/get-docker/)

### Docker macOS Issue
If you experience issues with macOS identifying Docker Desktop as Malware, these resources helped me to resolve this:
- https://docs.docker.com/desktop/cert-revoke-solution/
- https://www.docker.com/blog/incident-update-docker-desktop-for-mac/
- https://github.com/docker/for-mac/issues/7527


## Development

For local development, you will want to clone the repository, install the dependencies, and then build and run the Docker image.

```bash
git clone git@github.com:lambdapioneer/p79-sample.git
cd p79-sample
uv sync
./run.sh
```

You can run all tests with:

```bash
uv run -m unittest
```

You can check your types with:

```bash
uvx ty check
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

Once you complete your implementation for an assignment, please submit it on Moodle as a .zip file with the contents of your project.
Name the file `P79_{crsid}_A{nr}.zip`, where `crsid` is your Cambridge CRSID, and `nr` is the assignment number (1 to 4).
For example, Daniel's submission for the first assignment would be named `P79_dh623_A1.zip`.
Include your lab report as a PDF file named `P79_{crsid}_A{nr}.pdf`.

All submissions should contain a `README.md` file, a `Dockerfile`, and a `run.sh` script which builds and runs the Docker image.
It is a good idea to double check that your submission is self-contained by opening the zip file on a different machine and double checking that the `run.sh` script works.
