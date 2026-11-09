---
symbol: "IMPACT"
type: "gene"
col: 7764
ensembl_id: "ENSG00000154059"
name: "impact RWD domain protein"
location: "18q11.2"
module: 1
arm: "+"
pooled_cpm: 21.41
n_lines_expressing: 48
n_dd_up: 12
n_dd_down: 18
n_dd_up_clean: 7
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# IMPACT

*impact RWD domain protein* — 18q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.06× (z +19.0, q 0e+00, up in 39 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.20× (z +4.3, q 0.003, up in 12 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.410× (z -15.1, q 0e+00, down in 42 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DCAF17]] (+0.77, fdr 7e-06), [[GUF1]] (+0.75, fdr 7e-06), [[RIOX2]] (+0.72, fdr 7e-06); moves opposite to [[UBL5]] (-0.66, fdr 1e-05), [[MARK4]] (-0.65, fdr 1e-05), [[COX6A1]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FAR2P1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7764.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.06×** | +19.0 | 0e+00 | 39/40 (HEC-1-A, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.71×** | +16.3 | 0e+00 | 27/31 (NCI-H1792, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.93×** | +10.3 | 2e-22 | 33/39 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.20×** | +4.3 | 0.003 | 12/46 (SK-MEL-2, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.24×** | +3.7 | 0.023 | 18/46 (A-427, NCI-H2030, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.23×** | +3.5 | 0.044 | 18/45 (A-427, CFPAC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.24×** | +3.4 | 0.044 | 13/45 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~21% of this change | **1.22×** | +3.4 | 0.044 | 14/43 (AsPC-1, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.22×** | +3.4 | 0.044 | 12/45 (NCI-H1573, HOP62, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.46×** | +3.3 | 0.050 | 7/44 (LS 180, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[AZD-7648 (drug)]] 5 µM |  | **1.46×** | +3.3 | 0.053 | 6/41 (NCI-H1792, C32, …) | rises with dose | noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.05 µM |  | **1.21×** | +3.1 | 0.083 | 5/45 (HCT15, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7764.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.410×** | -15.1 | 0e+00 | 42/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.461×** | -13.1 | 1e-36 | 39/45 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.534×** | -10.6 | 6e-24 | 40/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.569×** | -9.5 | 3e-19 | 34/45 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.695×** | -6.1 | 1e-07 | 24/46 (A-427, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.780×** | -5.8 | 6e-07 | 24/45 (SK-MEL-2, SNU-1, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.715×** | -5.7 | 1e-06 | 25/46 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.720×** | -5.5 | 2e-06 | 22/46 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.552×** | -5.2 | 1e-05 | 21/43 (PANC-1, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.759×** | -4.6 | 2e-04 | 18/45 (HS-578T, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.752×** | -4.5 | 3e-04 | 18/45 (HEC-1-A, hTERT-HPNE, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.603×** | -4.4 | 5e-04 | 18/46 (A-427, SNU-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.773×** | -4.3 | 6e-04 | 16/45 (C-33 A, NCI-H23, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.797×** | -3.8 | 0.005 | 16/45 (PANC-1, SW480, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.665×** | -3.5 | 0.015 | 17/43 (Hs 766T, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.816×** | -3.4 | 0.020 | 14/46 (PANC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cepharanthine (drug)]] 5 µM |  | 0.871× | -3.2 | 0.048 | 11/46 (NCI-H661, HT-29, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7764. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 35.9 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +9.8) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.166× (z -17.9) |
| [[SW480 (line)]] | alt | 25.5 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.52× (z +8.5) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.194× (z -15.6) |
| [[HEC-1-A (line)]] | alt | 26.0 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.89× (z +15.0) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.376× (z -9.3) |
| [[LS 180 (line)]] | wt | 25.1 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +10.5) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 0.5 µM 0.278× (z -10.0) |
| [[A-427 (line)]] | wt | 53.0 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 0.5 µM 2.58× (z +10.3) ⚠ cell-cycle shift, explains ~22% of this change | [[TAK-901 (drug)]] 5 µM 0.161× (z -10.2) |
| [[HS-578T (line)]] | alt | 24.5 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +9.0) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.209× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.258× (z -10.4) |
| [[LoVo (line)]] | wt | 26.2 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +10.6) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.312× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 40.0 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +9.8) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.365× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 31.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.63× (z +14.2) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 22.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.87× (z +9.3) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 17.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.28× (z +11.0) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 20.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.169× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.176× (z -10.8) |
| [[CFPAC-1 (line)]] | alt | 13.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.84× (z +10.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 30.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.66× (z +13.5) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 28.2 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.264× (z -11.3) |
| [[NCI-H2347 (line)]] | alt | 19.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.19× (z +11.9) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 13.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.82× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 14.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.287× (z -8.5) |
| [[J82 (line)]] | alt | 18.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.212× (z -10.3) |
| [[NCI-H2030 (line)]] | alt | 12.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.164× (z -11.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 23.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -11.9) |
| [[SNU-1 (line)]] | wt | 29.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -8.8) |
| [[SW1417 (line)]] | alt | 16.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.197× (z -10.6) |
| [[A-172 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.22 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7764), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCAF17]] | +0.77 | +0.76 / +0.66 | both halves | 7e-06 |  |
| [[GUF1]] | +0.75 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[RIOX2]] | +0.72 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[PEX1]] | +0.70 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[TMA16]] | +0.69 | +0.76 / +0.53 | both halves | 1e-05 |  |
| [[FKTN]] | +0.69 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[N6AMT1]] | +0.69 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[DPH5]] | +0.68 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[FARSB]] | +0.67 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[ATIC]] | +0.67 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[GMFB]] | +0.67 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[LARS1]] | +0.67 | +0.67 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBL5]] | -0.66 | -0.72 / -0.49 | both halves | 1e-05 |  |
| [[MARK4]] | -0.65 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[COX6A1]] | -0.63 | -0.69 / -0.53 | both halves | 1e-05 |  |
| [[PRKD2]] | -0.60 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[TRIM62]] | -0.60 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[RNF122]] | -0.60 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[GNB2]] | -0.60 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[NDUFA2]] | -0.59 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[ZNHIT1]] | -0.58 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[NARF]] | -0.58 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[UBA52]] | -0.58 | -0.52 / -0.52 | both halves | 1e-05 | pathway: Cellular response to starvation |
| [[TESK2]] | -0.57 | -0.39 / -0.58 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAR2P1]] | B | FAR2P1 activity raises IMPACT's level | lines that do not express FAR2P1 (29) vs lines expressing it (21) | 1.34× lower at baseline in the lines without FAR2P1 | 0.099 | ⚠ within organs, on part of the lines; co-absent genes; also absent: POTEE, ENSG00000264660, ENSG00000286329 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.697). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-30.5, -16.6); signed map (-0.3, -38.3). **Vector** length 83.1, 17.3% of its response variance represented; |z| ≥ 3 in 922 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +19.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +16.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +4.8 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +3.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +1.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +3.4 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.6 | +1.4 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.6 | +3.3 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.1 | -13.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -5.0 | -15.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.0 | -9.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.4 | -10.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.9 | -5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -4.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.2 | -3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.9 | -2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | -0.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -1.5 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | impact RWD domain protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q11.2 — chr18:24,426,634-24,453,531 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RWDD5 |
| Gene groups (HGNC) | RWD domain containing |
| Reactome | 4 pathways, smallest: Response of EIF2AK4 (GCN2) to amino acid deficiency; Cellular response to starvation; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2X3](https://www.uniprot.org/uniprotkb/Q9P2X3) (Protein IMPACT):

> Translational regulator that ensures constant high levels of translation upon a variety of stress conditions, such as amino acid starvation, UV-C irradiation, proteasome inhibitor treatment and glucose deprivation. Plays a role as a negative regulator of the EIF2AK4/GCN2 kinase activity; impairs GCN1-mediated EIF2AK4/GCN2 activation, and hence EIF2AK4/GCN2-mediated eIF-2-alpha phosphorylation and subsequent down-regulation of protein synthesis. May be required to regulate translation in …

**Summary**, from NCBI Gene [55364](https://www.ncbi.nlm.nih.gov/gene/55364):

> Predicted to enable protein sequestering activity. Predicted to be involved in several processes, including GCN2-mediated signaling; cellular response to amino acid starvation; and regulation of gene expression. Predicted to act upstream of or within negative regulation of protein phosphorylation. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20387](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20387) · Entrez [55364](https://www.ncbi.nlm.nih.gov/gene/55364) · UniProt [Q9P2X3](https://www.uniprot.org/uniprotkb/Q9P2X3) · Ensembl [ENSG00000154059](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154059)

## Data

Gene col 7764: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7764); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7764, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7764]; `tensor/DDL_lfc|DDL_z.npy` [7764]; `embed/gene_vectors.npy` [7764]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7764 or target_col == 7764). Every well: [[IMPACT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IMPACT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
