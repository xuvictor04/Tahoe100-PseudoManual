---
symbol: "ZP3"
type: "gene"
col: 12009
ensembl_id: "ENSG00000188372"
name: "zona pellucida glycoprotein 3"
location: "7q11.23"
module: 4
arm: "+"
pooled_cpm: 9.32
n_lines_expressing: 39
n_dd_up: 6
n_dd_down: 19
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 6
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# ZP3

*zona pellucida glycoprotein 3* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.56× (z +4.7, q 0.001, up in 5 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Clobetasol propionate (drug)]] 0.5 µM: 1.42× (z +3.9, q 0.018, up in 9 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.468× (z -11.7, q 6e-29, down in 27 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSEN2]] (+0.69, fdr 7e-06), [[PVT1]] (+0.68, fdr 7e-06), [[CLYBL]] (+0.67, fdr 7e-06); moves opposite to [[APAF1]] (-0.57, fdr 1e-05), [[SYNJ1]] (-0.54, fdr 5e-05), [[HNRNPLL]] (-0.53, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LAMC3]] → it (grade B ⚠); 6 go from it, the strongest it → [[LINC02595]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12009.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.56×** | +4.7 | 0.001 | 5/12 (NCI-H2347, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.54×** | +4.4 | 0.003 | 6/18 (A498, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.42×** | +3.9 | 0.018 | 9/34 (HS-578T, HT-29, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.48×** | +3.8 | 0.018 | 14/35 (AsPC-1, NCI-H1573, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.044 | 7/36 (SW480, A549, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.39×** | +3.4 | 0.056 | 10/35 (NCI-H23, NCI-H2030, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | 1.39× | +3.2 | 0.10 | 6/36 (NCI-H2030, A498, …) | inconsistent across doses |  |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 1.22× | +3.0 | 0.17 | 2/36 (HCT15, LOX-IMVI) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12009.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.468×** | -11.7 | 6e-29 | 27/34 (PANC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.511×** | -10.4 | 1e-22 | 25/35 (PANC-1, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.495×** | -7.4 | 3e-11 | 24/36 (PANC-1, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.534×** | -6.6 | 6e-09 | 17/32 (A-427, NCI-H23, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.584×** | -5.7 | 2e-06 | 19/37 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.614×** | -5.3 | 1e-05 | 17/33 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.636×** | -4.7 | 2e-04 | 18/34 (A-427, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.644×** | -4.6 | 3e-04 | 16/30 (PANC-1, A-427, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.641×** | -4.6 | 3e-04 | 14/34 (Hs 766T, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.676×** | -4.3 | 0.001 | 18/35 (PANC-1, LoVo, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.694×** | -4.0 | 0.003 | 10/37 (NCI-H460, A-427, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.703×** | -3.8 | 0.006 | 16/36 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **0.706×** | -3.7 | 0.011 | 17/35 (PANC-1, SW1417, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.734×** | -3.4 | 0.029 | 13/35 (COLO 205, PANC-1, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.554×** | -3.4 | 0.029 | 9/33 (SW48, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.730×** | -3.3 | 0.033 | 16/37 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cloxacillin (sodium) (drug)]] 0.05 µM |  | **0.749×** | -3.2 | 0.051 | 2/36 (Panc 03.27, LoVo) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12009. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 22.5 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0612× (z -30.8) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.174× (z -19.3) |
| [[MIA PaCa-2 (line)]] | alt | 30.0 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0595× (z -23.9) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.110× (z -18.7) |
| [[A-427 (line)]] | wt | 19.4 | 0 | 5 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0790× (z -15.8) |
| [[NCI-H460 (line)]] | wt | 11.4 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -13.5) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -8.5) |
| [[COLO 205 (line)]] | alt | 7.35 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0479× (z -9.8) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.0565× (z -9.6) |
| [[SW48 (line)]] | wt | 18.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0485× (z -11.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.142× (z -10.5) |
| [[SW480 (line)]] | alt | 9.81 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -13.4) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.242× (z -13.2) |
| [[HEC-1-A (line)]] | alt | 11.5 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.144× (z -11.9) |
| [[NCI-H23 (line)]] | alt | 22.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -12.2) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.128× (z -11.5) |
| [[SW1417 (line)]] | alt | 12.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -12.4) |
| [[A498 (line)]] | wt | 19.6 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.203× (z -9.4) ⚠ cell-cycle shift, explains ~35% of this change |
| [[A549 (line)]] | wt | 10.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -9.6) ⚠ cell-cycle shift, explains ~43% of this change |
| [[C-33 A (line)]] | alt | 9.68 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.0771× (z -8.9) |
| [[Hs 766T (line)]] | wt | 6.30 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0556× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~33% of this change |
| [[LoVo (line)]] | wt | 11.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -15.9) ⚠ cell-cycle shift, explains ~43% of this change |
| [[LS 180 (line)]] | wt | 5.12 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0584× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 9.25 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -9.6) ⚠ cell-cycle shift, explains ~43% of this change |
| [[SK-MEL-2 (line)]] | alt | 13.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.136× (z -14.0) |
| [[SNU-423 (line)]] | alt | 6.56 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0814× (z -12.7) |
| [[A-172 (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.06 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12009), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSEN2]] | +0.69 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[PVT1]] | +0.68 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[CLYBL]] | +0.67 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[TANGO6]] | +0.66 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[METAP1D]] | +0.65 | +0.61 / +0.75 | both halves | 7e-06 |  |
| [[POLR1A]] | +0.65 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[ZNF485]] | +0.64 | +0.58 / +0.69 | both halves | 8e-06 |  |
| [[DPH6]] | +0.63 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[KLHDC4]] | +0.62 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[NAA15]] | +0.62 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[SP2-AS1]] | +0.62 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[LINC01357]] | +0.62 | +0.58 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APAF1]] | -0.57 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[SYNJ1]] | -0.54 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[HNRNPLL]] | -0.53 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[MPC2]] | -0.53 | -0.46 / -0.62 | both halves | 3e-05 |  |
| [[CDKL5]] | -0.53 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[SELENOW]] | -0.52 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[SHOC2]] | -0.51 | -0.49 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAMC3]] | B | LAMC3 activity raises ZP3's level | lines that do not express LAMC3 (25) vs lines expressing it (25) | 1.79× lower at baseline in the lines without LAMC3 | 0.019 | ⚠ within organs, on part of the lines; also absent: DLL3, ADD2, CNKSR2 |
| [[MPV17L]] | B | MPV17L activity raises ZP3's level | lines that do not express MPV17L (26) vs lines expressing it (24) | 1.41× lower at baseline in the lines without MPV17L | 0.036 | ⚠ within organs, on part of the lines; also absent: THBD, NR2E3, CYP24A1 |
| [[FAM78B]] | B | FAM78B activity raises ZP3's level | lines that do not express FAM78B (15) vs lines expressing it (35) | 1.70× lower at baseline in the lines without FAM78B | 0.045 | ⚠ within organs, on part of the lines; also absent: SEMA6B, ENSG00000260498, TTYH2 |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02595]] | B | ZP3 activity raises LINC02595's level | lines that do not express ZP3 (11) vs lines expressing it (39) | 2.18× lower at baseline in the lines without ZP3 | 0.030 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[HSF2BP]] | B | ZP3 activity raises HSF2BP's level | lines that do not express ZP3 (11) vs lines expressing it (39) | 1.33× lower at baseline in the lines without ZP3 | 0.050 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TXNRD3]] | B | ZP3 activity raises TXNRD3's level | lines that do not express ZP3 (11) vs lines expressing it (39) | 1.57× lower at baseline in the lines without ZP3 | 0.073 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[GATD1]] | B | ZP3 activity raises GATD1's level | lines that do not express ZP3 (11) vs lines expressing it (39) | 1.38× lower at baseline in the lines without ZP3 | 0.083 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SLC25A13]] | B | ZP3 activity raises SLC25A13's level | lines that do not express ZP3 (11) vs lines expressing it (39) | 1.44× lower at baseline in the lines without ZP3 | 0.088 | ⚠ within organs, on part of the lines; maybe low, not absent |
| cells under [[Sonidegib (drug)]] 5 µM | B | ZP3 activity raises the cells' numbers under Sonidegib 5 µM (protects the cells) | lines that do not express ZP3 (11) vs lines expressing it (37) | the lines without ZP3: 0.83× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.587). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-12.7, -34.6); signed map (-2.4, -49.9). **Vector** length 72.5, 15.7% of its response variance represented; |z| ≥ 3 in 782 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.3 | +2.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +3.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.1 | +4.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.0 | +3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +3.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.5 | +2.1 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +1.4 | +2.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.8 | -11.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.7 | -4.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.9 | -6.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -2.7 | -10.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -1.6 | -7.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -3.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.4 | -4.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.3 | -1.2 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | -1.3 | -2.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.3 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | zona pellucida glycoprotein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23 — chr7:76,397,518-76,442,071 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ZP3-424, ZP3-372, ZPC; previously ZP3A, ZP3B |
| Gene groups (HGNC) | Zona pellucida glycoproteins |
| Reactome | 3 pathways, smallest: Interaction With Cumulus Cells And The Zona Pellucida; Fertilization; Reproduction |
| Matched by | ensembl_id |

