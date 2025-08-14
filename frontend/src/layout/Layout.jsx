import "react"
import { SignedIn, SignedOut, UserButton } from "@clerk/clerk-react"
import { Outlet, Link, Navigate } from "react-router-dom"

export function Layout() {
    return <div className="app-layout">
        <header className="app-header">
            <div className="header-content">
                <h1>CodeAI</h1>
                <SignedIn>
                    <nav>
                        <Link to='/'>Generate Challenge</Link>
                        <Link to='/'>History</Link>
                        <UserButton />
                    </nav>
                </SignedIn>
            </div>
        </header>

    </div>
}