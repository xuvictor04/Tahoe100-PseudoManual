---
symbol: "RAB3A"
type: "gene"
col: 2636
ensembl_id: "ENSG00000105649"
name: "RAB3A, member RAS oncogene family"
location: "19p13.11"
module: 124
arm: "-"
pooled_cpm: 3.06
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 17
n_dd_up_clean: 10
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 3
direction_downstream: 4
tags: ["gene", "module/124"]
generated_by: "tahoemap"
---

# RAB3A

*RAB3A, member RAS oncogene family* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 9.56× (z +18.5, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.405× (z -7.5, q 2e-11, down in 28 of 44 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AHDC1]] (+0.74, fdr 7e-06), [[SNAPC3]] (+0.74, fdr 7e-06), [[CDON]] (+0.73, fdr 1e-05); moves opposite to [[ENOX2]] (-0.80, fdr 7e-06), [[ITPA]] (-0.77, fdr 7e-06), [[AVEN]] (-0.75, fdr 1e-05).
> It sits in the **-** arm of [[Module 124]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SNHG18]] → it (grade B ⚠); 4 go from it, the strongest it → [[SIRT5]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2636.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **9.56×** | +18.5 | 0e+00 | 46/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **7.93×** | +17.0 | 0e+00 | 44/44 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **6.24×** | +15.0 | 0e+00 | 44/44 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.95×** | +8.9 | 1e-16 | 41/46 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.99×** | +8.0 | 2e-13 | 16/34 (LoVo, HS-578T, …) | top dose only | cell-cycle shift (explains ~14% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.61×** | +5.5 | 4e-06 | 20/45 (NCI-H460, RKO, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **3.20×** | +5.0 | 5e-05 | 13/41 (HEC-1-A, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.81×** | +4.9 | 8e-05 | 13/32 (SW1417, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.61×** | +3.9 | 0.007 | 5/18 (NCI-H2347, HCT15, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.40×** | +3.8 | 0.010 | 8/40 (LS 180, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.010 | 9/45 (NCI-H2347, MIA PaCa-2, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +3.2 | 0.064 | 8/48 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2636.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.405×** | -7.5 | 2e-11 | 28/44 (Hs 766T, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.405×** | -7.5 | 2e-11 | 29/46 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.443×** | -6.7 | 3e-09 | 21/42 (HS-578T, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.472×** | -6.0 | 3e-07 | 21/40 (BT-474, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.531×** | -5.2 | 2e-05 | 19/36 (A-172, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.557×** | -4.9 | 1e-04 | 17/32 (NCI-H2347, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.606×** | -4.1 | 0.003 | 17/44 (NCI-H2030, RPMI-7951, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.611×** | -4.1 | 0.003 | 16/45 (HOP62, A498, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.636×** | -3.7 | 0.011 | 17/45 (LoVo, A549, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.643×** | -3.7 | 0.014 | 14/46 (H4, AN3 CA, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.645×** | -3.6 | 0.014 | 11/44 (A549, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.663×** | -3.4 | 0.028 | 12/44 (HS-578T, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.749×** | -3.4 | 0.028 | 12/45 (Hs 766T, RKO, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.681×** | -3.2 | 0.057 | 11/42 (HOP62, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.688×** | -3.1 | 0.070 | 11/43 (SK-MEL-2, LS 180, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.690×** | -3.1 | 0.073 | 15/41 (NCI-H2030, RPMI-7951, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.694×** | -3.0 | 0.080 | 9/45 (SK-MEL-2, A549, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2636. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 1.52 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 24.3× (z +10.1) | — |
| [[HS-578T (line)]] | alt | 6.61 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.10× (z +9.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0403× (z -11.1) |
| [[A498 (line)]] | wt | 3.65 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +8.6) | — |
| [[C32 (line)]] | wt | 9.85 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.0808× (z -10.4) ⚠ toxic; unreliable plate only |
| [[HOP62 (line)]] | alt | 3.12 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0459× (z -9.8) |
| [[LoVo (line)]] | wt | 2.04 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +10.3) | — |
| [[NCI-H2347 (line)]] | alt | 3.29 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0682× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 1.55 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.60× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 10.0 | 0 | 1 | — | [[Cepharanthine (drug)]] 0.5 µM 0.0896× (z -8.9) |
| [[A-172 (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.986 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.992 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.48 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.82 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.88 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.897 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.89 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.899 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.82 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.82 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2636), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHDC1]] | +0.74 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[SNAPC3]] | +0.74 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[CDON]] | +0.73 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[DNAAF3]] | +0.73 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[ABCB9]] | +0.72 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[YIF1B]] | +0.71 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[SEPTIN6]] | +0.71 | +0.58 / +0.63 | both halves | 8e-06 |  |
| [[ALAD]] | +0.71 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[OSBPL7]] | +0.71 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[ARL6]] | +0.70 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[PFKFB4]] | +0.70 | +0.68 / +0.49 | both halves | 1e-05 |  |
| [[NPRL2]] | +0.70 | +0.56 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENOX2]] | -0.80 | -0.73 / -0.61 | both halves | 7e-06 |  |
| [[ITPA]] | -0.77 | -0.63 / -0.58 | both halves | 7e-06 |  |
| [[AVEN]] | -0.75 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[DPH5-DT]] | -0.73 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[GABPB1]] | -0.73 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[NIPAL2]] | -0.69 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[POU6F1]] | -0.69 | -0.56 / -0.36 | both halves | 9e-05 |  |
| [[EPM2A]] | -0.69 | -0.62 / -0.26 | both halves | 4e-04 |  |
| [[ST7L]] | -0.69 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[DGKH]] | -0.68 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[WARS2-AS1]] | -0.68 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[ATE1]] | -0.67 | -0.62 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNHG18]] | B | SNHG18 activity raises RAB3A's level | lines that do not express SNHG18 (29) vs lines expressing it (21) | 1.40× lower at baseline in the lines without SNHG18 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SEMA5A, AMPH, LINC02930 |
| [[RAB20]] | B | RAB20 activity raises RAB3A's level | lines that do not express RAB20 (8) vs lines expressing it (42) | 1.62× lower at baseline in the lines without RAB20 | 0.080 | ⚠ within organs, on part of the lines; also absent: RPS6KA2, PRDX2, YPEL3; maybe low, not absent |
| [[TMEM144]] | C | TMEM144 activity lowers RAB3A's level | lines that do not express TMEM144 (3) vs lines expressing it (47) | 1.89× higher at baseline in the lines without TMEM144 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: WNK4, RNF103-CHMP3, RBMS2; maybe low, not absent; its own permutation p |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SIRT5]] | C | RAB3A's natural level weakens SIRT5's drug response | RAB3A's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.74, reverse -0.07; direction clear | 0.003 | ⚠ tissue can mimic it; precision caveat |
| [[RARA]] | C | RAB3A's natural level weakens RARA's drug response | RAB3A's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.62, reverse +0.02; direction not clear | 0.089 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[HMGA1P4]] | C | RAB3A's natural level weakens HMGA1P4's drug response | RAB3A's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.64, reverse +0.12; direction not clear | 0.0995 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| cells under [[Docetaxel (drug)]] 5 µM | C | RAB3A's natural level raises the cells' numbers under Docetaxel 5 µM (protects the cells) | RAB3A's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.68 | 0.285 over the table, 0.050 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 124]]; 39 genes; this gene is in the **-** arm (projection on the module's main direction -0.865). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (6.5, -6.8); signed map (-31.1, 20.7). **Vector** length 86.2, 16.9% of its response variance represented; |z| ≥ 3 in 1,147 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +5.7 | +17.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.3 | +18.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.0 | +15.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.2 | +8.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.4 | +3.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +5.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +5.5 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +1.5 | +2.4 |
|  | [[Fumaric acid (drug)]] 5 µM |  | +1.5 | +1.4 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.7 | -2.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | -2.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.4 | -3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.9 | -6.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.4 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -4.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -2.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.6 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | RAB3A, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:18,196,784-18,204,042 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Reactome | 19 pathways, smallest: Acetylcholine Neurotransmitter Release Cycle; GABA synthesis, release, reuptake and degradation; Norepinephrine Neurotransmitter Release Cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [P20336](https://www.uniprot.org/uniprotkb/P20336) (Ras-related protein Rab-3A):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different sets of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion. RAB3A plays a central role in regulated exocytosis and secretion. Controls the recruitment, tethering and docking of …

**Summary**, from NCBI Gene [5864](https://www.ncbi.nlm.nih.gov/gene/5864):

> Enables G protein activity and myosin V binding activity. Involved in several processes, including acrosomal vesicle exocytosis; plasma membrane repair; and regulation of plasma membrane repair. Located in perinuclear region of cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:9777](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9777) · Entrez [5864](https://www.ncbi.nlm.nih.gov/gene/5864) · UniProt [P20336](https://www.uniprot.org/uniprotkb/P20336) · Ensembl [ENSG00000105649](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105649)

## Data

Gene col 2636: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2636); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2636, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2636]; `tensor/DDL_lfc|DDL_z.npy` [2636]; `embed/gene_vectors.npy` [2636]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2636 or target_col == 2636). Every well: [[RAB3A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB3A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