**Function**, from UniProt [P21754](https://www.uniprot.org/uniprotkb/P21754) (Zona pellucida sperm-binding protein 3):

> Component of the zona pellucida, an extracellular matrix surrounding oocytes which mediates sperm binding, induction of the acrosome reaction and prevents post-fertilization polyspermy. The zona pellucida is composed of 3 to 4 glycoproteins, ZP1, ZP2, ZP3, and ZP4. ZP3 is essential for sperm binding and zona matrix formation.

**Summary**, from NCBI Gene [7784](https://www.ncbi.nlm.nih.gov/gene/7784):

> The zona pellucida is an extracellular matrix that surrounds the oocyte and early embryo. It is composed primarily of three or four glycoproteins with various functions during fertilization and preimplantation development. The protein encoded by this gene is a structural component of the zona pellucida and functions in primary binding and induction of the sperm acrosome reaction. The nascent protein contains a N-terminal signal peptide sequence, a conserved ZP domain, a C-terminal consensus …

**Accessions** — [HGNC:13189](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13189) · Entrez [7784](https://www.ncbi.nlm.nih.gov/gene/7784) · UniProt [P21754](https://www.uniprot.org/uniprotkb/P21754) · Ensembl [ENSG00000188372](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188372)

## Data

Gene col 12009: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12009); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12009, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12009]; `tensor/DDL_lfc|DDL_z.npy` [12009]; `embed/gene_vectors.npy` [12009]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12009 or target_col == 12009). Every well: [[ZP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
