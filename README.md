# Конспекты, III семестр

В репозитории хранятся исходники конспектов в формате LaTeX. При изменении любого файла `.tex` GitHub Actions автоматически пересобирает PDF-файлы и добавляет их в репозиторий.

## Предметы

1. [Теоретическая механика — PDF](subjects/01-theoretical-mechanics/main.pdf) · [LaTeX](subjects/01-theoretical-mechanics/main.tex)
2. [Математический анализ — PDF](subjects/02-mathematical-analysis/main.pdf) · [LaTeX](subjects/02-mathematical-analysis/main.tex)
3. [Теория функций комплексной переменной — PDF](subjects/03-complex-analysis/main.pdf) · [LaTeX](subjects/03-complex-analysis/main.tex)
4. [Теория групп и теория чисел — PDF](subjects/04-group-theory-number-theory/main.pdf) · [LaTeX](subjects/04-group-theory-number-theory/main.tex)
5. [Дифференциальные уравнения — PDF](subjects/05-differential-equations/main.pdf) · [LaTeX](subjects/05-differential-equations/main.tex)
6. [Численные методы — PDF](subjects/06-numerical-methods/main.pdf) · [LaTeX](subjects/06-numerical-methods/main.tex)
7. [Базы данных и сетевые технологии — PDF](subjects/07-databases-network-technologies/main.pdf) · [LaTeX](subjects/07-databases-network-technologies/main.tex)

## Как добавлять конспект

Откройте нужный `subjects/.../main.tex` и пишите материал между `\begin{document}` и `\end{document}`, после строки `\setcounter{lection}{0}`.

```tex
\newlection{1 сентября 2026 г.}

\chapter{Название главы}
\section{Название раздела}

Обычный текст. Формула внутри строки: $f(x)=x^2$.

\[
    \int_0^1 x^2 \d x = \frac{1}{3}.
\]

\definition{Текст определения.}
\theorem{Формулировка теоремы.}
\provehere{Текст доказательства.}
```

Не удаляйте строки `\documentclass`, `\input{../../preamble.tex}`, `\begin{document}` и `\end{document}`. Название предмета, лектора и семестр можно менять в верхней части файла и на титульной странице.

## Исправления

Если вы нашли ошибку, неточность или опечатку, можете создать pull request в репозитории или написать в Telegram: [@Tangerine232](https://t.me/Tangerine232).


