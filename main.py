from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[WebSocket, str] = {}

    async def connect(self, websocket: WebSocket, username: str):
        await websocket.accept()
        self.active_connections[websocket] = username
        await self.broadcast(f"{username} joined the chat")

    def disconnect(self, websocket: WebSocket):
        username = self.active_connections.get(websocket)
        if username:
            del self.active_connections[websocket]
            return username
        return None

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


@app.get("/", response_class=HTMLResponse)
async def get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    await manager.connect(websocket, username)
    try:
        while True:
            data = await websocket.receive_text()
            # Create a styled HTML message
            decorated_message = f"""
            <div class="p-2 bg-gray-100 rounded-lg shadow-sm my-2">
                <span class="font-bold text-blue-600">{username}</span>: 
                <span class="text-gray-800">{data}</span>
            </div>
            """
            await manager.broadcast(decorated_message)
    except WebSocketDisconnect:
        username = manager.disconnect(websocket)
        if username:
            # Styled disconnect message
            decorated_disconnect_message = f"""
            <div class="p-2 bg-red-100 rounded-lg shadow-sm my-2">
                <span class="text-red-600 font-semibold">{username} left the chat</span>
            </div>
            """
            await manager.broadcast(decorated_disconnect_message)
