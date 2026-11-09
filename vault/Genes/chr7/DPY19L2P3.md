---
symbol: "DPY19L2P3"
type: "gene"
col: 13611
ensembl_id: "ENSG00000227855"
name: "DPY19L2 pseudogene 3"
location: "7p14.3"
module: 15
arm: "+"
pooled_cpm: 6.49
n_lines_expressing: 49
n_dd_up: 9
n_dd_down: 32
n_dd_up_clean: 6
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# DPY19L2P3

*DPY19L2 pseudogene 3* — 7p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.24× (z +28.3, q 0e+00, up in 40 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.601× (z -9.9, q 2e-20, down in 28 of 40 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.499× (z -9.0, q 4e-17, down in 24 of 44 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNRF2P2]] (+0.71, fdr 7e-06, ⚠ same locus), [[SPESP1]] (+0.70, fdr 1e-05), [[DPY19L1P1]] (+0.65, fdr 7e-06), [[FKBP14-AS1]] (+0.64, fdr 3e-05); moves opposite to [[DPF1]] (-0.55, fdr 8e-05), [[DNAJB1]] (-0.53, fdr 1e-04), [[NUDT12]] (-0.51, fdr 2e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13611.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.24×** | +28.3 | 0e+00 | 40/41 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.66×** | +7.0 | 5e-10 | 9/26 (J82, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +6.4 | 3e-08 | 16/36 (H4, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.56×** | +5.8 | 9e-07 | 2/10 (HOP62, HT-29) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +5.5 | 5e-06 | 16/42 (HT-29, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.36×** | +4.3 | 0.001 | 6/43 (A498, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.32×** | +3.8 | 0.011 | 2/42 (SW480, LoVo) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.021 | 11/41 (SW480, A-172, …) | all doses, stronger at high dose |  |
| [[Larotrectinib sulfate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +3.3 | 0.061 | 2/45 (NCI-H1573, HEC-1-A) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13611.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.601×** | -9.9 | 2e-20 | 28/40 (PANC-1, HEC-1-A, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.499×** | -9.0 | 4e-17 | 24/44 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.565×** | -7.9 | 8e-13 | 25/45 (HEC-1-A, SW48, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.605×** | -6.9 | 6e-10 | 21/46 (PANC-1, C-33 A, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.619×** | -6.6 | 5e-09 | 20/39 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.654×** | -5.8 | 5e-07 | 19/45 (PANC-1, SHP-77, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.679×** | -5.3 | 8e-06 | 17/44 (HT-29, NCI-H2030, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.682×** | -5.3 | 1e-05 | 13/45 (HT-29, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.502×** | -5.0 | 4e-05 | 15/42 (C-33 A, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.517×** | -4.8 | 1e-04 | 12/43 (HEC-1-A, COLO 205, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.519×** | -4.7 | 1e-04 | 12/37 (MIA PaCa-2, BT-474, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.695×** | -4.7 | 1e-04 | 15/43 (SNU-423, SNU-1, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.541×** | -4.4 | 4e-04 | 14/37 (C-33 A, LS 180, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.565×** | -4.1 | 0.002 | 13/37 (A498, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Decitabine (drug)]] 0.05 µM |  | **0.724×** | -4.1 | 0.002 | 11/40 (AsPC-1, HCT15, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.756×** | -3.8 | 0.004 | 10/43 (HCT15, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Cytarabine (drug)]] 0.05 µM |  | **0.743×** | -3.8 | 0.005 | 8/44 (CHP-212, SNU-423, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.592×** | -3.8 | 0.005 | 9/40 (SW 900, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.600×** | -3.7 | 0.006 | 11/31 (HEC-1-A, SW480, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13611. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 15.0 | 1 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.80× (z +13.7) | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -16.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.259× (z -9.2) |
| [[A-172 (line)]] | wt | 5.76 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.15× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -9.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Hydroxyurea (drug)]] 0.05 µM 0.108× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 12.6 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -15.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.154× (z -11.3) |
| [[A498 (line)]] | wt | 6.64 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.72× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -11.2) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HOP62 (line)]] | alt | 3.34 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.62× (z +8.5) | [[Monocrotaline (drug)]] 0.05 µM 0.0866× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 6.48 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.63× (z +10.3) | [[Temsirolimus (drug)]] 0.5 µM 0.188× (z -9.3) |
| [[SW1417 (line)]] | alt | 5.10 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.88× (z +11.7) | [[Talc (drug)]] 0.5 µM 0.0537× (z -11.6) |
| [[A549 (line)]] | wt | 6.31 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.87× (z +10.0) | — |
| [[C-33 A (line)]] | alt | 18.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.110× (z -10.1) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 2.70 | 0 | 1 | — | [[Darinaparsin (drug)]] 0.5 µM 0.0523× (z -9.2) |
| [[H4 (line)]] | wt | 8.25 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.52× (z +8.5) | — |
| [[HT-29 (line)]] | alt | 7.22 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.13× (z +8.9) | — |
| [[LoVo (line)]] | wt | 6.32 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.09× (z +9.1) | — |
| [[LOX-IMVI (line)]] | wt | 3.88 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.95× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 13.1 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.156× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 7.06 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.29× (z +8.6) | — |
| [[SHP-77 (line)]] | alt | 8.17 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.104× (z -9.2) |
| [[SNU-423 (line)]] | alt | 2.32 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.1× (z +9.1) | — |
| [[SW480 (line)]] | alt | 6.14 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.04× (z +10.8) | — |
| [[A-427 (line)]] | wt | 7.36 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.89 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.83 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.62 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.23 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13611), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNRF2P2]] | +0.71 | +0.69 / +0.64 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[SPESP1]] | +0.70 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[DPY19L1P1]] | +0.65 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[FKBP14-AS1]] | +0.64 | +0.46 / +0.63 | both halves | 3e-05 |  |
| [[H3-3A-DT]] | +0.64 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[DARS1-AS1]] | +0.63 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[SEC24B-AS1]] | +0.62 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[ING2-DT]] | +0.62 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[SAP30L-AS1]] | +0.60 | +0.57 / +0.39 | both halves | 5e-05 |  |
| [[DICER1-AS1]] | +0.60 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[ZBTB44]] | +0.60 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[PSMD6-AS2]] | +0.60 | +0.54 / +0.46 | both halves | 2e-05 |  |
| [[ZNF460-AS1]] | +0.59 | +0.55 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPF1]] | -0.55 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[DNAJB1]] | -0.53 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[NUDT12]] | -0.51 | -0.29 / -0.50 | both halves | 2e-04 |  |
| [[RAB3GAP2]] | -0.51 | -0.37 / -0.51 | both halves | 9e-05 |  |
| [[ALAS1]] | -0.51 | -0.36 / -0.41 | both halves | 9e-05 |  |
| [[DRG2]] | -0.50 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[SLC39A3]] | -0.49 | -0.32 / -0.40 | both halves | 2e-04 |  |
| [[KIF3B]] | -0.49 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[MOCS2]] | -0.49 | -0.32 / -0.41 | both halves | 2e-04 |  |
| [[THOP1]] | -0.49 | -0.22 / -0.51 | both halves | 6e-04 |  |
| [[BCKDK]] | -0.49 | -0.28 / -0.43 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DPY19L2P3's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[INHA]] | B | INHA activity raises DPY19L2P3's level | lines that do not express INHA (11) vs lines expressing it (39) | 1.43× lower at baseline in the lines without INHA | 0.056 | ⚠ within organs, on part of the lines; also absent: OBSL1, KCNK13 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.683). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (2.3, 21.8); signed map (16.9, -4.5). **Vector** length 77.5, 13.7% of its response variance represented; |z| ≥ 3 in 995 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.4 | +28.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +6.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.2 | +1.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.2 | +2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.2 | +0.5 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.2 | +2.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.1 | +1.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.0 | +1.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.5 | -9.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.5 | -7.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -3.3 | -5.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -3.1 | -6.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | -2.4 | -2.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.3 | -4.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.1 | -3.8 |
|  | [[EX229 (drug)]] 5 µM |  | -2.0 | -4.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.8 | -3.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.8 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | DPY19L2 pseudogene 3 |
| Locus type | pseudogene |
| Location | 7p14.3 — chr7:29,650,227-29,742,594 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:22367](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22367) · Entrez [442524](https://www.ncbi.nlm.nih.gov/gene/442524) · Ensembl [ENSG00000227855](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000227855)

## Data

Gene col 13611: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13611); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13611, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13611]; `tensor/DDL_lfc|DDL_z.npy` [13611]; `embed/gene_vectors.npy` [13611]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13611 or target_col == 13611). Every well: [[DPY19L2P3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DPY19L2P3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
