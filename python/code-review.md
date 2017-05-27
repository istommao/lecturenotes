title: python code review
speaker: silence
url: https://github.com/ksky521/nodePPT
transition: cards

[slide style="background-color:#2C3F51"]

# Code Review
## 演讲者：silence

[slide style="background-color:#2C3F51"]

## 代码审查作用

- 在项目早期就能够发现代码中的BUG
- 帮助初级开发人员学习高级开发人员的经验，达到知识共享
- 避免开发人员犯一些很常见，很普通的错误
- 保证项目组人员的良好沟通
- 项目或产品的代码更容易维护代码的一致性、编码风格、代码的安全问题、代码冗余、是否正确设计以满足需求（性能、功能）等等

> 程序员最大的问题就是“自负”，尤其当我们Reivew别人的代码的时候，我已经见过无数的场面，程序员在Code Review的时候，开始抨击别人的代码，质疑别人的能力。太可笑了，我分析了一下，这类的程序员其实并没有什么本事，因为他们指责对方的目的是想告诉大家自己有多么的牛，靠这种手段来表现自己的程序员，其实是就是传说中所说的“半瓶水”。

[slide style="background-color:#2C3F51"]

# 代码审查的意义

- 让代码正常工作
- 加强团队沟通合作

[slide style="background-color:#2C3F51"]

# 如何进行代码审查

## 审查正确性

> 我们开始代码审查的目的是改进代码质量，寻找测试中没有发现的问题。这么做并不是教授经验不足的开发者如何编写更好的代码，或是如何在团队内分享知识。这些都应该是代码审查所带来的间接好处，不过审查的最终目的应该是确保代码能够正常工作。

*相对于使用长长的检查列表，审查者在看代码时首先会问几个问题：*

- 代码的行为是否与预期一致，其逻辑是否是正确无误的？
- 被审查的代码是否与其他代码拥有类似的结构和功能？

**理解而不是批评**

- 审查目的是理解代码，确保其能正常工作，而不是批评任何人
- 在代码审查过程中，请不要掺入诸如“我认为好的代码是什么，你认为好的代码是什么”这样的争论中
- 应该关注的重点是“我需要完全理解这部分代码才能确保它能够正常工作，如果由我来修复代码中的问题，我是不会这么写的，因此希望你也不要这么写。


[slide style="background-color:#2C3F51"]

# 谷歌是如何做代码审查的
- 在Google，没有程序，任何产品、任何项目的程序代码，可以在没有经过有效的代码审查前提交到代码库里的。


- 最重要的一个原则：代码审查用意是在代码提交前找到其中的问题——你要发现是它的正确。在代码审查中最常犯的错误——几乎每个新手都会犯的错误——是，审查者根据自己的编程习惯来评判别人的代码

- 第三是速度。

> 你不能匆匆忙忙的进行一次代码审查——但你也要能迅速的完成。你的同伴在等你。如果你和你的同事并不想花太多时间进行代码复查，你们很快的完成，那被审查者会觉得很沮丧，这种代码审查带来的只有失望的感觉。就好象是打搅了大家，使大家放下手头的工作来进行审查。事情不该是这样。你并不需要推掉手头上的任何事情来做代码审查。但如果中途耽误了几个小时，你中间还要休息一会，喝杯茶，冲个澡，或谈会儿闲话。当你回到审查现场，你可以继续下去，把事情做完。如果你真是这样，我想没有人愿意在那干等着你。

[slide style="background-color:#2C3F51"]

# 代码审查清单 常规项

- 代码能够工作么？它有没有实现预期的功能，逻辑是否正确等。
所有的代码是否简单易懂？
- 代码符合你所遵循的编程规范么？这通常包括大括号的位置，变量名和函数名，行的长度，缩进，格式和注释。
- 是否存在多余的或是重复的代码？
- 代码是否尽可能的模块化了？
- 是否有可以被替换的全局变量？
- 是否有被注释掉的代码？
- 循环是否设置了长度和正确的终止条件？
- 是否有可以被库函数替代的代码？
- 是否有可以删除的日志或调试代码？

[slide style="background-color:#2C3F51"]

# 代码审查清单 安全

