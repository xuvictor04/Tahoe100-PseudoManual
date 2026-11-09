---
symbol: "EBPL"
type: "gene"
col: 4413
ensembl_id: "ENSG00000123179"
name: "EBP like"
location: "13q14.2"
module: 18
arm: "+"
pooled_cpm: 21.85
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 15
n_dd_up_clean: 3
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# EBPL

*EBP like* — 13q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.55× (z +7.3, q 2e-10, up in 27 of 42 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Radotinib (drug)]] 5 µM: 1.15× (z +3.4, q 0.072, up in 15 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.474× (z -17.6, q 0e+00, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TBC1D14]] (+0.70, fdr 7e-06), [[METAP1]] (+0.69, fdr 7e-06), [[FXN]] (+0.68, fdr 1e-05); moves opposite to [[USP11]] (-0.61, fdr 1e-05), [[TP53INP2]] (-0.57, fdr 1e-05), [[TSGA10]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[WNK2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4413.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.55×** | +7.3 | 2e-10 | 27/42 (A498, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +5.6 | 5e-06 | 22/46 (A-172, COLO 205, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.34×** | +4.7 | 4e-04 | 21/35 (KATO III, A498, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +3.7 | 0.029 | 15/47 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.27×** | +3.7 | 0.029 | 17/37 (A-172, A549, …) | all doses, stronger at high dose | composition shift |
| [[Radotinib (drug)]] 5 µM |  | 1.15× | +3.4 | 0.072 | 15/48 (CFPAC-1, COLO 205, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.22×** | +3.3 | 0.073 | 15/47 (NCI-H1573, A498, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 1.15× | +3.3 | 0.074 | 8/48 (Hs 766T, PANC-1, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.21×** | +3.2 | 0.081 | 13/47 (Panc 03.27, A498, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.34×** | +3.2 | 0.081 | 9/45 (RKO, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.21×** | +3.2 | 0.081 | 18/47 (COLO 205, HT-29, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, none with an alert; shown: the 15 strongest. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4413.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.474×** | -17.6 | 0e+00 | 39/47 (RKO, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.489×** | -11.9 | 2e-30 | 35/46 (RKO, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.510×** | -10.8 | 5e-25 | 39/47 (NCI-H23, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.673×** | -6.6 | 5e-09 | 29/47 (RKO, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.588×** | -4.6 | 4e-04 | 21/48 (SW480, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.768×** | -4.2 | 0.002 | 17/47 (NCI-H2030, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.787×** | -4.0 | 0.005 | 16/48 (RKO, CHP-212, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.787×** | -4.0 | 0.005 | 15/47 (BT-474, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.653×** | -3.7 | 0.012 | 14/47 (H4, AN3 CA, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.856× | -3.7 | 0.014 | 16/48 (NCI-H2030, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.819×** | -3.3 | 0.038 | 10/47 (SW48, AsPC-1, …) | inconsistent across doses |  |
| [[NVP-BHG712 (drug)]] 0.05 µM |  | **0.809×** | -3.3 | 0.038 | 8/48 (Hs 766T, A498, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.819×** | -3.3 | 0.038 | 18/47 (BT-474, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.821×** | -3.3 | 0.039 | 18/47 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.829×** | -3.1 | 0.065 | 12/47 (H4, Hs 766T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4413. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 43.4 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -18.5) |
| [[NCI-H460 (line)]] | wt | 23.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.255× (z -12.1) |
| [[PANC-1 (line)]] | alt | 30.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -16.7) |
| [[BT-474 (line)]] | alt | 18.0 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.174× (z -10.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.320× (z -9.7) |
| [[Hs 766T (line)]] | wt | 35.2 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.297× (z -13.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.426× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 41.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -13.2) |
| [[NCI-H23 (line)]] | alt | 24.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -13.4) |
| [[SW48 (line)]] | wt | 41.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -12.3) |
| [[A-172 (line)]] | wt | 12.6 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.201× (z -9.1) |
| [[A498 (line)]] | wt | 19.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[HCT15 (line)]] | alt | 34.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.217× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 16.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -10.8) |
| [[LOX-IMVI (line)]] | wt | 27.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -9.1) |
| [[LS 180 (line)]] | wt | 41.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -10.9) |
| [[NCI-H2030 (line)]] | alt | 15.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -11.4) |
| [[NCI-H2347 (line)]] | alt | 15.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -13.6) |
| [[Panc 03.27 (line)]] | alt | 30.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -12.4) |
| [[SK-MEL-2 (line)]] | alt | 14.2 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.151× (z -9.6) |
| [[SNU-1 (line)]] | wt | 23.7 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.164× (z -8.9) |
| [[SW480 (line)]] | alt | 31.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -11.8) |
| [[A-427 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.84 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4413), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D14]] | +0.70 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[METAP1]] | +0.69 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[FXN]] | +0.68 | +0.72 / +0.57 | both halves | 1e-05 |  |
| [[SORD]] | +0.68 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[WDR3]] | +0.67 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[CCDC88C]] | +0.67 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[SFXN4]] | +0.66 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[MDN1]] | +0.66 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[UCK2]] | +0.65 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[DDX54]] | +0.65 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[DFFB]] | +0.64 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[ASB13]] | +0.64 | +0.63 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP11]] | -0.61 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[TP53INP2]] | -0.57 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[TSGA10]] | -0.55 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[RIPK2-DT]] | -0.55 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[CDKN2B]] | -0.55 | -0.50 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WNK2]] | B | WNK2 activity raises EBPL's level | lines that do not express WNK2 (16) vs lines expressing it (34) | 1.52× lower at baseline in the lines without WNK2 | 0.021 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, CHDH |
| [[DUXAP10]] | B | DUXAP10 activity raises EBPL's level | lines that do not express DUXAP10 (7) vs lines expressing it (43) | 1.42× lower at baseline in the lines without DUXAP10 | 0.024 | ⚠ within organs, on part of the lines; also absent: DUXAP8, KLRG1, DUXAP9 |
| [[DUXAP8]] | B | DUXAP8 activity raises EBPL's level | lines that do not express DUXAP8 (7) vs lines expressing it (43) | 1.46× lower at baseline in the lines without DUXAP8 | 0.048 | ⚠ within organs, on part of the lines; also absent: DUXAP10, DUXAP9, TTYH2 |
| [[LRRC20]] | B | LRRC20 activity raises EBPL's level | lines that do not express LRRC20 (5) vs lines expressing it (45) | 1.84× lower at baseline in the lines without LRRC20 | 0.078 | ⚠ within organs, on part of the lines; also absent: MCM2, MCM10, SEMA4D; maybe low, not absent |
| [[MCOLN2]] | B | MCOLN2 activity raises EBPL's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 1.11× lower at baseline in the lines without MCOLN2 | 0.082 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[ANKRD13B]] | C | ANKRD13B activity raises EBPL's level | lines that do not express ANKRD13B (3) vs lines expressing it (47) | 1.70× lower at baseline in the lines without ANKRD13B | 0.077 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.701). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-9.2, -38.7); signed map (-6.7, -54.7). **Vector** length 92.4, 20.5% of its response variance represented; |z| ≥ 3 in 894 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Nucleotide biosynthesis* (reactome, mean cos +0.51 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.7 | +3.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +2.7 | +3.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.2 | +5.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.2 | +2.8 |
|  | [[EX229 (drug)]] 5 µM |  | +2.1 | +2.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.1 | +2.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.0 | +1.7 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +2.0 | +2.1 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.3 | -10.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.8 | -17.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.5 | -11.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.2 | -3.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -3.7 | -4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -3.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.1 | -3.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.8 | +0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | EBP like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.2 — chr13:49,660,674-49,691,486 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EBRP |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BY08](https://www.uniprot.org/uniprotkb/Q9BY08) (Emopamil-binding protein-like):

> Does not possess sterol isomerase activity and does not bind sigma ligands.

**Summary**, from NCBI Gene [84650](https://www.ncbi.nlm.nih.gov/gene/84650):

> Predicted to enable cholestenol delta-isomerase activity. Predicted to be involved in sterol metabolic process. Located in endoplasmic reticulum. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18061](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18061) · Entrez [84650](https://www.ncbi.nlm.nih.gov/gene/84650) · UniProt [Q9BY08](https://www.uniprot.org/uniprotkb/Q9BY08) · Ensembl [ENSG00000123179](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123179)

## Data

Gene col 4413: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4413); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4413, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4413]; `tensor/DDL_lfc|DDL_z.npy` [4413]; `embed/gene_vectors.npy` [4413]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4413 or target_col == 4413). Every well: [[EBPL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EBPL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
