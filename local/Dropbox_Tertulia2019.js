// JavaScript source code
const puppeteer = require('puppeteer');

let dropbox = async () => {
    const browser = await puppeteer.launch()
    const page = await browser.newPage()
    await page.goto('https://www.dropbox.com/sh/otin06bro9p4izs/AABdGcmTA7lDp-t5crR8sAmKa?dl=0&lst=')
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


dropbox().then((value) => {
	console.log(JSON.stringify(value));
});

