---
symbol: "CMPK2"
type: "gene"
col: 5548
ensembl_id: "ENSG00000134326"
name: "cytidine/uridine monophosphate kinase 2"
location: "2p25.2"
module: 32
arm: "+"
pooled_cpm: 20.0
n_lines_expressing: 39
n_dd_up: 18
n_dd_down: 70
n_dd_up_clean: 18
n_dd_down_clean: 58
in_vector_space: true
direction_upstream: 61
direction_downstream: 73
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# CMPK2

*cytidine/uridine monophosphate kinase 2* — 2p25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.90× (z +5.1, q 2e-04, up in 20 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 70 drug-doses (12 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.0896× (z -19.1, q 0e+00, down in 36 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OAS2]] (+0.97, fdr 7e-06), [[MX1]] (+0.96, fdr 7e-06), [[USP18]] (+0.96, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 61 arrows point to it, the strongest [[SRMS]] → it (grade B ⚠); 73 go from it, the strongest it → [[HERC6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, none with an alert; shown: the 15 strongest. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5548.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.90×** | +5.1 | 2e-04 | 20/36 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.91×** | +5.0 | 2e-04 | 25/36 (Hs 766T, CFPAC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 5 µM |  | **1.44×** | +4.2 | 0.004 | 23/37 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.69×** | +4.2 | 0.004 | 19/36 (CFPAC-1, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.67×** | +4.1 | 0.004 | 16/36 (Hs 766T, CFPAC-1, …) | rises with dose |  |
| [[venetoclax (drug)]] 0.05 µM |  | **1.64×** | +3.8 | 0.014 | 17/37 (LoVo, Hs 766T, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.63×** | +3.8 | 0.014 | 17/36 (Hs 766T, AsPC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.41×** | +3.7 | 0.014 | 19/37 (CFPAC-1, LoVo, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.56×** | +3.5 | 0.026 | 16/37 (CFPAC-1, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.55×** | +3.3 | 0.045 | 13/37 (COLO 205, Panc 03.27, …) | inconsistent across doses |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.55×** | +3.3 | 0.045 | 12/36 (SW1417, BT-474, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.36×** | +3.3 | 0.045 | 16/37 (CFPAC-1, LoVo, …) | all doses, flat |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.49×** | +3.2 | 0.056 | 14/37 (NCI-H2347, A-172, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **1.49×** | +3.2 | 0.056 | 13/36 (NCI-H1792, A-172, …) | top dose only | position effect removed |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **1.51×** | +3.1 | 0.065 | 14/36 (SW1417, HepG2/C3A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 70 in all, 12 with an alert ⚠; shown: the 15 strongest. 70 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5548.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.0896×** | -19.1 | 0e+00 | 36/36 (RPMI-7951, BT-474, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.114×** | -17.1 | 0e+00 | 36/37 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Tofacitinib (drug)]] 5 µM |  | **0.243×** | -15.8 | 0e+00 | 30/37 (CFPAC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.147×** | -15.1 | 0e+00 | 36/37 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.162×** | -14.4 | 8e-45 | 32/36 (RPMI-7951, A549, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.292×** | -13.7 | 8e-41 | 32/37 (A498, NCI-H1573, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.293×** | -13.7 | 1e-40 | 28/35 (A549, BT-474, …) | top dose only | cell-cycle shift (explains ~23% here); composition shift |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.297×** | -13.5 | 8e-40 | 29/37 (A549, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.209×** | -12.4 | 3e-33 | 31/37 (LoVo, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.237×** | -11.4 | 3e-28 | 31/36 (SK-MEL-2, KATO III, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.232×** | -10.9 | 8e-26 | 34/37 (A549, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.266×** | -10.4 | 7e-24 | 30/36 (BT-474, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.268×** | -10.4 | 1e-23 | 29/37 (A549, BT-474, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.261×** | -10.0 | 6e-22 | 31/37 (BT-474, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.283×** | -10.0 | 9e-22 | 30/36 (NCI-H1792, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5548. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 40.6 | 0 | 27 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0389× (z -25.2) |
| [[BT-474 (line)]] | alt | 34.4 | 0 | 25 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.00762× (z -23.2) |
| [[LoVo (line)]] | wt | 68.6 | 0 | 24 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0191× (z -23.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.0354× (z -19.6) |
| [[NCI-H1573 (line)]] | alt | 21.2 | 0 | 18 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0642× (z -19.2) |
| [[COLO 205 (line)]] | alt | 75.9 | 0 | 17 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0901× (z -14.6) |
| [[KATO III (line)]] | alt | 48.9 | 0 | 16 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0145× (z -20.3) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0293× (z -17.6) |
| [[RPMI-7951 (line)]] | alt | 50.6 | 0 | 16 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.00548× (z -28.6) |
| [[SNU-423 (line)]] | alt | 24.2 | 0 | 16 (2 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0160× (z -18.9) |
| [[AsPC-1 (line)]] | alt | 20.0 | 0 | 15 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0528× (z -14.4) |
| [[A-172 (line)]] | wt | 53.4 | 0 | 14 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0344× (z -20.3) |
| [[NCI-H1792 (line)]] | alt | 26.2 | 0 | 14 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0179× (z -17.3) |
| [[A498 (line)]] | wt | 22.8 | 0 | 13 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0779× (z -18.2) |
| [[NCI-H2347 (line)]] | alt | 38.9 | 0 | 13 (3 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.164× (z -15.5) |
| [[CFPAC-1 (line)]] | alt | 40.2 | 0 | 11 (2 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.116× (z -17.6) |
| [[MIA PaCa-2 (line)]] | alt | 17.1 | 0 | 10 | — | [[Panobinostat (drug)]] 5 µM 0.0383× (z -13.3) |
| [[RKO (line)]] | wt | 26.0 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0295× (z -15.2) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.113× (z -13.3) |
| [[SK-MEL-2 (line)]] | alt | 23.9 | 0 | 9 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0310× (z -15.3) |
| [[HepG2_C3A (line)]] | wt | 23.4 | 0 | 8 | — | [[Digitoxin (drug)]] 0.5 µM 0.0219× (z -13.7) |
| [[HS-578T (line)]] | alt | 13.2 | 0 | 8 | — | [[Belinostat (drug)]] 5 µM 0.00904× (z -19.9) |
| [[SW1417 (line)]] | alt | 21.9 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.0942× (z -14.0) |
| [[SHP-77 (line)]] | alt | 22.8 | 0 | 6 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0152× (z -15.7) |
| [[Panc 03.27 (line)]] | alt | 41.0 | 0 | 5 | — | [[Tofacitinib (drug)]] 5 µM 0.249× (z -9.3) |
| [[A-427 (line)]] | wt | 5.94 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0760× (z -10.4) |
| [[C-33 A (line)]] | alt | 16.4 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.0469× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 12.1 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.116× (z -12.4) |
| [[SNU-1 (line)]] | wt | 14.0 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.0428× (z -9.1) |
| [[CHP-212 (line)]] | wt | 15.1 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0251× (z -8.8) |
| [[Hs 766T (line)]] | wt | 16.7 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.116× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 8.25 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.112× (z -9.4) |
| [[SW 900 (line)]] | alt | 14.3 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.187× (z -8.6) |
| [[AN3 CA (line)]] | alt | 2.94 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.74 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.30 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.37 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.59 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.71 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.10 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.72 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.81 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.41 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.67 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.92 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.56 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5548), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OAS2]] | +0.97 | +0.93 / +0.97 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 794 |
| [[MX1]] | +0.96 | +0.92 / +0.97 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 811 |
| [[USP18]] | +0.96 | +0.94 / +0.96 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 883 |
| [[OAS1]] | +0.95 | +0.92 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 776 |
| [[PARP9]] | +0.94 | +0.89 / +0.96 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 769 |
| [[OAS3]] | +0.94 | +0.91 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 724 |
| [[IFIT1]] | +0.93 | +0.91 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 830 |
| [[IFI44]] | +0.93 | +0.89 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 790 |
| [[PLSCR1]] | +0.92 | +0.87 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 456 |
| [[XAF1]] | +0.92 | +0.83 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 653 |
| [[HERC6]] | +0.92 | +0.90 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 685 |
| [[RSAD2]] | +0.92 | +0.88 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 976; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[IFIT3]] | +0.92 | +0.87 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 904 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*61 arrows, 61 of them with an alert ⚠; grade A 0, B 45, C 16. Shown: the 12 strongest; 49 more arrows (49 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SRMS]] | B | SRMS activity raises CMPK2's level | lines that do not express SRMS (14) vs lines expressing it (36) | 3.56× lower at baseline in the lines without SRMS | 2e-04 | ⚠ within organs, on part of the lines; also absent: MX1, OAS2, RSAD2 |
| [[TRIM22]] | B | TRIM22 activity raises CMPK2's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 3.28× lower at baseline in the lines without TRIM22 | 6e-04 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[RASGRP3]] | B | RASGRP3 activity raises CMPK2's level | lines that do not express RASGRP3 (16) vs lines expressing it (34) | 3.51× lower at baseline in the lines without RASGRP3 | 7e-04 | ⚠ within organs, on part of the lines; also absent: IFI6, SLC15A3, GBP4; maybe low, not absent |
| [[RSAD2]] | B | RSAD2 activity raises CMPK2's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 3.45× lower at baseline in the lines without RSAD2 | 0.001 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[MX1]] | B | MX1 activity raises CMPK2's level | lines that do not express MX1 (19) vs lines expressing it (31) | 3.04× lower at baseline in the lines without MX1 | 0.001 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[PLSCR1]] | B | PLSCR1 activity raises CMPK2's level | lines that do not express PLSCR1 (8) vs lines expressing it (42) | 3.88× lower at baseline in the lines without PLSCR1 | 0.001 | ⚠ within organs, on part of the lines; also absent: PARP9, ENSG00000279320, IFI6; maybe low, not absent |
| [[IFI27]] | B | IFI27 activity raises CMPK2's level | lines that do not express IFI27 (21) vs lines expressing it (29) | 2.95× lower at baseline in the lines without IFI27 | 0.001 | ⚠ within organs, on part of the lines; also absent: TRIM22, OAS2, RSAD2 |
| [[SAMD9L]] | B | SAMD9L activity raises CMPK2's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 2.59× lower at baseline in the lines without SAMD9L | 0.002 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[GBP4]] | B | GBP4 activity raises CMPK2's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 2.59× lower at baseline in the lines without GBP4 | 0.002 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[ETV7]] | B | ETV7 activity raises CMPK2's level | lines that do not express ETV7 (13) vs lines expressing it (37) | 2.26× lower at baseline in the lines without ETV7 | 0.002 | ⚠ within organs, on part of the lines; also absent: TUBA4A, AGMAT, ANO9; maybe low, not absent |
| [[IFI6]] | B | IFI6 activity raises CMPK2's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 3.61× lower at baseline in the lines without IFI6 | 0.003 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[SLC15A3]] | B | SLC15A3 activity raises CMPK2's level | lines that do not express SLC15A3 (16) vs lines expressing it (34) | 2.63× lower at baseline in the lines without SLC15A3 | 0.005 | ⚠ within organs, on part of the lines; also absent: XAF1, MX2, GBP4 |

### Downstream of this gene

*73 arrows, 73 of them with an alert ⚠; grade A 0, B 66, C 7. Shown: the 12 strongest; 61 more arrows (61 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HERC6]] | B | CMPK2 activity raises HERC6's level | lines that do not express CMPK2 (11) vs lines expressing it (39) | 3.10× lower at baseline in the lines without CMPK2 | 4e-04 | ⚠ within organs, on part of the lines; also absent: OAS2, NRIR, OAS1 |
| [[OAS3]] | B | CMPK2 activity raises OAS3's level | lines that do not express CMPK2 (11) vs lines expressing it (39) | 3.37× lower at baseline in the lines without CMPK2 | 0.001 | ⚠ within organs, on part of the lines; also absent: OAS2, NRIR, OAS1 |
| [[PARP10]] | B | CMPK2 activity raises PARP10's level | lines that do not express CMPK2 (11) vs lines expressing it (39) | 2.01× lower at baseline in the lines without CMPK2 | 0.001 | ⚠ within organs, on part of the lines; also absent: OAS2, NRIR, OAS1 |
| [[TRIM14]] | B | CMPK2 activity raises TRIM14's level | lines that do not express CMPK2 (11) vs lines expressing it (39) | 2.14× lower at baseline in the lines without CMPK2 | 0.002 | ⚠ within organs, on part of the lines; also absent: OAS2, NRIR, OAS1 |
| [[USP18]] | B | CMPK2 activity raises USP18's level | lines that do not express CMPK2 (11) vs lines expressing it (39) | 2.90× lower at baseline in the lines without CMPK2 | 0.002 | ⚠ within organs, on part of the lines; also absent: OAS2, NRIR, OAS1 |
| [[PLSCR1]] | B | CMPK2 activity raises PLSCR1's level | lines that do not express CMPK2 (11) vs lines expressing it (39) | 2.79× lower at baseline in the lines without CMPK2 | 0.003 | ⚠ within organs, on part of the lines; also absent: OAS2, NRIR, OAS1 |
| [[EIF2AK2]] | B | CMPK2 activity raises EIF2AK2's level | lines that do not express CMPK2 (11) vs lines expressing it (39) | 2.13× lower at baseline in the lines without CMPK2 | 0.003 | ⚠ within organs, on part of the lines; also absent: OAS2, NRIR, OAS1 |
| [[NLRC5]] | B | CMPK2 activity raises NLRC5's level | lines that do not express CMPK2 (11) vs lines expressing it (39) | 2.32× lower at baseline in the lines without CMPK2 | 0.003 | ⚠ within organs, on part of the lines; also absent: OAS2, NRIR, OAS1 |
| [[DTX3L]] | B | CMPK2 activity raises DTX3L's level | lines that do not express CMPK2 (11) vs lines expressing it (39) | 2.15× lower at baseline in the lines without CMPK2 | 0.004 | ⚠ within organs, on part of the lines; also absent: OAS2, NRIR, OAS1 |
| [[TRIM25]] | B | CMPK2 activity raises TRIM25's level | lines that do not express CMPK2 (11) vs lines expressing it (39) | 1.77× lower at baseline in the lines without CMPK2 | 0.005 | ⚠ within organs, on part of the lines; also absent: OAS2, NRIR, OAS1 |
| [[MX2]] | B | CMPK2 activity strengthens MX2's drug response | lines that do not express CMPK2 (6) vs lines expressing it (27) | the lines without CMPK2 respond 0.49× as strongly (z diff +4.20); strongest at Fedratinib (hydrochloride hydrate) 5 µM: 0.65x vs 0.16x (z diff +7.4) | 0.006 | ⚠ within organs, on part of the lines; also absent: OAS2, NRIR, OAS1; target measured in part of the lines; artifact flags |
| [[HELZ2]] | B | CMPK2 activity raises HELZ2's level | lines that do not express CMPK2 (11) vs lines expressing it (39) | 2.33× lower at baseline in the lines without CMPK2 | 0.006 | ⚠ within organs, on part of the lines; also absent: OAS2, NRIR, OAS1 |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.953). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.7, 54.0); signed map (65.1, 31.8). **Vector** length 148, 57.8% of its response variance represented; |z| ≥ 3 in 1,520 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon* (control, mean cos +0.89 to 23); *Interferon Signaling* (reactome, mean cos +0.83 to 45); *Interferon alpha/beta signaling* (reactome, mean cos +0.87 to 27).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +8.0 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +7.4 | -1.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +5.0 | +4.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +4.4 | -6.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +1.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.9 | +5.0 |
|  | [[Docetaxel (drug)]] 5 µM |  | +3.9 | +4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | -1.5 |
|  | [[venetoclax (drug)]] 0.05 µM |  | +3.3 | +3.8 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -10.7 | -15.8 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -9.4 | -13.5 |
|  | [[Selinexor (drug)]] 5 µM |  | -8.9 | -13.7 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -8.8 | -10.4 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -8.6 | -10.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -7.9 | -14.4 |

## What is on record

|  |  |
|---|---|
| Name | cytidine/uridine monophosphate kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p25.2 — chr2:6,840,570-6,866,635 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TYKi, UMP-CMPK2, NDK |
| Gene groups (HGNC) | Cytidine/uridine monophosphate kinases |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, DNA_REPAIR, INTERFERON_GAMMA_RESPONSE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5EBM0](https://www.uniprot.org/uniprotkb/Q5EBM0) (UMP-CMP kinase 2, mitochondrial):

> Mitochondrial nucleotide monophosphate kinase needed for salvage dNTP synthesis that mediates immunomodulatory and antiviral activities through IFN-dependent and IFN-independent pathways. Restricts the replication of multiple viruses including flaviviruses or coronaviruses. Together with viperin/RSAD2 and ddhCTP, suppresses the replication of several coronaviruses through inhibition of the viral RNA-dependent RNA polymerase activities. Concerning flaviviruses, restricts RNA translation when …

**Summary**, from NCBI Gene [129607](https://www.ncbi.nlm.nih.gov/gene/129607):

> This gene encodes one of the enzymes in the nucleotide synthesis salvage pathway that may participate in terminal differentiation of monocytic cells. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Feb 2012]

**Accessions** — [HGNC:27015](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27015) · Entrez [129607](https://www.ncbi.nlm.nih.gov/gene/129607) · UniProt [Q5EBM0](https://www.uniprot.org/uniprotkb/Q5EBM0) · Ensembl [ENSG00000134326](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134326)

## Data

Gene col 5548: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5548); `tables/drug_effects.parquet` (88 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5548, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5548]; `tensor/DDL_lfc|DDL_z.npy` [5548]; `embed/gene_vectors.npy` [5548]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5548 or target_col == 5548). Every well: [[CMPK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CMPK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
