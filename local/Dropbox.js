// JavaScript source code
const puppeteer = require('puppeteer');

var myArgs = process.argv.slice(2);
var busca = myArgs[0];
argumentos = ['https://www.dropbox.com/sh/vuhn9yr0gxntnmb/AACeY6qxzi7FNsZ413SEDeM3a?dl=0','https://www.dropbox.com/sh/8ei2kfbf0u88zh2/AAC4Yc1ZpmxpB6MDxZ6mcjWWa?dl=0','https://www.dropbox.com/sh/z2qw4egoyoypr2u/AABSVaXGFVos3amCUU6pUoy3a?dl=0','https://www.dropbox.com/sh/242jkg2tznmnbpj/AACUCITfCm4DRCBGVyj477zHa?dl=0','https://www.dropbox.com/sh/kpr0jlc4w76logp/AACSD6QQW2tIgtAdOAOt__4Ea?dl=0','https://www.dropbox.com/sh/0499fesjmiis3xq/AADCXwvcNlFbBU9pMFLas5Rfa?dl=0','https://www.dropbox.com/sh/2bocp5qffs3afs5/AABFn19_TBqL6daD9QGGLulNa?dl=0','https://www.dropbox.com/sh/3revm5znz2rez5q/AADcQ5Ij7xTuOTW3Dk_BrmPVa?dl=0','https://www.dropbox.com/sh/ztkzzszd309cxyc/AACgdL-U7Lvup5eYAVijLizka?dl=0','https://www.dropbox.com/sh/j11vhqdy93o3f0o/AAAE5b1dE6gjcEowwoyVb7Tta?dl=0']

let dropbox = async () => {
    const browser = await puppeteer.launch()
    const page = await browser.newPage()
	//for (var x = 0; i < argumentos.length; i++) {
	//console.log (argumentos[0])
	await page.goto(myArgs[0]+'&lst=')
	for (var i = 0; i < 5; i++) {
		//previousHeight = await page.evaluate('document.body.scrollHeight');
		//await page.evaluate('window.scrollTo(0, document.body.scrollHeight - 500)');
		//await page.waitForFunction(`document.body.scrollHeight > ${previousHeight}`);
		//await page.waitFor(300);
		await page.evaluate('window.scrollTo(0, 50000)');
		await page.waitFor(3000);
	}

    const result = await page.evaluate( () => {
        var saida = [];
        var titulo = [];
        var descr = [];
        var data = [];
        var link = [];
        var list2 = document.querySelectorAll('tbody > tr');
        for (var i = 0; i < list2.length; i++) {
            titulo.push(list2[i].getElementsByTagName("a")[0].getAttribute("aria-label"));
            //descr.push(list2[i].getElementsByClassName("job-result-card__snippet")[0].textContent);
            data.push(list2[i].getElementsByClassName("mc-media-cell-text mc-media-cell-text-title")[1].textContent);
            link.push(list2[i].getElementsByTagName("a")[0].getAttribute("href"));
        }
        saida = { titulo, data , link };
        return saida
    })
    browser.close();
    return result
};
//}

dropbox().then((value) => {
	//console.log (value)
	var tamanho = value.titulo.length
	for (var i = 0; i < value.titulo.length; i++) {
		console.log (value.titulo[i] + ";" + value.data[i] + ";" +value.link[i]);
	}
	//console.log(JSON.stringify(value));
});

