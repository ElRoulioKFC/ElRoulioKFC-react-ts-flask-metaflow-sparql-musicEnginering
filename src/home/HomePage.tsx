import { Button, TextField, Typography } from "@mui/material";
import React, { useEffect } from "react";
import { callTest,callHello } from "../interface";

export function HomePage(){
    const [ezTest, setEzTest] = React.useState<string>("");
    const [testContent, setTestContent] = React.useState({
        "un": "1",
        "deux": "2"
    });
    const launchEzTest = async () => {
            const test = await callTest(testContent.un, testContent.deux)
            test != null ? setEzTest(test):setEzTest("error")
    }
    return<div>
            <h1>Home Page</h1>
            <p>Home page body content</p>
            <Typography variant="h5">LaunchTest api</Typography>
                <div>
                    <TextField
                        label="un"
                        id="outlined-size-small"
                        defaultValue={testContent.un}
                        size="small"
                        onChange={(e) => setTestContent({ ...testContent, un: e.target.value })} />
                    <TextField
                        label="deux"
                        id="outlined-size-small"
                        defaultValue={testContent.deux}
                        size="small"
                        onChange={(e) => setTestContent({ ...testContent, deux: e.target.value })} />
                </div>
                <div>
                    <Button variant="contained" onClick={() => { launchEzTest() } }>Submit</Button>
                </div>
            <div>
                <Typography variant="h5">Résults</Typography><div>
                <p>
                    <p>calcul: {ezTest}</p>
                </p>
            </div>
            <div>
                <Button variant="contained" onClick={() => { callHello()} }>callHello</Button>
            </div>
        </div>
        </div>
        
}
