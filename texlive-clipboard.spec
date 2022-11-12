Name:		texlive-clipboard
Version:	47747
Release:	1
Summary:	Copy and paste into and across documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/clipboard
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/clipboard.r47747.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/clipboard.doc.r47747.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The clipboard package provides a basic framework for copying
and pasting text and commands into and across multiple
documents. It replaces the copypaste package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/clipboard/clipboard.sty
%doc %{_texmfdistdir}/doc/latex/clipboard/README
%doc %{_texmfdistdir}/doc/latex/clipboard/clipboard.pdf
%doc %{_texmfdistdir}/doc/latex/clipboard/clipboard.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
