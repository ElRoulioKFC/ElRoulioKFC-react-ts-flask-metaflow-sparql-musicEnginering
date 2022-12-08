import React from "react";

export async function callTest(un:string,deux:string):Promise<string> {
    let path: string = "/api/essai"
    path += "?un=" + un + "&deux=" + deux;

    const response = await fetch(path).then(res => res.json()).then(data => {
        return data.te;
      ;});
      return response;
}
export async function callHello() {
    let path: string = "/api/launchFlow"

    const response = await fetch(path)
}