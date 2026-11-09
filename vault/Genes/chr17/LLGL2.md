---
symbol: "LLGL2"
type: "gene"
col: 1048
ensembl_id: "ENSG00000073350"
name: "LLGL scribble cell polarity complex component 2"
location: "17q25.1"
module: 3
arm: "+"
pooled_cpm: 67.56
n_lines_expressing: 38
n_dd_up: 14
n_dd_down: 8
n_dd_up_clean: 11
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 7
direction_downstream: 15
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# LLGL2

*LLGL scribble cell polarity complex component 2* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.25× (z +21.2, q 0e+00, up in 35 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.347× (z -9.9, q 2e-20, down in 29 of 37 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP1R13B]] (+0.68, fdr 7e-06), [[GNAI2]] (+0.63, fdr 2e-04), [[PIP5K1C]] (+0.63, fdr 3e-05); moves opposite to [[PRR3]] (-0.62, fdr 2e-04), [[MTHFSD]] (-0.61, fdr 4e-05), [[PIGW]] (-0.60, fdr 6e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[LMTK3]] → it (grade B ⚠); 15 go from it, the strongest it → [[LMTK3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠; shown: the 15 strongest. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1048.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.25×** | +21.2 | 0e+00 | 35/36 (PANC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.09×** | +20.3 | 0e+00 | 35/36 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.62×** | +17.3 | 0e+00 | 34/35 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +7.9 | 3e-13 | 17/36 (PANC-1, SK-MEL-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +7.5 | 7e-12 | 15/29 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.51×** | +7.4 | 2e-11 | 21/36 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.34×** | +5.2 | 2e-05 | 15/33 (C-33 A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.31×** | +4.9 | 7e-05 | 17/35 (SW480, SW1417, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.63×** | +4.6 | 3e-04 | 21/35 (NCI-H2347, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.62×** | +4.6 | 3e-04 | 19/37 (PANC-1, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.41×** | +4.4 | 6e-04 | 13/34 (SW1417, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.26×** | +4.2 | 0.001 | 16/35 (LoVo, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.26×** | +4.2 | 0.001 | 12/36 (SK-MEL-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.010 | 16/37 (NCI-H2347, HEC-1-A, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.1 | 0.067 | 13/35 (SHP-77, SW48, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1048.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.347×** | -9.9 | 2e-20 | 29/37 (LoVo, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.404×** | -8.5 | 5e-15 | 25/35 (HEC-1-A, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.905× | -6.3 | 6e-08 | 4/38 (NCI-H460, J82, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **0.784×** | -6.2 | 9e-08 | 23/36 (Panc 03.27, MIA PaCa-2, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.743×** | -5.3 | 1e-05 | 22/35 (KATO III, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.759×** | -5.0 | 7e-05 | 20/36 (A498, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.781×** | -4.3 | 0.002 | 20/36 (KATO III, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.803×** | -3.9 | 0.006 | 19/35 (AsPC-1, COLO 205, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.812×** | -3.7 | 0.011 | 17/35 (MIA PaCa-2, LoVo, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.865× | -3.7 | 0.012 | 14/36 (Panc 03.27, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1048. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 33.3 | 3 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 4.48× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -12.8) ⚠ cell-cycle shift, explains ~3% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.354× (z -11.0) |
| [[SW480 (line)]] | alt | 132 | 4 (1 ⚠) | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.82× (z +15.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.577× (z -11.5) ⚠ cell-cycle shift, explains ~3% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.240× (z -11.1) |
| [[HEC-1-A (line)]] | alt | 159 | 4 (1 ⚠) | 2 | [[Panobinostat (drug)]] 5 µM 2.71× (z +14.8) | [[TAK-901 (drug)]] 5 µM 0.252× (z -10.7) |
| [[Panc 03.27 (line)]] | alt | 138 | 3 | 2 | [[Panobinostat (drug)]] 5 µM 3.33× (z +15.8) | [[Selinexor (drug)]] 5 µM 0.503× (z -12.7) |
| [[A-427 (line)]] | wt | 46.6 | 3 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.81× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -11.4) ⚠ cell-cycle shift, explains ~14% of this change |
| [[C-33 A (line)]] | alt | 23.7 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.47× (z +9.2) | — |
| [[COLO 205 (line)]] | alt | 232 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.334× (z -9.6) |
| [[HepG2_C3A (line)]] | wt | 99.4 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.73× (z +10.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.343× (z -10.3) ⚠ toxic; cell-cycle shift, explains ~8% of this change |
| [[HT-29 (line)]] | alt | 94.0 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 3.27× (z +14.0) | [[TAK-901 (drug)]] 5 µM 0.191× (z -10.2) |
| [[KATO III (line)]] | alt | 406 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -14.0) ⚠ cell-cycle shift, explains ~3% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.365× (z -12.0) |
| [[LoVo (line)]] | wt | 117 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 2.73× (z +12.8) | [[TAK-901 (drug)]] 5 µM 0.153× (z -12.6) |
| [[SW1417 (line)]] | alt | 184 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.29× (z +11.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.606× (z -9.9) ⚠ cell-cycle shift, explains ~3% of this change |
| [[A498 (line)]] | wt | 23.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.89× (z +13.3) | — |
| [[A549 (line)]] | wt | 39.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.32× (z +13.9) | — |
| [[J82 (line)]] | alt | 17.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.71× (z +12.0) | — |
| [[NCI-H2347 (line)]] | alt | 79.8 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 2.61× (z +11.6) | [[Selinexor (drug)]] 5 µM 0.571× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 22.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.40× (z +14.5) | — |
| [[PANC-1 (line)]] | alt | 24.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.62× (z +16.0) | — |
| [[BT-474 (line)]] | alt | 115 | 0 | 2 | — | [[TAK-901 (drug)]] 5 µM 0.183× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 54.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.95× (z +13.2) ⚠ toxic; transcription drop | [[Selinexor (drug)]] 5 µM 0.458× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 24.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.91× (z +10.0) | — |
| [[RKO (line)]] | wt | 35.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.26× (z +11.4) | — |
| [[SK-MEL-2 (line)]] | alt | 22.5 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.65× (z +10.1) | — |
| [[SW 900 (line)]] | alt | 18.9 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.74× (z +10.9) | — |
| [[SW48 (line)]] | wt | 87.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.13× (z +10.1) | — |
| [[AsPC-1 (line)]] | alt | 104 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.397× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 55.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.46× (z +9.2) | — |
| [[LS 180 (line)]] | wt | 175 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.230× (z -10.5) |
| [[A-172 (line)]] | wt | 8.48 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.2 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 15.6 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 219 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.6 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 8.71 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.46 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.88 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 8.72 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 11.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 87.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.96 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.7 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 11.1 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1048), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R13B]] | +0.68 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[GNAI2]] | +0.63 | +0.47 / +0.31 | both halves | 2e-04 |  |
| [[PIP5K1C]] | +0.63 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[SREBF2]] | +0.62 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[CBFA2T2]] | +0.62 | +0.52 / +0.38 | both halves | 7e-05 |  |
| [[LMTK3]] | +0.61 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[PI4KAP1]] | +0.61 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[TAOK3]] | +0.61 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[PRKCI]] | +0.61 | +0.47 / +0.41 | both halves | 4e-05 | STRING 996 |
| [[TNK2]] | +0.61 | +0.30 / +0.55 | both halves | 2e-04 |  |
| [[CAMSAP3]] | +0.61 | +0.60 / +0.41 | both halves | 4e-05 |  |
| [[PI4KAP1-1]] | +0.60 | +0.59 / +0.40 | both halves | 4e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRR3]] | -0.62 | -0.41 / -0.30 | both halves | 2e-04 |  |
| [[MTHFSD]] | -0.61 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[PIGW]] | -0.60 | -0.40 / -0.38 | both halves | 6e-05 |  |
| [[MCTS1]] | -0.59 | -0.48 / -0.31 | both halves | 2e-04 |  |
| [[RBM12B]] | -0.59 | -0.46 / -0.38 | both halves | 6e-05 |  |
| [[KICS2]] | -0.59 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[PEF1]] | -0.58 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[RWDD2B]] | -0.58 | -0.36 / -0.21 | both halves | 7e-04 |  |
| [[ANGEL2]] | -0.58 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[GTF3C4]] | -0.57 | -0.41 / -0.38 | both halves | 6e-05 |  |
| [[PSME3IP1]] | -0.57 | -0.51 / -0.28 | both halves | 3e-04 |  |
| [[C8orf33]] | -0.57 | -0.48 / -0.20 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 4, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LMTK3]] | B | LMTK3 activity raises LLGL2's level | lines that do not express LMTK3 (15) vs lines expressing it (35) | 3.33× lower at baseline in the lines without LMTK3 | 0.007 | ⚠ within organs, on part of the lines; also absent: CRYBG2, CXADR, CCDC120; maybe low, not absent |
| [[ATAD3C]] | B | ATAD3C activity raises LLGL2's level | lines that do not express ATAD3C (17) vs lines expressing it (33) | 3.66× lower at baseline in the lines without ATAD3C | 0.035 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MYH14, SORL1 |
| [[F11R]] | B | F11R activity raises LLGL2's level | lines that do not express F11R (10) vs lines expressing it (40) | 2.81× lower at baseline in the lines without F11R | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000287306, LONRF3, TUBA4A |
| [[KIAA1522]] | B | KIAA1522 activity raises LLGL2's level | lines that do not express KIAA1522 (5) vs lines expressing it (45) | 3.65× lower at baseline in the lines without KIAA1522 | 0.087 | ⚠ across organs; also absent: ENSG00000257489, TRIB3, PBX4 |
| [[ENTPD2]] | C | ENTPD2 activity raises LLGL2's level | lines that do not express ENTPD2 (22) vs lines expressing it (28) | 4.83× lower at baseline in the lines without ENTPD2 | 0.005 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ESRP2; co-absent with the target |
| [[CAMSAP3]] | C | CAMSAP3 activity raises LLGL2's level | lines that do not express CAMSAP3 (16) vs lines expressing it (34) | 4.51× lower at baseline in the lines without CAMSAP3 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: CGN, FGFR4, UNC5A; maybe low, not absent; co-absent with the target |
| [[MLXIPL]] | C | MLXIPL activity raises LLGL2's level | lines that do not express MLXIPL (13) vs lines expressing it (37) | 4.06× lower at baseline in the lines without MLXIPL | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: GRTP1, PLS1, LAMP3; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 13, C 2. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LMTK3]] | B | LLGL2 activity raises LMTK3's level | lines that do not express LLGL2 (12) vs lines expressing it (38) | 2.91× lower at baseline in the lines without LLGL2 | 0.012 | ⚠ within organs, on part of the lines; also absent: GRTP1, FGFR4, LSR |
| [[ERH]] | B | LLGL2 activity raises ERH's level | lines that do not express LLGL2 (12) vs lines expressing it (38) | 1.44× lower at baseline in the lines without LLGL2 | 0.014 | ⚠ within organs, on part of the lines; also absent: GRTP1, FGFR4, LSR |
| [[RPS6KA1]] | B | LLGL2 activity raises RPS6KA1's level | lines that do not express LLGL2 (12) vs lines expressing it (38) | 2.10× lower at baseline in the lines without LLGL2 | 0.025 | ⚠ within organs, on part of the lines; also absent: GRTP1, FGFR4, LSR |
| [[PIGW]] | B | LLGL2 activity raises PIGW's level | lines that do not express LLGL2 (12) vs lines expressing it (38) | 1.37× lower at baseline in the lines without LLGL2 | 0.057 | ⚠ within organs, on part of the lines; also absent: GRTP1, FGFR4, LSR |
| [[F11R]] | B | LLGL2 activity raises F11R's level | lines that do not express LLGL2 (12) vs lines expressing it (38) | 3.49× lower at baseline in the lines without LLGL2 | 0.057 | ⚠ within organs, on part of the lines; also absent: GRTP1, FGFR4, LSR |
| [[C9orf64]] | B | LLGL2 activity raises C9orf64's level | lines that do not express LLGL2 (12) vs lines expressing it (38) | 1.93× lower at baseline in the lines without LLGL2 | 0.057 | ⚠ within organs, on part of the lines; also absent: GRTP1, FGFR4, LSR |
| [[CHKA]] | B | LLGL2 activity raises CHKA's level | lines that do not express LLGL2 (12) vs lines expressing it (38) | 1.65× lower at baseline in the lines without LLGL2 | 0.062 | ⚠ within organs, on part of the lines; also absent: GRTP1, FGFR4, LSR |
| [[EPM2A]] | B | LLGL2 activity weakens EPM2A's drug response | lines that do not express LLGL2 (12) vs lines expressing it (34) | the lines without LLGL2 respond 1.26× as strongly (z diff -0.47); strongest at Auranofin 5 µM: 4.15x vs 1.81x (z diff -3.1) | 0.082 | ⚠ within organs, on part of the lines; also absent: GRTP1, FGFR4, LSR; target measured in part of the lines; artifact flags |
| [[PPP1R13B]] | B | LLGL2 activity raises PPP1R13B's level | lines that do not express LLGL2 (12) vs lines expressing it (38) | 1.53× lower at baseline in the lines without LLGL2 | 0.087 | ⚠ within organs, on part of the lines; also absent: GRTP1, FGFR4, LSR |
| [[BAIAP2L1]] | B | LLGL2 activity raises BAIAP2L1's level | lines that do not express LLGL2 (12) vs lines expressing it (38) | 2.60× lower at baseline in the lines without LLGL2 | 0.090 | ⚠ within organs, on part of the lines; also absent: GRTP1, FGFR4, LSR |
| [[CYSTM1]] | B | LLGL2 activity raises CYSTM1's level | lines that do not express LLGL2 (12) vs lines expressing it (38) | 1.94× lower at baseline in the lines without LLGL2 | 0.092 | ⚠ within organs, on part of the lines; also absent: GRTP1, FGFR4, LSR |
| [[SMG6]] | B | LLGL2 activity lowers SMG6's level | lines that do not express LLGL2 (12) vs lines expressing it (38) | 1.26× higher at baseline in the lines without LLGL2 | 0.094 | ⚠ within organs, on part of the lines; also absent: GRTP1, FGFR4, LSR |

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.522). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (3.8, -0.7); signed map (-27.2, 18.8). **Vector** length 107, 28.6% of its response variance represented; |z| ≥ 3 in 850 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +7.3 | +21.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.8 | +20.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.9 | +17.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +7.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +4.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.0 | +4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +7.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.6 | +2.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.3 | +4.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.3 | +2.8 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -6.5 | -9.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.1 | -6.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.8 | -5.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.3 | -8.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.0 | -5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -3.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.2 | -0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | LLGL scribble cell polarity complex component 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:75,525,080-75,575,209 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HGL, Hugl-2 |
| Gene groups (HGNC) | WD repeat domain containing; Scribble complex; LLGL scribble cell polarity complex component family |
| Hallmark sets | ESTROGEN_RESPONSE_LATE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P1M3](https://www.uniprot.org/uniprotkb/Q6P1M3) (LLGL scribble cell polarity complex component 2):

> Part of a complex with GPSM2/LGN, PRKCI/aPKC and PARD6B/Par-6, which may ensure the correct organization and orientation of bipolar spindles for normal cell division. This complex plays roles in the initial phase of the establishment of epithelial cell polarity.

**Summary**, from NCBI Gene [3993](https://www.ncbi.nlm.nih.gov/gene/3993):

> The lethal (2) giant larvae protein of Drosophila plays a role in asymmetric cell division, epithelial cell polarity, and cell migration. This human gene encodes a protein similar to lethal (2) giant larvae of Drosophila. In fly, the protein's ability to localize cell fate determinants is regulated by the atypical protein kinase C (aPKC). In human, this protein interacts with aPKC-containing complexes and is cortically localized in mitotic cells. Alternative splicing results in multiple …

**Accessions** — [HGNC:6629](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6629) · Entrez [3993](https://www.ncbi.nlm.nih.gov/gene/3993) · UniProt [Q6P1M3](https://www.uniprot.org/uniprotkb/Q6P1M3) · Ensembl [ENSG00000073350](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000073350)

## Data

Gene col 1048: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1048); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1048, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1048]; `tensor/DDL_lfc|DDL_z.npy` [1048]; `embed/gene_vectors.npy` [1048]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1048 or target_col == 1048). Every well: [[LLGL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LLGL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
