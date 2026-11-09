---
symbol: "RNF20"
type: "gene"
col: 7920
ensembl_id: "ENSG00000155827"
name: "ring finger protein 20"
location: "9q31.1"
module: 17
arm: "+"
pooled_cpm: 54.82
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 6
n_dd_up_clean: 11
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# RNF20

*ring finger protein 20* — 9q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.42× (z +16.6, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.630× (z -8.6, q 3e-15, down in 34 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.635× (z -8.5, q 6e-15, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SKIC3]] (+0.70, fdr 7e-06), [[SNRNP48]] (+0.70, fdr 7e-06), [[SF3B2]] (+0.70, fdr 1e-05); moves opposite to [[SATB2]] (-0.60, fdr 2e-05), [[AGO2]] (-0.57, fdr 1e-05), [[TLNRD1]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PLEKHA6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠; shown: the 15 strongest. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7920.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.42×** | +16.6 | 0e+00 | 47/48 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.33×** | +15.9 | 0e+00 | 46/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.93×** | +12.4 | 5e-33 | 43/48 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.79×** | +5.7 | 2e-06 | 31/49 (PANC-1, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.74×** | +5.4 | 7e-06 | 24/48 (PANC-1, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | **1.32×** | +5.3 | 1e-05 | 27/48 (SNU-423, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[NG25 (drug)]] 5 µM |  | **1.64×** | +4.9 | 8e-05 | 30/47 (NCI-H23, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.5 | 4e-04 | 24/48 (AsPC-1, A-427, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.26×** | +4.4 | 7e-04 | 25/48 (LOX-IMVI, RKO, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.25×** | +4.2 | 0.001 | 24/48 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Radotinib (drug)]] 5 µM |  | 1.16× | +4.0 | 0.004 | 17/48 (RKO, AsPC-1, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.22×** | +3.8 | 0.008 | 20/48 (LOX-IMVI, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +3.7 | 0.010 | 23/48 (LOX-IMVI, PANC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.45×** | +3.7 | 0.010 | 23/48 (A498, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.22×** | +3.6 | 0.013 | 22/43 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7920.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.630×** | -8.6 | 3e-15 | 34/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.635×** | -8.5 | 6e-15 | 37/48 (SNU-423, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.636×** | -8.4 | 6e-15 | 36/48 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.648×** | -8.1 | 8e-14 | 35/48 (hTERT-HPNE, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.774×** | -4.8 | 2e-04 | 31/48 (A549, SK-MEL-2, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.782×** | -4.6 | 4e-04 | 24/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.872× | -3.6 | 0.028 | 13/48 (SNU-1, H4, …) | top dose only |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.845× | -3.1 | 0.12 | 7/48 (PANC-1, A-427, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7920. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 67.4 | 4 (1 ⚠) | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.73× (z +14.0) | [[Digitoxin (drug)]] 0.5 µM 0.420× (z -11.9) |
| [[NCI-H460 (line)]] | wt | 63.4 | 3 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.50× (z +12.3) | [[Digitoxin (drug)]] 5 µM 0.316× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.491× (z -9.6) |
| [[PANC-1 (line)]] | alt | 54.5 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 1.96× (z +9.2) | — |
| [[HEC-1-A (line)]] | alt | 60.0 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.57× (z +10.1) | — |
| [[HOP62 (line)]] | alt | 39.1 | 2 | 2 | [[Panobinostat (drug)]] 5 µM 2.61× (z +9.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.369× (z -9.3) |
| [[LS 180 (line)]] | wt | 44.8 | 3 (1 ⚠) | 1 | [[Panobinostat (drug)]] 0.5 µM 3.41× (z +11.5) | [[Digitoxin (drug)]] 0.5 µM 0.362× (z -9.4) |
| [[RKO (line)]] | wt | 50.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +14.8) ⚠ cell-cycle shift, explains ~6% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.95× (z +11.6) | — |
| [[SNU-423 (line)]] | alt | 70.6 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | [[Homoharringtonine (drug)]] 5 µM 0.497× (z -10.4) ⚠ cell-cycle shift, explains ~6% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.408× (z -9.4) |
| [[A-172 (line)]] | wt | 77.0 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.48× (z +10.7) | — |
| [[A498 (line)]] | wt | 60.0 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.72× (z +11.7) | — |
| [[J82 (line)]] | alt | 72.3 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.72× (z +11.9) | — |
| [[KATO III (line)]] | alt | 68.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.70× (z +9.7) | — |
| [[Hs 766T (line)]] | wt | 66.5 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.53× (z +9.4) | — |
| [[HT-29 (line)]] | alt | 35.1 | 1 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.58× (z +8.5) | [[Digitoxin (drug)]] 0.5 µM 0.347× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 47.1 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.253× (z -10.1) |
| [[LoVo (line)]] | wt | 25.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.10× (z +10.7) | — |
| [[NCI-H1792 (line)]] | alt | 47.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.70× (z +9.1) | — |
| [[SHP-77 (line)]] | alt | 93.8 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.14× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.395× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[AN3 CA (line)]] | alt | 86.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.154× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 54.1 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.92× (z +8.7) | — |
| [[H4 (line)]] | wt | 50.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.236× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 51.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.306× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[LOX-IMVI (line)]] | wt | 63.7 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.23× (z +9.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 61.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.80× (z +9.2) | — |
| [[NCI-H2347 (line)]] | alt | 36.0 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.56× (z +9.3) | — |
| [[SK-MEL-2 (line)]] | alt | 70.3 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.41× (z +8.9) | — |
| [[SNU-1 (line)]] | wt | 56.5 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.330× (z -11.5) |
| [[SW 900 (line)]] | alt | 39.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.316× (z -8.8) |
| [[SW48 (line)]] | wt | 54.0 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.50× (z +9.0) | — |
| [[A-427 (line)]] | wt | 44.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 69.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 58.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 71.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 76.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 76.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 98.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 77.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7920), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SKIC3]] | +0.70 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[SNRNP48]] | +0.70 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[SF3B2]] | +0.70 | +0.75 / +0.53 | both halves | 1e-05 |  |
| [[METTL14]] | +0.69 | +0.77 / +0.61 | both halves | 7e-06 |  |
| [[HARS2]] | +0.68 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[LONP2]] | +0.67 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[CDC40]] | +0.67 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[VIRMA]] | +0.67 | +0.72 / +0.58 | both halves | 7e-06 | STRING 518 |
| [[RNF214]] | +0.64 | +0.65 / +0.54 | both halves | 1e-05 | same gene group |
| [[MIGA1]] | +0.64 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[RFC1]] | +0.64 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[HEATR6]] | +0.63 | +0.59 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SATB2]] | -0.60 | -0.54 / -0.46 | both halves | 2e-05 |  |
| [[AGO2]] | -0.57 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[TLNRD1]] | -0.57 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[PHLDA2]] | -0.56 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[E2F3]] | -0.53 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[HIVEP1]] | -0.53 | -0.43 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHA6]] | B | PLEKHA6 activity lowers RNF20's level | lines that do not express PLEKHA6 (16) vs lines expressing it (34) | 1.32× higher at baseline in the lines without PLEKHA6 | 0.029 | ⚠ within organs, on part of the lines; also absent: KCNK1, ELF3, TNK1; maybe low, not absent |
| [[ZNF420]] | B | ZNF420 activity raises RNF20's level | lines that do not express ZNF420 (7) vs lines expressing it (43) | 1.34× lower at baseline in the lines without ZNF420 | 0.055 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF850, ZNF540 |
| [[ZNF567-DT]], [[ZNF571]] | B | ZNF567-DT, ZNF571 activity raises RNF20's level | lines that do not express ZNF567-DT, ZNF571 (6) vs lines expressing them (44) | 1.35× lower at baseline in the lines without ZNF567-DT, ZNF571 | 0.077 | ⚠ within organs, on part of the lines; also absent: ZNF420, ZNF850, ZNF540; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.723). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-19.4, -5.8); signed map (-26.3, -16.4). **Vector** length 117, 33.1% of its response variance represented; |z| ≥ 3 in 1,042 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.9 | +5.7 |
|  | [[NG25 (drug)]] 5 µM |  | +5.1 | +4.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.6 | +5.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.4 | +16.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.9 | +15.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.8 | +4.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.6 | +4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +3.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.5 | +2.5 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -8.1 | -8.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -7.9 | -8.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -7.6 | -8.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -6.7 | -8.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.4 | +1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.5 | -3.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.6 | -1.8 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | -2.2 | -2.2 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -2.1 | -2.4 |
|  | [[Decitabine (drug)]] 0.05 µM |  | -2.0 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | ring finger protein 20 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q31.1 — chr9:101,533,853-101,563,344 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20382, FLJ11189, KAIA2779, BRE1A, hBRE1, BRE1 |
| Gene groups (HGNC) | Ring finger proteins; RING finger E3 ubiquitin protein ligases |
| Reactome | 7 pathways, smallest: RHOBTB1 GTPase cycle; RHOBTB GTPase Cycle; E3 ubiquitin ligases ubiquitinate target proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VTR2](https://www.uniprot.org/uniprotkb/Q5VTR2) (E3 ubiquitin-protein ligase BRE1A):

> Component of the RNF20/40 E3 ubiquitin-protein ligase complex that mediates monoubiquitination of 'Lys-120' of histone H2B (H2BK120ub1). H2BK120ub1 gives a specific tag for epigenetic transcriptional activation and is also prerequisite for histone H3 'Lys-4' and 'Lys-79' methylation (H3K4me and H3K79me, respectively). It thereby plays a central role inb histone code and gene regulation. The RNF20/40 complex forms a H2B ubiquitin ligase complex in cooperation with the E2 enzyme UBE2A or UBE2B; …

**Summary**, from NCBI Gene [56254](https://www.ncbi.nlm.nih.gov/gene/56254):

> The protein encoded by this gene shares similarity with BRE1 of S. cerevisiae. The protein encoded by this human gene is an E3 ubiquitin ligase that regulates chromosome structure by monoubiquitinating histone H2B. This protein acts as a putative tumor suppressor and positively regulates the p53 tumor suppressor as well as numerous histone H2A and H2B genes. In contrast, this protein also suppresses the expression of several protooncogenes and growth-related genes, including many genes that are …

**Accessions** — [HGNC:10062](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10062) · Entrez [56254](https://www.ncbi.nlm.nih.gov/gene/56254) · UniProt [Q5VTR2](https://www.uniprot.org/uniprotkb/Q5VTR2) · Ensembl [ENSG00000155827](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155827)

## Data

Gene col 7920: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7920); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7920, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7920]; `tensor/DDL_lfc|DDL_z.npy` [7920]; `embed/gene_vectors.npy` [7920]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7920 or target_col == 7920). Every well: [[RNF20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNF20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
