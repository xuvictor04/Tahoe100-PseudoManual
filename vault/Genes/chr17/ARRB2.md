---
symbol: "ARRB2"
type: "gene"
col: 6528
ensembl_id: "ENSG00000141480"
name: "arrestin beta 2"
location: "17p13.2"
module: 83
arm: "-"
pooled_cpm: 13.67
n_lines_expressing: 48
n_dd_up: 16
n_dd_down: 10
n_dd_up_clean: 9
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 12
direction_downstream: 0
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# ARRB2

*arrestin beta 2* — 17p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 3.13× (z +14.9, q 0e+00, up in 44 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.720× (z -6.0, q 9e-07, down in 25 of 45 measured lines).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMARCD3]] (+0.76, fdr 7e-06), [[HACE1]] (+0.75, fdr 1e-05), [[PAFAH1B3]] (+0.71, fdr 2e-05); moves opposite to [[DNAJB14]] (-0.72, fdr 1e-05), [[PPP3CB-AS1]] (-0.71, fdr 1e-04), [[MMADHC-DT]] (-0.71, fdr 5e-05).
> It sits in the **-** arm of [[Module 083]].
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[SEMA6B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6528.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **3.13×** | +14.9 | 0e+00 | 44/45 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.91×** | +14.0 | 7e-42 | 44/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.49×** | +12.0 | 1e-30 | 43/45 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.11×** | +9.8 | 2e-20 | 29/36 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.68×** | +9.7 | 5e-20 | 37/46 (SW480, LS 180, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.00×** | +9.1 | 1e-17 | 40/46 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.88×** | +7.9 | 2e-13 | 16/23 (J82, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.72×** | +7.1 | 7e-11 | 30/44 (KATO III, BT-474, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.71×** | +7.0 | 1e-10 | 23/40 (HS-578T, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.65×** | +6.1 | 6e-08 | 18/29 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.19×** | +5.4 | 4e-06 | 22/46 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +4.4 | 4e-04 | 21/44 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +4.3 | 8e-04 | 15/42 (SW480, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.20×** | +3.4 | 0.026 | 17/46 (NCI-H1792, SHP-77, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 1.19× | +3.3 | 0.035 | 11/46 (PANC-1, NCI-H1573, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6528.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.720×** | -6.0 | 9e-07 | 25/45 (NCI-H2030, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.495×** | -4.8 | 5e-04 | 18/43 (PANC-1, SW 900, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.715×** | -4.4 | 0.002 | 21/45 (NCI-H1792, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.716×** | -4.3 | 0.002 | 19/45 (RPMI-7951, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.723×** | -4.2 | 0.004 | 18/45 (MIA PaCa-2, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.736×** | -4.0 | 0.006 | 18/46 (LOX-IMVI, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.720×** | -3.8 | 0.012 | 18/45 (SW480, RKO, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.815×** | -3.8 | 0.012 | 20/44 (NCI-H23, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.581×** | -3.7 | 0.013 | 17/46 (NCI-H23, SNU-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.757×** | -3.6 | 0.016 | 15/45 (SW 1271, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6528. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 13.6 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.10× (z +10.7) | — |
| [[A-427 (line)]] | wt | 30.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -10.5) |
| [[J82 (line)]] | alt | 15.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.22× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 28.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -12.0) |
| [[NCI-H23 (line)]] | alt | 22.2 | 0 | 2 | — | [[TAK-901 (drug)]] 5 µM 0.0631× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 15.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -9.0) |
| [[RKO (line)]] | wt | 51.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.195× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.365× (z -11.8) |
| [[KATO III (line)]] | alt | 15.5 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.48× (z +8.8) | — |
| [[LOX-IMVI (line)]] | wt | 11.2 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.286× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 21.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.111× (z -14.3) |
| [[RPMI-7951 (line)]] | alt | 7.40 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.101× (z -8.8) |
| [[SW1417 (line)]] | alt | 10.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.171× (z -9.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 7.08 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.64 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.69 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.23 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.94 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.18 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.88 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6528), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMARCD3]] | +0.76 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[HACE1]] | +0.75 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[PAFAH1B3]] | +0.71 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[STX7]] | +0.70 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[KCTD17]] | +0.70 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[PEDS1]] | +0.69 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[MAST3]] | +0.69 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[RSAD1]] | +0.68 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[ARL6]] | +0.68 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[ALAD]] | +0.68 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[TCIRG1]] | +0.68 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[CDON]] | +0.67 | +0.55 / +0.51 | both halves | 1e-05 | pathway: Activation of SMO |

## Genes that move opposite

*50 of its nearest partners move opposite, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJB14]] | -0.72 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[PPP3CB-AS1]] | -0.71 | -0.55 / -0.33 | both halves | 1e-04 |  |
| [[MMADHC-DT]] | -0.71 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[LINC00571]] | -0.70 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[MZF1-AS1]] | -0.70 | -0.53 / -0.29 | both halves | 2e-04 |  |
| [[PBLD]] | -0.69 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[EFCAB2]] | -0.69 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[CCDC90B-AS1]] | -0.69 | -0.52 / -0.29 | both halves | 2e-04 |  |
| [[SPRY3]] | -0.69 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[WARS2-AS1]] | -0.68 | -0.50 / -0.36 | both halves | 9e-05 |  |
| [[PKN2-AS1]] | -0.67 | -0.46 / -0.32 | both halves | 2e-04 |  |
| [[INO80D]] | -0.67 | -0.40 / -0.46 | both halves | 5e-05 | pathway: Deubiquitination |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 10, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEMA6B]] | B | SEMA6B activity raises ARRB2's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 1.76× lower at baseline in the lines without SEMA6B | 0.002 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[GNAZ]] | B | GNAZ activity raises ARRB2's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 2.01× lower at baseline in the lines without GNAZ | 0.018 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[ENPP5]] | B | ENPP5 activity lowers ARRB2's level | lines that do not express ENPP5 (27) vs lines expressing it (23) | 1.20× higher at baseline in the lines without ENPP5 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ESRP1, ENSG00000243004 |
| [[NXPH4]] | B | NXPH4 activity raises ARRB2's level | lines that do not express NXPH4 (13) vs lines expressing it (37) | 1.70× lower at baseline in the lines without NXPH4 | 0.043 | ⚠ within organs, on part of the lines; also absent: LINC01234; maybe low, not absent |
| [[BCAM]] | B | BCAM activity raises ARRB2's level | lines that do not express BCAM (8) vs lines expressing it (42) | 1.94× lower at baseline in the lines without BCAM | 0.057 | ⚠ within organs, on part of the lines; also absent: DNMT3B; maybe low, not absent |
| [[MPP2]] | B | MPP2 activity raises ARRB2's level | lines that do not express MPP2 (7) vs lines expressing it (43) | 1.61× lower at baseline in the lines without MPP2 | 0.074 | ⚠ within organs, on part of the lines; also absent: FAM229B, STARD9, CNN3-DT |
| [[KATNAL1]] | B | KATNAL1 activity raises ARRB2's level | lines that do not express KATNAL1 (7) vs lines expressing it (43) | 1.48× lower at baseline in the lines without KATNAL1 | 0.089 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17 |
| [[LYPD5]] | B | LYPD5 activity lowers ARRB2's level | lines that do not express LYPD5 (16) vs lines expressing it (34) | 1.30× higher at baseline in the lines without LYPD5 | 0.095 | ⚠ within organs, on part of the lines; also absent: AGMAT, ZNF320, LIPG; maybe low, not absent |
| [[ATP1A3]] | B | ATP1A3 activity raises ARRB2's level | lines that do not express ATP1A3 (12) vs lines expressing it (38) | 1.40× lower at baseline in the lines without ATP1A3 | 0.096 | ⚠ within organs, on part of the lines; also absent: KIF26A; maybe low, not absent |
| [[FHIP1A]] | B | FHIP1A activity lowers ARRB2's level | lines that do not express FHIP1A (7) vs lines expressing it (43) | 1.75× higher at baseline in the lines without FHIP1A | 0.097 | ⚠ within organs, on part of the lines; also absent: SLC18B1, NIPAL1, TXNIP; maybe low, not absent |
| [[RFX3-DT]] | C | RFX3-DT activity raises ARRB2's level | lines that do not express RFX3-DT (3) vs lines expressing it (47) | 2.56× lower at baseline in the lines without RFX3-DT | 0.077 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent |
| [[DNMT3B]] | C | DNMT3B activity raises ARRB2's level | lines that do not express DNMT3B (4) vs lines expressing it (46) | 2.24× lower at baseline in the lines without DNMT3B | 0.095 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CCDC113, SLC29A4, MYBL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **-** arm (projection on the module's main direction -0.767). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (9.2, -5.2); signed map (-33.0, -6.9). **Vector** length 77.0, 15.1% of its response variance represented; |z| ≥ 3 in 867 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +9.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.5 | +12.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.4 | +9.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.1 | +14.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.1 | +4.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.3 | +5.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +3.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +1.0 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +1.6 | +1.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.2 | -3.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.3 | -6.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.7 | -4.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | -1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.5 | -2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -1.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.0 | -0.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.8 | -3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | arrestin beta 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.2 — chr17:4,710,596-4,721,499 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BARR2, DKFZp686L0365; previously ARR2 |
| Gene groups (HGNC) | Classical arrestins |
| Hallmark sets | UV_RESPONSE_UP |
| Reactome | 38 pathways, smallest: TGFBR3 regulates TGF-beta signaling; WNT5A-dependent internalization of FZD4; Activation of SMO |
| Matched by | ensembl_id |

