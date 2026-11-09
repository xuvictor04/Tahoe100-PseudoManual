---
symbol: "LAMA4"
type: "gene"
col: 3404
ensembl_id: "ENSG00000112769"
name: "laminin subunit alpha 4"
location: "6q21"
module: 13
arm: "+"
pooled_cpm: 44.1
n_lines_expressing: 23
n_dd_up: 4
n_dd_down: 54
n_dd_up_clean: 1
n_dd_down_clean: 49
in_vector_space: true
direction_upstream: 14
direction_downstream: 18
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# LAMA4

*laminin subunit alpha 4* — 6q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.24× (z +10.5, q 5e-23, up in 10 of 21 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Rapamycin (drug)]] 5 µM: 1.22× (z +3.7, q 0.035, up in 7 of 21 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (SK-MEL-2 4.54×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 54 drug-doses (5 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.436× (z -10.7, q 4e-24, down in 20 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AK5]] (+0.70, fdr 7e-06), [[ITGA11]] (+0.69, fdr 7e-06), [[INSYN2B]] (+0.68, fdr 7e-06); moves opposite to [[CMKLR2]] (-0.48, fdr 4e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 18 go from it, the strongest it → [[MMP14]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3404.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (SK-MEL-2 4.54×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.24×** | +10.5 | 5e-23 | 10/21 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.25×** | +10.1 | 9e-22 | 11/18 (SK-MEL-2, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.96×** | +8.1 | 9e-14 | 10/19 (NCI-H1792, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Rapamycin (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.035 | 7/21 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 5 µM |  | 1.19× | +3.3 | 0.11 | 11/21 (A-172, PANC-1, …) | rises with dose |  |
| [[Bexarotene (drug)]] 5 µM |  | 1.26× | +3.0 | 0.25 | 7/21 (PANC-1, SNU-423, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 58 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 54 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3404.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.436×** | -10.7 | 4e-24 | 20/21 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.483×** | -9.4 | 1e-18 | 19/21 (Hs 766T, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.487×** | -9.0 | 7e-17 | 15/21 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.513×** | -8.6 | 9e-16 | 18/21 (Panc 03.27, LoVo, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.548×** | -7.8 | 9e-13 | 19/21 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.703×** | -6.4 | 1e-08 | 19/21 (HOP62, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.630×** | -6.0 | 2e-07 | 17/21 (HOP62, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Clobetasol propionate (drug)]] 5 µM | ⚠ position correction uncertain | **0.633×** | -5.9 | 3e-07 | 16/21 (HOP62, J82, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.634×** | -5.9 | 3e-07 | 18/21 (J82, hTERT-HPNE, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.737×** | -5.6 | 2e-06 | 12/21 (HOP62, J82, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.677×** | -5.0 | 2e-05 | 13/21 (HOP62, A498, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.681×** | -4.9 | 4e-05 | 12/21 (hTERT-HPNE, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.682×** | -4.9 | 4e-05 | 17/21 (HOP62, J82, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.664×** | -4.9 | 4e-05 | 6/21 (HOP62, LoVo, …) | all doses, flat |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.767×** | -4.8 | 5e-05 | 13/21 (SK-MEL-2, A498, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.695×** | -4.7 | 9e-05 | 14/21 (hTERT-HPNE, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.697×** | -4.6 | 1e-04 | 18/21 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~22% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3404. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 335 | 0 | 32 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0602× (z -28.5) |
| [[J82 (line)]] | alt | 112 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -17.0) |
| [[hTERT-HPNE (line)]] | wt | 257 | 0 | 12 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.120× (z -13.4) |
| [[LoVo (line)]] | wt | 34.3 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.127× (z -14.6) |
| [[Panc 03.27 (line)]] | alt | 62.5 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -15.3) |
| [[Hs 766T (line)]] | wt | 186 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -17.2) |
| [[AsPC-1 (line)]] | alt | 63.7 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.115× (z -15.3) |
| [[C32 (line)]] | wt | 176 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.305× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 255 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -15.7) |
| [[H4 (line)]] | wt | 14.8 | 0 | 3 | — | [[Betamethasone dipropionate (drug)]] 0.5 µM 0.0543× (z -10.6) |
| [[SK-MEL-2 (line)]] | alt | 95.8 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.54× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -11.6) |
| [[NCI-H2347 (line)]] | alt | 44.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -12.7) |
| [[A498 (line)]] | wt | 27.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -9.5) |
| [[PANC-1 (line)]] | alt | 25.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -11.2) |
| [[RPMI-7951 (line)]] | alt | 24.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -11.6) |
| [[SNU-423 (line)]] | alt | 40.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -8.6) |
| [[SW 1088 (line)]] | alt | 145 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -8.5) |
| [[A-172 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.17 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.31 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.63 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.72 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.61 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.12 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.73 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.15 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.41 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 7.56 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.74 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.08 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.79 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.73 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.83 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.55 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.13 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.54 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.51 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.29 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.48 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.22 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 6.89 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.93 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 10.4 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.86 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3404), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AK5]] | +0.70 | +0.71 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[ITGA11]] | +0.69 | +0.67 / +0.72 | both halves | 7e-06 | pathway: Extracellular matrix organization; STRING 800 |
| [[INSYN2B]] | +0.68 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[SIGLEC15]] | +0.66 | +0.67 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[MMP14]] | +0.65 | +0.68 / +0.61 | both halves | 7e-06 | pathway: Extracellular matrix organization |
| [[DOCK2]] | +0.65 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[CTHRC1]] | +0.63 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[CSMD2]] | +0.62 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[FRMD4A]] | +0.61 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[SAMD3]] | +0.61 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[TMEM200A]] | +0.61 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[SEMA5A]] | +0.61 | +0.57 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMKLR2]] | -0.48 | -0.41 / -0.57 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 2, C 12. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises LAMA4's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 8.7% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds |
| [[RPSAP52]] | B | RPSAP52 activity raises LAMA4's level | lines that do not express RPSAP52 (20) vs lines expressing it (30) | 3.88× lower at baseline in the lines without RPSAP52 | 0.050 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, LINC00702, PLAT; maybe low, not absent |
| [[CSPG4]] | C | CSPG4 activity raises LAMA4's level | lines that do not express CSPG4 (31) vs lines expressing it (19) | 4.61× lower at baseline in the lines without CSPG4 | 0.003 | ⚠ within organs, on part of the lines; also absent: MMP2, PCDH18, AEBP1; co-absent with the target |
| [[HTR1F]] | C | HTR1F activity raises LAMA4's level | lines that do not express HTR1F (34) vs lines expressing it (16) | 5.93× lower at baseline in the lines without HTR1F | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MGP, TIMP3, AEBP1; maybe low, not absent; co-absent with the target |
| [[AEBP1]] | C | AEBP1 activity raises LAMA4's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 3.86× lower at baseline in the lines without AEBP1 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1; co-absent with the target |
| [[GDNF]] | C | GDNF activity raises LAMA4's level | lines that do not express GDNF (38) vs lines expressing it (12) | 5.32× lower at baseline in the lines without GDNF | 0.026 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ITIH5, TDRD9; co-absent with the target |
| [[HHIP]] | C | HHIP activity raises LAMA4's level | lines that do not express HHIP (33) vs lines expressing it (17) | 2.94× lower at baseline in the lines without HHIP | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL5A1, PLPP4, LINC01411; maybe low, not absent; co-absent with the target |
| [[AK5]] | C | AK5 activity raises LAMA4's level | lines that do not express AK5 (25) vs lines expressing it (25) | 4.19× lower at baseline in the lines without AK5 | 0.038 | ⚠ within organs, on part of the lines; also absent: SHISAL1, LINC03047, ITGA4; maybe low, not absent; co-absent with the target |
| [[NES]] | C | NES activity raises LAMA4's level | lines that do not express NES (26) vs lines expressing it (24) | 3.89× lower at baseline in the lines without NES | 0.041 | ⚠ within organs, on part of the lines; also absent: LAPTM5, CSPG4, ENSG00000230490; co-absent with the target |
| [[CTHRC1]] | C | CTHRC1 activity raises LAMA4's level | lines that do not express CTHRC1 (26) vs lines expressing it (24) | 3.94× lower at baseline in the lines without CTHRC1 | 0.048 | ⚠ within organs, on part of the lines; also absent: ARMCX1, MAGI2-AS3, ITGA4; maybe low, not absent; co-absent with the target |
| [[DENND2A]] | C | DENND2A activity raises LAMA4's level | lines that do not express DENND2A (23) vs lines expressing it (27) | 2.36× lower at baseline in the lines without DENND2A | 0.050 | ⚠ within organs, on part of the lines; also absent: PTPRN, SPARC, BAALC; maybe low, not absent; co-absent with the target |
| [[IGFBP7]] | C | IGFBP7 activity raises LAMA4's level | lines that do not express IGFBP7 (27) vs lines expressing it (23) | 4.22× lower at baseline in the lines without IGFBP7 | 0.060 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, FN1; co-absent with the target |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 1, C 17. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MMP14]] | B | LAMA4 activity raises MMP14's level | lines that do not express LAMA4 (27) vs lines expressing it (23) | 5.03× lower at baseline in the lines without LAMA4 | 0.069 | ⚠ within organs, on part of the lines; also absent: SLFN12, ARMCX1, BAALC |
| [[CTHRC1]] | C | LAMA4 activity raises CTHRC1's level | lines that do not express LAMA4 (27) vs lines expressing it (23) | 2.85× lower at baseline in the lines without LAMA4 | 0.005 | ⚠ within organs, on part of the lines; also absent: SLFN12, ARMCX1, BAALC; co-absent with the target |
| [[DENND2A]] | C | LAMA4 activity raises DENND2A's level | lines that do not express LAMA4 (27) vs lines expressing it (23) | 2.81× lower at baseline in the lines without LAMA4 | 0.007 | ⚠ within organs, on part of the lines; also absent: SLFN12, ARMCX1, BAALC; co-absent with the target |
| [[CSPG4]] | C | LAMA4 activity raises CSPG4's level | lines that do not express LAMA4 (27) vs lines expressing it (23) | 3.12× lower at baseline in the lines without LAMA4 | 0.013 | ⚠ within organs, on part of the lines; also absent: SLFN12, ARMCX1, BAALC; co-absent with the target |
| [[ZNF385D]] | C | LAMA4 activity raises ZNF385D's level | lines that do not express LAMA4 (27) vs lines expressing it (23) | 2.55× lower at baseline in the lines without LAMA4 | 0.027 | ⚠ within organs, on part of the lines; also absent: SLFN12, ARMCX1, BAALC; co-absent with the target |
| [[NES]] | C | LAMA4 activity raises NES's level | lines that do not express LAMA4 (27) vs lines expressing it (23) | 2.76× lower at baseline in the lines without LAMA4 | 0.042 | ⚠ within organs, on part of the lines; also absent: SLFN12, ARMCX1, BAALC; co-absent with the target |
| [[PLAT]] | C | LAMA4 activity raises PLAT's level | lines that do not express LAMA4 (27) vs lines expressing it (23) | 4.06× lower at baseline in the lines without LAMA4 | 0.054 | ⚠ within organs, on part of the lines; also absent: SLFN12, ARMCX1, BAALC; co-absent with the target |
| [[IGFBP7]] | C | LAMA4 activity raises IGFBP7's level | lines that do not express LAMA4 (27) vs lines expressing it (23) | 5.00× lower at baseline in the lines without LAMA4 | 0.054 | ⚠ within organs, on part of the lines; also absent: SLFN12, ARMCX1, BAALC; co-absent with the target |
| [[AEBP1]] | C | LAMA4 activity raises AEBP1's level | lines that do not express LAMA4 (27) vs lines expressing it (23) | 2.04× lower at baseline in the lines without LAMA4 | 0.061 | ⚠ within organs, on part of the lines; also absent: SLFN12, ARMCX1, BAALC; co-absent with the target |
| [[IL1RAPL1]] | C | LAMA4 activity raises IL1RAPL1's level | lines that do not express LAMA4 (27) vs lines expressing it (23) | 3.59× lower at baseline in the lines without LAMA4 | 0.068 | ⚠ within organs, on part of the lines; also absent: SLFN12, ARMCX1, BAALC; co-absent with the target |
| [[GDNF]] | C | LAMA4 activity raises GDNF's level | lines that do not express LAMA4 (27) vs lines expressing it (23) | 2.18× lower at baseline in the lines without LAMA4 | 0.073 | ⚠ within organs, on part of the lines; also absent: SLFN12, ARMCX1, BAALC; co-absent with the target |
| [[NAV1]] | C | LAMA4 activity raises NAV1's level | lines that do not express LAMA4 (27) vs lines expressing it (23) | 3.67× lower at baseline in the lines without LAMA4 | 0.084 | ⚠ within organs, on part of the lines; also absent: SLFN12, ARMCX1, BAALC; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.661). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.9, 15.2); signed map (21.4, 46.2). **Vector** length 91.7, 29.7% of its response variance represented; |z| ≥ 3 in 870 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Integrin cell surface interactions* (reactome, mean cos +0.51 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +10.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +8.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +2.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +0.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +2.9 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +1.6 | +2.5 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +1.5 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | -0.9 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +1.2 | +2.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.9 | -8.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.9 | -5.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.8 | -3.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.8 | -2.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.8 | -4.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | laminin subunit alpha 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q21 — chr6:112,107,931-112,254,939 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LAMA3 |
| Gene groups (HGNC) | Laminin subunits |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 18 pathways, smallest: Attachment of bacteria to epithelial cells; Biofilm formation; Developmental Lineage of Pancreatic Ductal Cells |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16363](https://www.uniprot.org/uniprotkb/Q16363) (Laminin subunit alpha-4):

> Binding to cells via a high affinity receptor, laminin is thought to mediate the attachment, migration and organization of cells into tissues during embryonic development by interacting with other extracellular matrix components.

**Summary**, from NCBI Gene [3910](https://www.ncbi.nlm.nih.gov/gene/3910):

> Laminins, a family of extracellular matrix glycoproteins, are the major noncollagenous constituent of basement membranes. They have been implicated in a wide variety of biological processes including cell adhesion, differentiation, migration, signaling, neurite outgrowth and metastasis. Laminins are composed of 3 non identical chains: laminin alpha, beta and gamma (formerly A, B1, and B2, respectively) and they form a cruciform structure consisting of 3 short arms, each formed by a different …

**Accessions** — [HGNC:6484](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6484) · Entrez [3910](https://www.ncbi.nlm.nih.gov/gene/3910) · UniProt [Q16363](https://www.uniprot.org/uniprotkb/Q16363) · Ensembl [ENSG00000112769](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112769)

## Data

Gene col 3404: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3404); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3404, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3404]; `tensor/DDL_lfc|DDL_z.npy` [3404]; `embed/gene_vectors.npy` [3404]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3404 or target_col == 3404). Every well: [[LAMA4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LAMA4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
