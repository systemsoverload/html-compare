from html_compare import html_equal


def test_whitespace():
    # Whitespace/newlines should not be significant
    assert html_equal("<a>\n\n\n\t\tHi</a>", "<a> Hi </a>")


def test_whitespace_span():
    # ...unless whitespace is significant, as within a span tag
    assert html_equal("<span> <p>Hi</p>    </span>", "<span><p>Hi </p></span>")


def test_attributes():
    # Attributes should be significant
    assert html_equal("<a data-foo='bar'>Hi\n</a>", '<a data-foo="bar"> Hi </a>')


def test_classes():
    # Classes are significant, but ordering is not
    assert html_equal(
        "<a class='foo bar baz'>Hi</a>", '<a class="baz bar foo"> Hi </a>'
    )


def test_boolean_attributes():
    # Boolean attributes should optionally be able to exclude the `={attr_name}` expression
    assert html_equal("<a checked>Hi</a>", '<a checked="checked"> Hi </a>')


def test_svg():
    # Compare a non-trivial SVG path with mixed whitespace
    actual = """<svg width="24" height="24" version="1.1" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" xmlns:cc="http://creativecommons.org/ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
     <metadata>
      <rdf:RDF>
       <cc:Work rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage"/>
        <dc:title/>
       </cc:Work>
      </rdf:RDF>
     </metadata>
     <path d="m19.818 8.9715c-1.4849-1.4849-3.8891-1.2021-5.9397-1.2728 0.14142 0.14142 0.42426 0.28284 0.6364 0.49497 0.35355 0.35355 0.6364 0.77782 0.84853 1.2728 1.1314 0 2.3335-0.070711 3.182 0.77782 0.42426 0.42426 0.70711 1.1314 0.77782 1.7678 0 1.4142-1.1314 2.5456-2.5456 2.5456h-3.677c-0.56568 0-1.3435-0.35355-1.7678-0.77782-0.98995-0.98995-0.84853-2.1213-0.42426-3.2527h-1.8385c-0.49497 1.6263-0.42426 3.2527 0.84853 4.5255 0.84853 0.84853 1.9799 1.2728 3.0406 1.2021h3.677c1.2728 0 2.4749-0.35355 3.3941-1.2728 1.4142-1.6971 1.3435-4.4548-0.21213-6.0104zm-11.597 5.5154h-1.2728c-0.56569 0-1.3435-0.35355-1.7678-0.77782-0.42426-0.42426-0.70711-1.1314-0.77782-1.7678 0-1.4142 1.2021-2.6163 2.5456-2.5456h3.677c0.56568 0 1.3435 0.35355 1.7678 0.77782 0.98995 0.98995 0.77782 2.192 0.42426 3.2527h1.8385c0.49498-1.6263 0.42426-3.2527-0.84853-4.5255-0.84853-0.84853-1.9799-1.2728-3.0406-1.2021h-3.677c-2.4042 0-4.3134 1.9092-4.2426 4.2426 0 2.2627 1.9092 4.3134 4.1719 4.1719h2.687c-0.28284-0.14142-0.49497-0.35355-0.70711-0.56568-0.35355-0.35355-0.6364-0.6364-0.77782-1.0607z"/>
    </svg>"""

    expected = (
        '<svg width="24" height="24" version="1.1" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"'
        ' xmlns:cc="http://creativecommons.org/ns#" xmlns:dc="http://purl.org/dc/elements/1.1/"'
        ' xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">'
        "<metadata>"
        "<rdf:RDF>"
        '<cc:Work rdf:about="">'
        "<dc:format>image/svg+xml</dc:format>"
        '<dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage"/>'
        "<dc:title/>"
        "</cc:Work>"
        "</rdf:RDF>"
        "</metadata>"
        '<path d="m19.818 8.9715c-1.4849-1.4849-3.8891-1.2021-5.9397-1.2728 0.14142 0.14142 0.42426 0.28284 0.6364'
        " 0.49497 0.35355 0.35355 0.6364 0.77782 0.84853 1.2728 1.1314 0 2.3335-0.070711 3.182 0.77782 0.42426"
        " 0.42426 0.70711 1.1314 0.77782 1.7678 0 1.4142-1.1314 2.5456-2.5456 2.5456h-3.677c-0.56568"
        " 0-1.3435-0.35355-1.7678-0.77782-0.98995-0.98995-0.84853-2.1213-0.42426-3.2527h-1.8385c-0.49497"
        " 1.6263-0.42426 3.2527 0.84853 4.5255 0.84853 0.84853 1.9799 1.2728 3.0406 1.2021h3.677c1.2728 0"
        " 2.4749-0.35355 3.3941-1.2728 1.4142-1.6971 1.3435-4.4548-0.21213-6.0104zm-11.597 5.5154h-1.2728c-0.56569"
        " 0-1.3435-0.35355-1.7678-0.77782-0.42426-0.42426-0.70711-1.1314-0.77782-1.7678 0-1.4142 1.2021-2.6163"
        " 2.5456-2.5456h3.677c0.56568 0 1.3435 0.35355 1.7678 0.77782 0.98995 0.98995 0.77782 2.192 0.42426 3.2527h1.8385c0.49498-1.6263"
        " 0.42426-3.2527-0.84853-4.5255-0.84853-0.84853-1.9799-1.2728-3.0406-1.2021h-3.677c-2.4042 0-4.3134"
        " 1.9092-4.2426 4.2426 0 2.2627 1.9092 4.3134 4.1719"
        ' 4.1719h2.687c-0.28284-0.14142-0.49497-0.35355-0.70711-0.56568-0.35355-0.35355-0.6364-0.6364-0.77782-1.0607z" '
        "/>"
        "</svg>"
    )

    assert html_equal(actual, expected)
