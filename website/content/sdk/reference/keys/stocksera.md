---
title: stocksera
description: 'The OpenBB project: how to set your Stocksera API key using Python.
  Documentation provides information about parameters, return types, and examples
  for the stocksera method.'
keywords:
- Stocksera
- API Key
- Jupyter Notebook
- Environment Variables
---

import HeadTitle from '@site/src/components/General/HeadTitle.tsx';

<HeadTitle title="keys.stocksera - Reference | OpenBB SDK Docs" />

Set Stocksera key.

Source Code: [[link](https://github.com/OpenBB-finance/OpenBBTerminal/tree/main/openbb_terminal/keys_model.py#L2545)]

```python
openbb.keys.stocksera(key: str, persist: bool = False, show_output: bool = False)
```

---

## Parameters

| Name | Type | Description | Default | Optional |
| ---- | ---- | ----------- | ------- | -------- |
| key | str | API key | None | False |
| persist | bool | If False, api key change will be contained to where it was changed. For example, a Jupyter notebook session.<br/>If True, api key change will be global, i.e. it will affect terminal environment variables.<br/>By default, False. | False | True |
| show_output | bool | Display status string or not. By default, False. | False | True |


---

## Returns

| Type | Description |
| ---- | ----------- |
| str | Status of key set |
---

## Examples

```python
from openbb_terminal.sdk import openbb
openbb.keys.stocksera(key="example_key")
```

---
