---
symbol: "LRP3"
type: "gene"
col: 5143
ensembl_id: "ENSG00000130881"
name: "LDL receptor related protein 3"
location: "19q13.11"
module: 146
arm: "+"
pooled_cpm: 2.98
n_lines_expressing: 43
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 20
tags: ["gene", "module/146"]
generated_by: "tahoemap"
---

# LRP3

*LDL receptor related protein 3* — 19q13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 9.12× (z +20.5, q 0e+00, up in 4 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.66× (z +6.9, q 7e-10, up in 16 of 27 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A498 0.219×); [[Silodosin (drug)]] 5 µM in 1 line (SW1417 0.0942×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MSI1]] (+0.57, fdr 3e-05), [[MTARC1]] (+0.56, fdr 2e-05), [[CARM1]] (+0.55, fdr 1e-05); moves opposite to [[BZW1]] (-0.44, fdr 1e-04), [[SETX]] (-0.43, fdr 6e-05).
> It sits in the **+** arm of [[Module 146]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[BRSK2]] → it (grade B ⚠); 20 go from it, the strongest it → [[DFFB]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5143.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **9.12×** | +20.5 | 0e+00 | 4/4 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.76×** | +18.4 | 0e+00 | 15/16 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.44×** | +13.6 | 1e-39 | 6/6 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.17×** | +7.2 | 1e-10 | 10/21 (NCI-H460, A-427, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +6.9 | 7e-10 | 16/27 (A549, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.79×** | +5.2 | 2e-05 | 6/12 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.46×** | +5.1 | 3e-05 | 8/38 (HOP62, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +4.0 | 0.005 | 5/16 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.50×** | +3.9 | 0.006 | 6/18 (BT-474, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.45×** | +3.5 | 0.031 | 5/34 (MIA PaCa-2, NCI-H1792, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.43×** | +3.4 | 0.032 | 11/38 (HEC-1-A, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.29×** | +3.4 | 0.032 | 9/28 (HEC-1-A, NCI-H2347, …) | top dose only | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +3.3 | 0.041 | 7/28 (A-172, A498, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +3.3 | 0.041 | 6/36 (CFPAC-1, HEC-1-A, …) | rises with dose |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +3.0 | 0.097 | 5/27 (NCI-H460, C-33 A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5143.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A498 0.219×); [[Silodosin (drug)]] 5 µM in 1 line (SW1417 0.0942×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[(S)-Crizotinib (drug)]] 0.5 µM |  | 0.723× | -3.2 | 0.49 | 7/39 (Panc 03.27, H4, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.725× | -3.1 | 0.49 | 9/39 (SW 900, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5143. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 3.44 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 8.15× (z +8.7) ⚠ toxic; transcription drop | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.219× (z -9.3) |
| [[HOP62 (line)]] | alt | 2.47 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 30.0× (z +10.0) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 3.20 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 20.3× (z +9.1) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 2.34 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.06× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 5.06 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0942× (z -8.8) |
| [[SW480 (line)]] | alt | 3.60 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.0× (z +12.0) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 7.87 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.47 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.601 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.70 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.420 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.535 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.315 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.389 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.602 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.50 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.888 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.60 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.528 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.30 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5143), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSI1]] | +0.57 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[MTARC1]] | +0.56 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[CARM1]] | +0.55 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[PXN-AS1]] | +0.54 | +0.28 / +0.65 | both halves | 3e-04 |  |
| [[HSPE1-MOB4]] | +0.52 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[PACSIN3]] | +0.52 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[RAVER2]] | +0.51 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[ABCC11]] | +0.51 | +0.33 / +0.53 | both halves | 1e-04 |  |
| [[MLLT10]] | +0.51 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[GEMIN7-AS1]] | +0.51 | +0.37 / +0.63 | both halves | 7e-05 |  |
| [[RYK]] | +0.50 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[TCEA2]] | +0.50 | +0.44 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BZW1]] | -0.44 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[SETX]] | -0.43 | -0.38 / -0.43 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BRSK2]] | B | BRSK2 activity raises LRP3's level | lines that do not express BRSK2 (14) vs lines expressing it (36) | 1.64× lower at baseline in the lines without BRSK2 | 0.060 | ⚠ within organs, on part of the lines; also absent: KIF26A, APLP1, E2F2; maybe low, not absent |
| [[PRTG]] | B | PRTG activity raises LRP3's level | lines that do not express PRTG (14) vs lines expressing it (36) | 1.48× lower at baseline in the lines without PRTG | 0.060 | ⚠ within organs, on part of the lines; also absent: ANKRD6, BNIP3, SNRPN |
| [[NCS1]] | B | NCS1 activity raises LRP3's level | lines that do not express NCS1 (6) vs lines expressing it (44) | 2.09× lower at baseline in the lines without NCS1 | 0.061 | ⚠ within organs, on part of the lines; also absent: SH3BP5, ZNF618, PBK; maybe low, not absent |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 20, C 0. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DFFB]] | B | LRP3 activity raises DFFB's level | lines that do not express LRP3 (7) vs lines expressing it (43) | 1.65× lower at baseline in the lines without LRP3 | 0.001 | ⚠ within organs, on part of the lines; also absent: ACBD7, SNTA1, TMCC2; maybe low, not absent |
| [[DUSP12]] | B | LRP3 activity raises DUSP12's level | lines that do not express LRP3 (7) vs lines expressing it (43) | 1.51× lower at baseline in the lines without LRP3 | 0.014 | ⚠ within organs, on part of the lines; also absent: ACBD7, SNTA1, TMCC2; maybe low, not absent |
| [[CARM1]] | B | LRP3 activity raises CARM1's level | lines that do not express LRP3 (7) vs lines expressing it (43) | 1.40× lower at baseline in the lines without LRP3 | 0.031 | ⚠ within organs, on part of the lines; also absent: ACBD7, SNTA1, TMCC2; maybe low, not absent |
| [[BLMH]] | B | LRP3 activity raises BLMH's level | lines that do not express LRP3 (7) vs lines expressing it (43) | 2.72× lower at baseline in the lines without LRP3 | 0.033 | ⚠ within organs, on part of the lines; also absent: ACBD7, SNTA1, TMCC2; maybe low, not absent |
| [[CIBAR1]] | B | LRP3 activity raises CIBAR1's level | lines that do not express LRP3 (7) vs lines expressing it (43) | 2.44× lower at baseline in the lines without LRP3 | 0.040 | ⚠ within organs, on part of the lines; also absent: ACBD7, SNTA1, TMCC2; maybe low, not absent |
| [[MLLT10]] | B | LRP3 activity raises MLLT10's level | lines that do not express LRP3 (7) vs lines expressing it (43) | 1.54× lower at baseline in the lines without LRP3 | 0.041 | ⚠ within organs, on part of the lines; also absent: ACBD7, SNTA1, TMCC2; maybe low, not absent |
| [[ANKRD13B]] | B | LRP3 activity raises ANKRD13B's level | lines that do not express LRP3 (7) vs lines expressing it (43) | 2.07× lower at baseline in the lines without LRP3 | 0.042 | ⚠ within organs, on part of the lines; also absent: ACBD7, SNTA1, TMCC2; maybe low, not absent |
| [[HSF2]] | B | LRP3 activity raises HSF2's level | lines that do not express LRP3 (7) vs lines expressing it (43) | 1.55× lower at baseline in the lines without LRP3 | 0.043 | ⚠ within organs, on part of the lines; also absent: ACBD7, SNTA1, TMCC2; maybe low, not absent |
| [[NT5C3B]] | B | LRP3 activity raises NT5C3B's level | lines that do not express LRP3 (7) vs lines expressing it (43) | 2.05× lower at baseline in the lines without LRP3 | 0.045 | ⚠ within organs, on part of the lines; also absent: ACBD7, SNTA1, TMCC2; maybe low, not absent |
| [[FBXO44]] | B | LRP3 activity raises FBXO44's level | lines that do not express LRP3 (7) vs lines expressing it (43) | 1.95× lower at baseline in the lines without LRP3 | 0.046 | ⚠ within organs, on part of the lines; also absent: ACBD7, SNTA1, TMCC2; maybe low, not absent |
| [[PRTG]] | B | LRP3 activity raises PRTG's level | lines that do not express LRP3 (7) vs lines expressing it (43) | 5.14× lower at baseline in the lines without LRP3 | 0.051 | ⚠ within organs, on part of the lines; also absent: ACBD7, SNTA1, TMCC2; maybe low, not absent |
| [[NCS1]] | B | LRP3 activity raises NCS1's level | lines that do not express LRP3 (7) vs lines expressing it (43) | 2.59× lower at baseline in the lines without LRP3 | 0.055 | ⚠ within organs, on part of the lines; also absent: ACBD7, SNTA1, TMCC2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 146]]; 31 genes; this gene is in the **+** arm (projection on the module's main direction 0.544). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-0.6, 43.3); signed map (-5.4, -59.2). **Vector** length 41.1, 5.14% of its response variance represented; |z| ≥ 3 in 769 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +20.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +18.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +13.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +6.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.6 | +5.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +2.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +1.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -1.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -0.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | +0.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.0 | -0.8 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.0 | -2.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -1.6 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -1.8 |
|  | [[Entecavir (monohydrate) (drug)]] 5 µM |  | -0.9 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | LDL receptor related protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.11 — chr19:33,177,603-33,208,864 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LRP-3, hLRp105 |
| Gene groups (HGNC) | Low density lipoprotein receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [O75074](https://www.uniprot.org/uniprotkb/O75074) (Low-density lipoprotein receptor-related protein 3):

> Probable receptor, which may be involved in the internalization of lipophilic molecules and/or signal transduction. Its precise role is however unclear, since it does not bind to very low density lipoprotein (VLDL) or to LRPAP1 in vitro.

**Summary**, from NCBI Gene [4037](https://www.ncbi.nlm.nih.gov/gene/4037):

> Involved in negative regulation of fat cell differentiation; positive regulation of osteoblast differentiation; and regulation of gene expression. Predicted to be located in membrane. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:6695](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6695) · Entrez [4037](https://www.ncbi.nlm.nih.gov/gene/4037) · UniProt [O75074](https://www.uniprot.org/uniprotkb/O75074) · Ensembl [ENSG00000130881](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130881)

## Data

Gene col 5143: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5143); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5143, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5143]; `tensor/DDL_lfc|DDL_z.npy` [5143]; `embed/gene_vectors.npy` [5143]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5143 or target_col == 5143). Every well: [[LRP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
