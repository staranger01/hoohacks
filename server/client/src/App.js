import React from "react";
import {
  Typography,
  AppBar,
  Toolbar,
  IconButton,
  Button,
  Container
} from "@material-ui/core";
import { BrowserRouter, Route, Link } from "react-router-dom";
import Filler from "./Filler";
import Scroll, { Element } from "react-scroll";
import MenuIcon from "@material-ui/icons/Menu";
const ScrollLink = Scroll.Link;

function App() {
  return (
    <BrowserRouter>
      <Container>
        <Route exact path="/">
          <AppBar position="static">
            <Toolbar>
              <IconButton>
                <MenuIcon />
              </IconButton>
              <ScrollLink spy={true} smooth={true} duration={500} to="section4">
                Section 4
              </ScrollLink>
            </Toolbar>
          </AppBar>
          <nav></nav>

          <Filler />
          <Filler />
          <Filler />
          <Element id="section4" name="section4">
            <Filler />
          </Element>
        </Route>
        <Route exact path="/1">
          <h1>page1</h1>
        </Route>
        <Route exact path="/2">
          <h1>page2</h1>
        </Route>
      </Container>
    </BrowserRouter>
  );
}

export default App;
