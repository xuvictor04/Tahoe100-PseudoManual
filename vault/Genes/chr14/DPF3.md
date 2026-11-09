---
symbol: "DPF3"
type: "gene"
col: 13001
ensembl_id: "ENSG00000205683"
name: "double PHD fingers 3"
location: "14q24.2"
module: 81
arm: "+"
pooled_cpm: 8.74
n_lines_expressing: 37
n_dd_up: 38
n_dd_down: 11
n_dd_up_clean: 27
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 9
direction_downstream: 7
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# DPF3

*double PHD fingers 3* — 14q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 43.3× (z +49.0, q 0e+00, up in 34 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (none with an alert); the strongest is [[Betamethasone dipropionate (drug)]] 5 µM: 0.646× (z -5.5, q 2e-05, down in 14 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTHLH]] (+0.67, fdr 1e-05), [[EHD1]] (+0.67, fdr 2e-05), [[ANTXR2]] (+0.65, fdr 2e-05); moves opposite to [[NAGPA]] (-0.55, fdr 1e-05), [[LTBR]] (-0.53, fdr 3e-05), [[CMKLR2]] (-0.49, fdr 9e-05).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 7 go from it, the strongest it → [[TM4SF1-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13001.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **43.3×** | +49.0 | 0e+00 | 34/34 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **14.0×** | +48.5 | 0e+00 | 28/29 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **31.9×** | +45.0 | 0e+00 | 34/34 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **29.4×** | +43.9 | 0e+00 | 34/34 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **10.6×** | +43.3 | 0e+00 | 29/29 (CFPAC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **10.4×** | +30.4 | 0e+00 | 34/34 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **6.18×** | +23.7 | 0e+00 | 24/27 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **6.55×** | +23.5 | 0e+00 | 24/28 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.40×** | +22.5 | 0e+00 | 31/34 (SW480, LS 180, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **5.07×** | +20.3 | 0e+00 | 23/25 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.75×** | +18.5 | 0e+00 | 28/34 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **4.28×** | +18.2 | 0e+00 | 28/31 (LoVo, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **11.9×** | +16.8 | 0e+00 | 31/32 (LoVo, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **3.63×** | +16.7 | 0e+00 | 26/27 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **2.61×** | +12.0 | 2e-31 | 12/20 (LoVo, HEC-1-A, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.47×** | +11.8 | 2e-30 | 27/33 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13001.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.646×** | -5.5 | 2e-05 | 14/32 (HOP62, J82, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.669×** | -5.2 | 5e-05 | 13/32 (HOP62, RPMI-7951, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.714×** | -4.4 | 0.002 | 13/31 (HOP62, HS-578T, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.908× | -4.4 | 0.002 | 7/35 (NCI-H2030, HOP62, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.733×** | -4.1 | 0.006 | 10/26 (NCI-H2030, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.5 µM |  | **0.743×** | -3.9 | 0.010 | 15/32 (HOP62, NCI-H2030, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.749×** | -3.8 | 0.013 | 14/32 (HOP62, NCI-H2030, …) | inconsistent across doses |  |
| [[Econazole (drug)]] 5 µM |  | **0.761×** | -3.6 | 0.024 | 12/34 (HOP62, NCI-H2030, …) | top dose only |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.762×** | -3.5 | 0.024 | 11/34 (HOP62, hTERT-HPNE, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.764×** | -3.5 | 0.025 | 14/30 (A-172, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.776×** | -3.3 | 0.046 | 17/33 (NCI-H2030, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.777×** | -3.3 | 0.046 | 12/34 (A-172, J82, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.78 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13001. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 14.7 | 10 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.1× (z +15.3) | [[Clobetasol propionate (drug)]] 0.5 µM 0.0922× (z -11.2) |
| [[LoVo (line)]] | wt | 6.65 | 12 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 23.2× (z +20.3) | — |
| [[HOP62 (line)]] | alt | 17.1 | 8 | 3 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +17.4) | [[Betamethasone dipropionate (drug)]] 5 µM 0.0797× (z -12.8) |
| [[HEC-1-A (line)]] | alt | 6.36 | 10 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.8× (z +17.0) | — |
| [[SW480 (line)]] | alt | 3.92 | 10 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.7× (z +17.3) | — |
| [[BT-474 (line)]] | alt | 12.7 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.2× (z +16.4) | — |
| [[CFPAC-1 (line)]] | alt | 70.6 | 6 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.65× (z +22.1) | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 13.5 | 7 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 20.5× (z +14.4) | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 9.58 | 7 | 1 | [[Panobinostat (drug)]] 5 µM 30.5× (z +13.0) | [[Roxadustat (drug)]] 0.05 µM 0.0885× (z -8.6) |
| [[LS 180 (line)]] | wt | 3.12 | 7 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 28.4× (z +12.9) | — |
| [[RKO (line)]] | wt | 6.87 | 6 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.1× (z +11.7) | [[Ixazomib citrate (drug)]] 0.5 µM 0.0539× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 21.5 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +14.3) | — |
| [[Panc 03.27 (line)]] | alt | 20.6 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.95× (z +15.2) | — |
| [[SW1417 (line)]] | alt | 3.14 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.0× (z +11.4) | — |
| [[A549 (line)]] | wt | 5.22 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 43.9× (z +11.0) | — |
| [[C32 (line)]] | wt | 4.26 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 29.6× (z +13.6) | — |
| [[HepG2_C3A (line)]] | wt | 3.49 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.7× (z +9.9) | — |
| [[NCI-H1573 (line)]] | alt | 2.38 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 33.0× (z +12.4) | — |
| [[NCI-H2030 (line)]] | alt | 38.3 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 15.7× (z +15.2) | [[Adagrasib (drug)]] 0.05 µM 0.527× (z -12.7) ⚠ position not correctable |
| [[RPMI-7951 (line)]] | alt | 34.7 | 4 | 1 | [[Panobinostat (drug)]] 5 µM 7.87× (z +10.4) | [[Auranofin (drug)]] 5 µM 0.135× (z -10.2) |
| [[SW48 (line)]] | wt | 6.57 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.6× (z +10.6) | — |
| [[HCT15 (line)]] | alt | 3.80 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.9× (z +10.0) | — |
| [[Hs 766T (line)]] | wt | 7.53 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 22.5× (z +11.5) | — |
| [[HS-578T (line)]] | alt | 10.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.22× (z +12.1) | — |
| [[J82 (line)]] | alt | 15.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 13.2× (z +12.0) | — |
| [[NCI-H1792 (line)]] | alt | 2.37 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 57.1× (z +10.3) | — |
| [[SK-MEL-2 (line)]] | alt | 3.57 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 31.6× (z +9.2) | — |
| [[H4 (line)]] | wt | 2.48 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 78.6× (z +9.2) | — |
| [[SHP-77 (line)]] | alt | 13.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.41× (z +11.2) | — |
| [[A-427 (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.14 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.89 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.53 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13001), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTHLH]] | +0.67 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[EHD1]] | +0.67 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[ANTXR2]] | +0.65 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[FAM107B]] | +0.65 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[PRDM8]] | +0.65 | +0.50 / +0.57 | both halves | 1e-05 | same gene group |
| [[IL11]] | +0.64 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[BCL2A1]] | +0.63 | +0.46 / +0.63 | both halves | 3e-05 | pathway: MITF-M-dependent gene expression |
| [[AFF3]] | +0.62 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[LINC00973]] | +0.62 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[PKIA]] | +0.61 | +0.46 / +0.72 | both halves | 2e-05 |  |
| [[HBEGF]] | +0.61 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[TMEM158]] | +0.61 | +0.41 / +0.60 | both halves | 4e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAGPA]] | -0.55 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[LTBR]] | -0.53 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[CMKLR2]] | -0.49 | -0.37 / -0.42 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DPF3's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 6.4% of all compounds | 0.008 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[NR3C1]] | B | NR3C1 activity lowers DPF3's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.2% of all compounds | 0.020 | ⚠ off-target possible; 3 compounds |
| [[LINC00973]] | B | LINC00973 activity raises DPF3's level | lines that do not express LINC00973 (23) vs lines expressing it (27) | 2.12× lower at baseline in the lines without LINC00973 | 0.027 | ⚠ within organs, on part of the lines; also absent: ENSG00000239462, IL11, BICC1 |
| [[TSPAN5]] | B | TSPAN5 activity raises DPF3's level | lines that do not express TSPAN5 (9) vs lines expressing it (41) | 2.02× lower at baseline in the lines without TSPAN5 | 0.060 | ⚠ within organs, on part of the lines; also absent: KLF12 |
| [[TRAF1]] | B | TRAF1 activity raises DPF3's level | lines that do not express TRAF1 (12) vs lines expressing it (38) | 2.22× lower at baseline in the lines without TRAF1 | 0.076 | ⚠ within organs, on part of the lines; also absent: MT2A, TUBA1A, ENSG00000230479; maybe low, not absent |
| [[CSF2]] | B | CSF2 activity raises DPF3's level | lines that do not express CSF2 (26) vs lines expressing it (24) | 2.07× lower at baseline in the lines without CSF2 | 0.076 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: IL6, CCBE1, G0S2 |
| [[IL11]] | B | IL11 activity raises DPF3's level | lines that do not express IL11 (27) vs lines expressing it (23) | 2.04× lower at baseline in the lines without IL11 | 0.081 | ⚠ within organs, on part of the lines; also absent: EDNRA, LINC00973, LINC01583 |
| [[GLUL]] | B | GLUL activity raises DPF3's level | lines that do not express GLUL (10) vs lines expressing it (40) | 2.03× lower at baseline in the lines without GLUL | 0.090 | ⚠ within organs, on part of the lines |
| [[PINLYP]] | B | PINLYP activity raises DPF3's level | lines that do not express PINLYP (17) vs lines expressing it (33) | 1.84× lower at baseline in the lines without PINLYP | 0.0997 | ⚠ within organs, on part of the lines; also absent: C9, BMPER, CALD1; maybe low, not absent |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TM4SF1-AS1]] | B | DPF3 activity weakens TM4SF1-AS1's drug response | lines that do not express DPF3 (11) vs lines expressing it (22) | the lines without DPF3 respond 1.86× as strongly (z diff -1.98); strongest at Homoharringtonine 5 µM: 0.27x vs 0.55x (z diff -4.7) | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000267175, RNF152, RORA; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[TM4SF1-AS1]] | B | DPF3 activity lowers TM4SF1-AS1's level | lines that do not express DPF3 (13) vs lines expressing it (37) | 1.98× higher at baseline in the lines without DPF3 | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000267175, RNF152, RORA; maybe low, not absent |
| [[MAMLD1]] | B | DPF3 activity raises MAMLD1's level | lines that do not express DPF3 (13) vs lines expressing it (37) | 2.11× lower at baseline in the lines without DPF3 | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000267175, RNF152, RORA; maybe low, not absent |
| [[GLUL]] | B | DPF3 activity raises GLUL's level | lines that do not express DPF3 (13) vs lines expressing it (37) | 2.82× lower at baseline in the lines without DPF3 | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000267175, RNF152, RORA; maybe low, not absent |
| [[TMEM158]] | B | DPF3 activity raises TMEM158's level | lines that do not express DPF3 (13) vs lines expressing it (37) | 2.18× lower at baseline in the lines without DPF3 | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000267175, RNF152, RORA; maybe low, not absent |
| [[AMOTL1]] | B | DPF3 activity raises AMOTL1's level | lines that do not express DPF3 (13) vs lines expressing it (37) | 2.46× lower at baseline in the lines without DPF3 | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000267175, RNF152, RORA; maybe low, not absent |
| [[SMTN]] | B | DPF3 activity raises SMTN's level | lines that do not express DPF3 (13) vs lines expressing it (37) | 1.77× lower at baseline in the lines without DPF3 | 0.090 | ⚠ within organs, on part of the lines; also absent: ENSG00000267175, RNF152, RORA; maybe low, not absent |

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.714). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (42.9, 0.1); signed map (2.5, 45.1). **Vector** length 79.0, 16.0% of its response variance represented; |z| ≥ 3 in 1,346 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +22.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.6 | +9.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +18.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.3 | +18.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.9 | +11.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.3 | +16.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.2 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.2 | +3.1 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | +1.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.3 | -1.3 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.2 | -3.5 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | -2.9 | -2.6 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.9 | -4.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.9 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | double PHD fingers 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.2 — chr14:72,609,034-72,894,101 (-) |
| Ensembl biotype | protein_coding |
| Also known as | cer-d4, Cerd4, FLJ14079, BAF45c, SMARCG3 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; PHD finger proteins; BAF complex subunits |
| Reactome | 15 pathways, smallest: Formation of the canonical BAF (cBAF) complex; Formation of neuronal progenitor and neuronal BAF (npBAF and nBAF); SWI/SNF chromatin remodelers |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92784](https://www.uniprot.org/uniprotkb/Q92784) (Zinc finger protein DPF3):

> Belongs to the neuron-specific chromatin remodeling complex (nBAF complex). During neural development a switch from a stem/progenitor to a post-mitotic chromatin remodeling mechanism occurs as neurons exit the cell cycle and become committed to their adult state. The transition from proliferating neural stem/progenitor cells to post-mitotic neurons requires a switch in subunit composition of the npBAF and nBAF complexes. As neural progenitors exit mitosis and differentiate into neurons, npBAF …

**Summary**, from NCBI Gene [8110](https://www.ncbi.nlm.nih.gov/gene/8110):

> This gene encodes a member of the D4 protein family. The encoded protein is a transcription regulator that binds acetylated histones and is a component of the BAF chromatin remodeling complex. Alternate splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:17427](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17427) · Entrez [8110](https://www.ncbi.nlm.nih.gov/gene/8110) · UniProt [Q92784](https://www.uniprot.org/uniprotkb/Q92784) · Ensembl [ENSG00000205683](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205683)

## Data

Gene col 13001: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13001); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13001, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13001]; `tensor/DDL_lfc|DDL_z.npy` [13001]; `embed/gene_vectors.npy` [13001]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13001 or target_col == 13001). Every well: [[DPF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DPF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
