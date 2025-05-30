import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  static Future<bool> validateCode(String code) async {
    const String url = 'https://your-backend.com/api/validate';

    try {
      final response = await http.post(
        Uri.parse(url),
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({'code': code}),
      );

      if (response.statusCode == 200) {
        final Map<String, dynamic> result = jsonDecode(response.body);
        return result['valid'] == true;
      }
    } catch (_) {}
    return false;
  }
}
