---
symbol: "GPR137B"
type: "gene"
col: 1194
ensembl_id: "ENSG00000077585"
name: "G protein-coupled receptor 137B"
location: "1q42.3"
module: 110
arm: "+"
pooled_cpm: 43.97
n_lines_expressing: 47
n_dd_up: 24
n_dd_down: 17
n_dd_up_clean: 20
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/110"]
generated_by: "tahoemap"
---

# GPR137B

*G protein-coupled receptor 137B* — 1q42.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.64× (z +25.4, q 0e+00, up in 36 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.868× (z -9.0, q 1e-16, down in 10 of 46 measured lines) ⚠ position not correctable. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.565× (z -5.5, q 6e-06, down in 25 of 42 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GBX1]] (+0.58, fdr 1e-05), [[BEX4]] (+0.53, fdr 3e-05), [[RUNDC3B]] (+0.53, fdr 1e-04); moves opposite to [[TADA2A]] (-0.47, fdr 5e-05), [[ARMC8]] (-0.45, fdr 2e-04), [[PSMA3]] (-0.44, fdr 5e-05).
> It is in [[Module 110]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[DOCK11]] → it (grade B ⚠); 2 go from it, the strongest it → [[ERO1B]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1194.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.64×** | +25.4 | 0e+00 | 36/44 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.33×** | +15.7 | 0e+00 | 41/44 (SW480, A-427, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +10.2 | 5e-22 | 33/43 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +9.7 | 6e-20 | 28/45 (SW1417, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.66×** | +9.4 | 9e-19 | 32/45 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +9.2 | 4e-18 | 30/45 (PANC-1, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.57×** | +8.3 | 6e-15 | 28/45 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.53×** | +7.9 | 1e-13 | 27/45 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.49×** | +7.4 | 1e-11 | 31/44 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.43×** | +6.7 | 1e-09 | 27/44 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.43×** | +6.7 | 1e-09 | 27/44 (PANC-1, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.45×** | +6.6 | 2e-09 | 26/44 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +6.5 | 3e-09 | 25/44 (SW1417, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.40×** | +6.3 | 1e-08 | 30/45 (PANC-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.72×** | +5.3 | 5e-06 | 21/45 (AsPC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.26×** | +4.4 | 5e-04 | 18/44 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1194.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.868× | -9.0 | 1e-16 | 10/46 (HOP62, NCI-H23, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.696×** | -6.5 | 3e-08 | 21/38 (J82, C-33 A, …) | rises with dose | composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.565×** | -5.5 | 6e-06 | 25/42 (NCI-H2347, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.752×** | -5.3 | 2e-05 | 24/43 (A-427, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.758×** | -5.1 | 4e-05 | 24/44 (HT-29, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.746×** | -5.0 | 5e-05 | 21/43 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.730×** | -4.9 | 6e-05 | 22/44 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.767×** | -4.9 | 6e-05 | 22/44 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.776×** | -4.6 | 2e-04 | 21/46 (NCI-H460, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.821×** | -4.3 | 8e-04 | 12/45 (NCI-H460, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.651×** | -4.2 | 0.002 | 16/42 (NCI-H1792, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.803×** | -3.9 | 0.005 | 18/44 (NCI-H23, MIA PaCa-2, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.848× | -3.7 | 0.009 | 17/45 (HOP62, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.857× | -3.7 | 0.009 | 12/45 (HOP62, C32, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~5% of this change | **0.819×** | -3.5 | 0.015 | 17/43 (RKO, MIA PaCa-2, …) | top dose only |  |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.879× | -3.4 | 0.026 | 11/45 (RKO, NCI-H460, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.708×** | -3.3 | 0.028 | 14/42 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | 0.886× | -3.1 | 0.047 | 13/45 (NCI-H661, SW 900, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.844× | -3.1 | 0.047 | 13/44 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.844× | -3.1 | 0.047 | 12/45 (NCI-H460, NCI-H2347, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1194. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 60.8 | 12 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +32.6) | — |
| [[SW480 (line)]] | alt | 48.4 | 12 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.28× (z +31.1) | — |
| [[BT-474 (line)]] | alt | 41.7 | 7 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.34× (z +12.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.32× (z +11.1) | — |
| [[PANC-1 (line)]] | alt | 30.5 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +16.9) | — |
| [[AsPC-1 (line)]] | alt | 19.9 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.41× (z +13.6) | — |
| [[SW 900 (line)]] | alt | 64.6 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.36× (z +21.6) | [[Dinaciclib (drug)]] 5 µM 0.158× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SW1417 (line)]] | alt | 42.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +22.5) | — |
| [[A-427 (line)]] | wt | 60.5 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.40× (z +14.7) | [[Dinaciclib (drug)]] 0.5 µM 0.269× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[C32 (line)]] | wt | 153 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.86× (z +29.9) | — |
| [[HOP62 (line)]] | alt | 76.9 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +10.3) | [[Adagrasib (drug)]] 0.05 µM 0.636× (z -12.9) ⚠ position not correctable · without an alert: [[Binimetinib (drug)]] 0.05 µM 0.431× (z -8.6) |
| [[LoVo (line)]] | wt | 33.3 | 3 | 0 | [[Auranofin (drug)]] 5 µM 3.36× (z +11.6) | — |
| [[NCI-H1573 (line)]] | alt | 16.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +19.6) | [[Dinaciclib (drug)]] 0.05 µM 0.136× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 52.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +21.5) | — |
| [[SW48 (line)]] | wt | 110 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.07× (z +22.3) | — |
| [[C-33 A (line)]] | alt | 107 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.416× (z -9.6) |
| [[COLO 205 (line)]] | alt | 49.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.46× (z +17.8) | — |
| [[H4 (line)]] | wt | 19.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.18× (z +10.4) | — |
| [[HCT15 (line)]] | alt | 38.3 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.64× (z +11.3) | — |
| [[J82 (line)]] | alt | 37.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +14.4) | [[Dinaciclib (drug)]] 5 µM 0.0323× (z -25.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[LOX-IMVI (line)]] | wt | 16.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.38× (z +12.9) | — |
| [[NCI-H2347 (line)]] | alt | 44.4 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.78× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.265× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SNU-1 (line)]] | wt | 70.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.203× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A-172 (line)]] | wt | 38.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +13.1) | — |
| [[A549 (line)]] | wt | 31.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +11.7) | — |
| [[CFPAC-1 (line)]] | alt | 16.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.34× (z +18.7) | — |
| [[HEC-1-A (line)]] | alt | 36.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.46× (z +12.5) | — |
| [[Hs 766T (line)]] | wt | 24.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.88× (z +15.1) | — |
| [[HT-29 (line)]] | alt | 30.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.58× (z +9.9) | — |
| [[LS 180 (line)]] | wt | 33.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +11.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 76.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[NCI-H23 (line)]] | alt | 25.6 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.589× (z -10.9) ⚠ position not correctable |
| [[Panc 03.27 (line)]] | alt | 38.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.270× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 68.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +10.3) | — |
| [[SHP-77 (line)]] | alt | 40.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.02× (z +13.4) | — |
| [[SNU-423 (line)]] | alt | 96.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[A498 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 76.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.95 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 37.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.77 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.50 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1194), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GBX1]] | +0.58 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[BEX4]] | +0.53 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[RUNDC3B]] | +0.53 | +0.36 / +0.58 | both halves | 1e-04 |  |
| [[MOAP1]] | +0.52 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[TLE2]] | +0.50 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[CDKN1C]] | +0.50 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[ATG2A]] | +0.49 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[STX10]] | +0.49 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[ACP7]] | +0.48 | +0.37 / +0.51 | both halves | 7e-05 |  |
| [[ITGA7]] | +0.48 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[MBP]] | +0.48 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[INSR]] | +0.48 | +0.44 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TADA2A]] | -0.47 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[ARMC8]] | -0.45 | -0.30 / -0.50 | both halves | 2e-04 |  |
| [[PSMA3]] | -0.44 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[PDHA1]] | -0.44 | -0.36 / -0.49 | both halves | 1e-04 |  |
| [[NUP205]] | -0.43 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[MRPL3]] | -0.43 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[EXOSC10]] | -0.43 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[HNRNPR]] | -0.43 | -0.44 / -0.36 | both halves | 9e-05 |  |
| [[SIL1]] | -0.42 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[DLAT]] | -0.42 | -0.46 / -0.37 | both halves | 9e-05 |  |
| [[DROSHA]] | -0.42 | -0.38 / -0.41 | both halves | 7e-05 |  |
| [[LTV1]] | -0.42 | -0.33 / -0.42 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DOCK11]] | B | DOCK11 activity raises GPR137B's level | lines that do not express DOCK11 (13) vs lines expressing it (37) | 1.89× lower at baseline in the lines without DOCK11 | 0.005 | ⚠ within organs, on part of the lines; also absent: KIF26A, HOXD8, ABCA17P; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises GPR137B's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, TAK-733, Trametinib) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[ERO1B]] | C | ERO1B activity raises GPR137B's level | lines that do not express ERO1B (3) vs lines expressing it (47) | 3.22× lower at baseline in the lines without ERO1B | 0.067 | ⚠ few lines (3 vs 47); across organs; also absent: ARHGEF26, ZNF483, RUNDC3A-AS1; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ERO1B]] | C | GPR137B activity raises ERO1B's level | lines that do not express GPR137B (3) vs lines expressing it (47) | 4.41× lower at baseline in the lines without GPR137B | 0.004 | ⚠ few lines (3 vs 47); across organs; also absent: CRYBG3, ERO1B, TEX14; maybe low, not absent; co-absent with the target |
| [[WDR26]] | C | GPR137B activity raises WDR26's level | lines that do not express GPR137B (3) vs lines expressing it (47) | 1.78× lower at baseline in the lines without GPR137B | 0.020 | ⚠ few lines (3 vs 47); across organs; also absent: CRYBG3, ERO1B, TEX14; maybe low, not absent |

