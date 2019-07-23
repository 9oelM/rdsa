function solution(puddles, width, height){
	let startX = 0
	let startY = 0
	const row = [...Array(width)].map(elem=>0)
	let markedMap = [...Array(height)].map(elem=>[...row])
	markedMap[0][0] = 1
	obstacles.forEach(obstacle => {
		markedMap[obstacle[0]][obstacle[1]] = -1
    })
	for(let i = 0; i < width; i++){
		for(let j = 0; j < height; j++){
			if(markedMap[i][j] !== -1){ 
                if(i - 1 >= 0 && markedMap[i-1][j] !== -1)
                    markedMap[i][j] += markedMap[i-1][j]
                if(j - 1 >= 0 && markedMap[i][j-1] !== -1) 
                    markedMap[i][j] += markedMap[i][j-1]
            }
        }
    }
	return markedMap
}
