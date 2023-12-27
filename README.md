# geez2ethiop

This module converts Ethiopian scripts into PDFLaTeX commands.

## Installation
```bash
pip install geez2ethiop
```

## Command Line
First, find the installed script
```bash
which geez2ethiop
```
Then add the `bin` directory to the `$PATH` if needed.
Then run the following
```bash
echo አዲስ አበባ | geez2ethiop --latex
```
or 
```bash
geez2ethiop --latex
አዲስ አበባ
```

## Python
See `demo`.

## Usage with PDFLaTeX
Following is an example of PDFLaTeX
```latex
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{tipa}
\usepackage[ethiop,main=english]{babel}
\newcommand{\geeztext}[1]{{\selectlanguage{ethiop}\mbox{#1}}}

\title{Example}
\author{Author}
\date{\today}

\begin{document}
\maketitle
\geeztext{'adise 'ababA}
\textipa{'\"adis\textschwa{} '\"ab\"aba}
\end{document}
```
If you are interested in using XeLaTeX, LuaLaTeX, you can write the Ethiopic texts directly using the `fontspec` package and appropriate Ethiopic fonts.