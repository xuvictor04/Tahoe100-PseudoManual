---
symbol: "BBOX1-AS1"
type: "gene"
col: 14882
ensembl_id: "ENSG00000254560"
name: "BBOX1 antisense RNA 1"
location: "11p14.2-p14.1"
module: 10
arm: "+"
pooled_cpm: 26.33
n_lines_expressing: 29
n_dd_up: 33
n_dd_down: 18
n_dd_up_clean: 25
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 7
direction_downstream: 4
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# BBOX1-AS1

*BBOX1 antisense RNA 1* — 11p14.2-p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 13.2× (z +34.1, q 0e+00, up in 17 of 24 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Trametinib (drug)]] 0.5 µM: 1.55× (z +6.8, q 2e-09, up in 15 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.484× (z -9.6, q 4e-19, down in 22 of 26 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Betamethasone dipropionate (drug)]] 0.05 µM: 0.631× (z -5.6, q 2e-06, down in 10 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNGT1]] (+0.66, fdr 7e-06), [[ZSCAN30]] (+0.63, fdr 3e-05), [[RIPK2-DT]] (+0.62, fdr 1e-05); moves opposite to [[MT1A]] (-0.59, fdr 1e-05), [[MT1X]] (-0.59, fdr 1e-05), [[TBC1D8]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[LINC00649]] → it (grade B ⚠); 4 go from it, the strongest it → [[LINC00649]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14882.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **13.2×** | +34.1 | 0e+00 | 17/24 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **13.1×** | +32.7 | 0e+00 | 13/18 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **8.76×** | +26.5 | 0e+00 | 18/21 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.55×** | +6.8 | 2e-09 | 15/27 (NCI-H460, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.63×** | +6.2 | 6e-08 | 17/26 (SW480, NCI-H460, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +6.0 | 2e-07 | 7/26 (LoVo, SK-MEL-2, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM |  | **1.49×** | +5.5 | 4e-06 | 16/27 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +5.4 | 4e-06 | 6/27 (HepG2/C3A, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.53×** | +5.3 | 7e-06 | 8/26 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.16×** | +5.3 | 8e-06 | 3/14 (HEC-1-A, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.47×** | +5.2 | 8e-06 | 13/27 (NCI-H460, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +4.8 | 8e-05 | 6/27 (LoVo, HepG2/C3A, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +4.8 | 8e-05 | 3/25 (RKO, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.41×** | +4.6 | 2e-04 | 16/26 (KATO III, AsPC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.93×** | +4.5 | 3e-04 | 8/21 (SW480, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.40×** | +4.4 | 3e-04 | 10/26 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.41×** | +4.3 | 5e-04 | 14/26 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.3 | 5e-04 | 8/27 (A498, SW480, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.37×** | +4.1 | 0.001 | 17/26 (SW480, NCI-H460, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.29×** | +4.0 | 0.002 | 13/27 (SW480, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.37×** | +3.9 | 0.002 | 9/27 (SW480, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14882.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.484×** | -9.6 | 4e-19 | 22/26 (Hs 766T, J82, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.573×** | -7.4 | 5e-11 | 24/26 (MIA PaCa-2, Hs 766T, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.585×** | -7.1 | 2e-10 | 22/26 (COLO 205, SW480, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.621×** | -6.3 | 4e-08 | 21/26 (NCI-H1792, Hs 766T, …) | two highest doses |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.631×** | -5.6 | 2e-06 | 10/26 (Hs 766T, HepG2/C3A, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.663×** | -5.5 | 5e-06 | 18/26 (SK-MEL-2, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.671×** | -5.3 | 1e-05 | 21/26 (COLO 205, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.689×** | -4.9 | 6e-05 | 20/26 (MIA PaCa-2, Hs 766T, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.502×** | -4.7 | 1e-04 | 16/26 (MIA PaCa-2, NCI-H1792, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.712×** | -4.5 | 4e-04 | 12/26 (Hs 766T, J82, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.736×** | -4.1 | 0.003 | 7/26 (Hs 766T, H4, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.560×** | -4.0 | 0.003 | 14/26 (SW480, H4, …) | top dose only | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.738×** | -3.9 | 0.005 | 13/26 (Hs 766T, NCI-H460, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.595×** | -3.6 | 0.015 | 13/26 (SHP-77, Hs 766T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.777×** | -3.4 | 0.030 | 9/26 (Hs 766T, H4, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.779×** | -3.3 | 0.031 | 8/26 (Hs 766T, H4, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.790×** | -3.1 | 0.057 | 9/26 (Hs 766T, NCI-H1792, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14882. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 97.2 | 0 | 25 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -17.9) |
| [[MIA PaCa-2 (line)]] | alt | 111 | 0 | 10 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.113× (z -18.3) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -18.1) |
| [[NCI-H1792 (line)]] | alt | 248 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -21.1) |
| [[COLO 205 (line)]] | alt | 44.3 | 0 | 8 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0778× (z -14.9) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.246× (z -11.6) |
| [[SW480 (line)]] | alt | 34.2 | 2 (2 ⚠) | 6 (6 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.37× (z +11.9) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.199× (z -11.9) ⚠ cell-cycle shift, explains ~35% of this change |
| [[A498 (line)]] | wt | 10.7 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 12.4× (z +12.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.0921× (z -16.2) |
| [[HEC-1-A (line)]] | alt | 47.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 14.2× (z +19.9) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 15.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 19.3× (z +10.3) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 50.2 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.178× (z -11.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[LoVo (line)]] | wt | 17.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 30.6× (z +22.9) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 74.8 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.53× (z +10.4) | [[Panobinostat (drug)]] 0.5 µM 0.110× (z -10.7) ⚠ cell-cycle shift, explains ~97% of this change |
| [[AsPC-1 (line)]] | alt | 12.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.00× (z +10.0) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 22.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 17.8× (z +14.0) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 29.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 19.5× (z +10.4) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 17.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 10.6× (z +9.3) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.0711× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[NCI-H460 (line)]] | wt | 64.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +9.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -13.4) |
| [[SNU-423 (line)]] | alt | 7.66 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 16.9× (z +10.8) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 32.6 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.220× (z -8.7) ⚠ cell-cycle shift, explains ~57% of this change |
| [[SHP-77 (line)]] | alt | 54.3 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.249× (z -9.3) ⚠ cell-cycle shift, explains ~97% of this change |
| [[SW 900 (line)]] | alt | 6.71 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 21.8× (z +10.4) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 5.72 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.55 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.74 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.50 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.74 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.65 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.61 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.02 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.52 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.25 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.15 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.76 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.17 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.63 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.25 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.08 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.54 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.43 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.69 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14882), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNGT1]] | +0.66 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[ZSCAN30]] | +0.63 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[RIPK2-DT]] | +0.62 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[SLC44A5]] | +0.62 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[ZSCAN31]] | +0.61 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[MIR325HG]] | +0.59 | +0.69 / +0.40 | both halves | 5e-05 |  |
| [[ABCA13]] | +0.59 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[LINC02542]] | +0.59 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[LINC02466]] | +0.59 | +0.58 / +0.39 | both halves | 6e-05 |  |
| [[CLIC2]] | +0.58 | +0.39 / +0.47 | both halves | 5e-05 |  |
| [[PRECSIT]] | +0.58 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[TTC6]] | +0.58 | +0.50 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MT1A]] | -0.59 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[MT1X]] | -0.59 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[TBC1D8]] | -0.59 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[SKI]] | -0.57 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[FBH1]] | -0.57 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[SH2B2]] | -0.56 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[FANCE]] | -0.56 | -0.37 / -0.51 | both halves | 9e-05 |  |
| [[ZMYND19]] | -0.55 | -0.36 / -0.53 | both halves | 1e-04 |  |
| [[ANKRD13D]] | -0.55 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[MT2A]] | -0.55 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[SOCS7]] | -0.55 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[CCNQ]] | -0.54 | -0.30 / -0.49 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 4, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00649]] | B | LINC00649 activity raises BBOX1-AS1's level | lines that do not express LINC00649 (25) vs lines expressing it (25) | 2.76× lower at baseline in the lines without LINC00649 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000287923, RMST, SERPINF1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers BBOX1-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SLC44A5]] | B | SLC44A5 activity raises BBOX1-AS1's level | lines that do not express SLC44A5 (17) vs lines expressing it (33) | 2.42× lower at baseline in the lines without SLC44A5 | 0.049 | ⚠ within organs, on part of the lines; also absent: ENSG00000289609; maybe low, not absent |
| [[LINC02904]] | B | LINC02904 activity raises BBOX1-AS1's level | lines that do not express LINC02904 (17) vs lines expressing it (33) | 2.29× lower at baseline in the lines without LINC02904 | 0.094 | ⚠ within organs, on part of the lines; also absent: AQP3, B3GALNT1 |
| [[CASC9]] | C | CASC9 activity raises BBOX1-AS1's level | lines that do not express CASC9 (22) vs lines expressing it (28) | 3.25× lower at baseline in the lines without CASC9 | 0.006 | ⚠ within organs, on part of the lines; also absent: MSLN, LINC00857, SLC38A5; co-absent with the target |
| [[GLDN]] | C | GLDN activity raises BBOX1-AS1's level | lines that do not express GLDN (25) vs lines expressing it (25) | 2.70× lower at baseline in the lines without GLDN | 0.025 | ⚠ within organs, on part of the lines; also absent: MIR4713HG, MT1G, ENSG00000255595; co-absent with the target |
| [[PTGIS]] | C | PTGIS activity raises BBOX1-AS1's level | lines that do not express PTGIS (39) vs lines expressing it (11) | 2.35× lower at baseline in the lines without PTGIS | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMRN1, PREX2, GCG; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00649]] | B | BBOX1-AS1 activity raises LINC00649's level | lines that do not express BBOX1-AS1 (21) vs lines expressing it (29) | 2.24× lower at baseline in the lines without BBOX1-AS1 | 0.005 | ⚠ within organs, on part of the lines; also absent: GLDN, CHN2, CPVL; maybe low, not absent |
| [[GLDN]] | C | BBOX1-AS1 activity raises GLDN's level | lines that do not express BBOX1-AS1 (21) vs lines expressing it (29) | 2.66× lower at baseline in the lines without BBOX1-AS1 | 0.003 | ⚠ within organs, on part of the lines; also absent: GLDN, CHN2, CPVL; maybe low, not absent; co-absent with the target |
| [[CASC9]] | C | BBOX1-AS1 activity raises CASC9's level | lines that do not express BBOX1-AS1 (21) vs lines expressing it (29) | 2.52× lower at baseline in the lines without BBOX1-AS1 | 0.035 | ⚠ within organs, on part of the lines; also absent: GLDN, CHN2, CPVL; maybe low, not absent; co-absent with the target |
| [[PTGIS]] | C | BBOX1-AS1 activity raises PTGIS's level | lines that do not express BBOX1-AS1 (21) vs lines expressing it (29) | 1.91× lower at baseline in the lines without BBOX1-AS1 | 0.051 | ⚠ within organs, on part of the lines; also absent: GLDN, CHN2, CPVL; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.491). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (18.2, 18.2); signed map (39.6, 1.1). **Vector** length 86.7, 22.8% of its response variance represented; |z| ≥ 3 in 904 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +10.6 | +26.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.8 | +32.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.0 | +34.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.0 | +3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.9 | +6.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.6 | +6.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.0 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +4.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.7 | +5.2 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -3.4 | -3.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -3.2 | -7.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.8 | -3.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~97% of this change | -2.8 | -2.7 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -2.6 | -2.2 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.4 | -3.4 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.3 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | BBOX1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11p14.2-p14.1 — chr11:27,047,186-27,220,113 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:50700](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:50700) · Entrez [103695435](https://www.ncbi.nlm.nih.gov/gene/103695435) · Ensembl [ENSG00000254560](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000254560)

## Data

Gene col 14882: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14882); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14882, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14882]; `tensor/DDL_lfc|DDL_z.npy` [14882]; `embed/gene_vectors.npy` [14882]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14882 or target_col == 14882). Every well: [[BBOX1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BBOX1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
