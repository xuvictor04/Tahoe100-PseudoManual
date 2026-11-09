---
symbol: "NOD1"
type: "gene"
col: 2723
ensembl_id: "ENSG00000106100"
name: "nucleotide binding oligomerization domain containing 1"
location: "7p14.3"
module: 146
arm: "+"
pooled_cpm: 25.86
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 30
n_dd_up_clean: 5
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/146"]
generated_by: "tahoemap"
---

# NOD1

*nucleotide binding oligomerization domain containing 1* — 7p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Radotinib (drug)]] 5 µM: 1.23× (z +5.8, q 4e-06, up in 23 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.279× (z -35.2, q 0e+00, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TADA1]] (+0.67, fdr 1e-05), [[ZFP64]] (+0.63, fdr 7e-06), [[EEF2K]] (+0.60, fdr 1e-05); moves opposite to [[TUG1]] (-0.55, fdr 1e-05), [[LINC00641]] (-0.55, fdr 1e-05), [[PRKAR1A]] (-0.55, fdr 4e-05).
> It sits in the **+** arm of [[Module 146]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2723.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Radotinib (drug)]] 5 µM |  | **1.23×** | +5.8 | 4e-06 | 23/48 (AsPC-1, A498, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +4.8 | 4e-04 | 16/48 (RKO, AsPC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.23×** | +4.0 | 0.010 | 11/48 (PANC-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.15× | +3.8 | 0.020 | 13/48 (SNU-1, NCI-H1792, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.023 | 17/47 (BT-474, AsPC-1, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.16× | +3.6 | 0.026 | 11/48 (AsPC-1, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 1.18× | +3.6 | 0.026 | 14/48 (AsPC-1, SW1417, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.20× | +3.6 | 0.026 | 13/48 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.20×** | +3.5 | 0.033 | 8/47 (CFPAC-1, J82, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.19× | +3.2 | 0.071 | 9/48 (AsPC-1, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.12× | +3.2 | 0.071 | 5/48 (AsPC-1, HT-29, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.098 | 11/47 (AsPC-1, HS-578T, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.13× | +3.0 | 0.10 | 8/48 (AsPC-1, HS-578T, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2723.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.279×** | -35.2 | 0e+00 | 45/47 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.244×** | -26.5 | 0e+00 | 44/48 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.318×** | -22.3 | 0e+00 | 46/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.341×** | -21.0 | 0e+00 | 42/47 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.378×** | -17.5 | 0e+00 | 35/38 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.435×** | -16.2 | 0e+00 | 39/46 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.452×** | -15.5 | 0e+00 | 41/48 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.456×** | -15.3 | 0e+00 | 34/43 (HEC-1-A, A498, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.460×** | -15.1 | 0e+00 | 42/48 (MIA PaCa-2, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.449×** | -15.0 | 0e+00 | 32/35 (MIA PaCa-2, A-172, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.584×** | -14.8 | 0e+00 | 36/47 (Panc 03.27, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.492×** | -13.8 | 9e-42 | 37/48 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.513×** | -13.0 | 5e-37 | 42/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.540×** | -12.0 | 1e-31 | 41/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.318×** | -11.7 | 6e-30 | 38/48 (PANC-1, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.630×** | -9.0 | 8e-18 | 27/48 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.629×** | -8.7 | 1e-16 | 31/47 (SK-MEL-2, A-172, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.743×** | -8.2 | 9e-15 | 29/48 (A498, HS-578T, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.668×** | -7.6 | 1e-12 | 26/48 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~19% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2723. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 27.7 | 0 | 17 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0333× (z -30.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.182× (z -23.3) |
| [[PANC-1 (line)]] | alt | 23.6 | 0 | 14 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -28.7) |
| [[A-172 (line)]] | wt | 32.3 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0986× (z -27.1) |
| [[MIA PaCa-2 (line)]] | alt | 34.8 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -23.4) |
| [[SW480 (line)]] | alt | 29.8 | 0 | 11 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.119× (z -21.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.237× (z -15.6) |
| [[HEC-1-A (line)]] | alt | 45.9 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -20.4) |
| [[A498 (line)]] | wt | 40.0 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -28.3) |
| [[A549 (line)]] | wt | 23.7 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0634× (z -26.2) |
| [[AsPC-1 (line)]] | alt | 30.8 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -19.5) |
| [[Hs 766T (line)]] | wt | 36.3 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -14.9) |
| [[SNU-423 (line)]] | alt | 20.6 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -14.4) |
| [[NCI-H2030 (line)]] | alt | 25.0 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -19.2) |
| [[Panc 03.27 (line)]] | alt | 30.3 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -16.7) |
| [[SK-MEL-2 (line)]] | alt | 33.1 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.142× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.189× (z -12.3) |
| [[SW1417 (line)]] | alt | 36.8 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -15.9) |
| [[LoVo (line)]] | wt | 24.9 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -18.1) |
| [[H4 (line)]] | wt | 41.9 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0807× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.217× (z -12.3) |
| [[HOP62 (line)]] | alt | 18.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -15.5) |
| [[HS-578T (line)]] | alt | 25.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -19.2) |
| [[J82 (line)]] | alt | 19.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -16.0) |
| [[KATO III (line)]] | alt | 23.8 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.177× (z -12.1) |
| [[LOX-IMVI (line)]] | wt | 21.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -13.4) |
| [[NCI-H1792 (line)]] | alt | 24.8 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0881× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.292× (z -11.5) |
| [[SW48 (line)]] | wt | 32.0 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0964× (z -13.7) |
| [[C32 (line)]] | wt | 19.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.214× (z -9.4) |
| [[RKO (line)]] | wt | 17.7 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.143× (z -10.7) |
| [[RPMI-7951 (line)]] | alt | 30.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -10.1) |
| [[CFPAC-1 (line)]] | alt | 14.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.138× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.369× (z -8.9) |
| [[LS 180 (line)]] | wt | 18.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -10.8) |
| [[NCI-H1573 (line)]] | alt | 10.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -10.9) |
| [[SHP-77 (line)]] | alt | 38.7 | 0 | 2 (1 ⚠) | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.251× (z -10.5) |
| [[AN3 CA (line)]] | alt | 40.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.109× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[BT-474 (line)]] | alt | 33.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HCT15 (line)]] | alt | 25.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -16.4) |
| [[HT-29 (line)]] | alt | 16.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -11.9) |
| [[hTERT-HPNE (line)]] | wt | 15.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0964× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 17.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -17.8) |
| [[NCI-H2347 (line)]] | alt | 20.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -12.1) |
| [[SNU-1 (line)]] | wt | 22.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.155× (z -9.0) |
| [[SW 1088 (line)]] | alt | 42.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -8.8) |
| [[A-427 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2723), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TADA1]] | +0.67 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[ZFP64]] | +0.63 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[EEF2K]] | +0.60 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[PRMT7]] | +0.59 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[OTX1]] | +0.57 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[PCGF6]] | +0.57 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[SYBU]] | +0.57 | +0.59 / +0.40 | both halves | 5e-05 |  |
| [[MRPL34]] | +0.56 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[GATA4]] | +0.56 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[CCZ1]] | +0.55 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[FHIP2A]] | +0.55 | +0.61 / +0.46 | both halves | 2e-05 |  |
| [[LSM11]] | +0.55 | +0.43 / +0.58 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUG1]] | -0.55 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[LINC00641]] | -0.55 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[PRKAR1A]] | -0.55 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[CHMP1B]] | -0.53 | -0.62 / -0.38 | both halves | 7e-05 |  |
| [[MFSD4B]] | -0.53 | -0.59 / -0.34 | both halves | 1e-04 |  |
| [[ENSA]] | -0.51 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[ZNF655]] | -0.50 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[DDX5]] | -0.50 | -0.56 / -0.40 | both halves | 5e-05 | pathway: SARS-CoV-2 Infection |
| [[TSPAN31]] | -0.50 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[CCDC200]] | -0.50 | -0.38 / -0.56 | both halves | 7e-05 |  |
| [[DAB1]] | -0.49 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[HCG17]] | -0.49 | -0.53 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises NOD1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 146]]; 31 genes; this gene is in the **+** arm (projection on the module's main direction 0.677). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-6.6, -6.9); signed map (-28.3, -12.8). **Vector** length 83.6, 20.8% of its response variance represented; |z| ≥ 3 in 1,272 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Radotinib (drug)]] 5 µM |  | +5.2 | +5.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +5.2 | +4.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.6 | -0.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +4.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.3 | -0.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.6 | +1.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.1 | +3.6 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +2.1 | +3.5 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.8 | -17.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -6.6 | -15.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -5.9 | -15.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.2 | -8.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.3 | -35.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.3 | -2.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.0 | -0.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.9 | -1.5 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.8 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | nucleotide binding oligomerization domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.3 — chr7:30,424,527-30,478,784 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NLRC1, CLR7.1; previously CARD4 |
| Gene groups (HGNC) | NLR family; Caspase recruitment domain containing |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING, INTERFERON_GAMMA_RESPONSE |
| Reactome | 35 pathways, smallest: JNK (c-Jun kinases) phosphorylation and  activation mediated by activated human TAK1; activated TAK1 mediates p38 MAPK activation; NOD1/2 Signaling Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y239](https://www.uniprot.org/uniprotkb/Q9Y239) (Nucleotide-binding oligomerization domain-containing protein 1):

> Pattern recognition receptor (PRR) that detects bacterial peptidoglycan fragments and other danger signals and thus participates in both innate and adaptive immune responses. Specifically recognizes and binds gamma-D-glutamyl-meso-diaminopimelic acid (iE-DAP), a dipeptide present in peptidoglycan of Gram-negative bacteria. Preferentially binds iE-DAP in tripeptide-containing muropeptides (MurNAc-TriDAP or TriDAP). Ligand binding triggers oligomerization that facilitates the binding and …

**Summary**, from NCBI Gene [10392](https://www.ncbi.nlm.nih.gov/gene/10392):

> This gene encodes a member of the nucleotide-binding oligomerization domain (NOD)-like receptor (NLR) family of proteins. The encoded protein plays a role in innate immunity by acting as a pattern-recognition receptor (PRR) that binds bacterial peptidoglycans and initiates inflammation. This protein has also been implicated in the immune response to viral and parasitic infection. Major structural features of this protein include an N-terminal caspase recruitment domain (CARD), a centrally …

**Accessions** — [HGNC:16390](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16390) · Entrez [10392](https://www.ncbi.nlm.nih.gov/gene/10392) · UniProt [Q9Y239](https://www.uniprot.org/uniprotkb/Q9Y239) · Ensembl [ENSG00000106100](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106100)

## Data

Gene col 2723: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2723); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2723, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2723]; `tensor/DDL_lfc|DDL_z.npy` [2723]; `embed/gene_vectors.npy` [2723]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2723 or target_col == 2723). Every well: [[NOD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
