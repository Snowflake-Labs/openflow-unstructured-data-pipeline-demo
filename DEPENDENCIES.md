<!--
Copyright 2025 Snowflake Inc.
SPDX-License-Identifier: Apache-2.0

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->

# Third-Party Dependencies and Licenses

This document lists all third-party dependencies used in the Unstructured Document Intelligence Demo project and their respective licenses.

## Project License

This project is licensed under the **Apache License 2.0**. See [LICENSE](LICENSE) file for details.

## Development Dependencies

All development dependencies are used for documentation generation and Google API integration.

### Documentation Tools

| Package | Version | License | PyPI Link |
|---------|---------|---------|-----------|
| **mkdocs** | ≥1.6.0 | BSD License | [PyPI](https://pypi.org/project/mkdocs/) |
| **mkdocs-material** | ≥9.5.0 | MIT License | [PyPI](https://pypi.org/project/mkdocs-material/) |
| **mkdocs-glightbox** | ≥0.4.0 | MIT License | [PyPI](https://pypi.org/project/mkdocs-glightbox/) |
| **mkdocs-include-markdown-plugin** | ≥6.2.5 | Apache 2.0 | [PyPI](https://pypi.org/project/mkdocs-include-markdown-plugin/) |
| **mkdocs-macros-plugin** | ≥1.3.0 | MIT License | [PyPI](https://pypi.org/project/mkdocs-macros-plugin/) |
| **mkdocs-mermaid2-plugin** | ≥1.1.1 | MIT License | [PyPI](https://pypi.org/project/mkdocs-mermaid2-plugin/) |
| **mkdocs-minify-plugin** | ≥0.8.0 | MIT License | [PyPI](https://pypi.org/project/mkdocs-minify-plugin/) |
| **mkdocs-redirects** | ≥1.2.1 | MIT License | [PyPI](https://pypi.org/project/mkdocs-redirects/) |
| **mkdocs-git-revision-date-localized-plugin** | ≥1.2.9 | MIT License | [PyPI](https://pypi.org/project/mkdocs-git-revision-date-localized-plugin/) |
| **mkdocs-git-committers-plugin-2** | ≥2.4.0 | MIT License | [PyPI](https://pypi.org/project/mkdocs-git-committers-plugin-2/) |
| **pygments** | ≥2.18.0 | BSD-2-Clause | [PyPI](https://pypi.org/project/pygments/) |
| **pymdown-extensions** | ≥10.11.2 | MIT License | [PyPI](https://pypi.org/project/pymdown-extensions/) |

### Google API Tools

| Package | Version | License | PyPI Link |
|---------|---------|---------|-----------|
| **google-auth** | ≥2.22.0 | Apache 2.0 | [PyPI](https://pypi.org/project/google-auth/) |
| **google-API-Python-client** | ≥2.97.0 | Apache 2.0 | [PyPI](https://pypi.org/project/google-api-python-client/) |

## License Summary

### By License Type

| License Type | Count | Percentage |
|--------------|-------|------------|
| **MIT License** | 10 | 71% |
| **Apache 2.0** | 3 | 21% |
| **BSD License** | 2 | 14% |

**Total Dependencies**: 14 packages

### License Compatibility

All dependencies use OSI-approved, permissive licenses that are compatible with this project's Apache 2.0 license:

✅ **MIT License** - Very permissive, allows commercial use, modification, and distribution  
✅ **Apache License 2.0** - Explicit patent grants, same as project license  
✅ **BSD License** - Permissive license with minimal restrictions

## License Texts

### MIT License

The MIT License is used by the majority of our dependencies. Key permissions:

- ✅ Commercial use
- ✅ Modification
- ✅ Distribution
- ✅ Private use

**Conditions**: License and copyright notice must be included.

### Apache License 2.0

Used by this project and several dependencies. Key features:

- ✅ Commercial use
- ✅ Modification
- ✅ Distribution
- ✅ Patent use
- ✅ Private use

**Conditions**: License and copyright notice, state changes, include NOTICE file if present.

### BSD License (BSD-2-Clause)

Very permissive license similar to MIT. Key permissions:

- ✅ Commercial use
- ✅ Modification
- ✅ Distribution
- ✅ Private use

**Conditions**: License and copyright notice must be included.

## Compliance

### Attribution Requirements

When distributing this project, ensure you:

1. ✅ Include this `DEPENDENCIES.md` file
2. ✅ Include the project's `LICENSE` file
3. ✅ Retain all copyright notices from dependencies
4. ✅ Include license texts for all dependencies (if redistributing)

### No Runtime Dependencies

This project has **no runtime dependencies** - all dependencies are development-only tools for:

- Documentation generation (MkDocs and plugins)
- Google Drive integration testing (Google API clients)

Users of the demo do not need to install these dependencies unless they are:

- Building documentation locally
- Modifying documentation
- Running Google Drive API verification scripts

## Updates

This dependency list was last verified: **January 2025**

To update this file with current license information:

```bash
python3 scripts/check_licenses.py  # (if script exists)
```

Or manually verify each package at their PyPI pages linked above.

## References

- **Open Source Initiative (OSI)**: <https://opensource.org/licenses>
- **Choose a License**: <https://choosealicense.com/>
- **SPDX License List**: <https://spdx.org/licenses/>
- **Python Package Index (PyPI)**: <https://pypi.org/>

---

**Note**: This file documents dependencies defined in `pyproject.toml`. Transitive dependencies (dependencies of dependencies) inherit their parent package's license compatibility.

For questions about licensing, please open an issue in the project repository or contact the maintainers.
