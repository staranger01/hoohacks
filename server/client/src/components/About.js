import React from "react";
import { Typography, Grid } from "@material-ui/core";
import AboutCard from "./AboutCard";

function About(props) {
  const cardContent = [
    {
      name: "May Kamreen",
      college: "GGC",
      contribution: "project management/troubleshooting"
    },
    {
      name: "Caleb Chang",
      college: "CUNY, Queens College",
      contribution: "created website"
    },
    {
      name: "Hisham Iqbal",
      college: "UVA",
      contribution:
        "helped with the google cloud products and the data visualization"
    },
    {
      name: "Evert Garcia-Guzman",
      college: "denver?",
      contribution: "used google cloud products to webscrape"
    },
    {
      name: "Mohmmadhalimy",
      college: "?what college",
      contribution: "data visualization"
    }
  ];
  return (
    <div>
      <Grid container spacing={3}></Grid>
      <Typography variant="h1">This is the about section</Typography>
      {cardContent.map(person => (
        <AboutCard person={person} />
      ))}
    </div>
  );
}

export default About;
