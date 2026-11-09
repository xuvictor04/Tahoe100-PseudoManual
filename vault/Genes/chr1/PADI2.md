---
symbol: "PADI2"
type: "gene"
col: 3874
ensembl_id: "ENSG00000117115"
name: "peptidyl arginine deiminase 2"
location: "1p36.13"
module: 100
arm: "+"
pooled_cpm: 3.38
n_lines_expressing: 29
n_dd_up: 22
n_dd_down: 4
n_dd_up_clean: 15
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 6
direction_downstream: 10
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# PADI2

*peptidyl arginine deiminase 2* — 1p36.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 10.3× (z +22.4, q 0e+00, up in 25 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.667× (z -3.9, q 0.021, down in 9 of 22 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPHB3]] (+0.62, fdr 2e-05), [[SGSM1]] (+0.61, fdr 2e-05), [[FCHO1]] (+0.61, fdr 1e-04); moves opposite to [[AP5M1]] (-0.58, fdr 5e-04), [[ZNF785]] (-0.57, fdr 2e-04), [[TCEANC2]] (-0.57, fdr 3e-05).
> It is in [[Module 100]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[AMOT]] → it (grade B ⚠); 10 go from it, the strongest it → [[ATP6V0E2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3874.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **10.3×** | +22.4 | 0e+00 | 25/25 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **7.55×** | +19.5 | 0e+00 | 23/24 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **4.07×** | +19.1 | 0e+00 | 23/24 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **4.78×** | +15.1 | 0e+00 | 21/24 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.72×** | +12.6 | 1e-34 | 3/10 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.05×** | +10.7 | 6e-25 | 19/24 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.17×** | +10.7 | 1e-24 | 3/8 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.67×** | +9.5 | 2e-19 | 18/21 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.52×** | +8.2 | 1e-14 | 2/7 (PANC-1, BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.82×** | +5.2 | 1e-05 | 9/20 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.42×** | +4.7 | 1e-04 | 2/24 (CFPAC-1, HT-29) | top dose only | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.63×** | +4.7 | 1e-04 | 5/19 (LS 180, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.52×** | +4.0 | 0.002 | 1/19 (CFPAC-1) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.52×** | +4.0 | 0.002 | 1/17 (A-427) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.33×** | +3.8 | 0.004 | 3/21 (SW480, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Pimozide (drug)]] 0.05 µM |  | **1.40×** | +3.2 | 0.035 | 1/17 (HT-29) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.60×** | +3.2 | 0.035 | 0/14 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.25×** | +3.0 | 0.066 | 2/22 (BT-474, LoVo) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.40×** | +3.0 | 0.070 | 2/19 (C-33 A, A-427) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3874.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.667×** | -3.9 | 0.021 | 9/22 (NCI-H2030, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.669×** | -3.9 | 0.021 | 12/21 (NCI-H23, C-33 A, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.670×** | -3.9 | 0.021 | 8/24 (LS 180, LoVo, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.685×** | -3.6 | 0.039 | 13/25 (SW48, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.696× | -3.3 | 0.11 | 6/20 (SW48, SNU-423, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.715× | -3.2 | 0.12 | 10/23 (LS 180, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.725× | -3.1 | 0.16 | 4/23 (SW480, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3874. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 8.12 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 13.4× (z +13.7) | — |
| [[SW480 (line)]] | alt | 1.46 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 24.6× (z +13.4) | — |
| [[C-33 A (line)]] | alt | 11.9 | 0 | 3 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0503× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0572× (z -10.3) |
| [[NCI-H2030 (line)]] | alt | 6.37 | 0 | 3 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0651× (z -10.4) ⚠ unreliable plate only · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.0669× (z -10.3) |
| [[NCI-H23 (line)]] | alt | 8.92 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0710× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.0786× (z -10.9) |
| [[SW1417 (line)]] | alt | 7.51 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 6.84× (z +9.9) | — |
| [[LoVo (line)]] | wt | 2.95 | 0 | 2 | — | [[Ciclopirox (drug)]] 0.05 µM 0.0543× (z -9.7) |
| [[A-427 (line)]] | wt | 9.22 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 7.49× (z +9.6) | — |
| [[HEC-1-A (line)]] | alt | 18.6 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.55× (z +11.3) | — |
| [[HT-29 (line)]] | alt | 6.81 | 0 | 1 (1 ⚠) | — | [[Fostamatinib (disodium hexahydrate) (drug)]] 5 µM 0.0387× (z -9.0) ⚠ unreliable plate only |
| [[LS 180 (line)]] | wt | 2.72 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 14.0× (z +9.6) | — |
| [[A-172 (line)]] | wt | 0.332 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.280 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.560 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.327 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.451 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.454 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.317 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.338 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.593 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.350 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.381 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.596 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.637 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.378 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.282 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.418 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.434 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.320 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.981 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.442 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.513 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.773 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.65 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3874), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPHB3]] | +0.62 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[SGSM1]] | +0.61 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[FCHO1]] | +0.61 | +0.33 / +0.55 | both halves | 1e-04 |  |
| [[SMARCD3]] | +0.61 | +0.35 / +0.60 | both halves | 1e-04 | pathway: Chromatin modifying enzymes |
| [[ESPN]] | +0.59 | +0.35 / +0.61 | both halves | 1e-04 |  |
| [[HPSE]] | +0.59 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[IQGAP2]] | +0.59 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[FGFR4]] | +0.59 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[FOXO6]] | +0.58 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[KCTD17]] | +0.58 | +0.38 / +0.44 | both halves | 7e-05 |  |
| [[LPCAT2]] | +0.57 | +0.33 / +0.54 | both halves | 1e-04 |  |
| [[STARD5]] | +0.57 | +0.41 / +0.52 | both halves | 4e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP5M1]] | -0.58 | -0.40 / -0.23 | both halves | 5e-04 |  |
| [[ZNF785]] | -0.57 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[TCEANC2]] | -0.57 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[TAS2R4]] | -0.57 | -0.35 / -0.33 | both halves | 1e-04 |  |
| [[GPATCH2]] | -0.57 | -0.43 / -0.30 | both halves | 2e-04 |  |
| [[METTL4]] | -0.56 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[CCDC122]] | -0.56 | -0.38 / -0.29 | both halves | 2e-04 |  |
| [[SAP30L-AS1]] | -0.56 | -0.37 / -0.36 | both halves | 1e-04 |  |
| [[DNAI4]] | -0.56 | -0.27 / -0.41 | both halves | 3e-04 |  |
| [[DCAF4L1]] | -0.56 | -0.41 / -0.26 | both halves | 4e-04 |  |
| [[CHD1-DT]] | -0.55 | -0.26 / -0.42 | both halves | 4e-04 |  |
| [[TRAPPC13]] | -0.55 | -0.41 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AMOT]] | B | AMOT activity raises PADI2's level | lines that do not express AMOT (12) vs lines expressing it (38) | 2.27× lower at baseline in the lines without AMOT | 0.016 | ⚠ within organs, on part of the lines; also absent: SYCP2, ENSG00000289956, ENSG00000132832 |
| [[XKR7]] | B | XKR7 activity strengthens PADI2's drug response | lines that do not express XKR7 (19) vs lines expressing it (6) | the lines without XKR7 respond 0.70× as strongly (z diff +1.52); strongest at Dinaciclib 5 µM: 1.06x vs 2.59x (z diff +5.1) | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, LINC01205, BMP5; target measured in part of the lines; artifact flags |
| [[ENTPD2]] | C | ENTPD2 activity raises PADI2's level | lines that do not express ENTPD2 (22) vs lines expressing it (28) | 2.29× lower at baseline in the lines without ENTPD2 | 0.021 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ESRP2; co-absent with the target |
| [[KSR2]] | C | KSR2 activity raises PADI2's level | lines that do not express KSR2 (20) vs lines expressing it (30) | 2.26× lower at baseline in the lines without KSR2 | 0.050 | ⚠ within organs, on part of the lines; also absent: SPTB, MYT1, YBX2; maybe low, not absent; co-absent with the target |
| [[LMTK3]] | C | LMTK3 activity raises PADI2's level | lines that do not express LMTK3 (15) vs lines expressing it (35) | 2.32× lower at baseline in the lines without LMTK3 | 0.055 | ⚠ within organs, on part of the lines; also absent: CRYBG2, CXADR, CCDC120; maybe low, not absent; co-absent with the target |
| [[RASAL1]] | C | RASAL1 activity raises PADI2's level | lines that do not express RASAL1 (25) vs lines expressing it (25) | 1.67× lower at baseline in the lines without RASAL1 | 0.074 | ⚠ within organs, on part of the lines; also absent: CSF2RA, SMPDL3B, SKAP1; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 8, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATP6V0E2]] | B | PADI2 activity raises ATP6V0E2's level | lines that do not express PADI2 (21) vs lines expressing it (29) | 1.82× lower at baseline in the lines without PADI2 | 0.012 | ⚠ within organs, on part of the lines; also absent: HES2, YBX2, FBXO2 |
| [[PREX1]] | B | PADI2 activity raises PREX1's level | lines that do not express PADI2 (21) vs lines expressing it (29) | 1.51× lower at baseline in the lines without PADI2 | 0.034 | ⚠ within organs, on part of the lines; also absent: HES2, YBX2, FBXO2 |
| [[CFD]] | B | PADI2 activity raises CFD's level | lines that do not express PADI2 (21) vs lines expressing it (29) | 1.82× lower at baseline in the lines without PADI2 | 0.037 | ⚠ within organs, on part of the lines; also absent: HES2, YBX2, FBXO2 |
| [[CRACR2B]] | B | PADI2 activity raises CRACR2B's level | lines that do not express PADI2 (21) vs lines expressing it (29) | 1.98× lower at baseline in the lines without PADI2 | 0.048 | ⚠ within organs, on part of the lines; also absent: HES2, YBX2, FBXO2 |
| [[LINC00937]] | B | PADI2 activity raises LINC00937's level | lines that do not express PADI2 (21) vs lines expressing it (29) | 1.89× lower at baseline in the lines without PADI2 | 0.054 | ⚠ within organs, on part of the lines; also absent: HES2, YBX2, FBXO2 |
| [[FCHO1]] | B | PADI2 activity raises FCHO1's level | lines that do not express PADI2 (21) vs lines expressing it (29) | 1.65× lower at baseline in the lines without PADI2 | 0.058 | ⚠ within organs, on part of the lines; also absent: HES2, YBX2, FBXO2 |
| [[TPPP]] | B | PADI2 activity raises TPPP's level | lines that do not express PADI2 (21) vs lines expressing it (29) | 1.51× lower at baseline in the lines without PADI2 | 0.072 | ⚠ within organs, on part of the lines; also absent: HES2, YBX2, FBXO2 |
| [[AMOT]] | B | PADI2 activity raises AMOT's level | lines that do not express PADI2 (21) vs lines expressing it (29) | 1.81× lower at baseline in the lines without PADI2 | 0.084 | ⚠ within organs, on part of the lines; also absent: HES2, YBX2, FBXO2 |
| [[RASAL1]] | C | PADI2 activity raises RASAL1's level | lines that do not express PADI2 (21) vs lines expressing it (29) | 1.86× lower at baseline in the lines without PADI2 | 0.024 | ⚠ within organs, on part of the lines; also absent: HES2, YBX2, FBXO2; co-absent with the target |
| [[KSR2]] | C | PADI2 activity raises KSR2's level | lines that do not express PADI2 (21) vs lines expressing it (29) | 2.85× lower at baseline in the lines without PADI2 | 0.085 | ⚠ within organs, on part of the lines; also absent: HES2, YBX2, FBXO2; co-absent with the target |

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.547). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (10.4, 2.6); signed map (-21.6, 30.4). **Vector** length 51.7, 10.9% of its response variance represented; |z| ≥ 3 in 653 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +19.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.3 | +9.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.5 | +22.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.5 | +19.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +10.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +5.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +1.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +0.9 | +0.3 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.2 | -0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -2.3 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.9 | -3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | -3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.3 | -0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | peptidyl arginine deiminase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.13 — chr1:17,066,761-17,119,451 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0994, PDI2 |
| Gene groups (HGNC) | Peptidyl arginine deiminases |
| Reactome | 4 pathways, smallest: Chromatin modifying enzymes; Chromatin organization; Neutrophil degranulation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2J8](https://www.uniprot.org/uniprotkb/Q9Y2J8) (Protein-arginine deiminase type-2):

> Catalyzes the deimination of arginine residues of proteins.

**Summary**, from NCBI Gene [11240](https://www.ncbi.nlm.nih.gov/gene/11240):

> This gene encodes a member of the peptidyl arginine deiminase family of enzymes, which catalyze the post-translational deimination of proteins by converting arginine residues into citrullines in the presence of calcium ions. The family members have distinct substrate specificities and tissue-specific expression patterns. The type II enzyme is the most widely expressed family member. Known substrates for this enzyme include myelin basic protein in the central nervous system and vimentin in …

**Accessions** — [HGNC:18341](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18341) · Entrez [11240](https://www.ncbi.nlm.nih.gov/gene/11240) · UniProt [Q9Y2J8](https://www.uniprot.org/uniprotkb/Q9Y2J8) · Ensembl [ENSG00000117115](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117115)

## Data

Gene col 3874: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3874); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3874, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3874]; `tensor/DDL_lfc|DDL_z.npy` [3874]; `embed/gene_vectors.npy` [3874]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3874 or target_col == 3874). Every well: [[PADI2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PADI2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
