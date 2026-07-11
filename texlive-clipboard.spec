%global tl_name clipboard
%global tl_revision 78101

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3
Release:	%{tl_revision}.1
Summary:	Copy and paste into and across documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/clipboard
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/clipboard.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/clipboard.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The clipboard package provides a basic framework for copying and pasting
text and commands into and across multiple documents. It replaces the
copypaste package.

