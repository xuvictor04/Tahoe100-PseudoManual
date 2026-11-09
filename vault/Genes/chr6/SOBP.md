---
symbol: "SOBP"
type: "gene"
col: 3358
ensembl_id: "ENSG00000112320"
name: "sine oculis binding protein homolog"
location: "6q21"
module: 9
arm: "+"
pooled_cpm: 28.23
n_lines_expressing: 31
n_dd_up: 17
n_dd_down: 11
n_dd_up_clean: 12
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 13
direction_downstream: 25
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# SOBP

*sine oculis binding protein homolog* — 6q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.76× (z +17.1, q 0e+00, up in 13 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.778× (z -7.6, q 2e-11, down in 16 of 29 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDE3B]] (+0.58, fdr 1e-05), [[RUNX1T1]] (+0.57, fdr 3e-05), [[CARD18]] (+0.55, fdr 2e-05); moves opposite to [[PSORS1C1]] (-0.41, fdr 3e-04), [[VPS29]] (-0.41, fdr 1e-04), [[TPD52L2]] (-0.40, fdr 2e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[LEF1]] → it (grade B ⚠); 25 go from it, the strongest it → [[PDE7A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3358.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.76×** | +17.1 | 0e+00 | 13/29 (HEC-1-A, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.95×** | +14.3 | 6e-44 | 16/29 (RKO, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +13.5 | 3e-39 | 13/29 (LoVo, RKO, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.79×** | +12.5 | 1e-33 | 16/29 (NCI-H2030, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.75×** | +12.0 | 3e-31 | 15/28 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.63×** | +10.5 | 7e-24 | 12/28 (RKO, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.54×** | +9.2 | 3e-18 | 8/29 (NCI-H2030, RKO, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **2.08×** | +8.2 | 2e-14 | 11/29 (RKO, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.43×** | +7.6 | 1e-12 | 9/29 (NCI-H2030, NCI-H1792, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.25×** | +6.8 | 7e-10 | 11/29 (SNU-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.33×** | +6.2 | 4e-08 | 8/29 (SNU-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.31×** | +5.8 | 3e-07 | 11/28 (RKO, LoVo, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.22×** | +4.3 | 7e-04 | 6/28 (A-427, MIA PaCa-2, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.22×** | +4.3 | 8e-04 | 8/29 (RKO, NCI-H2030, …) | inconsistent across doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.15× | +4.1 | 0.001 | 5/29 (PANC-1, C32, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.20× | +3.9 | 0.003 | 2/29 (LoVo, A-427) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.40×** | +3.8 | 0.005 | 0/28 | rises with dose | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 0.5 µM |  | 1.17× | +3.4 | 0.018 | 0/28 | two highest doses |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.25×** | +3.4 | 0.020 | 3/29 (HEC-1-A, HepG2/C3A, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3358.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.778×** | -7.6 | 2e-11 | 16/29 (PANC-1, A-427, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.711×** | -7.3 | 1e-10 | 17/28 (SNU-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.741×** | -6.4 | 3e-08 | 18/29 (SW480, C32, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.747×** | -6.2 | 7e-08 | 13/29 (PANC-1, AN3 CA, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.756×** | -6.0 | 3e-07 | 16/26 (NCI-H661, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.766×** | -5.7 | 1e-06 | 13/28 (PANC-1, SHP-77, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.849× | -4.9 | 7e-05 | 17/29 (PANC-1, SHP-77, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.799×** | -4.8 | 1e-04 | 8/29 (NCI-H1792, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.786×** | -4.6 | 3e-04 | 11/28 (PANC-1, LoVo, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.682×** | -4.3 | 0.001 | 10/30 (LOX-IMVI, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.819×** | -4.3 | 0.001 | 13/29 (SK-MEL-2, PANC-1, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.821×** | -4.0 | 0.003 | 8/29 (SK-MEL-2, SW480, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.840× | -3.7 | 0.009 | 7/28 (PANC-1, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~3% of this change | 0.841× | -3.7 | 0.010 | 4/29 (SHP-77, A-427, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | 0.842× | -3.6 | 0.010 | 7/29 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.854× | -3.3 | 0.025 | 2/29 (LOX-IMVI, SW 900) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.855× | -3.3 | 0.028 | 10/28 (PANC-1, C32, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.860× | -3.2 | 0.039 | 6/28 (H4, RKO, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.858× | -3.1 | 0.050 | 7/28 (SK-MEL-2, A549, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3358. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 287 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.152× (z -22.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.348× (z -12.5) |
| [[PANC-1 (line)]] | alt | 96.5 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -12.7) |
| [[AN3 CA (line)]] | alt | 260 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -16.2) |
| [[C-33 A (line)]] | alt | 138 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0305× (z -30.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 58.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 14.3 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.87× (z +9.6) | — |
| [[SNU-1 (line)]] | wt | 71.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +10.6) | [[Digitoxin (drug)]] 5 µM 0.211× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 58.1 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.311× (z -11.9) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A-427 (line)]] | wt | 46.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.196× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[A549 (line)]] | wt | 15.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.31× (z +10.1) | — |
| [[C32 (line)]] | wt | 50.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 7.33 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.20× (z +10.7) | — |
| [[LoVo (line)]] | wt | 11.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.05× (z +12.2) | — |
| [[NCI-H23 (line)]] | alt | 10.4 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.192× (z -8.5) |
| [[NCI-H661 (line)]] | alt | 55.6 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0843× (z -9.0) ⚠ transcription drop |
| [[RKO (line)]] | wt | 39.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +11.2) | — |
| [[SK-MEL-2 (line)]] | alt | 20.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -9.8) |
| [[SW48 (line)]] | wt | 39.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.175× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[A-172 (line)]] | wt | 6.53 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.50 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.07 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.99 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.42 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 86.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.98 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.84 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.40 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 50.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.26 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.76 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.80 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 5.20 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.85 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.47 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.31 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3358), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDE3B]] | +0.58 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[RUNX1T1]] | +0.57 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[CARD18]] | +0.55 | +0.47 / +0.59 | both halves | 2e-05 | **novel candidate** |
| [[SOX2]] | +0.54 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[GPR63]] | +0.53 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[UNC5C]] | +0.52 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[NFIA]] | +0.51 | +0.46 / +0.47 | both halves | 2e-05 |  |
| [[CACHD1]] | +0.51 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[NR2F1]] | +0.50 | +0.43 / +0.43 | both halves | 3e-05 |  |
| [[PRKD1]] | +0.49 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[TSPAN12]] | +0.49 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[COL11A1]] | +0.48 | +0.37 / +0.51 | both halves | 8e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSORS1C1]] | -0.41 | -0.27 / -0.49 | both halves | 3e-04 |  |
| [[VPS29]] | -0.41 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[TPD52L2]] | -0.40 | -0.48 / -0.30 | both halves | 2e-04 |  |
| [[HGS]] | -0.40 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[MKNK1]] | -0.40 | -0.30 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 13, C 0. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LEF1]] | B | LEF1 activity raises SOBP's level | lines that do not express LEF1 (29) vs lines expressing it (21) | 1.73× lower at baseline in the lines without LEF1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF521, LEF1-AS1, LAMA1 |
| [[CARD18]] | B | CARD18 activity raises SOBP's level | lines that do not express CARD18 (44) vs lines expressing it (6) | 6.05× lower at baseline in the lines without CARD18 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000237031, APOB, BMP10 |
| [[SAMD11]] | B | SAMD11 activity raises SOBP's level | lines that do not express SAMD11 (13) vs lines expressing it (37) | 3.79× lower at baseline in the lines without SAMD11 | 0.026 | ⚠ within organs, on part of the lines; also absent: TTC28, B4GALNT1, RASSF8-AS1 |
| [[ADAM22]] | B | ADAM22 activity raises SOBP's level | lines that do not express ADAM22 (12) vs lines expressing it (38) | 3.88× lower at baseline in the lines without ADAM22 | 0.027 | ⚠ within organs, on part of the lines; also absent: ASGR1; maybe low, not absent |
| [[RUNX1T1]] | B | RUNX1T1 activity raises SOBP's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 2.31× lower at baseline in the lines without RUNX1T1 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4 |
| [[PHYHIPL]] | B | PHYHIPL activity raises SOBP's level | lines that do not express PHYHIPL (39) vs lines expressing it (11) | 4.59× lower at baseline in the lines without PHYHIPL | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA |
| [[HGF]] | B | HGF activity raises SOBP's level | lines that do not express HGF (38) vs lines expressing it (12) | 3.04× lower at baseline in the lines without HGF | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SYT4, RIT2, CALCA |
| [[ROBO1]] | B | ROBO1 activity raises SOBP's level | lines that do not express ROBO1 (13) vs lines expressing it (37) | 3.02× lower at baseline in the lines without ROBO1 | 0.053 | ⚠ within organs, on part of the lines; also absent: CRMP1, PEG10, MGAT5B |
| [[LINC02197]] | B | LINC02197 activity raises SOBP's level | lines that do not express LINC02197 (35) vs lines expressing it (15) | 3.06× lower at baseline in the lines without LINC02197 | 0.067 | ⚠ within organs, on part of the lines; also absent: RIT2, SNTG1, CALCA; maybe low, not absent |
| [[CTNNA2]] | B | CTNNA2 activity raises SOBP's level | lines that do not express CTNNA2 (33) vs lines expressing it (17) | 3.32× lower at baseline in the lines without CTNNA2 | 0.067 | ⚠ within organs, on part of the lines; also absent: SRRM4, MAGEA4, KCNH7 |
| [[PSORS1C1]] | B | PSORS1C1 activity lowers SOBP's level | lines that do not express PSORS1C1 (15) vs lines expressing it (35) | 3.24× higher at baseline in the lines without PSORS1C1 | 0.077 | ⚠ within organs, on part of the lines; also absent: IL15, MGLL, SH3TC2 |
| [[FUT9]] | B | FUT9 activity raises SOBP's level | lines that do not express FUT9 (40) vs lines expressing it (10) | 1.61× lower at baseline in the lines without FUT9 | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, KCNH7, GCG |

### Downstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 25, C 0. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDE7A]] | B | SOBP activity raises PDE7A's level | lines that do not express SOBP (19) vs lines expressing it (31) | 1.59× lower at baseline in the lines without SOBP | 0.003 | ⚠ within organs, on part of the lines; also absent: ANK2, TMEM145, SYT11 |
| [[REV3L]] | B | SOBP activity raises REV3L's level | lines that do not express SOBP (19) vs lines expressing it (31) | 2.00× lower at baseline in the lines without SOBP | 0.003 | ⚠ within organs, on part of the lines; also absent: ANK2, TMEM145, SYT11 |
| [[ADAM22]] | B | SOBP activity raises ADAM22's level | lines that do not express SOBP (19) vs lines expressing it (31) | 3.01× lower at baseline in the lines without SOBP | 0.007 | ⚠ within organs, on part of the lines; also absent: ANK2, TMEM145, SYT11 |
| [[REV3L]] | B | SOBP activity strengthens REV3L's drug response | lines that do not express SOBP (19) vs lines expressing it (30) | the lines without SOBP respond 1.00× as strongly (z diff +0.83); strongest at Dinaciclib 5 µM: 0.72x vs 0.44x (z diff +4.2) | 0.016 | ⚠ within organs, on part of the lines; also absent: ANK2, TMEM145, SYT11; target measured in part of the lines; artifact flags |
| [[LINC01013]] | B | SOBP activity raises LINC01013's level | lines that do not express SOBP (19) vs lines expressing it (31) | 2.07× lower at baseline in the lines without SOBP | 0.019 | ⚠ within organs, on part of the lines; also absent: ANK2, TMEM145, SYT11 |
| [[ARID2]] | B | SOBP activity raises ARID2's level | lines that do not express SOBP (19) vs lines expressing it (31) | 1.51× lower at baseline in the lines without SOBP | 0.023 | ⚠ within organs, on part of the lines; also absent: ANK2, TMEM145, SYT11 |
| [[SLC35D1]] | B | SOBP activity raises SLC35D1's level | lines that do not express SOBP (19) vs lines expressing it (31) | 1.56× lower at baseline in the lines without SOBP | 0.041 | ⚠ within organs, on part of the lines; also absent: ANK2, TMEM145, SYT11 |
| [[CACHD1]] | B | SOBP activity raises CACHD1's level | lines that do not express SOBP (19) vs lines expressing it (31) | 2.27× lower at baseline in the lines without SOBP | 0.044 | ⚠ within organs, on part of the lines; also absent: ANK2, TMEM145, SYT11 |
| [[GSE1]] | B | SOBP activity raises GSE1's level | lines that do not express SOBP (19) vs lines expressing it (31) | 1.46× lower at baseline in the lines without SOBP | 0.046 | ⚠ within organs, on part of the lines; also absent: ANK2, TMEM145, SYT11 |
| [[ADGRL1]] | B | SOBP activity raises ADGRL1's level | lines that do not express SOBP (19) vs lines expressing it (31) | 2.14× lower at baseline in the lines without SOBP | 0.046 | ⚠ within organs, on part of the lines; also absent: ANK2, TMEM145, SYT11 |
| [[PCNX1]] | B | SOBP activity raises PCNX1's level | lines that do not express SOBP (19) vs lines expressing it (31) | 1.48× lower at baseline in the lines without SOBP | 0.049 | ⚠ within organs, on part of the lines; also absent: ANK2, TMEM145, SYT11 |
| [[SAMD1]] | B | SOBP activity raises SAMD1's level | lines that do not express SOBP (19) vs lines expressing it (31) | 1.41× lower at baseline in the lines without SOBP | 0.059 | ⚠ within organs, on part of the lines; also absent: ANK2, TMEM145, SYT11 |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.429). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.8, 38.6); signed map (38.0, 34.9). **Vector** length 70.9, 15.6% of its response variance represented; |z| ≥ 3 in 747 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +3.7 | +12.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +13.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.1 | +14.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +17.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +2.9 | -2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +4.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +8.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.9 | +3.8 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -6.4 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~3% of this change | -2.1 | -3.7 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -2.1 | -4.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.0 | -4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | -6.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.8 | -5.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.6 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | sine oculis binding protein homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q21 — chr6:107,490,106-107,661,306 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10159 |
| Gene groups (HGNC) | Zinc fingers MYM-type; Sine oculis binding protein homologs |
| Matched by | ensembl_id |

**Function**, from UniProt [A7XYQ1](https://www.uniprot.org/uniprotkb/A7XYQ1) (Sine oculis-binding protein homolog):

> Implicated in development of the cochlea.

**Summary**, from NCBI Gene [55084](https://www.ncbi.nlm.nih.gov/gene/55084):

> The protein encoded by this gene is a nuclear zinc finger protein that is involved in development of the cochlea. Defects in this gene have also been linked to intellectual disability. [provided by RefSeq, Mar 2011]

**Accessions** — [HGNC:29256](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29256) · Entrez [55084](https://www.ncbi.nlm.nih.gov/gene/55084) · UniProt [A7XYQ1](https://www.uniprot.org/uniprotkb/A7XYQ1) · Ensembl [ENSG00000112320](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112320)

## Data

Gene col 3358: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3358); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3358, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3358]; `tensor/DDL_lfc|DDL_z.npy` [3358]; `embed/gene_vectors.npy` [3358]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3358 or target_col == 3358). Every well: [[SOBP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SOBP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
