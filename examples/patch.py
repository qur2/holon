# -*- coding: utf-8 -*-
"""Patch objects returned by the txtr-reaktor.
"""

import types


# Mapping of txtr UUID's to something meaningful.
# Copied from apps/reaktor_documents/mapper.py
# This list seems not to be complete.
ID_TO_NAME = {
    '20514d7d-7591-49a4-a62d-f5c02a8f5edd' : 'author',
    '65534960-94f7-4cb8-b473-d2ce34740f44' : 'title',
    'a95ae1a4-23d6-4f99-a306-4c64c0d8b1ea' : 'subtitle',
    'd968f428-fa66-47fc-8d40-9092cdd35c4b' : 'note',
    '0bc56cdc-1bee-4b0d-a4a5-00b79831a1ed' : 'date',
    '2ada5e59-e695-4ba8-8e26-2dffaee88f55' : 'abstract',
    '108907b5-7bd5-4510-8e2f-8e14d6b52e3b' : 'status',
    'abb2f161-35f6-405b-99e0-a6c908715f6d' : 'url',
    'c4e9e520-8103-4d92-a18b-0cd77abcb886' : 'tex_type',
    '8252c9f4-97be-4299-a76b-792d98875d32' : 'key',
    '45675fa2-bc70-4e47-bd71-2b321982e4ae' : 'natures',
    'd562fc92-308f-44c5-8e17-fd024d13d0ce' : 'editor',
    '8af805fc-27c2-4753-af4e-24f8e680bfff' : 'publisher',
    '76c43cd3-66f8-44af-a543-8075e926d028' : 'location_of_publication',
    '264a88e1-62df-4291-95bd-e1c8ae3ed544' : 'year_of_publication',
    '86bd46fb-33b9-44e7-8887-c083d8f73699' : 'isbn',
    'f369cb47-e696-4437-9add-d585e6a1acb1' : 'translator',
    'c5c0941e-dfe6-4ee4-a6e4-525d0aa6154b' : 'language',
    '1419e84c-d24d-4c9f-b568-0278a06df527' : 'binding',
    'c9f0c626-009e-47cf-ba06-7158186ec6af' : 'edition',
    '5d4f2c37-5ecb-4afe-84fd-96de6567e61e' : 'series',
    '89ecd706-8427-4451-b882-854bd215adeb' : 'organization',
    '3cb93a1d-7191-4db1-82dd-84e7eef02989' : 'genre',
    'fffcae65-2196-4661-8e40-b5ac350a9dd3' : 'volume',
    '24293836-2f0e-4362-a38d-0f9a2f9f80f7' : 'number',
    'fc0747ae-3a6e-4f14-b1f7-fed5a982a40f' : 'journal',
    '36aad0d0-a829-4bae-98ee-534d4ce953a8' : 'pages',
    '05e537b3-b72c-4e78-a2fa-f27c22998663' : 'chapter',
    'afac2cff-61ef-47ce-8aab-1d1139674bcf' : 'containing_book',
    '52d3e4fa-37fb-43e5-bd0b-b43f2f78eafd' : 'provider',
    '9d555d05-b668-48b0-bc1b-90c524837279' : 'provider_logo_url',
    '1654dcfd-40a7-4746-b3b0-387e70dfcb90' : 'provider_logo_link_url',
    '913e8249-5bbd-4d2f-9705-8beb0e51dce2' : 'provider_link_url',
    'e1675548-0e27-411d-be59-1a9b00e34290' : 'provider_claim',
    'd24af6ea-402e-47b7-9bb5-f64c237ce775' : 'provider_flags',
    '8686c091-366b-4dad-ae3c-8fedc6bed741' : 'importer_organization',
    '1980a6e8-8868-4081-99e3-3c7d52dd6095' : 'importer',
    '343dd4ed-cb29-4d10-abd5-0e119d4d0944' : 'importer_version',
    '3b91b5dd-9b7c-4542-a0e8-666a1b73a595' : 'importer_data',
    '84ec958f-a84f-46fd-85a7-046c26257225' : 'sync_id',
    '0e73de16-2e13-4112-b297-2969f1003645' : 'feed_url',
    'd24e2c74-e1ff-4c36-a570-62837852965a' : 'guid',
    '9829f56e-8f5d-4d37-b1b4-77d3b5ccbcd4' : 'comments',
    '857c5576-b54f-46ea-b389-25f11a13dfe2' : 'summary',
    '836a2044-aaba-4299-aab1-b35f6a0b40fd' : 'modification_date',
    'cdc93ba7-9461-41fa-b3e5-7f5d3e14e354' : 'primary_category_id',
    '33abea90-9979-4744-b4ae-cc7f7743fb0f' : 'primary_category_discovered_id',
    'c635ce65-3480-4ac0-a542-1edba1e8b613' : 'secondary_category_id',
    'ac175e55-b146-4268-889e-a5d6fb096274' : 'secondary_category_discovered_id',
    '3949e8bf-bc3a-4ceb-9409-3558a60b5a64' : 'tertiary_category_id',
    '4ded0639-8e4f-4a80-bb1f-6005f116307d' : 'tertiary_category_discovered_id',
    'f312e645-a3c9-46a9-b7ca-fce072a1cd65' : 'description',
    '698cc249-d052-4b0b-ae96-df0bd7967c2f' : 'extract',
    '658400da-3092-49d2-a8fd-1a1ba1b9e23f' : 'video',
    '3e098a6e-9fc0-44fd-b28f-56a66a25869a' : 'audio',
    'dd68c7a1-11a2-4c21-a811-408c06a92cf0' : 'web_site',
    '5f254a1a-4c36-4dbf-9afe-6ae6b1f53466' : 'size',
    '44cc1c3a-2313-44ce-924f-4a486e2e8d8f' : 'number_of_pages',
    '223eb465-4cd9-4ae4-8253-8d03f14f47d4' : 'available_as_pdf',
    '08e63728-7013-416e-9ab0-6d6a31a06300' : 'available_as_pdf_mobile',
    '9ce2d40f-d0b8-42e9-a564-7f7c61a6daba' : 'available_as_epub',
    '1203e8e3-f439-49cd-ab02-6286d2592eb3' : 'available_without_drm',
    '24849f04-cf5b-4167-93cb-dac57eb80959' : 'available_with_adobe_drm',
    '5c623967-f4d7-48f7-a749-25445214f875' : 'price',
    '88a312b0-bc45-4c03-848b-ea6abde92ad2' : 'currency',
    '9f21c7da-7df8-43f7-8203-bc809aeb9c38' : 'tax_group',
    'e79289cf-4105-411d-bfb4-85bea29c667a' : 'fulfillment_token_id',
    '2d5d803f-066b-4427-81a4-244707ee194a' : 'publisher_website',
    '224481fa-2ce0-4194-8d98-162f516333e7' : 'fixed_document_price',
    '029437ac-03bb-469f-963a-782fadeda9fa' : 'content_source_id',
}


def patch(value, keep_ids=False):
    """Recursively make the keys in dicts in txtr-reaktor results descriptive.

    Txtr-reaktor results have some very strange keys in its dicts, its a pain
    to work with it, eg. in templates.

    The attributes in txtr-reaktor results are basically keys in dicts, its
    just a different way to access the values. This works via __getattr__.
    So this function works on the keys in the dicts as well on the attributes.

    If passed bool 'keep_ids' is False (default), remove the old non-descriptive
    keys.  Else the dicts will hold the value twice: once with the old key and
    once with the new key.
    """
    if isinstance(value, types.DictType):
        for dkey, dval in value.items():
            nkey, nval = ID_TO_NAME.get(dkey), patch(dval, keep_ids)
            if nkey:
                value[nkey] = nval
                if keep_ids:
                    value[dkey] = nval
                else:
                    del value[dkey]
            else:
                value[dkey] = nval
        return value

    if isinstance(value, types.ListType):
        return [patch(lvalue, keep_ids) for lvalue in value]

    return value

