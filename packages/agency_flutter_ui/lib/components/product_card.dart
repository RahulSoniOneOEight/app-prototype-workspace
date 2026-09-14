import 'package:flutter/material.dart';
import 'price_display.dart';
import 'verified_badge.dart';

enum ProductCardVariant { standard, compact, marketplace, b2b, bulk }

class ProductCard extends StatelessWidget {
  const ProductCard({
    super.key,
    required this.name,
    required this.price,
    this.imageUrl,
    this.variant = ProductCardVariant.standard,
    this.seller,
    this.sellerVerified = false,
    this.moq,
    this.uom,
    this.onTap,
  });

  final String name;
  final double price;
  final String? imageUrl;
  final ProductCardVariant variant;
  final String? seller;
  final bool sellerVerified;
  final int? moq;
  final String? uom;
  final VoidCallback? onTap;

  bool get _showsTradeMetadata =>
      variant == ProductCardVariant.b2b || variant == ProductCardVariant.bulk;

  @override
  Widget build(BuildContext context) {
    return Card(
      child: InkWell(
        onTap: onTap,
        child: Padding(
          padding: const EdgeInsets.all(12),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              if (imageUrl != null)
                AspectRatio(
                  aspectRatio: 1,
                  child: Image.network(imageUrl!, fit: BoxFit.cover),
                ),
              Text(name, maxLines: 2, overflow: TextOverflow.ellipsis),
              const SizedBox(height: 4),
              PriceDisplay(price: price),
              if (seller != null) ...[
                const SizedBox(height: 4),
                Row(
                  children: [
                    Flexible(child: Text(seller!)),
                    if (sellerVerified) ...[
                      const SizedBox(width: 6),
                      const VerifiedBadge(compact: true),
                    ],
                  ],
                ),
              ],
              if (_showsTradeMetadata && (moq != null || uom != null)) ...[
                const SizedBox(height: 4),
                Text([if (moq != null) 'MOQ $moq', if (uom != null) uom!].join(' · ')),
              ],
            ],
          ),
        ),
      ),
    );
  }
}
