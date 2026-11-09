# validation/ - does the vector space recover known biology, and what in it is new?

Written by `tahoemap validate` (tahoemap/validate.py). `cos` = signed cosine of two genes' unit vectors
(embed/gene_unit.npy). Every number is over the genes in the vector space (embed/included_cols.npy). Gene cols are the
row order of atlas/effects/genes.csv; symbols can repeat, so join on col. Read report.md first. Nothing is left out of
a list for a flag: an item with a reason for doubt keeps its ranked place and carries ⚠ with the reason in plain words.

## control_sets.csv - one row per tested gene set
| column | meaning |
|---|---|
| `source` | control (tahoemap/data/control_sets.json), hallmark, reactome (reference/gene_sets.parquet, >= 5 genes in the space), synthetic (only with truth=) |
| `set`, `label`, `note` | set name, short name, curator's note |
| `n_listed`, `n_found`, `n_in_space` | genes listed by the source, found among Tahoe genes, in the vector space (all metrics use these) |
| `mean_cos`, `median_cos`, `frac_pos` | over within-set pairs |
| `auroc_cos`, `auroc_abs` | AUROC of within-set pairs vs 20,000 random pairs of genes in the space, on cos / on abs(cos) (P(set pair > random pair), ties 1/2) |
| `p_random_sets_cos`, `p_random_sets_abs` | share of 200 random gene sets of the same size with an AUROC at least as high ((1 + count) / 201; control, Hallmark, synthetic only) |
| `mean_cos_half1`, `mean_cos_half2` | mean within-set cos in the spaces fitted on each half of the compounds |
| `top_module`, `top_module_share` | the module (nodal map) holding most of the set's genes, and the share of the set's genes in it |
| `top_module_genome_share` | that module's share of all genes in the space (chance level of top_module_share) |
| `top_module_arm_share` | share of the set's genes in that module on its majority arm |
| `best_dd_up`, `best_dd_down` | the 5 drug-doses with the highest / lowest mean pooled z (DD_z) over the set's genes, every drug-dose in its ranked place ('drug dose uM (mean z)'). One with an artifact flag (unreliable plate only, position not correctable, wells disagree, toxic, ...) reads 'drug dose uM (mean z, ⚠ its flags)'; for a cell-cycle shift with the share of the set's mean change the shift would explain ('cell-cycle shift, explains ~N% of this change': the tables stage's rule on the members' mean lfc and mean cell-cycle slopes; a shift that does not explain the change is named without ⚠). When the 5 strongest hold drug-doses with an alert, the 5 strongest without one follow in their ranked place too |
| `best_dd_up_n_alert`, `best_dd_down_n_alert` | how many drug-doses of each list carry an alert |

## opposite_pairs.csv - programmes expected to move in opposite directions
| column | meaning |
|---|---|
| `source`, `a`, `b`, `note` | the pair (control_sets.json 'opposite_pairs'; synthetic: planted arms) |
| `n_a`, `n_b`, `n_shared_dropped` | genes in the space per set (genes in both sets are dropped) |
| `mean_cross_cos`, `median_cross_cos` | over all cross pairs (a gene of a, a gene of b); expect < 0 |
| `frac_cross_neg` | share of cross pairs with cos < 0 |
| `auroc_anti` | P(cross pair cos < random pair cos) |
| `mean_cross_cos_half1`, `mean_cross_cos_half2` | the same in the two half spaces |
| `within_cos_a`, `within_cos_b` | mean within-set cos of each set |
| `share_same_module` | share of cross pairs in the same module of the nodal map (module 0 = unassigned never counts) |
| `random_same_module` | the same for two random genes (sum of squared module shares) |
| `share_opposite_arms_in_same_module` | among cross pairs in one module, the share on opposite arms |
| `nodal_centroid_dist`, `signed_centroid_dist` | distance between the two sets' centroids on the nodal map (x, y) / signed map (xs, ys), divided by the map's spread sqrt(var x + var y) |
| `reading` | the plain-language reading |

