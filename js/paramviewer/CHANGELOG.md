# @gradio/paramviewer

## 0.3.0

### Highlights

#### Custom component documentation generator ([#7030](https://github.com/gradio-app/gradio/pull/7030) [`3a944ed`](https://github.com/gradio-app/gradio/commit/3a944ed9f162a224d26959a9c556346a9d205311))

If your custom component has type hints and docstrings for both parameters and return values, you can now automatically generate a documentation page and README.md with no additional effort. Simply run the following command:

```sh
gradio cc docs
```

This will generate a Gradio app that you can upload to spaces providing rich documentation for potential users. The documentation page includes:

- Installation instructions.
- A live embedded demo and working code snippet, pulled from your demo app.
- An API reference for initialising the component, with types, default values and descriptions.
- An explanation of how the component affects the user's predict function inputs and outputs.
- Any additional interfaces or classes that are necessary to understand the API reference.
- Optional links to GitHub, PyPi, and Hugging Face Spaces.

A README will also be generated detailing the same information but in a format that is optimised for viewing on GitHub or PyPi!

 Thanks [@pngwn](https://github.com/pngwn)!

### Features

- [#7069](https://github.com/gradio-app/gradio/pull/7069) [`07d520c`](https://github.com/gradio-app/gradio/commit/07d520c7a2590eb5544bd0b17f82ea31ecf43e00) - fix versions.  Thanks [@pngwn](https://github.com/pngwn)!