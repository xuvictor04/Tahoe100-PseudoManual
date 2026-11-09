---
symbol: "IFITM1"
type: "gene"
col: 11748
ensembl_id: "ENSG00000185885"
name: "interferon induced transmembrane protein 1"
location: "11p15.5"
module: 32
arm: "+"
pooled_cpm: 99.19
n_lines_expressing: 31
n_dd_up: 0
n_dd_down: 47
n_dd_up_clean: 0
n_dd_down_clean: 38
in_vector_space: true
direction_upstream: 26
direction_downstream: 61
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# IFITM1

*interferon induced transmembrane protein 1* — 11p15.5

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (J82 6.01×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (J82 5.49×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 47 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.142× (z -16.8, q 0e+00, down in 29 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFITM3]] (+0.89, fdr 7e-06, ⚠ same locus), [[IFI6]] (+0.88, fdr 7e-06), [[BST2]] (+0.87, fdr 7e-06), [[UBE2L6]] (+0.84, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 26 arrows point to it, the strongest [[OAS2]] → it (grade B ⚠); 61 go from it, the strongest it → [[UBA7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11748.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (J82 6.01×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (J82 5.49×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 0.5 µM |  | 2.68× | +3.2 | 0.40 | 22/29 (A-172, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | 1.42× | +3.1 | 0.40 | 25/29 (RPMI-7951, hTERT-HPNE, …) | rises with dose |  |
| [[Arbutin (drug)]] 5 µM |  | 1.68× | +3.1 | 0.40 | 25/29 (J82, PANC-1, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 9 with an alert ⚠; shown: the 15 strongest. 47 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11748.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.142×** | -16.8 | 0e+00 | 29/29 (HepG2/C3A, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tofacitinib (drug)]] 5 µM |  | **0.184×** | -14.6 | 1e-45 | 28/29 (A-172, SNU-423, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.113×** | -13.2 | 9e-38 | 28/29 (HS-578T, BT-474, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.133×** | -12.3 | 2e-32 | 28/29 (SNU-423, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.266×** | -11.4 | 8e-28 | 28/30 (A-172, SNU-423, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.164×** | -11.0 | 5e-26 | 28/29 (A-172, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.197×** | -9.9 | 4e-21 | 28/29 (A-172, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.223×** | -9.1 | 6e-18 | 28/29 (NCI-H1792, KATO III, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.211×** | -9.1 | 6e-18 | 27/29 (A498, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.244×** | -8.6 | 6e-16 | 28/29 (A498, KATO III, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.376×** | -8.4 | 3e-15 | 29/29 (LoVo, HS-578T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.261×** | -8.2 | 2e-14 | 27/29 (A-172, SNU-423, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.244×** | -8.1 | 3e-14 | 29/29 (C32, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.284×** | -7.6 | 8e-13 | 28/29 (RKO, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.288×** | -7.5 | 2e-12 | 26/29 (SNU-423, A-172, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.46 per unit of S-phase module lfc, +0.54 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11748. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 316 | 0 | 25 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0562× (z -22.9) |
| [[SNU-423 (line)]] | alt | 191 | 0 | 22 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0514× (z -23.1) |
| [[BT-474 (line)]] | alt | 61.7 | 0 | 21 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0111× (z -19.6) |
| [[LoVo (line)]] | wt | 62.0 | 0 | 20 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0615× (z -16.3) |
| [[A498 (line)]] | wt | 82.8 | 0 | 19 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0235× (z -24.6) |
| [[HepG2_C3A (line)]] | wt | 200 | 0 | 18 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0311× (z -25.7) |
| [[RPMI-7951 (line)]] | alt | 148 | 0 | 16 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -15.5) |
| [[HS-578T (line)]] | alt | 74.4 | 0 | 15 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0244× (z -19.8) |
| [[NCI-H1792 (line)]] | alt | 87.3 | 0 | 14 | — | [[Homoharringtonine (drug)]] 5 µM 0.0534× (z -19.1) |
| [[KATO III (line)]] | alt | 167 | 0 | 13 | — | [[Homoharringtonine (drug)]] 5 µM 0.0605× (z -20.5) |
| [[MIA PaCa-2 (line)]] | alt | 296 | 0 | 12 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.122× (z -15.9) |
| [[C32 (line)]] | wt | 176 | 0 | 10 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.120× (z -16.7) |
| [[NCI-H2347 (line)]] | alt | 329 | 0 | 10 (2 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.157× (z -15.8) |
| [[AsPC-1 (line)]] | alt | 105 | 0 | 9 | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -14.0) |
| [[PANC-1 (line)]] | alt | 94.5 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0762× (z -20.1) |
| [[RKO (line)]] | wt | 51.2 | 0 | 8 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0112× (z -16.2) |
| [[SNU-1 (line)]] | wt | 80.8 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -13.2) |
| [[J82 (line)]] | alt | 188 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 6.01× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -11.0) |
| [[SW 900 (line)]] | alt | 130 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -15.2) |
| [[CFPAC-1 (line)]] | alt | 300 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -16.4) |
| [[Panc 03.27 (line)]] | alt | 255 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -14.7) |
| [[Hs 766T (line)]] | wt | 349 | 0 | 3 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.222× (z -11.5) |
| [[SK-MEL-2 (line)]] | alt | 27.6 | 0 | 3 (1 ⚠) | — | [[Tofacitinib (citrate) (drug)]] 0.5 µM 0.0695× (z -10.1) |
| [[CHP-212 (line)]] | wt | 32.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0331× (z -14.0) |
| [[SW1417 (line)]] | alt | 199 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -17.1) |
| [[COLO 205 (line)]] | alt | 27.3 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.155× (z -8.7) |
| [[HCT15 (line)]] | alt | 39.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -11.0) |
| [[hTERT-HPNE (line)]] | wt | 54.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -8.5) |
| [[LS 180 (line)]] | wt | 47.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -12.5) |
| [[A-427 (line)]] | wt | 4.91 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 22.5 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 17.9 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 15.4 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.88 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 11.3 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 8.40 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 13.1 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.86 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.85 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.61 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 5.57 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.48 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 16.5 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 17.5 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 7.03 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 7.33 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 10.4 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11748), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFITM3]] | +0.89 | +0.77 / +0.94 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 872; ⚠ same locus (4.4 kb: neighbours can correlate without regulation) |
| [[IFI6]] | +0.88 | +0.77 / +0.93 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 891 |
| [[BST2]] | +0.87 | +0.79 / +0.89 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INFLAMMATORY_RESPONSE; STRING 810 |
| [[IFITM2]] | +0.85 | +0.69 / +0.90 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 796; ⚠ same locus (0.6 kb, same strand: neighbours can correlate without regulation) |
| [[UBE2L6]] | +0.84 | +0.68 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 614 |
| [[IFI27]] | +0.84 | +0.74 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 908 |
| [[OAS1]] | +0.82 | +0.67 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 863 |
| [[IFI44L]] | +0.80 | +0.71 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 795 |
| [[ISG15]] | +0.80 | +0.60 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 903 |
| [[MX2]] | +0.80 | +0.69 / +0.87 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 776 |
| [[CMPK2]] | +0.80 | +0.70 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 450 |
| [[OAS2]] | +0.79 | +0.71 / +0.87 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 786 |
| [[USP18]] | +0.79 | +0.70 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 556 |
| [[EPSTI1]] | +0.78 | +0.71 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 520 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 16, C 10. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OAS2]] | B | OAS2 activity raises IFITM1's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 4.10× lower at baseline in the lines without OAS2 | 0.005 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[UBA7]] | B | UBA7 activity raises IFITM1's level | lines that do not express UBA7 (9) vs lines expressing it (41) | 7.01× lower at baseline in the lines without UBA7 | 0.005 | ⚠ within organs, on part of the lines; also absent: XAF1, SH3TC1, SLC15A3; maybe low, not absent |
| [[PLAAT4]] | B | PLAAT4 activity raises IFITM1's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 2.96× lower at baseline in the lines without PLAAT4 | 0.011 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |
| [[SAMD9L]] | B | SAMD9L activity raises IFITM1's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 3.44× lower at baseline in the lines without SAMD9L | 0.013 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[BATF2]] | B | BATF2 activity raises IFITM1's level | lines that do not express BATF2 (13) vs lines expressing it (37) | 3.69× lower at baseline in the lines without BATF2 | 0.013 | ⚠ within organs, on part of the lines; also absent: RSAD2; maybe low, not absent |
| [[IFI44L]] | B | IFI44L activity raises IFITM1's level | lines that do not express IFI44L (22) vs lines expressing it (28) | 3.14× lower at baseline in the lines without IFI44L | 0.015 | ⚠ within organs, on part of the lines; also absent: GBP1, EPSTI1, GBP4 |
| [[IDO1]] | B | IDO1 activity raises IFITM1's level | lines that do not express IDO1 (28) vs lines expressing it (22) | 2.61× lower at baseline in the lines without IDO1 | 0.021 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, DKK3 |
| [[OAS1]] | B | OAS1 activity raises IFITM1's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 4.15× lower at baseline in the lines without OAS1 | 0.022 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[FBXO39]] | B | FBXO39 activity raises IFITM1's level | lines that do not express FBXO39 (16) vs lines expressing it (34) | 4.09× lower at baseline in the lines without FBXO39 | 0.031 | ⚠ within organs, on part of the lines; also absent: XAF1, TRIM22, SLC15A3 |
| [[GMPR]] | B | GMPR activity raises IFITM1's level | lines that do not express GMPR (14) vs lines expressing it (36) | 2.50× lower at baseline in the lines without GMPR | 0.031 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TRANK1]] | B | TRANK1 activity raises IFITM1's level | lines that do not express TRANK1 (7) vs lines expressing it (43) | 4.36× lower at baseline in the lines without TRANK1 | 0.033 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[STING1]] | B | STING1 activity raises IFITM1's level | lines that do not express STING1 (17) vs lines expressing it (33) | 2.96× lower at baseline in the lines without STING1 | 0.048 | ⚠ within organs, on part of the lines; also absent: MANCR, SATB1, NLRP1 |

### Downstream of this gene

*61 arrows, 61 of them with an alert ⚠; grade A 0, B 51, C 10. Shown: the 12 strongest; 49 more arrows (49 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UBA7]] | B | IFITM1 activity raises UBA7's level | lines that do not express IFITM1 (19) vs lines expressing it (31) | 2.31× lower at baseline in the lines without IFITM1 | 0.002 | ⚠ within organs, on part of the lines; also absent: TRIM22, IFI6, SLC15A3 |
| [[HERC6]] | B | IFITM1 activity raises HERC6's level | lines that do not express IFITM1 (19) vs lines expressing it (31) | 2.36× lower at baseline in the lines without IFITM1 | 0.002 | ⚠ within organs, on part of the lines; also absent: TRIM22, IFI6, SLC15A3 |
| [[IFITM3]] | B | IFITM1 activity raises IFITM3's level | lines that do not express IFITM1 (19) vs lines expressing it (31) | 2.97× lower at baseline in the lines without IFITM1 | 0.003 | ⚠ within organs, on part of the lines; also absent: TRIM22, IFI6, SLC15A3 |
| [[IFI44L]] | B | IFITM1 activity raises IFI44L's level | lines that do not express IFITM1 (19) vs lines expressing it (31) | 4.01× lower at baseline in the lines without IFITM1 | 0.003 | ⚠ within organs, on part of the lines; also absent: TRIM22, IFI6, SLC15A3 |
| [[SAMD9L]] | B | IFITM1 activity raises SAMD9L's level | lines that do not express IFITM1 (19) vs lines expressing it (31) | 3.62× lower at baseline in the lines without IFITM1 | 0.003 | ⚠ within organs, on part of the lines; also absent: TRIM22, IFI6, SLC15A3 |
| [[PARP10]] | B | IFITM1 activity raises PARP10's level | lines that do not express IFITM1 (19) vs lines expressing it (31) | 1.96× lower at baseline in the lines without IFITM1 | 0.005 | ⚠ within organs, on part of the lines; also absent: TRIM22, IFI6, SLC15A3 |
| [[MX2]] | B | IFITM1 activity raises MX2's level | lines that do not express IFITM1 (19) vs lines expressing it (31) | 4.78× lower at baseline in the lines without IFITM1 | 0.006 | ⚠ within organs, on part of the lines; also absent: TRIM22, IFI6, SLC15A3 |
| [[OAS2]] | B | IFITM1 activity raises OAS2's level | lines that do not express IFITM1 (19) vs lines expressing it (31) | 4.13× lower at baseline in the lines without IFITM1 | 0.007 | ⚠ within organs, on part of the lines; also absent: TRIM22, IFI6, SLC15A3 |
| [[PARP14]] | B | IFITM1 activity raises PARP14's level | lines that do not express IFITM1 (19) vs lines expressing it (31) | 2.30× lower at baseline in the lines without IFITM1 | 0.008 | ⚠ within organs, on part of the lines; also absent: TRIM22, IFI6, SLC15A3 |
| [[USP18]] | B | IFITM1 activity raises USP18's level | lines that do not express IFITM1 (19) vs lines expressing it (31) | 2.15× lower at baseline in the lines without IFITM1 | 0.011 | ⚠ within organs, on part of the lines; also absent: TRIM22, IFI6, SLC15A3 |
| [[IFI16]] | B | IFITM1 activity raises IFI16's level | lines that do not express IFITM1 (19) vs lines expressing it (31) | 3.50× lower at baseline in the lines without IFITM1 | 0.011 | ⚠ within organs, on part of the lines; also absent: TRIM22, IFI6, SLC15A3 |
| [[UBE2L6]] | B | IFITM1 activity raises UBE2L6's level | lines that do not express IFITM1 (19) vs lines expressing it (31) | 2.21× lower at baseline in the lines without IFITM1 | 0.012 | ⚠ within organs, on part of the lines; also absent: TRIM22, IFI6, SLC15A3 |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.787). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.1, 52.1); signed map (66.1, 29.5). **Vector** length 139, 54.4% of its response variance represented; |z| ≥ 3 in 1,167 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon gamma response* (hallmark, mean cos +0.68 to 60); *interferon* (control, mean cos +0.76 to 23); *Interferon gamma signaling* (reactome, mean cos +0.65 to 17).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cobimetinib (drug)]] 5 µM |  | +3.4 | +2.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | -1.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.0 | -11.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.9 | -7.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | -0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.1 | +1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | -3.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.0 | +2.3 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -8.6 | -14.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | -7.3 | -1.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.9 | -4.2 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -6.8 | -11.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.8 | -5.0 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -6.7 | -9.9 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -6.7 | -9.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -6.0 | -8.2 |

## What is on record

|  |  |
|---|---|
| Name | interferon induced transmembrane protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:310,041-315,272 (+) |
| Ensembl biotype | protein_coding |
| Also known as | 9-27, CD225, DSPA2a; previously IFI17 |
| Gene groups (HGNC) | CD molecules; Interferon induced transmembrane protein family; Dispanins |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, INFLAMMATORY_RESPONSE |
| Reactome | 5 pathways, smallest: Immunoregulatory interactions between a Lymphoid and a non-Lymphoid cell; Interferon alpha/beta signaling; Interferon Signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P13164](https://www.uniprot.org/uniprotkb/P13164) (Interferon-induced transmembrane protein 1):

> IFN-induced antiviral protein which inhibits the entry of viruses to the host cell cytoplasm, permitting endocytosis, but preventing subsequent viral fusion and release of viral contents into the cytosol. Active against multiple viruses, including influenza A virus, SARS coronaviruses (SARS-CoV and SARS-CoV-2), Marburg virus (MARV), Ebola virus (EBOV), Dengue virus (DNV), West Nile virus (WNV), human immunodeficiency virus type 1 (HIV-1) and hepatitis C virus (HCV). Can inhibit: influenza virus …

**Summary**, from NCBI Gene [8519](https://www.ncbi.nlm.nih.gov/gene/8519):

> Interferon-induced transmembrane (IFITM) proteins are a family of interferon induced antiviral proteins. The family contains five members, including IFITM1, IFITM2 and IFITM3 that belong to the CD225 superfamily. The protein encoded by this gene restricts cellular entry by diverse viral pathogens, such as influenza A virus, Ebola virus and Sars-CoV-2. [provided by RefSeq, Nov 2021]

**Accessions** — [HGNC:5412](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5412) · Entrez [8519](https://www.ncbi.nlm.nih.gov/gene/8519) · UniProt [P13164](https://www.uniprot.org/uniprotkb/P13164) · Ensembl [ENSG00000185885](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185885)

## Data

Gene col 11748: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11748); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11748, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11748]; `tensor/DDL_lfc|DDL_z.npy` [11748]; `embed/gene_vectors.npy` [11748]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11748 or target_col == 11748). Every well: [[IFITM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IFITM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
