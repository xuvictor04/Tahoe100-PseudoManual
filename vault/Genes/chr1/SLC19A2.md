---
symbol: "SLC19A2"
type: "gene"
col: 3914
ensembl_id: "ENSG00000117479"
name: "solute carrier family 19 member 2"
location: "1q24.2"
module: 106
arm: "+"
pooled_cpm: 31.48
n_lines_expressing: 49
n_dd_up: 30
n_dd_down: 10
n_dd_up_clean: 22
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/106"]
generated_by: "tahoemap"
---

# SLC19A2

*solute carrier family 19 member 2* — 1q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.06× (z +12.4, q 9e-33, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.506× (z -8.0, q 9e-13, down in 24 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Megestrol (drug)]] 0.05 µM: 0.749× (z -3.4, q 0.073, down in 18 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHPT1]] (+0.58, fdr 1e-05), [[UGP2]] (+0.56, fdr 2e-05), [[TSC22D3]] (+0.54, fdr 1e-05); moves opposite to [[TLR6]] (-0.55, fdr 1e-05), [[GPR39]] (-0.54, fdr 1e-05), [[BACH1]] (-0.53, fdr 1e-05).
> It is in [[Module 106]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ADGRG2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3914.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.06×** | +12.4 | 9e-33 | 41/47 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.48×** | +11.0 | 1e-25 | 42/47 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.22×** | +9.7 | 7e-20 | 38/45 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.09×** | +8.6 | 1e-15 | 34/44 (SK-MEL-2, LS 180, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.58×** | +7.8 | 7e-13 | 29/46 (AsPC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.88×** | +7.7 | 2e-12 | 35/46 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.90×** | +7.5 | 5e-12 | 33/47 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.85×** | +7.5 | 5e-12 | 32/47 (A-427, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.85×** | +7.5 | 5e-12 | 35/46 (AsPC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.83×** | +7.3 | 2e-11 | 38/46 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.78×** | +6.7 | 9e-10 | 34/44 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.56×** | +5.4 | 3e-06 | 30/47 (AsPC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +5.1 | 1e-05 | 26/44 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.31×** | +4.7 | 1e-04 | 22/47 (Panc 03.27, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Budesonide (drug)]] 0.05 µM |  | **1.50×** | +4.4 | 5e-04 | 19/46 (H4, NCI-H460, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.98×** | +4.3 | 5e-04 | 24/48 (NCI-H1792, HepG2/C3A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.90×** | +4.1 | 0.002 | 21/44 (C32, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.44×** | +3.9 | 0.003 | 21/47 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.38×** | +3.9 | 0.003 | 21/47 (NCI-H1573, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3914.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.506×** | -8.0 | 9e-13 | 24/35 (SHP-77, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.549×** | -7.3 | 1e-10 | 28/41 (J82, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.700×** | -4.2 | 0.005 | 23/44 (SW1417, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.708×** | -3.9 | 0.015 | 18/37 (SW1417, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Megestrol (drug)]] 0.05 µM |  | **0.749×** | -3.4 | 0.073 | 18/47 (NCI-H2347, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.753×** | -3.4 | 0.073 | 14/47 (A-172, SW1417, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | **0.828×** | -3.3 | 0.080 | 15/47 (Hs 766T, SW48, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | **0.765×** | -3.3 | 0.080 | 11/47 (A-172, NCI-H1573, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.767×** | -3.2 | 0.080 | 12/47 (Panc 03.27, NCI-H460, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.767×** | -3.1 | 0.097 | 16/47 (NCI-H460, Panc 03.27, …) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 0.773× | -3.0 | 0.12 | 13/47 (A-172, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3914. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 19.9 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.79× (z +14.3) | — |
| [[NCI-H460 (line)]] | wt | 25.7 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +10.0) | — |
| [[KATO III (line)]] | alt | 22.7 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.54× (z +10.1) | — |
| [[H4 (line)]] | wt | 34.6 | 4 | 0 | [[Triamcinolone (drug)]] 5 µM 4.59× (z +9.9) | — |
| [[HT-29 (line)]] | alt | 40.2 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.21× (z +12.8) | — |
| [[SW1417 (line)]] | alt | 36.1 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.45× (z +8.9) | [[Docetaxel (drug)]] 0.05 µM 0.226× (z -10.5) ⚠ transcription drop |
| [[COLO 205 (line)]] | alt | 24.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +11.2) | — |
| [[LS 180 (line)]] | wt | 25.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +9.8) | — |
| [[NCI-H1573 (line)]] | alt | 32.4 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.02× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.177× (z -11.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 29.1 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.62× (z +11.2) | — |
| [[A-172 (line)]] | wt | 15.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.37× (z +11.1) | [[Dinaciclib (drug)]] 0.05 µM 0.127× (z -8.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 40.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -9.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 20.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +12.5) | — |
| [[HOP62 (line)]] | alt | 25.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.76× (z +11.5) | — |
| [[J82 (line)]] | alt | 29.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -10.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 11.5 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.110× (z -10.1) ⚠ transcription drop · without an alert: [[Riluzole hydrochloride (drug)]] 0.5 µM 0.147× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 50.4 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.38× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.156× (z -12.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 32.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +11.1) | — |
| [[SHP-77 (line)]] | alt | 80.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0902× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.393× (z -9.3) |
| [[C32 (line)]] | wt | 35.1 | 0 | 1 | — | [[OTS514 (drug)]] 5 µM 0.0528× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 39.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +11.0) | — |
| [[HEC-1-A (line)]] | alt | 16.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +8.9) | — |
| [[Hs 766T (line)]] | wt | 26.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -8.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 48.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.241× (z -9.6) |
| [[RKO (line)]] | wt | 43.6 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0963× (z -8.9) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 31.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.109× (z -10.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 32.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.197× (z -8.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 76.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +9.2) | — |
| [[SW48 (line)]] | wt | 23.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -9.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 20.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.231× (z -12.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 86.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.47 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 77.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3914), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHPT1]] | +0.58 | +0.55 / +0.64 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[UGP2]] | +0.56 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[TSC22D3]] | +0.54 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[ACSL1]] | +0.54 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[TMEM131L]] | +0.54 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[FLVCR2]] | +0.54 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[CRLS1]] | +0.54 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[DCN]] | +0.54 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[PHKA1]] | +0.53 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[TLR2]] | +0.52 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[ATP1B3]] | +0.51 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[DNER]] | +0.51 | +0.42 / +0.54 | both halves | 4e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLR6]] | -0.55 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[GPR39]] | -0.54 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[BACH1]] | -0.53 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[ZNF518B]] | -0.51 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[DCBLD2]] | -0.51 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[ANAPC1P4]] | -0.50 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[ZKSCAN2]] | -0.50 | -0.49 / -0.37 | both halves | 8e-05 |  |
| [[NAV3]] | -0.49 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[PTHLH]] | -0.49 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[RANBP6]] | -0.49 | -0.45 / -0.37 | both halves | 8e-05 |  |
| [[IL11]] | -0.49 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[CFAP299]] | -0.48 | -0.43 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADGRG2]] | B | ADGRG2 activity lowers SLC19A2's level | lines that do not express ADGRG2 (10) vs lines expressing it (40) | 1.37× higher at baseline in the lines without ADGRG2 | 0.036 | ⚠ within organs, on part of the lines; also absent: KCNN3, SLC17A7, STARD8; maybe low, not absent |
| [[SYTL5]] | B | SYTL5 activity raises SLC19A2's level | lines that do not express SYTL5 (20) vs lines expressing it (30) | 1.43× lower at baseline in the lines without SYTL5 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: GBP4, LINC00589, ENSG00000227400 |
| [[SYTL5]] | B | SYTL5 activity strengthens SLC19A2's drug response | lines that do not express SYTL5 (19) vs lines expressing it (28) | the lines without SYTL5 respond 0.66× as strongly (z diff +1.32); strongest at Homoharringtonine 5 µM: 1.28x vs 1.74x (z diff +2.4) | 0.069 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: GBP4, LINC00589, ENSG00000227400; target measured in part of the lines; artifact flags |
| [[NR3C1]] | B | NR3C1 activity raises SLC19A2's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[AGT]] | B | AGT activity raises SLC19A2's level | lines that do not express AGT (33) vs lines expressing it (17) | 1.48× lower at baseline in the lines without AGT | 0.080 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: AMBP, RIT2, SOX11 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 106]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.513). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.9, 14.9); signed map (15.8, 29.6). **Vector** length 105, 31.3% of its response variance represented; |z| ≥ 3 in 1,309 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +12.4 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +5.1 | +4.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +7.5 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +4.7 | +3.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +8.6 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +4.6 | +2.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +4.5 | +2.8 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +4.5 | +2.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.1 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.6 | -2.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | +2.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.4 | +3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | +0.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.7 | -2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.0 | +0.4 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | -1.9 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 19 member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q24.2 — chr1:169,463,909-169,485,944 (-) |
| Ensembl biotype | protein_coding |
| Also known as | THTR1, ThT1; previously TRMA |
| Gene groups (HGNC) | Solute carrier family 19 |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY, P53_PATHWAY |
| Reactome | 3 pathways, smallest: Vitamin B1 (thiamin) metabolism; Metabolism of water-soluble vitamins and cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [O60779](https://www.uniprot.org/uniprotkb/O60779) (Thiamine transporter 1):

> High-affinity transporter for the intake of thiamine. Mediates H(+)-dependent pyridoxine transport.

**Summary**, from NCBI Gene [10560](https://www.ncbi.nlm.nih.gov/gene/10560):

> This gene encodes the thiamin transporter protein. Mutations in this gene cause thiamin-responsive megaloblastic anemia syndrome (TRMA), which is an autosomal recessive disorder characterized by diabetes mellitus, megaloblastic anemia and sensorineural deafness. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Feb 2016]

**Accessions** — [HGNC:10938](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10938) · Entrez [10560](https://www.ncbi.nlm.nih.gov/gene/10560) · UniProt [O60779](https://www.uniprot.org/uniprotkb/O60779) · Ensembl [ENSG00000117479](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117479)

## Data

Gene col 3914: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3914); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3914, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3914]; `tensor/DDL_lfc|DDL_z.npy` [3914]; `embed/gene_vectors.npy` [3914]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3914 or target_col == 3914). Every well: [[SLC19A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC19A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
