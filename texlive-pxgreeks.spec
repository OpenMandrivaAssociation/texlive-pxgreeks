Name:		texlive-pxgreeks
Version:	21838
Release:	2
Summary:	Shape selection for PX fonts Greek letters
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pxgreeks
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pxgreeks.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pxgreeks.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pxgreeks.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows LaTeX users who use the PX fonts to select
the shapes (italic or upright) for the Greek lowercase and
uppercase letters. Once the shapes for lowercase and uppercase
have been selected via a package option, the \other prefix
(e.g., \otheralpha) allows using the alternate glyph (as in the
fourier package). The pxgreeks package does not constrain the
text font that may be used in the document.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pxgreeks/pxgreeks.sty
%doc %{_texmfdistdir}/doc/latex/pxgreeks/README
%doc %{_texmfdistdir}/doc/latex/pxgreeks/pxgreeks.pdf
#- source
%doc %{_texmfdistdir}/source/latex/pxgreeks/pxgreeks.dtx
%doc %{_texmfdistdir}/source/latex/pxgreeks/pxgreeks.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
