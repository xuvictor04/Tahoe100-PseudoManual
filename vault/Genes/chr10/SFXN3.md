---
symbol: "SFXN3"
type: "gene"
col: 2884
ensembl_id: "ENSG00000107819"
name: "sideroflexin 3"
location: "10q24.31"
module: 137
arm: "-"
pooled_cpm: 39.86
n_lines_expressing: 47
n_dd_up: 5
n_dd_down: 39
n_dd_up_clean: 4
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 7
direction_downstream: 9
tags: ["gene", "module/137"]
generated_by: "tahoemap"
---

# SFXN3

*sideroflexin 3* — 10q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.10× (z +5.2, q 1e-04, up in 3 of 46 measured lines) ⚠ position not correctable. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 1.51× (z +4.7, q 8e-04, up in 25 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.203× (z -35.7, q 0e+00, down in 43 of 44 measured lines).
> Its strongest partners by |cos| (81 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 20 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDZD7]] (+0.66, fdr 3e-05, ⚠ same locus), [[GNAI2]] (+0.63, fdr 8e-05), [[SLC27A1]] (+0.63, fdr 2e-04), [[CARD19]] (+0.63, fdr 2e-05); moves opposite to [[SLC25A21]] (-0.62, fdr 1e-04), [[TMCO4]] (-0.60, fdr 9e-05), [[ENOX2]] (-0.60, fdr 6e-05).
> It sits in the **-** arm of [[Module 137]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[SRPX]] → it (grade B ⚠); 9 go from it, the strongest it → [[FCHSD1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2884.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +5.2 | 1e-04 | 3/46 (HOP62, NCI-H23, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.51×** | +4.7 | 8e-04 | 25/43 (NCI-H460, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.28×** | +3.9 | 0.017 | 19/44 (SK-MEL-2, LS 180, …) | two highest doses | low cells (technical?) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +3.6 | 0.033 | 16/38 (SW 900, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.033 | 17/45 (SNU-423, BT-474, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.36×** | +3.5 | 0.045 | 12/44 (SHP-77, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | 1.33× | +3.2 | 0.10 | 10/44 (Hs 766T, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | 1.32× | +3.2 | 0.11 | 10/44 (PANC-1, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Saquinavir (drug)]] 0.5 µM |  | 1.21× | +3.1 | 0.12 | 14/44 (C32, NCI-H1792, …) | two highest doses |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | 1.21× | +3.0 | 0.13 | 11/45 (Hs 766T, A498, …) | all doses, flat | position effect removed |
| [[4EGI-1 (drug)]] 5 µM |  | 1.46× | +3.0 | 0.13 | 13/44 (SW480, Hs 766T, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 16 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2884.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.203×** | -35.7 | 0e+00 | 43/44 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.276×** | -19.6 | 0e+00 | 42/44 (SW 900, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.302×** | -19.0 | 0e+00 | 40/43 (HOP62, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.449×** | -18.0 | 0e+00 | 41/43 (NCI-H1792, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.384×** | -15.2 | 0e+00 | 41/45 (SNU-423, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.448×** | -12.7 | 3e-35 | 37/44 (HepG2/C3A, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.481×** | -11.6 | 4e-29 | 39/45 (SW 900, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.499×** | -11.0 | 2e-26 | 40/45 (SW 900, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.537×** | -9.9 | 3e-21 | 36/44 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.322×** | -9.1 | 8e-18 | 38/46 (LOX-IMVI, C32, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.569×** | -8.6 | 4e-16 | 27/42 (Hs 766T, HT-29, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.603×** | -8.0 | 5e-14 | 29/45 (HOP62, C32, …) | rises with dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.594×** | -7.9 | 9e-14 | 31/45 (SNU-423, SW480, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.621×** | -7.6 | 2e-12 | 23/45 (RPMI-7951, C32, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.625×** | -7.2 | 3e-11 | 30/42 (H4, HOP62, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.728×** | -7.1 | 5e-11 | 28/45 (HOP62, SNU-423, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.417×** | -7.0 | 1e-10 | 30/43 (C32, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.763×** | -6.1 | 4e-08 | 25/45 (NCI-H460, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.697×** | -5.7 | 3e-07 | 26/45 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.725×** | -5.1 | 9e-06 | 25/44 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.41 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2884. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 85.3 | 0 | 18 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0523× (z -37.6) |
| [[SNU-423 (line)]] | alt | 96.9 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0729× (z -32.5) |
| [[C32 (line)]] | wt | 95.8 | 0 | 13 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -23.7) |
| [[NCI-H460 (line)]] | wt | 46.8 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -31.5) |
| [[SW 900 (line)]] | alt | 56.5 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -24.6) |
| [[HS-578T (line)]] | alt | 39.4 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -25.9) |
| [[LOX-IMVI (line)]] | wt | 45.0 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -17.3) |
| [[SW480 (line)]] | alt | 36.1 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -27.1) |
| [[A-172 (line)]] | wt | 120 | 0 | 6 (3 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.319× (z -11.2) |
| [[NCI-H1792 (line)]] | alt | 45.9 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.104× (z -24.2) |
| [[RPMI-7951 (line)]] | alt | 70.2 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0766× (z -20.7) |
| [[SK-MEL-2 (line)]] | alt | 61.2 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -20.8) |
| [[A549 (line)]] | wt | 34.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -19.6) |
| [[CFPAC-1 (line)]] | alt | 44.6 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.0879× (z -27.9) |
| [[H4 (line)]] | wt | 53.0 | 0 | 5 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0716× (z -16.3) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0815× (z -16.1) |
| [[HepG2_C3A (line)]] | wt | 42.1 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0579× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.175× (z -15.3) |
| [[LoVo (line)]] | wt | 17.9 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -14.6) |
| [[PANC-1 (line)]] | alt | 20.3 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -21.3) |
| [[HCT15 (line)]] | alt | 47.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -15.5) |
| [[Hs 766T (line)]] | wt | 66.9 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -19.7) |
| [[HT-29 (line)]] | alt | 38.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -18.8) |
| [[hTERT-HPNE (line)]] | wt | 53.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -19.5) |
| [[J82 (line)]] | alt | 61.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -25.3) |
| [[NCI-H2347 (line)]] | alt | 23.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -17.5) |
| [[Panc 03.27 (line)]] | alt | 29.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -23.2) |
| [[BT-474 (line)]] | alt | 17.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -12.5) |
| [[HEC-1-A (line)]] | alt | 52.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -16.5) |
| [[A498 (line)]] | wt | 27.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 34.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -11.3) |
| [[CHP-212 (line)]] | wt | 73.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0835× (z -12.6) |
| [[COLO 205 (line)]] | alt | 21.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -12.4) |
| [[KATO III (line)]] | alt | 15.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.78× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -9.9) |
| [[RKO (line)]] | wt | 33.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -19.3) |
| [[LS 180 (line)]] | wt | 41.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -13.0) |
| [[NCI-H1573 (line)]] | alt | 17.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 22.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -18.4) |
| [[NCI-H23 (line)]] | alt | 13.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -9.9) |
| [[SW 1271 (line)]] | alt | 51.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0799× (z -11.9) |
| [[A-427 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.45 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.79 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.83 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 50.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2884), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 7 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDZD7]] | +0.66 | +0.59 / +0.45 | both halves | 3e-05 | STRING 429; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[GNAI2]] | +0.63 | +0.57 / +0.37 | both halves | 8e-05 |  |
| [[SLC27A1]] | +0.63 | +0.59 / +0.32 | both halves | 2e-04 |  |
| [[CARD19]] | +0.63 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[SLC26A6]] | +0.61 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[MGST3]] | +0.61 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[RAB3A]] | +0.60 | +0.44 / +0.34 | both halves | 1e-04 |  |
| [[TRAM2]] | +0.60 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[UNC45A]] | +0.60 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[SNTA1]] | +0.58 | +0.56 / +0.33 | both halves | 1e-04 |  |
| [[PEDS1]] | +0.58 | +0.53 / +0.25 | both halves | 4e-04 |  |
| [[ANO8]] | +0.58 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[ATOSB]] | +0.58 | +0.61 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 13 of them with an alert (⚠; 13 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A21]] | -0.62 | -0.57 / -0.34 | both halves | 1e-04 |  |
| [[TMCO4]] | -0.60 | -0.48 / -0.37 | both halves | 9e-05 |  |
| [[ENOX2]] | -0.60 | -0.61 / -0.38 | both halves | 6e-05 |  |
| [[EPM2A]] | -0.59 | -0.52 / -0.22 | both halves | 6e-04 |  |
| [[GTF3C6]] | -0.59 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[DPH5-DT]] | -0.58 | -0.60 / -0.27 | both halves | 3e-04 |  |
| [[PHACTR2]] | -0.58 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[HNF4G]] | -0.58 | -0.48 / -0.37 | both halves | 7e-05 |  |
| [[WARS2-AS1]] | -0.58 | -0.60 / -0.26 | both halves | 4e-04 |  |
| [[PCBD2]] | -0.57 | -0.58 / -0.33 | both halves | 1e-04 |  |
| [[IQCH-AS1]] | -0.57 | -0.62 / -0.19 | ⚠ one half (not replicated) | 9e-04 |  |
| [[ARAP2]] | -0.55 | -0.55 / -0.36 | both halves | 1e-04 |  |
| [[GRIP1]] | -0.54 | -0.48 / -0.21 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SRPX]] | B | SRPX activity raises SFXN3's level | lines that do not express SRPX (22) vs lines expressing it (28) | 1.97× lower at baseline in the lines without SRPX | 0.013 | ⚠ within organs, on part of the lines; also absent: COL15A1, ARHGEF6, ENSG00000230647 |
| [[CA12]] | B | CA12 activity raises SFXN3's level | lines that do not express CA12 (29) vs lines expressing it (21) | 1.95× lower at baseline in the lines without CA12 | 0.017 | ⚠ within organs, on part of the lines; also absent: NID2, IL33, IDO1 |
| [[OSBPL7]] | B | OSBPL7 activity raises SFXN3's level | lines that do not express OSBPL7 (7) vs lines expressing it (43) | 3.01× lower at baseline in the lines without OSBPL7 | 0.021 | ⚠ within organs, on part of the lines; also absent: TBXAS1, PYROXD2, ETS2 |
| [[LINC02575]] | B | LINC02575 activity lowers SFXN3's level | lines that do not express LINC02575 (32) vs lines expressing it (18) | 1.73× higher at baseline in the lines without LINC02575 | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000289309, LINC01205, MSRB3-AS1 |
| [[TOP2A]] | B | TOP2A activity raises SFXN3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NDRG1]] | B | NDRG1 activity raises SFXN3's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 3.78× lower at baseline in the lines without NDRG1 | 0.068 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |
| [[VLDLR]] | B | VLDLR activity strengthens SFXN3's drug response | lines that do not express VLDLR (8) vs lines expressing it (38) | the lines without VLDLR respond 0.60× as strongly (z diff +2.38); strongest at Homoharringtonine 0.5 µM: 0.49x vs 0.23x (z diff +3.7) | 0.081 | ⚠ within organs, on part of the lines; also absent: NEURL3, ALK, ENSG00000258989; target measured in part of the lines; artifact flags |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 0, C 9.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FCHSD1]] | C | SFXN3 activity raises FCHSD1's level | lines that do not express SFXN3 (3) vs lines expressing it (47) | 3.77× lower at baseline in the lines without SFXN3 | 9e-04 | ⚠ few lines (3 vs 47); across organs; also absent: LRRCC1, GULP1, SMAD7; co-absent with the target |
| [[NDRG1]] | C | SFXN3 activity raises NDRG1's level | lines that do not express SFXN3 (3) vs lines expressing it (47) | 5.29× lower at baseline in the lines without SFXN3 | 0.021 | ⚠ few lines (3 vs 47); across organs; also absent: LRRCC1, GULP1, SMAD7 |
| [[MGST3]] | C | SFXN3 activity raises MGST3's level | lines that do not express SFXN3 (3) vs lines expressing it (47) | 2.45× lower at baseline in the lines without SFXN3 | 0.023 | ⚠ few lines (3 vs 47); across organs; also absent: LRRCC1, GULP1, SMAD7 |
| cells under [[Ouabain (Octahydrate) (drug)]] 0.05 µM | C | SFXN3 activity raises the cells' numbers under Ouabain (Octahydrate) 0.05 µM (protects the cells) | lines that do not express SFXN3 (3) vs lines expressing it (45) | the lines without SFXN3: 0.71× the cells of the other lines | 0.055 | ⚠ few lines (3 vs 47); across organs; also absent: LRRCC1, GULP1, SMAD7 |
| cells under [[Pentoxifylline (drug)]] 0.5 µM | C | SFXN3 activity raises the cells' numbers under Pentoxifylline 0.5 µM (protects the cells) | lines that do not express SFXN3 (3) vs lines expressing it (45) | the lines without SFXN3: 0.76× the cells of the other lines | 0.055 | ⚠ few lines (3 vs 47); across organs; also absent: LRRCC1, GULP1, SMAD7 |
| [[ITGA5]] | C | SFXN3 activity strengthens ITGA5's drug response | lines that do not express SFXN3 (3) vs lines expressing it (35) | the lines without SFXN3 respond 0.12× as strongly (z diff +4.82); rises at some drug-doses, falls at others (37% from rises): Homoharringtonine 0.5 µM: 1.80x vs 0.40x (z diff +8.4); Idarubicin (hydrochloride) 5 µM: 1.56x vs 0.63x (z diff +7.7); PH-797804 5 µM: 2.31x vs 4.63x (z diff +4.6) | 0.064 | ⚠ few lines (3 vs 47); across organs; also absent: LRRCC1, GULP1, SMAD7; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[MAST1]] | C | SFXN3 activity lowers MAST1's level | lines that do not express SFXN3 (3) vs lines expressing it (47) | 3.27× higher at baseline in the lines without SFXN3 | 0.072 | ⚠ few lines (3 vs 47); across organs; also absent: LRRCC1, GULP1, SMAD7 |
| [[PDZD7]] | C | SFXN3 activity raises PDZD7's level | lines that do not express SFXN3 (3) vs lines expressing it (47) | 1.98× lower at baseline in the lines without SFXN3 | 0.087 | ⚠ few lines (3 vs 47); across organs; also absent: LRRCC1, GULP1, SMAD7 |
| cells under [[Niclosamide (olamine) (drug)]] 5 µM | C | SFXN3 activity raises the cells' numbers under Niclosamide (olamine) 5 µM (protects the cells) | lines that do not express SFXN3 (3) vs lines expressing it (45) | the lines without SFXN3: 0.39× the cells of the other lines | 0.094 | ⚠ few lines (3 vs 47); across organs; also absent: LRRCC1, GULP1, SMAD7 |

