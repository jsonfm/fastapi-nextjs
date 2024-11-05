import { NextResponse } from "next/server"

export const GET = async () => {
    return NextResponse.json({
        message: "about message from Next.js!"
    })
}