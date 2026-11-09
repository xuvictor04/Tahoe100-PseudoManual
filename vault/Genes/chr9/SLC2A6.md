---
symbol: "SLC2A6"
type: "gene"
col: 8342
ensembl_id: "ENSG00000160326"
name: "solute carrier family 2 member 6"
location: "9q34.2"
module: 14
arm: "+"
pooled_cpm: 5.83
n_lines_expressing: 44
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 13
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# SLC2A6

*solute carrier family 2 member 6* — 9q34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.20× (z +17.0, q 0e+00, up in 28 of 34 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IL32]] (+0.73, fdr 7e-06), [[CCL5]] (+0.72, fdr 7e-06), [[KMO]] (+0.72, fdr 7e-06); moves opposite to [[THOC5]] (-0.56, fdr 1e-05), [[BCAP31]] (-0.56, fdr 1e-05), [[STRAP]] (-0.56, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SSTR2]] → it (grade B ⚠); 13 go from it, the strongest it → [[ZFHX2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8342.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.20×** | +17.0 | 0e+00 | 28/34 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **7.60×** | +14.2 | 3e-43 | 36/40 (J82, A498, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.64×** | +9.4 | 1e-18 | 21/33 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.23×** | +8.3 | 2e-14 | 27/34 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.46×** | +6.6 | 6e-09 | 25/39 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **2.10×** | +5.4 | 6e-06 | 8/19 (J82, RPMI-7951, …) | two highest doses | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.62×** | +5.0 | 5e-05 | 21/41 (A-172, HOP62, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.93×** | +4.6 | 3e-04 | 18/34 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.79×** | +4.2 | 0.001 | 14/41 (SW480, SW1417, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.62×** | +3.5 | 0.024 | 15/39 (SW480, SW1417, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.55×** | +3.3 | 0.052 | 10/41 (HOP62, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.57×** | +3.3 | 0.052 | 12/30 (SW 900, PANC-1, …) | top dose only | position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.052 | 12/39 (SNU-1, C-33 A, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.57×** | +3.2 | 0.062 | 11/33 (A498, HS-578T, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **1.54×** | +3.1 | 0.062 | 7/25 (MIA PaCa-2, HepG2/C3A, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.50×** | +2.9 | 0.097 | 12/38 (A498, A-172, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8342.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Quinestrol (drug)]] 5 µM |  | 0.741× | -3.1 | 0.71 | 6/40 (BT-474, CHP-212, …) | top dose only | position effect removed |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.661× | -3.0 | 0.71 | 11/40 (C-33 A, HCT15, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8342. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 24.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +19.4) | — |
| [[HS-578T (line)]] | alt | 5.81 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.8× (z +12.1) | — |
| [[A-172 (line)]] | wt | 11.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +15.3) | — |
| [[HEC-1-A (line)]] | alt | 2.27 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.1× (z +12.0) | — |
| [[J82 (line)]] | alt | 26.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.2× (z +20.5) | — |
| [[SNU-423 (line)]] | alt | 6.39 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 38.9× (z +16.3) | — |
| [[HOP62 (line)]] | alt | 5.28 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.9× (z +16.4) | — |
| [[Panc 03.27 (line)]] | alt | 7.33 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.6× (z +14.4) | — |
| [[PANC-1 (line)]] | alt | 6.81 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.88× (z +12.0) | — |
| [[SW 900 (line)]] | alt | 5.61 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.7× (z +13.8) | — |
| [[A549 (line)]] | wt | 12.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.09× (z +9.2) | — |
| [[AsPC-1 (line)]] | alt | 5.11 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 46.5× (z +17.6) | — |
| [[BT-474 (line)]] | alt | 5.26 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 36.9× (z +12.6) | — |
| [[CFPAC-1 (line)]] | alt | 3.96 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.9× (z +13.3) | — |
| [[HepG2_C3A (line)]] | wt | 5.78 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.6× (z +11.8) | — |
| [[hTERT-HPNE (line)]] | wt | 3.14 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 32.2× (z +10.9) | — |
| [[RPMI-7951 (line)]] | alt | 6.93 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 26.0× (z +10.0) | — |
| [[A-427 (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.644 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.927 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.44 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.936 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.820 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.99 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.19 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.47 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.21 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8342), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IL32]] | +0.73 | +0.78 / +0.70 | both halves | 7e-06 |  |
| [[CCL5]] | +0.72 | +0.68 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[KMO]] | +0.72 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[TNFAIP2]] | +0.69 | +0.70 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[MARCKS]] | +0.69 | +0.62 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[CSF1]] | +0.68 | +0.66 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[CX3CL1]] | +0.68 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[NINJ1]] | +0.68 | +0.57 / +0.72 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[NEURL3]] | +0.67 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[MSC]] | +0.65 | +0.53 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[STAP2]] | +0.64 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[BTN2A2]] | +0.63 | +0.67 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THOC5]] | -0.56 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[BCAP31]] | -0.56 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[STRAP]] | -0.56 | -0.54 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SSTR2]] | B | SSTR2 activity raises SLC2A6's level | lines that do not express SSTR2 (25) vs lines expressing it (25) | 1.83× lower at baseline in the lines without SSTR2 | 0.027 | ⚠ within organs, on part of the lines; also absent: PPP2R2B, DKK3, ENSG00000260517 |
| [[CSF1]] | B | CSF1 activity raises SLC2A6's level | lines that do not express CSF1 (21) vs lines expressing it (29) | 2.05× lower at baseline in the lines without CSF1 | 0.035 | ⚠ within organs, on part of the lines; also absent: SERPINE1, TNFRSF9, ROR1-AS1 |
| [[IFI16]] | B | IFI16 activity strengthens SLC2A6's drug response | lines that do not express IFI16 (17) vs lines expressing it (25) | the lines without IFI16 respond 0.64× as strongly (z diff +0.91); strongest at Homoharringtonine 0.5 µM: 2.50x vs 5.00x (z diff +2.5) | 0.092 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF; target measured in part of the lines; artifact flags |
| [[SLC43A2]] | C | SLC43A2 activity raises SLC2A6's level | lines that do not express SLC43A2 (3) vs lines expressing it (47) | 2.56× lower at baseline in the lines without SLC43A2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CTDSPL, ZNF44, ITGA9-AS1; maybe low, not absent; its own permutation p |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 13, C 0. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZFHX2]] | B | SLC2A6 activity raises ZFHX2's level | lines that do not express SLC2A6 (6) vs lines expressing it (44) | 1.93× lower at baseline in the lines without SLC2A6 | 0.051 | ⚠ within organs, on part of the lines; also absent: GFOD1, SOAT1, RGS9; maybe low, not absent |
| [[CSF1]] | B | SLC2A6 activity raises CSF1's level | lines that do not express SLC2A6 (6) vs lines expressing it (44) | 3.03× lower at baseline in the lines without SLC2A6 | 0.057 | ⚠ within organs, on part of the lines; also absent: GFOD1, SOAT1, RGS9; maybe low, not absent |
| [[SLC31A2]] | B | SLC2A6 activity raises SLC31A2's level | lines that do not express SLC2A6 (6) vs lines expressing it (44) | 1.36× lower at baseline in the lines without SLC2A6 | 0.066 | ⚠ within organs, on part of the lines; also absent: GFOD1, SOAT1, RGS9; maybe low, not absent |
| [[SDSL]] | B | SLC2A6 activity raises SDSL's level | lines that do not express SLC2A6 (6) vs lines expressing it (44) | 1.52× lower at baseline in the lines without SLC2A6 | 0.067 | ⚠ within organs, on part of the lines; also absent: GFOD1, SOAT1, RGS9; maybe low, not absent |
| [[FLT3LG]] | B | SLC2A6 activity raises FLT3LG's level | lines that do not express SLC2A6 (6) vs lines expressing it (44) | 1.42× lower at baseline in the lines without SLC2A6 | 0.068 | ⚠ within organs, on part of the lines; also absent: GFOD1, SOAT1, RGS9; maybe low, not absent |
| [[BTN2A2]] | B | SLC2A6 activity raises BTN2A2's level | lines that do not express SLC2A6 (6) vs lines expressing it (44) | 1.92× lower at baseline in the lines without SLC2A6 | 0.072 | ⚠ within organs, on part of the lines; also absent: GFOD1, SOAT1, RGS9; maybe low, not absent |
| [[FDX2]] | B | SLC2A6 activity raises FDX2's level | lines that do not express SLC2A6 (6) vs lines expressing it (44) | 1.41× lower at baseline in the lines without SLC2A6 | 0.073 | ⚠ within organs, on part of the lines; also absent: GFOD1, SOAT1, RGS9; maybe low, not absent |
| [[DNPEP]] | B | SLC2A6 activity raises DNPEP's level | lines that do not express SLC2A6 (6) vs lines expressing it (44) | 1.13× lower at baseline in the lines without SLC2A6 | 0.075 | ⚠ within organs, on part of the lines; also absent: GFOD1, SOAT1, RGS9; maybe low, not absent |
| [[RHOV]] | B | SLC2A6 activity lowers RHOV's level | lines that do not express SLC2A6 (6) vs lines expressing it (44) | 2.49× higher at baseline in the lines without SLC2A6 | 0.079 | ⚠ within organs, on part of the lines; also absent: GFOD1, SOAT1, RGS9; maybe low, not absent |
| [[IL10RB]] | B | SLC2A6 activity lowers IL10RB's level | lines that do not express SLC2A6 (6) vs lines expressing it (44) | 1.49× higher at baseline in the lines without SLC2A6 | 0.083 | ⚠ within organs, on part of the lines; also absent: GFOD1, SOAT1, RGS9; maybe low, not absent |
| [[SLC31A2]] | B | SLC2A6 activity strengthens SLC31A2's drug response | lines that do not express SLC2A6 (6) vs lines expressing it (41) | the lines without SLC2A6 respond 0.67× as strongly (z diff +0.96); strongest at Homoharringtonine 5 µM: 2.05x vs 5.66x (z diff +4.3) | 0.093 | ⚠ within organs, on part of the lines; also absent: GFOD1, SOAT1, RGS9; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[ZFHX2]] | B | SLC2A6 activity strengthens ZFHX2's drug response | lines that do not express SLC2A6 (6) vs lines expressing it (38) | the lines without SLC2A6 respond 0.87× as strongly (z diff +0.58); strongest at Homoharringtonine 0.5 µM: 2.14x vs 3.98x (z diff +3.2) | 0.093 | ⚠ within organs, on part of the lines; also absent: GFOD1, SOAT1, RGS9; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.797). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.8, 3.1); signed map (44.0, 9.7). **Vector** length 78.6, 18.4% of its response variance represented; |z| ≥ 3 in 730 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *NF-kB* (control, mean cos +0.51 to 12); *inflammatory response* (hallmark, mean cos +0.53 to 22); *Chemokine receptors bind chemokines* (reactome, mean cos +0.53 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +7.0 | +14.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.0 | +17.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.9 | +9.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.2 | +6.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +8.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.5 | +4.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.1 | +3.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.0 | +2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.8 | +2.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.4 | +2.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.1 | -0.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.8 | -0.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -2.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.7 | -2.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -3.0 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.6 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 2 member 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.2 — chr9:133,471,094-133,479,127 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GLUT9, GLUT6, HSA011372 |
| Gene groups (HGNC) | Solute carrier family 2 |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB |
| Reactome | 3 pathways, smallest: Cellular hexose transport; SLC-mediated transmembrane transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UGQ3](https://www.uniprot.org/uniprotkb/Q9UGQ3) (Solute carrier family 2, facilitated glucose transporter member 6):

> Probable sugar transporter that acts as a regulator of glycolysis in macrophages (Probable). Does not transport glucose.

**Summary**, from NCBI Gene [11182](https://www.ncbi.nlm.nih.gov/gene/11182):

> Hexose transport into mammalian cells is catalyzed by a family of membrane proteins, including SLC2A6, that contain 12 transmembrane domains and a number of critical conserved residues.[supplied by OMIM, Jul 2002]

**Accessions** — [HGNC:11011](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11011) · Entrez [11182](https://www.ncbi.nlm.nih.gov/gene/11182) · UniProt [Q9UGQ3](https://www.uniprot.org/uniprotkb/Q9UGQ3) · Ensembl [ENSG00000160326](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160326)

## Data

Gene col 8342: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8342); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8342, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8342]; `tensor/DDL_lfc|DDL_z.npy` [8342]; `embed/gene_vectors.npy` [8342]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8342 or target_col == 8342). Every well: [[SLC2A6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC2A6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
