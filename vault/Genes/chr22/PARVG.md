---
symbol: "PARVG"
type: "gene"
col: 6255
ensembl_id: "ENSG00000138964"
name: "parvin gamma"
location: "22q13.31"
module: 47
arm: "+"
pooled_cpm: 2.49
n_lines_expressing: 35
n_dd_up: 3
n_dd_down: 13
n_dd_up_clean: 0
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 8
direction_downstream: 12
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# PARVG

*parvin gamma* — 22q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.23× (z +8.0, q 8e-13, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.232× (z -8.5, q 1e-14, down in 23 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PARVB]] (+0.73, fdr 7e-06, ⚠ read-through risk), [[BLZF2P]] (+0.70, fdr 7e-06), [[A3GALT2]] (+0.69, fdr 7e-06), [[SPTBN5]] (+0.69, fdr 7e-06); moves opposite to [[RCOR3]] (-0.52, fdr 8e-05), [[XPA]] (-0.48, fdr 4e-05), [[PHC3]] (-0.48, fdr 4e-05).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[LEF1-AS1]] → it (grade B ⚠); 12 go from it, the strongest it → [[ZFP69B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6255.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.23×** | +8.0 | 8e-13 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.18×** | +5.1 | 1e-04 | 2/7 (SW480, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.67×** | +3.6 | 0.054 | 1/12 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Proglumide (drug)]] 0.05 µM |  | 1.59× | +3.2 | 0.16 | 3/25 (J82, H4, …) | inconsistent across doses | position effect removed |
| [[Demeclocycline (drug)]] 5 µM |  | 1.37× | +3.1 | 0.20 | 3/29 (HOP62, BT-474, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.55× | +3.1 | 0.20 | 8/20 (J82, NCI-H460, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6255.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.232×** | -8.5 | 1e-14 | 23/30 (H4, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.448×** | -8.1 | 2e-13 | 19/22 (C32, SW480, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.319×** | -7.8 | 1e-12 | 22/26 (SW480, RPMI-7951, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.412×** | -6.3 | 4e-08 | 19/26 (SW480, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.431×** | -6.0 | 2e-07 | 17/27 (RPMI-7951, PANC-1, …) | two highest doses | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.443×** | -5.8 | 6e-07 | 18/29 (H4, C32, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.463×** | -5.5 | 3e-06 | 11/29 (H4, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.665×** | -4.1 | 0.003 | 9/29 (C32, AsPC-1, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.346×** | -3.9 | 0.005 | 13/26 (RPMI-7951, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.514×** | -3.9 | 0.006 | 14/16 (SW480, RPMI-7951, …) | two highest doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.608×** | -3.6 | 0.019 | 9/29 (C32, AsPC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.610×** | -3.5 | 0.019 | 14/22 (C32, SW480, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.415×** | -3.3 | 0.045 | 9/19 (C32, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.595× | -3.0 | 0.10 | 6/29 (C32, hTERT-HPNE, …) | top dose only | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.54 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6255. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 5.59 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0586× (z -11.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.118× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 16.6 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0329× (z -12.4) |
| [[C32 (line)]] | wt | 27.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0533× (z -15.0) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.0412× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 3.81 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0298× (z -8.7) |
| [[PANC-1 (line)]] | alt | 2.28 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0384× (z -11.2) |
| [[A-172 (line)]] | wt | 0.679 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.350 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.478 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.463 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.244 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.252 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.229 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.272 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.219 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.581 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.290 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.215 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.996 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.515 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.510 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.836 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.858 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.203 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.402 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6255), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PARVB]] | +0.73 | +0.69 / +0.69 | both halves | 7e-06 | same gene group; STRING 914; ⚠ **readthrough risk**: this gene lies 0.0 kb 3′ of PARVB on the same strand (can correlate by spillover, not regulation) |
| [[BLZF2P]] | +0.70 | +0.63 / +0.74 | both halves | 7e-06 |  |
| [[A3GALT2]] | +0.69 | +0.62 / +0.75 | both halves | 7e-06 |  |
| [[SPTBN5]] | +0.69 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[C13orf46]] | +0.68 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[MSANTD1]] | +0.62 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[NPAS1]] | +0.60 | +0.60 / +0.58 | both halves | 8e-06 |  |
| [[GHRLOS]] | +0.60 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[REP15]] | +0.60 | +0.61 / +0.57 | both halves | 8e-06 |  |
| [[LINC02236]] | +0.59 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[BMP8A]] | +0.59 | +0.46 / +0.64 | both halves | 2e-05 |  |
| [[DOK3]] | +0.58 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[SPRED3]] | +0.57 | +0.54 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RCOR3]] | -0.52 | -0.37 / -0.59 | both halves | 8e-05 |  |
| [[XPA]] | -0.48 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[PHC3]] | -0.48 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[RAB9A]] | -0.47 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[FBXL5]] | -0.46 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[NR1D2]] | -0.46 | -0.38 / -0.52 | both halves | 7e-05 |  |
| [[KIF13A]] | -0.46 | -0.41 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LEF1-AS1]] | B | LEF1-AS1 activity raises PARVG's level | lines that do not express LEF1-AS1 (33) vs lines expressing it (17) | 2.27× lower at baseline in the lines without LEF1-AS1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL19A1, ENSG00000226043, DCT; maybe low, not absent |
| [[HS3ST3A1]] | B | HS3ST3A1 activity raises PARVG's level | lines that do not express HS3ST3A1 (33) vs lines expressing it (17) | 2.00× lower at baseline in the lines without HS3ST3A1 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000224865, CDH13, COL19A1 |
| [[ADAMTS4]] | B | ADAMTS4 activity raises PARVG's level | lines that do not express ADAMTS4 (39) vs lines expressing it (11) | 1.99× lower at baseline in the lines without ADAMTS4 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: FCRLA, APOA2, A2M |
| [[MIR3681HG]] | B | MIR3681HG activity raises PARVG's level | lines that do not express MIR3681HG (27) vs lines expressing it (23) | 1.65× lower at baseline in the lines without MIR3681HG | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000225649, BAALC, LINC02930; maybe low, not absent |
| [[LINC02985]] | B | LINC02985 activity raises PARVG's level | lines that do not express LINC02985 (15) vs lines expressing it (35) | 1.49× lower at baseline in the lines without LINC02985 | 0.074 | ⚠ within organs, on part of the lines; also absent: GXYLT2 |
| [[PTPRZ1]] | B | PTPRZ1 activity raises PARVG's level | lines that do not express PTPRZ1 (40) vs lines expressing it (10) | 2.37× lower at baseline in the lines without PTPRZ1 | 0.077 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, KRT5, ENSG00000242029 |
| [[PARVB]] | C | PARVB activity raises PARVG's level | lines that do not express PARVB (13) vs lines expressing it (37) | 2.61× lower at baseline in the lines without PARVB | 0.002 | ⚠ within organs, on part of the lines; also absent: PARVG, MSRB3, RASSF8; co-absent with the target |
| [[FRMD4A]] | C | FRMD4A activity raises PARVG's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 1.87× lower at baseline in the lines without FRMD4A | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 11, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZFP69B]] | B | PARVG activity raises ZFP69B's level | lines that do not express PARVG (15) vs lines expressing it (35) | 2.23× lower at baseline in the lines without PARVG | 0.035 | ⚠ within organs, on part of the lines; also absent: PARVB, DCLK2, RASSF8 |
| [[NPAS1]] | B | PARVG activity raises NPAS1's level | lines that do not express PARVG (15) vs lines expressing it (35) | 2.39× lower at baseline in the lines without PARVG | 0.036 | ⚠ within organs, on part of the lines; also absent: PARVB, DCLK2, RASSF8 |
| [[REP15]] | B | PARVG activity raises REP15's level | lines that do not express PARVG (15) vs lines expressing it (35) | 1.39× lower at baseline in the lines without PARVG | 0.066 | ⚠ within organs, on part of the lines; also absent: PARVB, DCLK2, RASSF8 |
| cells under [[Afatinib (drug)]] 0.5 µM | B | PARVG activity raises the cells' numbers under Afatinib 0.5 µM (protects the cells) | lines that do not express PARVG (15) vs lines expressing it (33) | the lines without PARVG: 0.90× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: PARVB, DCLK2, RASSF8 |
| cells under [[Minodronic acid (drug)]] 0.5 µM | B | PARVG activity raises the cells' numbers under Minodronic acid 0.5 µM (protects the cells) | lines that do not express PARVG (15) vs lines expressing it (33) | the lines without PARVG: 0.82× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: PARVB, DCLK2, RASSF8 |
| cells under [[Berbamine (dihydrochloride) (drug)]] 0.5 µM | B | PARVG activity raises the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (protects the cells) | lines that do not express PARVG (15) vs lines expressing it (33) | the lines without PARVG: 0.86× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: PARVB, DCLK2, RASSF8 |
| [[FIBCD1]] | B | PARVG activity strengthens FIBCD1's drug response | lines that do not express PARVG (11) vs lines expressing it (24) | the lines without PARVG respond 0.48× as strongly (z diff +1.88); strongest at Harringtonine 5 µM: 0.41x vs 0.17x (z diff +3.6) | 0.086 | ⚠ within organs, on part of the lines; also absent: PARVB, DCLK2, RASSF8; target measured in part of the lines; artifact flags |
| cells under [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM | B | PARVG activity raises the cells' numbers under Sivelestat (sodium tetrahydrate) 5 µM (protects the cells) | lines that do not express PARVG (15) vs lines expressing it (33) | the lines without PARVG: 0.87× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: PARVB, DCLK2, RASSF8 |
| [[MSS51]] | B | PARVG activity raises MSS51's level | lines that do not express PARVG (15) vs lines expressing it (35) | 1.17× lower at baseline in the lines without PARVG | 0.091 | ⚠ within organs, on part of the lines; also absent: PARVB, DCLK2, RASSF8 |
| [[FIBCD1]] | B | PARVG activity raises FIBCD1's level | lines that do not express PARVG (15) vs lines expressing it (35) | 1.56× lower at baseline in the lines without PARVG | 0.093 | ⚠ within organs, on part of the lines; also absent: PARVB, DCLK2, RASSF8 |
| cells under [[Aliskiren (drug)]] 0.5 µM | B | PARVG activity lowers the cells' numbers under Aliskiren 0.5 µM (makes them more sensitive) | lines that do not express PARVG (15) vs lines expressing it (33) | the lines without PARVG: 1.36× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: PARVB, DCLK2, RASSF8 |
| [[PARVB]] | C | PARVG activity raises PARVB's level | lines that do not express PARVG (15) vs lines expressing it (35) | 5.62× lower at baseline in the lines without PARVG | 2e-04 | ⚠ within organs, on part of the lines; also absent: PARVB, DCLK2, RASSF8; co-absent with the target |

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.607). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.9, -15.3); signed map (15.8, 16.1). **Vector** length 57.7, 11.4% of its response variance represented; |z| ≥ 3 in 812 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +5.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +1.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.5 | +3.6 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +2.2 | +1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +0.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.5 | +1.4 |
|  | [[EX229 (drug)]] 5 µM |  | +1.3 | +2.4 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.3 | +2.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.2 | +2.4 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.8 | -8.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -6.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.4 | -4.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.3 | -6.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.2 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -2.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.8 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.8 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | parvin gamma |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.31 — chr22:44,172,956-44,219,533 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Parvins; ILK-PINCH-Parvin complex subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HBI0](https://www.uniprot.org/uniprotkb/Q9HBI0) (Gamma-parvin):

> Plays a role with ILK in promoting the cell adhesion and spreading of leukocytes.

**Summary**, from NCBI Gene [64098](https://www.ncbi.nlm.nih.gov/gene/64098):

> Members of the parvin family, including PARVG, are actin-binding proteins associated with focal contacts.[supplied by OMIM, Aug 2004]

**Accessions** — [HGNC:14654](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14654) · Entrez [64098](https://www.ncbi.nlm.nih.gov/gene/64098) · UniProt [Q9HBI0](https://www.uniprot.org/uniprotkb/Q9HBI0) · Ensembl [ENSG00000138964](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138964)

## Data

Gene col 6255: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6255); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6255, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6255]; `tensor/DDL_lfc|DDL_z.npy` [6255]; `embed/gene_vectors.npy` [6255]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6255 or target_col == 6255). Every well: [[PARVG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PARVG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
