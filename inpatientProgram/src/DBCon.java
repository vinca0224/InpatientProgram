import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

class DBCon {
        void connect(){
    		Connection conn = null;
		try {
			Class.forName("oracle.jdbc.driver.OracleDriver");
			String url = "jdbc:oracle:thin:@localhost:1521:xe";
			String user = "ADAM";
			String pw = "1234";
			String sql = "SELECT * FROM EMP";
			conn = DriverManager.getConnection(url, user, pw);
			System.out.printf("DB 연결 성공!\n");
			
			Statement st = conn.createStatement();
			ResultSet rs = st.executeQuery(sql);
			//data 읽어오기
			while(rs.next()) {
				for(int i=1; i<9; i++) {
					String en = rs.getNString(i);
					System.out.printf("%s ",en);
				}System.out.println();
			}
		} catch (ClassNotFoundException | SQLException e) {
			e.printStackTrace();
		} finally {
			try {
				conn.close();
				System.out.printf("DB 연결 해제\n");
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
    }
}
