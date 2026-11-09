---
symbol: "MEST"
type: "gene"
col: 2767
ensembl_id: "ENSG00000106484"
name: "mesoderm specific transcript"
location: "7q32.2"
module: 4
arm: "+"
pooled_cpm: 23.43
n_lines_expressing: 33
n_dd_up: 8
n_dd_down: 8
n_dd_up_clean: 3
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 10
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# MEST

*mesoderm specific transcript* — 7q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.06× (z +17.5, q 0e+00, up in 20 of 24 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[NG25 (drug)]] 5 µM: 1.92× (z +4.3, q 0.002, up in 10 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.455× (z -14.0, q 2e-41, down in 25 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PODXL2]] (+0.71, fdr 7e-06), [[PFKM]] (+0.69, fdr 1e-05), [[DHX15]] (+0.69, fdr 7e-06); moves opposite to [[SELENOK]] (-0.66, fdr 1e-05), [[NOXRED1]] (-0.60, fdr 1e-05), [[STX5]] (-0.60, fdr 2e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LARGE2]] → it (grade B ⚠); 10 go from it, the strongest it → [[LARGE2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2767.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.06×** | +17.5 | 0e+00 | 20/24 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.24×** | +14.2 | 1e-43 | 16/19 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.67×** | +11.4 | 6e-28 | 13/21 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[NG25 (drug)]] 5 µM |  | **1.92×** | +4.3 | 0.002 | 10/28 (CFPAC-1, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +4.0 | 0.007 | 8/31 (J82, HCT15, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +3.9 | 0.010 | 13/29 (A-427, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.31×** | +3.4 | 0.058 | 1/30 (SW 900) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +3.3 | 0.075 | 13/30 (NCI-H1792, NCI-H2347, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | 1.28× | +3.1 | 0.13 | 5/30 (SW480, LoVo, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.29× | +3.0 | 0.13 | 8/27 (CFPAC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~6% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2767.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.455×** | -14.0 | 2e-41 | 25/31 (AN3 CA, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.573×** | -6.8 | 4e-09 | 16/30 (AN3 CA, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.607×** | -6.3 | 5e-08 | 12/29 (AN3 CA, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.652×** | -5.2 | 3e-05 | 17/30 (NCI-H23, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.478×** | -4.9 | 1e-04 | 10/31 (A-427, AN3 CA, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.767×** | -4.7 | 2e-04 | 19/29 (SW480, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.761×** | -3.5 | 0.044 | 11/30 (SW48, SW480, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.770×** | -3.3 | 0.066 | 10/31 (AN3 CA, CHP-212, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.781× | -3.1 | 0.12 | 6/30 (AN3 CA, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2767. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 2,926 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0185× (z -34.2) |
| [[SW480 (line)]] | alt | 31.6 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +9.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -14.8) |
| [[KATO III (line)]] | alt | 23.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 7.64× (z +12.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -10.3) |
| [[LoVo (line)]] | wt | 15.1 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 6.95× (z +11.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -13.6) |
| [[PANC-1 (line)]] | alt | 13.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.49× (z +13.7) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 16.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.65× (z +9.8) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 27.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -12.0) |
| [[NCI-H1792 (line)]] | alt | 8.23 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 23.3× (z +12.1) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 23.9 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.103× (z -13.5) |
| [[A-427 (line)]] | wt | 13.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.183× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change |
| [[COLO 205 (line)]] | alt | 9.89 | 0 | 1 | — | [[Sulfatinib (drug)]] 0.05 µM 0.0559× (z -8.7) |
| [[HT-29 (line)]] | alt | 15.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.50× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 19.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 20.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -10.1) |
| [[SW48 (line)]] | wt | 25.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.131× (z -13.7) |
| [[A-172 (line)]] | wt | 2.45 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.96 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.42 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.60 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.02 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.47 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.37 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.89 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.32 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.55 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.65 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.33 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.10 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2767), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PODXL2]] | +0.71 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[PFKM]] | +0.69 | +0.57 / +0.69 | both halves | 1e-05 | same gene group |
| [[DHX15]] | +0.69 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[GLB1L2]] | +0.69 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[MRPL42]] | +0.69 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[ALDH5A1]] | +0.68 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[ASIC1]] | +0.66 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[ADAT2]] | +0.64 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[DHX9]] | +0.64 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[PPT1]] | +0.63 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[PFAS]] | +0.62 | +0.49 / +0.63 | both halves | 2e-05 |  |
| [[CAD]] | +0.62 | +0.48 / +0.61 | both halves | 2e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SELENOK]] | -0.66 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[NOXRED1]] | -0.60 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[STX5]] | -0.60 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[C6orf62]] | -0.59 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[CFAP53]] | -0.58 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[SMIM14]] | -0.58 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[BOLA1]] | -0.57 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[GPANK1]] | -0.57 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[MTRFR]] | -0.56 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[ING2]] | -0.56 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[RAB4B]] | -0.55 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[ZMYM5]] | -0.55 | -0.52 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LARGE2]] | B | LARGE2 activity raises MEST's level | lines that do not express LARGE2 (21) vs lines expressing it (29) | 1.51× lower at baseline in the lines without LARGE2 | 0.071 | ⚠ within organs, on part of the lines; also absent: EPHA10, YBX2, FBXO2 |
| [[HEPHL1]] | B | HEPHL1 activity raises MEST's level | lines that do not express HEPHL1 (45) vs lines expressing it (5) | 2.44× lower at baseline in the lines without HEPHL1 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KRT20, GPR15, APOB |
| [[COPG2IT1]] | C | COPG2IT1 activity raises MEST's level | lines that do not express COPG2IT1 (12) vs lines expressing it (38) | 4.39× lower at baseline in the lines without COPG2IT1 | 0.012 | ⚠ within organs, on part of the lines; also absent: MEST, GLS2, NMNAT3; maybe low, not absent; co-absent with the target |
| [[PRR36]] | C | PRR36 activity raises MEST's level | lines that do not express PRR36 (19) vs lines expressing it (31) | 2.66× lower at baseline in the lines without PRR36 | 0.081 | ⚠ within organs, on part of the lines; also absent: NUP210, TTC9, CGN; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 7, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LARGE2]] | B | MEST activity raises LARGE2's level | lines that do not express MEST (17) vs lines expressing it (33) | 1.86× lower at baseline in the lines without MEST | 0.011 | ⚠ within organs, on part of the lines; also absent: COPG2IT1, CHDH, IL17RB |
| [[LRP5]] | B | MEST activity raises LRP5's level | lines that do not express MEST (17) vs lines expressing it (33) | 2.96× lower at baseline in the lines without MEST | 0.018 | ⚠ within organs, on part of the lines; also absent: COPG2IT1, CHDH, IL17RB |
| [[AKAP1]] | B | MEST activity raises AKAP1's level | lines that do not express MEST (17) vs lines expressing it (33) | 1.85× lower at baseline in the lines without MEST | 0.032 | ⚠ within organs, on part of the lines; also absent: COPG2IT1, CHDH, IL17RB |
| [[ORAI3]] | B | MEST activity lowers ORAI3's level | lines that do not express MEST (17) vs lines expressing it (33) | 1.50× higher at baseline in the lines without MEST | 0.050 | ⚠ within organs, on part of the lines; also absent: COPG2IT1, CHDH, IL17RB |
| [[PRDX3]] | B | MEST activity raises PRDX3's level | lines that do not express MEST (17) vs lines expressing it (33) | 1.19× lower at baseline in the lines without MEST | 0.063 | ⚠ within organs, on part of the lines; also absent: COPG2IT1, CHDH, IL17RB |
| [[JMJD8]] | B | MEST activity raises JMJD8's level | lines that do not express MEST (17) vs lines expressing it (33) | 1.37× lower at baseline in the lines without MEST | 0.087 | ⚠ within organs, on part of the lines; also absent: COPG2IT1, CHDH, IL17RB |
| [[ABHD5]] | B | MEST activity raises ABHD5's level | lines that do not express MEST (17) vs lines expressing it (33) | 1.41× lower at baseline in the lines without MEST | 0.099 | ⚠ within organs, on part of the lines; also absent: COPG2IT1, CHDH, IL17RB |
| [[COPG2IT1]] | C | MEST activity raises COPG2IT1's level | lines that do not express MEST (17) vs lines expressing it (33) | 3.02× lower at baseline in the lines without MEST | 8e-04 | ⚠ within organs, on part of the lines; also absent: COPG2IT1, CHDH, IL17RB; co-absent with the target |
| [[NMNAT3]] | C | MEST activity raises NMNAT3's level | lines that do not express MEST (17) vs lines expressing it (33) | 2.97× lower at baseline in the lines without MEST | 0.005 | ⚠ within organs, on part of the lines; also absent: COPG2IT1, CHDH, IL17RB; co-absent with the target |
| [[DMKN]] | C | MEST activity raises DMKN's level | lines that do not express MEST (17) vs lines expressing it (33) | 2.94× lower at baseline in the lines without MEST | 0.068 | ⚠ within organs, on part of the lines; also absent: COPG2IT1, CHDH, IL17RB; co-absent with the target |

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.623). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-27.9, -29.2); signed map (-19.9, -43.2). **Vector** length 59.1, 11.9% of its response variance represented; |z| ≥ 3 in 525 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +14.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +17.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +11.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +4.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.9 | +3.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.6 | +0.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.6 | +1.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +2.7 |
|  | [[EX229 (drug)]] 5 µM |  | +1.4 | +2.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -2.5 | -6.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.9 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.9 | -6.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.6 | -3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.6 | -3.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.5 | -4.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -2.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.2 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | mesoderm specific transcript |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q32.2 — chr7:130,486,171-130,506,465 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PEG1 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5EB52](https://www.uniprot.org/uniprotkb/Q5EB52) (Mesoderm-specific transcript homolog protein):

> Plays an important role in enabling neurons to transition from bipolar to multipolar shapes, a process essential for their correct migration toward the cortical plate during brain development. This function is likely achieved through the regulation of N-cadherin-dependent cell adhesion and the modulation of Akt and canonical Wnt signaling pathways. Essential for the development and maintenance of meso-diencephalic dopaminergic (mdDA) neurons during development. Negatively regulates the …

**Summary**, from NCBI Gene [4232](https://www.ncbi.nlm.nih.gov/gene/4232):

> This gene encodes a member of the alpha/beta hydrolase superfamily. It is imprinted, exhibiting preferential expression from the paternal allele in fetal tissues, and isoform-specific imprinting in lymphocytes. The loss of imprinting of this gene has been linked to certain types of cancer and may be due to promotor switching. The encoded protein may play a role in development. Alternatively spliced transcript variants encoding multiple isoforms have been identified for this gene. Pseudogenes of …

**Accessions** — [HGNC:7028](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7028) · Entrez [4232](https://www.ncbi.nlm.nih.gov/gene/4232) · UniProt [Q5EB52](https://www.uniprot.org/uniprotkb/Q5EB52) · Ensembl [ENSG00000106484](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106484)

## Data

Gene col 2767: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2767); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2767, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2767]; `tensor/DDL_lfc|DDL_z.npy` [2767]; `embed/gene_vectors.npy` [2767]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2767 or target_col == 2767). Every well: [[MEST — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MEST.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
