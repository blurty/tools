## gostats

### 背景

随着项目的快速迭代，有些无用代码出于某些原因没有及时清理。这样在后来者在阅读代码的时候，这些不再使用的代码会造成一些困扰。
另一方面，在需求迭代几个版本之后，后来者甚至原来的coder都无法得知这些代码的用途，出于安全考虑，甚至不会删除，这样就会造成
无用的代码越来越多。

本工具统计出go程序中没有引用/使用的代码，这样在每次提交代码的时候，都可以通过这个工具检查一下哪些代码不再使用，或定期清理、
或对这些代码进行注释说明等。