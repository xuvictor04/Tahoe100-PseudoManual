---
symbol: "HK1"
type: "gene"
col: 7993
ensembl_id: "ENSG00000156515"
name: "hexokinase 1"
location: "10q22.1"
module: 134
arm: "+"
pooled_cpm: 130.01
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 17
n_dd_up_clean: 6
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/134"]
generated_by: "tahoemap"
---

# HK1

*hexokinase 1* — 10q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.75× (z +11.1, q 1e-25, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.336× (z -30.6, q 0e+00, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFYVE28]] (+0.78, fdr 7e-06), [[MAP2K1]] (+0.74, fdr 7e-06), [[WASF3]] (+0.69, fdr 3e-05); moves opposite to [[NFYC]] (-0.67, fdr 1e-05), [[PMF1]] (-0.65, fdr 3e-05), [[UNK]] (-0.64, fdr 8e-05).
> It is in [[Module 134]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ITPRIP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7993.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.75×** | +11.1 | 1e-25 | 42/47 (SW480, SNU-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.41×** | +6.8 | 3e-09 | 33/47 (SW1417, SNU-423, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.31×** | +5.3 | 2e-05 | 26/47 (SNU-423, A-427, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.30×** | +5.2 | 3e-05 | 24/47 (SW1417, SNU-423, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.24×** | +4.2 | 0.002 | 25/47 (SW1417, LoVo, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.50×** | +4.2 | 0.002 | 28/47 (NCI-H460, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.23×** | +4.2 | 0.002 | 25/47 (NCI-H1573, SW1417, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.22×** | +3.9 | 0.008 | 21/47 (Hs 766T, PANC-1, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.016 | 21/48 (NCI-H1792, HOP62, …) | top dose only | plate-row cell shift |
| [[PF-06260933 (drug)]] 5 µM |  | **1.42×** | +3.6 | 0.016 | 24/47 (SNU-1, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.20× | +3.6 | 0.016 | 21/47 (PANC-1, HT-29, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +3.6 | 0.016 | 16/47 (SNU-423, HEC-1-A, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.18× | +3.2 | 0.059 | 15/46 (NCI-H1573, SK-MEL-2, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.17× | +3.2 | 0.059 | 19/47 (NCI-H1573, A498, …) | rises with dose |  |
| [[EX229 (drug)]] 0.05 µM |  | 1.18× | +3.2 | 0.059 | 16/47 (LoVo, AsPC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.35×** | +3.1 | 0.059 | 18/47 (HS-578T, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.24×** | +3.0 | 0.090 | 14/47 (NCI-H460, AsPC-1, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7993.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.336×** | -30.6 | 0e+00 | 43/47 (LOX-IMVI, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.470×** | -14.9 | 0e+00 | 41/47 (C32, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.491×** | -13.5 | 2e-39 | 41/47 (SK-MEL-2, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.574×** | -10.6 | 6e-24 | 37/46 (C32, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.747×** | -8.1 | 4e-14 | 34/47 (RKO, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.684×** | -7.2 | 5e-11 | 33/47 (NCI-H23, J82, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.723×** | -6.4 | 1e-08 | 32/47 (C32, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.738×** | -5.5 | 2e-06 | 25/44 (SK-MEL-2, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.767×** | -5.2 | 1e-05 | 26/47 (HT-29, J82, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.837× | -5.0 | 4e-05 | 21/47 (J82, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.771×** | -4.9 | 4e-05 | 23/43 (C32, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.776×** | -4.8 | 7e-05 | 26/49 (J82, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.852× | -4.4 | 6e-04 | 18/48 (AsPC-1, C32, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.807×** | -4.1 | 0.002 | 24/46 (C-33 A, C32, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | 0.862× | -4.1 | 0.002 | 19/47 (LS 180, AsPC-1, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.848× | -4.0 | 0.002 | 17/47 (AsPC-1, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.819×** | -3.9 | 0.003 | 21/48 (AsPC-1, C32, …) | all doses, flat |  |
| [[NG25 (drug)]] 5 µM |  | **0.692×** | -3.8 | 0.005 | 24/46 (KATO III, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.831×** | -3.5 | 0.012 | 20/47 (C32, AsPC-1, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7993. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 628 | 0 | 16 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -33.0) |
| [[J82 (line)]] | alt | 136 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -36.1) |
| [[AsPC-1 (line)]] | alt | 104 | 1 | 6 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.32× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -17.6) |
| [[LOX-IMVI (line)]] | wt | 219 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -37.3) |
| [[NCI-H23 (line)]] | alt | 95.0 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -25.4) |
| [[SK-MEL-2 (line)]] | alt | 162 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -33.0) |
| [[BT-474 (line)]] | alt | 171 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -12.1) |
| [[NCI-H460 (line)]] | wt | 88.2 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -21.3) |
| [[RKO (line)]] | wt | 175 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.215× (z -18.0) |
| [[SNU-1 (line)]] | wt | 206 | 1 | 4 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.69× (z +12.4) | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -17.0) |
| [[A549 (line)]] | wt | 83.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -17.7) |
| [[HCT15 (line)]] | alt | 190 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -21.0) |
| [[HOP62 (line)]] | alt | 378 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -25.6) |
| [[HS-578T (line)]] | alt | 150 | 2 (1 ⚠) | 2 | [[PH-797804 (drug)]] 5 µM 4.67× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -20.5) |
| [[LoVo (line)]] | wt | 70.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -20.3) |
| [[MIA PaCa-2 (line)]] | alt | 179 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -28.8) |
| [[NCI-H1573 (line)]] | alt | 99.3 | 1 | 3 | [[Dexamethasone (drug)]] 0.05 µM 2.43× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -24.8) |
| [[Panc 03.27 (line)]] | alt | 84.3 | 1 | 3 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.59× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -12.5) |
| [[SW480 (line)]] | alt | 104 | 1 | 3 | [[Auranofin (drug)]] 5 µM 3.08× (z +12.7) | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -16.5) |
| [[A-172 (line)]] | wt | 217 | 1 | 2 | [[Auranofin (drug)]] 5 µM 2.25× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.526× (z -11.4) |
| [[C-33 A (line)]] | alt | 116 | 0 | 3 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.150× (z -15.9) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.438× (z -10.2) |
| [[hTERT-HPNE (line)]] | wt | 155 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -13.4) |
| [[NCI-H2030 (line)]] | alt | 123 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -31.2) |
| [[NCI-H2347 (line)]] | alt | 93.3 | 1 | 2 | [[Auranofin (drug)]] 5 µM 2.17× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -19.3) |
| [[PANC-1 (line)]] | alt | 114 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -19.3) |
| [[RPMI-7951 (line)]] | alt | 170 | 1 | 2 | [[Auranofin (drug)]] 5 µM 2.35× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -26.4) |
| [[A-427 (line)]] | wt | 43.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.93× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -12.6) |
| [[H4 (line)]] | wt | 148 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -18.7) |
| [[Hs 766T (line)]] | wt | 173 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -23.4) |
| [[HT-29 (line)]] | alt | 109 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -19.2) |
| [[LS 180 (line)]] | wt | 86.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -21.5) |
| [[SNU-423 (line)]] | alt | 42.1 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.17× (z +9.2) | — |
| [[SW 900 (line)]] | alt | 128 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.25× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -11.1) |
| [[SW1417 (line)]] | alt | 55.1 | 1 (1 ⚠) | 1 | [[Panobinostat (drug)]] 0.5 µM 2.44× (z +8.7) ⚠ cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -10.9) |
| [[A498 (line)]] | wt | 89.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +11.6) | — |
| [[AN3 CA (line)]] | alt | 209 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.166× (z -13.9) |
| [[CFPAC-1 (line)]] | alt | 96.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.65× (z +11.0) | — |
| [[KATO III (line)]] | alt | 97.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -13.6) |
| [[NCI-H1792 (line)]] | alt | 157 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -12.9) |
| [[SW 1088 (line)]] | alt | 149 | 0 | 1 | — | [[Irinotecan (hydrochloride) (drug)]] 0.05 µM 0.0669× (z -10.9) |
| [[SW48 (line)]] | wt | 126 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -11.7) |
| [[CHP-212 (line)]] | wt | 88.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 105 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7993), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFYVE28]] | +0.78 | +0.77 / +0.66 | both halves | 7e-06 |  |
| [[MAP2K1]] | +0.74 | +0.78 / +0.64 | both halves | 7e-06 |  |
| [[WASF3]] | +0.69 | +0.69 / +0.43 | both halves | 3e-05 |  |
| [[FLNB]] | +0.67 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[SLC2A3]] | +0.66 | +0.65 / +0.44 | both halves | 3e-05 | pathway: HALLMARK_HYPOXIA; STRING 737 |
| [[SERGEF]] | +0.65 | +0.75 / +0.46 | both halves | 3e-05 |  |
| [[HK2]] | +0.65 | +0.71 / +0.43 | both halves | 3e-05 | same gene group; pathway: HALLMARK_HYPOXIA; STRING 979 |
| [[CHSY1]] | +0.65 | +0.70 / +0.60 | both halves | 7e-06 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |
| [[CSNK1E]] | +0.65 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[FAM210A]] | +0.64 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[DNAJC5]] | +0.63 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[ATRN]] | +0.63 | +0.58 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFYC]] | -0.67 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[PMF1]] | -0.65 | -0.62 / -0.43 | both halves | 3e-05 |  |
| [[UNK]] | -0.64 | -0.67 / -0.37 | both halves | 8e-05 |  |
| [[RC3H2]] | -0.63 | -0.64 / -0.41 | both halves | 4e-05 |  |
| [[CASC9]] | -0.63 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[BAZ2B]] | -0.61 | -0.58 / -0.37 | both halves | 9e-05 |  |
| [[TXNRD2]] | -0.60 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[TIA1]] | -0.60 | -0.65 / -0.37 | both halves | 8e-05 |  |
| [[RNF115]] | -0.59 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[ERCC6L2-AS1]] | -0.59 | -0.67 / -0.22 | both halves | 6e-04 |  |
| [[AHI1-DT]] | -0.58 | -0.64 / -0.19 | ⚠ one half (not replicated) | 8e-04 |  |
| [[TAPBPL]] | -0.58 | -0.57 / -0.34 | both halves | 1e-04 |  |
| [[TBC1D22B]] | -0.58 | -0.43 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITPRIP]] | B | ITPRIP activity raises HK1's level | lines that do not express ITPRIP (10) vs lines expressing it (40) | 1.73× lower at baseline in the lines without ITPRIP | 0.089 | ⚠ within organs, on part of the lines; also absent: C13orf46; maybe low, not absent |
| [[SMAP1]] | C | SMAP1's natural level strengthens HK1's drug response | SMAP1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.32; direction not clear | 0.082 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 134]]; 35 genes; every member is in the + arm (projection on the module's main direction 0.801). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (9.1, -15.0); signed map (-42.1, 23.7). **Vector** length 149, 49.0% of its response variance represented; |z| ≥ 3 in 1,498 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +11.7 | +11.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +10.4 | +6.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +9.6 | +5.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +9.5 | +5.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | +8.4 | +4.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.6 | +2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +3.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.8 | +3.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.4 | +4.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -9.6 | -13.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.5 | -30.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.1 | -14.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.5 | -10.6 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.4 | -8.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.4 | -4.0 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -4.1 | -4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.6 | -3.5 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.5 | -4.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.4 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | hexokinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.1 — chr10:69,269,984-69,401,884 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HKI |
| Gene groups (HGNC) | Hexokinase family |
| Hallmark sets | HYPOXIA |
| Reactome | 9 pathways, smallest: Synthesis of GDP-mannose; Synthesis of substrates in N-glycan biosythesis; Glycolysis |
| Matched by | ensembl_id |

**Function**, from UniProt [P19367](https://www.uniprot.org/uniprotkb/P19367) (Hexokinase-1):

> Catalyzes the phosphorylation of various hexoses, such as D-glucose, D-glucosamine, D-fructose, D-mannose and 2-deoxy-D-glucose, to hexose 6-phosphate (D-glucose 6-phosphate, D-glucosamine 6-phosphate, D-fructose 6-phosphate, D-mannose 6-phosphate and 2-deoxy-D-glucose 6-phosphate, respectively). Does not phosphorylate N-acetyl-D-glucosamine. Mediates the initial step of glycolysis by catalyzing phosphorylation of D-glucose to D-glucose 6-phosphate (By similarity). Involved in innate immunity …

**Summary**, from NCBI Gene [3098](https://www.ncbi.nlm.nih.gov/gene/3098):

> Hexokinases phosphorylate glucose to produce glucose-6-phosphate, the first step in most glucose metabolism pathways. This gene encodes a ubiquitous form of hexokinase which localizes to the outer membrane of mitochondria. Mutations in this gene have been associated with hemolytic anemia due to hexokinase deficiency. Alternative splicing of this gene results in several transcript variants which encode different isoforms, some of which are tissue-specific. [provided by RefSeq, Apr 2016]

**Accessions** — [HGNC:4922](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4922) · Entrez [3098](https://www.ncbi.nlm.nih.gov/gene/3098) · UniProt [P19367](https://www.uniprot.org/uniprotkb/P19367) · Ensembl [ENSG00000156515](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156515)

## Data

Gene col 7993: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7993); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7993, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7993]; `tensor/DDL_lfc|DDL_z.npy` [7993]; `embed/gene_vectors.npy` [7993]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7993 or target_col == 7993). Every well: [[HK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
