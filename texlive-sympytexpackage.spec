%global tl_name sympytexpackage
%global tl_revision 57090

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3
Release:	%{tl_revision}.1
Summary:	Include symbolic computation (using sympy) in documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/sympytexpackage
License:	gpl2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sympytexpackage.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sympytexpackage.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sympytexpackage.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle supports inclusion of symbolic-python (sympy) expressions, as
well as graphical output from the sympy plotting module (or from
matplotlib).

