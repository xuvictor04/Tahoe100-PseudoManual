---
symbol: "FHIP1A"
type: "gene"
col: 8881
ensembl_id: "ENSG00000164142"
name: "FHF complex subunit HOOK interacting protein 1A"
location: "4q31.3"
module: 99
arm: "+"
pooled_cpm: 237.8
n_lines_expressing: 43
n_dd_up: 4
n_dd_down: 33
n_dd_up_clean: 4
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 14
direction_downstream: 13
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# FHIP1A

*FHF complex subunit HOOK interacting protein 1A* — 4q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 1.94× (z +4.6, q 0.002, up in 29 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.301× (z -16.0, q 0e+00, down in 34 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.450× (z -15.1, q 0e+00, down in 37 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPR160]] (+0.70, fdr 7e-06), [[TEC]] (+0.69, fdr 1e-05), [[PDK3]] (+0.69, fdr 7e-06); moves opposite to [[AVEN]] (-0.66, fdr 2e-05), [[ST7L]] (-0.65, fdr 7e-06), [[REXO1]] (-0.64, fdr 9e-06).
> It is in [[Module 099]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[MPZL3]] → it (grade B ⚠); 13 go from it, the strongest it → [[DLL3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8881.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.94×** | +4.6 | 0.002 | 29/42 (BT-474, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.40×** | +4.4 | 0.004 | 33/42 (NCI-H460, KATO III, …) | top dose only | plate-row cell shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.034 | 17/41 (RKO, A-172, …) | rises with dose |  |
| [[Fumaric acid (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.073 | 25/42 (NCI-H460, CHP-212, …) | top dose only | plate-row cell shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.27× | +3.2 | 0.16 | 19/42 (RKO, C32, …) | rises with dose |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.28× | +3.1 | 0.16 | 23/41 (SW480, KATO III, …) | rises with dose | plate-row cell shift |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 1.42× | +3.0 | 0.21 | 22/41 (SW480, HCT15, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8881.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.301×** | -16.0 | 0e+00 | 34/42 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.290×** | -15.9 | 0e+00 | 35/37 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.450×** | -15.1 | 0e+00 | 37/42 (CFPAC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.532×** | -11.9 | 2e-30 | 30/41 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.415×** | -11.7 | 1e-29 | 35/41 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.411×** | -11.4 | 5e-28 | 36/41 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.464×** | -9.5 | 3e-19 | 32/38 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.491×** | -9.1 | 5e-18 | 36/40 (CFPAC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.516×** | -8.8 | 8e-17 | 37/41 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.504×** | -8.8 | 1e-16 | 37/41 (SNU-423, C32, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.643×** | -8.3 | 4e-15 | 37/41 (MIA PaCa-2, CFPAC-1, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.602×** | -6.5 | 4e-09 | 34/43 (NCI-H2347, CFPAC-1, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.640×** | -5.7 | 5e-07 | 29/41 (CHP-212, RKO, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.661×** | -5.5 | 1e-06 | 30/41 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.768×** | -5.0 | 2e-05 | 33/41 (CFPAC-1, C32, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.703×** | -4.7 | 1e-04 | 29/41 (CFPAC-1, COLO 205, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.730×** | -4.2 | 8e-04 | 25/41 (NCI-H460, NCI-H1792, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.733×** | -4.1 | 9e-04 | 29/41 (A-172, SK-MEL-2, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.737×** | -4.1 | 0.001 | 29/41 (MIA PaCa-2, A-172, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.754×** | -3.8 | 0.004 | 29/41 (A-172, H4, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.756×** | -3.7 | 0.004 | 24/41 (NCI-H1573, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8881. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 950 | 0 | 17 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0761× (z -28.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -25.1) |
| [[Panc 03.27 (line)]] | alt | 370 | 0 | 11 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -23.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -20.8) |
| [[SW480 (line)]] | alt | 269 | 0 | 11 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -19.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.267× (z -17.0) |
| [[BT-474 (line)]] | alt | 328 | 6 (4 ⚠) | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 8.65× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.212× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -13.6) |
| [[NCI-H1573 (line)]] | alt | 628 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -23.3) |
| [[NCI-H1792 (line)]] | alt | 357 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -24.9) |
| [[NCI-H2347 (line)]] | alt | 725 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0984× (z -25.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -23.5) |
| [[Hs 766T (line)]] | wt | 248 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -14.4) |
| [[KATO III (line)]] | alt | 264 | 1 | 7 (3 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.39× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -17.9) |
| [[MIA PaCa-2 (line)]] | alt | 147 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -19.6) |
| [[SNU-423 (line)]] | alt | 360 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -16.7) |
| [[HCT15 (line)]] | alt | 551 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0892× (z -20.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.272× (z -15.3) |
| [[HepG2_C3A (line)]] | wt | 306 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.351× (z -11.5) |
| [[COLO 205 (line)]] | alt | 303 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -17.0) |
| [[SK-MEL-2 (line)]] | alt | 257 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.160× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -11.3) |
| [[SW48 (line)]] | wt | 379 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.353× (z -13.4) |
| [[C32 (line)]] | wt | 155 | 2 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 14.0× (z +12.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -12.5) |
| [[HT-29 (line)]] | alt | 248 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -8.8) |
| [[LoVo (line)]] | wt | 329 | 2 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.22× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.585× (z -9.3) |
| [[LS 180 (line)]] | wt | 448 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -21.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.403× (z -12.6) |
| [[SW1417 (line)]] | alt | 272 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.201× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -15.4) |
| [[HEC-1-A (line)]] | alt | 419 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -15.0) |
| [[RKO (line)]] | wt | 127 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -22.1) |
| [[CHP-212 (line)]] | wt | 141 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.104× (z -11.0) |
| [[HOP62 (line)]] | alt | 183 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.248× (z -9.7) |
| [[SHP-77 (line)]] | alt | 110 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -19.5) |
| [[SW 900 (line)]] | alt | 233 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -11.8) |
| [[A498 (line)]] | wt | 124 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +11.3) | — |
| [[AsPC-1 (line)]] | alt | 65.3 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.312× (z -8.5) |
| [[C-33 A (line)]] | alt | 113 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -10.8) |
| [[H4 (line)]] | wt | 248 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.138× (z -11.3) |
| [[LOX-IMVI (line)]] | wt | 61.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 122 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -12.4) |
| [[A-172 (line)]] | wt | 86.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 108 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 45.1 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 56.1 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 47.9 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 77.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 357 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 44.8 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 76.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 276 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.2 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 22.9 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.3 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 114 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8881), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPR160]] | +0.70 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[TEC]] | +0.69 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[PDK3]] | +0.69 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[TPD52]] | +0.68 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[INSIG2]] | +0.67 | +0.73 / +0.53 | both halves | 1e-05 |  |
| [[MXI1]] | +0.67 | +0.76 / +0.52 | both halves | 1e-05 |  |
| [[ERO1A]] | +0.67 | +0.73 / +0.51 | both halves | 1e-05 |  |
| [[PPP1R2]] | +0.66 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[RAB11FIP1]] | +0.66 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[SLC25A23]] | +0.66 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[RAB8B]] | +0.65 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[SRP54-AS1]] | +0.65 | +0.66 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AVEN]] | -0.66 | -0.71 / -0.46 | both halves | 2e-05 |  |
| [[ST7L]] | -0.65 | -0.68 / -0.59 | both halves | 7e-06 |  |
| [[REXO1]] | -0.64 | -0.57 / -0.60 | both halves | 9e-06 |  |
| [[MCM3AP]] | -0.64 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[E2F3]] | -0.63 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[PRDM5]] | -0.63 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[AGAP6]] | -0.62 | -0.62 / -0.59 | both halves | 7e-06 |  |
| [[CPSF2]] | -0.62 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[ITPA]] | -0.62 | -0.68 / -0.44 | both halves | 3e-05 |  |
| [[FBXO30]] | -0.62 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[NIP7]] | -0.62 | -0.70 / -0.53 | both halves | 1e-05 |  |
| [[ENOX2]] | -0.61 | -0.68 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 12, C 2. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MPZL3]] | B | MPZL3 activity raises FHIP1A's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 3.20× lower at baseline in the lines without MPZL3 | 0.002 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |
| [[IRF6]] | B | IRF6 activity raises FHIP1A's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 3.33× lower at baseline in the lines without IRF6 | 0.002 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[KLHL32]] | B | KLHL32 activity raises FHIP1A's level | lines that do not express KLHL32 (13) vs lines expressing it (37) | 2.86× lower at baseline in the lines without KLHL32 | 0.013 | ⚠ within organs, on part of the lines; also absent: ATP8A1, ENSG00000270265, CHN2; maybe low, not absent |
| [[GPRC5A]] | B | GPRC5A activity raises FHIP1A's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 2.71× lower at baseline in the lines without GPRC5A | 0.017 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[CDA]] | B | CDA activity raises FHIP1A's level | lines that do not express CDA (16) vs lines expressing it (34) | 2.66× lower at baseline in the lines without CDA | 0.031 | ⚠ within organs, on part of the lines; also absent: TMEM92, LASTR, KITLG |
| [[CDS1]] | B | CDS1 activity raises FHIP1A's level | lines that do not express CDS1 (19) vs lines expressing it (31) | 2.46× lower at baseline in the lines without CDS1 | 0.054 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, C6orf132; maybe low, not absent |
| [[DLL3]] | B | DLL3 activity lowers FHIP1A's level | lines that do not express DLL3 (28) vs lines expressing it (22) | 2.01× higher at baseline in the lines without DLL3 | 0.063 | ⚠ within organs, on part of the lines; also absent: LAMC3, FBXO27, INA |
| [[FAR2]] | B | FAR2 activity raises FHIP1A's level | lines that do not express FAR2 (19) vs lines expressing it (31) | 1.48× lower at baseline in the lines without FAR2 | 0.071 | ⚠ within organs, on part of the lines; also absent: CCN3, MIR155HG, LINC02605; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises FHIP1A's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.6% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ATG9B]] | B | ATG9B activity raises FHIP1A's level | lines that do not express ATG9B (20) vs lines expressing it (30) | 2.10× lower at baseline in the lines without ATG9B | 0.073 | ⚠ within organs, on part of the lines; also absent: AFAP1L2, GJB3, EREG |
| [[WNT5B]] | B | WNT5B activity lowers FHIP1A's level | lines that do not express WNT5B (22) vs lines expressing it (28) | 2.14× higher at baseline in the lines without WNT5B | 0.081 | ⚠ within organs, on part of the lines; also absent: DPY19L2, TRIML2, VASH1 |
| [[TEC]] | B | TEC activity raises FHIP1A's level | lines that do not express TEC (8) vs lines expressing it (42) | 2.03× lower at baseline in the lines without TEC | 0.097 | ⚠ within organs, on part of the lines; also absent: TXK; maybe low, not absent |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 13, C 0. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DLL3]] | B | FHIP1A activity lowers DLL3's level | lines that do not express FHIP1A (7) vs lines expressing it (43) | 3.17× higher at baseline in the lines without FHIP1A | 0.038 | ⚠ within organs, on part of the lines; also absent: SLC18B1, NIPAL1, TXNIP; maybe low, not absent |
| [[LINC02987]] | B | FHIP1A activity lowers LINC02987's level | lines that do not express FHIP1A (7) vs lines expressing it (43) | 2.44× higher at baseline in the lines without FHIP1A | 0.052 | ⚠ within organs, on part of the lines; also absent: SLC18B1, NIPAL1, TXNIP; maybe low, not absent |
| [[ZNF507]] | B | FHIP1A activity lowers ZNF507's level | lines that do not express FHIP1A (7) vs lines expressing it (43) | 1.53× higher at baseline in the lines without FHIP1A | 0.057 | ⚠ within organs, on part of the lines; also absent: SLC18B1, NIPAL1, TXNIP; maybe low, not absent |
| [[IRF6]] | B | FHIP1A activity raises IRF6's level | lines that do not express FHIP1A (7) vs lines expressing it (43) | 3.41× lower at baseline in the lines without FHIP1A | 0.069 | ⚠ within organs, on part of the lines; also absent: SLC18B1, NIPAL1, TXNIP; maybe low, not absent |
| [[UTP20]] | B | FHIP1A activity lowers UTP20's level | lines that do not express FHIP1A (7) vs lines expressing it (43) | 1.38× higher at baseline in the lines without FHIP1A | 0.070 | ⚠ within organs, on part of the lines; also absent: SLC18B1, NIPAL1, TXNIP; maybe low, not absent |
| [[RNASET2]] | B | FHIP1A activity raises RNASET2's level | lines that do not express FHIP1A (7) vs lines expressing it (43) | 1.63× lower at baseline in the lines without FHIP1A | 0.073 | ⚠ within organs, on part of the lines; also absent: SLC18B1, NIPAL1, TXNIP; maybe low, not absent |
| [[MPZL3]] | B | FHIP1A activity raises MPZL3's level | lines that do not express FHIP1A (7) vs lines expressing it (43) | 3.23× lower at baseline in the lines without FHIP1A | 0.079 | ⚠ within organs, on part of the lines; also absent: SLC18B1, NIPAL1, TXNIP; maybe low, not absent |
| [[C20orf96]] | B | FHIP1A activity lowers C20orf96's level | lines that do not express FHIP1A (7) vs lines expressing it (43) | 1.56× higher at baseline in the lines without FHIP1A | 0.079 | ⚠ within organs, on part of the lines; also absent: SLC18B1, NIPAL1, TXNIP; maybe low, not absent |
| [[FRRS1]] | B | FHIP1A activity raises FRRS1's level | lines that do not express FHIP1A (7) vs lines expressing it (43) | 1.64× lower at baseline in the lines without FHIP1A | 0.087 | ⚠ within organs, on part of the lines; also absent: SLC18B1, NIPAL1, TXNIP; maybe low, not absent |
| [[PREPL]] | B | FHIP1A activity lowers PREPL's level | lines that do not express FHIP1A (7) vs lines expressing it (43) | 1.35× higher at baseline in the lines without FHIP1A | 0.093 | ⚠ within organs, on part of the lines; also absent: SLC18B1, NIPAL1, TXNIP; maybe low, not absent |
| [[GPR160]] | B | FHIP1A activity raises GPR160's level | lines that do not express FHIP1A (7) vs lines expressing it (43) | 2.17× lower at baseline in the lines without FHIP1A | 0.096 | ⚠ within organs, on part of the lines; also absent: SLC18B1, NIPAL1, TXNIP; maybe low, not absent |
| [[ARRB2]] | B | FHIP1A activity lowers ARRB2's level | lines that do not express FHIP1A (7) vs lines expressing it (43) | 1.75× higher at baseline in the lines without FHIP1A | 0.097 | ⚠ within organs, on part of the lines; also absent: SLC18B1, NIPAL1, TXNIP; maybe low, not absent |

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction 0.708). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.5, -10.7); signed map (-31.9, 22.3). **Vector** length 133, 49.5% of its response variance represented; |z| ≥ 3 in 1,329 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.6 | +3.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +6.3 | +3.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.3 | -0.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.9 | +0.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.2 | -2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.1 | +1.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.8 | +1.8 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.8 | +2.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.8 | +0.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.0 | -11.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.6 | -8.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.1 | -8.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.9 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.4 | -5.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.0 | -5.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.4 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | FHF complex subunit HOOK interacting protein 1A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.3 — chr4:151,409,176-151,670,503 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ43373, FHIP-L; previously FAM160A1 |
| Gene groups (HGNC) | FHF complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q05DH4](https://www.uniprot.org/uniprotkb/Q05DH4) (FHF complex subunit HOOK-interacting protein 1A):

> Probable component of the FTS/Hook/FHIP complex (FHF complex). FHF complex promotes the distribution of AP-4 complex to the perinuclear area of the cell.

**Summary**, from NCBI Gene [729830](https://www.ncbi.nlm.nih.gov/gene/729830):

> Involved in protein localization to perinuclear region of cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:34237](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34237) · Entrez [729830](https://www.ncbi.nlm.nih.gov/gene/729830) · UniProt [Q05DH4](https://www.uniprot.org/uniprotkb/Q05DH4) · Ensembl [ENSG00000164142](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164142)

## Data

Gene col 8881: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8881); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8881, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8881]; `tensor/DDL_lfc|DDL_z.npy` [8881]; `embed/gene_vectors.npy` [8881]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8881 or target_col == 8881). Every well: [[FHIP1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FHIP1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
