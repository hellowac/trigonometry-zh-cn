前言
===========
Preface

本书涵盖了初等三角学的内容。它适用于大学阶段的一学期课程，当然也可以在高中中使用。其前置要求为高中代数和几何知识。

本书主要由我在 Schoolcraft College 多年来教授三角学课程的讲义组成，并在此基础上添加了一些习题。每节的结尾都包含了习题。我尽量加入了一些更具挑战性的问题，并在我认为必要时提供了提示。一个普通的学生应当能够完成大多数习题。对于许多奇数题目以及部分偶数题目，解答和提示可参见 :ref:`附录 A <appendix a>`。

本教材可能比当前大多数三角学教材更具几何感。这事实上也是我想写这本书的原因之一。我认为若从过于分析性的角度来介绍该学科，对学生来说反而是令人困惑的。这会让很多内容显得缺乏动机。本书以“老式”的直角三角形方法来介绍三角函数，这种方式对学生来说更直观易懂。

根据我的经验，在介绍完三角函数的定义后立刻跳转到恒等式证明，这对于大多数学生而言，是从几何直接跳到分析的一个太大的转折。所以本书的内容顺序与大多数现今教材截然不同。例如，在从直角三角形定义及其部分应用开始之后，接下来便介绍一般（三角）形。与其像传统教材那样把一般三角形放到最后，不如这样安排更为自然。

本书的目标也有所不同。与其采取那种注定失败的方式——让学生相信三角学“与他们的日常生活息息相关”（这最终只会显得做作），不如换一种思维方式：
**为学生在其他课程中使用三角学做好准备**
几乎没有学生会在“日常生活”中，用量角器测树高，或者计算摩天轮的角速度。学生在其他课程中（如工程、物理）更有可能需要用到三角学。我认为数学教师有责任为此做好准备。

在 :ref:`第 5 章 <c5>` 中，学生将被要求使用开源免费软件 Gnuplot 来绘图。然而，只要程序能够准确绘制图像，任何软件都可以完成这些练习。:ref:`附录 B <appendix b>` 包含了 Gnuplot 的简要教程。

部分习题要求学生编写自己的计算机程序来解决一些数值计算问题。:ref:`第 6 章 <c6>` 中提供了一些 Java 和 Python 编写的代码示例，希望这些示例足够清晰，即便读者不了解这些语言，也能理解其含义。此外，还提到了 Octave 和 Sage。本书可能比同类教材更注重数值问题（例如，使用海伦公式计算三角形面积时的数值不稳定性、用割线法求解三角函数方程等）。鉴于即便是中等复杂度的三角方程也极少能用初等方法求解，而且数学软件如此普及，教材对数值方法的强调可能还不够。

我希望这本书尽可能简明。有人曾调侃说，三角学其实只有两周的内容，却被拉长成一整个学期的课程，我觉得这话也不无道理。不过，这就意味着必须对取舍有所决断。我本来打算加入关于向量、球面三角学（一个近几十年几乎在教材中消失的主题，为什么？）以及其他几个话题的章节，但最终决定舍弃。最困难的决定是排除了 Paul Rider 提出的、不使用和积恒等式的正切定理巧妙几何证明，尽管我在文中给出了相关参考。

本书以 GNU 自由文档许可证（GFDL）发布，允许他人不仅复制、分发本书，还可以修改。有关详情请参阅所附的 GFDL 副本。为避免对此产生任何歧义，任何人均可无限量复制和分发本书，无需征得我的许可。PDF 版本将始终免费向公众开放（参见 http://www.mecmath.net/trig）。如有任何关于本书的疑问（例如意见、建议、勘误等），欢迎通过 mcorral@schoolcraft.edu 与我联系。我期待您的反馈。

2009 年 7 月 —— Michael Corral

密歇根州 利沃尼亚市

