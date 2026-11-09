---
symbol: "DHX30"
type: "gene"
col: 5278
ensembl_id: "ENSG00000132153"
name: "DExH-box helicase 30"
location: "3p21.31"
module: 1
arm: "+"
pooled_cpm: 35.66
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 10
n_dd_up_clean: 13
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 5
direction_downstream: 2
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# DHX30

*DExH-box helicase 30* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.51× (z +14.8, q 0e+00, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.674× (z -10.0, q 7e-21, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CIAPIN1]] (+0.74, fdr 7e-06), [[MRPL38]] (+0.71, fdr 7e-06), [[ZNF282]] (+0.70, fdr 7e-06); moves opposite to [[SPAG9]] (-0.57, fdr 1e-05), [[APLP2]] (-0.56, fdr 2e-05), [[PNPLA8]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[MVB12B]] → it (grade B ⚠); 2 go from it, the strongest it → cells under [[Clofarabine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5278.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.51×** | +14.8 | 0e+00 | 35/48 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.42×** | +9.0 | 9e-17 | 35/47 (HOP62, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +8.3 | 1e-14 | 29/48 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.41×** | +8.2 | 5e-14 | 31/48 (LOX-IMVI, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +7.9 | 3e-13 | 30/46 (RKO, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.33×** | +6.9 | 6e-10 | 30/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.64×** | +6.6 | 4e-09 | 24/48 (HEC-1-A, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.62×** | +6.4 | 1e-08 | 22/48 (MIA PaCa-2, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.28×** | +6.3 | 2e-08 | 22/48 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.25×** | +5.6 | 1e-06 | 21/48 (KATO III, SW480, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.23×** | +5.2 | 1e-05 | 20/48 (HOP62, KATO III, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.5 | 4e-04 | 13/47 (NCI-H2030, HepG2/C3A, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.20× | +4.4 | 4e-04 | 15/48 (HCT15, SNU-423, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.40×** | +4.4 | 4e-04 | 16/48 (MIA PaCa-2, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.39×** | +4.4 | 4e-04 | 16/43 (LOX-IMVI, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.38×** | +4.3 | 6e-04 | 9/46 (NCI-H460, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.17× | +3.7 | 0.007 | 16/47 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.30×** | +3.5 | 0.014 | 8/47 (AsPC-1, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.16× | +3.4 | 0.016 | 10/47 (LoVo, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.016 | 6/48 (Hs 766T, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.14× | +3.2 | 0.029 | 11/48 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5278.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.674×** | -10.0 | 7e-21 | 33/48 (SHP-77, NCI-H2347, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.830×** | -6.7 | 5e-09 | 22/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.784×** | -6.2 | 1e-07 | 23/48 (NCI-H460, SW1417, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.788×** | -6.1 | 2e-07 | 21/48 (NCI-H460, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.804×** | -5.6 | 3e-06 | 20/48 (NCI-H460, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.806×** | -5.5 | 4e-06 | 20/48 (NCI-H460, SW1417, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.807×** | -5.4 | 4e-06 | 20/48 (Hs 766T, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.803×** | -5.4 | 6e-06 | 20/47 (NCI-H23, A-172, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.821×** | -4.8 | 9e-05 | 19/48 (C-33 A, SW48, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.714×** | -4.5 | 4e-04 | 18/46 (LOX-IMVI, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.904× | -3.7 | 0.013 | 16/48 (RKO, SK-MEL-2, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.885× | -3.1 | 0.085 | 7/47 (A-172, SW480, …) | two highest doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5278. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 26.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.387× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 56.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change |
| [[A-427 (line)]] | wt | 54.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -20.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 23.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +10.0) | — |
| [[AN3 CA (line)]] | alt | 62.2 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0692× (z -13.1) |
| [[C-33 A (line)]] | alt | 68.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 53.6 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.125× (z -9.8) |
| [[HOP62 (line)]] | alt | 29.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +10.2) | — |
| [[Hs 766T (line)]] | wt | 23.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.125× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 29.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +9.0) | — |
| [[NCI-H23 (line)]] | alt | 45.4 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -8.9) ⚠ cell-cycle shift, explains ~12% of this change |
| [[NCI-H2347 (line)]] | alt | 40.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.473× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 38.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.506× (z -8.8) |
| [[NCI-H661 (line)]] | alt | 45.3 | 0 | 1 | — | [[Estrone sulfate (potassium) (drug)]] 0.5 µM 0.0744× (z -9.7) |
| [[SHP-77 (line)]] | alt | 76.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.423× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 54.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.217× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 45.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.544× (z -8.7) |
| [[A-172 (line)]] | wt | 38.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 39.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 63.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 56.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5278), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIAPIN1]] | +0.74 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[MRPL38]] | +0.71 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[ZNF282]] | +0.70 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[MTPAP]] | +0.68 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[ZNF746]] | +0.67 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[NUDT19]] | +0.67 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[QRSL1]] | +0.66 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[LTV1]] | +0.66 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[NOL9]] | +0.65 | +0.71 / +0.57 | both halves | 1e-05 |  |
| [[SETD4]] | +0.65 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[INTS14]] | +0.64 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[YTHDC2]] | +0.64 | +0.62 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPAG9]] | -0.57 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[APLP2]] | -0.56 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[PNPLA8]] | -0.56 | -0.49 / -0.60 | both halves | 2e-05 |  |
| [[TMBIM6]] | -0.54 | -0.42 / -0.61 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MVB12B]] | B | MVB12B activity raises DHX30's level | lines that do not express MVB12B (6) vs lines expressing it (44) | 1.70× lower at baseline in the lines without MVB12B | 0.093 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: PDE5A, TSEN2, TYMSOS; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises DHX30's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises DHX30's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CSRP2]] | B | CSRP2 activity raises DHX30's level | lines that do not express CSRP2 (6) vs lines expressing it (44) | 1.46× lower at baseline in the lines without CSRP2 | 0.096 | ⚠ within organs, on part of the lines; also absent: TPST1, TBKBP1, CYP46A1; maybe low, not absent |
| [[LINC02656]] | C | LINC02656 activity lowers DHX30's level | lines that do not express LINC02656 (4) vs lines expressing it (46) | 1.66× higher at baseline in the lines without LINC02656 | 0.029 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02649, MAP3K8, ENSG00000250842; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Clofarabine (drug)]] 0.5 µM | C | DHX30's natural level raises the cells' numbers under Clofarabine 0.5 µM (protects the cells) | DHX30's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.61 | 0.452 over the table, 0.069 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Bendamustine (drug)]] 0.5 µM | C | DHX30's natural level raises the cells' numbers under Bendamustine 0.5 µM (protects the cells) | DHX30's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.57 | 0.507 over the table, 0.098 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.652). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-44.6, 5.0); signed map (-6.4, -24.6). **Vector** length 97.5, 21.3% of its response variance represented; |z| ≥ 3 in 878 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Mitochondrial mRNA modification* (reactome, mean cos +0.52 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.6 | +14.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +7.5 | +7.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.5 | +4.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.2 | +9.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.2 | +8.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.9 | +4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +5.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +4.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.2 | +3.5 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +2.2 | +3.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.4 | -10.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -6.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | -3.3 | -4.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.6 | -5.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.6 | -4.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.2 | -2.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.9 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | DExH-box helicase 30 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:47,802,909-47,850,195 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0890, FLJ11214; previously DDX30 |
| Gene groups (HGNC) | DEAH-box helicases; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7L2E3](https://www.uniprot.org/uniprotkb/Q7L2E3) (ATP-dependent RNA helicase DHX30):

> RNA-dependent helicase. Plays an important role in the assembly of the mitochondrial large ribosomal subunit. Required for optimal function of the zinc-finger antiviral protein ZC3HAV1 (By similarity). Associates with mitochondrial DNA. Involved in nervous system development and differentiation through its involvement in the up-regulation of a number of genes which are required for neurogenesis, including GSC, NCAM1, neurogenin, and NEUROD (By similarity).

**Summary**, from NCBI Gene [22907](https://www.ncbi.nlm.nih.gov/gene/22907):

> DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this DEAD box protein family are believed to be involved in embryogenesis, spermatogenesis, and cellular growth and division. …

**Accessions** — [HGNC:16716](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16716) · Entrez [22907](https://www.ncbi.nlm.nih.gov/gene/22907) · UniProt [Q7L2E3](https://www.uniprot.org/uniprotkb/Q7L2E3) · Ensembl [ENSG00000132153](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132153)

## Data

Gene col 5278: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5278); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5278, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5278]; `tensor/DDL_lfc|DDL_z.npy` [5278]; `embed/gene_vectors.npy` [5278]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5278 or target_col == 5278). Every well: [[DHX30 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DHX30.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
