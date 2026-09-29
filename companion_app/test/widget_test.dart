import 'package:flutter_test/flutter_test.dart';
import 'package:secondpaytech_companion/main.dart';

void main() {
  testWidgets('App smoke test', (WidgetTester tester) async {
    await tester.pumpWidget(const SecondPayTechCompanionApp());
    expect(find.text('2ndPayTech SMS Gateway'), findsOneWidget);
  });
}