**Function**, from UniProt [P32121](https://www.uniprot.org/uniprotkb/P32121) (Beta-arrestin-2):

> Functions in regulating agonist-mediated G protein-coupled receptor (GPCR) signaling by mediating both receptor desensitization and resensitization processes. During homologous desensitization, beta-arrestins bind to the GPCR-phosphorylated receptor and sterically preclude its coupling to the cognate G protein; the binding appears to require additional receptor determinants exposed only in the active receptor conformation. The beta-arrestins target many receptors for internalization by acting …

**Summary**, from NCBI Gene [409](https://www.ncbi.nlm.nih.gov/gene/409):

> Members of arrestin/beta-arrestin protein family are thought to participate in agonist-mediated desensitization of G-protein-coupled receptors and cause specific dampening of cellular responses to stimuli such as hormones, neurotransmitters, or sensory signals. Arrestin beta 2, like arrestin beta 1, was shown to inhibit beta-adrenergic receptor function in vitro. It is expressed at high levels in the central nervous system and may play a role in the regulation of synaptic receptors. Besides the …

**Accessions** — [HGNC:712](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:712) · Entrez [409](https://www.ncbi.nlm.nih.gov/gene/409) · UniProt [P32121](https://www.uniprot.org/uniprotkb/P32121) · Ensembl [ENSG00000141480](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141480)

## Data

Gene col 6528: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6528); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6528, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6528]; `tensor/DDL_lfc|DDL_z.npy` [6528]; `embed/gene_vectors.npy` [6528]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6528 or target_col == 6528). Every well: [[ARRB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARRB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