## Where it sits

- **Module**: [[Module 137]]; 34 genes; this gene is in the **-** arm (projection on the module's main direction -0.659). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (5.3, -1.7); signed map (-28.5, 19.0). **Vector** length 93.7, 26.4% of its response variance represented; |z| ≥ 3 in 1,202 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.8 | +0.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.8 | +1.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +4.1 | -7.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.8 | +3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.3 | -0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +0.3 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +3.0 | +2.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.9 | +4.7 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.8 | -19.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.8 | -9.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.6 | -19.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -5.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.5 | -2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -7.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.9 | -3.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.9 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | sideroflexin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.31 — chr10:101,031,234-101,041,241 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SFX3, SLC56A3 |
| Gene groups (HGNC) | Solute carrier family 56, sideroflexins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BWM7](https://www.uniprot.org/uniprotkb/Q9BWM7) (Sideroflexin-3):

> Mitochondrial serine transporter that mediates transport of serine into mitochondria, an important step of the one-carbon metabolism pathway. Mitochondrial serine is converted to glycine and formate, which then exits to the cytosol where it is used to generate the charged folates that serve as one-carbon donors.

**Summary**, from NCBI Gene [81855](https://www.ncbi.nlm.nih.gov/gene/81855):

> Enables L-serine transmembrane transporter activity. Involved in serine import into mitochondrion. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16087](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16087) · Entrez [81855](https://www.ncbi.nlm.nih.gov/gene/81855) · UniProt [Q9BWM7](https://www.uniprot.org/uniprotkb/Q9BWM7) · Ensembl [ENSG00000107819](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107819)

## Data

Gene col 2884: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2884); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2884, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2884]; `tensor/DDL_lfc|DDL_z.npy` [2884]; `embed/gene_vectors.npy` [2884]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2884 or target_col == 2884). Every well: [[SFXN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SFXN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
