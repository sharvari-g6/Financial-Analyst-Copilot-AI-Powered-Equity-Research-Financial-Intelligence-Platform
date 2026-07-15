import { useState } from "react";
import api from "../services/api";
import "./Upload.css";

function Upload(){

    const[file,setFile]=useState(null);

    const[company,setCompany]=useState("");

    const[year,setYear]=useState("");

    const[msg,setMsg]=useState("");

    const upload=async()=>{

        if(!file){

            alert("Select PDF");

            return;

        }

        const form=new FormData();

        form.append("file",file);

        form.append("company",company);

        form.append("year",year);

        try{

            const res=await api.post("/upload",form);

            setMsg(res.data.message);

        }

        catch{

            setMsg("Upload Failed");

        }

    }

    return(

        <div className="upload-page">

            <div className="upload-card">

                <h1>

                    Upload Annual Report

                </h1>

                <p>

                    Upload the company's annual report
                    and let AI perform a complete
                    financial analysis.

                </p>

                <input

                type="file"

                accept=".pdf"

                onChange={(e)=>setFile(e.target.files[0])}

                />

                <input

                type="text"

                placeholder="Company Name"

                value={company}

                onChange={(e)=>setCompany(e.target.value)}

                />

                <input

                type="number"

                placeholder="Year"

                value={year}

                onChange={(e)=>setYear(e.target.value)}

                />

                <button

                onClick={upload}

                >

                    Upload & Analyze

                </button>

                <h3>

                    {msg}

                </h3>

            </div>

        </div>

    )

}

export default Upload;