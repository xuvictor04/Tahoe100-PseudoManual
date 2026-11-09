# direction/ - probable direction between genes

Directed edges SOURCE -> TARGET, each from a statistical test (p, BH q < 0.10), with an evidence grade and its alerts. Nothing that passes is dropped because of doubt: it keeps its place with its alerts (the `alerts` text starts with ⚠) and a lower grade. A pair without such a test result is not an edge. Method: tahoemap/direction.py (module docstring); a user-facing explanation: docs/direction.md.

## What direction means here - and what it does not

- The source is what the test conditions on: a recorded mutation of the source gene (fixed before the experiment, so not a consequence of the target), its absence from some lines, its natural level, or compounds that target its protein. The target is what differs with it: its level, its drug response, or the cells' growth under a drug.
- It is not proof of direct regulation: A -> B -> C looks like A -> C; another alteration carried by the same lines can be the cause (see the co-occurrence alerts); 'not recorded' is not proof of wild type.
- One time point (~24 h): fast and slow effects are mixed; compensation and feedback are not seen.
- Drugs act on proteins, not on mRNA; a compound can act on other proteins than its listed target.
- Level edges come from natural differences between lines; tissue and other differences can mimic them, and a stronger correlation one way can reflect how precisely each gene's level is measured.

## How to read a grade

