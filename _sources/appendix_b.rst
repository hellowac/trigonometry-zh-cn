.. _appendix b:

附录 B
===============
Appendix B

使用 Gnuplot 绘图
-----------------------
Graphing with Gnuplot

Gnuplot 是一个免费的开源软件包，用于生成各种图形。它有适用于多种操作系统的版本。下面是一个简要教程，介绍如何使用 Gnuplot 绘制三角函数图像。

.. toggle::

    Gnuplot is a free, open-source software package for producing a variety of graphs. Versions are
    available for many operating systems. Below is a very brief tutorial on how to use Gnuplot to graph
    trigonometric functions.

安装
~~~~~~~~~~~~~~~~
INSTALLATION

#. 访问 http://www.gnuplot.info/download.html，按照链接下载适用于你的操作系统的最新版本。对于 Windows，你应下载名为类似 ``gp460-win32-setup.exe`` 的安装文件（即版本 4.6.0）。这里讨论的所有示例都假设至少是 4.6.0 版本，尽管它们在早期的 4.x 版本中通常也能运行。
#. 安装下载的文件。例如，在 Windows 中运行你在第 1 步下载的安装文件，默认将 Gnuplot 安装在 ``C:\symbol{92}Program Files\gnuplot`` 文件夹中。你可以接受默认设置，但应在 **选择附加任务** 界面中选择 “创建桌面图标” 选项。
#. （可选）阅读 http://gnuplot.info/documentation.html 上的文档。

.. toggle::

    #. Go to http://www.gnuplot.info/download.html and follow the links to download the latest version for your operating system. For Windows, you should download the setup file with a name such as ``gp460-win32-setup.exe``, which is version 4.6.0. All the examples discussed here will assume at least version 4.6.0, though they should work with earlier 4.x versions.
    #. Install the downloaded file. For example, in Windows you would run the setup file you downloaded in Step 1, which installs Gnuplot in the ``C:\symbol{92}Program Files\gnuplot`` folder by default. You can accept the defaults during installation, though you should select the  "Create a desktop icon" option in the **Select Additional Tasks** screen.
    #. (Optional) Read the documentation at http://gnuplot.info/documentation.html.

运行 Gnuplot
~~~~~~~~~~~~~~~~~~
RUNNING GNUPLOT


#. 在 Windows 中，从你安装 Gnuplot 的 ``bin`` 文件夹中运行 ``wgnuplot.exe``（默认位置是 ``C:\Program Files\gnuplot\bin\wgnuplot.exe``），或者如果你在安装时选择了该选项，也可以双击桌面图标。在 Linux 中，只需在终端窗口中输入 ``gnuplot``。
#. 你现在应该能看到一个带有 ``gnuplot>`` 命令提示符的 Gnuplot 终端。在 Windows 中，它会出现在一个新窗口中，如下一页所示的图片。在 Linux 中，它会出现在运行 ``gnuplot`` 命令的终端窗口中。对于 Windows，如果字体难以辨认，可以通过右键点击 Gnuplot 窗口的文本区域并选择 “选择字体…” 选项进行更改。例如，字体选择 “Courier”，样式 “Regular”，字号 “12” 通常是一个不错的选择（可以通过再次右键点击 Gnuplot 窗口并选择更新 wgnuplot.ini 的选项来保存该设置，以便下次会话使用）。
#. 现在在 ``gnuplot>`` 命令提示符下，你可以运行绘图命令，下面将对其进行说明。

.. figure:: ./img/164-0.png
    :align: center

**函数绘图**

在 Gnuplot 中创建图像的常用方式是使用 **plot** 命令：

.. math::

 \texttt{plot <range> <comma-separated list of functions>}

对于一个函数 :math:`y=f(x)`，*<range>* 是用于绘图的 :math:`x` 值范围（可选地也包括 :math:`y` 值范围）。若要指定一个 :math:`x` 范围，使用形式为 :math:`[a:b]` 的表达式，其中 :math:`a<b`。这将使图像在 :math:`a\le x\le b` 的区间内绘制。

