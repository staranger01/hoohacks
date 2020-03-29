import React from "react";
import Filler from "./Filler";
import { Element } from "react-scroll";

function Insights(props) {
  const sections = [
    "Donald Trump",
    "Barrack Obama",
    "Taylor Swift",
    "Bernie Sanders"
  ];
  function renderSections(sections) {
    return sections.map(title => (
      <Element id={`${title}`}>
        <Filler title={`${title}`} />
      </Element>
    ));
  }
  return (
    <div>
      <nav></nav>
      <Container>{renderSections(sections)}</Container>
    </div>
  );
}

export default Insights;