- **A**: a recorded genotype, >= 5 lines on each side (within organs: lines sharing an organ with the other side), q < 0.05, compared within organs, no co-occurrence alert (another gene's altered lines on the same side, or on the other side); for a response, not resting on the global-sensitivity correction and not mostly from drug-doses without any correction.
- **B**: other genotype edges (with alerts, or 3-4 lines) that are not tissue-confounded; expression-null with >= 5 lines lacking the gene (not tissue-confounded); drug_target.
- **C**: a glimpse: level and level_sensitivity; expression-null with 3-4 lines, tissue-confounded, co-absent, or resting on the correction; a genotype edge that is tissue-confounded or significant only within its own group (q_group < 0.10, table-wide q >= 0.10).

## How to read a sign

- The sign is the effect of the SOURCE's activity. For a level or the cells: +1 raises it, -1 lowers it.
- For a drug response (genotype_response, null_response, level): +1 strengthens the target's response, -1 weakens it, in the target's own direction at each drug-dose - where the target falls under the drugs, 'strengthens' means it falls further (the source deepens the fall). Read which from all of top_drugdoses and from rise_share; a target that rises at some drug-doses and falls at others is alerted, and the sign then says how strongly it responds, not whether the source induces or represses it.

## This run

- 102,590 edges; groups tested: 64 genotype groups, 60 pseudo-groups, 5,791 expression-null line sets (5,939 genes; 293 sets / 322 genes could not be compared within organs)
- ⚠ expression-null: for 97 genes (88 line sets) absent from lines concentrated in organs, their partners' baseline and response were not tested (absence and tissue cannot be told apart there; groups.parquet note says so for each); their effect on cell numbers was. The other sets without a within-organ comparison were compared across organs as a separate BH family
- by kind and grade: genotype_response A17/B13/C106; genotype_baseline A8/B2/C9; genotype_sensitivity A0/B0/C1; null_response A0/B2026/C150; null_baseline A0/B38332/C42174; null_sensitivity A0/B4194/C1811; drug_target A0/B11874/C0; level A0/B0/C1359; level_sensitivity A0/B0/C514
- global-sensitivity correction of the (gene, drug-dose) responses: 165,529 against the drug-dose's other responsive genes, 856 line-wide only, 45 without; the lines' overall responsiveness was used (668 drug-doses of 307 compounds; SD 0.24 across lines, split-half r 0.99)
- expected false edges (negative controls; in brackets the 95% upper bound): genotype_response 12.8 (up to 20.74) of 43; genotype_response_within_group_only 4.27 (up to 9.76) of 93; genotype_baseline 0.0 (up to 3.2) of 10; genotype_baseline_within_group_only 13.87 (up to 22.05) of 9; genotype_sensitivity 0.0 (up to 3.2) of 0; genotype_sensitivity_within_group_only 1.07 (up to 5.06) of 1; level 102 (up to 120.24) of 1359; level_sensitivity 0 (up to 3.0) of 0; level_sensitivity_within_drugdose_only 37 (up to 48.68) of 514. expected_false: the controls' estimate of the false edges among the written ones; expected_false_upper: its 95% upper bound (Poisson: the controls are a small sample - 0 edges in 60 pseudo-groups still allows about 3 per 60 groups, and the level controls are one permutation each). The estimate can be low when real groups overlap other recorded or unrecorded alterations, tissue programmes or each other, which random groups do not.
- pseudo-groups, edges per group vs real groups: response 0.2 vs 0.6719; baseline 0.0 vs 0.1719; sensitivity 0.0 vs 0.0
- ⚠ genotype_baseline_within_group_only: the controls expect 13.87 false edges among the 9 written
- ⚠ genotype_sensitivity_within_group_only: the controls expect 1.07 false edges among the 1 written

## edges.parquet

- `source`: the upstream gene: the genotype's gene, the gene that is absent, whose level varies, or that the compounds target
- `source_col`: its gene col (genes.csv; -1 = a drug target that is not a measured gene)
- `target`: the gene that changes, or 'cells under DRUG DOSE' (the cells' growth: sensitivity kinds)
- `target_col`: the target gene's col (-1 for cells)
- `target_dd`: the drug-dose row for a cells target (-1)
- `target_type`: gene or cells
- `kind`: the evidence: genotype_response / genotype_baseline / genotype_sensitivity (recorded mutation), null_response / null_baseline / null_sensitivity (the gene is not expressed in some lines), drug_target (compounds that target it), level / level_sensitivity (its natural level)
- `grade`: A (recorded genotype, >= 5 lines each side, q < 0.05, compared within organs, no co-occurrence or anti-occurrence alert, and for a response not resting on the global-sensitivity correction), B, C (a glimpse; also a tissue-confounded genotype edge) - see 'How to read a grade'
- `sign`: +1: the source's activity raises the target's level or the cell numbers, or strengthens the target's drug response in its own direction (for a target that falls under the drugs: a deeper fall); -1: lowers it / weakens it; 0: not inferred (mechanism unknown) - see 'How to read a sign'
- `reading`: the edge in words
- `group`: the comparison ('TP53 loss of function (10 lines) vs not recorded (8)')
- `mechanism`: loss of function / gain of function / altered (any record) / not expressed / level / inhibitor ...
- `n_altered`: lines on the altered (or lacking) side with a value for the target (-1: not applicable)
- `n_intact`: lines on the other side with a value
- `n_lines`: lines in a level correlation
- `contrast`: the tested effect: response kinds mean corrected response (z units) intact - altered; baseline log2 level intact - altered; sensitivity log2 relative cell number intact - altered; level r; drug_target the share of the compounds that move the target
- `D_raw`: response kinds: the same contrast without the global-sensitivity correction
- `retained_fraction`: response kinds: the altered lines' mean raw response / the intact lines' (1 = unchanged, 0 = lost, < 0 = reversed)
- `raw_share`: response kinds: the evidence in the edge's direction without the global-sensitivity correction / with it (sum of squared per-drug-dose scores); below 0.25 the edge rests on the correction (alerted, not grade A)
- `rise_share`: response kinds and level: the share of the target's response from drug-doses where it rises (the rest: where it falls) - of the evidence carrying the difference (genotype / null response), or of its own response over its significant drug-doses, weighted by |pooled z| (level). Between 0.25 and 0.75 it is alerted: the sign then says how strongly it responds, not whether the source induces or represses it
- `baseline_log2_diff`: the target's baseline log2 level intact - altered (for response edges: context)
- `r`: level kinds: correlation of the lineage-adjusted level with the response / cell number
- `r_reverse`: level: the same with the roles of the two genes swapped
- `direction_clear`: level: |r| > |r_reverse| and p_direction < 0.05; False when the reverse is not clearly weaker or could not be tested
- `p_direction`: level: one-sided p that |r| - |r_reverse| is no larger than two equally strong directions give once the forward has passed the same cut (the edge was selected because |r| is large, which inflates it; the largest p over the common strength); 1 when the reverse is at least as strong
- `n_compounds`: drug_target: compounds of the class
- `n_supporting`: drug_target: of them, those that move the target that way
- `background_rate`: drug_target: share of all compounds that move the target that way
- `compounds`: drug_target: every compound of the class, '; '-joined; one molecule counts once (salt forms, letter case and salt words merged; its names ' / '-joined) ('' for other kinds)
- `compounds_supporting`: drug_target: those of them that move the target that way, '; '-joined
- `drug_effect`: drug_target: what the compounds do to the target's level, 'raises' or 'lowers' (sign is relative to the source's activity: an inhibitor that raises the target gives sign -1)
- `T`: the tested statistic: permutation-standardised (and divided by the group's inflation) for the group kinds; t = r sqrt(dof / (1 - r^2)) for the level kinds; empty for drug_target
- `p`: group kinds: from the pooled permutation null with a fitted generalized-Pareto tail (no floor), never below the target's own permutation p where its own shuffles disagree with the pool, nor below 1 / its number of label arrangements; two-sided, except the response kinds (one-sided upper tail of the omnibus S). Level kinds: two-sided, from the t distribution (calibrated by a Freedman-Lane null). drug_target: one-sided hypergeometric
- `q`: BH q over the kind's whole family: every genotype group of the kind; every expression-null test of the kind (within-organ and across-organ comparisons as two families); every level pair; every (gene, drug-dose) level_sensitivity test; every drug_target test
- `q_group`: genotype kinds: BH q within the edge's own group (its tests of the kind); level_sensitivity: within the drug-dose (the genes tested for it). These edges are written when q_group < 0.10 (significant in their own family); grade A / B also need q < 0.10 over the whole table; with q >= 0.10 the edge is grade C (a lead) and its alert says so, with the expected number of such false edges
- `alerts`: every doubt, in plain words: '' or '⚠ ' + the reasons, '; '-joined
- `n_alerts`: number of alerts (reasons)
- `top_drugdoses`: response: the drug-doses carrying the difference, each as 'fold in the altered lines vs fold in the other lines (z diff: corrected contrast)', the strongest first within the target's main direction (rise_share), then the other direction; when mixed, the strongest of each; drug_target: each supporting compound's strongest drug-dose

## groups.parquet

- `group_id`: kind:gene:mechanism
- `kind`: genotype, null (expression-null line set) or pseudo (control)
- `gene`: the gene
- `gene_col`: its col (-1 = not measured)
- `mechanism`: as in edges
- `description`: the comparison
- `n_altered`: lines altered / lacking the gene
- `n_intact`: lines compared
- `altered_lines`: their names
- `intact_lines`: their names
- `organs_altered`: organs (count)
- `organs_intact`: organs (count)
- `stratified`: permuted within organs
- `n_arrangements`: distinct arrangements of the labels the permutations draw from (within organs when stratified)
- `n_altered_shared_organs`: altered lines in organs that also hold lines of the other side (within organs only those carry the comparison; grade A needs >= 5)
- `n_intact_shared_organs`: the same for the other side
- `organ_enrichment_p`: compared across organs: Monte Carlo p that the two sides' organs differ (chi-square over label permutations; empty when compared within organs)
- `tissue_confounded`: compared across organs and the sides' organs differ (organ_enrichment_p < 0.05)
- `cooccurs_with`: other genes' altered sets overlapping this one (Jaccard >= 0.5; blocks grade A)
- `anti_occurs_with`: genes whose altered lines sit on the other side of the comparison (phi <= -0.5): a confounder with the opposite sign (an alert; blocks grade A)
- `variants`: variant types of the altered lines' records
- `x_not_expressed_in_altered`: altered lines where the gene itself is not expressed (-1: not measured)
- `x_baseline_log2_diff`: the gene's own level, intact - altered (log2)
- `genes_same_lines`: null: every gene absent from exactly these lines
- `max_phi_to_real`: pseudo: largest |phi| to a recorded group (drawn below 0.3)
- `max_phi_to_null_sets`: pseudo: largest |phi| to an expression-null line set with >= 5 lines each side (drawn below 0.5)
- `alerts`: the group's alerts
- `inflation`: per test, the genomic-control factor its statistics were divided by (>= 1; how much wider than the permutation null the bulk of all targets' statistics spread for this grouping)
- `note`: null: how its partners' baseline and response were compared (across organs: a separate BH family), or why they were not tested (lines concentrated in organs)
- `n_edges_response`: edges written (pseudo: tests at or below the real family's BH cut, counted, not written)
- `n_edges_baseline`: same
- `n_edges_sensitivity`: same

## controls.json, info.json

- controls.json: positive controls (TP53 -> p53 targets with sign and rank; TP53 -> cells under DNA-damaging drugs; KEAP1 -> NRF2 targets when KEAP1 is recorded in enough lines); negative controls (pseudo-groups counted at the real family's BH cut: the false edges a group without any effect adds); permuted-level controls for the level kinds; the expected false edges per kind.
- info.json: counts per kind and grade, groups and tests, the BH cuts, the fitted null tails, the level kinds' calibration, settings, peak memory, minutes.
