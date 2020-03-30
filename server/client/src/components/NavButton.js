import React, { useState } from "react";
import { Menu, IconButton, MenuItem } from "@material-ui/core";
import MenuIcon from "@material-ui/icons/Menu";
import { withStyles } from "@material-ui/core/styles";
import styles from "../styling/styles";
import { Link } from "react-router-dom";
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

  function renderNavItems(navItems) {
    return navItems.map(item => (
      <Link to={`/${item}`}>
        <MenuItem onClick={handleClose}>{`${item}`}</MenuItem>
      </Link>
    ));
  }
  function renderSideBarItems(navItems) {
    return navItems.map(title => (
      <ScrollLink
        activeClass={classes.spiedOn}
        spy={true}
        smooth={true}
        duration={500}
        to={`${title}`}
      >
        <MenuItem onClick={handleClose}>{`${title}`}</MenuItem>
      </ScrollLink>
    ));
  }
  return (
    <div className={classes.size1}>
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
        {renderNavItems(props.navItems)}
      </Menu>
    </div>
  );
}

export default withStyles(styles)(NavButton);
