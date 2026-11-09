---
symbol: "CEP76"
type: "gene"
col: 2159
ensembl_id: "ENSG00000101624"
name: "centrosomal protein 76"
location: "18p11.21"
module: 40
arm: "+"
pooled_cpm: 23.6
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 8
n_dd_up_clean: 7
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# CEP76

*centrosomal protein 76* — 18p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.73× (z +16.2, q 0e+00, up in 34 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Belumosudil (drug)]] 5 µM: 0.707× (z -7.0, q 1e-09, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC138]] (+0.56, fdr 1e-05), [[RBM4B]] (+0.55, fdr 2e-05), [[NANS]] (+0.48, fdr 3e-05); moves opposite to [[PACRG]] (-0.43, fdr 2e-04), [[HEXB]] (-0.42, fdr 1e-04), [[PTP4A1]] (-0.41, fdr 2e-04).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2159.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.73×** | +16.2 | 0e+00 | 34/47 (LOX-IMVI, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.41×** | +7.2 | 2e-10 | 24/47 (MIA PaCa-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.39×** | +7.0 | 6e-10 | 21/47 (SK-MEL-2, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.37×** | +6.6 | 5e-09 | 23/48 (LOX-IMVI, NCI-H1573, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +6.1 | 9e-08 | 23/47 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +6.1 | 9e-08 | 22/44 (NCI-H2030, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.25×** | +4.5 | 7e-04 | 16/48 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.23×** | +4.3 | 0.001 | 11/47 (RKO, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.23×** | +4.3 | 0.001 | 13/48 (SK-MEL-2, NCI-H1573, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +4.2 | 0.001 | 15/47 (LOX-IMVI, HOP62, …) | rises with dose |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 1.13× | +3.6 | 0.016 | 10/48 (HOP62, A-427, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.25×** | +3.4 | 0.034 | 7/48 (HOP62, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 1.19× | +3.3 | 0.041 | 12/46 (Panc 03.27, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.17× | +3.3 | 0.045 | 7/47 (PANC-1, KATO III, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 1.17× | +3.2 | 0.045 | 9/47 (LS 180, LoVo, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.34×** | +3.2 | 0.047 | 3/46 (LOX-IMVI, HOP62, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2159.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belumosudil (drug)]] 5 µM |  | **0.707×** | -7.0 | 1e-09 | 28/47 (MIA PaCa-2, J82, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.799×** | -4.6 | 0.001 | 16/35 (HCT15, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **0.803×** | -4.5 | 0.002 | 18/47 (SNU-423, C-33 A, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.864× | -4.4 | 0.002 | 16/48 (LoVo, C-33 A, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.678×** | -4.3 | 0.002 | 12/48 (SW480, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.678×** | -4.3 | 0.002 | 16/46 (HEC-1-A, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.868× | -4.2 | 0.002 | 16/48 (HT-29, KATO III, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.811×** | -4.1 | 0.003 | 12/46 (BT-474, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[venetoclax (drug)]] 5 µM |  | **0.713×** | -3.7 | 0.012 | 11/44 (SNU-1, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.716×** | -3.7 | 0.013 | 14/45 (AN3 CA, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.844× | -3.6 | 0.017 | 13/47 (SW480, A549, …) | two highest doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.889× | -3.5 | 0.021 | 16/48 (HepG2/C3A, HOP62, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.846× | -3.4 | 0.028 | 10/47 (HOP62, A-427, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.852× | -3.4 | 0.028 | 13/47 (HT-29, Hs 766T, …) | rises with dose |  |
| [[EX229 (drug)]] 0.05 µM |  | 0.845× | -3.4 | 0.028 | 10/48 (BT-474, NCI-H1573, …) | all doses, flat |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.905× | -3.0 | 0.091 | 11/48 (LoVo, BT-474, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2159. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 48.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.169× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 11.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.148× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 16.6 | 0 | 1 | — | [[Amsacrine (drug)]] 5 µM 0.204× (z -8.9) |
| [[HCT15 (line)]] | alt | 32.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -9.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 27.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.307× (z -9.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 42.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -8.7) ⚠ cell-cycle shift, explains ~54% of this change |
| [[HOP62 (line)]] | alt | 32.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +11.0) | — |
| [[KATO III (line)]] | alt | 22.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.136× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 31.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +11.4) | — |
| [[LOX-IMVI (line)]] | wt | 15.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +13.5) | — |
| [[LS 180 (line)]] | wt | 41.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -9.7) ⚠ cell-cycle shift, explains ~54% of this change |
| [[MIA PaCa-2 (line)]] | alt | 26.1 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.35× (z +9.4) | — |
| [[NCI-H1573 (line)]] | alt | 16.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +11.9) | — |
| [[NCI-H460 (line)]] | wt | 16.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +10.4) | — |
| [[RKO (line)]] | wt | 22.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +8.6) | — |
| [[RPMI-7951 (line)]] | alt | 16.9 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.177× (z -8.6) |
| [[SW480 (line)]] | alt | 30.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +10.3) | — |
| [[A-172 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.53 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2159), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC138]] | +0.56 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[RBM4B]] | +0.55 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[NANS]] | +0.48 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[DSN1]] | +0.48 | +0.29 / +0.59 | both halves | 3e-04 | pathway: Mitotic Prometaphase |
| [[CHST12]] | +0.48 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[DRG1]] | +0.47 | +0.52 / +0.38 | both halves | 7e-05 |  |
| [[ZNF10]] | +0.46 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[CENPC]] | +0.46 | +0.30 / +0.53 | both halves | 2e-04 | pathway: Mitotic Prometaphase |
| [[MIS18A]] | +0.46 | +0.50 / +0.38 | both halves | 7e-05 |  |
| [[CEP192]] | +0.46 | +0.32 / +0.48 | both halves | 2e-04 | pathway: AURKA Activation by TPX2; STRING 575 |
| [[HS6ST1]] | +0.46 | +0.48 / +0.39 | both halves | 5e-05 |  |
| [[TFB2M]] | +0.45 | +0.27 / +0.50 | both halves | 3e-04 | pathway: Organelle biogenesis and maintenance |

## Genes that move opposite

*14 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PACRG]] | -0.43 | -0.32 / -0.33 | both halves | 2e-04 |  |
| [[HEXB]] | -0.42 | -0.33 / -0.37 | both halves | 1e-04 |  |
| [[PTP4A1]] | -0.41 | -0.30 / -0.42 | both halves | 2e-04 |  |
| [[HIF1A]] | -0.40 | -0.32 / -0.40 | both halves | 2e-04 |  |
| [[SLC36A1]] | -0.40 | -0.25 / -0.30 | both halves | 4e-04 |  |
| [[SRFBP1]] | -0.39 | -0.21 / -0.35 | both halves | 7e-04 |  |
| [[VPS13C]] | -0.38 | -0.21 / -0.43 | both halves | 7e-04 |  |
| [[ARL8B]] | -0.38 | -0.27 / -0.43 | both halves | 3e-04 |  |
| [[LINC01505]] | -0.38 | -0.20 / -0.34 | both halves | 7e-04 |  |
| [[IGF2R]] | -0.38 | -0.26 / -0.36 | both halves | 3e-04 |  |
| [[LIPA]] | -0.38 | -0.29 / -0.39 | both halves | 3e-04 |  |
| [[CTTN]] | -0.37 | -0.43 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers CEP76's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers CEP76's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.262). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-27.3, -54.1); signed map (-47.0, -30.8). **Vector** length 84.9, 16.2% of its response variance represented; |z| ≥ 3 in 883 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.5 | +6.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +16.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +3.8 | +4.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.1 | +6.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.9 | +3.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.8 | +3.2 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.7 | +2.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | +1.8 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +1.6 | +2.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.6 | -3.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | -2.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.9 | -3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.7 | -7.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -3.6 | +2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -4.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.3 | -4.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.1 | -4.3 |
|  | [[EX229 (drug)]] 5 µM |  | -3.0 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | centrosomal protein 76 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.21 — chr18:12,661,833-12,702,777 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HsT1705, FLJ12542; previously C18orf9 |
| Reactome | 17 pathways, smallest: Loss of Nlp from mitotic centrosomes; Loss of proteins required for interphase microtubule organization from the centrosome; AURKA Activation by TPX2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TAP6](https://www.uniprot.org/uniprotkb/Q8TAP6) (Centrosomal protein of 76 kDa):

> Centrosomal protein involved in regulation of centriole duplication. Required to limit centriole duplication to once per cell cycle by preventing centriole reduplication.

**Summary**, from NCBI Gene [79959](https://www.ncbi.nlm.nih.gov/gene/79959):

> This gene encodes a centrosomal protein which regulates centriole amplification by limiting centriole duplication to once per cell cycle. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2012]

**Accessions** — [HGNC:25727](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25727) · Entrez [79959](https://www.ncbi.nlm.nih.gov/gene/79959) · UniProt [Q8TAP6](https://www.uniprot.org/uniprotkb/Q8TAP6) · Ensembl [ENSG00000101624](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101624)

## Data

Gene col 2159: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2159); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2159, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2159]; `tensor/DDL_lfc|DDL_z.npy` [2159]; `embed/gene_vectors.npy` [2159]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2159 or target_col == 2159). Every well: [[CEP76 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CEP76.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
