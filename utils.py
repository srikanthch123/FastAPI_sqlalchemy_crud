

class GlobalHelper:
    def success_response(status_code:int,message:str,data:list[dict]):
        return {"status_code":status_code,'message':message,"data":data}
    
    def error_response(status_code:int,message:str,error_code:str):
        return {'status_code':status_code,'message':message,'error_code':error_code}