.. toggle::

    This book covers elementary trigonometry. It is suitable for a one-semester course at the college
    level, though it could also be used in high schools. The prerequisites are high school algebra and
    geometry.

    This book basically consists of my lecture notes from teaching trigonometry at Schoolcraft College
    over several years, expanded with some exercises. There are exercises at the end of each section.
    I have tried to include some
    more challenging problems, with hints when I felt those were needed. An average student should be
    able to do most of the exercises. Answers and hints to many of the odd-numbered and some of the
    even-numbered exercises are provided in :ref:`Appendix A <appendix a>`.

    This text probably has a more geometric feel to it than most current trigonometry texts.
    That was, in fact, one of the reasons I wanted to write this book. I think that approaching the
    subject with too much of an analytic emphasis is a bit confusing to students. It makes much of the
    material appear unmotivated. This book starts with the "old-fashioned" right triangle approach to
    the trigonometric functions, which is more intuitive for students to grasp.

    In my experience, presenting the definitions of the trigonometric
    functions and then immediately jumping into proving identities is too much of a detour from
    geometry to analysis for most students.
    So this book presents material in a very different order than most books today. For
    example, after starting with the right triangle definitions and some applications, general (oblique)
    triangles are presented. That seems like a more natural progression of topics, instead of leaving
    general triangles until the end as is usually the case.

    The goal of this book is a bit different, too. Instead of taking the (doomed) approach that students
    have to be shown that trigonometry is "relevant to their everyday lives" (which inevitably comes
    off as artificial), this book has a different mindset:
    **preparing students to use trigonometry as it is used in other courses**
    Virtually no students will ever in their "everyday life" figure out the height of a tree
    with a protractor or determine the angular speed of a Ferris wheel.
    Students are far more likely to need trigonometry in other courses (e.g. engineering, physics).
    I think that math instructors have a duty to prepare students for that.

    In :ref:`Chapter 5 <c5>` students are asked to use the free open-source software Gnuplot to graph
    some functions. However, any program can be used for those exercises, as long as it produces
    accurate graphs. :ref:`Appendix B <appendix b>` contains a brief tutorial on Gnuplot.

    There are a few exercises that require the student to write his or her own computer program
    to solve some numerical computation problems. There
    are a few code samples in :ref:`Chapter 6 <c6>`, written in the Java and Python programming languages, hopefully
    sufficiently clear so that the reader can figure out what is being done even without knowing those
    languages. Octave and Sage are also mentioned. This book probably discusses numerical issues more
    than most texts at this level (e.g. the numerical instability of Heron's formula for the area of a
    triangle, the secant method for solving trigonometric equations). Numerical methods probably should
    have been emphasized even more in the text, since it is rare when even a moderately complicated
    trigonometric equation can be solved with elementary methods, and since mathematical software is
    so readily available.

    I wanted to keep this book as brief as possible. Someone once joked that trigonometry is two weeks
    of material spread out over a full semester, and I think that there is some truth to that.
    However, some decisions had to be made on what material to leave out. I had planned to include
    sections on vectors, spherical trigonometry - a subject which has basically vanished from
    trigonometry texts in the last few decades (why?) - and a few other topics, but decided against it.
    The hardest decision was to exclude Paul Rider's clever geometric proof of the Law of Tangents
    without using any sum-to-product identities, though I do give a reference to it.

    This book is released under the GNU Free Documentation License (GFDL), which allows others to not
    only copy and distribute the book but also to modify it. For more details, see the included copy of
    the GFDL. So that there is no ambiguity on this matter, anyone can make as many copies of this book
    as desired and distribute it as desired, without needing my permission. The PDF version will always
    be freely available to the public at no cost (go to http://www.mecmath.net/trig ). Feel free to
    contact me at mcorral@schoolcraft.edu for any
    questions on this or any other matter involving the book (e.g. comments, suggestions, corrections,
    etc). I welcome your input.

    July 2009 - Michael Corral

    Livonia, Michigan
