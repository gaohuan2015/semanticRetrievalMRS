def select_top_k_and_to_results_dict(scored_dict, merged_field_name='merged_field',
                                     score_field_name='score', item_field_name='element',
                                     top_k=5, filter_value=None, result_field='sp_doc', result_scored_field='scored_results'):

    results_dict = {result_field: dict(), result_scored_field: dict()}
    for key, value in scored_dict.items():
        fitems_dict = value[merged_field_name]
        scored_element_list = []
        for item in fitems_dict.values():
            score = item[score_field_name]
            element = item[item_field_name]
            scored_element_list.append((score, element))  # score is index 0.

        results_dict[result_scored_field][key] = scored_element_list
        sorted_e_list = sorted(scored_element_list, key=lambda x: x[0], reverse=True)

        results_dict[result_field][key] = []
        if filter_value is None:
            results_dict[result_field][key] = [e for s, e in sorted_e_list[:top_k]]
        else:
            for s, e in sorted_e_list:
                if s >= filter_value:
                    results_dict[result_field][key].append(e)
                if len(results_dict[result_field][key]) == top_k:
                    break

    return results_dict


def field_name_convert(d_list, old_field_name, new_field_name):
    for item in d_list:
        assert old_field_name in item
        item[new_field_name] = item[old_field_name]
        del item[old_field_name]
    return d_list