若要同时指定 :math:`x` 范围和 :math:`y` 范围，使用形式为 :math:`[a:b]` :math:`[c:d]` 的表达式，其中 :math:`a<b` 且 :math:`c<d`。这将使图像在 :math:`a\le x\le b` 且 :math:`c\le y \le d` 的区间内绘制。

函数定义使用 :math:`x` 变量与下列数学运算符组合：

.. list-table::

    * - **符号**
      - **操作**
      - **示例**
      - **结果**
    * - :math:`+`
      - 加法
      - :math:`2 + 3`
      - :math:`5`
    * - :math:`-`
      - 减法
      - :math:`3 - 2`
      - :math:`1`
    * - \*
      - 乘法
      - :math:`2`*`3`
      - :math:`6`
    * - :math:`/`
      - 除法
      - :math:`4/2`
      - :math:`2`
    * - \*\*
      - 平方
      - :math:`2` \*\* :math:`3`
      - :math:`2^3 = 8`
    * - exp(:math:`x`)
      - :math:`e^x`
      - exp(:math:`2`)
      - :math:`e^2`
    * - log(:math:`x`)
      - :math:`\ln x`
      - log(:math:`2`)
      - :math:`\ln 2`
    * - sin(:math:`x`)
      - :math:`\sin x`
      - sin(pi/:math:`2`)
      - :math:`1`
    * - cos(:math:`x`)
      - :math:`\cos x`
      - cos(pi)
      - :math:`-1`
    * - tan(:math:`x`)
      - :math:`\tan x`
      - tan(pi/:math:`4`)
      - :math:`1`

注意我们使用特殊关键字 "pi" 来表示 :math:`\pi` 的值。

.. admonition:: 示例 B.1.

    要绘制函数 :math:`y=\sin\;x` 在区间 :math:`x=0` 到 :math:`x=2\pi` 上的图像，在 **gnuplot** 提示符下输入：

    .. math::

        \texttt{plot [0:2*pi] sin(x)}

    结果如下图所示：

    .. figure:: ./img/165-0.png
        :align: center

    注意 :math:`x` 轴标注为整数。若要将 :math:`x` 轴标注为 :math:`\pi` 的分数形式，需要修改 *terminal* 设置。在 Windows 中，可以使用如下命令：

    .. math::

        \texttt{set terminal windows enhanced}

    在 Linux 中则使用：

    .. math::

        \texttt{set terminal wxt enhanced}

    然后（前提是系统已安装 Symbol 字体，通常已安装）可使用以下命令（需一行输入）将 :math:`x` 轴标注为从 :math:`0` 到 :math:`2\pi` 的 :math:`\pi/2` 的倍数：

    .. math::

        \begin{gather*}
        \texttt{set xtics ('0' 0,'\{/Symbol p\}/2' pi/2,'\{/Symbol p\}' pi,'3\{/Symbol p\}/2' 3*pi/2,}\\
        \texttt{'2\{/Symbol p\}' 2*pi)}
        \end{gather*}

    在上面的示例中，若要在同一图像中绘制函数 :math:`y=\cos\;2x + \sin\;3x`，可在第一个函数后加一个逗号并添加新函数：

    .. math::

        \texttt{plot [0:2*pi] sin(x), cos(2*x) + sin(3*x)}

    默认情况下，图像中不会显示 `x` 轴。若要显示它，请在 **plot** 命令 *之前* 输入以下命令：

    .. math::

        \texttt{set zeroaxis}

    此外，若要为坐标轴添加标签，请使用如下命令：

    .. math::

        \begin{gather*}
        \texttt{set xlabel "x"}\\\texttt{set ylabel "y"}
        \end{gather*}

    绘图默认的采样数量为 :math:`100`，对于复杂曲线可能会导致边缘不平滑。为了获得更平滑的曲线，可将采样数增加（例如到 :math:`1000`），命令如下：

    .. math::

        \texttt{set samples 1000}

    将以上设置整合后，可得到如下图像：

    .. figure:: ./img/167-0.png
        :align: center

