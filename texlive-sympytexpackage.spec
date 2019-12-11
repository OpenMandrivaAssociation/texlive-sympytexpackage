Name:		texlive-sympytexpackage
Version:	20190228
Release:	2
Summary:	TeXLive sympytexpackage package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sympytexpackage.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sympytexpackage.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sympytexpackage.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive sympytexpackage package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/scripts/sympytexpackage
%{_texmfdistdir}/tex/latex/sympytexpackage
%doc %{_texmfdistdir}/doc/latex/sympytexpackage
#- source
%doc %{_texmfdistdir}/source/latex/sympytexpackage

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar scripts tex doc source %{buildroot}%{_texmfdistdir}
