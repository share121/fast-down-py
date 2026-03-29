# fastdown

[![GitHub last commit](https://img.shields.io/github/last-commit/fast-down/fast-down-py/main)](https://github.com/fast-down/fast-down-py/commits/main)
[![CI](https://github.com/fast-down/fast-down-py/workflows/CI/badge.svg)](https://github.com/fast-down/fast-down-py/actions)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/fast-down/fast-down-py/blob/main/LICENSE)

`fastdown` 是一个特别快下载器，封装自 [fast-down-ffi](https://github.com/fast-down/ffi)，由 Rust 驱动，简洁易用。

## 示例

```py
import fastdown

task = await fastdown.prefetch("https://example.com/test.zip");
await task.start(task.info.filename());
```

[查看更多示例](https://github.com/fast-down/fast-down-py/blob/main/example)
