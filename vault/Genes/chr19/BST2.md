---
symbol: "BST2"
type: "gene"
col: 5046
ensembl_id: "ENSG00000130303"
name: "bone marrow stromal cell antigen 2"
location: "19p13.11"
module: 32
arm: "+"
pooled_cpm: 29.81
n_lines_expressing: 32
n_dd_up: 3
n_dd_down: 22
n_dd_up_clean: 0
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 24
direction_downstream: 56
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# BST2

*bone marrow stromal cell antigen 2* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.09× (z +5.6, q 2e-05, up in 20 of 28 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (J82 7.03×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (J82 6.02×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (J82 4.59×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.253× (z -14.6, q 3e-45, down in 27 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFITM1]] (+0.87, fdr 7e-06), [[IFI6]] (+0.86, fdr 7e-06), [[IFI27]] (+0.84, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 24 arrows point to it, the strongest [[OAS1]] → it (grade B ⚠); 56 go from it, the strongest it → [[TMEM140]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5046.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (J82 7.03×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (J82 6.02×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (J82 4.59×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.09×** | +5.6 | 2e-05 | 20/28 (J82, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.98×** | +5.0 | 2e-04 | 12/21 (J82, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **1.59×** | +3.5 | 0.078 | 22/29 (LoVo, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 1.34× | +3.2 | 0.20 | 20/30 (H4, Hs 766T, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5046.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.253×** | -14.6 | 3e-45 | 27/29 (RKO, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tofacitinib (drug)]] 5 µM |  | **0.448×** | -8.5 | 6e-15 | 26/30 (BT-474, A-172, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.403×** | -6.8 | 2e-09 | 24/29 (RKO, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.610×** | -5.2 | 3e-05 | 21/30 (A-172, BT-474, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.500×** | -5.0 | 7e-05 | 20/29 (RPMI-7951, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.533×** | -4.7 | 3e-04 | 22/30 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.539×** | -4.6 | 3e-04 | 22/30 (MIA PaCa-2, BT-474, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.666×** | -4.3 | 0.001 | 24/30 (A-172, HS-578T, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.578×** | -4.1 | 0.003 | 16/29 (SHP-77, HS-578T, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.584×** | -4.0 | 0.003 | 20/30 (A-172, BT-474, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.587×** | -4.0 | 0.004 | 22/30 (BT-474, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.590×** | -3.9 | 0.004 | 21/30 (A-172, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.601×** | -3.8 | 0.006 | 23/30 (BT-474, SNU-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.610×** | -3.7 | 0.009 | 20/30 (BT-474, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.707×** | -3.6 | 0.010 | 17/30 (BT-474, RPMI-7951, …) | rises with dose | low cells (technical?) |
| [[Budesonide (drug)]] 5 µM |  | **0.615×** | -3.6 | 0.010 | 22/30 (HT-29, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5046. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 52.8 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -14.4) |
| [[BT-474 (line)]] | alt | 19.5 | 0 | 6 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.0510× (z -15.3) |
| [[MIA PaCa-2 (line)]] | alt | 24.8 | 0 | 4 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.183× (z -11.0) |
| [[HS-578T (line)]] | alt | 23.9 | 0 | 3 | — | [[Tofacitinib (drug)]] 5 µM 0.124× (z -11.4) |
| [[J82 (line)]] | alt | 77.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.03× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[KATO III (line)]] | alt | 72.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -13.9) |
| [[RPMI-7951 (line)]] | alt | 69.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0713× (z -21.3) |
| [[CFPAC-1 (line)]] | alt | 81.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -11.5) |
| [[COLO 205 (line)]] | alt | 63.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -16.3) |
| [[H4 (line)]] | wt | 58.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0974× (z -16.6) |
| [[NCI-H2347 (line)]] | alt | 67.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -12.8) |
| [[RKO (line)]] | wt | 107 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0634× (z -24.1) |
| [[SK-MEL-2 (line)]] | alt | 19.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -9.7) |
| [[A498 (line)]] | wt | 58.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -10.0) |
| [[HepG2_C3A (line)]] | wt | 33.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -10.5) |
| [[HT-29 (line)]] | alt | 19.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -9.4) |
| [[LoVo (line)]] | wt | 67.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -9.5) |
| [[SHP-77 (line)]] | alt | 42.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0871× (z -19.8) |
| [[SNU-1 (line)]] | wt | 59.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0777× (z -12.5) |
| [[SNU-423 (line)]] | alt | 17.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0883× (z -13.8) |
| [[SW 900 (line)]] | alt | 69.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -11.0) |
| [[A-427 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.29 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 9.36 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.74 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 66.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.41 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.65 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.21 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.44 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.54 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.17 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 5.26 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.74 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.01 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5046), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFITM1]] | +0.87 | +0.79 / +0.89 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INFLAMMATORY_RESPONSE; STRING 810 |
| [[IFI6]] | +0.86 | +0.77 / +0.89 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 744 |
| [[IFI27]] | +0.84 | +0.71 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 614 |
| [[UBE2L6]] | +0.83 | +0.69 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 688 |
| [[IFITM3]] | +0.80 | +0.67 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 699 |
| [[OAS1]] | +0.79 | +0.67 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 779 |
| [[IFI44]] | +0.79 | +0.70 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 708 |
| [[IFI44L]] | +0.79 | +0.66 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 684 |
| [[MX2]] | +0.79 | +0.65 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 801 |
| [[CCDC194]] | +0.79 | +0.71 / +0.87 | both halves | 7e-06 | ⚠ same locus (8.7 kb, same strand: neighbours can correlate without regulation) |
| [[IFIT1]] | +0.78 | +0.73 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 709 |
| [[RSAD2]] | +0.78 | +0.70 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 754 |
| [[OAS2]] | +0.78 | +0.68 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 777 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 13, C 11. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OAS1]] | B | OAS1 activity raises BST2's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 3.62× lower at baseline in the lines without OAS1 | 0.011 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[OAS2]] | B | OAS2 activity raises BST2's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 3.51× lower at baseline in the lines without OAS2 | 0.012 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[FBXO39]] | B | FBXO39 activity raises BST2's level | lines that do not express FBXO39 (16) vs lines expressing it (34) | 3.99× lower at baseline in the lines without FBXO39 | 0.015 | ⚠ within organs, on part of the lines; also absent: XAF1, TRIM22, SLC15A3 |
| [[NRIR]] | B | NRIR activity raises BST2's level | lines that do not express NRIR (14) vs lines expressing it (36) | 3.05× lower at baseline in the lines without NRIR | 0.022 | ⚠ within organs, on part of the lines; also absent: CMPK2, TSPAN7 |
| [[MX2]] | B | MX2 activity raises BST2's level | lines that do not express MX2 (16) vs lines expressing it (34) | 3.57× lower at baseline in the lines without MX2 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: NRP1, SLC15A3, DEPP1 |
| [[MX1]] | B | MX1 activity raises BST2's level | lines that do not express MX1 (19) vs lines expressing it (31) | 2.27× lower at baseline in the lines without MX1 | 0.030 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[UBA7]] | B | UBA7 activity raises BST2's level | lines that do not express UBA7 (9) vs lines expressing it (41) | 5.34× lower at baseline in the lines without UBA7 | 0.034 | ⚠ within organs, on part of the lines; also absent: XAF1, SH3TC1, SLC15A3; maybe low, not absent |
| [[CMPK2]] | B | CMPK2 activity raises BST2's level | lines that do not express CMPK2 (11) vs lines expressing it (39) | 2.94× lower at baseline in the lines without CMPK2 | 0.042 | ⚠ within organs, on part of the lines; also absent: OAS2, NRIR, OAS1 |
| [[IFI6]] | B | IFI6 activity raises BST2's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 3.51× lower at baseline in the lines without IFI6 | 0.044 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[RSAD2]] | B | RSAD2 activity raises BST2's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 2.66× lower at baseline in the lines without RSAD2 | 0.056 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[CD74]] | B | CD74 activity raises BST2's level | lines that do not express CD74 (31) vs lines expressing it (19) | 2.01× lower at baseline in the lines without CD74 | 0.057 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, SHROOM4, LAPTM5 |
| [[EPSTI1]] | B | EPSTI1 activity raises BST2's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 3.00× lower at baseline in the lines without EPSTI1 | 0.081 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |

### Downstream of this gene

*56 arrows, 56 of them with an alert ⚠; grade A 0, B 48, C 8. Shown: the 12 strongest; 44 more arrows (44 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM140]] | B | BST2 activity raises TMEM140's level | lines that do not express BST2 (18) vs lines expressing it (32) | 2.84× lower at baseline in the lines without BST2 | 0.001 | ⚠ within organs, on part of the lines; also absent: CCDC194, DEPP1, SLC15A3 |
| [[MVB12A]] | B | BST2 activity raises MVB12A's level | lines that do not express BST2 (18) vs lines expressing it (32) | 1.83× lower at baseline in the lines without BST2 | 0.002 | ⚠ within organs, on part of the lines; also absent: CCDC194, DEPP1, SLC15A3 |
| [[MX2]] | B | BST2 activity raises MX2's level | lines that do not express BST2 (18) vs lines expressing it (32) | 4.43× lower at baseline in the lines without BST2 | 0.003 | ⚠ within organs, on part of the lines; also absent: CCDC194, DEPP1, SLC15A3 |
| [[PARP10]] | B | BST2 activity raises PARP10's level | lines that do not express BST2 (18) vs lines expressing it (32) | 1.81× lower at baseline in the lines without BST2 | 0.008 | ⚠ within organs, on part of the lines; also absent: CCDC194, DEPP1, SLC15A3 |
| [[LAP3]] | B | BST2 activity raises LAP3's level | lines that do not express BST2 (18) vs lines expressing it (32) | 1.69× lower at baseline in the lines without BST2 | 0.010 | ⚠ within organs, on part of the lines; also absent: CCDC194, DEPP1, SLC15A3 |
| [[N4BP1]] | B | BST2 activity raises N4BP1's level | lines that do not express BST2 (18) vs lines expressing it (32) | 1.30× lower at baseline in the lines without BST2 | 0.012 | ⚠ within organs, on part of the lines; also absent: CCDC194, DEPP1, SLC15A3 |
| [[OAS2]] | B | BST2 activity raises OAS2's level | lines that do not express BST2 (18) vs lines expressing it (32) | 3.70× lower at baseline in the lines without BST2 | 0.013 | ⚠ within organs, on part of the lines; also absent: CCDC194, DEPP1, SLC15A3 |
| [[CMPK2]] | B | BST2 activity raises CMPK2's level | lines that do not express BST2 (18) vs lines expressing it (32) | 2.62× lower at baseline in the lines without BST2 | 0.015 | ⚠ within organs, on part of the lines; also absent: CCDC194, DEPP1, SLC15A3 |
| [[IFI6]] | B | BST2 activity raises IFI6's level | lines that do not express BST2 (18) vs lines expressing it (32) | 2.82× lower at baseline in the lines without BST2 | 0.015 | ⚠ within organs, on part of the lines; also absent: CCDC194, DEPP1, SLC15A3 |
| [[PLSCR1]] | B | BST2 activity raises PLSCR1's level | lines that do not express BST2 (18) vs lines expressing it (32) | 2.54× lower at baseline in the lines without BST2 | 0.018 | ⚠ within organs, on part of the lines; also absent: CCDC194, DEPP1, SLC15A3 |
| [[PARP9]] | B | BST2 activity raises PARP9's level | lines that do not express BST2 (18) vs lines expressing it (32) | 2.24× lower at baseline in the lines without BST2 | 0.019 | ⚠ within organs, on part of the lines; also absent: CCDC194, DEPP1, SLC15A3 |
| [[HERC6]] | B | BST2 activity raises HERC6's level | lines that do not express BST2 (18) vs lines expressing it (32) | 2.22× lower at baseline in the lines without BST2 | 0.019 | ⚠ within organs, on part of the lines; also absent: CCDC194, DEPP1, SLC15A3 |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.788). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.3, 52.2); signed map (66.3, 29.6). **Vector** length 92.3, 31.7% of its response variance represented; |z| ≥ 3 in 688 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Interferon gamma signaling* (reactome, mean cos +0.65 to 17); *Antimicrobial mechanism of IFN-stimulated genes* (reactome, mean cos +0.71 to 21); *Modulation of host responses by IFN-stimulated genes* (reactome, mean cos +0.74 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +1.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.0 | +2.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.5 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | -1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.0 | +1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | -3.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.8 | +2.1 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -5.8 | -8.5 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -4.6 | -5.2 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -4.4 | -4.6 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -4.2 | -4.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.1 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | bone marrow stromal cell antigen 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:17,402,939-17,405,630 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CD317, tetherin, BST-2, HM1.24 |
| Gene groups (HGNC) | CD molecules |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, INFLAMMATORY_RESPONSE, INTERFERON_GAMMA_RESPONSE |
| Reactome | 10 pathways, smallest: SARS-CoV-1 activates/modulates innate immune responses; Interferon alpha/beta signaling; SARS-CoV-1-host interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [Q10589](https://www.uniprot.org/uniprotkb/Q10589) (Bone marrow stromal antigen 2):

> IFN-induced antiviral host restriction factor which efficiently blocks the release of diverse mammalian enveloped viruses by directly tethering nascent virions to the membranes of infected cells. Acts as a direct physical tether, holding virions to the cell membrane and linking virions to each other. The tethered virions can be internalized by endocytosis and subsequently degraded or they can remain on the cell surface. In either case, their spread as cell-free virions is restricted. Its target …

**Summary**, from NCBI Gene [684](https://www.ncbi.nlm.nih.gov/gene/684):

> Bone marrow stromal cells are involved in the growth and development of B-cells. The specific function of the protein encoded by the bone marrow stromal cell antigen 2 is undetermined; however, this protein may play a role in pre-B-cell growth and in rheumatoid arthritis. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1119](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1119) · Entrez [684](https://www.ncbi.nlm.nih.gov/gene/684) · UniProt [Q10589](https://www.uniprot.org/uniprotkb/Q10589) · Ensembl [ENSG00000130303](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130303)

## Data

Gene col 5046: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5046); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5046, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5046]; `tensor/DDL_lfc|DDL_z.npy` [5046]; `embed/gene_vectors.npy` [5046]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5046 or target_col == 5046). Every well: [[BST2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BST2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
