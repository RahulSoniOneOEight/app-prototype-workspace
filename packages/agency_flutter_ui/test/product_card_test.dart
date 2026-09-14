import 'package:agency_flutter_ui/agency_flutter_ui.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  testWidgets('b2b variant renders trade metadata', (tester) async {
    await tester.pumpWidget(const MaterialApp(home: Scaffold(body: ProductCard(name: 'Pipe', price: 120, variant: ProductCardVariant.b2b, moq: 10, uom: 'box'))));
    expect(find.text('Pipe'), findsOneWidget);
    expect(find.text('MOQ 10 · box'), findsOneWidget);
  });
}
