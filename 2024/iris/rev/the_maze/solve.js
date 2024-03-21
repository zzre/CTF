
    finished = true;

    async function pressKey(key) {
        keydownEvent = new KeyboardEvent('keydown', {
            key: key,
            code: key,
            keyCode: key,
            which: key,
        });

        keyupEvent = new KeyboardEvent('keyup', {
            key: key,
            code: key,
            keyCode: key,
            which: key,
        });

        const targetElement = document;
        targetElement.dispatchEvent(keydownEvent);
        await delay(100);
        targetElement.dispatchEvent(keyupEvent);
    }

    function delay(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    async function checkFinished() {
        while (!finished) {
            await delay(100);
        }
    }

    async function solve() {
        lst = [solve0, solve1, solve2, solve3]
        for (func of lst) {
            finished = false;
            func();
            await checkFinished();
            finished = true;
            i.g = {x: 31, y: 31}
            await pressKey(39);
            console.log(func.name + " done!");
        }
    }

    
    function solve0() {
        path = [40, 39, 37, 40, 40, 39, 40, 40, 39, 37, 38, 38, 37, 40, 38, 39, 37, 38, 38, 39, 37, 38, 39, 39, 39, 40, 38, 39, 40, 40, 37, 40, 39, 37, 37, 40, 39, 37, 38, 39, 38, 39, 38, 39, 40, 40, 38, 38];
        let idx = 0;
        async function go() {
            if (idx < path.length) {
                const key = path[idx];
                await pressKey(key);
                idx++;
                go();
            } else {
                finished = true;
            }
        }

        go();
    }
    
    
    function solve1() {
        path = [39, 39, 40, 37, 39, 38, 39, 40, 39, 39, 40, 37, 39, 40, 39, 40, 40, 40, 37, 37, 40, 39, 37, 40, 39, 40, 39, 40, 40, 38, 38, 39, 40, 38, 37, 37, 38, 37, 38, 39, 39, 37, 37, 38, 39, 39, 38, 40];
        let idx = 0;
        async function go() {
            if (idx < path.length) {
                const key = path[idx];
                await pressKey(key);
                idx++;
                go();
            } else {
                finished = true;
            }
        }

        go();
    }
    
    
    function solve2() {
        path = [39, 39, 40, 37, 39, 40, 39, 40, 40, 37, 40, 37, 39, 40, 40, 39, 40, 39, 40, 40, 37, 37, 40, 38, 39, 40, 40, 39, 40, 37, 37, 37, 37, 39, 39, 37, 40, 38, 39, 39, 40, 37, 40, 40, 37, 39, 38, 38];
        let idx = 0;
        async function go() {
            if (idx < path.length) {
                const key = path[idx];
                await pressKey(key);
                idx++;
                go();
            } else {
                finished = true;
            }
        }

        go();
    }
    
    
    function solve3() {
        path = [39, 40, 40, 38, 38, 39, 39, 40, 38, 39, 40, 38, 39, 39, 39, 39, 40, 37, 39, 40, 40, 39, 39, 40, 37, 39, 38, 39, 40, 40, 37, 40, 37, 40, 37, 39, 40, 40, 39, 40, 37, 39, 38, 37, 38, 37, 37, 40];
        let idx = 0;
        async function go() {
            if (idx < path.length) {
                const key = path[idx];
                await pressKey(key);
                idx++;
                go();
            } else {
                finished = true;
            }
        }

        go();
    }
    
    solve();