---
symbol: "OSTF1"
type: "gene"
col: 5634
ensembl_id: "ENSG00000134996"
name: "osteoclast stimulating factor 1"
location: "9q21.13"
module: 88
arm: "-"
pooled_cpm: 30.34
n_lines_expressing: 49
n_dd_up: 9
n_dd_down: 12
n_dd_up_clean: 8
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# OSTF1

*osteoclast stimulating factor 1* — 9q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 2.26× (z +15.4, q 0e+00, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.628× (z -8.8, q 7e-16, down in 26 of 46 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCMT1]] (+0.69, fdr 7e-06), [[POGLUT2]] (+0.68, fdr 1e-05), [[ARL3]] (+0.67, fdr 1e-05); moves opposite to [[GTF2H1]] (-0.66, fdr 3e-05), [[WARS2-AS1]] (-0.66, fdr 2e-04), [[DUS3L]] (-0.62, fdr 2e-05).
> It sits in the **-** arm of [[Module 088]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TSPAN33]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5634.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **2.26×** | +15.4 | 0e+00 | 42/47 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.92×** | +12.4 | 5e-33 | 40/47 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.86×** | +11.8 | 1e-29 | 37/47 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.60×** | +8.9 | 8e-17 | 35/46 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.54×** | +8.2 | 3e-14 | 33/47 (SNU-423, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.92×** | +6.5 | 1e-08 | 28/47 (HEC-1-A, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +6.3 | 2e-08 | 25/47 (NCI-H460, HEC-1-A, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.62×** | +4.8 | 1e-04 | 18/47 (SW480, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 5 µM |  | 1.14× | +3.6 | 0.022 | 6/47 (NCI-H460, SNU-1, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.21×** | +3.4 | 0.035 | 10/46 (SW480, SW1417, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5634.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.628×** | -8.8 | 7e-16 | 26/46 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.650×** | -8.2 | 1e-13 | 26/47 (HS-578T, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.756×** | -7.5 | 1e-11 | 27/46 (Hs 766T, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.787×** | -6.4 | 2e-08 | 23/47 (AsPC-1, LOX-IMVI, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.547×** | -6.0 | 3e-07 | 24/47 (LoVo, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.755×** | -5.3 | 1e-05 | 22/47 (NCI-H2347, BT-474, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.770×** | -4.9 | 6e-05 | 19/47 (HS-578T, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.835× | -4.8 | 1e-04 | 21/47 (A-427, HOP62, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.783×** | -4.6 | 2e-04 | 22/46 (HS-578T, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.785×** | -4.6 | 3e-04 | 19/46 (A-172, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.788×** | -4.5 | 3e-04 | 18/46 (HS-578T, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.676×** | -3.9 | 0.005 | 14/46 (HOP62, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.824×** | -3.5 | 0.020 | 19/45 (NCI-H1573, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.952× | -3.4 | 0.026 | 3/47 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.843× | -3.2 | 0.048 | 10/46 (LOX-IMVI, BT-474, …) | top dose only |  |
| [[Omeprazole (drug)]] 0.05 µM |  | 0.845× | -3.2 | 0.054 | 6/47 (A-427, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5634. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 36.5 | 0 | 7 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.147× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.176× (z -13.1) |
| [[A498 (line)]] | wt | 21.8 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 2.93× (z +9.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.300× (z -10.2) |
| [[NCI-H460 (line)]] | wt | 21.0 | 3 | 1 | [[Belinostat (drug)]] 5 µM 3.39× (z +11.8) | [[Homoharringtonine (drug)]] 0.05 µM 0.379× (z -9.4) |
| [[HOP62 (line)]] | alt | 28.2 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.265× (z -10.5) |
| [[hTERT-HPNE (line)]] | wt | 55.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 15.0 | 2 | 1 | [[Belinostat (drug)]] 5 µM 4.47× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -9.5) |
| [[A-172 (line)]] | wt | 14.6 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.228× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 21.2 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.151× (z -12.5) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.409× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 18.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -10.5) |
| [[SW1417 (line)]] | alt | 40.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.267× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 20.7 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.327× (z -10.9) |
| [[AsPC-1 (line)]] | alt | 40.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.311× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 26.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.107× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 32.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 28.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.155× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 36.2 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.53× (z +9.3) | — |
| [[Hs 766T (line)]] | wt | 57.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -13.3) |
| [[J82 (line)]] | alt | 71.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -10.9) |
| [[KATO III (line)]] | alt | 57.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.321× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[LOX-IMVI (line)]] | wt | 41.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -12.8) |
| [[PANC-1 (line)]] | alt | 22.8 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.34× (z +8.7) | — |
| [[A549 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.45 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 35.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5634), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCMT1]] | +0.69 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[POGLUT2]] | +0.68 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[ARL3]] | +0.67 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[RAP1A]] | +0.66 | +0.61 / +0.57 | both halves | 8e-06 |  |
| [[YIF1B]] | +0.66 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[CARD19]] | +0.63 | +0.60 / +0.41 | both halves | 4e-05 |  |
| [[MBOAT2]] | +0.63 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[SLC9A6]] | +0.63 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[RRAS]] | +0.63 | +0.60 / +0.32 | both halves | 2e-04 |  |
| [[INPP5F]] | +0.62 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[LPCAT4]] | +0.62 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[MACO1]] | +0.62 | +0.65 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2H1]] | -0.66 | -0.63 / -0.43 | both halves | 3e-05 |  |
| [[WARS2-AS1]] | -0.66 | -0.64 / -0.29 | both halves | 2e-04 |  |
| [[DUS3L]] | -0.62 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[LINC00571]] | -0.61 | -0.55 / -0.39 | both halves | 6e-05 |  |
| [[VPS35L]] | -0.61 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[ZFY]] | -0.61 | -0.56 / -0.38 | both halves | 7e-05 |  |
| [[SNAPC5]] | -0.60 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[WARS2]] | -0.60 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[FBXL19-AS1]] | -0.60 | -0.54 / -0.30 | both halves | 2e-04 |  |
| [[ZNF24]] | -0.60 | -0.55 / -0.39 | both halves | 6e-05 |  |
| [[SPART-AS1]] | -0.60 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[ZNF507]] | -0.60 | -0.55 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSPAN33]] | B | TSPAN33 activity lowers OSTF1's level | lines that do not express TSPAN33 (12) vs lines expressing it (38) | 1.36× higher at baseline in the lines without TSPAN33 | 0.067 | ⚠ within organs, on part of the lines; also absent: SRCIN1, CRACD, GNAZ; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers OSTF1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers OSTF1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **-** arm (projection on the module's main direction -0.670). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (4.1, -11.9); signed map (-31.6, 15.8). **Vector** length 111, 27.2% of its response variance represented; |z| ≥ 3 in 948 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +6.6 | +15.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.1 | +8.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.9 | +11.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.8 | +8.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.5 | +12.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.2 | +6.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +6.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.0 | +4.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.3 | +2.3 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +2.2 | +2.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.0 | -8.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.4 | -4.8 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.0 | -6.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.8 | -7.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.4 | -2.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.8 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -2.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.5 | -1.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.5 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | osteoclast stimulating factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.13 — chr9:75,088,514-75,147,265 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SH3P2, OSF, bA235O14.1 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; SH3 domain containing |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92882](https://www.uniprot.org/uniprotkb/Q92882) (Osteoclast-stimulating factor 1):

> Induces bone resorption, acting probably through a signaling cascade which results in the secretion of factor(s) enhancing osteoclast formation and activity.

**Summary**, from NCBI Gene [26578](https://www.ncbi.nlm.nih.gov/gene/26578):

> Osteoclast-stimulating factor-1 is an intracellular protein produced by osteoclasts that indirectly induces osteoclast formation and bone resorption (Reddy et al., 1998 [PubMed 10092216]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:8510](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8510) · Entrez [26578](https://www.ncbi.nlm.nih.gov/gene/26578) · UniProt [Q92882](https://www.uniprot.org/uniprotkb/Q92882) · Ensembl [ENSG00000134996](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134996)

## Data

Gene col 5634: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5634); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5634, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5634]; `tensor/DDL_lfc|DDL_z.npy` [5634]; `embed/gene_vectors.npy` [5634]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5634 or target_col == 5634). Every well: [[OSTF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OSTF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
