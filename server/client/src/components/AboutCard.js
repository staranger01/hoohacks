import React from "react";
import { Card, CardContent, Typography } from "@material-ui/core";

function AboutCard(props) {
  /*props:{
    name:
    pic:
    contribution:
  }
  */
  const { name, college, contribution } = props.person;
  return (
    <div>
      <Card>
        <CardContent>
          <Typography variant="h5">{name}</Typography>
          <Typography variant="body2">{college}</Typography>
          <Typography variant="body1">{contribution}</Typography>
        </CardContent>
      </Card>
    </div>
  );
}

export default AboutCard;
