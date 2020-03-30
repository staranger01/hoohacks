import React from "react";
import Scroll, { Element } from "react-scroll";
import { Typography } from "@material-ui/core";
import Filler from "./Filler";
const ScrollLink = Scroll.Link;

function Landing(props) {
  const { classes } = props;
  const sideBarItems = ["corOHNO!", "What we do", "Demo"];
  function renderSideBarItems(navItems) {
    return navItems.map(title => (
      <ScrollLink
        activeClass={classes.spiedOn}
        spy={true}
        smooth={true}
        duration={500}
        to={`${title}`}
        className={classes.size2}
      >
        <Typography variant="h5">
          <span className={classes.navItem}>{`${title}`}</span>
        </Typography>
      </ScrollLink>
    ));
  }
  function renderSections(sideBarItems) {
    return sideBarItems.map(title => (
      <Element id={`${title}`}>
        <Filler title={`${title}`} />
      </Element>
    ));
  }
  return (
    <div>
      <iframe
        width="600"
        height="450"
        src="https://datastudio.google.com/embed/reporting/a9baff5b-fc87-4fcf-9d81-601d945db661/page/mGDKB"
        frameborder="0"
        style={{ border: "0" }}
        allowfullscreen
      ></iframe>
      {renderSections(sideBarItems)}
    </div>
  );
}

export default Landing;
