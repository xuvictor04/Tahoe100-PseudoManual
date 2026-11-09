---
symbol: "RAB8B"
type: "gene"
col: 9239
ensembl_id: "ENSG00000166128"
name: "RAB8B, member RAS oncogene family"
location: "15q22.2"
module: 99
arm: "+"
pooled_cpm: 107.39
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 15
n_dd_up_clean: 10
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# RAB8B

*RAB8B, member RAS oncogene family* — 15q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 1.46× (z +5.8, q 4e-06, up in 35 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.365× (z -14.8, q 0e+00, down in 37 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.652× (z -6.5, q 1e-08, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPR160]] (+0.72, fdr 7e-06), [[PPP1R2]] (+0.69, fdr 7e-06), [[ANKRD37]] (+0.69, fdr 1e-05); moves opposite to [[MCM3AP]] (-0.71, fdr 7e-06), [[DNAJC11]] (-0.67, fdr 7e-06), [[UTP20]] (-0.65, fdr 1e-05).
> It is in [[Module 099]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CLEC2B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, none with an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9239.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +5.8 | 4e-06 | 35/49 (HOP62, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.38×** | +5.0 | 2e-04 | 33/48 (LoVo, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +4.9 | 2e-04 | 27/48 (Panc 03.27, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.33×** | +4.3 | 0.002 | 27/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.71×** | +4.3 | 0.002 | 27/48 (C32, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.30×** | +4.0 | 0.006 | 24/48 (PANC-1, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.64×** | +4.0 | 0.006 | 27/49 (RPMI-7951, Hs 766T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.28×** | +3.7 | 0.016 | 25/49 (NCI-H1792, SNU-423, …) | top dose only | plate-row cell shift |
| [[Fumaric acid (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.017 | 25/49 (NCI-H2030, A-172, …) | rises with dose | plate-row cell shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.049 | 21/48 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Hexylresorcinol (drug)]] 5 µM |  | 1.16× | +3.2 | 0.078 | 8/49 (A-427, SW 900, …) | top dose only |  |
| [[Terfenadine (drug)]] 5 µM |  | 1.16× | +3.1 | 0.078 | 14/48 (NCI-H2030, A-427, …) | rises with dose |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.23× | +3.0 | 0.10 | 23/48 (HS-578T, SW 900, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9239.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.365×** | -14.8 | 0e+00 | 37/41 (NCI-H1792, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.431×** | -12.9 | 2e-35 | 46/49 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.497×** | -9.9 | 1e-20 | 36/44 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.652×** | -6.5 | 1e-08 | 41/48 (HEC-1-A, MIA PaCa-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.696×** | -5.3 | 1e-05 | 27/47 (HepG2/C3A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.825×** | -4.1 | 0.003 | 31/48 (CFPAC-1, A549, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.774×** | -3.9 | 0.007 | 27/48 (SK-MEL-2, NCI-H1792, …) | two highest doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.937× | -3.6 | 0.021 | 0/50 | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.792×** | -3.6 | 0.022 | 26/48 (Panc 03.27, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.793×** | -3.5 | 0.022 | 26/49 (SW480, AsPC-1, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.800×** | -3.3 | 0.053 | 22/48 (NCI-H2347, LOX-IMVI, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.811×** | -3.2 | 0.066 | 18/49 (J82, LS 180, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.813×** | -3.2 | 0.070 | 20/49 (LOX-IMVI, SW480, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.815×** | -3.1 | 0.074 | 17/48 (HOP62, HEC-1-A, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.818×** | -3.1 | 0.084 | 18/48 (A498, AsPC-1, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.820×** | -3.0 | 0.090 | 19/48 (LS 180, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9239. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 312 | 2 | 4 (4 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.17× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.153× (z -17.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 57.8 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +10.4) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.24× (z +8.8) | — |
| [[LOX-IMVI (line)]] | wt | 229 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -13.7) ⚠ cell-cycle shift, explains ~20% of this change |
| [[NCI-H2347 (line)]] | alt | 91.2 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -16.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 175 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.308× (z -12.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 144 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -12.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 217 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -14.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 298 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.158× (z -19.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 116 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.273× (z -12.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 113 | 1 | 2 (2 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.87× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -16.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 216 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -14.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 150 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -9.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 88.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.250× (z -10.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 170 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -13.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 80.4 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.202× (z -13.6) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 109 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.249× (z -10.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 124 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -10.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 153 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.232× (z -14.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 55.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.264× (z -10.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 195 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -13.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 131 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.271× (z -10.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 65.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -12.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 135 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.361× (z -9.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 173 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.290× (z -11.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 55.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.446× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 76.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.378× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 46.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.374× (z -8.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 65.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.21× (z +10.4) | — |
| [[SHP-77 (line)]] | alt | 68.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.339× (z -9.7) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 120 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.156× (z -8.6) |
| [[A-427 (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 105 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 91.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 84.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 62.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 114 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 67.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 49.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 49.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9239), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPR160]] | +0.72 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[PPP1R2]] | +0.69 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[ANKRD37]] | +0.69 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[MXI1]] | +0.68 | +0.73 / +0.57 | both halves | 1e-05 |  |
| [[HDAC3]] | +0.67 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[ARL3]] | +0.67 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[INSIG2]] | +0.66 | +0.71 / +0.49 | both halves | 1e-05 |  |
| [[FHIP1A]] | +0.65 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[HILPDA]] | +0.65 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[KDM3A]] | +0.65 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[RYBP]] | +0.65 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[TSPAN33]] | +0.64 | +0.47 / +0.51 | both halves | 2e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCM3AP]] | -0.71 | -0.66 / -0.64 | both halves | 7e-06 |  |
| [[DNAJC11]] | -0.67 | -0.68 / -0.60 | both halves | 7e-06 |  |
| [[UTP20]] | -0.65 | -0.67 / -0.53 | both halves | 1e-05 |  |
| [[REXO1]] | -0.65 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[GNL3L]] | -0.64 | -0.61 / -0.60 | both halves | 7e-06 |  |
| [[HECTD1]] | -0.62 | -0.58 / -0.58 | both halves | 8e-06 |  |
| [[ABCE1]] | -0.62 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[AGAP6]] | -0.62 | -0.61 / -0.63 | both halves | 7e-06 |  |
| [[ANAPC7]] | -0.61 | -0.67 / -0.51 | both halves | 1e-05 |  |
| [[DNAJB12]] | -0.61 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[ST7L]] | -0.60 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[FEM1A]] | -0.60 | -0.65 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLEC2B]] | B | CLEC2B activity raises RAB8B's level | lines that do not express CLEC2B (22) vs lines expressing it (28) | 2.03× lower at baseline in the lines without CLEC2B | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, TMEM158, FRMD4A |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction 0.669). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.4, -11.9); signed map (-32.4, 22.2). **Vector** length 124, 39.4% of its response variance represented; |z| ≥ 3 in 1,100 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.7 | +4.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.4 | +5.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.4 | +5.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.5 | +4.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.2 | +3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.7 | +2.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.2 | +2.7 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +2.6 | +3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.4 | +0.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -5.7 | -1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.6 | -6.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -2.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | +0.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.3 | -0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -1.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.0 | -0.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.8 | -2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.7 | +4.3 |

## What is on record

|  |  |
|---|---|
| Name | RAB8B, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.2 — chr15:63,189,560-63,267,776 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Reactome | 6 pathways, smallest: TBC/RABGAPs; RAB geranylgeranylation; RAB GEFs exchange GTP for GDP on RABs |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92930](https://www.uniprot.org/uniprotkb/Q92930) (Ras-related protein Rab-8B):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different sets of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion (By similarity). RAB8B may be involved in polarized vesicular trafficking and neurotransmitter release (Probable). May …

**Summary**, from NCBI Gene [51762](https://www.ncbi.nlm.nih.gov/gene/51762):

> RAB proteins, like RAB8B, are low molecular mass monomeric GTPases that localize on the cytoplasmic surfaces of distinct membrane-bound organelles. RAB proteins function in intracellular vesicle transport by aiding in the docking and/or fusion of vesicles with their target membranes (summary by Chen et al., 1997 [PubMed 9030196]).[supplied by OMIM, Nov 2010]

**Accessions** — [HGNC:30273](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30273) · Entrez [51762](https://www.ncbi.nlm.nih.gov/gene/51762) · UniProt [Q92930](https://www.uniprot.org/uniprotkb/Q92930) · Ensembl [ENSG00000166128](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166128)

## Data

Gene col 9239: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9239); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9239, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9239]; `tensor/DDL_lfc|DDL_z.npy` [9239]; `embed/gene_vectors.npy` [9239]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9239 or target_col == 9239). Every well: [[RAB8B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB8B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
