---
symbol: "BATF2"
type: "gene"
col: 9590
ensembl_id: "ENSG00000168062"
name: "basic leucine zipper ATF-like transcription factor 2"
location: "11q13.1"
module: 32
arm: "+"
pooled_cpm: 4.52
n_lines_expressing: 37
n_dd_up: 12
n_dd_down: 35
n_dd_up_clean: 10
n_dd_down_clean: 30
in_vector_space: true
direction_upstream: 19
direction_downstream: 81
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# BATF2

*basic leucine zipper ATF-like transcription factor 2* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 0.5 µM: 2.48× (z +7.4, q 1e-10, up in 18 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (5 with an alert ⚠); the strongest is [[Tofacitinib (citrate) (drug)]] 5 µM: 0.467× (z -8.6, q 4e-15, down in 26 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MX1]] (+0.89, fdr 7e-06), [[OAS1]] (+0.89, fdr 7e-06), [[CMPK2]] (+0.88, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[OAS1]] → it (grade B ⚠); 81 go from it, the strongest it → [[PARP9]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9590.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.48×** | +7.4 | 1e-10 | 18/31 (NCI-H2347, A498, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **2.14×** | +6.1 | 2e-07 | 17/32 (NCI-H2347, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.04×** | +5.8 | 2e-06 | 20/32 (NCI-H2347, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +5.1 | 5e-05 | 1/6 (SW1417) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.85×** | +5.0 | 7e-05 | 13/27 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.61×** | +3.7 | 0.021 | 14/29 (AsPC-1, KATO III, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.61×** | +3.7 | 0.021 | 11/31 (CFPAC-1, LS 180, …) | inconsistent across doses | position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.38×** | +3.6 | 0.023 | 5/32 (AsPC-1, LoVo, …) | all doses, flat |  |
| [[venetoclax (drug)]] 0.05 µM |  | **1.57×** | +3.5 | 0.032 | 5/31 (LoVo, CFPAC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.50×** | +3.3 | 0.057 | 12/31 (A-172, NCI-H2347, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +3.1 | 0.096 | 4/20 (NCI-H2347, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.46×** | +3.1 | 0.096 | 6/32 (CFPAC-1, NCI-H1792, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.48× | +3.0 | 0.10 | 8/31 (A498, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9590.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.467×** | -8.6 | 4e-15 | 26/32 (RKO, A549, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.472×** | -8.5 | 4e-15 | 25/31 (MIA PaCa-2, COLO 205, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.364×** | -8.1 | 9e-14 | 23/33 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.371×** | -8.0 | 2e-13 | 23/30 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.389×** | -7.6 | 4e-12 | 24/29 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.379×** | -7.4 | 2e-11 | 21/30 (NCI-H23, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.415×** | -7.1 | 1e-10 | 21/32 (MIA PaCa-2, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.423×** | -6.9 | 4e-10 | 22/31 (PANC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.448×** | -6.4 | 8e-09 | 22/32 (NCI-H23, SNU-423, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.449×** | -6.4 | 8e-09 | 19/30 (A549, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.479×** | -5.9 | 2e-07 | 23/32 (MIA PaCa-2, NCI-H1573, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.478×** | -5.7 | 6e-07 | 16/21 (NCI-H1573, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.559×** | -4.7 | 1e-04 | 16/33 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.586×** | -4.3 | 8e-04 | 12/33 (BT-474, LoVo, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.689×** | -4.2 | 1e-03 | 16/31 (A498, CFPAC-1, …) | rises with dose | position effect removed |
| [[Ixazomib (drug)]] 0.05 µM |  | **0.607×** | -3.8 | 0.005 | 10/28 (PANC-1, SHP-77, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9590. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 13.7 | 0 | 9 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0431× (z -12.4) |
| [[A549 (line)]] | wt | 10.7 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0708× (z -14.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tofacitinib (citrate) (drug)]] 5 µM 0.172× (z -9.7) |
| [[COLO 205 (line)]] | alt | 29.4 | 0 | 5 | — | [[Auranofin (drug)]] 5 µM 0.0479× (z -11.4) |
| [[NCI-H23 (line)]] | alt | 7.71 | 0 | 5 | — | [[Bortezomib (drug)]] 0.05 µM 0.0219× (z -12.5) |
| [[NCI-H2347 (line)]] | alt | 9.03 | 3 | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 22.2× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.0841× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.254× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 19.1 | 2 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 8.65× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.108× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 7.56 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0336× (z -13.1) |
| [[RKO (line)]] | wt | 5.84 | 0 | 3 | — | [[Tofacitinib (citrate) (drug)]] 5 µM 0.0659× (z -11.1) |
| [[BT-474 (line)]] | alt | 4.52 | 0 | 2 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.0653× (z -9.3) |
| [[PANC-1 (line)]] | alt | 2.11 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0361× (z -12.7) |
| [[SNU-423 (line)]] | alt | 7.33 | 0 | 2 | — | [[Bortezomib (drug)]] 0.05 µM 0.0297× (z -10.4) |
| [[A-172 (line)]] | wt | 3.48 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 25.2× (z +9.4) | — |
| [[NCI-H1573 (line)]] | alt | 5.49 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0520× (z -9.9) ⚠ toxic |
| [[SW1417 (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0906× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.711 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.74 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.626 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.627 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.761 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.993 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.537 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.525 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.762 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.477 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.754 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9590), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MX1]] | +0.89 | +0.81 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 418 |
| [[OAS1]] | +0.89 | +0.81 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 430 |
| [[CMPK2]] | +0.88 | +0.80 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 456 |
| [[STAT1]] | +0.88 | +0.83 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 545 |
| [[SP110]] | +0.87 | +0.81 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[USP18]] | +0.87 | +0.79 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 415 |
| [[PARP9]] | +0.87 | +0.77 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 558 |
| [[RSAD2]] | +0.86 | +0.81 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 551 |
| [[OAS2]] | +0.86 | +0.78 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 444 |
| [[RIGI]] | +0.86 | +0.81 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 424 |
| [[IFI44]] | +0.86 | +0.78 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[IFIT1]] | +0.86 | +0.78 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 18, C 1. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OAS1]] | B | OAS1 activity raises BATF2's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 2.30× lower at baseline in the lines without OAS1 | 0.005 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[SRMS]] | B | SRMS activity raises BATF2's level | lines that do not express SRMS (14) vs lines expressing it (36) | 2.11× lower at baseline in the lines without SRMS | 0.007 | ⚠ within organs, on part of the lines; also absent: MX1, OAS2, RSAD2 |
| [[OAS2]] | B | OAS2 activity raises BATF2's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 2.15× lower at baseline in the lines without OAS2 | 0.007 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[IFI6]] | B | IFI6 activity raises BATF2's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 2.22× lower at baseline in the lines without IFI6 | 0.010 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[PARP9]] | B | PARP9 activity raises BATF2's level | lines that do not express PARP9 (7) vs lines expressing it (43) | 2.35× lower at baseline in the lines without PARP9 | 0.019 | ⚠ within organs, on part of the lines; also absent: PLSCR1, OAS3, SRMS; maybe low, not absent |
| [[PLSCR1]] | B | PLSCR1 activity raises BATF2's level | lines that do not express PLSCR1 (8) vs lines expressing it (42) | 2.33× lower at baseline in the lines without PLSCR1 | 0.019 | ⚠ within organs, on part of the lines; also absent: PARP9, ENSG00000279320, IFI6; maybe low, not absent |
| [[CMPK2]] | B | CMPK2 activity raises BATF2's level | lines that do not express CMPK2 (11) vs lines expressing it (39) | 2.17× lower at baseline in the lines without CMPK2 | 0.023 | ⚠ within organs, on part of the lines; also absent: OAS2, NRIR, OAS1 |
| [[IFI27]] | B | IFI27 activity raises BATF2's level | lines that do not express IFI27 (21) vs lines expressing it (29) | 2.01× lower at baseline in the lines without IFI27 | 0.028 | ⚠ within organs, on part of the lines; also absent: TRIM22, OAS2, RSAD2 |
| [[RASGRP3]] | B | RASGRP3 activity raises BATF2's level | lines that do not express RASGRP3 (16) vs lines expressing it (34) | 2.03× lower at baseline in the lines without RASGRP3 | 0.033 | ⚠ within organs, on part of the lines; also absent: IFI6, SLC15A3, GBP4; maybe low, not absent |
| [[FBXO39]] | B | FBXO39 activity raises BATF2's level | lines that do not express FBXO39 (16) vs lines expressing it (34) | 1.78× lower at baseline in the lines without FBXO39 | 0.033 | ⚠ within organs, on part of the lines; also absent: XAF1, TRIM22, SLC15A3 |
| [[TRIM22]] | B | TRIM22 activity raises BATF2's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 1.99× lower at baseline in the lines without TRIM22 | 0.040 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[MX1]] | B | MX1 activity raises BATF2's level | lines that do not express MX1 (19) vs lines expressing it (31) | 1.90× lower at baseline in the lines without MX1 | 0.043 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |

### Downstream of this gene

*81 arrows, 81 of them with an alert ⚠; grade A 0, B 81, C 0. Shown: the 12 strongest; 69 more arrows (69 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PARP9]] | B | BATF2 activity raises PARP9's level | lines that do not express BATF2 (13) vs lines expressing it (37) | 2.61× lower at baseline in the lines without BATF2 | 0.001 | ⚠ within organs, on part of the lines; also absent: RSAD2; maybe low, not absent |
| [[OAS3]] | B | BATF2 activity raises OAS3's level | lines that do not express BATF2 (13) vs lines expressing it (37) | 2.67× lower at baseline in the lines without BATF2 | 0.001 | ⚠ within organs, on part of the lines; also absent: RSAD2; maybe low, not absent |
| [[IRF9]] | B | BATF2 activity raises IRF9's level | lines that do not express BATF2 (13) vs lines expressing it (37) | 2.10× lower at baseline in the lines without BATF2 | 0.001 | ⚠ within organs, on part of the lines; also absent: RSAD2; maybe low, not absent |
| [[PARP10]] | B | BATF2 activity raises PARP10's level | lines that do not express BATF2 (13) vs lines expressing it (37) | 1.95× lower at baseline in the lines without BATF2 | 0.001 | ⚠ within organs, on part of the lines; also absent: RSAD2; maybe low, not absent |
| [[UNC93B1]] | B | BATF2 activity raises UNC93B1's level | lines that do not express BATF2 (13) vs lines expressing it (37) | 1.89× lower at baseline in the lines without BATF2 | 0.001 | ⚠ within organs, on part of the lines; also absent: RSAD2; maybe low, not absent |
| [[EIF2AK2]] | B | BATF2 activity raises EIF2AK2's level | lines that do not express BATF2 (13) vs lines expressing it (37) | 2.01× lower at baseline in the lines without BATF2 | 0.002 | ⚠ within organs, on part of the lines; also absent: RSAD2; maybe low, not absent |
| [[REC8]] | B | BATF2 activity raises REC8's level | lines that do not express BATF2 (13) vs lines expressing it (37) | 1.89× lower at baseline in the lines without BATF2 | 0.002 | ⚠ within organs, on part of the lines; also absent: RSAD2; maybe low, not absent |
| [[HELZ2]] | B | BATF2 activity raises HELZ2's level | lines that do not express BATF2 (13) vs lines expressing it (37) | 2.09× lower at baseline in the lines without BATF2 | 0.002 | ⚠ within organs, on part of the lines; also absent: RSAD2; maybe low, not absent |
| [[IFI6]] | B | BATF2 activity raises IFI6's level | lines that do not express BATF2 (13) vs lines expressing it (37) | 2.65× lower at baseline in the lines without BATF2 | 0.003 | ⚠ within organs, on part of the lines; also absent: RSAD2; maybe low, not absent |
| [[SHFL]] | B | BATF2 activity raises SHFL's level | lines that do not express BATF2 (13) vs lines expressing it (37) | 1.68× lower at baseline in the lines without BATF2 | 0.003 | ⚠ within organs, on part of the lines; also absent: RSAD2; maybe low, not absent |
| [[SP110]] | B | BATF2 activity raises SP110's level | lines that do not express BATF2 (13) vs lines expressing it (37) | 2.29× lower at baseline in the lines without BATF2 | 0.004 | ⚠ within organs, on part of the lines; also absent: RSAD2; maybe low, not absent |
| [[PLSCR1]] | B | BATF2 activity raises PLSCR1's level | lines that do not express BATF2 (13) vs lines expressing it (37) | 2.56× lower at baseline in the lines without BATF2 | 0.005 | ⚠ within organs, on part of the lines; also absent: RSAD2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.904). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.2, 53.7); signed map (65.5, 31.3). **Vector** length 103, 28.4% of its response variance represented; |z| ≥ 3 in 1,013 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon* (control, mean cos +0.83 to 23); *Interferon Signaling* (reactome, mean cos +0.78 to 45); *Interferon alpha/beta signaling* (reactome, mean cos +0.81 to 27).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +6.6 | +5.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.2 | +5.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.9 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.5 | +3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +3.2 | +6.1 |
|  | [[Docetaxel (drug)]] 5 µM |  | +2.5 | +2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +3.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +2.8 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -6.4 | -8.5 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -5.5 | -8.6 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -5.3 | -7.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -5.3 | -8.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.7 | -5.9 |

## What is on record

|  |  |
|---|---|
| Name | basic leucine zipper ATF-like transcription factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:64,987,945-64,997,018 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC20410, SARI |
| Gene groups (HGNC) | Basic leucine zipper ATF-like transcription factor family |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, INTERFERON_GAMMA_RESPONSE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N1L9](https://www.uniprot.org/uniprotkb/Q8N1L9) (Basic leucine zipper transcriptional factor ATF-like 2):

> AP-1 family transcription factor that controls the differentiation of lineage-specific cells in the immune system. Following infection, participates in the differentiation of CD8(+) thymic conventional dendritic cells in the immune system. Acts via the formation of a heterodimer with JUN family proteins that recognizes and binds DNA sequence 5'-TGA[CG]TCA-3' and regulates expression of target genes (By similarity). Selectively suppresses CCN1 transcription and hence blocks the downstream cell …

**Summary**, from NCBI Gene [116071](https://www.ncbi.nlm.nih.gov/gene/116071):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in defense response to protozoan; myeloid dendritic cell differentiation; and regulation of transcription by RNA polymerase II. Predicted to be located in chromatin. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25163](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25163) · Entrez [116071](https://www.ncbi.nlm.nih.gov/gene/116071) · UniProt [Q8N1L9](https://www.uniprot.org/uniprotkb/Q8N1L9) · Ensembl [ENSG00000168062](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168062)

## Data

Gene col 9590: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9590); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9590, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9590]; `tensor/DDL_lfc|DDL_z.npy` [9590]; `embed/gene_vectors.npy` [9590]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9590 or target_col == 9590). Every well: [[BATF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BATF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
