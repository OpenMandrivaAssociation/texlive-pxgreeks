%global tl_name pxgreeks
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Shape selection for PX fonts Greek letters
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pxgreeks
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pxgreeks.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pxgreeks.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pxgreeks.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package allows LaTeX maths users of the PX fonts to select the
shapes (italic or upright) for the Greek lowercase and uppercase
letters. Once the shapes for lowercase and uppercase have been selected
via a package option, the \other prefix (e.g., \otheralpha) allows using
the alternate glyph (as in the fourier package). The pxgreeks package
does not constrain the text font that may be used in the document.

