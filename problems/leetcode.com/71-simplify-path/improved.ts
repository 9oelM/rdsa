export function simplifyPath(path: string) {
  let stack: string[] = [];
  const splitPath: string[] = path.split('/');
  
  for (let i=0;i< splitPath.length;i++) {
      if (splitPath[i]=='.' || splitPath[i]=='') continue;
      if (splitPath[i]=='..') stack.pop();
      else stack.push(splitPath[i]);
  }
  
  return '/'+stack.join('/');
};
