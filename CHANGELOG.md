# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0] - 2024-10-13

### Bug Fixes

- [`64f0050`](https://github.com/pufereq/simulat/commit/64f00505635f8329ebeb5a4595c6620a64ad08b5) **ollama_python_api.py**: fix error in `cleanup()` method when sessions queued
- [`97059f1`](https://github.com/pufereq/simulat/commit/97059f1cce731effabf71f4eb2262eeed6186216) b64 error
- [`f1af484`](https://github.com/pufereq/simulat/commit/f1af484c389b03fe3ba985d72bf05ddab6de78b8) error on python < 3.12

### Documentation

- [`fa3bb92`](https://github.com/pufereq/simulat/commit/fa3bb92e30c8ac923036477df363294bae4e35eb) update readme
- [`3271aeb`](https://github.com/pufereq/simulat/commit/3271aebf364a4d0e6fbcdcc8ad33c49c0c1585e0) **README.md**: add explanation to usage
- [`a176abf`](https://github.com/pufereq/simulat/commit/a176abf95146c990950442841ad0063ba7faf0d7) **rest.py**: add docstrings
- [`c581ed9`](https://github.com/pufereq/simulat/commit/c581ed9d8382fe417276c97239c78d4210cbd4ae) **README.md**: add README

### Features

- [`db93d0d`](https://github.com/pufereq/simulat/commit/db93d0d691842a1ab87406da92db35e333904e8c) **rest.py**: adjust API endpoints to adhere to changes in OllamaAPI class
- [`4532c23`](https://github.com/pufereq/simulat/commit/4532c23efe85888d26c9370bcb0ea51c99abeca9) **ollama_python_api.py**: assign contexts to session id instead of per-message
- [`9f2ee28`](https://github.com/pufereq/simulat/commit/9f2ee28abaf29a61050ce19e6b44c47ae1a1fd1d) **ollama_python_api.py**: detect language using `langdetect`, support only `pl` and `en`
- [`b7ad210`](https://github.com/pufereq/simulat/commit/b7ad21014f77d786fcbeb8837102cef52dac10f8) **translate.py**: add translation support
- [`5d75555`](https://github.com/pufereq/simulat/commit/5d7555533f149002ca2f74f50d81be2c7a34f721) **rest.py**: add `context` field in the API and provide it to `api.chat()`
- [`4377969`](https://github.com/pufereq/simulat/commit/43779699a322c7b9bb55a91e2ef86c542af313de) **storage.py**: store files in the filesystem
- [`65eed70`](https://github.com/pufereq/simulat/commit/65eed707b568248de6b27f32464e5e680472e92a) **rest.py**: implement storage
- [`d7fe86f`](https://github.com/pufereq/simulat/commit/d7fe86fb144f87091a74320d9a50f9ed83fb8871) **storage.py**: add storage
- [`870058e`](https://github.com/pufereq/simulat/commit/870058e7add33a641c26dec88f7a0743016ab921) **ollama_python_api.py**: add cleanup
- [`4792a25`](https://github.com/pufereq/simulat/commit/4792a25e2b2a519aaf5873c9e5741faaf52e3dc0) **rest.py**: add REST API
- [`d70133f`](https://github.com/pufereq/simulat/commit/d70133f35b6c8d00362d2e1bc4bbe567b06d8263) **ollama_python_api.py**: add `OllamaAPI` class

### Miscellaneous Tasks

- [`41cdcb9`](https://github.com/pufereq/simulat/commit/41cdcb9af1aee41559620a858f3de37811254d59) **system_prompt.txt**: expand the system prompt
- [`fbec2c0`](https://github.com/pufereq/simulat/commit/fbec2c0180724deea621559fab1764f2451762c9) **ollama_python_api.py**: set fallback language to English
- [`ef8dfec`](https://github.com/pufereq/simulat/commit/ef8dfecbafb7efd37974d5199eae4ebbab58f78f) **translate.py**: return translated text instead of a whole object
- [`fe04e1c`](https://github.com/pufereq/simulat/commit/fe04e1c7448661e8e6702562159b124b4a7aedd3) **translate.py**: use `langdetect`'s country codes
- [`bab4899`](https://github.com/pufereq/simulat/commit/bab4899ccc0a018ea51239b4e78fc7badebdcf3d) **system_prompt.txt**: add restrictions regarding unwanted user input and data erasing
- [`9ebf2e7`](https://github.com/pufereq/simulat/commit/9ebf2e727b77d7087a203401dd1864856d1ea1bd) **ollama_python_api.py**: add `<<END_DATA>>` marker to context prompt
- [`be8fb24`](https://github.com/pufereq/simulat/commit/be8fb245e87eb331c8cd1bcddc3fb6d43787d9dd) **ollama_python_api.py**: add `target_lang` argument to `OllamaAPI.chat()`, translation currently unused
- [`54f91f5`](https://github.com/pufereq/simulat/commit/54f91f5055ada2f1f6a48bdf4aa7655b4d7310b3) **ollama_python_api.py**: add context support in `OllamaAPI.chat()`
- [`1fd76b5`](https://github.com/pufereq/simulat/commit/1fd76b5d5e52a2672dc2857df30ca6a94126a7e0) **system_prompt.txt**: add system prompt
- [`56e928a`](https://github.com/pufereq/simulat/commit/56e928a49c6bb8d8b0198af2c6ffedff6b6a9320) change naming of storage routes
- [`8e531df`](https://github.com/pufereq/simulat/commit/8e531df3785d4107e242f2731354124d735a517c) **rest.py**: fix typo
- [`41d19c7`](https://github.com/pufereq/simulat/commit/41d19c78e3001f68951c77712eff4a5e75ed80aa) **rest.py**: handle exceptions
- [`7053c33`](https://github.com/pufereq/simulat/commit/7053c3308766c32e25c8d1424d1290ccc5251b7b) **system_prompt.txt**: add system prompt config file

### Build

- [`cb0af77`](https://github.com/pufereq/simulat/commit/cb0af7708ff1447194a4c20a0e495711e09cc0dd) **requirements.txt**: add `langdetect` depedency
- [`8e1c5a6`](https://github.com/pufereq/simulat/commit/8e1c5a663615ca16d045bf18361ffb122815573d) **requirements.txt**: add `deepl` depedency
- [`9a2ad64`](https://github.com/pufereq/simulat/commit/9a2ad64f321c5325e560c103d5702b20827dfaa3) **.gitignore**: add `stored_files/` to gitignore
- [`aa4ae30`](https://github.com/pufereq/simulat/commit/aa4ae30655c78b37c229f8e8eeba9f32c301124f) **launch.json**: add launch.json
- [`3dc9ff6`](https://github.com/pufereq/simulat/commit/3dc9ff63bfb557310d0f1fe2f8f917c15ebfbdd4) **requirements.txt**: add requirements
- [`809b9b9`](https://github.com/pufereq/simulat/commit/809b9b93700290ab68b1c806b5faef1fc535bff8) **Makefile**: add Makefile

<!-- generated by git-cliff -->
