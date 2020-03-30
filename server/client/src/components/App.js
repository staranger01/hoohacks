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
import Landing from "./Landing";
import About from "./About";
import MyAppBar from "./MyAppBar";
const ScrollLink = Scroll.Link;

function App(props) {
  const { classes } = props;

  return (
    <ThemeProvider theme={theme}>
      <BrowserRouter>
        <Container>
          <MyAppBar />

          <Route exact path="/">
            <Landing />
          </Route>
          <Route exact path="/about">
            <About />
          </Route>
        </Container>
      </BrowserRouter>
    </ThemeProvider>
  );
}

export default withStyles(styles)(App);
