var AWS = require('aws-sdk');
AWS.config.update({ region: 'us-east-1' });
var sns = new AWS.SNS();
var ec2 = new AWS.EC2();

function ec2Operations(){
    var params = { 
        ImageId: "ami-04b9e92b5572fa0d1", 
        InstanceType: "t2.micro", 
        KeyName: "140919", 
        MaxCount: 1, 
        MinCount: 1, 
        SecurityGroupIds: [
           "sg-046d29f67dd4b43dc"
        ], 
        SubnetId: "subnet-79773a57", 
       };
       ec2.runInstances(params, function(err, data) {
         if (err){
              console.log(err, err.stack);
          } // an error occurred
         else {
                 console.log(data);  
                 setTimeout(function () {
                    attachEIP(data[0].InstanceId) ;  
                  }, 30000)   // successful response
         }
       });

}

function attachEIP(InstanceId){
    var params = {
        AllocationId: "eipalloc-0cc2df4a717bfa9b6", 
        InstanceId: InstanceId
       };
       ec2.associateAddress(params, function(err, data) {
         if (err) console.log(err, err.stack); // an error occurred
         else     console.log(data);           // successful response
         /*
         data = {
          AssociationId: "eipassoc-2bebb745"
         }
         */
       });
}

module.exports.handler = ec2Operations;