- 所有的数据输入是否都进行了检查（检测正确的类型，长度，格式和范围）并且进行了编码？
- 在哪里使用了第三方工具，返回的错误是否被捕获？
- 输出的值是否进行了检查并且编码？
- 无效的参数值是否能够处理？

[slide style="background-color:#2C3F51"]

# 代码审查清单 文档
- 是否有注释，并且描述了代码的意图？
- 所有的函数都有注释吗？
- 对非常规行为和边界情况处理是否有描述？
- 第三方库的使用和函数是否有文档？
- 数据结构和计量单位是否进行了解释？
- 是否有未完成的代码？如果是的话，是不是应该移除，或者用合适的标记进行标记比如‘TODO’？

[slide style="background-color:#2C3F51"]

# 代码审查清单 测试

- 代码是否可以测试？比如，不要添加太多的或是隐藏的依赖关系，不能够初始化对象，测试框架可以使用方法等。
- 是否存在测试，它们是否可以被理解？比如，至少达到你满意的代码覆盖(code coverage)。
- 单元测试是否真正的测试了代码是否可以完成预期的功能？
- 是否检查了数组的“越界“错误？
- 是否有可以被已经存在的API所替代的测试代码？


[slide style="background-color:#2C3F51"]

# 参考资料 {:&.flexbox.vleft}

- [让代码审查成为你的团队习惯](http://yedingding.com/2013/08/08/dig-into-code-review-process.html)
- [我们如何进行代码审查](http://www.infoq.com/cn/news/2014/01/how-we-do-code-review)
- [谷歌是如何做代码审查的](http://www.vaikan.com/things-everyone-should-do-code-review/)
- [程序员必备的代码审查（Code Review）清单](http://blog.jobbole.com/83595/)
- [提高代码质量之代码审查](https://www.pureweber.com/article/code-review/)
- [高效代码审查的十个经验](http://www.williamlong.info/archives/3272.html)
- [代码审查思路](http://developer.51cto.com/art/201207/346410.htm)
- [Code Review最佳实践](http://blog.csdn.net/u011570979/article/details/45951419)
- [关于代码审查的几点建议](http://www.infoq.com/cn/news/2014/09/code-check)
- [同行代码审查的实战经验](http://blog.jobbole.com/85184/)
- [代码Review那些事](http://www.jianshu.com/p/6324361d1ab1)


[slide style="background-color:#2C3F51"]

# 高效代码审查的十个经验

-  代码审查要求团队有良好的文化
- 谨慎的使用审查中问题的发现率作为考评标准
- 控制每次审查的代码数量
- 带着问题去进行审查
- 所有的问题和修改，必须由原作者进行确认
- 利用代码审查激活个体“能动性"
- 在非正式，轻松的环境下进行代码审查
- 提交代码前自我审查，添加对代码的说明
- 实现中记录笔记可以很好的提高问题发现率
- 使用好的工具进行轻量级的代码审查

[slide style="background-color:#2C3F51"]

# 代码审查之前

- 自己提交前先过一遍
- 提交前本地先进行编码规范的检查  (pylint pre-commit)


[slide style="background-color:#2C3F51"]

# 扩展

- [如何利用GitHub进行代码审查](https://realm.io/cn/news/codereview-howto/)
- [代码审查的价值——为何做、何时做、如何做？](http://www.infoq.com/cn/news/2013/11/code-review-why-when-how)
- [同行代码审查的实战经验](http://www.techug.com/code-review)

[slide style="background-color:#2C3F51"]

# 代码的坏味道 {:&.flexbox.vleft}

- `神奇的数字` 使用常量代替
- 不再使用的代码，别注释掉，直接删除
- 重复的代码 DRY
- 不必要的复杂
- 不知所云的变量名
- 冗长的类
- 过长的函数

- [五种应该避免的代码注释](http://coolshell.cn/articles/2746.html)
- [清除代码异味](http://www.vaikan.com/cleaning-up-code-smells/)
- [代码的坏味道](http://www.cnblogs.com/mywolrd/archive/2012/04/24/2467395.html)

[slide style="background-color:#2C3F51"]

# 谢谢

Github：https://github.com/istommao/lecturenotes
