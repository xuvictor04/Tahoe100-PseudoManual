---
symbol: "MAGED1"
type: "gene"
col: 11011
ensembl_id: "ENSG00000179222"
name: "MAGE family member D1"
location: "Xp11.22"
module: 41
arm: "+"
pooled_cpm: 84.33
n_lines_expressing: 48
n_dd_up: 2
n_dd_down: 27
n_dd_up_clean: 1
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# MAGED1

*MAGE family member D1* — Xp11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.23× (z +6.2, q 4e-07, up in 23 of 46 measured lines) ⚠ cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[NG25 (drug)]] 5 µM: 1.47× (z +4.3, q 0.006, up in 21 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (12 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.369× (z -20.9, q 0e+00, down in 45 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.391× (z -19.7, q 0e+00, down in 44 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZC4H2]] (+0.54, fdr 5e-05), [[MRPL1]] (+0.54, fdr 1e-05), [[VIRMA]] (+0.53, fdr 3e-05); moves opposite to [[DUSP22]] (-0.48, fdr 3e-05), [[ARHGAP21]] (-0.47, fdr 6e-05), [[DPY19L1P1]] (-0.46, fdr 4e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11011.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.23×** | +6.2 | 4e-07 | 23/46 (A549, HT-29, …) | rises with dose | low cells (technical?) |
| [[NG25 (drug)]] 5 µM |  | **1.47×** | +4.3 | 0.006 | 21/45 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.19× | +3.8 | 0.033 | 18/47 (SW1417, NCI-H1573, …) | all doses, flat |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 1.15× | +3.1 | 0.22 | 10/46 (NCI-H2347, SNU-423, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.1 | 0.22 | 13/46 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | 1.15× | +3.1 | 0.22 | 8/46 (RPMI-7951, A-172, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11011.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.369×** | -20.9 | 0e+00 | 45/46 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.391×** | -19.7 | 0e+00 | 44/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.456×** | -16.5 | 0e+00 | 45/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.614×** | -14.4 | 8e-45 | 37/46 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.517×** | -13.8 | 2e-41 | 41/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.592×** | -10.9 | 7e-26 | 37/46 (CFPAC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.708×** | -10.2 | 2e-22 | 31/47 (SW1417, SW 900, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.633×** | -9.2 | 3e-18 | 30/45 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.659×** | -8.4 | 4e-15 | 33/46 (NCI-H23, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.679×** | -8.1 | 4e-14 | 29/46 (HCT15, CFPAC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.689×** | -7.5 | 5e-12 | 32/46 (PANC-1, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.744×** | -5.9 | 2e-07 | 24/48 (LS 180, H4, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.753×** | -5.9 | 2e-07 | 27/46 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.734×** | -5.8 | 2e-07 | 27/45 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.743×** | -5.6 | 8e-07 | 29/46 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.768×** | -5.5 | 1e-06 | 24/46 (H4, MIA PaCa-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.762×** | -5.3 | 3e-06 | 29/46 (SNU-423, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.775×** | -5.3 | 4e-06 | 25/46 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.809×** | -4.2 | 6e-04 | 19/46 (CFPAC-1, MIA PaCa-2, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.873× | -4.0 | 0.002 | 12/47 (CFPAC-1, A-172, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11011. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 81.1 | 0 | 13 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.152× (z -24.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.182× (z -22.1) |
| [[H4 (line)]] | wt | 202 | 0 | 11 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.226× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.250× (z -15.4) |
| [[PANC-1 (line)]] | alt | 143 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -23.7) |
| [[MIA PaCa-2 (line)]] | alt | 108 | 0 | 10 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.277× (z -13.4) ⚠ toxic; cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.327× (z -12.2) |
| [[LS 180 (line)]] | wt | 91.9 | 0 | 8 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.294× (z -13.9) |
| [[SW 900 (line)]] | alt | 101 | 0 | 8 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.301× (z -13.1) |
| [[RPMI-7951 (line)]] | alt | 199 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.251× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -13.9) |
| [[SW480 (line)]] | alt | 98.0 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.181× (z -22.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.190× (z -22.0) |
| [[hTERT-HPNE (line)]] | wt | 160 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.257× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.412× (z -13.0) |
| [[HOP62 (line)]] | alt | 71.6 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.316× (z -13.2) |
| [[HT-29 (line)]] | alt | 104 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.332× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.368× (z -11.7) |
| [[SNU-423 (line)]] | alt | 166 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -18.4) |
| [[SW1417 (line)]] | alt | 75.7 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.175× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.242× (z -15.4) |
| [[CFPAC-1 (line)]] | alt | 100 | 0 | 4 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.418× (z -10.3) |
| [[HCT15 (line)]] | alt | 127 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.200× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.350× (z -11.2) |
| [[J82 (line)]] | alt | 65.3 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.339× (z -11.9) |
| [[KATO III (line)]] | alt | 126 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0698× (z -31.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.290× (z -14.6) |
| [[RKO (line)]] | wt | 64.5 | 0 | 4 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -12.7) |
| [[A-172 (line)]] | wt | 81.2 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.398× (z -8.9) |
| [[NCI-H1792 (line)]] | alt | 38.4 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.220× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.252× (z -11.4) |
| [[SHP-77 (line)]] | alt | 121 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.392× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -11.0) |
| [[A498 (line)]] | wt | 68.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.312× (z -9.9) |
| [[AN3 CA (line)]] | alt | 212 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -16.7) |
| [[AsPC-1 (line)]] | alt | 41.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -9.7) |
| [[BT-474 (line)]] | alt | 57.0 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.280× (z -8.9) |
| [[Hs 766T (line)]] | wt | 72.8 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.253× (z -11.2) |
| [[NCI-H23 (line)]] | alt | 74.2 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.107× (z -20.7) |
| [[SK-MEL-2 (line)]] | alt | 92.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -10.2) |
| [[A-427 (line)]] | wt | 121 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -13.6) |
| [[C32 (line)]] | wt | 78.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -10.2) |
| [[CHP-212 (line)]] | wt | 87.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.170× (z -9.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 46.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.380× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 55.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.489× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 80.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -11.3) |
| [[SNU-1 (line)]] | wt | 98.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -9.3) |
| [[SW 1271 (line)]] | alt | 81.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0988× (z -10.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 76.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 138 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.18 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 83.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.71 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 90.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 86.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11011), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC4H2]] | +0.54 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[MRPL1]] | +0.54 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[VIRMA]] | +0.53 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[KBTBD7]] | +0.53 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[MAGED2]] | +0.53 | +0.59 / +0.42 | both halves | 4e-05 | same gene group; STRING 771 |
| [[LINC00632]] | +0.53 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[NDUFA8]] | +0.52 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[EDC3]] | +0.52 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[SMARCAD1]] | +0.51 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[NMD3]] | +0.51 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[RIOK2]] | +0.51 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[VTA1]] | +0.51 | +0.42 / +0.52 | both halves | 4e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUSP22]] | -0.48 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[ARHGAP21]] | -0.47 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[DPY19L1P1]] | -0.46 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[PDE6D]] | -0.46 | -0.46 / -0.31 | both halves | 2e-04 |  |
| [[NFATC2IP]] | -0.46 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[CCDC93]] | -0.45 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[NUP50-DT]] | -0.45 | -0.54 / -0.30 | both halves | 2e-04 |  |
| [[SRPK1]] | -0.43 | -0.45 / -0.40 | both halves | 4e-05 |  |
| [[DGKE]] | -0.42 | -0.42 / -0.32 | both halves | 1e-04 |  |
| [[SAP30L-AS1]] | -0.42 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[BRD3]] | -0.42 | -0.36 / -0.39 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.320). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-37.1, -5.9); signed map (-13.5, -10.9). **Vector** length 86.4, 22.1% of its response variance represented; |z| ≥ 3 in 1,156 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +7.1 | +6.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +6.5 | +0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.1 | -1.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.9 | +1.4 |
|  | [[NG25 (drug)]] 5 µM |  | +3.4 | +4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +2.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.5 | +1.2 |
|  | [[EX229 (drug)]] 5 µM |  | +2.2 | +1.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.2 | +0.8 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.7 | -8.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -4.0 | -5.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.3 | -16.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.2 | -13.8 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -3.2 | -5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -5.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.9 | -0.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -8.1 |
|  | [[Neratinib (drug)]] 5 µM |  | -1.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | MAGE family member D1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.22 — chrX:51,803,007-51,902,354 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NRAGE, DLXIN-1 |
| Gene groups (HGNC) | MAGE family |
| Reactome | 10 pathways, smallest: Caspase activation via Dependence Receptors in the absence of ligand; NPAS4 regulates expression of target genes; Caspase activation via extrinsic apoptotic signalling pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5V3](https://www.uniprot.org/uniprotkb/Q9Y5V3) (Melanoma-associated antigen D1):

> Involved in the apoptotic response after nerve growth factor (NGF) binding in neuronal cells. Inhibits cell cycle progression, and facilitates NGFR-mediated apoptosis. May act as a regulator of the function of DLX family members. May enhance ubiquitin ligase activity of RING-type zinc finger-containing E3 ubiquitin-protein ligases. Proposed to act through recruitment and/or stabilization of the Ubl-conjugating enzyme (E2) at the E3:substrate complex. Plays a role in the circadian rhythm …

**Summary**, from NCBI Gene [9500](https://www.ncbi.nlm.nih.gov/gene/9500):

> This gene is a member of the melanoma antigen gene (MAGE) family. Most of the genes of this family encode tumor specific antigens that are not expressed in normal adult tissues except testis. Although the protein encoded by this gene shares strong homology with members of the MAGE family, it is expressed in almost all normal adult tissues. This gene has been demonstrated to be involved in the p75 neurotrophin receptor mediated programmed cell death pathway. Three transcript variants encoding …

**Accessions** — [HGNC:6813](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6813) · Entrez [9500](https://www.ncbi.nlm.nih.gov/gene/9500) · UniProt [Q9Y5V3](https://www.uniprot.org/uniprotkb/Q9Y5V3) · Ensembl [ENSG00000179222](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179222)

## Data

Gene col 11011: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11011); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11011, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11011]; `tensor/DDL_lfc|DDL_z.npy` [11011]; `embed/gene_vectors.npy` [11011]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11011 or target_col == 11011). Every well: [[MAGED1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAGED1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
