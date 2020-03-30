import React from "react";
import HideOnScroll from "../styling/HideOnScroll";
import { AppBar, Toolbar, Typography } from "@material-ui/core";
import NavButton from "./NavButton";
import { Link } from "react-router-dom";
import { withStyles } from "@material-ui/core/styles";
import styles from "../styling/styles";

function MyAppBar(props) {
  const { classes } = props;
  const navItems = ["corOHNO", "About"];
  function renderNavItems(navItems) {
    return navItems.map(item => (
      <Link to={navItems.indexOf(item) == 0 ? "/" : `/${item}`}>
        <Typography
          variant="h5"
          className={classes.appBarItem}
        >{`${item}`}</Typography>
      </Link>
    ));
  }
  return (
    <HideOnScroll>
      <AppBar position="sticky">
        <Toolbar>
          <NavButton className={classes.upSm} navItems={navItems} />
          {renderNavItems(navItems)}
        </Toolbar>
      </AppBar>
    </HideOnScroll>
  );
}

export default withStyles(styles)(MyAppBar);
