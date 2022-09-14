const LETTERS = {
  PERIOD: `.`,
  SLASH: '/',
  OTHERS: `MEH`,
} as const

function lookAhead(path: string, currentIndex: number): null | string {
  return path[currentIndex + 1] ?? null
}

/**
 * walks until you find 
 */
function tokenize(path: string): string[] {
  let token = ``
  let tokens: string[] = []
  let prevCharKind: typeof LETTERS[keyof typeof LETTERS] | null = null

  const pushToken = () => {
    if (token === ``) return
    tokens.push(token)
    token = ``
  }

  for (let i = 0; i < path.length; i++) {
    switch (path[i]) {
      case LETTERS.PERIOD:
        if (prevCharKind !== LETTERS.PERIOD) {
          pushToken()
        }
        token += path[i]

        prevCharKind = LETTERS.PERIOD
        break
      case LETTERS.SLASH:
        if (prevCharKind !== LETTERS.SLASH) {
          pushToken()
        }
        // multiple slashes are equivalent to one slash
        token = `/`
          
        prevCharKind = LETTERS.SLASH
        break
      default:
        if (prevCharKind !== LETTERS.OTHERS) {
          pushToken()
        }

        token += path[i]
        prevCharKind = LETTERS.OTHERS
    }
  }
  // last token
  tokens.push(token)

  return tokens
}
function simplifyPath(path: string): string {
  const stack: string[] = []

  const peek = () => stack.length === 0 ? null : stack[stack.length - 1]

  const tokens = tokenize(path)
  const simplifiedPath = ``
  console.log(tokens)
  while (tokens.length) {
    const lastToken = tokens.pop()
  }

  return simplifiedPath;
};