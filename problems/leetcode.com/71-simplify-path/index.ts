const TOKEN_KINDS = {
  PERIOD: `.`,
  SLASH: '/',
  DIR_OR_FILE_NAME: `DIR_OR_FILE_NAME`,
} as const

type Token = {
  kind: typeof TOKEN_KINDS[keyof typeof TOKEN_KINDS],
  str: string
}

export function tokenize(path: string): Token[] {
  let token: Token | null = null
  let tokens: Token[] = []
  let prevCharKind: typeof TOKEN_KINDS[keyof typeof TOKEN_KINDS] | null = null
  const processToken = () => {
    if (!token) return
    // must be a string full of periods, longer than or equal to "..."
    if (token.str !== `.` && token.str !== `..` && token.kind === TOKEN_KINDS.PERIOD) {
      token.kind = TOKEN_KINDS.DIR_OR_FILE_NAME
      prevCharKind = TOKEN_KINDS.DIR_OR_FILE_NAME
    }
    tokens.push(token)
    token = null
  }

  for (let i = 0; i < path.length; i++) {
    const updateToken = (kind: Token['kind']) => {
      if (token) {
        // multiple slashes are equivalent to one slash
        if (kind === TOKEN_KINDS.SLASH) token.str = `/`
        else token.str += path[i]
      } else {
        token = {
          kind,
          str: path[i],
        }
      }
    }

    switch (path[i]) {
      case TOKEN_KINDS.PERIOD:
        if (prevCharKind === TOKEN_KINDS.SLASH) {
          processToken()
        }
        
        updateToken(TOKEN_KINDS.PERIOD)

        prevCharKind = TOKEN_KINDS.PERIOD
        break
      case TOKEN_KINDS.SLASH:
        if (prevCharKind !== TOKEN_KINDS.SLASH) {
          processToken()
        }
        updateToken(TOKEN_KINDS.SLASH)
          
        prevCharKind = TOKEN_KINDS.SLASH
        break
      default:
        if (prevCharKind === TOKEN_KINDS.SLASH) {
          processToken()
        }
        updateToken(TOKEN_KINDS.DIR_OR_FILE_NAME)
        prevCharKind = TOKEN_KINDS.DIR_OR_FILE_NAME
    }
  }
  // last token
  processToken()

  return tokens
}

function handlePrevPeriodToken(prevToken: Token | null, transformedTokens: Token[]) {
  switch (prevToken?.str) {
    // must be the last two characters of "blah_blah/./"
    // remove "." which is already in the array
    case ".":
      transformedTokens.pop()
      break
      // must be the last three characters of "blah_blah2/blah_blah/../"
      // remove the entire "blah_blah/../" part
    case "..":
      // remove ".."
      transformedTokens.pop()
      if (transformedTokens.length > 1) {
        // remove "/"
        transformedTokens.pop()
        // remove "blah_blah"
        transformedTokens.pop()
      }
      break
    default:
      throw new Error(`period has an unexpected string`)
  }
}

function handleSlashTransform(token: Token, prevToken: Token | null, transformedTokens: Token[]) {
  switch (prevToken?.kind) {
    // must be "blah_blah/"
    case TOKEN_KINDS.DIR_OR_FILE_NAME:
      transformedTokens.push(token)
      break
    case TOKEN_KINDS.PERIOD:
      handlePrevPeriodToken(prevToken, transformedTokens)
      break
    case TOKEN_KINDS.SLASH:
      throw new Error(`adjacent slashes were detected`)
    default:
      // must be the first character in the path.
      if (prevToken === null) {
        transformedTokens.push(token)
      }
  }
}

function transformer(tokens: Token[]): Token[] {
  const transformedTokens: Token[] = []
  let prevToken: Token | null = null

  for (let i = 0; i < tokens.length; i++) {
    const token = tokens[i]
    if (!token) break

    switch (token.kind) {
      case TOKEN_KINDS.SLASH:
        handleSlashTransform(token, prevToken, transformedTokens)
        break
      case TOKEN_KINDS.PERIOD:
      case TOKEN_KINDS.DIR_OR_FILE_NAME:
        transformedTokens.push(token)
        break
    }

    prevToken = token
  }
  
  if (prevToken?.kind === TOKEN_KINDS.PERIOD) {
    handlePrevPeriodToken(prevToken, transformedTokens)
  }
  // if everything is removed, keep the root directory slash "/"
  if (transformedTokens.length === 0) {
    transformedTokens.push({ kind: TOKEN_KINDS.SLASH, str: TOKEN_KINDS.SLASH })
  }
  // remove the trailing slash (which must not be the beginning slash) if it exists
  if (transformedTokens.length > 1 && transformedTokens[transformedTokens.length - 1]?.kind === TOKEN_KINDS.SLASH) {
    transformedTokens.pop()
  }
  return transformedTokens
}
function simplifyPath(path: string): string {
  const tokens = tokenize(path)
  const transformedTokens = transformer(tokens)
  return transformedTokens.reduce((prev, curr, i) => {
    return prev + curr.str
  }, ``)
};