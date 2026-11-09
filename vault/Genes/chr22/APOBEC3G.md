---
symbol: "APOBEC3G"
type: "gene"
col: 14208
ensembl_id: "ENSG00000239713"
name: "apolipoprotein B mRNA editing enzyme catalytic subunit 3G"
location: "22q13.1"
module: 32
arm: "+"
pooled_cpm: 3.49
n_lines_expressing: 28
n_dd_up: 4
n_dd_down: 21
n_dd_up_clean: 2
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 3
direction_downstream: 7
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# APOBEC3G

*apolipoprotein B mRNA editing enzyme catalytic subunit 3G* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.83× (z +5.4, q 4e-05, up in 0 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[GSK1059615 (drug)]] 0.5 µM: 1.83× (z +4.0, q 0.017, up in 6 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.318× (z -10.6, q 2e-23, down in 20 of 24 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LMO2]] (+0.63, fdr 7e-06), [[APOL3]] (+0.63, fdr 3e-05), [[APOBEC3F]] (+0.61, fdr 1e-05, ⚠ same locus), [[AIM2]] (+0.60, fdr 1e-05); moves opposite to [[PKP2]] (-0.47, fdr 4e-05), [[TMEM181]] (-0.47, fdr 5e-05), [[APPL2]] (-0.46, fdr 1e-04).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HTR1F]] → it (grade C ⚠); 7 go from it, the strongest it → [[ZNF404]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14208.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.83×** | +5.4 | 4e-05 | 0/7 | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.83×** | +4.0 | 0.017 | 6/21 (HS-578T, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.80×** | +3.9 | 0.017 | 4/16 (NCI-H1792, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.71×** | +3.6 | 0.052 | 2/13 (NCI-H23, H4) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Oxaprozin (drug)]] 0.5 µM |  | 1.39× | +3.1 | 0.24 | 3/21 (SW 900, A-427, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.40× | +3.0 | 0.24 | 7/21 (Hs 766T, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14208.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.318×** | -10.6 | 2e-23 | 20/24 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.462×** | -10.1 | 2e-21 | 18/20 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.391×** | -8.7 | 7e-16 | 16/22 (H4, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.395×** | -8.6 | 1e-15 | 22/25 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.399×** | -8.5 | 2e-15 | 19/24 (HS-578T, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.424×** | -7.9 | 2e-13 | 18/22 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.444×** | -7.5 | 5e-12 | 16/23 (RPMI-7951, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.518×** | -5.8 | 4e-07 | 13/23 (A-172, HS-578T, …) | top dose only | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.617×** | -4.5 | 5e-04 | 13/23 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.620×** | -4.4 | 6e-04 | 8/23 (HS-578T, H4, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.624×** | -4.3 | 7e-04 | 13/20 (HS-578T, H4, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.418×** | -4.2 | 0.001 | 14/22 (Hs 766T, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.446×** | -3.9 | 0.004 | 9/23 (RPMI-7951, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.661×** | -3.8 | 0.006 | 14/18 (HOP62, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.647×** | -3.7 | 0.009 | 11/24 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.663×** | -3.5 | 0.017 | 10/24 (A-172, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.685×** | -3.5 | 0.017 | 12/20 (CFPAC-1, SNU-423, …) | all doses, flat |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.766×** | -3.5 | 0.017 | 8/23 (A-172, NCI-H1792, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.709×** | -3.2 | 0.047 | 9/23 (C32, A-172, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14208. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 13.6 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0473× (z -10.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Hydroxyurea (drug)]] 0.05 µM 0.0693× (z -9.0) |
| [[A-172 (line)]] | wt | 13.8 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -16.3) |
| [[HS-578T (line)]] | alt | 8.56 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0891× (z -11.0) |
| [[HOP62 (line)]] | alt | 5.82 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0494× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.237× (z -9.1) |
| [[Hs 766T (line)]] | wt | 19.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -14.6) |
| [[MIA PaCa-2 (line)]] | alt | 3.84 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0540× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.0622× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 9.80 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0662× (z -9.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0787× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 10.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -13.1) |
| [[SW480 (line)]] | alt | 5.51 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0965× (z -16.4) |
| [[C32 (line)]] | wt | 5.23 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.0733× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 8.78 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -8.7) |
| [[PANC-1 (line)]] | alt | 4.07 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0786× (z -11.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.436 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.388 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.568 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.908 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.308 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.360 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.544 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.611 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.385 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.526 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.370 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.12 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.649 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.972 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.408 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.390 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.562 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.319 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.512 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.456 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.302 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.280 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.377 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.498 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.397 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14208), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LMO2]] | +0.63 | +0.59 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[APOL3]] | +0.63 | +0.43 / +0.76 | both halves | 3e-05 |  |
| [[APOBEC3F]] | +0.61 | +0.53 / +0.73 | both halves | 1e-05 | same gene group; pathway: HALLMARK_COMPLEMENT; STRING 933; ⚠ same locus (21.1 kb, same strand: neighbours can correlate without regulation) |
| [[AIM2]] | +0.60 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[MXRA5]] | +0.59 | +0.60 / +0.51 | both halves | 1e-05 | **novel candidate** |
| [[CHROMR]] | +0.55 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[BTN3A3]] | +0.54 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[BST2]] | +0.52 | +0.41 / +0.63 | both halves | 4e-05 | STRING 943 |
| [[STING1]] | +0.52 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[STRA6]] | +0.51 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[CAVIN3]] | +0.51 | +0.51 / +0.37 | both halves | 8e-05 |  |
| [[GRIP2]] | +0.51 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[ARMCX2]] | +0.50 | +0.48 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKP2]] | -0.47 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[TMEM181]] | -0.47 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[APPL2]] | -0.46 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[CPS1]] | -0.44 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[MYO5C]] | -0.42 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[STK39]] | -0.42 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[ARHGEF28]] | -0.41 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[SLC20A2]] | -0.41 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[NR2E3]] | -0.40 | -0.34 / -0.36 | both halves | 1e-04 |  |
| [[B3GALT1]] | -0.40 | -0.41 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HTR1F]] | C | HTR1F activity raises APOBEC3G's level | lines that do not express HTR1F (34) vs lines expressing it (16) | 2.89× lower at baseline in the lines without HTR1F | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MGP, TIMP3, AEBP1; maybe low, not absent; co-absent with the target |
| [[ADAMTS14]] | C | ADAMTS14 activity raises APOBEC3G's level | lines that do not express ADAMTS14 (31) vs lines expressing it (19) | 2.23× lower at baseline in the lines without ADAMTS14 | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000287335, CARD11, LINC01411; co-absent with the target |
| [[MXRA5]] | C | MXRA5 activity raises APOBEC3G's level | lines that do not express MXRA5 (34) vs lines expressing it (16) | 2.55× lower at baseline in the lines without MXRA5 | 0.067 | ⚠ within organs, on part of the lines; also absent: IRAG2, VCAM1, LINC02476; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF404]] | B | APOBEC3G activity raises ZNF404's level | lines that do not express APOBEC3G (22) vs lines expressing it (28) | 3.95× lower at baseline in the lines without APOBEC3G | 0.003 | ⚠ within organs, on part of the lines; also absent: LINC02813, PTX3, PDLIM3 |
| [[BOC]] | B | APOBEC3G activity raises BOC's level | lines that do not express APOBEC3G (22) vs lines expressing it (28) | 1.43× lower at baseline in the lines without APOBEC3G | 0.034 | ⚠ within organs, on part of the lines; also absent: LINC02813, PTX3, PDLIM3 |
| [[MANCR]] | B | APOBEC3G activity raises MANCR's level | lines that do not express APOBEC3G (22) vs lines expressing it (28) | 2.74× lower at baseline in the lines without APOBEC3G | 0.071 | ⚠ within organs, on part of the lines; also absent: LINC02813, PTX3, PDLIM3 |
| [[CHROMR]] | B | APOBEC3G activity raises CHROMR's level | lines that do not express APOBEC3G (22) vs lines expressing it (28) | 2.41× lower at baseline in the lines without APOBEC3G | 0.078 | ⚠ within organs, on part of the lines; also absent: LINC02813, PTX3, PDLIM3 |
| [[THBS2-AS1]] | B | APOBEC3G activity raises THBS2-AS1's level | lines that do not express APOBEC3G (22) vs lines expressing it (28) | 1.36× lower at baseline in the lines without APOBEC3G | 0.086 | ⚠ within organs, on part of the lines; also absent: LINC02813, PTX3, PDLIM3 |
| [[CPNE5]] | B | APOBEC3G activity raises CPNE5's level | lines that do not express APOBEC3G (22) vs lines expressing it (28) | 1.72× lower at baseline in the lines without APOBEC3G | 0.097 | ⚠ within organs, on part of the lines; also absent: LINC02813, PTX3, PDLIM3 |
| [[CAVIN3]] | C | APOBEC3G activity raises CAVIN3's level | lines that do not express APOBEC3G (22) vs lines expressing it (28) | 2.51× lower at baseline in the lines without APOBEC3G | 0.022 | ⚠ within organs, on part of the lines; also absent: LINC02813, PTX3, PDLIM3; co-absent with the target |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.428). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.9, 51.5); signed map (59.2, 31.3). **Vector** length 54.5, 13.1% of its response variance represented; |z| ≥ 3 in 589 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.3 | +1.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.8 | +2.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.2 | +1.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +1.2 | +1.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.2 | +0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.2 | +0.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +0.9 | +2.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +0.8 | +1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.8 | -2.4 |
|  | [[Docetaxel (drug)]] 5 µM |  | +0.7 | +1.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -8.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.0 | -7.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.7 | -8.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.6 | -3.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.6 | -3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.3 | -2.5 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.3 | -2.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.2 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | apolipoprotein B mRNA editing enzyme catalytic subunit 3G |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:39,077,067-39,087,743 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CEM15, MDS019, dJ494G10.1, FLJ12740, bK150C2.7 |
| Gene groups (HGNC) | Apolipoprotein B mRNA editing enzyme catalytic subunits |
| Hallmark sets | COMPLEMENT |
| Reactome | 5 pathways, smallest: APOBEC3G mediated resistance to HIV-1 infection; Vif-mediated degradation of APOBEC3G; Host Interactions of HIV factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HC16](https://www.uniprot.org/uniprotkb/Q9HC16) (DNA dC->dU-editing enzyme APOBEC-3G):

> DNA deaminase (cytidine deaminase) which acts as an inhibitor of retrovirus replication and retrotransposon mobility via deaminase-dependent and -independent mechanisms. Exhibits potent antiviral activity against Vif-deficient HIV-1. After the penetration of retroviral nucleocapsids into target cells of infection and the initiation of reverse transcription, it can induce the conversion of cytosine to uracil in the minus-sense single-strand viral DNA, leading to G-to-A hypermutations in the …

**Summary**, from NCBI Gene [60489](https://www.ncbi.nlm.nih.gov/gene/60489):

> This gene is a member of the cytidine deaminase gene family. It is one of seven related genes or pseudogenes found in a cluster, thought to result from gene duplication, on chromosome 22. Members of the cluster encode proteins that are structurally and functionally related to the C to U RNA-editing cytidine deaminase APOBEC1. The protein encoded by this gene catalyzes site-specific deamination of both RNA and single-stranded DNA. The encoded protein has been found to be a specific inhibitor of …

**Accessions** — [HGNC:17357](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17357) · Entrez [60489](https://www.ncbi.nlm.nih.gov/gene/60489) · UniProt [Q9HC16](https://www.uniprot.org/uniprotkb/Q9HC16) · Ensembl [ENSG00000239713](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000239713)

## Data

Gene col 14208: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14208); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14208, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14208]; `tensor/DDL_lfc|DDL_z.npy` [14208]; `embed/gene_vectors.npy` [14208]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14208 or target_col == 14208). Every well: [[APOBEC3G — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APOBEC3G.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
