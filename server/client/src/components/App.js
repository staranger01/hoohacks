import React, { useState } from "react";
import {
  Typography,
  AppBar,
  Toolbar,
  IconButton,
  Button,
  Container,
  Menu,
  ThemeProvider
} from "@material-ui/core";
import { BrowserRouter, Route, Link } from "react-router-dom";
import Filler from "./Filler";
import MenuIcon from "@material-ui/icons/Menu";
import NavButton from "./NavButton";
import theme from "../styling/theme";
import Scroll, { Element } from "react-scroll";
import { withStyles } from "@material-ui/core/styles";
import styles from "../styling/styles";
import HideOnScroll from "../styling/HideOnScroll";
const ScrollLink = Scroll.Link;

function App(props) {
  const { classes } = props;
  const navItems = ["section 1", "section 2", "section 3", "section 4"];

  function renderNavItems(navItems) {
    return navItems.map(title => (
      <ScrollLink
        activeClass={classes.spiedOn}
        spy={true}
        smooth={true}
        duration={500}
        to={`${title}`}
        className={classes.upSm}
      >
        <Typography variant="h5">
          <span className={classes.navItem}>{`${title}`}</span>
        </Typography>
      </ScrollLink>
    ));
  }

  function renderSections(navItems) {
    return navItems.map(title => (
      <Element id={`${title}`}>
        <Filler title={`${title}`} />
      </Element>
    ));
  }
  return (
    <ThemeProvider theme={theme}>
      <BrowserRouter>
        <Container>
          <HideOnScroll>
            <AppBar position="sticky">
              <Toolbar>
                <NavButton className={classes.betweenXsSm} />
                {renderNavItems(navItems)}
              </Toolbar>
            </AppBar>
          </HideOnScroll>

          <Route exact path="/">
            {renderSections(navItems)}
          </Route>
          <Route exact path="/1">
            <h1>page1</h1>
          </Route>
          <Route exact path="/2">
            <h1>page2</h1>
          </Route>
        </Container>
      </BrowserRouter>
    </ThemeProvider>
  );
}

export default withStyles(styles)(App);
