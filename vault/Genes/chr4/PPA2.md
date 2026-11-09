---
symbol: "PPA2"
type: "gene"
col: 6236
ensembl_id: "ENSG00000138777"
name: "inorganic pyrophosphatase 2"
location: "4q24"
module: 4
arm: "+"
pooled_cpm: 89.68
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 14
n_dd_up_clean: 0
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# PPA2

*inorganic pyrophosphatase 2* — 4q24

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1573 2.07×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.504× (z -26.5, q 0e+00, down in 47 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DTWD2]] (+0.64, fdr 1e-05), [[SHPRH]] (+0.61, fdr 7e-06), [[VWA8]] (+0.60, fdr 1e-05); moves opposite to [[SLC10A3]] (-0.61, fdr 1e-05), [[EPOR]] (-0.56, fdr 1e-05), [[CATSPERG]] (-0.52, fdr 1e-04).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6236.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1573 2.07×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +4.8 | 0.001 | 14/48 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.19× | +4.5 | 0.002 | 21/47 (NCI-H1573, A549, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.14× | +3.7 | 0.039 | 17/48 (NCI-H1792, LoVo, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.09× | +3.5 | 0.071 | 0/48 | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.13× | +3.4 | 0.076 | 19/49 (CFPAC-1, PANC-1, …) | inconsistent across doses | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.12× | +3.2 | 0.12 | 14/48 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 16 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6236.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.504×** | -26.5 | 0e+00 | 47/49 (HEC-1-A, LS 180, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.703×** | -13.6 | 9e-40 | 43/48 (HEC-1-A, SW1417, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.642×** | -11.6 | 6e-29 | 33/48 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.663×** | -11.2 | 6e-27 | 38/48 (SW480, RKO, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.697×** | -9.8 | 9e-21 | 34/48 (SW480, C-33 A, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.712×** | -9.3 | 2e-18 | 31/48 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.746×** | -7.7 | 1e-12 | 30/50 (HEC-1-A, C-33 A, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.757×** | -7.3 | 2e-11 | 29/48 (PANC-1, A498, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.768×** | -7.2 | 4e-11 | 29/48 (LoVo, C-33 A, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.771×** | -7.1 | 8e-11 | 32/48 (SW48, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.776×** | -6.9 | 2e-10 | 28/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.821×** | -5.4 | 4e-06 | 24/48 (SW480, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 0.871× | -5.3 | 4e-06 | 20/48 (A498, C32, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.825×** | -5.3 | 6e-06 | 22/48 (HT-29, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.840× | -4.7 | 8e-05 | 21/48 (AN3 CA, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.884× | -3.4 | 0.021 | 13/48 (C-33 A, HT-29, …) | two highest doses |  |
| [[vincristine (drug)]] 0.5 µM |  | 0.852× | -3.1 | 0.044 | 11/48 (NCI-H460, LS 180, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 0.889× | -3.1 | 0.046 | 9/48 (Panc 03.27, LS 180, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.853× | -3.1 | 0.046 | 15/48 (KATO III, LoVo, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.894× | -3.0 | 0.050 | 14/48 (C32, HOP62, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.924× | -3.0 | 0.050 | 8/49 (HT-29, BT-474, …) | all doses, flat |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.859× | -3.0 | 0.062 | 13/48 (NCI-H460, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | 0.898× | -2.9 | 0.062 | 8/49 (COLO 205, SNU-423, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6236. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 73.4 | 0 | 10 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -18.3) |
| [[NCI-H460 (line)]] | wt | 113 | 0 | 8 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -17.7) |
| [[PANC-1 (line)]] | alt | 79.4 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.540× (z -14.3) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.621× (z -11.0) |
| [[C-33 A (line)]] | alt | 180 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -20.6) |
| [[A498 (line)]] | wt | 106 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -17.8) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -14.7) |
| [[HEC-1-A (line)]] | alt | 147 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -22.9) |
| [[LoVo (line)]] | wt | 129 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.520× (z -15.5) |
| [[LS 180 (line)]] | wt | 172 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -22.8) |
| [[C32 (line)]] | wt | 95.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -14.9) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -13.8) |
| [[HepG2_C3A (line)]] | wt | 65.4 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -9.5) |
| [[RKO (line)]] | wt | 150 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -16.3) |
| [[SW1417 (line)]] | alt | 70.7 | 0 | 3 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.496× (z -12.9) |
| [[AN3 CA (line)]] | alt | 152 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.255× (z -10.8) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 62.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -10.1) |
| [[H4 (line)]] | wt | 82.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -10.6) |
| [[HOP62 (line)]] | alt | 75.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -12.5) |
| [[HT-29 (line)]] | alt | 158 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -20.2) |
| [[MIA PaCa-2 (line)]] | alt | 91.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.594× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 111 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.07× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -11.9) |
| [[Panc 03.27 (line)]] | alt | 90.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -15.3) |
| [[SW48 (line)]] | wt | 136 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.263× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.283× (z -11.1) |
| [[A549 (line)]] | wt | 63.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -8.7) |
| [[CHP-212 (line)]] | wt | 103 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.143× (z -17.1) |
| [[HCT15 (line)]] | alt | 121 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -10.6) |
| [[Hs 766T (line)]] | wt | 74.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -12.0) |
| [[HS-578T (line)]] | alt | 50.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 88.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -12.8) |
| [[J82 (line)]] | alt | 55.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -10.6) |
| [[KATO III (line)]] | alt | 93.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -15.7) |
| [[NCI-H2030 (line)]] | alt | 79.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.554× (z -9.7) |
| [[SHP-77 (line)]] | alt | 83.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -13.3) |
| [[SK-MEL-2 (line)]] | alt | 84.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.574× (z -8.9) |
| [[SW 1271 (line)]] | alt | 87.4 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0731× (z -10.8) |
| [[SW 900 (line)]] | alt | 66.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -12.6) |
| [[A-172 (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 83.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 91.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 70.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 74.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 74.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 85.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 93.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 87.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 57.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6236), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DTWD2]] | +0.64 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[SHPRH]] | +0.61 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[VWA8]] | +0.60 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[VPS36]] | +0.59 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[TSEN15]] | +0.58 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[MRPS9]] | +0.58 | +0.53 / +0.56 | both halves | 1e-05 | STRING 425 |
| [[CARNMT1]] | +0.57 | +0.42 / +0.67 | both halves | 4e-05 |  |
| [[MRPL19]] | +0.57 | +0.49 / +0.58 | both halves | 1e-05 | STRING 424 |
| [[TTC39C]] | +0.56 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[MRPL42]] | +0.56 | +0.36 / +0.62 | both halves | 1e-04 |  |
| [[IDE]] | +0.55 | +0.59 / +0.58 | both halves | 8e-06 |  |
| [[DCAF17]] | +0.55 | +0.47 / +0.61 | both halves | 2e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC10A3]] | -0.61 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[EPOR]] | -0.56 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[CATSPERG]] | -0.52 | -0.35 / -0.55 | both halves | 1e-04 |  |
| [[CYTH2]] | -0.52 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[WFDC3]] | -0.52 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[KCTD5]] | -0.51 | -0.39 / -0.50 | both halves | 6e-05 |  |
| [[MYL6]] | -0.51 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[LRRC8A]] | -0.51 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[ORMDL2]] | -0.50 | -0.33 / -0.52 | both halves | 1e-04 |  |
| [[SHPK]] | -0.50 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[ZNF324]] | -0.50 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[CDKL5]] | -0.50 | -0.40 / -0.46 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PPA2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NFIA]] | B | NFIA activity raises PPA2's level | lines that do not express NFIA (11) vs lines expressing it (39) | 1.53× lower at baseline in the lines without NFIA | 0.080 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, PCAT7; maybe low, not absent |
| [[NFIA]] | B | NFIA activity strengthens PPA2's drug response | lines that do not express NFIA (11) vs lines expressing it (39) | the lines without NFIA respond 0.53× as strongly (z diff +2.83); strongest at Belinostat 5 µM: 1.05x vs 0.72x (z diff +3.8) | 0.090 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, PCAT7; maybe low, not absent; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.430). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-28.3, -14.3); signed map (-10.6, -40.7). **Vector** length 117, 33.0% of its response variance represented; |z| ≥ 3 in 1,130 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.0 | +3.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.0 | +0.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.9 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +4.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.8 | +3.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +1.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | +4.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.8 | +1.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.1 | -26.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -7.7 | -13.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.2 | -11.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.3 | -7.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.9 | -9.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.7 | -2.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -3.1 | -3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -5.3 |
|  | [[vincristine (drug)]] 0.5 µM |  | -2.1 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | inorganic pyrophosphatase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q24 — chr4:105,369,077-105,474,067 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20459 |
| Gene groups (HGNC) | Inorganic pyrophosphatase family |
| Reactome | 4 pathways, smallest: Pyrophosphate hydrolysis; Mitochondrial tRNA aminoacylation; tRNA Aminoacylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H2U2](https://www.uniprot.org/uniprotkb/Q9H2U2) (Inorganic pyrophosphatase 2, mitochondrial):

> Hydrolyzes inorganic pyrophosphate. This activity is essential for correct regulation of mitochondrial membrane potential, and mitochondrial organization and function.

**Summary**, from NCBI Gene [27068](https://www.ncbi.nlm.nih.gov/gene/27068):

> The protein encoded by this gene is localized to the mitochondrion, is highly similar to members of the inorganic pyrophosphatase (PPase) family, and contains the signature sequence essential for the catalytic activity of PPase. PPases catalyze the hydrolysis of pyrophosphate to inorganic phosphate, which is important for the phosphate metabolism of cells. Alternate transcriptional splice variants, encoding different isoforms, have been characterized. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:28883](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28883) · Entrez [27068](https://www.ncbi.nlm.nih.gov/gene/27068) · UniProt [Q9H2U2](https://www.uniprot.org/uniprotkb/Q9H2U2) · Ensembl [ENSG00000138777](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138777)

## Data

Gene col 6236: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6236); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6236, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6236]; `tensor/DDL_lfc|DDL_z.npy` [6236]; `embed/gene_vectors.npy` [6236]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6236 or target_col == 6236). Every well: [[PPA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
