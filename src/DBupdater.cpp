#include <iostream>
#include <fstream>
#include <mariadb/conncpp.hpp>

using namespace std;

class DBupdater 
{
public:
    DBupdater() {
//생성자: 마리아DB 연결 및 종목코드 딕셔너리 생성//
    }

    ~DBupdater() {
//소멸자: 마리아DB 연결해제//
    }

    iostream& read_yahoo_code() {
        //상장법인목록 파일 읽어와서 데이터프레임 변환 // 
    }

    string& update_corp_info() {
        //종목코드를 corporate_info 테이블에 업데이트후 딕셔너리에 저장//
    }



};