## Where it sits

- **Module**: [[Module 110]]; 43 genes; every member is in the + arm (projection on the module's main direction 0.333). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.7, 20.2); signed map (0.5, 27.3). **Vector** length 110, 29.1% of its response variance represented; |z| ≥ 3 in 1,144 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +11.4 | +15.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.3 | +9.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.2 | +6.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.8 | +25.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +4.4 | -6.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | +3.4 | +3.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.9 | +0.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.8 | +1.8 |
| fall | [[TAK-733 (drug)]] 5 µM |  | -4.7 | -5.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.4 | -4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -4.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.9 | -5.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.5 | -9.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.3 | -4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -1.7 |
|  | [[EX229 (drug)]] 5 µM |  | -3.2 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | G protein-coupled receptor 137B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.3 — chr1:236,142,505-236,221,865 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously TM7SF1 |
| Gene groups (HGNC) | 7TM uncharacterized proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [O60478](https://www.uniprot.org/uniprotkb/O60478) (Integral membrane protein GPR137B):

> Lysosomal integral membrane protein that regulates the localization and activity of mTORC1, a signaling complex promoting cell growth in response to growth factors, energy levels, and amino acids. Interacts with Rag GTPases and increases the lysosomal localization and activity of Rag GTPases and thereby regulates mTORC1 translocation and activity in lysosome. Involved in the regulation of lysosomal morphology and autophagy.; Also acts as a negative regulator of osteoclast activity (By …

**Summary**, from NCBI Gene [7107](https://www.ncbi.nlm.nih.gov/gene/7107):

> Involved in positive regulation of TORC1 signaling; positive regulation of protein localization to lysosome; and regulation of autophagy. Located in lysosomal membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:11862](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11862) · Entrez [7107](https://www.ncbi.nlm.nih.gov/gene/7107) · UniProt [O60478](https://www.uniprot.org/uniprotkb/O60478) · Ensembl [ENSG00000077585](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000077585)

## Data

Gene col 1194: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1194); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1194, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1194]; `tensor/DDL_lfc|DDL_z.npy` [1194]; `embed/gene_vectors.npy` [1194]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1194 or target_col == 1194). Every well: [[GPR137B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPR137B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
