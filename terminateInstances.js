var AWS = require('aws-sdk');
AWS.config.update({ region: 'us-east-1' });
var ec2 = new AWS.EC2();

function ec2Operations(){
    var params = {
        InstanceIds: [
           "i-0e2450b00164b25fb","i-01533ca6a39faa7fb","i-080f80df6da014106","i-0dc4871a2426bc3ee"
        ]
       };
       ec2.terminateInstances(params, function(err, data) {
         if (err){ 
             console.log(err, err.stack);
        } // an error occurred
         else    {
              console.log(data);    
                }       // successful response
        
       });
}

module.exports.handler = ec2Operations;