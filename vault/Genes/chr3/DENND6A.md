---
symbol: "DENND6A"
type: "gene"
col: 10531
ensembl_id: "ENSG00000174839"
name: "DENN domain containing 6A"
location: "3p14.3"
module: 26
arm: "-"
pooled_cpm: 55.09
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 22
n_dd_up_clean: 1
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# DENND6A

*DENN domain containing 6A* — 3p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.26× (z +6.4, q 8e-08, up in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Tucidinostat (drug)]] 5 µM in 3 lines (LS 180 2.08×, LoVo 1.79×, KATO III 1.88×).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.570× (z -15.4, q 0e+00, down in 43 of 48 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.509× (z -13.3, q 4e-38, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BRAT1]] (+0.65, fdr 1e-05), [[TTLL4]] (+0.61, fdr 1e-05), [[SLC35A1]] (+0.61, fdr 2e-05); moves opposite to [[PHF8]] (-0.66, fdr 1e-05), [[LINC00571]] (-0.64, fdr 1e-05), [[NLGN3]] (-0.60, fdr 3e-05).
> It sits in the **-** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10531.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Tucidinostat (drug)]] 5 µM in 3 lines (LS 180 2.08×, LoVo 1.79×, KATO III 1.88×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +6.4 | 8e-08 | 24/48 (LS 180, LoVo, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.22×** | +3.9 | 0.030 | 20/48 (LS 180, KATO III, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | 1.38× | +3.3 | 0.20 | 14/48 (NCI-H460, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.18× | +3.2 | 0.20 | 17/47 (NCI-H2030, COLO 205, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10531.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.570×** | -15.4 | 0e+00 | 43/48 (HEC-1-A, A-172, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.450×** | -15.1 | 0e+00 | 34/43 (Panc 03.27, HCT15, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.445×** | -14.7 | 0e+00 | 38/44 (A-427, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.509×** | -13.3 | 4e-38 | 45/48 (HEC-1-A, SNU-423, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.646×** | -12.0 | 3e-31 | 44/48 (HEC-1-A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.599×** | -9.7 | 3e-20 | 31/48 (A-172, HEC-1-A, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.611×** | -9.7 | 3e-20 | 36/48 (A-427, SW480, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.390×** | -9.5 | 2e-19 | 40/49 (LOX-IMVI, HEC-1-A, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.621×** | -9.4 | 5e-19 | 33/48 (SW480, NCI-H460, …) | rises with dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.763×** | -7.4 | 8e-12 | 29/48 (A-427, HEC-1-A, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.721×** | -6.4 | 8e-09 | 28/48 (LS 180, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.726×** | -6.3 | 1e-08 | 27/48 (HEC-1-A, C32, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.730×** | -6.2 | 3e-08 | 31/48 (HEC-1-A, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.725×** | -6.1 | 5e-08 | 30/48 (SNU-423, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.732×** | -5.9 | 2e-07 | 31/48 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.775×** | -5.0 | 2e-05 | 28/48 (J82, C32, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.790×** | -4.4 | 4e-04 | 27/48 (HEC-1-A, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.678×** | -3.9 | 0.003 | 21/48 (HS-578T, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.800×** | -3.1 | 0.047 | 14/48 (Panc 03.27, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10531. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 109 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -22.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.290× (z -17.4) |
| [[NCI-H460 (line)]] | wt | 42.2 | 0 | 8 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.334× (z -12.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SW480 (line)]] | alt | 55.3 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.277× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.454× (z -10.6) |
| [[C32 (line)]] | wt | 59.8 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -16.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.280× (z -11.5) |
| [[HOP62 (line)]] | alt | 60.8 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -13.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.355× (z -11.2) |
| [[LS 180 (line)]] | wt | 42.5 | 1 | 5 (5 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.08× (z +9.5) | [[Digitoxin (drug)]] 5 µM 0.247× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[A-172 (line)]] | wt | 56.8 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -19.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.493× (z -10.6) |
| [[AN3 CA (line)]] | alt | 63.2 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -11.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.174× (z -9.0) |
| [[HS-578T (line)]] | alt | 71.0 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.363× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.525× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 65.4 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -13.4) |
| [[PANC-1 (line)]] | alt | 54.1 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.352× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.603× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 56.5 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.207× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.294× (z -10.5) |
| [[SNU-423 (line)]] | alt | 60.5 | 0 | 4 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.209× (z -15.2) |
| [[A-427 (line)]] | wt | 73.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.131× (z -20.5) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.347× (z -16.1) |
| [[A498 (line)]] | wt | 49.0 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.505× (z -10.2) ⚠ cell-cycle shift, explains ~27% of this change |
| [[LOX-IMVI (line)]] | wt | 49.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.266× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.164× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 52.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0531× (z -27.8) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.362× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 61.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.256× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 64.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -13.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 61.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.366× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 67.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.340× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -10.4) |
| [[COLO 205 (line)]] | alt | 29.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -10.3) ⚠ cell-cycle shift, explains ~27% of this change |
| [[H4 (line)]] | wt | 46.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[HCT15 (line)]] | alt | 68.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.108× (z -18.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 49.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -12.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -8.7) |
| [[J82 (line)]] | alt | 61.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.508× (z -10.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[KATO III (line)]] | alt | 52.2 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.88× (z +8.8) | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.132× (z -10.3) ⚠ toxic |
| [[LoVo (line)]] | wt | 50.6 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.79× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.366× (z -10.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 37.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -13.9) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H23 (line)]] | alt | 64.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -11.5) |
| [[RPMI-7951 (line)]] | alt | 63.4 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.304× (z -9.2) ⚠ transcription drop; cell-cycle shift, explains ~53% of this change |
| [[SNU-1 (line)]] | wt | 48.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -16.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.196× (z -11.0) |
| [[BT-474 (line)]] | alt | 37.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.326× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[C-33 A (line)]] | alt | 68.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.374× (z -9.1) |
| [[CHP-212 (line)]] | wt | 54.2 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0868× (z -11.2) |
| [[Hs 766T (line)]] | wt | 59.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.227× (z -12.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 59.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0806× (z -24.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 43.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -16.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW 1088 (line)]] | alt | 61.7 | 0 | 1 | — | [[Clopidogrel (drug)]] 5 µM 0.0586× (z -9.1) |
| [[SW 900 (line)]] | alt | 52.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -11.3) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW1417 (line)]] | alt | 34.7 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.463× (z -9.6) |
| [[SW48 (line)]] | wt | 57.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.150× (z -12.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10531), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRAT1]] | +0.65 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[TTLL4]] | +0.61 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[SLC35A1]] | +0.61 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[NR2C1]] | +0.60 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[ANAPC4]] | +0.60 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[CRLF3]] | +0.60 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[SLC15A4]] | +0.60 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[COPG2]] | +0.59 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[KANSL3]] | +0.58 | +0.66 / +0.40 | both halves | 4e-05 |  |
| [[RSAD1]] | +0.58 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[FBXL4]] | +0.58 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[GALNT11]] | +0.57 | +0.64 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHF8]] | -0.66 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[LINC00571]] | -0.64 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[NLGN3]] | -0.60 | -0.62 / -0.43 | both halves | 3e-05 |  |
| [[AKT1S1]] | -0.59 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[ZNF546]] | -0.59 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[NQO1-DT]] | -0.58 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[FBXL19-AS1]] | -0.58 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[CCDC90B-AS1]] | -0.57 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[PIPOX]] | -0.57 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[FAM120AOS]] | -0.56 | -0.57 / -0.34 | both halves | 1e-04 |  |
| [[MZF1-AS1]] | -0.55 | -0.57 / -0.31 | both halves | 2e-04 |  |
| [[C2orf49-DT]] | -0.55 | -0.58 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises DENND6A's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **-** arm (projection on the module's main direction -0.562). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-1.0, -1.9); signed map (-39.4, -17.5). **Vector** length 98.2, 25.7% of its response variance represented; |z| ≥ 3 in 1,107 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.6 | +1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +6.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | +1.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +0.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | +3.0 | +3.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.7 | +0.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.5 | +1.8 |
|  | [[Bexarotene (drug)]] 5 µM |  | +2.3 | +2.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.1 | +1.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.6 | -12.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.6 | -13.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.8 | -14.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.6 | -15.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -5.5 | -9.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.9 | -7.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.3 | -1.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.2 | -1.4 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -2.2 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | DENN domain containing 6A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p14.3 — chr3:57,625,454-57,693,077 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ34969, AFI1A; previously FAM116A |
| Gene groups (HGNC) | DENN domain containing |
| Reactome | 4 pathways, smallest: RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IWF6](https://www.uniprot.org/uniprotkb/Q8IWF6) (Protein DENND6A):

> Guanine nucleotide exchange factor (GEF) for RAB14. Component of an endocytic recycling pathway that is required for the control of ADAM10 transport, shedding of N-cadherin/CDH2 by ADAM9 or ADAM10 and regulation of cell-cell junctions. Required for RAB14 recruitment to recycling endosomes.

**Summary**, from NCBI Gene [201627](https://www.ncbi.nlm.nih.gov/gene/201627):

> Enables guanyl-nucleotide exchange factor activity. Involved in positive regulation of cell-cell adhesion mediated by cadherin. Located in recycling endosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26635](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26635) · Entrez [201627](https://www.ncbi.nlm.nih.gov/gene/201627) · UniProt [Q8IWF6](https://www.uniprot.org/uniprotkb/Q8IWF6) · Ensembl [ENSG00000174839](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174839)

## Data

Gene col 10531: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10531); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10531, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10531]; `tensor/DDL_lfc|DDL_z.npy` [10531]; `embed/gene_vectors.npy` [10531]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10531 or target_col == 10531). Every well: [[DENND6A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DENND6A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
