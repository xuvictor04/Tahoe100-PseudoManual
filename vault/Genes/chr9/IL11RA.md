---
symbol: "IL11RA"
type: "gene"
col: 5961
ensembl_id: "ENSG00000137070"
name: "interleukin 11 receptor subunit alpha"
location: "9p13.3"
module: 157
arm: "+"
pooled_cpm: 2.96
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 7
n_dd_up_clean: 15
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/157"]
generated_by: "tahoemap"
---

# IL11RA

*interleukin 11 receptor subunit alpha* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.55× (z +9.0, q 2e-16, up in 34 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 0.532× (z -6.1, q 7e-07, down in 20 of 42 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GALT]] (+0.61, fdr 7e-06, ⚠ same locus), [[BCAM]] (+0.61, fdr 9e-06), [[LMNTD2]] (+0.59, fdr 1e-05), [[HCN3]] (+0.58, fdr 1e-05); moves opposite to [[PRR14L]] (-0.55, fdr 2e-05), [[TMCC1]] (-0.52, fdr 4e-05), [[MIB1]] (-0.52, fdr 3e-05).
> It is in [[Module 157]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ID2-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5961.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.55×** | +9.0 | 2e-16 | 34/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.03×** | +6.8 | 3e-09 | 23/43 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.09×** | +6.5 | 2e-08 | 0/3 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.98×** | +6.3 | 5e-08 | 0/2 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.76×** | +5.4 | 9e-06 | 16/44 (PANC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.46×** | +5.1 | 4e-05 | 8/45 (A498, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.60×** | +4.5 | 6e-04 | 7/46 (HEC-1-A, SW480, …) | all doses, flat | cell-cycle shift (explains ~22% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.57×** | +4.3 | 0.001 | 9/45 (NCI-H23, KATO III, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | **1.53×** | +4.1 | 0.002 | 8/45 (C-33 A, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.53×** | +4.1 | 0.003 | 5/40 (A-427, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +4.0 | 0.003 | 11/46 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.34×** | +3.9 | 0.004 | 4/44 (NCI-H460, SHP-77, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +3.8 | 0.006 | 8/45 (RKO, A498, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.32×** | +3.7 | 0.009 | 9/34 (SW480, A549, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +3.6 | 0.011 | 7/48 (NCI-H23, HOP62, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.30×** | +3.4 | 0.024 | 6/43 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +3.2 | 0.038 | 7/28 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.91×** | +3.2 | 0.038 | 2/40 (NCI-H23, PANC-1) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +3.1 | 0.046 | 2/41 (BT-474, MIA PaCa-2) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +2.9 | 0.089 | 7/46 (SW1417, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5961.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.532×** | -6.1 | 7e-07 | 20/42 (HT-29, HEC-1-A, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.528×** | -5.8 | 2e-06 | 19/40 (PANC-1, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.603×** | -4.9 | 2e-04 | 19/44 (hTERT-HPNE, H4, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.713×** | -4.6 | 5e-04 | 16/45 (SHP-77, COLO 205, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.660×** | -4.0 | 0.007 | 8/44 (NCI-H460, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~19% here); position effect removed |
| [[Fingolimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.686×** | -3.6 | 0.025 | 10/39 (CFPAC-1, SK-MEL-2, …) | rises with dose |  |
| [[Atazanavir (sulfate) (drug)]] 5 µM |  | **0.705×** | -3.4 | 0.057 | 5/44 (NCI-H2030, H4, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.722× | -3.1 | 0.12 | 13/43 (SW480, HCT15, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5961. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 5.32 | 0 | 1 | — | [[Peretinoin (drug)]] 0.5 µM 0.0459× (z -8.7) |
| [[A-172 (line)]] | wt | 4.69 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.871 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.41 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.38 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5961), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GALT]] | +0.61 | +0.62 / +0.62 | both halves | 7e-06 | STRING 930; ⚠ same locus (1.1 kb, same strand: neighbours can correlate without regulation) |
| [[BCAM]] | +0.61 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[LMNTD2]] | +0.59 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[HCN3]] | +0.58 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[ZBED6]] | +0.58 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[PPM1M]] | +0.58 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[RMRP]] | +0.57 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[YY1AP1]] | +0.55 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[AJM1]] | +0.55 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[CFAP410]] | +0.55 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[CRTC2]] | +0.54 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[SLC9A3-AS1]] | +0.54 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[LRCH4]] | +0.54 | +0.47 / +0.50 | both halves | 2e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRR14L]] | -0.55 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[TMCC1]] | -0.52 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[MIB1]] | -0.52 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[CCT6A]] | -0.51 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[NLN]] | -0.51 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[DAP3]] | -0.50 | -0.56 / -0.32 | both halves | 2e-04 |  |
| [[METTL2B]] | -0.47 | -0.38 / -0.29 | both halves | 3e-04 |  |
| [[ZNF562]] | -0.47 | -0.43 / -0.38 | both halves | 7e-05 |  |
| [[DNTTIP2]] | -0.46 | -0.31 / -0.41 | both halves | 2e-04 |  |
| [[EIF3I]] | -0.46 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[SUPT3H]] | -0.46 | -0.48 / -0.40 | both halves | 4e-05 |  |
| [[KATNBL1]] | -0.46 | -0.40 / -0.42 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ID2-AS1]] | B | ID2-AS1 activity raises IL11RA's level | lines that do not express ID2-AS1 (8) vs lines expressing it (42) | 1.61× lower at baseline in the lines without ID2-AS1 | 0.044 | ⚠ within organs, on part of the lines; also absent: ID2, RDM1P5 |
| [[PSMB5]] | B | PSMB5 activity raises IL11RA's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 157]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.680). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-15.3, -23.8); signed map (-0.3, 5.6). **Vector** length 41.8, 4.35% of its response variance represented; |z| ≥ 3 in 1,069 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +6.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +3.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.5 | +1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +1.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +3.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +0.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.2 | +4.1 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -1.9 | -4.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -1.9 | -5.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -6.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -2.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.2 | -1.4 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -0.9 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | interleukin 11 receptor subunit alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:34,652,162-34,661,902 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Immunoglobulin like domain containing; Interleukin receptors |
| Reactome | 4 pathways, smallest: IL-6-type cytokine receptor ligand interactions; Interleukin-6 family signaling; Signaling by Interleukins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14626](https://www.uniprot.org/uniprotkb/Q14626) (Interleukin-11 receptor subunit alpha):

> Receptor for interleukin-11 (IL11). The receptor systems for IL6, LIF, OSM, CNTF, IL11 and CT1 can utilize IL6ST for initiating signal transmission. The IL11/IL11RA/IL6ST complex may be involved in the control of proliferation and/or differentiation of skeletogenic progenitor or other mesenchymal cells (Probable). Essential for the normal development of craniofacial bones and teeth. Restricts suture fusion and tooth number.; [Soluble interleukin-11 receptor subunit alpha]: Soluble form of IL11 …

**Summary**, from NCBI Gene [3590](https://www.ncbi.nlm.nih.gov/gene/3590):

> Interleukin 11 is a stromal cell-derived cytokine that belongs to a family of pleiotropic and redundant cytokines that use the gp130 transducing subunit in their high affinity receptors. This gene encodes the IL-11 receptor, which is a member of the hematopoietic cytokine receptor family. This particular receptor is very similar to ciliary neurotrophic factor, since both contain an extracellular region with a 2-domain structure composed of an immunoglobulin-like domain and a cytokine …

**Accessions** — [HGNC:5967](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5967) · Entrez [3590](https://www.ncbi.nlm.nih.gov/gene/3590) · UniProt [Q14626](https://www.uniprot.org/uniprotkb/Q14626) · Ensembl [ENSG00000137070](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137070)

## Data

Gene col 5961: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5961); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5961, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5961]; `tensor/DDL_lfc|DDL_z.npy` [5961]; `embed/gene_vectors.npy` [5961]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5961 or target_col == 5961). Every well: [[IL11RA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IL11RA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
