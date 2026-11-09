---
symbol: "NT5C3A"
type: "gene"
col: 4360
ensembl_id: "ENSG00000122643"
name: "5'-nucleotidase, cytosolic IIIA"
location: "7p14.3"
module: 70
arm: "+"
pooled_cpm: 117.93
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 1
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 14
direction_downstream: 0
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# NT5C3A

*5'-nucleotidase, cytosolic IIIA* — 7p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 1.57× (z +10.0, q 6e-21, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.791× (z -4.8, q 7e-04, down in 24 of 45 measured lines) ⚠ toxic; transcription drop.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Tofacitinib (drug)]] 5 µM in 6 lines (CFPAC-1 0.440×, NCI-H2347 0.492×, A498 0.587×, Panc 03.27 0.567×, …); [[Dinaciclib (drug)]] 5 µM in 4 lines (HEC-1-A 0.235×, SHP-77 0.183×, C32 0.165×, NCI-H2347 0.384×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (COLO 205 0.173×, C32 0.233×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (COLO 205 0.364×, C32 0.320×); [[5-Azacytidine (drug)]] 0.5 µM in 1 line (SW 1088 0.0736×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LYN]] (+0.61, fdr 1e-05), [[MVB12A]] (+0.61, fdr 1e-05), [[UBE2L6]] (+0.56, fdr 3e-05); moves opposite to [[THOC6]] (-0.52, fdr 2e-05), [[LAMC1]] (-0.50, fdr 7e-05), [[CYREN]] (-0.48, fdr 5e-05).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[DUOX2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4360.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.57×** | +10.0 | 6e-21 | 35/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.52×** | +9.4 | 2e-18 | 36/48 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.39×** | +7.3 | 4e-11 | 31/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.22×** | +4.4 | 0.002 | 23/48 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~3% of this change | 1.19× | +3.9 | 0.011 | 20/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Terfenadine (drug)]] 5 µM |  | 1.12× | +3.7 | 0.021 | 8/48 (SNU-423, SK-MEL-2, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 1.17× | +3.6 | 0.029 | 17/48 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~8% of this change | 1.17× | +3.3 | 0.062 | 20/47 (NCI-H460, J82, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.062 | 19/48 (PANC-1, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4360.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Tofacitinib (drug)]] 5 µM in 6 lines (CFPAC-1 0.440×, NCI-H2347 0.492×, A498 0.587×, Panc 03.27 0.567×, …); [[Dinaciclib (drug)]] 5 µM in 4 lines (HEC-1-A 0.235×, SHP-77 0.183×, C32 0.165×, NCI-H2347 0.384×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (COLO 205 0.173×, C32 0.233×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (COLO 205 0.364×, C32 0.320×); [[5-Azacytidine (drug)]] 0.5 µM in 1 line (SW 1088 0.0736×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.791×** | -4.8 | 7e-04 | 24/45 (C32, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.861× | -4.7 | 7e-04 | 14/48 (A-427, C32, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.953× | -3.8 | 0.024 | 1/50 (NCI-H23) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 0.848× | -3.7 | 0.036 | 21/48 (C32, NCI-H2347, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.863× | -3.3 | 0.12 | 15/48 (LoVo, AsPC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.865× | -3.2 | 0.12 | 20/49 (COLO 205, C32, …) | all doses, flat | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4360. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 307 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.320× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 282 | 3 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +10.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Trametinib (drug)]] 0.5 µM 1.98× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.425× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.590× (z -8.5) |
| [[COLO 205 (line)]] | alt | 353 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.364× (z -9.1) |
| [[A-172 (line)]] | wt | 111 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.28× (z +14.9) ⚠ cell-cycle shift, explains ~16% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.00× (z +8.7) | — |
| [[NCI-H2347 (line)]] | alt | 141 | 1 (1 ⚠) | 3 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.53× (z +11.0) ⚠ cell-cycle shift, explains ~13% of this change | [[Tofacitinib (drug)]] 5 µM 0.492× (z -11.9) |
| [[NCI-H460 (line)]] | wt | 81.4 | 4 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.61× (z +13.2) | — |
| [[A498 (line)]] | wt | 159 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.16× (z +9.8) ⚠ cell-cycle shift, explains ~16% of this change | [[Tofacitinib (drug)]] 5 µM 0.587× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 134 | 1 (1 ⚠) | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.44× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Tofacitinib (drug)]] 5 µM 0.440× (z -12.6) |
| [[HEC-1-A (line)]] | alt | 114 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +10.9) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.235× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 147 | 0 | 1 | — | [[Tofacitinib (citrate) (drug)]] 0.5 µM 0.365× (z -9.2) |
| [[BT-474 (line)]] | alt | 80.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +12.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HepG2_C3A (line)]] | wt | 93.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -13.1) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 64.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +11.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LoVo (line)]] | wt | 152 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.611× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 98.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.560× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 67.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[Panc 03.27 (line)]] | alt | 113 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.567× (z -9.0) |
| [[SHP-77 (line)]] | alt | 209 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.183× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 166 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.424× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 1088 (line)]] | alt | 129 | 0 | 1 | — | [[5-Azacytidine (drug)]] 0.5 µM 0.0736× (z -10.3) |
| [[SW1417 (line)]] | alt | 115 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.464× (z -9.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 120 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.01× (z +9.8) | — |
| [[A-427 (line)]] | wt | 72.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 120 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 92.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 68.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 123 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 81.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 81.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 88.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 50.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 171 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 53.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 141 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 79.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 72.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 85.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 80.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 78.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 75.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 69.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 199 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4360), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LYN]] | +0.61 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[MVB12A]] | +0.61 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[UBE2L6]] | +0.56 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[PSMB9]] | +0.54 | +0.43 / +0.67 | both halves | 3e-05 |  |
| [[TNFSF10]] | +0.53 | +0.44 / +0.66 | both halves | 3e-05 |  |
| [[IFITM1]] | +0.53 | +0.35 / +0.66 | both halves | 1e-04 |  |
| [[CFB]] | +0.53 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[GBP4]] | +0.53 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[GBP2]] | +0.53 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[LY6E]] | +0.52 | +0.30 / +0.67 | both halves | 2e-04 |  |
| [[BTN3A2]] | +0.52 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[SRI]] | +0.51 | +0.49 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THOC6]] | -0.52 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[LAMC1]] | -0.50 | -0.37 / -0.46 | both halves | 7e-05 |  |
| [[CYREN]] | -0.48 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[MSANTD2]] | -0.48 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[SEC14L1]] | -0.46 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[PPP1R3F]] | -0.46 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[ERMAP]] | -0.46 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[BRD9]] | -0.45 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[ZNF655]] | -0.44 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[TAOK2]] | -0.44 | -0.43 / -0.36 | both halves | 1e-04 |  |
| [[CCDC9B]] | -0.44 | -0.36 / -0.38 | both halves | 1e-04 |  |
| [[ZNF577]] | -0.43 | -0.34 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 14, C 0. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DUOX2]] | B | DUOX2 activity raises NT5C3A's level | lines that do not express DUOX2 (32) vs lines expressing it (18) | 1.58× lower at baseline in the lines without DUOX2 | 0.012 | ⚠ within organs, on part of the lines; also absent: MMP7, SLC44A4, MAOB |
| [[TRIM31]] | B | TRIM31 activity raises NT5C3A's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 1.73× lower at baseline in the lines without TRIM31 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1 |
| [[RNF128]] | B | RNF128 activity raises NT5C3A's level | lines that do not express RNF128 (23) vs lines expressing it (27) | 1.50× lower at baseline in the lines without RNF128 | 0.025 | ⚠ within organs, on part of the lines; also absent: AZGP1, RNF43, PROM1 |
| [[HSH2D]] | B | HSH2D activity raises NT5C3A's level | lines that do not express HSH2D (27) vs lines expressing it (23) | 1.51× lower at baseline in the lines without HSH2D | 0.026 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM; maybe low, not absent |
| [[APOL1]] | B | APOL1 activity raises NT5C3A's level | lines that do not express APOL1 (24) vs lines expressing it (26) | 1.49× lower at baseline in the lines without APOL1 | 0.031 | ⚠ within organs, on part of the lines; also absent: POU5F1, UGT1A6, NMRAL2P-1 |
| [[BST2]] | B | BST2 activity raises NT5C3A's level | lines that do not express BST2 (18) vs lines expressing it (32) | 1.42× lower at baseline in the lines without BST2 | 0.044 | ⚠ within organs, on part of the lines; also absent: CCDC194, DEPP1, SLC15A3 |
| [[PDZK1IP1]] | B | PDZK1IP1 activity raises NT5C3A's level | lines that do not express PDZK1IP1 (32) vs lines expressing it (18) | 1.50× lower at baseline in the lines without PDZK1IP1 | 0.051 | ⚠ within organs, on part of the lines; also absent: MUC5B, UCA1, PRSS8 |
| [[HDAC6]] | B | HDAC6 activity lowers NT5C3A's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ELF3]] | B | ELF3 activity raises NT5C3A's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 1.33× lower at baseline in the lines without ELF3 | 0.063 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |
| [[GBP4]] | B | GBP4 activity raises NT5C3A's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 1.21× lower at baseline in the lines without GBP4 | 0.077 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[HERC5]] | B | HERC5 activity lowers NT5C3A's level | lines that do not express HERC5 (15) vs lines expressing it (35) | 1.51× higher at baseline in the lines without HERC5 | 0.085 | ⚠ within organs, on part of the lines; also absent: RAB31, CACNG6, MYOSLID |
| [[XAF1]] | B | XAF1 activity raises NT5C3A's level | lines that do not express XAF1 (14) vs lines expressing it (36) | 1.31× lower at baseline in the lines without XAF1 | 0.085 | ⚠ within organs, on part of the lines; also absent: SLC15A3, TRIM22, FBXO39 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.485). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (51.5, 52.9); signed map (67.7, 30.0). **Vector** length 127, 35.7% of its response variance represented; |z| ≥ 3 in 1,115 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +4.2 | +10.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.3 | +1.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.3 | +2.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.1 | +7.3 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.9 | +3.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.8 | +1.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.7 | +1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +0.8 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -5.0 | -2.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -4.7 | -3.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.7 | -1.9 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -4.5 | -2.1 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -4.0 | -2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.6 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | 5'-nucleotidase, cytosolic IIIA |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.3 — chr7:33,014,130-33,062,796 (-) |
| Ensembl biotype | protein_coding |
| Also known as | UMPH1, PSN1, PN-I, UMPH, P5'N-1, cN-III, p36, POMP; previously NT5C3 |
| Gene groups (HGNC) | 5'-nucleotidases |
| Hallmark sets | DNA_REPAIR |
| Reactome | 3 pathways, smallest: Pyrimidine catabolism; Nucleotide catabolism; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0P0](https://www.uniprot.org/uniprotkb/Q9H0P0) (Cytosolic 5'-nucleotidase 3A):

> Nucleotidase which shows specific activity towards cytidine monophosphate (CMP) and 7-methylguanosine monophosphate (m(7)GMP). CMP seems to be the preferred substrate.

**Summary**, from NCBI Gene [51251](https://www.ncbi.nlm.nih.gov/gene/51251):

> This gene encodes a member of the 5'-nucleotidase family of enzymes that catalyze the dephosphorylation of nucleoside 5'-monophosphates. The encoded protein is the type 1 isozyme of pyrimidine 5' nucleotidase and catalyzes the dephosphorylation of pyrimidine 5' monophosphates. Mutations in this gene are a cause of hemolytic anemia due to uridine 5-prime monophosphate hydrolase deficiency. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene, and …

**Accessions** — [HGNC:17820](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17820) · Entrez [51251](https://www.ncbi.nlm.nih.gov/gene/51251) · UniProt [Q9H0P0](https://www.uniprot.org/uniprotkb/Q9H0P0) · Ensembl [ENSG00000122643](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122643)

## Data

Gene col 4360: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4360); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4360, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4360]; `tensor/DDL_lfc|DDL_z.npy` [4360]; `embed/gene_vectors.npy` [4360]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4360 or target_col == 4360). Every well: [[NT5C3A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NT5C3A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
