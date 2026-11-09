---
symbol: "TMCC2"
type: "gene"
col: 5411
ensembl_id: "ENSG00000133069"
name: "transmembrane and coiled-coil domain family 2"
location: "1q32.1"
module: 100
arm: "+"
pooled_cpm: 2.93
n_lines_expressing: 45
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 20
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 10
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# TMCC2

*transmembrane and coiled-coil domain family 2* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (5 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 6.36× (z +17.1, q 0e+00, up in 37 of 39 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 0.05 µM in 1 line (LoVo 0.0818×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADGRB2]] (+0.75, fdr 7e-06), [[HMSD]] (+0.64, fdr 1e-05), [[SEMA6B]] (+0.63, fdr 1e-05); moves opposite to [[ANAPC1]] (-0.56, fdr 3e-05), [[COX10]] (-0.55, fdr 4e-05), [[RNASEH1]] (-0.54, fdr 7e-05).
> It is in [[Module 100]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SEMA6B]] → it (grade B ⚠); 10 go from it, the strongest it → [[C1orf109]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5411.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **6.36×** | +17.1 | 0e+00 | 37/39 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **6.33×** | +17.0 | 0e+00 | 40/42 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.46×** | +15.7 | 0e+00 | 37/39 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **4.73×** | +14.3 | 2e-44 | 38/40 (C32, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.81×** | +13.5 | 3e-39 | 27/29 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.58×** | +12.4 | 3e-33 | 36/41 (C32, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **3.53×** | +11.6 | 2e-29 | 25/28 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.24×** | +10.5 | 5e-24 | 16/31 (NCI-H2347, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.78×** | +9.1 | 8e-18 | 22/36 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.55×** | +8.7 | 3e-16 | 29/35 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **5.06×** | +7.8 | 2e-13 | 24/34 (C32, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.27×** | +7.3 | 2e-11 | 1/2 (A498) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.11×** | +6.9 | 2e-10 | 8/15 (SNU-423, C32, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.38×** | +5.9 | 2e-07 | 11/33 (A-172, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.66×** | +4.7 | 1e-04 | 14/31 (NCI-H2347, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.61×** | +4.4 | 4e-04 | 5/41 (C32, SW48, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.53×** | +3.9 | 0.003 | 12/39 (NCI-H2347, A549, …) | rises with dose | cell-cycle shift (explains ~12% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5411.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 0.05 µM in 1 line (LoVo 0.0818×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.686× | -3.5 | 0.22 | 10/40 (CHP-212, NCI-H2030, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.775× | -3.4 | 0.22 | 8/41 (CHP-212, H4, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5411. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 3.56 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0818× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 3.61 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.51× (z +9.4) | — |
| [[PANC-1 (line)]] | alt | 1.74 | 1 | 0 | [[Belinostat (drug)]] 5 µM 18.3× (z +8.6) | — |
| [[A-172 (line)]] | wt | 5.81 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.42 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.31 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.499 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.614 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.74 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.829 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.413 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.877 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.524 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.366 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.892 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.46 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.56 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5411), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADGRB2]] | +0.75 | +0.68 / +0.79 | both halves | 7e-06 |  |
| [[HMSD]] | +0.64 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[SEMA6B]] | +0.63 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[CYRIA]] | +0.63 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[GRHL1]] | +0.61 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[TSPAN33]] | +0.60 | +0.42 / +0.68 | both halves | 4e-05 |  |
| [[RGS9]] | +0.60 | +0.34 / +0.68 | both halves | 1e-04 |  |
| [[SUSD4]] | +0.60 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[PIK3CD]] | +0.59 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[REEP2]] | +0.58 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[PIK3C2B]] | +0.58 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[KCNN3]] | +0.58 | +0.49 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANAPC1]] | -0.56 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[COX10]] | -0.55 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[RNASEH1]] | -0.54 | -0.38 / -0.54 | both halves | 7e-05 |  |
| [[ACAD9]] | -0.54 | -0.33 / -0.55 | both halves | 1e-04 |  |
| [[AVEN]] | -0.53 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[ATR]] | -0.53 | -0.41 / -0.40 | both halves | 4e-05 |  |
| [[PUM3]] | -0.52 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[LINC02987]] | -0.51 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[SPRY3]] | -0.51 | -0.34 / -0.55 | both halves | 1e-04 |  |
| [[MSANTD2]] | -0.51 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[UTP20]] | -0.50 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[DPH5-DT]] | -0.50 | -0.22 / -0.43 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEMA6B]] | B | SEMA6B activity raises TMCC2's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 1.89× lower at baseline in the lines without SEMA6B | 0.003 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[MITF]] | B | MITF activity raises TMCC2's level | lines that do not express MITF (9) vs lines expressing it (41) | 2.25× lower at baseline in the lines without MITF | 0.008 | ⚠ within organs, on part of the lines; also absent: LRP12, DUBR, CYP46A1 |
| [[ENTREP1]] | B | ENTREP1 activity raises TMCC2's level | lines that do not express ENTREP1 (18) vs lines expressing it (32) | 1.67× lower at baseline in the lines without ENTREP1 | 0.083 | ⚠ within organs, on part of the lines; also absent: LHX2, OLFM1, COL4A4 |
| [[TLE2]] | B | TLE2 activity raises TMCC2's level | lines that do not express TLE2 (10) vs lines expressing it (40) | 1.68× lower at baseline in the lines without TLE2 | 0.096 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C1orf109]] | B | TMCC2 activity raises C1orf109's level | lines that do not express TMCC2 (5) vs lines expressing it (45) | 1.47× lower at baseline in the lines without TMCC2 | 0.033 | ⚠ within organs, on part of the lines; also absent: AXDND1, SUCLG2-DT, SACS; maybe low, not absent |
| [[PUM3]] | B | TMCC2 activity raises PUM3's level | lines that do not express TMCC2 (5) vs lines expressing it (45) | 1.56× lower at baseline in the lines without TMCC2 | 0.050 | ⚠ within organs, on part of the lines; also absent: AXDND1, SUCLG2-DT, SACS; maybe low, not absent |
| [[ABCG1]] | B | TMCC2 activity lowers ABCG1's level | lines that do not express TMCC2 (5) vs lines expressing it (45) | 4.61× higher at baseline in the lines without TMCC2 | 0.057 | ⚠ within organs, on part of the lines; also absent: AXDND1, SUCLG2-DT, SACS; maybe low, not absent |
| [[MITF]] | B | TMCC2 activity raises MITF's level | lines that do not express TMCC2 (5) vs lines expressing it (45) | 4.38× lower at baseline in the lines without TMCC2 | 0.064 | ⚠ within organs, on part of the lines; also absent: AXDND1, SUCLG2-DT, SACS; maybe low, not absent |
| [[SLC30A4]] | B | TMCC2 activity raises SLC30A4's level | lines that do not express TMCC2 (5) vs lines expressing it (45) | 1.57× lower at baseline in the lines without TMCC2 | 0.072 | ⚠ within organs, on part of the lines; also absent: AXDND1, SUCLG2-DT, SACS; maybe low, not absent |
| [[PIK3CD]] | B | TMCC2 activity raises PIK3CD's level | lines that do not express TMCC2 (5) vs lines expressing it (45) | 3.09× lower at baseline in the lines without TMCC2 | 0.082 | ⚠ within organs, on part of the lines; also absent: AXDND1, SUCLG2-DT, SACS; maybe low, not absent |
| [[GLIPR2]] | B | TMCC2 activity raises GLIPR2's level | lines that do not express TMCC2 (5) vs lines expressing it (45) | 3.43× lower at baseline in the lines without TMCC2 | 0.085 | ⚠ within organs, on part of the lines; also absent: AXDND1, SUCLG2-DT, SACS; maybe low, not absent |
| [[REEP2]] | B | TMCC2 activity raises REEP2's level | lines that do not express TMCC2 (5) vs lines expressing it (45) | 2.52× lower at baseline in the lines without TMCC2 | 0.086 | ⚠ within organs, on part of the lines; also absent: AXDND1, SUCLG2-DT, SACS; maybe low, not absent |
| [[ANAPC1]] | B | TMCC2 activity raises ANAPC1's level | lines that do not express TMCC2 (5) vs lines expressing it (45) | 1.61× lower at baseline in the lines without TMCC2 | 0.090 | ⚠ within organs, on part of the lines; also absent: AXDND1, SUCLG2-DT, SACS; maybe low, not absent |
| [[TMEM63B]] | B | TMCC2 activity raises TMEM63B's level | lines that do not express TMCC2 (5) vs lines expressing it (45) | 1.53× lower at baseline in the lines without TMCC2 | 0.098 | ⚠ within organs, on part of the lines; also absent: AXDND1, SUCLG2-DT, SACS; maybe low, not absent |

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.693). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (26.1, 0.3); signed map (20.1, 22.1). **Vector** length 58.1, 9.03% of its response variance represented; |z| ≥ 3 in 1,046 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +12.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.2 | +8.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.9 | +14.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +3.9 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +3.8 | +6.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | +7.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.8 | +3.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -3.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | -0.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -1.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.5 | -0.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.4 | -2.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane and coiled-coil domain family 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:205,227,946-205,285,632 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HUCEP11, FLJ38497 |
| Gene groups (HGNC) | Transmembrane and coiled-coil domain containing |
| Hallmark sets | HEME_METABOLISM |
| Matched by | ensembl_id |

**Function**, from UniProt [O75069](https://www.uniprot.org/uniprotkb/O75069) (Transmembrane and coiled-coil domains protein 2):

> May be involved in the regulation of the proteolytic processing of the amyloid precursor protein (APP) possibly also implicating APOE.

**Summary**, from NCBI Gene [9911](https://www.ncbi.nlm.nih.gov/gene/9911):

> Involved in amyloid precursor protein metabolic process. Located in endoplasmic reticulum. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24239](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24239) · Entrez [9911](https://www.ncbi.nlm.nih.gov/gene/9911) · UniProt [O75069](https://www.uniprot.org/uniprotkb/O75069) · Ensembl [ENSG00000133069](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133069)

## Data

Gene col 5411: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5411); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5411, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5411]; `tensor/DDL_lfc|DDL_z.npy` [5411]; `embed/gene_vectors.npy` [5411]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5411 or target_col == 5411). Every well: [[TMCC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMCC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
