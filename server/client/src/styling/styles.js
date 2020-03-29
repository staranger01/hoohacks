import theme from "./theme";

const styles = {
  spiedOn: {
    textDecoration: "underline"
  },
  navItem: {
    margin: "0 20px"
  },
  betweenXsSm: {
    [theme.breakpoints.up("sm")]: {
      display: "none"
    }
  },
  upSm: {
    [theme.breakpoints.between("xs", "sm")]: {
      display: "none"
    }
  }
};

export default styles;
