# revision 21838
# category Package
# catalog-ctan /macros/latex/contrib/pxgreeks
# catalog-date 2011-03-18 12:27:11 +0100
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-pxgreeks
Version:	1.0
Release:	11
Summary:	Shape selection for PX fonts Greek letters
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pxgreeks
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pxgreeks.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pxgreeks.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pxgreeks.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 755549
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 719417
- texlive-pxgreeks
- texlive-pxgreeks
- texlive-pxgreeks
- texlive-pxgreeks

