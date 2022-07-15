# A (very) minimalist wrapper to run xmlformatter with pre-commit

This is a very minimalist wrapper to run [xmlformatter](https://pypi.org/project/xmlformatter/)
as part of a [pre-commit](http://pre-commit.com) configuration.

This hook runs xmlformatter with default arguments against
all files with an `.xml` extension in the present working directory
and all subdirectories.

## How to use

- Ensure you have `pip3` on your `$PATH` (usually installed with Python 3)
- Install the Pip3 package `xmlformatter` with the following: `pip3 install xmlformatter`
- Add the required configuration to your `.pre-commit-config.yaml` file (see below for example)
- For first-time use you may want to run your pre-commit hooks against all files: `pre-commit run --all-files`

### Example .pre-commit-config.yaml configuration
```
repos:
    - repo: https://github.com/james9001/pre-commit-hook-xmlformat
      rev: v1.0.0
      hooks:
          - id: xml-format
```

## License

The code in this repo is licensed under the [MIT License](LICENSE).