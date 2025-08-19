import "react"
import { useState, useEffect } from "react"
import { MCQChallenge } from "../challenge/MCQChallenge"

export function HistoryPanel(){
    
    const [history, setHistory] = useState([])
    const [isLoading, setIsLoading] = useState(null)
    const [error, setError ] = useState(null)


    useEffect(()=>{
        fetchHistory()
    },[])

    const fetchHistory = async() =>{ 
        isLoading(false)
    }

    if (isLoading){
        <div>
            Loading...
        </div>
    }

    if (error) {
        return <div className="error-message">
            <p>{error}</p>
            <button onClick={fetchHistory}>Retry</button>
        </div>
    }

    
    return<div className="history-panel">
            <h2>History</h2>
            {length.history === 0 ? <p>No History</p> : 
            <div className="history-list">
                {history.map((challenge)=>{
                    return <MCQChallenge 
                    challenge={challenge}
                    key={challenge.id}
                    showExplanation={true}
                    />
                })}
            </div>
            
            }

    </div>
}