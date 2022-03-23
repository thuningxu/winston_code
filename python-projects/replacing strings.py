string = '''
if self.app.player.grid_pos.x > COLS // 2 and\
    self.app.player.grid_pos.y > ROWS // 2:
        return vec(1, 1)
if self.app.player.grid_pos.x > COLS // 2 and\
    self.app.player.grid_pos.y < ROWS // 2:
        return vec(1, ROWS - 2)
if self.app.player.grid_pos.x < COLS // 2 and\
    self.app.player.grid_pos.y > ROWS // 2:
        return vec(COLS - 2, 1)'''
string.replace('.x', '[0]')
print(string)
