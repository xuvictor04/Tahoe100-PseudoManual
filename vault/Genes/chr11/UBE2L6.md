---
symbol: "UBE2L6"
type: "gene"
col: 7998
ensembl_id: "ENSG00000156587"
name: "ubiquitin conjugating enzyme E2 L6"
location: "11q12.1"
module: 32
arm: "+"
pooled_cpm: 28.02
n_lines_expressing: 44
n_dd_up: 7
n_dd_down: 33
n_dd_up_clean: 6
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 64
direction_downstream: 16
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# UBE2L6

*ubiquitin conjugating enzyme E2 L6* — 11q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.73× (z +4.8, q 0.001, up in 29 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.204× (z -20.3, q 0e+00, down in 41 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OAS1]] (+0.92, fdr 7e-06), [[IFI35]] (+0.89, fdr 7e-06), [[IFI6]] (+0.88, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 64 arrows point to it, the strongest [[SAMD9L]] → it (grade B ⚠); 16 go from it, the strongest it → [[IFITM3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7998.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.73×** | +4.8 | 0.001 | 29/40 (NCI-H1573, KATO III, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.55×** | +4.0 | 0.021 | 25/40 (PANC-1, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.49×** | +3.6 | 0.038 | 23/41 (C32, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.50×** | +3.6 | 0.038 | 22/42 (CFPAC-1, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.49×** | +3.5 | 0.051 | 26/41 (NCI-H1573, KATO III, …) | rises with dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.46×** | +3.5 | 0.051 | 18/42 (NCI-H23, KATO III, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.47×** | +3.2 | 0.100 | 21/42 (KATO III, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[venetoclax (drug)]] 0.05 µM |  | 1.42× | +3.0 | 0.17 | 17/42 (Panc 03.27, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7998.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.204×** | -20.3 | 0e+00 | 41/41 (NCI-H1573, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tofacitinib (drug)]] 5 µM |  | **0.473×** | -9.5 | 5e-19 | 32/42 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.429×** | -7.6 | 5e-12 | 29/42 (MIA PaCa-2, LoVo, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **0.444×** | -7.3 | 4e-11 | 31/42 (A-172, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.457×** | -7.0 | 2e-10 | 29/42 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.585×** | -6.8 | 1e-09 | 29/42 (CFPAC-1, COLO 205, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.494×** | -6.1 | 9e-08 | 27/41 (A549, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.512×** | -6.0 | 1e-07 | 26/42 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.521×** | -5.9 | 3e-07 | 25/42 (LoVo, A549, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.524×** | -5.8 | 3e-07 | 28/42 (COLO 205, LoVo, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.524×** | -5.8 | 3e-07 | 30/42 (NCI-H1573, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.531×** | -5.7 | 6e-07 | 28/42 (LoVo, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.540×** | -5.3 | 4e-06 | 26/37 (SW1417, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.584×** | -4.8 | 5e-05 | 25/42 (LoVo, SNU-423, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.574×** | -4.7 | 9e-05 | 25/42 (MIA PaCa-2, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.705×** | -4.4 | 3e-04 | 25/42 (COLO 205, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~20% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7998. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 41.4 | 0 | 12 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -19.6) |
| [[MIA PaCa-2 (line)]] | alt | 44.7 | 0 | 11 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0775× (z -14.6) |
| [[A-172 (line)]] | wt | 78.5 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -17.9) |
| [[A549 (line)]] | wt | 48.3 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0505× (z -25.8) |
| [[COLO 205 (line)]] | alt | 72.1 | 0 | 6 | — | [[Selinexor (drug)]] 5 µM 0.215× (z -12.6) |
| [[NCI-H2347 (line)]] | alt | 67.3 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -16.7) |
| [[SNU-423 (line)]] | alt | 69.5 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -18.4) |
| [[HS-578T (line)]] | alt | 56.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -20.1) |
| [[A498 (line)]] | wt | 47.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -21.6) |
| [[BT-474 (line)]] | alt | 8.76 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0902× (z -11.6) |
| [[J82 (line)]] | alt | 33.9 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 7.06× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -10.6) |
| [[NCI-H1792 (line)]] | alt | 75.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0834× (z -23.3) |
| [[RKO (line)]] | wt | 25.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0284× (z -17.2) |
| [[SW1417 (line)]] | alt | 21.2 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0711× (z -20.5) |
| [[KATO III (line)]] | alt | 30.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -15.6) |
| [[NCI-H1573 (line)]] | alt | 19.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0242× (z -28.0) |
| [[CFPAC-1 (line)]] | alt | 65.1 | 0 | 2 | — | [[Tofacitinib (drug)]] 5 µM 0.256× (z -14.0) |
| [[CHP-212 (line)]] | wt | 26.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0534× (z -13.4) |
| [[HepG2_C3A (line)]] | wt | 18.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0833× (z -13.9) |
| [[PANC-1 (line)]] | alt | 15.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -19.0) |
| [[RPMI-7951 (line)]] | alt | 52.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -16.2) |
| [[A-427 (line)]] | wt | 14.7 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.136× (z -10.2) ⚠ cell-cycle shift, explains ~17% of this change |
| [[AsPC-1 (line)]] | alt | 8.72 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -8.6) |
| [[H4 (line)]] | wt | 25.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -9.1) |
| [[HOP62 (line)]] | alt | 9.01 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -13.0) |
| [[Hs 766T (line)]] | wt | 27.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 18.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -18.0) |
| [[NCI-H23 (line)]] | alt | 12.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0977× (z -14.4) |
| [[NCI-H460 (line)]] | wt | 7.19 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -11.2) |
| [[Panc 03.27 (line)]] | alt | 54.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -10.4) |
| [[SW 900 (line)]] | alt | 18.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -10.7) |
| [[AN3 CA (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.92 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.63 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.85 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.07 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.96 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.48 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7998), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OAS1]] | +0.92 | +0.86 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 769 |
| [[IFI35]] | +0.89 | +0.83 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 895 |
| [[IFI6]] | +0.88 | +0.79 / +0.90 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 697 |
| [[PARP9]] | +0.87 | +0.81 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 696 |
| [[IFIT1]] | +0.87 | +0.82 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 810 |
| [[OAS2]] | +0.86 | +0.81 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 779 |
| [[CMPK2]] | +0.86 | +0.79 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 490 |
| [[PSMB9]] | +0.86 | +0.77 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 856 |
| [[SHFL]] | +0.86 | +0.79 / +0.88 | both halves | 7e-06 | STRING 568 |
| [[IFITM3]] | +0.86 | +0.75 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 451 |
| [[IFIT3]] | +0.86 | +0.79 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 811 |
| [[MX1]] | +0.85 | +0.79 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 807 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*64 arrows, 64 of them with an alert ⚠; grade A 0, B 48, C 16. Shown: the 12 strongest; 52 more arrows (52 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SAMD9L]] | B | SAMD9L activity raises UBE2L6's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 2.96× lower at baseline in the lines without SAMD9L | 0.001 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[OAS2]] | B | OAS2 activity strengthens UBE2L6's drug response | lines that do not express OAS2 (9) vs lines expressing it (33) | the lines without OAS2 respond 0.29× as strongly (z diff +2.63); strongest at Fedratinib (hydrochloride hydrate) 5 µM: 0.91x vs 0.36x (z diff +4.2) | 0.004 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1; target measured in part of the lines; artifact flags |
| [[GBP4]] | B | GBP4 activity raises UBE2L6's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 2.95× lower at baseline in the lines without GBP4 | 0.005 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[SLC15A3]] | B | SLC15A3 activity raises UBE2L6's level | lines that do not express SLC15A3 (16) vs lines expressing it (34) | 3.22× lower at baseline in the lines without SLC15A3 | 0.006 | ⚠ within organs, on part of the lines; also absent: XAF1, MX2, GBP4 |
| [[CD5L]] | B | CD5L activity strengthens UBE2L6's drug response | lines that do not express CD5L (18) vs lines expressing it (24) | the lines without CD5L respond 0.51× as strongly (z diff +2.13); strongest at Panobinostat 5 µM: 0.56x vs 0.34x (z diff +3.7) | 0.006 | ⚠ within organs, on part of the lines; also absent: GBP4, TRIM22, GBP5; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[LMO2]] | B | LMO2 activity strengthens UBE2L6's drug response | lines that do not express LMO2 (22) vs lines expressing it (20) | the lines without LMO2 respond 0.50× as strongly (z diff +2.24); strongest at Panobinostat 5 µM: 0.58x vs 0.30x (z diff +4.4) | 0.006 | ⚠ within organs, on part of the lines; also absent: TNFSF10, SAA1, SAA4; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[OAS1]] | B | OAS1 activity strengthens UBE2L6's drug response | lines that do not express OAS1 (10) vs lines expressing it (32) | the lines without OAS1 respond 0.31× as strongly (z diff +2.66); strongest at Fedratinib (hydrochloride hydrate) 5 µM: 0.89x vs 0.35x (z diff +4.6) | 0.008 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[TRIM22]] | B | TRIM22 activity raises UBE2L6's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 2.66× lower at baseline in the lines without TRIM22 | 0.011 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[IFITM1]] | B | IFITM1 activity raises UBE2L6's level | lines that do not express IFITM1 (19) vs lines expressing it (31) | 2.21× lower at baseline in the lines without IFITM1 | 0.012 | ⚠ within organs, on part of the lines; also absent: TRIM22, IFI6, SLC15A3 |
| [[IFI6]] | B | IFI6 activity raises UBE2L6's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 2.61× lower at baseline in the lines without IFI6 | 0.012 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[SAMD9L]] | B | SAMD9L activity strengthens UBE2L6's drug response | lines that do not express SAMD9L (13) vs lines expressing it (29) | the lines without SAMD9L respond 0.52× as strongly (z diff +1.96); strongest at Belinostat 5 µM: 0.67x vs 0.37x (z diff +3.7) | 0.013 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22; target measured in part of the lines; artifact flags |
| [[TRIM22]] | B | TRIM22 activity strengthens UBE2L6's drug response | lines that do not express TRIM22 (14) vs lines expressing it (28) | the lines without TRIM22 respond 0.39× as strongly (z diff +2.38); strongest at Panobinostat 5 µM: 0.62x vs 0.35x (z diff +3.9) | 0.014 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1; target measured in part of the lines; the reference differs; artifact flags |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 14, C 2. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFITM3]] | B | UBE2L6 activity raises IFITM3's level | lines that do not express UBE2L6 (6) vs lines expressing it (44) | 2.65× lower at baseline in the lines without UBE2L6 | 0.015 | ⚠ within organs, on part of the lines; also absent: BLVRA, ADAMTSL4, HLA-B |
| [[HLA-F]] | B | UBE2L6 activity raises HLA-F's level | lines that do not express UBE2L6 (6) vs lines expressing it (44) | 2.66× lower at baseline in the lines without UBE2L6 | 0.045 | ⚠ within organs, on part of the lines; also absent: BLVRA, ADAMTSL4, HLA-B |
| [[REC8]] | B | UBE2L6 activity raises REC8's level | lines that do not express UBE2L6 (6) vs lines expressing it (44) | 2.07× lower at baseline in the lines without UBE2L6 | 0.048 | ⚠ within organs, on part of the lines; also absent: BLVRA, ADAMTSL4, HLA-B |
| [[SP100]] | B | UBE2L6 activity raises SP100's level | lines that do not express UBE2L6 (6) vs lines expressing it (44) | 2.02× lower at baseline in the lines without UBE2L6 | 0.049 | ⚠ within organs, on part of the lines; also absent: BLVRA, ADAMTSL4, HLA-B |
| [[SP110]] | B | UBE2L6 activity raises SP110's level | lines that do not express UBE2L6 (6) vs lines expressing it (44) | 3.23× lower at baseline in the lines without UBE2L6 | 0.057 | ⚠ within organs, on part of the lines; also absent: BLVRA, ADAMTSL4, HLA-B |
| [[PARP10]] | B | UBE2L6 activity raises PARP10's level | lines that do not express UBE2L6 (6) vs lines expressing it (44) | 1.77× lower at baseline in the lines without UBE2L6 | 0.061 | ⚠ within organs, on part of the lines; also absent: BLVRA, ADAMTSL4, HLA-B |
| [[IRF9]] | B | UBE2L6 activity raises IRF9's level | lines that do not express UBE2L6 (6) vs lines expressing it (44) | 2.38× lower at baseline in the lines without UBE2L6 | 0.062 | ⚠ within organs, on part of the lines; also absent: BLVRA, ADAMTSL4, HLA-B |
| [[N4BP1]] | B | UBE2L6 activity raises N4BP1's level | lines that do not express UBE2L6 (6) vs lines expressing it (44) | 1.26× lower at baseline in the lines without UBE2L6 | 0.079 | ⚠ within organs, on part of the lines; also absent: BLVRA, ADAMTSL4, HLA-B |
| [[CASP8]] | B | UBE2L6 activity raises CASP8's level | lines that do not express UBE2L6 (6) vs lines expressing it (44) | 1.51× lower at baseline in the lines without UBE2L6 | 0.089 | ⚠ within organs, on part of the lines; also absent: BLVRA, ADAMTSL4, HLA-B |
| [[PARP14]] | B | UBE2L6 activity raises PARP14's level | lines that do not express UBE2L6 (6) vs lines expressing it (44) | 2.11× lower at baseline in the lines without UBE2L6 | 0.093 | ⚠ within organs, on part of the lines; also absent: BLVRA, ADAMTSL4, HLA-B |
| [[NMI]] | B | UBE2L6 activity raises NMI's level | lines that do not express UBE2L6 (6) vs lines expressing it (44) | 2.17× lower at baseline in the lines without UBE2L6 | 0.093 | ⚠ within organs, on part of the lines; also absent: BLVRA, ADAMTSL4, HLA-B |
| [[BTN3A2]] | B | UBE2L6 activity raises BTN3A2's level | lines that do not express UBE2L6 (6) vs lines expressing it (44) | 1.65× lower at baseline in the lines without UBE2L6 | 0.096 | ⚠ within organs, on part of the lines; also absent: BLVRA, ADAMTSL4, HLA-B |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.895). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.6, 52.6); signed map (65.7, 30.1). **Vector** length 129, 43.9% of its response variance represented; |z| ≥ 3 in 1,140 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon* (control, mean cos +0.83 to 23); *Interferon alpha/beta signaling* (reactome, mean cos +0.82 to 27); *Interferon gamma signaling* (reactome, mean cos +0.75 to 17).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +4.9 | +3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.9 | +4.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.8 | +2.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.7 | +3.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.7 | +2.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.5 | +3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.5 | +3.5 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -8.6 | -9.5 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -7.0 | -5.8 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -6.9 | -6.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -6.7 | -7.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -6.1 | -5.9 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin conjugating enzyme E2 L6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.1 — chr11:57,551,656-57,568,284 (-) |
| Ensembl biotype | protein_coding |
| Also known as | UBCH8 |
| Gene groups (HGNC) | Ubiquitin conjugating enzymes E2 |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, FATTY_ACID_METABOLISM, INTERFERON_GAMMA_RESPONSE |
| Reactome | 20 pathways, smallest: Modulation of host responses by IFN-stimulated genes; Termination of translesion DNA synthesis; Negative regulators of DDX58/IFIH1 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [O14933](https://www.uniprot.org/uniprotkb/O14933) (Ubiquitin/ISG15-conjugating enzyme E2 L6):

> Catalyzes the covalent attachment of ubiquitin or ISG15 to other proteins. Functions in the E6/E6-AP-induced ubiquitination of p53/TP53. Promotes ubiquitination and subsequent proteasomal degradation of FLT3.

**Summary**, from NCBI Gene [9246](https://www.ncbi.nlm.nih.gov/gene/9246):

> The modification of proteins with ubiquitin is an important cellular mechanism for targeting abnormal or short-lived proteins for degradation. Ubiquitination involves at least three classes of enzymes: ubiquitin-activating enzymes (E1s), ubiquitin-conjugating enzymes (E2s) and ubiquitin-protein ligases (E3s). This gene encodes a member of the E2 ubiquitin-conjugating enzyme family. This enzyme is highly similar in primary structure to the enzyme encoded by the UBE2L3 gene. Two alternatively …

**Accessions** — [HGNC:12490](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12490) · Entrez [9246](https://www.ncbi.nlm.nih.gov/gene/9246) · UniProt [O14933](https://www.uniprot.org/uniprotkb/O14933) · Ensembl [ENSG00000156587](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156587)

## Data

Gene col 7998: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7998); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7998, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7998]; `tensor/DDL_lfc|DDL_z.npy` [7998]; `embed/gene_vectors.npy` [7998]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7998 or target_col == 7998). Every well: [[UBE2L6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE2L6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
