import theme from "./theme";

const styles = {
  spiedOn: {
    textDecoration: "underline"
  },
  navItem: {
    margin: "0 20px"
  },
  size1: {
    [theme.breakpoints.up("md")]: {
      display: "none"
    }
  },
  size2: {
    [theme.breakpoints.down("sm")]: {
      display: "none"
    }
  }
};

export default styles;
