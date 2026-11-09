---
symbol: "EFEMP1"
type: "gene"
col: 3668
ensembl_id: "ENSG00000115380"
name: "EGF-like fibulin extracellular matrix protein 1"
location: "2p16.1"
module: 66
arm: "+"
pooled_cpm: 19.34
n_lines_expressing: 19
n_dd_up: 26
n_dd_down: 7
n_dd_up_clean: 17
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 12
direction_downstream: 13
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# EFEMP1

*EGF-like fibulin extracellular matrix protein 1* — 2p16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.47× (z +20.7, q 0e+00, up in 14 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.70× (z +9.2, q 5e-18, up in 5 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.661× (z -5.0, q 1e-04, down in 12 of 16 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POSTN]] (+0.68, fdr 1e-05), [[COL5A2]] (+0.67, fdr 1e-05), [[TGFBI]] (+0.63, fdr 1e-05); moves opposite to [[C19orf25]] (-0.50, fdr 2e-05), [[ZBTB7A]] (-0.50, fdr 3e-05), [[ZNF503]] (-0.48, fdr 8e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[SPTLC3]] → it (grade B ⚠); 13 go from it, the strongest it → [[TGFB2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3668.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.47×** | +20.7 | 0e+00 | 14/14 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.78×** | +20.6 | 0e+00 | 14/14 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.89×** | +15.3 | 0e+00 | 13/14 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +9.2 | 5e-18 | 5/16 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +7.6 | 3e-12 | 13/17 (NCI-H2347, PANC-1, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.01×** | +7.0 | 2e-10 | 5/13 (HOP62, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.47×** | +5.8 | 6e-07 | 10/16 (NCI-H1792, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +5.2 | 2e-05 | 5/16 (HS-578T, HOP62, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.51×** | +5.0 | 3e-05 | 10/16 (NCI-H2347, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.43×** | +4.4 | 7e-04 | 0/15 | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +4.3 | 1e-03 | 3/15 (CFPAC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **1.39×** | +3.8 | 0.006 | 6/15 (Panc 03.27, CFPAC-1, …) | top dose only |  |
| [[Bimatoprost (drug)]] 0.5 µM |  | **1.36×** | +3.8 | 0.007 | 1/16 (SW 1088) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.36×** | +3.6 | 0.013 | 6/15 (PANC-1, SW 900, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.73×** | +3.5 | 0.016 | 5/15 (SW 900, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.019 | 7/16 (SW 900, HOP62, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.71×** | +3.4 | 0.021 | 11/16 (CFPAC-1, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Capmatinib (drug)]] 5 µM |  | **1.63×** | +3.1 | 0.050 | 2/15 (NCI-H1792, A498) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.29×** | +3.1 | 0.050 | 8/17 (SW 900, NCI-H1792, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.19× | +3.0 | 0.067 | 4/17 (NCI-H1792, SW 900, …) | all doses, flat |  |
| [[Omeprazole (drug)]] 0.5 µM |  | **1.28×** | +3.0 | 0.067 | 0/15 | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.27×** | +2.9 | 0.088 | 6/17 (A498, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3668.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.661×** | -5.0 | 1e-04 | 12/16 (NCI-H460, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.661×** | -5.0 | 1e-04 | 11/16 (NCI-H460, J82, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.683×** | -4.6 | 7e-04 | 8/16 (NCI-H460, NCI-H23, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.717×** | -4.0 | 0.008 | 2/15 (HS-578T, A498) | top dose only | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.718×** | -3.9 | 0.012 | 7/15 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.716×** | -3.8 | 0.012 | 2/17 (Hs 766T, SW 900) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | **0.564×** | -3.6 | 0.023 | 3/17 (Panc 03.27, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 0.832× | -3.1 | 0.12 | 8/17 (NCI-H460, CFPAC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.778× | -3.0 | 0.15 | 4/16 (NCI-H460, J82, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.769× | -3.0 | 0.15 | 3/17 (HS-578T, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3668. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 144 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -20.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0693× (z -18.5) |
| [[HOP62 (line)]] | alt | 22.1 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.90× (z +9.4) | — |
| [[HS-578T (line)]] | alt | 28.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.50× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 72.5 | 2 (2 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.94× (z +14.2) ⚠ position not correctable | — |
| [[NCI-H2030 (line)]] | alt | 29.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -10.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.246× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 23.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -9.1) |
| [[PANC-1 (line)]] | alt | 10.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.32× (z +10.6) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 54.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.37× (z +9.0) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 2.51 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.25 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.13 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.55 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.19 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.11 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.20 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.94 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.60 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.48 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3668), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POSTN]] | +0.68 | +0.55 / +0.62 | both halves | 1e-05 | STRING 508 |
| [[COL5A2]] | +0.67 | +0.53 / +0.68 | both halves | 1e-05 | pathway: HALLMARK_UV_RESPONSE_DN |
| [[TGFBI]] | +0.63 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[ALDH1A1]] | +0.63 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[TGFB2]] | +0.63 | +0.60 / +0.63 | both halves | 7e-06 | pathway: Elastic fibre formation; STRING 471 |
| [[SLC39A8]] | +0.62 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[OLFML2A]] | +0.62 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[ADAM9]] | +0.60 | +0.49 / +0.52 | both halves | 2e-05 | pathway: Extracellular matrix organization |
| [[SLITRK5]] | +0.60 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[ANGPT1]] | +0.59 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[MXRA8]] | +0.59 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[FSTL1]] | +0.58 | +0.51 / +0.52 | both halves | 1e-05 | STRING 428 |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C19orf25]] | -0.50 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[ZBTB7A]] | -0.50 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[ZNF503]] | -0.48 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[ZNF765]] | -0.48 | -0.37 / -0.46 | both halves | 7e-05 |  |
| [[RABIF]] | -0.47 | -0.37 / -0.51 | both halves | 7e-05 |  |
| [[SPATA2L]] | -0.47 | -0.43 / -0.52 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 1, C 11.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPTLC3]] | B | SPTLC3 activity raises EFEMP1's level | lines that do not express SPTLC3 (16) vs lines expressing it (34) | 2.46× lower at baseline in the lines without SPTLC3 | 0.060 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, CXCL3, PTPRB; maybe low, not absent |
| [[EDIL3]] | C | EDIL3 activity raises EFEMP1's level | lines that do not express EDIL3 (28) vs lines expressing it (22) | 4.29× lower at baseline in the lines without EDIL3 | 0.006 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, ENSG00000232949, STAC; co-absent with the target |
| [[FAT4]] | C | FAT4 activity raises EFEMP1's level | lines that do not express FAT4 (20) vs lines expressing it (30) | 4.39× lower at baseline in the lines without FAT4 | 0.020 | ⚠ within organs, on part of the lines; also absent: RFTN1, GPR176, GNG11; co-absent with the target |
| [[OLFML2A]] | C | OLFML2A activity raises EFEMP1's level | lines that do not express OLFML2A (20) vs lines expressing it (30) | 2.90× lower at baseline in the lines without OLFML2A | 0.022 | ⚠ within organs, on part of the lines; also absent: GBX1, FMNL1-DT, SCN5A; co-absent with the target |
| [[CCBE1]] | C | CCBE1 activity raises EFEMP1's level | lines that do not express CCBE1 (28) vs lines expressing it (22) | 4.47× lower at baseline in the lines without CCBE1 | 0.034 | ⚠ within organs, on part of the lines; also absent: EDNRA, IL7R, EFEMP1; co-absent with the target |
| [[TGFBI]] | C | TGFBI activity raises EFEMP1's level | lines that do not express TGFBI (25) vs lines expressing it (25) | 3.63× lower at baseline in the lines without TGFBI | 0.035 | ⚠ within organs, on part of the lines; also absent: IL6, SRPX2, ENSG00000232949; co-absent with the target |
| [[COL8A1]] | C | COL8A1 activity raises EFEMP1's level | lines that do not express COL8A1 (31) vs lines expressing it (19) | 3.07× lower at baseline in the lines without COL8A1 | 0.037 | ⚠ within organs, on part of the lines; also absent: IL6, LINC01411, NCAM1; co-absent with the target |
| [[SMIM10]] | C | SMIM10 activity raises EFEMP1's level | lines that do not express SMIM10 (24) vs lines expressing it (26) | 2.86× lower at baseline in the lines without SMIM10 | 0.044 | ⚠ within organs, on part of the lines; also absent: SNAI2, MCAM, ZNF365; co-absent with the target |
| [[CFH]] | C | CFH activity raises EFEMP1's level | lines that do not express CFH (28) vs lines expressing it (22) | 2.99× lower at baseline in the lines without CFH | 0.061 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ADAMTS9-AS2, COL22A1; co-absent with the target |
| [[SUSD5]] | C | SUSD5 activity raises EFEMP1's level | lines that do not express SUSD5 (23) vs lines expressing it (27) | 3.98× lower at baseline in the lines without SUSD5 | 0.062 | ⚠ within organs, on part of the lines; also absent: EDIL3, BVES, MAP9; co-absent with the target |
| [[DDIT4L]] | C | DDIT4L activity raises EFEMP1's level | lines that do not express DDIT4L (29) vs lines expressing it (21) | 2.94× lower at baseline in the lines without DDIT4L | 0.088 | ⚠ within organs, on part of the lines; also absent: EDNRA, IL1B, ARMCX2; co-absent with the target |
| [[GALC]] | C | GALC activity raises EFEMP1's level | lines that do not express GALC (17) vs lines expressing it (33) | 3.26× lower at baseline in the lines without GALC | 0.089 | ⚠ within organs, on part of the lines; also absent: HERC5, TNFRSF1B, ZNF354C; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 9, C 4. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TGFB2]] | B | EFEMP1 activity raises TGFB2's level | lines that do not express EFEMP1 (31) vs lines expressing it (19) | 4.42× lower at baseline in the lines without EFEMP1 | 0.010 | ⚠ within organs, on part of the lines; also absent: IL6, STEAP1B-AS1, IL31RA |
| [[PTGR1]] | B | EFEMP1 activity raises PTGR1's level | lines that do not express EFEMP1 (31) vs lines expressing it (19) | 2.38× lower at baseline in the lines without EFEMP1 | 0.045 | ⚠ within organs, on part of the lines; also absent: IL6, STEAP1B-AS1, IL31RA |
| [[GALNT2]] | B | EFEMP1 activity raises GALNT2's level | lines that do not express EFEMP1 (31) vs lines expressing it (19) | 1.58× lower at baseline in the lines without EFEMP1 | 0.050 | ⚠ within organs, on part of the lines; also absent: IL6, STEAP1B-AS1, IL31RA |
| [[SPATA2L]] | B | EFEMP1 activity lowers SPATA2L's level | lines that do not express EFEMP1 (31) vs lines expressing it (19) | 1.16× higher at baseline in the lines without EFEMP1 | 0.058 | ⚠ within organs, on part of the lines; also absent: IL6, STEAP1B-AS1, IL31RA |
| [[SPTLC3]] | B | EFEMP1 activity raises SPTLC3's level | lines that do not express EFEMP1 (31) vs lines expressing it (19) | 1.54× lower at baseline in the lines without EFEMP1 | 0.066 | ⚠ within organs, on part of the lines; also absent: IL6, STEAP1B-AS1, IL31RA |
| [[MYOF]] | B | EFEMP1 activity raises MYOF's level | lines that do not express EFEMP1 (31) vs lines expressing it (19) | 1.87× lower at baseline in the lines without EFEMP1 | 0.079 | ⚠ within organs, on part of the lines; also absent: IL6, STEAP1B-AS1, IL31RA |
| cells under [[Entecavir (monohydrate) (drug)]] 0.5 µM | B | EFEMP1 activity raises the cells' numbers under Entecavir (monohydrate) 0.5 µM (protects the cells) | lines that do not express EFEMP1 (31) vs lines expressing it (17) | the lines without EFEMP1: 0.79× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: IL6, STEAP1B-AS1, IL31RA |
| [[ALDH1A1]] | B | EFEMP1 activity lowers ALDH1A1's level | lines that do not express EFEMP1 (31) vs lines expressing it (19) | 1.57× higher at baseline in the lines without EFEMP1 | 0.092 | ⚠ within organs, on part of the lines; also absent: IL6, STEAP1B-AS1, IL31RA |
| [[RHOBTB3]] | B | EFEMP1 activity raises RHOBTB3's level | lines that do not express EFEMP1 (31) vs lines expressing it (19) | 1.59× lower at baseline in the lines without EFEMP1 | 0.095 | ⚠ within organs, on part of the lines; also absent: IL6, STEAP1B-AS1, IL31RA |
| [[EDIL3]] | C | EFEMP1 activity raises EDIL3's level | lines that do not express EFEMP1 (31) vs lines expressing it (19) | 5.65× lower at baseline in the lines without EFEMP1 | 0.037 | ⚠ within organs, on part of the lines; also absent: IL6, STEAP1B-AS1, IL31RA; co-absent with the target |
| [[CCBE1]] | C | EFEMP1 activity raises CCBE1's level | lines that do not express EFEMP1 (31) vs lines expressing it (19) | 5.25× lower at baseline in the lines without EFEMP1 | 0.058 | ⚠ within organs, on part of the lines; also absent: IL6, STEAP1B-AS1, IL31RA; co-absent with the target |
| [[SMIM10]] | C | EFEMP1 activity raises SMIM10's level | lines that do not express EFEMP1 (31) vs lines expressing it (19) | 1.80× lower at baseline in the lines without EFEMP1 | 0.067 | ⚠ within organs, on part of the lines; also absent: IL6, STEAP1B-AS1, IL31RA; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.695). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (56.9, 22.7); signed map (26.3, 34.7). **Vector** length 69.3, 25.6% of its response variance represented; |z| ≥ 3 in 459 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *angiogenesis* (hallmark, mean cos +0.55 to 5); *Signaling by PDGF* (reactome, mean cos +0.52 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.8 | +20.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.7 | +20.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.0 | +15.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +7.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.7 | +5.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.6 | +1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.6 | +3.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.5 | +5.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.5 | +2.8 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -2.5 | -5.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -2.3 | -3.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.0 | -2.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | -4.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.8 | -2.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.7 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | EGF-like fibulin extracellular matrix protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p16.1 — chr2:55,865,967-55,924,139 (-) |
| Ensembl biotype | protein_coding |
| Also known as | S1-5, FBLN3, MTLV; previously DHRD, FBNL |
| Gene groups (HGNC) | Fibulins |
| Hallmark sets | UV_RESPONSE_DN |
| Reactome | 3 pathways, smallest: Molecules associated with elastic fibres; Elastic fibre formation; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12805](https://www.uniprot.org/uniprotkb/Q12805) (EGF-containing fibulin-like extracellular matrix protein 1):

> Binds EGFR, the EGF receptor, inducing EGFR autophosphorylation and the activation of downstream signaling pathways. May play a role in cell adhesion and migration. May function as a negative regulator of chondrocyte differentiation. In the olfactory epithelium, it may regulate glial cell migration, differentiation and the ability of glial cells to support neuronal neurite outgrowth.

**Summary**, from NCBI Gene [2202](https://www.ncbi.nlm.nih.gov/gene/2202):

> This gene encodes a member of the fibulin family of extracellular matrix glycoproteins. Like all members of this family, the encoded protein contains tandemly repeated epidermal growth factor-like repeats followed by a C-terminus fibulin-type domain. This gene is upregulated in malignant gliomas and may play a role in the aggressive nature of these tumors. Mutations in this gene are associated with Doyne honeycomb retinal dystrophy. Alternatively spliced transcript variants that encode the same …

**Accessions** — [HGNC:3218](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3218) · Entrez [2202](https://www.ncbi.nlm.nih.gov/gene/2202) · UniProt [Q12805](https://www.uniprot.org/uniprotkb/Q12805) · Ensembl [ENSG00000115380](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115380)

## Data

Gene col 3668: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3668); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3668, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3668]; `tensor/DDL_lfc|DDL_z.npy` [3668]; `embed/gene_vectors.npy` [3668]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3668 or target_col == 3668). Every well: [[EFEMP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EFEMP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
