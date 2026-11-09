---
symbol: "SH3RF3"
type: "gene"
col: 10325
ensembl_id: "ENSG00000172985"
name: "SH3 domain containing ring finger 3"
location: "2q13"
module: 97
arm: "+"
pooled_cpm: 41.91
n_lines_expressing: 36
n_dd_up: 15
n_dd_down: 33
n_dd_up_clean: 15
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 8
direction_downstream: 6
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# SH3RF3

*SH3 domain containing ring finger 3* — 2q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.46× (z +6.9, q 3e-09, up in 19 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.631× (z -8.4, q 2e-14, down in 22 of 34 measured lines) ⚠ cell-cycle shift, explains ~55% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.549× (z -7.8, q 2e-12, down in 24 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDGFRA]] (+0.70, fdr 8e-06), [[JCAD]] (+0.67, fdr 7e-06), [[ABLIM3]] (+0.67, fdr 7e-06); moves opposite to [[PSG9]] (-0.48, fdr 2e-04), [[SLAMF7]] (-0.46, fdr 7e-05).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[SLC45A1]] → it (grade B ⚠); 6 go from it, the strongest it → [[ZHX3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, none with an alert; shown: the 15 strongest. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10325.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +6.9 | 3e-09 | 19/34 (NCI-H2030, J82, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.63×** | +6.3 | 8e-08 | 19/34 (HOP62, HS-578T, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.51×** | +5.3 | 2e-05 | 17/34 (SW480, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Budesonide (drug)]] 5 µM |  | **1.51×** | +5.3 | 2e-05 | 17/34 (HOP62, HS-578T, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.48×** | +5.1 | 5e-05 | 19/34 (HOP62, HS-578T, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.47×** | +5.0 | 7e-05 | 15/34 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.41×** | +4.5 | 6e-04 | 16/34 (HOP62, HS-578T, …) | all doses, flat | position effect removed |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.38×** | +4.2 | 0.002 | 15/34 (HOP62, HS-578T, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.37×** | +4.1 | 0.003 | 14/34 (HOP62, HS-578T, …) | all doses, flat |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.34×** | +3.7 | 0.010 | 11/34 (HOP62, HS-578T, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.32×** | +3.6 | 0.015 | 13/34 (HOP62, HS-578T, …) | all doses, flat | position effect removed |
| [[Budesonide (drug)]] 0.5 µM |  | **1.32×** | +3.6 | 0.015 | 15/34 (HOP62, HS-578T, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.62×** | +3.3 | 0.042 | 12/34 (SW480, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.042 | 15/34 (HOP62, HS-578T, …) | all doses, flat | position effect removed |
| [[Demeclocycline (drug)]] 5 µM |  | 1.19× | +3.3 | 0.042 | 9/34 (HOP62, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10325.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.631×** | -8.4 | 2e-14 | 22/34 (PANC-1, NCI-H1792, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.525×** | -7.9 | 9e-13 | 19/32 (HOP62, LS 180, …) | two highest doses | cell-cycle shift (explains ~3% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.549×** | -7.8 | 2e-12 | 24/34 (NCI-H23, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.542×** | -7.6 | 3e-12 | 19/33 (C32, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.556×** | -7.6 | 3e-12 | 21/33 (LS 180, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.607×** | -7.3 | 2e-11 | 22/34 (RPMI-7951, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.566×** | -7.0 | 3e-10 | 25/34 (NCI-H1792, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.670×** | -6.3 | 3e-08 | 22/34 (NCI-H1792, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.711×** | -6.2 | 3e-08 | 20/34 (HS-578T, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.610×** | -6.1 | 4e-08 | 21/30 (RPMI-7951, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.635×** | -5.9 | 2e-07 | 20/34 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.643×** | -5.5 | 2e-06 | 19/26 (HOP62, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 5 µM |  | **0.701×** | -5.3 | 4e-06 | 18/34 (Hs 766T, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.462×** | -5.2 | 7e-06 | 21/32 (HOP62, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.671×** | -5.0 | 3e-05 | 18/34 (RPMI-7951, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.755×** | -4.3 | 8e-04 | 19/34 (Hs 766T, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.729×** | -4.1 | 0.001 | 13/34 (HOP62, SW48, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.729×** | -3.9 | 0.003 | 15/33 (Hs 766T, RPMI-7951, …) | rises with dose | position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **0.573×** | -3.8 | 0.005 | 15/32 (Hs 766T, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.814×** | -3.8 | 0.005 | 15/34 (Hs 766T, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.748×** | -3.6 | 0.007 | 19/34 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10325. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 160 | 18 | 7 (4 ⚠) | [[Budesonide (drug)]] 5 µM 6.97× (z +17.0) | [[Dinaciclib (drug)]] 5 µM 0.181× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -12.9) |
| [[HS-578T (line)]] | alt | 84.1 | 15 | 6 (3 ⚠) | [[Dexamethasone (drug)]] 0.5 µM 4.99× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -14.7) |
| [[NCI-H1792 (line)]] | alt | 125 | 10 | 9 (2 ⚠) | [[Dexamethasone (drug)]] 0.5 µM 4.54× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -19.1) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Trametinib (drug)]] 5 µM 0.191× (z -11.9) |
| [[RPMI-7951 (line)]] | alt | 274 | 5 | 12 (5 ⚠) | [[Clobetasol propionate (drug)]] 0.5 µM 3.57× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -17.5) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.180× (z -12.4) |
| [[Hs 766T (line)]] | wt | 90.9 | 0 | 12 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.215× (z -12.0) |
| [[PANC-1 (line)]] | alt | 80.6 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -25.0) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -14.3) |
| [[C32 (line)]] | wt | 56.6 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -18.4) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.105× (z -13.1) |
| [[LS 180 (line)]] | wt | 71.2 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.108× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.189× (z -11.7) |
| [[A-172 (line)]] | wt | 93.3 | 1 | 3 (1 ⚠) | [[Clobetasol propionate (drug)]] 0.05 µM 3.58× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -10.8) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.205× (z -10.3) |
| [[NCI-H23 (line)]] | alt | 31.6 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.168× (z -12.4) |
| [[NCI-H460 (line)]] | wt | 36.1 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.219× (z -11.5) ⚠ cell-cycle shift, explains ~60% of this change |
| [[SW 900 (line)]] | alt | 50.9 | 2 | 1 | [[Dexamethasone (drug)]] 0.5 µM 3.96× (z +9.0) | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.248× (z -8.8) |
| [[C-33 A (line)]] | alt | 58.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -9.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 108 | 2 | 0 | [[Dexamethasone (drug)]] 0.5 µM 5.32× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 15.8 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.92× (z +10.5) | — |
| [[SW48 (line)]] | wt | 48.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -14.3) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.139× (z -10.3) |
| [[SW480 (line)]] | alt | 36.7 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.11× (z +10.7) | — |
| [[A549 (line)]] | wt | 10.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.11× (z +9.3) | — |
| [[BT-474 (line)]] | alt | 15.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 17.0× (z +10.5) | — |
| [[HEC-1-A (line)]] | alt | 10.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 10.7× (z +14.0) | — |
| [[J82 (line)]] | alt | 13.6 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.23× (z +9.3) | — |
| [[RKO (line)]] | wt | 22.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 10.1× (z +12.4) | — |
| [[SW 1088 (line)]] | alt | 144 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.145× (z -9.5) |
| [[SW1417 (line)]] | alt | 15.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.74× (z +10.2) | — |
| [[A-427 (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.04 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.17 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.47 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 69.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.74 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 114 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.76 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 7.07 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.35 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.16 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.38 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.63 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.33 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.81 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.24 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.00 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 25.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10325), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDGFRA]] | +0.70 | +0.58 / +0.74 | both halves | 8e-06 | **novel candidate** |
| [[JCAD]] | +0.67 | +0.67 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[ABLIM3]] | +0.67 | +0.62 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[AKAP12]] | +0.63 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[TOX2]] | +0.63 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[GAB3]] | +0.63 | +0.55 / +0.61 | both halves | 1e-05 | **novel candidate** |
| [[ITGA10]] | +0.62 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[AFAP1L1]] | +0.62 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[FOXL1]] | +0.62 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[PYGB]] | +0.61 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[DNER]] | +0.60 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[DAAM2]] | +0.60 | +0.48 / +0.64 | both halves | 2e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSG9]] | -0.48 | -0.29 / -0.47 | both halves | 2e-04 |  |
| [[SLAMF7]] | -0.46 | -0.38 / -0.46 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC45A1]] | B | SLC45A1 activity raises SH3RF3's level | lines that do not express SLC45A1 (19) vs lines expressing it (31) | 2.89× lower at baseline in the lines without SLC45A1 | 0.023 | ⚠ within organs, on part of the lines; also absent: LRRC34, PNMA2, SSTR2 |
| [[RTN4RL1]] | B | RTN4RL1 activity raises SH3RF3's level | lines that do not express RTN4RL1 (14) vs lines expressing it (36) | 3.19× lower at baseline in the lines without RTN4RL1 | 0.055 | ⚠ within organs, on part of the lines; also absent: EFR3B, B4GALNT1, HS6ST3; maybe low, not absent |
| [[GYPC]] | B | GYPC activity raises SH3RF3's level | lines that do not express GYPC (35) vs lines expressing it (15) | 2.97× lower at baseline in the lines without GYPC | 0.072 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PHACTR1, ANKRD30B, PLPP4 |
| [[PRR16]] | B | PRR16 activity raises SH3RF3's level | lines that do not express PRR16 (24) vs lines expressing it (26) | 2.28× lower at baseline in the lines without PRR16 | 0.084 | ⚠ within organs, on part of the lines; also absent: PCDH10, LINC00839, ZEB2 |
| [[RNF175]] | B | RNF175 activity raises SH3RF3's level | lines that do not express RNF175 (30) vs lines expressing it (20) | 2.77× lower at baseline in the lines without RNF175 | 0.086 | ⚠ within organs, on part of the lines; also absent: SCG2, ENSG00000266450, MIR493HG |
| [[TLR2]] | B | TLR2 activity strengthens SH3RF3's drug response | lines that do not express TLR2 (18) vs lines expressing it (16) | the lines without TLR2 respond 0.73× as strongly (z diff +1.08); strongest at Trametinib 5 µM: 0.76x vs 0.43x (z diff +3.3) | 0.086 | ⚠ within organs, on part of the lines; also absent: FYB1, DDIT4L, EDNRA; target measured in part of the lines; artifact flags |
| [[PLAT]] | B | PLAT activity strengthens SH3RF3's drug response | lines that do not express PLAT (18) vs lines expressing it (16) | the lines without PLAT respond 0.55× as strongly (z diff +1.80); strongest at Trametinib 5 µM: 0.81x vs 0.40x (z diff +4.6) | 0.090 | ⚠ within organs, on part of the lines; also absent: TIMP3, FN1, SNAI2; target measured in part of the lines; artifact flags |
| [[ITPRIP]] | B | ITPRIP activity raises SH3RF3's level | lines that do not express ITPRIP (10) vs lines expressing it (40) | 2.01× lower at baseline in the lines without ITPRIP | 0.093 | ⚠ within organs, on part of the lines; also absent: C13orf46; maybe low, not absent |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZHX3]] | B | SH3RF3 activity raises ZHX3's level | lines that do not express SH3RF3 (14) vs lines expressing it (36) | 1.25× lower at baseline in the lines without SH3RF3 | 0.014 | ⚠ within organs, on part of the lines; also absent: DCLK2, OSBPL6, FHL1 |
| [[IL1RL1]] | B | SH3RF3 activity lowers IL1RL1's level | lines that do not express SH3RF3 (14) vs lines expressing it (36) | 1.45× higher at baseline in the lines without SH3RF3 | 0.019 | ⚠ within organs, on part of the lines; also absent: DCLK2, OSBPL6, FHL1 |
| [[NRG2]] | B | SH3RF3 activity raises NRG2's level | lines that do not express SH3RF3 (14) vs lines expressing it (36) | 2.46× lower at baseline in the lines without SH3RF3 | 0.020 | ⚠ within organs, on part of the lines; also absent: DCLK2, OSBPL6, FHL1 |
| [[EVA1C]] | B | SH3RF3 activity strengthens EVA1C's drug response | lines that do not express SH3RF3 (7) vs lines expressing it (26) | the lines without SH3RF3 respond 0.74× as strongly (z diff +2.09); strongest at Homoharringtonine 0.5 µM: 0.42x vs 0.19x (z diff +4.3) | 0.029 | ⚠ within organs, on part of the lines; also absent: DCLK2, OSBPL6, FHL1; target measured in part of the lines; artifact flags |
| [[SSH1]] | B | SH3RF3 activity raises SSH1's level | lines that do not express SH3RF3 (14) vs lines expressing it (36) | 1.48× lower at baseline in the lines without SH3RF3 | 0.067 | ⚠ within organs, on part of the lines; also absent: DCLK2, OSBPL6, FHL1 |
| [[RCL1]] | B | SH3RF3 activity raises RCL1's level | lines that do not express SH3RF3 (14) vs lines expressing it (36) | 1.06× lower at baseline in the lines without SH3RF3 | 0.076 | ⚠ within organs, on part of the lines; also absent: DCLK2, OSBPL6, FHL1 |

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.665). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.9, 13.5); signed map (16.5, 35.4). **Vector** length 118, 31.9% of its response variance represented; |z| ≥ 3 in 1,242 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.3 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.7 | +6.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.5 | +5.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +5.1 | +5.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.0 | -1.4 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +4.4 | +3.6 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +4.3 | +2.6 |
| fall | [[Trametinib (drug)]] 5 µM |  | -6.5 | -7.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.3 | -7.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.3 | -6.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -5.3 | -3.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -5.1 | -3.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.6 | -5.3 |

## What is on record

|  |  |
|---|---|
| Name | SH3 domain containing ring finger 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q13 — chr2:109,129,205-109,504,634 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ00204, POSH2; previously SH3MD4 |
| Gene groups (HGNC) | Ring finger proteins; SH3 domain containing; SH3 domain containing ring finger family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TEJ3](https://www.uniprot.org/uniprotkb/Q8TEJ3) (E3 ubiquitin-protein ligase SH3RF3):

> Has E3 ubiquitin-protein ligase activity.

**Summary**, from NCBI Gene [344558](https://www.ncbi.nlm.nih.gov/gene/344558):

> Enables ubiquitin protein ligase activity. Involved in positive regulation of JNK cascade and protein autoubiquitination. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24699](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24699) · Entrez [344558](https://www.ncbi.nlm.nih.gov/gene/344558) · UniProt [Q8TEJ3](https://www.uniprot.org/uniprotkb/Q8TEJ3) · Ensembl [ENSG00000172985](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172985)

## Data

Gene col 10325: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10325); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10325, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10325]; `tensor/DDL_lfc|DDL_z.npy` [10325]; `embed/gene_vectors.npy` [10325]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10325 or target_col == 10325). Every well: [[SH3RF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SH3RF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
