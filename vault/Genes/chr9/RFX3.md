---
symbol: "RFX3"
type: "gene"
col: 1278
ensembl_id: "ENSG00000080298"
name: "regulatory factor X3"
location: "9p24.2"
module: 30
arm: "-"
pooled_cpm: 125.04
n_lines_expressing: 48
n_dd_up: 10
n_dd_down: 16
n_dd_up_clean: 10
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# RFX3

*regulatory factor X3* — 9p24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.49× (z +7.7, q 7e-12, up in 41 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.575× (z -7.2, q 3e-10, down in 34 of 45 measured lines) ⚠ toxic. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.616× (z -6.6, q 1e-08, down in 36 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASXL2]] (+0.58, fdr 1e-05), [[BAZ2B]] (+0.58, fdr 1e-05), [[PTPRK]] (+0.57, fdr 3e-05); moves opposite to [[RNF216P1]] (-0.66, fdr 1e-05), [[SUGT1P4-STRA6LP]] (-0.64, fdr 1e-05), [[TBCE]] (-0.63, fdr 1e-05).
> It sits in the **-** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ITPR2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1278.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.49×** | +7.7 | 7e-12 | 41/46 (A-172, SW1417, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.47×** | +7.3 | 6e-11 | 27/46 (SK-MEL-2, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +6.2 | 1e-07 | 29/47 (MIA PaCa-2, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +5.8 | 8e-07 | 35/46 (MIA PaCa-2, J82, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.69×** | +3.7 | 0.018 | 29/46 (AsPC-1, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.35×** | +3.7 | 0.018 | 25/46 (A-172, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.33×** | +3.7 | 0.018 | 23/46 (RKO, A549, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.062 | 26/48 (MIA PaCa-2, SW1417, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[AZD-8055 (drug)]] 0.5 µM |  | **1.40×** | +3.2 | 0.091 | 25/46 (J82, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | **1.56×** | +3.2 | 0.091 | 25/47 (A-427, HS-578T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.26× | +3.1 | 0.11 | 22/45 (SW48, HEC-1-A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1278.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.575×** | -7.2 | 3e-10 | 34/45 (LOX-IMVI, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.616×** | -6.6 | 1e-08 | 36/46 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.625×** | -6.4 | 3e-08 | 38/46 (KATO III, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.640×** | -5.6 | 3e-06 | 32/43 (KATO III, LoVo, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.493×** | -5.0 | 6e-05 | 34/47 (A-427, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.659×** | -4.9 | 1e-04 | 29/47 (SK-MEL-2, LoVo, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.784×** | -4.7 | 2e-04 | 34/47 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.542×** | -4.3 | 0.001 | 32/43 (A-427, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.734×** | -4.0 | 0.003 | 23/42 (NCI-H23, KATO III, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.666×** | -3.8 | 0.007 | 28/46 (SW480, SW48, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.770×** | -3.5 | 0.020 | 23/46 (LOX-IMVI, A-427, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.766×** | -3.5 | 0.023 | 23/46 (SW480, NCI-H460, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.774×** | -3.5 | 0.023 | 26/46 (SW480, LoVo, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.783×** | -3.3 | 0.036 | 24/46 (CHP-212, SW480, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.843× | -3.3 | 0.041 | 17/46 (PANC-1, A-427, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.772×** | -3.0 | 0.084 | 16/46 (AN3 CA, SK-MEL-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1278. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 264 | 1 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.239× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.314× (z -12.5) |
| [[KATO III (line)]] | alt | 216 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.194× (z -18.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 192 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.338× (z -13.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.452× (z -9.7) |
| [[HT-29 (line)]] | alt | 160 | 0 | 3 (3 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.108× (z -11.6) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 128 | 0 | 3 (3 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.177× (z -10.2) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 179 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +14.1) | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -18.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 134 | 0 | 3 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.239× (z -10.3) |
| [[SW480 (line)]] | alt | 181 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.318× (z -11.2) |
| [[A-172 (line)]] | wt | 71.3 | 2 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.70× (z +11.8) | — |
| [[HCT15 (line)]] | alt | 133 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.297× (z -10.5) |
| [[HepG2_C3A (line)]] | wt | 188 | 0 | 2 (1 ⚠) | — | [[Ponatinib (drug)]] 5 µM 0.300× (z -10.3) |
| [[LOX-IMVI (line)]] | wt | 284 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.293× (z -11.9) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 60.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +12.5) | — |
| [[Panc 03.27 (line)]] | alt | 153 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0996× (z -12.0) ⚠ toxic |
| [[A498 (line)]] | wt | 61.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +13.7) | — |
| [[AN3 CA (line)]] | alt | 215 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -11.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 65.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +10.7) | — |
| [[CHP-212 (line)]] | wt | 164 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.152× (z -11.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 76.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +8.9) | — |
| [[HS-578T (line)]] | alt | 95.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +10.0) | — |
| [[NCI-H23 (line)]] | alt | 130 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -20.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 148 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +13.2) | — |
| [[RKO (line)]] | wt | 195 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +9.7) | — |
| [[SHP-77 (line)]] | alt | 142 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.338× (z -11.3) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 149 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.111× (z -14.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 92.7 | 1 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.19× (z +11.0) | — |
| [[A549 (line)]] | wt | 150 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.8 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 132 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 66.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 82.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 108 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 109 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 122 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 70.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.3 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 95.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 153 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1278), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*34 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASXL2]] | +0.58 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[BAZ2B]] | +0.58 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[PTPRK]] | +0.57 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[FBXL17]] | +0.57 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[SLIT2]] | +0.56 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[FOXP1]] | +0.56 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[ERCC6L2]] | +0.54 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[TCF12]] | +0.53 | +0.39 / +0.48 | both halves | 5e-05 |  |
| [[SATB2]] | +0.53 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[TBC1D5]] | +0.52 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[CCDC90B-AS1]] | +0.51 | +0.58 / +0.31 | both halves | 2e-04 |  |
| [[CDKN2B-AS1]] | +0.51 | +0.47 / +0.39 | both halves | 6e-05 |  |

## Genes that move opposite

*66 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF216P1]] | -0.66 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[SUGT1P4-STRA6LP]] | -0.64 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[TBCE]] | -0.63 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[MKRN2]] | -0.62 | -0.66 / -0.48 | both halves | 2e-05 |  |
| [[STRA6LP]] | -0.61 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[OSBPL7]] | -0.59 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[SNTA1]] | -0.58 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[E4F1]] | -0.57 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[CDK5RAP1]] | -0.57 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[TRIM35]] | -0.57 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[IMPDH1]] | -0.56 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[MOCS1]] | -0.55 | -0.52 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITPR2]] | B | ITPR2 activity raises RFX3's level | lines that do not express ITPR2 (5) vs lines expressing it (45) | 1.86× lower at baseline in the lines without ITPR2 | 0.006 | ⚠ within organs, on part of the lines; also absent: ITPR2-AS1, ENSG00000286162, SPATA17; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers RFX3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **-** arm (projection on the module's main direction -0.594). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (0.4, -4.0); signed map (15.3, -11.9). **Vector** length 127, 41.8% of its response variance represented; |z| ≥ 3 in 1,075 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.1 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.1 | +7.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.9 | +0.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.7 | +2.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.3 | +1.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | +3.8 | +1.5 |
|  | [[Methylthiouracil (drug)]] 0.05 µM |  | +2.4 | +1.9 |
|  | [[Perindopril (erbumine) (drug)]] 0.05 µM |  | +2.3 | +2.8 |
|  | [[Lactate (calcium) (drug)]] 0.05 µM |  | +2.3 | +2.2 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.7 | -1.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.0 | -7.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.8 | +0.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.0 | -6.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | +1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.0 | -4.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.8 | -3.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.4 | -2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.4 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | regulatory factor X3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p24.2 — chr9:3,218,297-3,526,004 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Regulatory factor X family |
| Reactome | 4 pathways, smallest: Assembly of the 9+2 motile cilia; Transcriptional regulation of multiciliogenesis; Cilium Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [P48380](https://www.uniprot.org/uniprotkb/P48380) (Transcription factor RFX3):

> Transcription factor required for ciliogenesis and islet cell differentiation during endocrine pancreas development. Essential for the differentiation of nodal monocilia and left-right asymmetry specification during embryogenesis. Required for the biogenesis of motile cilia by governing growth and beating efficiency of motile cells. Also required for ciliated ependymal cell differentiation. Regulates the expression of genes involved in ciliary assembly (DYNC2LI1, FOXJ1 and BBS4) and genes …

**Summary**, from NCBI Gene [5991](https://www.ncbi.nlm.nih.gov/gene/5991):

> This gene is a member of the regulatory factor X gene family, which encodes transcription factors that contain a highly-conserved winged helix DNA binding domain. The protein encoded by this gene is structurally related to regulatory factors X1, X2, X4, and X5. It is a transcriptional activator that can bind DNA as a monomer or as a heterodimer with other RFX family members. Multiple transcript variants encoding different isoforms have been described for this gene. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:9984](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9984) · Entrez [5991](https://www.ncbi.nlm.nih.gov/gene/5991) · UniProt [P48380](https://www.uniprot.org/uniprotkb/P48380) · Ensembl [ENSG00000080298](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000080298)

## Data

Gene col 1278: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1278); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1278, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1278]; `tensor/DDL_lfc|DDL_z.npy` [1278]; `embed/gene_vectors.npy` [1278]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1278 or target_col == 1278). Every well: [[RFX3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RFX3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
