
var fs = require('fs'); 
var nodeCmd = require('node-cmd');
var images = require("images");

let targetDir = "./tex2"  //遍历目录
let isCompressJpg = true  //是否压缩jpg文件


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


let cmd = "pngquant.exe --force --verbose --speed=1   --ordered 256  {0} --output {1} " 




var compressPng = function (file) {
    let cmdStr = cmd.format(file,file)
    nodeCmd.get(cmdStr,function(err, data, stderr){
        if (err) {
            console.log("压缩出现似乎出现错误，但不影响:",file)            
        }else{
           console.log("压缩成功\n",file)
        }       
   });
   nodeCmd.run(cmdStr);
}
var compressJpg = function (file) {
   images(file)                                                              
        .save(file, {               
            quality : 80                   
        });
        console.log("压缩成功\n",file)
}

var walk = function(dir) {
    var results = []
    var list = fs.readdirSync(dir)
    list.forEach(function(fileName) {
        file = dir + '/' + fileName
        var stat = fs.statSync(file)
        if(fileName.match(".png|.PNG")){
           compressPng(file)
        }

        if(file.match(".JPG|.jpg")&&isCompressJpg){
            compressJpg(file)                                                              
        }
        
        if (stat && stat.isDirectory()) results = results.concat(walk(file))
        else results.push(file)
    })
    return results
}


let c1 = walk(targetDir)

//console.log(c1)