.. toggle::

    #. In Windows, run ``wgnuplot.exe`` from the ``bin`` folder where you installed Gnuplot (the default location is ``C:\Program Files\gnuplot\bin\wgnuplot.exe`` ), or double-click the desktop icon if you selected that option during the installation. In Linux, just type ``gnuplot`` in a terminal window.
    #. You should now get a Gnuplot terminal with a ``gnuplot>`` command prompt. In Windows this will appear in a new window, as shown in the picture on the next page. In Linux it will appear in the terminal window where the ``gnuplot`` command was run. For Windows, if the font is unreadable you can change it by right-clicking on the text part of the Gnuplot window and selecting the "Choose Font.." option. For example, the font "Courier", style "Regular", size "12" is usually a good choice (that choice can be saved for future sessions by right-clicking in the Gnuplot window again and selecting the option to update wgnuplot.ini).
    #. At the ``gnuplot>`` command prompt you can now run graphing commands, which we will now describe.

    .. figure:: ./img/164-0.png
        :align: center

    **GRAPHING FUNCTIONS**

    The usual way to create graphs in Gnuplot is with the **plot** command:

    .. math::

        \texttt{plot <range> <comma-separated list of functions>}

    For a function :math:`y=f(x)`, *<range>* is the range of :math:`x` values (and optionally the range of :math:`y` values) over which to plot. To specify an :math:`x` range, use an expression of the form :math:`[a:b]`, for some numbers :math:`a<b`. This will cause the graph to be plotted for :math:`a\le x\le b`.

    To specify an :math:`x` range and a :math:`y` range, use an expression of the form :math:`[a:b]` :math:`[c:d]`, for some numbers :math:`a<b` and :math:`c<d`. This will cause the graph to be plotted for :math:`a\le x\le b` and :math:`c\le y \le d`.

    Function definitions use the :math:`x` variable in combination with mathematical operators, listed below:

    .. list-table::

        * - **Symbol**
          - **Operation**
          - **Example**
          - **Result**
        * - :math:`+`
          - Addition
          - :math:`2 + 3`
          - :math:`5`
        * - :math:`-`
          - Subtraction
          - :math:`3 - 2`
          - :math:`1`
        * - \*
          - Multiplication
          - :math:`2`*`3`
          - :math:`6`
        * - :math:`/`
          - Division
          - :math:`4/2`
          - :math:`2`
        * - \*\*
          - Power
          - :math:`2` \*\* :math:`3`
          - :math:`2^3 = 8`
        * - exp(:math:`x`)
          - :math:`e^x`
          - exp(:math:`2`)
          - :math:`e^2`
        * - log(:math:`x`)
          - :math:`\ln x`
          - log(:math:`2`)
          - :math:`\ln 2`
        * - sin(:math:`x`)
          - :math:`\sin x`
          - sin(pi/:math:`2`)
          - :math:`1`
        * - cos(:math:`x`)
          - :math:`\cos x`
          - cos(pi)
          - :math:`-1`
        * - tan(:math:`x`)
          - :math:`\tan x`
          - tan(pi/:math:`4`)
          - :math:`1`

    Note that we use the special keyword "pi" to denote the value of :math:`\pi`.

    .. admonition:: Example B.1.

        To graph the function :math:`y=\sin\;x` from :math:`x=0` to :math:`x=2\pi`, type this at the **gnuplot** prompt:

        .. math::

            \texttt{plot [0:2*pi] sin(x)}

        The result is shown below:

        .. figure:: ./img/165-0.png
            :align: center

        Notice that the :math:`x`-axis is labeled with integers. To get the :math:`x`-axis labels with fractions of :math:`\pi`, you need to modify the *terminal* setting. In Windows, you would do this:

        .. math::

            \texttt{set terminal windows enhanced}

        In Linux you would do this:

        .. math::

            \texttt{set terminal wxt enhanced}

        You can then (provided the Symbol font is installed, which it usually is) set the :math:`x`-axis to have multiples of :math:`\pi/2` from :math:`0` to :math:`2\pi` as labels with this command (all on one line):

        .. math::

            \begin{gather*}
            \texttt{set xtics ('0' 0,'\{/Symbol p\}/2' pi/2,'\{/Symbol p\}' pi,'3\{/Symbol p\}/2' 3*pi/2,}\\
            \texttt{'2\{/Symbol p\}' 2*pi)}
            \end{gather*}

        In the above example, to also plot the function :math:`y=\cos\;2x + \sin\;3x` on the same graph, put a comma after the first function then append the new function:

        .. math::

            \texttt{plot [0:2*pi] sin(x), cos(2*x) + sin(3*x)}

        By default, the `x`-axis is not shown in the graph. To display it, use this command *before* the **plot** command:

        .. math::

            \texttt{set zeroaxis}

        Also, to label the axes, use these commands:

        .. math::

            \begin{gather*}
            \texttt{set xlabel "x"}\\\texttt{set ylabel "y"}
            \end{gather*}

        The default sample size for plots is :math:`100` units, which can result in jagged edges if the curve is complicated. To get a smoother curve, increase the sample size (to, say, :math:`1000`) like this:

        .. math::

            \texttt{set samples 1000}

        Putting all this together, we get the following graph:

        .. figure:: ./img/167-0.png
            :align: center

