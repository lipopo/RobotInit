# -*- coding: utf8 -*-


def translate_config(key, config_dict_or_list_or_other, remote = {}):
    if isinstance(config_dict_or_list_or_other, basestring):
        remote.update({key: config_dict_or_list_or_other})

    if isinstance(config_dict_or_list_or_other, dict):
        for k in config_dict_or_list_or_other:
            remote.update(
                translate_config( key+"_" + k if key is not None and key != "main" else k, config_dict_or_list_or_other[k])
            )

    if isinstance(config_dict_or_list_or_other, list):
        for v_idx, v in enumerate(config_dict_or_list_or_other):
            remote.update(
                translate_config(key + "_" + str(v_idx), v)
            )

    return remote