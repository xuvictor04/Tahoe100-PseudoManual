---
symbol: "AJAP1"
type: "gene"
col: 12241
ensembl_id: "ENSG00000196581"
name: "adherens junctions associated protein 1"
location: "1p36.32"
module: 116
arm: "+"
pooled_cpm: 6.2
n_lines_expressing: 10
n_dd_up: 46
n_dd_down: 5
n_dd_up_clean: 27
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 7
direction_downstream: 2
tags: ["gene", "module/116"]
generated_by: "tahoemap"
---

# AJAP1

*adherens junctions associated protein 1* — 1p36.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 46 drug-doses (19 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.59× (z +11.6, q 3e-28, up in 1 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.23× (z +8.6, q 2e-15, up in 3 of 7 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Rutin (trihydrate) (drug)]] 0.05 µM: 0.566× (z -4.1, q 0.028, down in 0 of 7 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NAV3]] (+0.70, fdr 1e-05), [[INHBA]] (+0.60, fdr 1e-05), [[IL31RA]] (+0.60, fdr 3e-05); moves opposite to [[TSC22D3]] (-0.46, fdr 1e-04), [[DHRS3]] (-0.46, fdr 4e-05), [[LPCAT3]] (-0.43, fdr 2e-04).
> It is in [[Module 116]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[SERPINB2]] → it (grade C ⚠); 2 go from it, the strongest it → [[DSCAM]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 19 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 46 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12241.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.59×** | +11.6 | 3e-28 | 1/6 (RPMI-7951) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.76×** | +11.4 | 1e-27 | 0/6 | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.83×** | +11.1 | 4e-26 | 3/6 (RPMI-7951, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.23×** | +8.6 | 2e-15 | 3/7 (NCI-H23, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.15×** | +8.2 | 3e-14 | 5/7 (RPMI-7951, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.58×** | +7.2 | 7e-11 | 5/7 (NCI-H1573, SNU-423, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.24×** | +6.1 | 9e-08 | 4/7 (SNU-423, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.23×** | +5.8 | 4e-07 | 2/7 (NCI-H1573, RPMI-7951) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.22×** | +5.7 | 7e-07 | 1/7 (NCI-H1573) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.17×** | +5.6 | 1e-06 | 5/6 (SNU-423, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.91×** | +5.4 | 3e-06 | 4/7 (RPMI-7951, NCI-H1573, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.81×** | +5.3 | 5e-06 | 3/5 (NCI-H1573, H4, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.63×** | +5.2 | 7e-06 | 6/7 (NCI-H1573, H4, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.90×** | +4.8 | 5e-05 | 3/7 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.90×** | +4.8 | 5e-05 | 4/7 (NCI-H1573, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.84×** | +4.6 | 1e-04 | 4/7 (RPMI-7951, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.78×** | +4.3 | 5e-04 | 3/7 (NCI-H1573, SNU-423, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.77×** | +4.3 | 5e-04 | 4/7 (SNU-423, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.14×** | +4.1 | 0.001 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.47×** | +4.1 | 0.001 | 4/7 (NCI-H1573, RPMI-7951, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.47×** | +4.1 | 0.001 | 2/7 (NCI-H23, HEC-1-A) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.70×** | +4.0 | 0.002 | 3/7 (NCI-H1573, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.97×** | +3.6 | 0.006 | 2/7 (NCI-H1573, SNU-423) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12241.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.566×** | -4.1 | 0.028 | 0/7 | inconsistent across doses |  |
| [[Tirabrutinib (drug)]] 0.05 µM |  | **0.614×** | -3.5 | 0.099 | 0/7 | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.640×** | -3.4 | 0.099 | 0/7 | two highest doses |  |
| [[Trametinib (drug)]] 5 µM |  | **0.623×** | -3.3 | 0.099 | 2/7 (NCI-H1573, H4) | top dose only | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 0.05 µM |  | **0.633×** | -3.3 | 0.099 | 0/7 | inconsistent across doses |  |
| [[Sulfatinib (drug)]] 0.5 µM |  | 0.662× | -3.2 | 0.13 | 0/7 | inconsistent across doses |  |
| [[Ciclopirox (drug)]] 0.5 µM |  | 0.668× | -3.1 | 0.14 | 0/7 | inconsistent across doses |  |
| [[Captopril (drug)]] 0.05 µM |  | 0.675× | -3.0 | 0.15 | 0/7 | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.655× | -3.0 | 0.15 | 0/7 | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.656× | -3.0 | 0.15 | 2/7 (NCI-H1573, NCI-H23) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12241. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 50.3 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 15.9× (z +11.1) | — |
| [[RPMI-7951 (line)]] | alt | 58.4 | 4 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 11.3× (z +11.8) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.45× (z +9.4) | — |
| [[H4 (line)]] | wt | 107 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -11.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 0.588 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.474 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.476 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.927 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.667 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.551 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.553 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.745 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.567 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.613 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.634 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.679 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.465 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.725 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.687 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.804 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.478 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.548 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.693 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 75.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.565 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.401 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.449 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.485 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.524 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.778 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.445 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.437 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.577 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.506 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.597 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.665 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.708 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.734 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.581 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.691 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.536 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12241), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAV3]] | +0.70 | +0.55 / +0.75 | both halves | 1e-05 |  |
| [[INHBA]] | +0.60 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[IL31RA]] | +0.60 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[EVA1A]] | +0.57 | +0.38 / +0.59 | both halves | 7e-05 |  |
| [[MARCHF4]] | +0.57 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[TFPI2]] | +0.57 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[TBILA]] | +0.56 | +0.40 / +0.56 | both halves | 4e-05 |  |
| [[FGF5]] | +0.56 | +0.46 / +0.60 | both halves | 3e-05 |  |
| [[FRMD6]] | +0.55 | +0.46 / +0.65 | both halves | 3e-05 |  |
| [[CXCL8]] | +0.55 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[ADTRP]] | +0.55 | +0.34 / +0.67 | both halves | 1e-04 |  |
| [[ADAMTSL1]] | +0.53 | +0.44 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSC22D3]] | -0.46 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[DHRS3]] | -0.46 | -0.43 / -0.44 | both halves | 4e-05 |  |
| [[LPCAT3]] | -0.43 | -0.30 / -0.38 | both halves | 2e-04 |  |
| [[DYNC2I1]] | -0.42 | -0.33 / -0.45 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SERPINB2]] | C | SERPINB2 activity raises AJAP1's level | lines that do not express SERPINB2 (36) vs lines expressing it (14) | 3.91× lower at baseline in the lines without SERPINB2 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000254337, TMPRSS15, LINC00824; co-absent with the target |
| [[INHBA]] | C | INHBA activity raises AJAP1's level | lines that do not express INHBA (32) vs lines expressing it (18) | 3.07× lower at baseline in the lines without INHBA | 0.048 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, DSCAM, TNIP3; co-absent with the target |
| [[DSCAM]] | C | DSCAM activity raises AJAP1's level | lines that do not express DSCAM (37) vs lines expressing it (13) | 3.99× lower at baseline in the lines without DSCAM | 0.069 | ⚠ within organs, on part of the lines; also absent: CGA, RIT2, LINC01456; maybe low, not absent; co-absent with the target |
| [[COLEC10]] | C | COLEC10 activity raises AJAP1's level | lines that do not express COLEC10 (31) vs lines expressing it (19) | 2.38× lower at baseline in the lines without COLEC10 | 0.085 | ⚠ within organs, on part of the lines; also absent: CCK, TRIM55, AJAP1; co-absent with the target |
| [[LY6K]] | C | LY6K activity raises AJAP1's level | lines that do not express LY6K (32) vs lines expressing it (18) | 2.21× lower at baseline in the lines without LY6K | 0.086 | ⚠ within organs, on part of the lines; also absent: IL6, STEAP1B-AS1, TNIP3; co-absent with the target |
| [[LINC01605]] | C | LINC01605 activity raises AJAP1's level | lines that do not express LINC01605 (27) vs lines expressing it (23) | 1.74× lower at baseline in the lines without LINC01605 | 0.096 | ⚠ within organs, on part of the lines; also absent: LINC00460, LINC01133, PTPRR; co-absent with the target |
| [[ADTRP]] | C | ADTRP activity raises AJAP1's level | lines that do not express ADTRP (25) vs lines expressing it (25) | 2.56× lower at baseline in the lines without ADTRP | 0.097 | ⚠ within organs, on part of the lines; also absent: LINC02725, ROBO4, AIM2; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DSCAM]] | C | AJAP1 activity raises DSCAM's level | lines that do not express AJAP1 (40) vs lines expressing it (10) | 3.09× lower at baseline in the lines without AJAP1 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMPRSS15, ENSG00000230972, LINC01425; co-absent with the target |
| [[PLAU]] | C | AJAP1 activity raises PLAU's level | lines that do not express AJAP1 (40) vs lines expressing it (10) | 2.18× lower at baseline in the lines without AJAP1 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMPRSS15, ENSG00000230972, LINC01425; co-absent with the target |

## Where it sits

- **Module**: [[Module 116]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.620). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (44.2, 12.0); signed map (15.1, 44.1). **Vector** length 29.9, 9.83% of its response variance represented; |z| ≥ 3 in 249 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.8 | +11.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +7.2 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.2 | +2.2 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.2 | +3.6 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -2.5 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -0.9 | -0.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -0.9 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.8 | -3.0 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -0.8 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | adherens junctions associated protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.32 — chr1:4,654,609-4,792,534 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SHREW1, SHREW-1, MOT8 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKB5](https://www.uniprot.org/uniprotkb/Q9UKB5) (Adherens junction-associated protein 1):

> Plays a role in cell adhesion and cell migration.

**Summary**, from NCBI Gene [55966](https://www.ncbi.nlm.nih.gov/gene/55966):

> Enables beta-catenin binding activity. Involved in negative regulation of cell-matrix adhesion; negative regulation of wound healing; and regulation of polarized epithelial cell differentiation. Located in several cellular components, including adherens junction; basolateral plasma membrane; and cell-cell contact zone. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30801](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30801) · Entrez [55966](https://www.ncbi.nlm.nih.gov/gene/55966) · UniProt [Q9UKB5](https://www.uniprot.org/uniprotkb/Q9UKB5) · Ensembl [ENSG00000196581](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196581)

## Data

Gene col 12241: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12241); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12241, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12241]; `tensor/DDL_lfc|DDL_z.npy` [12241]; `embed/gene_vectors.npy` [12241]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12241 or target_col == 12241). Every well: [[AJAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AJAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
