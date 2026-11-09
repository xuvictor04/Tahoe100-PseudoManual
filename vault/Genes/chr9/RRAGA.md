---
symbol: "RRAGA"
type: "gene"
col: 7927
ensembl_id: "ENSG00000155876"
name: "Ras related GTP binding A"
location: "9p22.1"
module: 16
arm: "+"
pooled_cpm: 15.12
n_lines_expressing: 49
n_dd_up: 19
n_dd_down: 17
n_dd_up_clean: 12
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# RRAGA

*Ras related GTP binding A* — 9p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.82× (z +6.7, q 1e-08, up in 31 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.485× (z -8.2, q 1e-13, down in 36 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MGAT2]] (+0.64, fdr 1e-05), [[C6orf120]] (+0.62, fdr 7e-06), [[BBS10]] (+0.60, fdr 1e-05); moves opposite to [[LUC7L3]] (-0.54, fdr 2e-05), [[PNN]] (-0.52, fdr 1e-04), [[LRRC75A]] (-0.49, fdr 4e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7927.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.82×** | +6.7 | 1e-08 | 31/46 (SW 900, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~8% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +6.4 | 4e-08 | 24/44 (KATO III, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +5.3 | 3e-05 | 15/38 (NCI-H1573, KATO III, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.54×** | +4.9 | 2e-04 | 25/47 (PANC-1, HS-578T, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.10×** | +4.4 | 0.001 | 22/46 (A549, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.48×** | +4.4 | 0.001 | 21/47 (Panc 03.27, KATO III, …) | all doses, flat | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.31×** | +4.2 | 0.002 | 18/47 (Hs 766T, KATO III, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +4.0 | 0.004 | 16/44 (HOP62, KATO III, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.38×** | +3.6 | 0.020 | 15/46 (SNU-423, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mifepristone (drug)]] 0.5 µM |  | **1.37×** | +3.5 | 0.027 | 18/46 (HS-578T, SW480, …) | two highest doses | position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.36×** | +3.5 | 0.027 | 10/47 (HOP62, LOX-IMVI, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.47×** | +3.4 | 0.028 | 15/42 (MIA PaCa-2, SW 900, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.35×** | +3.3 | 0.038 | 11/47 (KATO III, SNU-423, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **1.34×** | +3.2 | 0.047 | 13/43 (H4, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.34×** | +3.2 | 0.059 | 17/43 (KATO III, SW480, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.070 | 14/47 (A-427, HEC-1-A, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.0 | 0.076 | 11/47 (LOX-IMVI, CFPAC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7927.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.485×** | -8.2 | 1e-13 | 36/46 (A498, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.530×** | -7.2 | 2e-10 | 31/44 (H4, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.550×** | -6.8 | 2e-09 | 27/45 (NCI-H460, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.593×** | -5.6 | 3e-06 | 24/45 (A498, SW480, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.644×** | -5.0 | 6e-05 | 26/45 (C-33 A, C32, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.652×** | -4.9 | 1e-04 | 23/45 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.663×** | -4.7 | 2e-04 | 24/47 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.675×** | -4.3 | 0.001 | 23/40 (A498, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.520×** | -3.9 | 0.006 | 18/37 (J82, SW480, …) | all doses, flat | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.624×** | -3.8 | 0.007 | 18/47 (A498, HS-578T, …) | all doses, flat | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.739×** | -3.4 | 0.027 | 20/47 (A498, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Gemcitabine (drug)]] 0.5 µM |  | **0.742×** | -3.4 | 0.027 | 13/47 (SW480, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.744×** | -3.4 | 0.030 | 16/45 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.812×** | -3.4 | 0.030 | 19/45 (J82, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.821×** | -3.2 | 0.051 | 14/47 (CHP-212, NCI-H2347, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.822×** | -3.2 | 0.051 | 17/47 (A498, NCI-H1573, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 0.5 µM |  | **0.677×** | -3.2 | 0.051 | 12/44 (Hs 766T, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7927. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 46.3 | 0 | 3 | — | [[Ixazomib citrate (drug)]] 5 µM 0.192× (z -13.7) |
| [[J82 (line)]] | alt | 28.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -9.9) |
| [[NCI-H460 (line)]] | wt | 13.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.238× (z -10.4) |
| [[A549 (line)]] | wt | 26.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 10.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.113× (z -10.0) ⚠ cell-cycle shift, explains ~12% of this change |
| [[A-172 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.49 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.64 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.18 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.65 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.07 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 14.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7927), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MGAT2]] | +0.64 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[C6orf120]] | +0.62 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[BBS10]] | +0.60 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[EID1]] | +0.58 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[TTPAL]] | +0.56 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[MTFR1L]] | +0.56 | +0.60 / +0.46 | both halves | 2e-05 |  |
| [[FAHD1]] | +0.56 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[RBM22]] | +0.56 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[THNSL1]] | +0.55 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[ZNF217]] | +0.55 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[TTC30A]] | +0.54 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[LDHA]] | +0.54 | +0.47 / +0.62 | both halves | 2e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LUC7L3]] | -0.54 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[PNN]] | -0.52 | -0.34 / -0.57 | both halves | 1e-04 |  |
| [[LRRC75A]] | -0.49 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[ZDHHC18]] | -0.48 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[PNISR]] | -0.48 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[PABPN1]] | -0.48 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[RENO1]] | -0.48 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[EGFL8]] | -0.47 | -0.53 / -0.37 | both halves | 8e-05 |  |
| [[CARM1]] | -0.47 | -0.46 / -0.39 | both halves | 6e-05 |  |
| [[MAP2K2]] | -0.47 | -0.46 / -0.40 | both halves | 4e-05 |  |
| [[UBE2K]] | -0.47 | -0.42 / -0.46 | both halves | 4e-05 | pathway: Protein ubiquitination |
| [[ZC3H3]] | -0.47 | -0.42 / -0.47 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RRAGA's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PLIN2]] | B | PLIN2 activity raises RRAGA's level | lines that do not express PLIN2 (17) vs lines expressing it (33) | 1.40× lower at baseline in the lines without PLIN2 | 0.086 | ⚠ within organs, on part of the lines; also absent: AXL, UBE2Q2P13, SLC2A3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.393). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-36.8, 15.9); signed map (-1.8, -29.5). **Vector** length 92.8, 20.4% of its response variance represented; |z| ≥ 3 in 886 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +6.9 | +6.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.6 | +4.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.1 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.9 | +4.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.2 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +3.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.6 | +3.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.1 | +3.4 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -5.3 | -8.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.7 | -5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.5 | -5.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.4 | -4.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -3.9 | -3.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.4 | -3.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.2 | -2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.9 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | Ras related GTP binding A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p22.1 — chr9:19,049,427-19,051,025 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RAGA, FIP-1 |
| Gene groups (HGNC) | Ras related GTP binding proteins |
| Reactome | 17 pathways, smallest: mTORC1-mediated signalling; Energy dependent regulation of mTOR by LKB1-AMPK; MTOR signalling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7L523](https://www.uniprot.org/uniprotkb/Q7L523) (Ras-related GTP-binding protein A):

> Guanine nucleotide-binding protein that plays a crucial role in the cellular response to amino acid availability through regulation of the mTORC1 signaling cascade. Forms heterodimeric Rag complexes with RagC/RRAGC or RagD/RRAGD and cycles between an inactive GDP-bound and an active GTP-bound form: RagA/RRAGA is in its active form when GTP-bound RagA/RRAGA forms a complex with GDP-bound RagC/RRAGC (or RagD/RRAGD) and in an inactive form when GDP-bound RagA/RRAGA heterodimerizes with GTP-bound …

**Summary**, from NCBI Gene [10670](https://www.ncbi.nlm.nih.gov/gene/10670):

> Enables several functions, including GTP binding activity; protein dimerization activity; and ubiquitin protein ligase binding activity. Involved in several processes, including cellular response to amino acid starvation; positive regulation of TORC1 signaling; and tumor necrosis factor-mediated signaling pathway. Located in GATOR1 complex; lysosome; and nucleoplasm. Part of FNIP-folliculin RagC/D GAP. Is active in lysosomal membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16963](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16963) · Entrez [10670](https://www.ncbi.nlm.nih.gov/gene/10670) · UniProt [Q7L523](https://www.uniprot.org/uniprotkb/Q7L523) · Ensembl [ENSG00000155876](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155876)

## Data

Gene col 7927: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7927); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7927, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7927]; `tensor/DDL_lfc|DDL_z.npy` [7927]; `embed/gene_vectors.npy` [7927]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7927 or target_col == 7927). Every well: [[RRAGA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RRAGA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
