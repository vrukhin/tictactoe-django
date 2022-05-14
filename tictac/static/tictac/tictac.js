const cell_buttons = document.querySelectorAll('.tictac-field-button');
const roomID = JSON.parse(document.getElementById('room-id').textContent);
let roomState = JSON.parse(document.getElementById('room-state').textContent);
const cells_disabled_states = {
    '-': false,
    'X': true,
    'O': true,
}
const cells_values = {
    '-': '\xa0',
    'X': 'X',
    'O': 'O',
}
const winnerLines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 5],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
]
const winners = {
    'O': 'Нолики',
    'X': 'Крестики',
}
let player = 'X';
let next_player = 'O';

for (var i = 0; i < cell_buttons.length; i++)(function(i) {
    cell_buttons[i].disabled = cells_disabled_states[roomState[i]];
    cell_buttons[i].textContent = cells_values[roomState[i]]
    cell_buttons[i].onclick = function() {
        roomSocket.send(JSON.stringify({
            'player': player,
            'cell': this.id,
        }));
    }
})(i);

checkWinner = function(roomState, winnerLines) {
    for (let line of winnerLines) {
        if (roomState[line[0]] === roomState[line[1]] && roomState[line[1]] === roomState[line[2]] && roomState[line[0]] != '-') {
            return roomState[line[0]];
        }
    }
    return null;
}

const roomSocket = new WebSocket(
    'ws://' +
    window.location.host +
    '/ws/tictac/rooms/' +
    roomID +
    '/'
)

roomSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    btn = document.querySelector('#' + data.cell);
    btn.textContent = data.player;
    btn.disabled = true;
    [player, next_player] = [next_player, player];
    winner = checkWinner(data.state, winnerLines);
    if (winner) {
        alert(winners[winner] + ' выиграли!');
        for (var i = 0; i < cell_buttons.length; i++)(function(i) {
            cell_buttons[i].disabled = true;
        })(i);
    }
}