## module_enrichment.csv - modules and arms vs gene sets
Every module ('all'), its + arm and its - arm were tested against every set with >= 5 genes in the space
(hypergeometric upper tail, universe = genes in the space, Benjamini-Hochberg over all tests); rows with overlap >= 2
and p <= 0.05 (or q < 0.05) are kept.
| column | meaning |
|---|---|
| `module`, `arm`, `n_unit` | the module, the unit tested (all / + / -) and its genes |
| `source`, `set`, `set_label`, `n_set` | the set and its genes in the space |
| `overlap`, `expected`, `fold` | genes in both; expected by chance; overlap / expected |
| `p`, `q` | hypergeometric p, BH q over all tests |
| `genes` | overlapping genes (strongest on the module axis first, <= 25) |

## module_labels.csv - one row per module
| column | meaning |
|---|---|
| `module`, `n_genes`, `n_plus`, `n_minus` | the module and its arms |
| `label` | best set with q < 0.05 and >= 3 genes shared (smallest p among sets of <= 300 genes in the space, else any), short name; else 'genes: ...' (top genes of the + arm, then the - arm) |
| `label_source`, `label_set`, `label_arm` | where it came from (control / hallmark / reactome / top genes), the set, the unit (all / + / -) |
| `label_overlap`, `label_n_set`, `label_p`, `label_q` | its test |
| `plus_label`, `plus_set`, `plus_q`, `minus_label`, `minus_set`, `minus_q` | the best set of each arm alone |
| `top_plus`, `top_minus` | top genes of each arm (graph/modules.parquet; cut at 8 with the cap rule; a gene in the vector space only through drug-doses that carry an alert reads 'SYMBOL ⚠') |

## drug_moa.csv - mechanism classes (moa_fine) with >= 2 drugs
| column | meaning |
|---|---|
| `moa_fine`, `n_drugs`, `drugs` | the class and its drugs (the first 12; ⚠ = the drug's vector is of a dose with an artifact flag, embed/drugs.parquet alert; it is tested like the others) |
| `n_drugs_flagged_dose`, `n_drugs_no_trustworthy_dose` | the class's drugs marked ⚠; those of them with no trustworthy dose (every dose flagged unreliable plate only, position not correctable or wells disagree) |
| `n_pairs`, `mean_cos_within` | drug pairs within the class (salt forms of one compound not paired), their mean drug-vector cos |
| `mean_cos_to_other_classes` | mean cos of class members to drugs of other known classes |
| `auroc_within_vs_other` | AUROC of within-class pairs vs (member, other-class drug) pairs |

## novel_edges.csv - candidate new gene-gene relations (relations novel_candidate, one row per pair)
| column | meaning |
|---|---|
| `col_a`, `symbol_a`, `name_a`, `module_a`, `arm_a` | gene a (col_a < col_b), its HGNC name, module and arm |
| `col_b`, `symbol_b`, `name_b`, `module_b`, `arm_b` | gene b |
| `same_module` | both in the same module |
| `cos`, `cos_half1`, `cos_half2`, `evidence`, `fdr` | from relations (full space, the two compound halves, sign-concordance FDR) |
| `same_chrom`, `distance_bp` | genomic position (locus and read-through pairs are excluded) |
| `alert` | '' or '⚠ ' + the reasons to doubt the pair in plain words (relations' alert: e.g. a gene that is in the vector space only through drug-doses that carry an alert); such pairs are listed like the others |

## novel_members.csv - guilt by association
A module arm enriched (q < 0.01) for a set of <= 300 genes in the space with >= 3 of them on the arm; a gene of the arm
that the set does not list (by col or by symbol) is kept when its mean cos to the listed members is >= 0.5. Each
gene keeps its 5 most significant sets; genes are ranked by the mean cos for their most significant set.
| column | meaning |
|---|---|
| `col`, `symbol`, `name` | the candidate gene |
| `module`, `arm` | its module arm, which is enriched (q < 0.01) for the set |
| `source`, `set`, `set_label`, `set_q` | the set, and the arm's enrichment q |
| `n_annotated_in_arm`, `n_arm` | the set's genes on the arm; genes on the arm |
| `mean_cos`, `max_cos` | the candidate's cos to the arm's listed members (mean >= 0.5 kept) |
| `mean_cos_half1`, `mean_cos_half2` | the mean in the two half spaces |
| `n_reference_sets` | Hallmark / Reactome sets that already list the gene (0 = no pathway annotation at all) |
| `alert` | '' or '⚠ ' + why to doubt the gene's place: it is in the vector space only through drug-doses that carry an alert (embed/genes.parquet evidence_flagged_only); such genes are listed like the others |

## metrics.json
The headline numbers of report.md.
