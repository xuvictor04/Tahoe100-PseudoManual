---
symbol: "TRIM34"
type: "gene"
col: 15126
ensembl_id: "ENSG00000258659"
name: "tripartite motif containing 34"
location: "11p15.4"
module: 32
arm: "+"
pooled_cpm: 4.59
n_lines_expressing: 44
n_dd_up: 8
n_dd_down: 25
n_dd_up_clean: 5
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 22
direction_downstream: 21
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# TRIM34

*tripartite motif containing 34* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.67× (z +4.9, q 3e-04, up in 16 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.423× (z -11.8, q 2e-29, down in 26 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OAS1]] (+0.73, fdr 9e-06), [[IFI44]] (+0.73, fdr 9e-06), [[OAS2]] (+0.71, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[GBP1]] → it (grade B ⚠); 21 go from it, the strongest it → [[TRIM5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15126.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.67×** | +4.9 | 3e-04 | 16/35 (SK-MEL-2, A498, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.71×** | +4.9 | 3e-04 | 4/12 (J82, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +4.7 | 5e-04 | 2/8 (J82, PANC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.61×** | +4.7 | 5e-04 | 15/38 (AsPC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.49×** | +3.7 | 0.020 | 12/36 (A498, NCI-H23, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.021 | 8/40 (LoVo, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.39×** | +3.2 | 0.098 | 2/20 (J82, NCI-H2030) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Carbamazepine (drug)]] 5 µM |  | **1.38×** | +3.2 | 0.098 | 3/39 (HT-29, COLO 205, …) | top dose only |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 1.37× | +3.1 | 0.11 | 5/39 (NCI-H2347, COLO 205, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.29× | +3.1 | 0.12 | 5/38 (AsPC-1, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15126.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.423×** | -11.8 | 2e-29 | 26/31 (SNU-423, A498, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.319×** | -11.1 | 4e-26 | 32/38 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.336×** | -10.6 | 5e-24 | 35/39 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.414×** | -8.6 | 2e-15 | 24/30 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.444×** | -7.9 | 4e-13 | 23/36 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.468×** | -7.4 | 2e-11 | 20/31 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.548×** | -5.8 | 4e-07 | 14/39 (NCI-H23, BT-474, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.563×** | -5.6 | 2e-06 | 21/39 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.676×** | -5.4 | 5e-06 | 20/36 (A-172, RKO, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.591×** | -5.1 | 2e-05 | 13/36 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.617×** | -4.7 | 1e-04 | 15/39 (PANC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.617×** | -4.7 | 1e-04 | 15/39 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.606×** | -4.7 | 1e-04 | 13/33 (A549, PANC-1, …) | top dose only | cell-cycle shift (explains ~14% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.711×** | -4.7 | 1e-04 | 13/31 (HT-29, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.402×** | -4.6 | 1e-04 | 17/31 (SNU-423, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.714×** | -4.6 | 2e-04 | 15/37 (A-172, BT-474, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.624×** | -4.6 | 2e-04 | 14/32 (BT-474, COLO 205, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.414×** | -4.5 | 2e-04 | 14/34 (A549, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15126. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 5.61 | 0 | 8 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0699× (z -14.0) |
| [[A549 (line)]] | wt | 10.4 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0362× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.121× (z -12.9) |
| [[A498 (line)]] | wt | 10.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -13.8) |
| [[BT-474 (line)]] | alt | 14.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -12.5) |
| [[HT-29 (line)]] | alt | 3.86 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0276× (z -12.2) |
| [[A-172 (line)]] | wt | 10.1 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.103× (z -10.6) |
| [[Hs 766T (line)]] | wt | 9.47 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -11.4) |
| [[J82 (line)]] | alt | 6.39 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 11.3× (z +8.6) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.0938× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 5.03 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -11.6) |
| [[NCI-H2030 (line)]] | alt | 4.59 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0397× (z -12.2) |
| [[SNU-423 (line)]] | alt | 7.37 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0848× (z -14.7) |
| [[AsPC-1 (line)]] | alt | 5.00 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 3.46 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0308× (z -14.0) |
| [[A-427 (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.872 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.910 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.574 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.751 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.674 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15126), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OAS1]] | +0.73 | +0.57 / +0.83 | both halves | 9e-06 | pathway: Interferon Signaling |
| [[IFI44]] | +0.73 | +0.57 / +0.83 | both halves | 9e-06 | pathway: Interferon Signaling |
| [[OAS2]] | +0.71 | +0.58 / +0.81 | both halves | 7e-06 | pathway: Interferon Signaling |
| [[SAMHD1]] | +0.71 | +0.57 / +0.77 | both halves | 1e-05 | pathway: Interferon Signaling |
| [[UBE2L6]] | +0.70 | +0.56 / +0.78 | both halves | 1e-05 | pathway: Interferon Signaling |
| [[XAF1]] | +0.70 | +0.56 / +0.81 | both halves | 1e-05 | pathway: Interferon Signaling |
| [[EIF2AK2]] | +0.70 | +0.48 / +0.82 | both halves | 2e-05 | pathway: Interferon Signaling |
| [[SHFL]] | +0.70 | +0.48 / +0.80 | both halves | 2e-05 |  |
| [[UBA7]] | +0.69 | +0.60 / +0.76 | both halves | 7e-06 | pathway: Interferon Signaling |
| [[IFI44L]] | +0.69 | +0.53 / +0.78 | both halves | 1e-05 | pathway: Interferon Signaling |
| [[SAMD9L]] | +0.69 | +0.56 / +0.81 | both halves | 1e-05 |  |
| [[IFIT1]] | +0.69 | +0.56 / +0.79 | both halves | 1e-05 | pathway: Interferon Signaling |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 19, C 3. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GBP1]] | B | GBP1 activity raises TRIM34's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 2.18× lower at baseline in the lines without GBP1 | 0.005 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[GBP4]] | B | GBP4 activity raises TRIM34's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 2.14× lower at baseline in the lines without GBP4 | 0.006 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[IFI44]] | B | IFI44 activity raises TRIM34's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 2.15× lower at baseline in the lines without IFI44 | 0.008 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[MAP2K1]] | B | MAP2K1 activity lowers TRIM34's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.4% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds |
| [[SAMD9]] | B | SAMD9 activity raises TRIM34's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 2.33× lower at baseline in the lines without SAMD9 | 0.021 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6 |
| [[RSAD2]] | B | RSAD2 activity raises TRIM34's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 1.74× lower at baseline in the lines without RSAD2 | 0.026 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[TRIM6]] | B | TRIM6 activity raises TRIM34's level | lines that do not express TRIM6 (17) vs lines expressing it (33) | 2.07× lower at baseline in the lines without TRIM6 | 0.030 | ⚠ within organs, on part of the lines; also absent: TFPI2, KMO, ENSG00000289526 |
| [[ODF3B]] | B | ODF3B activity raises TRIM34's level | lines that do not express ODF3B (13) vs lines expressing it (37) | 1.49× lower at baseline in the lines without ODF3B | 0.033 | ⚠ within organs, on part of the lines; also absent: TYMP, RPP25, CGAS |
| [[GBP3]] | B | GBP3 activity raises TRIM34's level | lines that do not express GBP3 (11) vs lines expressing it (39) | 2.09× lower at baseline in the lines without GBP3 | 0.039 | ⚠ within organs, on part of the lines; also absent: PHLDA2, CD44, ITGA3 |
| [[OAS1]] | B | OAS1 activity raises TRIM34's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 1.63× lower at baseline in the lines without OAS1 | 0.040 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[OASL]] | B | OASL activity raises TRIM34's level | lines that do not express OASL (10) vs lines expressing it (40) | 1.81× lower at baseline in the lines without OASL | 0.048 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, GBP2, TENT5A; maybe low, not absent |
| [[TRIM38]] | B | TRIM38 activity raises TRIM34's level | lines that do not express TRIM38 (6) vs lines expressing it (44) | 2.17× lower at baseline in the lines without TRIM38 | 0.066 | ⚠ within organs, on part of the lines; also absent: SMOX, S100A13, ERAP2 |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 20, C 1. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIM5]] | B | TRIM34 activity raises TRIM5's level | lines that do not express TRIM34 (6) vs lines expressing it (44) | 2.02× lower at baseline in the lines without TRIM34 | 0.011 | ⚠ within organs, on part of the lines; also absent: BIRC3, FXYD5, TFAP2A; maybe low, not absent |
| [[NMI]] | B | TRIM34 activity raises NMI's level | lines that do not express TRIM34 (6) vs lines expressing it (44) | 3.09× lower at baseline in the lines without TRIM34 | 0.015 | ⚠ within organs, on part of the lines; also absent: BIRC3, FXYD5, TFAP2A; maybe low, not absent |
| [[GBP3]] | B | TRIM34 activity raises GBP3's level | lines that do not express TRIM34 (6) vs lines expressing it (44) | 4.94× lower at baseline in the lines without TRIM34 | 0.018 | ⚠ within organs, on part of the lines; also absent: BIRC3, FXYD5, TFAP2A; maybe low, not absent |
| [[IFIH1]] | B | TRIM34 activity raises IFIH1's level | lines that do not express TRIM34 (6) vs lines expressing it (44) | 2.82× lower at baseline in the lines without TRIM34 | 0.020 | ⚠ within organs, on part of the lines; also absent: BIRC3, FXYD5, TFAP2A; maybe low, not absent |
| [[ZNFX1]] | B | TRIM34 activity raises ZNFX1's level | lines that do not express TRIM34 (6) vs lines expressing it (44) | 1.68× lower at baseline in the lines without TRIM34 | 0.028 | ⚠ within organs, on part of the lines; also absent: BIRC3, FXYD5, TFAP2A; maybe low, not absent |
| [[ZC3HAV1]] | B | TRIM34 activity raises ZC3HAV1's level | lines that do not express TRIM34 (6) vs lines expressing it (44) | 1.79× lower at baseline in the lines without TRIM34 | 0.037 | ⚠ within organs, on part of the lines; also absent: BIRC3, FXYD5, TFAP2A; maybe low, not absent |
| [[TRANK1]] | B | TRIM34 activity raises TRANK1's level | lines that do not express TRIM34 (6) vs lines expressing it (44) | 3.06× lower at baseline in the lines without TRIM34 | 0.048 | ⚠ within organs, on part of the lines; also absent: BIRC3, FXYD5, TFAP2A; maybe low, not absent |
| [[IFI35]] | B | TRIM34 activity raises IFI35's level | lines that do not express TRIM34 (6) vs lines expressing it (44) | 2.27× lower at baseline in the lines without TRIM34 | 0.049 | ⚠ within organs, on part of the lines; also absent: BIRC3, FXYD5, TFAP2A; maybe low, not absent |
| [[OASL]] | B | TRIM34 activity raises OASL's level | lines that do not express TRIM34 (6) vs lines expressing it (44) | 3.69× lower at baseline in the lines without TRIM34 | 0.050 | ⚠ within organs, on part of the lines; also absent: BIRC3, FXYD5, TFAP2A; maybe low, not absent |
| [[IFIT1]] | B | TRIM34 activity raises IFIT1's level | lines that do not express TRIM34 (6) vs lines expressing it (44) | 2.46× lower at baseline in the lines without TRIM34 | 0.055 | ⚠ within organs, on part of the lines; also absent: BIRC3, FXYD5, TFAP2A; maybe low, not absent |
| [[PSMB9]] | B | TRIM34 activity raises PSMB9's level | lines that do not express TRIM34 (6) vs lines expressing it (44) | 2.47× lower at baseline in the lines without TRIM34 | 0.062 | ⚠ within organs, on part of the lines; also absent: BIRC3, FXYD5, TFAP2A; maybe low, not absent |
| [[DDX60]] | B | TRIM34 activity raises DDX60's level | lines that do not express TRIM34 (6) vs lines expressing it (44) | 3.36× lower at baseline in the lines without TRIM34 | 0.063 | ⚠ within organs, on part of the lines; also absent: BIRC3, FXYD5, TFAP2A; maybe low, not absent |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.705). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.0, 54.4); signed map (66.6, 31.7). **Vector** length 63.9, 11.4% of its response variance represented; |z| ≥ 3 in 946 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.59 to 56); *interferon gamma response* (hallmark, mean cos +0.59 to 60); *interferon* (control, mean cos +0.64 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +4.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.8 | +3.7 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.8 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.8 | +4.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.8 | +3.7 |
|  | [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | +1.6 | +2.1 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -2.7 | -5.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.6 | -11.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.5 | -3.1 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.4 | -2.7 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.3 | -4.2 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -2.3 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 34 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:5,619,764-5,644,398 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously RNF21 |
| Gene groups (HGNC) | Ring finger proteins; Tripartite motif family; RING finger E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Interferon gamma signaling; Interferon Signaling; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BYJ4](https://www.uniprot.org/uniprotkb/Q9BYJ4) (E3 ubiquitin-protein ligase TRIM34):

> Functions as antiviral protein and contributes to the defense against retroviral infections. Acts as a capsid-specific restriction factor with the help of TRIM5 and prevents infection from non-host-adapted retroviruses. During influenza A virus infection, promotes programmed cell death by targeting ZBP1 for 'Lys-63'-linked polyubiquitination. In turn, promotes ZBP1 recruitment of RIPK3 to mediate virus-induced programmed necrosis. Negatively regulates the function of mitochondria by enhancing …

**Summary**, from NCBI Gene [53840](https://www.ncbi.nlm.nih.gov/gene/53840):

> The protein encoded by this gene is a member of the tripartite motif (TRIM) family. The TRIM motif includes three zinc-binding domains, a RING, B-box type 1 and B-box type 2 domain, and a coiled-coil region. Expression of this gene is up-regulated by interferon. This gene is mapped to chromosome 11p15, where it resides within a TRIM gene cluster. Alternative splicing results in multiple transcript variants. A read-through transcript from the upstream TRIM6 gene has also been observed, which …

**Accessions** — [HGNC:10063](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10063) · Entrez [53840](https://www.ncbi.nlm.nih.gov/gene/53840) · UniProt [Q9BYJ4](https://www.uniprot.org/uniprotkb/Q9BYJ4) · Ensembl [ENSG00000258659](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000258659)

## Data

Gene col 15126: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15126); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15126, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15126]; `tensor/DDL_lfc|DDL_z.npy` [15126]; `embed/gene_vectors.npy` [15126]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15126 or target_col == 15126). Every well: [[TRIM34 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM34.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
