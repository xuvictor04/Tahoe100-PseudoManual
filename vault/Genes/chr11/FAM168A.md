---
symbol: "FAM168A"
type: "gene"
col: 616
ensembl_id: "ENSG00000054965"
name: "family with sequence similarity 168 member A"
location: "11q13.4"
module: 65
arm: "+"
pooled_cpm: 182.55
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 26
n_dd_up_clean: 0
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# FAM168A

*family with sequence similarity 168 member A* — 11q13.4

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 4 lines (PANC-1 4.06×, SW48 6.31×, A-427 3.50×, A498 3.79×); [[PH-797804 (drug)]] 5 µM in 2 lines (SW48 7.72×, C32 4.14×); [[Ponatinib (drug)]] 5 µM in 1 line (C32 2.06×).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.460× (z -21.4, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALG9]] (+0.76, fdr 7e-06), [[ARL6]] (+0.72, fdr 7e-06), [[FAM234B]] (+0.71, fdr 7e-06); moves opposite to [[NPIPB5]] (-0.63, fdr 1e-05), [[NPIPB4]] (-0.63, fdr 2e-05), [[ANKLE2]] (-0.60, fdr 3e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 616.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 4 lines (PANC-1 4.06×, SW48 6.31×, A-427 3.50×, A498 3.79×); [[PH-797804 (drug)]] 5 µM in 2 lines (SW48 7.72×, C32 4.14×); [[Ponatinib (drug)]] 5 µM in 1 line (C32 2.06×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.18× | +3.2 | 0.87 | 22/49 (NCI-H1792, A-172, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 616.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.460×** | -21.4 | 0e+00 | 46/48 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.355×** | -20.2 | 0e+00 | 47/48 (HOP62, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.362×** | -19.0 | 0e+00 | 44/44 (A-427, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.504×** | -18.9 | 0e+00 | 46/49 (NCI-H2347, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.406×** | -17.6 | 0e+00 | 47/49 (NCI-H2347, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.478×** | -13.9 | 1e-41 | 41/48 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.466×** | -13.8 | 3e-41 | 42/45 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.566×** | -10.7 | 1e-24 | 38/48 (SNU-423, HOP62, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.584×** | -10.5 | 6e-24 | 46/48 (HS-578T, A-172, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.601×** | -9.5 | 8e-20 | 39/50 (C32, HOP62, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.604×** | -9.4 | 2e-19 | 41/47 (NCI-H2347, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.626×** | -9.1 | 3e-18 | 47/48 (HOP62, SNU-423, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.675×** | -7.6 | 9e-13 | 35/48 (C32, HOP62, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.693×** | -7.2 | 3e-11 | 37/48 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.713×** | -6.6 | 2e-09 | 37/48 (RPMI-7951, HOP62, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.800×** | -6.1 | 3e-08 | 28/48 (NCI-H2347, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.769×** | -5.1 | 8e-06 | 33/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.814×** | -4.0 | 0.001 | 25/47 (HOP62, H4, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.837× | -3.5 | 0.012 | 24/48 (NCI-H460, NCI-H2347, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.897× | -3.0 | 0.057 | 8/49 (H4, HT-29, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.753×** | -2.9 | 0.075 | 19/49 (RPMI-7951, C32, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 616. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 163 | 0 | 19 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -26.8) |
| [[C32 (line)]] | wt | 305 | 2 | 15 (5 ⚠) | [[PH-797804 (drug)]] 5 µM 4.14× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -27.8) |
| [[HOP62 (line)]] | alt | 232 | 0 | 14 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -28.4) |
| [[SNU-423 (line)]] | alt | 197 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -22.6) |
| [[A-172 (line)]] | wt | 208 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -29.5) |
| [[CFPAC-1 (line)]] | alt | 180 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -26.6) |
| [[AsPC-1 (line)]] | alt | 87.8 | 0 | 11 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.206× (z -15.2) |
| [[MIA PaCa-2 (line)]] | alt | 201 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.358× (z -13.5) |
| [[RPMI-7951 (line)]] | alt | 227 | 0 | 11 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.309× (z -14.0) |
| [[HS-578T (line)]] | alt | 228 | 0 | 10 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -14.9) |
| [[LOX-IMVI (line)]] | wt | 215 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -26.2) |
| [[NCI-H2347 (line)]] | alt | 261 | 0 | 10 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -26.7) |
| [[Hs 766T (line)]] | wt | 167 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -19.0) |
| [[NCI-H1573 (line)]] | alt | 145 | 0 | 9 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.268× (z -16.7) |
| [[J82 (line)]] | alt | 169 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -25.2) |
| [[HepG2_C3A (line)]] | wt | 134 | 0 | 7 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.283× (z -13.2) |
| [[NCI-H1792 (line)]] | alt | 193 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.226× (z -18.8) |
| [[Panc 03.27 (line)]] | alt | 196 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -20.1) |
| [[PANC-1 (line)]] | alt | 189 | 2 (1 ⚠) | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.06× (z +12.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.389× (z -15.3) |
| [[SW1417 (line)]] | alt | 167 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -19.8) |
| [[HT-29 (line)]] | alt | 132 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.391× (z -11.8) |
| [[hTERT-HPNE (line)]] | wt | 155 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -16.1) |
| [[KATO III (line)]] | alt | 124 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -19.3) |
| [[LS 180 (line)]] | wt | 112 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -11.2) |
| [[NCI-H23 (line)]] | alt | 301 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.200× (z -22.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.231× (z -21.0) |
| [[RKO (line)]] | wt | 167 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -12.2) |
| [[SW 900 (line)]] | alt | 163 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -16.9) |
| [[SW48 (line)]] | wt | 174 | 2 | 4 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 7.72× (z +10.3) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -10.9) |
| [[A549 (line)]] | wt | 160 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -20.8) |
| [[BT-474 (line)]] | alt | 384 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -14.9) |
| [[HCT15 (line)]] | alt | 206 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.288× (z -12.9) |
| [[HEC-1-A (line)]] | alt | 197 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.343× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.541× (z -10.9) |
| [[NCI-H2030 (line)]] | alt | 227 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.452× (z -9.0) |
| [[A-427 (line)]] | wt | 214 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.50× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.0396× (z -44.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.519× (z -9.3) |
| [[COLO 205 (line)]] | alt | 104 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.280× (z -12.3) |
| [[H4 (line)]] | wt | 163 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -20.9) |
| [[SK-MEL-2 (line)]] | alt | 91.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -15.1) |
| [[SW480 (line)]] | alt | 168 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.386× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.563× (z -9.0) |
| [[AN3 CA (line)]] | alt | 283 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.212× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.369× (z -11.0) |
| [[C-33 A (line)]] | alt | 273 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.114× (z -22.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -9.7) |
| [[A498 (line)]] | wt | 70.2 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 3.79× (z +8.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.408× (z -11.2) |
| [[CHP-212 (line)]] | wt | 196 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.284× (z -9.8) ⚠ toxic |
| [[LoVo (line)]] | wt | 113 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.364× (z -13.5) |
| [[SHP-77 (line)]] | alt | 194 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.349× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.604× (z -9.8) |
| [[SW 1271 (line)]] | alt | 248 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -10.7) |
| [[SNU-1 (line)]] | wt | 243 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -19.0) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 182 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -9.4) |
| [[NCI-H2122 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 223 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 616), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALG9]] | +0.76 | +0.81 / +0.66 | both halves | 7e-06 |  |
| [[ARL6]] | +0.72 | +0.77 / +0.62 | both halves | 7e-06 |  |
| [[FAM234B]] | +0.71 | +0.77 / +0.60 | both halves | 7e-06 |  |
| [[HACE1]] | +0.71 | +0.78 / +0.59 | both halves | 7e-06 |  |
| [[KCTD6]] | +0.70 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[TFG]] | +0.67 | +0.74 / +0.60 | both halves | 7e-06 |  |
| [[EED]] | +0.66 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[PDK3]] | +0.66 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[SNAPC3]] | +0.66 | +0.75 / +0.53 | both halves | 1e-05 |  |
| [[VDAC3]] | +0.64 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[PRMT9]] | +0.63 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[PGAP1]] | +0.62 | +0.58 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPIPB5]] | -0.63 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[NPIPB4]] | -0.63 | -0.65 / -0.48 | both halves | 2e-05 |  |
| [[ANKLE2]] | -0.60 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[RESF1]] | -0.57 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[GGPS1]] | -0.57 | -0.66 / -0.40 | both halves | 5e-05 |  |
| [[REEP3]] | -0.56 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[C11orf58]] | -0.55 | -0.60 / -0.42 | both halves | 4e-05 |  |
| [[ZHX2]] | -0.55 | -0.56 / -0.38 | both halves | 6e-05 |  |
| [[SH3D19]] | -0.54 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[CDR2]] | -0.54 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[KDSR]] | -0.54 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[TUT7]] | -0.54 | -0.52 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises FAM168A's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SMARCD3]] | C | SMARCD3 activity raises FAM168A's level | lines that do not express SMARCD3 (3) vs lines expressing it (47) | 1.54× lower at baseline in the lines without SMARCD3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p |
| [[HACE1]] | C | HACE1 activity raises FAM168A's level | lines that do not express HACE1 (3) vs lines expressing it (47) | 1.75× lower at baseline in the lines without HACE1 | 0.064 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, CFL2, ATP6V1E2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.715). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (7.3, -12.8); signed map (-32.5, -7.4). **Vector** length 112, 42.9% of its response variance represented; |z| ≥ 3 in 1,374 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.4 | -0.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.0 | -5.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.4 | -1.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.2 | +1.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +3.1 | -6.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | +1.0 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +2.7 | +1.6 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +2.5 | +3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.2 | +1.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.8 | -20.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -5.6 | -5.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.6 | -21.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -4.7 | -4.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.1 | -1.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.4 | -1.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.2 | +1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -5.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.0 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 168 member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.4 — chr11:73,400,487-73,598,189 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TCRP1; previously KIAA0280 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92567](https://www.uniprot.org/uniprotkb/Q92567) (Protein FAM168A):

> In cancer context, decreases POLB ubiquitination and stabilizes its protein levels. Acts, at least in part, through PI3K/AKT/NFKB signaling pathway and by preventing POLB degradation. Results in protection of cells from induced-DNA damage and apoptosis.

**Summary**, from NCBI Gene [23201](https://www.ncbi.nlm.nih.gov/gene/23201):

> Involved in positive regulation of base-excision repair. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28999](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28999) · Entrez [23201](https://www.ncbi.nlm.nih.gov/gene/23201) · UniProt [Q92567](https://www.uniprot.org/uniprotkb/Q92567) · Ensembl [ENSG00000054965](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000054965)

## Data

Gene col 616: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 616); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 616, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 616]; `tensor/DDL_lfc|DDL_z.npy` [616]; `embed/gene_vectors.npy` [616]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 616 or target_col == 616). Every well: [[FAM168A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM168A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