打印与保存
---------------------------
PRINTING AND SAVING

在 Windows 中，如果你使用的是 *windows enhanced* 终端，那么要从 Gnuplot 中打印图像，只需点击图像窗口菜单栏中的打印图标。如果你使用的是默认的 *wxt* 终端，则需在 Gnuplot 主窗口上方选择 **Print**，在 ``Terminal type?`` 文本框中输入 ``png``，然后点击 OK 打开打印设置对话框。

在 Windows 中，若要将图像保存为 PNG 文件，可在 Gnuplot 主窗口的菜单栏中点击 File 菜单，选择 "Output Device ..."，在 *Terminal type?* 文本框中输入 ``png``，点击 OK。然后再次进入 File 菜单，选择 "Output ..." 选项，在 *Output filename?* 文本框中输入文件名（如 graph.png），点击 OK。接着再次运行绘图命令，文件将会保存在当前目录中，通常为 *我的文档* 文件夹（也可以通过 File 菜单中的 "show Current Directory" 选项查看）。

在 Linux 中，若要将图像保存为名为 graph.png 的文件，运行以下命令：

.. math::
    
    \begin{align}
    &\texttt{set terminal png}\\
    &\texttt{set output 'graph.png'}
    \end{align}

然后运行你的绘图命令。终端类型有很多种（它们决定了输出格式）。可运行命令 `set terminal` 查看所有可用类型。在 Linux 中， **postscript** 终端类型很常用，因为其打印质量高，且有许多 PostScript 查看器可用。

若要退出 Gnuplot，请在 ``gnuplot`` 命令提示符下输入 ``quit``。

.. toggle::

    In Windows, if you are using the *windows enhanced* terminal then to print a graph from Gnuplot click on the printer icon in the menubar of the graph's window. If you are using the default *wxt* terminal then select **Print** near the top of the main Gnuplot window and enter ``png`` in the ``Terminal type?`` textfield, then hit OK to get the Print Setup dialog.

    In Windows, to save a graph, say, as a PNG file, go to the File menu on the main Gnuplot menubar, select "Output Device ...", and enter ``png`` in the *Terminal type?* textfield, hit OK. Then, in the File menu again, select the "Output ..." option and enter a filename (say, graph.png) in the *Output filename?* textfield, hit OK. Now run your plot command again and the file will be saved in the current directory, usually in your *My Documents* folder (it can also be found by selecting the "show Current Directory" option in the File menu).

    In Linux, to save the graph as a file called graph.png run the following commands:

    .. math::
        
        \begin{align}
        &\texttt{set terminal png}\\
        &\texttt{set output 'graph.png'}
        \end{align}


    and then run your plot command. There are many terminal types (which determine the output format). Run
    the command `set terminal` to see all the possible types. In Linux, the **postscript** terminal type is
    popular, since the print quality is high and there are many PostScript viewers available.


    To quit Gnuplot, type ``quit`` at the ``gnuplot`` command prompt.
