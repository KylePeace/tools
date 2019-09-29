
var fs = require('fs'); 
var nodeCmd = require('node-cmd');

let pngquantPath = "C:/Users/Administrator/Desktop/test/pngquant/"

let targetDir = "C:/Users/Administrator/Desktop/test/pngquant/boss3"

// let outPutPath  = "C:/Users/Administrator/Desktop/test/pngquant/boss2"


String.prototype.format = function () {
    var values = arguments;
    return this.replace(/\{(\d+)\}/g, function (match, index) {
        if (values.length > index) {
            return values[index];
        } else {
            return "";
        }
    });
};


// let cmd = pngquantPath+"pngquant.exe --force --verbose --speed=1 --ordered 256 {1} --output {2}" %(srcFile, dstFile)
let cmd = pngquantPath+"pngquant.exe --force --verbose --speed=1 --ordered 256 {0} --output {1} " 



var walk = function(dir) {
    var results = []
    var list = fs.readdirSync(dir)
    list.forEach(function(fileName) {
        file = dir + '/' + fileName
        var stat = fs.statSync(file)
        //console.log(fileName)
        if(file.match(".png|.PNG|.JPG|.jpg")){
            let cmdStr = cmd.format(file,file)
            nodeCmd.get(cmdStr,function(err, data, stderr){
                if (err) {
                    console.log(err+'')
                    
                }else{
                   console.log("压缩成功",data)
                }
                    
           });
            nodeCmd.run(cmdStr);
            // console.log(cmdStr)
            return  
        }

        

        if (stat && stat.isDirectory()) results = results.concat(walk(file))
        else results.push(file)
    })
    return results
}


let c1 = walk(targetDir)

// console.log(c1)