---
symbol: "ATP10A"
type: "gene"
col: 13036
ensembl_id: "ENSG00000206190"
name: "ATPase phospholipid transporting 10A (putative)"
location: "15q12"
module: 167
arm: "+"
pooled_cpm: 23.12
n_lines_expressing: 25
n_dd_up: 6
n_dd_down: 31
n_dd_up_clean: 3
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 4
direction_downstream: 6
tags: ["gene", "module/167"]
generated_by: "tahoemap"
---

# ATP10A

*ATPase phospholipid transporting 10A (putative)* — 15q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.63× (z +13.2, q 6e-37, up in 0 of 22 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.55× (z +8.4, q 1e-14, up in 8 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.463× (z -14.9, q 0e+00, down in 23 of 23 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CP]] (+0.58, fdr 1e-05), [[TRPA1]] (+0.53, fdr 4e-05), [[ITIH2]] (+0.52, fdr 2e-04); moves opposite to [[VIPR1]] (-0.40, fdr 2e-04), [[TCFL5]] (-0.39, fdr 3e-04), [[ZDHHC11B]] (-0.39, fdr 3e-04).
> It is in [[Module 167]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CSGALNACT1]] → it (grade C ⚠); 6 go from it, the strongest it → [[GBP4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13036.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.63×** | +13.2 | 6e-37 | 0/22 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +8.4 | 1e-14 | 8/22 (NCI-H1573, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.88×** | +7.9 | 4e-13 | 3/19 (NCI-H1573, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.49×** | +3.9 | 0.014 | 1/21 (NCI-H460) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.075 | 10/22 (hTERT-HPNE, A549, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +3.3 | 0.093 | 6/23 (NCI-H2347, SK-MEL-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.28×** | +3.3 | 0.093 | 0/17 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 5 µM |  | 1.25× | +3.0 | 0.17 | 9/23 (CFPAC-1, HS-578T, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13036.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.463×** | -14.9 | 0e+00 | 23/23 (SK-MEL-2, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.421×** | -11.8 | 1e-29 | 19/23 (SW 900, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.428×** | -11.6 | 1e-28 | 21/23 (HepG2/C3A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.426×** | -11.2 | 6e-27 | 21/23 (A549, SW 900, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.451×** | -10.9 | 2e-25 | 20/22 (HepG2/C3A, A549, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.475×** | -10.1 | 3e-22 | 21/23 (A549, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.496×** | -9.6 | 9e-20 | 22/23 (HepG2/C3A, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.559×** | -7.9 | 2e-13 | 19/22 (NCI-H1792, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.614×** | -6.7 | 2e-09 | 15/22 (HepG2/C3A, A549, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.725×** | -6.2 | 3e-08 | 19/23 (NCI-H2347, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.676×** | -5.4 | 4e-06 | 17/23 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.711×** | -4.7 | 1e-04 | 16/22 (SNU-423, HepG2/C3A, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.716×** | -4.6 | 2e-04 | 13/23 (SK-MEL-2, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.735×** | -4.2 | 0.001 | 15/23 (SNU-423, HS-578T, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.746×** | -4.0 | 0.002 | 13/23 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.591×** | -3.7 | 0.006 | 11/22 (HepG2/C3A, H4, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13036. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 386 | 0 | 24 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -25.3) |
| [[A549 (line)]] | wt | 110 | 0 | 15 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0846× (z -25.5) |
| [[SNU-423 (line)]] | alt | 38.9 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -17.8) |
| [[SW480 (line)]] | alt | 16.6 | 0 | 9 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0996× (z -12.3) |
| [[A498 (line)]] | wt | 33.1 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.0832× (z -24.7) |
| [[HS-578T (line)]] | alt | 40.7 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -19.4) |
| [[NCI-H2030 (line)]] | alt | 75.2 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -23.3) |
| [[SK-MEL-2 (line)]] | alt | 55.7 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0280× (z -32.8) |
| [[SW 900 (line)]] | alt | 53.4 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -22.1) |
| [[SW1417 (line)]] | alt | 56.9 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.145× (z -12.0) |
| [[H4 (line)]] | wt | 19.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0879× (z -12.9) |
| [[NCI-H1792 (line)]] | alt | 20.4 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0325× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.0714× (z -13.2) |
| [[PANC-1 (line)]] | alt | 16.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -17.7) |
| [[CFPAC-1 (line)]] | alt | 41.0 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.306× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 14.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -13.8) |
| [[NCI-H2347 (line)]] | alt | 50.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -13.5) |
| [[NCI-H460 (line)]] | wt | 5.83 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.118× (z -11.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 19.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.221× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 15.2 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0889× (z -9.2) ⚠ cell-cycle shift, explains ~64% of this change |
| [[NCI-H1573 (line)]] | alt | 10.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -9.4) |
| [[A-172 (line)]] | wt | 2.02 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.50 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.13 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.94 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.81 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.71 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.29 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.14 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.88 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.07 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.41 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13036), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CP]] | +0.58 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[TRPA1]] | +0.53 | +0.42 / +0.49 | both halves | 4e-05 | pathway: Ion channel transport |
| [[ITIH2]] | +0.52 | +0.51 / +0.29 | both halves | 2e-04 |  |
| [[IDO1]] | +0.51 | +0.35 / +0.58 | both halves | 1e-04 |  |
| [[CXCL10]] | +0.50 | +0.39 / +0.51 | both halves | 6e-05 |  |
| [[CD38]] | +0.50 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[ITIH5]] | +0.50 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[PREX2]] | +0.48 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[IGFBP1]] | +0.48 | +0.45 / +0.39 | both halves | 5e-05 |  |
| [[TIMD4]] | +0.48 | +0.40 / +0.47 | both halves | 5e-05 |  |
| [[C1R]] | +0.47 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[LAP3]] | +0.46 | +0.28 / +0.59 | both halves | 3e-04 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VIPR1]] | -0.40 | -0.32 / -0.39 | both halves | 2e-04 |  |
| [[TCFL5]] | -0.39 | -0.28 / -0.40 | both halves | 3e-04 |  |
| [[ZDHHC11B]] | -0.39 | -0.27 / -0.44 | both halves | 3e-04 |  |
| [[NEFM]] | -0.39 | -0.36 / -0.28 | both halves | 3e-04 |  |
| [[SLC38A4]] | -0.36 | -0.44 / -0.30 | both halves | 2e-04 |  |
| [[FGFR2]] | -0.36 | -0.28 / -0.31 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CSGALNACT1]] | C | CSGALNACT1 activity raises ATP10A's level | lines that do not express CSGALNACT1 (25) vs lines expressing it (25) | 3.58× lower at baseline in the lines without CSGALNACT1 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: BCL2A1, ATP10A, FGF14; co-absent with the target |
| [[CYP24A1]] | C | CYP24A1 activity raises ATP10A's level | lines that do not express CYP24A1 (39) vs lines expressing it (11) | 5.16× lower at baseline in the lines without CYP24A1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, S100A9, FGG; co-absent with the target |
| [[FGA]] | C | FGA activity raises ATP10A's level | lines that do not express FGA (43) vs lines expressing it (7) | 5.11× lower at baseline in the lines without FGA | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, ITIH2, FGG; co-absent with the target |
| [[CP]] | C | CP activity raises ATP10A's level | lines that do not express CP (39) vs lines expressing it (11) | 5.57× lower at baseline in the lines without CP | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ITIH2, BHMT2, APOB; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 1, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GBP4]] | B | ATP10A activity raises GBP4's level | lines that do not express ATP10A (25) vs lines expressing it (25) | 2.25× lower at baseline in the lines without ATP10A | 0.093 | ⚠ within organs, on part of the lines; also absent: STAC, SALL1, TGFBI |
| [[CSGALNACT1]] | C | ATP10A activity raises CSGALNACT1's level | lines that do not express ATP10A (25) vs lines expressing it (25) | 4.29× lower at baseline in the lines without ATP10A | 0.005 | ⚠ within organs, on part of the lines; also absent: STAC, SALL1, TGFBI; co-absent with the target |
| [[BICC1]] | C | ATP10A activity raises BICC1's level | lines that do not express ATP10A (25) vs lines expressing it (25) | 3.90× lower at baseline in the lines without ATP10A | 0.053 | ⚠ within organs, on part of the lines; also absent: STAC, SALL1, TGFBI; co-absent with the target |
| [[CYP24A1]] | C | ATP10A activity raises CYP24A1's level | lines that do not express ATP10A (25) vs lines expressing it (25) | 2.77× lower at baseline in the lines without ATP10A | 0.078 | ⚠ within organs, on part of the lines; also absent: STAC, SALL1, TGFBI; co-absent with the target |
| [[EDIL3]] | C | ATP10A activity raises EDIL3's level | lines that do not express ATP10A (25) vs lines expressing it (25) | 4.32× lower at baseline in the lines without ATP10A | 0.091 | ⚠ within organs, on part of the lines; also absent: STAC, SALL1, TGFBI; co-absent with the target |
| [[MSC]] | C | ATP10A activity raises MSC's level | lines that do not express ATP10A (25) vs lines expressing it (25) | 2.13× lower at baseline in the lines without ATP10A | 0.096 | ⚠ within organs, on part of the lines; also absent: STAC, SALL1, TGFBI; co-absent with the target |

## Where it sits

- **Module**: [[Module 167]]; 25 genes; every member is in the + arm (projection on the module's main direction 0.501). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.1, 44.9); signed map (53.0, 27.5). **Vector** length 79.4, 23.6% of its response variance represented; |z| ≥ 3 in 758 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +8.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +3.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +1.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +3.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.8 | +13.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.3 | +2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.3 | +3.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.2 | +0.2 |
| fall | [[Selinexor (drug)]] 5 µM |  | -4.8 | -6.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.4 | -4.2 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -2.9 | -4.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | -6.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.4 | -11.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.8 | -0.4 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.8 | -0.3 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.7 | -1.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | ATPase phospholipid transporting 10A (putative) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q12 — chr15:25,677,273-25,865,184 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ATPVA, ATPVC, KIAA0566; previously ATP10C |
| Gene groups (HGNC) | ATPase phospholipid transporting; MicroRNA protein coding host genes |
| Reactome | 3 pathways, smallest: Ion transport by P-type ATPases; Ion channel transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [O60312](https://www.uniprot.org/uniprotkb/O60312) (Phospholipid-transporting ATPase VA):

> Catalytic component of P4-ATPase flippase complex, which catalyzes the hydrolysis of ATP coupled to the transport of phosphatidylcholine (PC) from the outer to the inner leaflet of the plasma membrane. Initiates inward plasma membrane bending and recruitment of Bin/amphiphysin/Rvs (BAR) domain-containing proteins involved in membrane tubulation and cell trafficking. Facilitates ITGB1/beta1 integrin endocytosis, delaying cell adhesion and cell spreading on extracellular matrix. Has low flippase …

**Summary**, from NCBI Gene [57194](https://www.ncbi.nlm.nih.gov/gene/57194):

> The protein encoded by this gene belongs to the family of P-type cation transport ATPases, and to the subfamily of aminophospholipid-transporting ATPases. The aminophospholipid translocases transport phosphatidylserine and phosphatidylethanolamine from one side of a bilayer to another. This gene is maternally expressed. It maps within the most common interval of deletion responsible for Angelman syndrome, also known as 'happy puppet syndrome'. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:13542](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13542) · Entrez [57194](https://www.ncbi.nlm.nih.gov/gene/57194) · UniProt [O60312](https://www.uniprot.org/uniprotkb/O60312) · Ensembl [ENSG00000206190](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000206190)

## Data

Gene col 13036: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13036); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13036, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13036]; `tensor/DDL_lfc|DDL_z.npy` [13036]; `embed/gene_vectors.npy` [13036]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13036 or target_col == 13036). Every well: [[ATP10A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP10A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
