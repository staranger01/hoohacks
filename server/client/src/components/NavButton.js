import React, { useState } from "react";
import { Menu, IconButton, MenuItem } from "@material-ui/core";
import MenuIcon from "@material-ui/icons/Menu";
import { withStyles } from "@material-ui/core/styles";
import styles from "../styling/styles";
import Scroll, { Element } from "react-scroll";
const ScrollLink = Scroll.Link;

function NavButton(props) {
  const { classes } = props;
  const [anchorEl, setAnchorEl] = useState(null);

  function handleOpen(evt) {
    setAnchorEl(evt.currentTarget);
  }
  function handleClose() {
    setAnchorEl(null);
  }
  return (
    <div>
      <IconButton onClick={handleOpen}>
        <MenuIcon />
      </IconButton>
      <Menu
        id="simple-menu"
        anchorEl={anchorEl}
        keepMounted
        open={Boolean(anchorEl)}
        onClose={handleClose}
      >
        <MenuItem onClick={handleClose}>X</MenuItem>
        <ScrollLink
          activeClass={classes.spiedOn}
          spy={true}
          smooth={true}
          duration={500}
          to="section1"
        >
          <MenuItem onClick={handleClose}>Section 1</MenuItem>
        </ScrollLink>
        <ScrollLink
          activeClass={classes.spiedOn}
          spy={true}
          smooth={true}
          duration={500}
          to="section2"
        >
          <MenuItem onClick={handleClose}>Section 2</MenuItem>
        </ScrollLink>
        <ScrollLink
          activeClass={classes.spiedOn}
          spy={true}
          smooth={true}
          duration={500}
          to="section3"
        >
          <MenuItem onClick={handleClose}>Section 3</MenuItem>
        </ScrollLink>
        <ScrollLink
          activeClass={classes.spiedOn}
          spy={true}
          smooth={true}
          duration={500}
          to="section4"
        >
          <MenuItem onClick={handleClose}>Section 4</MenuItem>
        </ScrollLink>
      </Menu>
    </div>
  );
}

export default withStyles(styles)(NavButton);
