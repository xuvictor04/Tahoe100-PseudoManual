---
symbol: "PTP4A2"
type: "gene"
col: 11481
ensembl_id: "ENSG00000184007"
name: "protein tyrosine phosphatase 4A2"
location: "1p35.2"
module: 45
arm: "+"
pooled_cpm: 246.77
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 13
n_dd_up_clean: 2
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# PTP4A2

*protein tyrosine phosphatase 4A2* — 1p35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.78× (z +8.4, q 2e-14, up in 41 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.10× (z +6.3, q 5e-08, up in 40 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Niclosamide (olamine) (drug)]] 5 µM in 4 lines (AsPC-1 2.41×, COLO 205 2.87×, LS 180 2.61×, LoVo 2.61×; ⚠ toxic); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SW480 2.95×, KATO III 2.64×, A-427 2.77×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (KATO III 2.53×, SW480 2.38×; ⚠ toxic; transcription drop); [[TAK-901 (drug)]] 5 µM in 1 line (RKO 4.17×).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.651× (z -9.8, q 6e-20, down in 39 of 49 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KHDRBS1]] (+0.60, fdr 4e-05), [[CFD]] (+0.56, fdr 3e-04), [[TMEM185A]] (+0.56, fdr 7e-05); moves opposite to [[RCC1L]] (-0.62, fdr 8e-05), [[RPAP1]] (-0.59, fdr 3e-05), [[ITPA]] (-0.59, fdr 1e-04).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PPP1R14A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11481.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Niclosamide (olamine) (drug)]] 5 µM in 4 lines (AsPC-1 2.41×, COLO 205 2.87×, LS 180 2.61×, LoVo 2.61×; ⚠ toxic); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SW480 2.95×, KATO III 2.64×, A-427 2.77×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (KATO III 2.53×, SW480 2.38×; ⚠ toxic; transcription drop); [[TAK-901 (drug)]] 5 µM in 1 line (RKO 4.17×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.78×** | +8.4 | 2e-14 | 41/49 (SW480, KATO III, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +8.4 | 2e-14 | 43/47 (AsPC-1, COLO 205, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.69×** | +7.8 | 1e-12 | 40/45 (SW480, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.10×** | +6.3 | 5e-08 | 40/49 (RKO, AsPC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +5.8 | 8e-07 | 33/44 (KATO III, SW480, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~59% of this change | **1.31×** | +4.3 | 0.002 | 32/48 (RPMI-7951, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.026 | 28/48 (SNU-1, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.24×** | +3.5 | 0.029 | 27/48 (NCI-H460, KATO III, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.22×** | +3.2 | 0.074 | 29/48 (NCI-H2347, SNU-423, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11481.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.651×** | -9.8 | 6e-20 | 39/49 (MIA PaCa-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.662×** | -6.7 | 8e-09 | 40/48 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.757×** | -6.4 | 4e-08 | 34/48 (HOP62, A549, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.802×** | -5.0 | 6e-05 | 26/48 (A549, COLO 205, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.803×** | -5.0 | 6e-05 | 24/48 (AN3 CA, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.734×** | -4.8 | 2e-04 | 33/48 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.779×** | -4.0 | 0.004 | 33/49 (A549, PANC-1, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | **0.794×** | -3.7 | 0.014 | 31/48 (Hs 766T, A549, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.794×** | -3.3 | 0.051 | 24/48 (MIA PaCa-2, LoVo, …) | two highest doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.816×** | -3.3 | 0.060 | 25/48 (A549, Hs 766T, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.809×** | -3.1 | 0.098 | 27/48 (SK-MEL-2, MIA PaCa-2, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.820×** | -3.1 | 0.098 | 25/50 (LS 180, COLO 205, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.827×** | -3.1 | 0.098 | 19/48 (A549, HS-578T, …) | two highest doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | 0.699× | -3.0 | 0.10 | 22/50 (HEC-1-A, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11481. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 208 | 6 (6 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 3.02× (z +12.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -10.4) |
| [[KATO III (line)]] | alt | 212 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.53× (z +12.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.636× (z -8.6) |
| [[LS 180 (line)]] | wt | 266 | 3 (3 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 2.61× (z +12.1) ⚠ toxic | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -15.0) |
| [[HOP62 (line)]] | alt | 285 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 2.25× (z +9.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.595× (z -9.3) |
| [[PANC-1 (line)]] | alt | 481 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -13.3) |
| [[SW480 (line)]] | alt | 190 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +13.3) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 233 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +10.9) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 240 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -12.8) |
| [[AsPC-1 (line)]] | alt | 270 | 2 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.41× (z +12.5) ⚠ toxic | — |
| [[COLO 205 (line)]] | alt | 215 | 1 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 2.87× (z +12.3) ⚠ toxic | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.537× (z -10.7) |
| [[LoVo (line)]] | wt | 217 | 1 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 2.61× (z +11.4) ⚠ toxic | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.561× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 173 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.58× (z +9.8) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 559 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.206× (z -26.1) |
| [[NCI-H1792 (line)]] | alt | 263 | 1 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 2.50× (z +9.2) ⚠ toxic | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -11.1) |
| [[NCI-H23 (line)]] | alt | 338 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -16.5) |
| [[Panc 03.27 (line)]] | alt | 266 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.592× (z -9.3) |
| [[RKO (line)]] | wt | 181 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 4.17× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.596× (z -8.6) |
| [[SHP-77 (line)]] | alt | 207 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.51× (z +10.9) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 346 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -17.5) |
| [[C-33 A (line)]] | alt | 130 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +8.5) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 266 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.509× (z -12.0) |
| [[H4 (line)]] | wt | 181 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -10.7) |
| [[HCT15 (line)]] | alt | 217 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 317 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.594× (z -8.7) |
| [[Hs 766T (line)]] | wt | 342 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.561× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 198 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.561× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 146 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.66× (z +9.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 332 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -10.8) |
| [[SW 1271 (line)]] | alt | 173 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.225× (z -8.5) ⚠ transcription drop; cell-cycle shift, explains ~59% of this change |
| [[A-172 (line)]] | wt | 148 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 215 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 150 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 92.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 167 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 306 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 245 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 227 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 263 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 240 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 237 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 139 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 244 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 223 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 117 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11481), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KHDRBS1]] | +0.60 | +0.58 / +0.43 | both halves | 4e-05 |  |
| [[CFD]] | +0.56 | +0.45 / +0.28 | both halves | 3e-04 |  |
| [[TMEM185A]] | +0.56 | +0.54 / +0.38 | both halves | 7e-05 |  |
| [[PJA2]] | +0.56 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[MED30]] | +0.56 | +0.59 / +0.38 | both halves | 6e-05 |  |
| [[SLC25A23]] | +0.55 | +0.56 / +0.28 | both halves | 3e-04 |  |
| [[ATP2A3]] | +0.55 | +0.35 / +0.36 | both halves | 1e-04 |  |
| [[GTF2IP4]] | +0.55 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[SPOPL]] | +0.55 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[SNX1]] | +0.54 | +0.60 / +0.30 | both halves | 2e-04 |  |
| [[ARL6]] | +0.53 | +0.48 / +0.26 | both halves | 4e-04 |  |
| [[SEC11A]] | +0.53 | +0.53 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RCC1L]] | -0.62 | -0.55 / -0.37 | both halves | 8e-05 |  |
| [[RPAP1]] | -0.59 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[ITPA]] | -0.59 | -0.58 / -0.34 | both halves | 1e-04 |  |
| [[CDK12]] | -0.58 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[ZNF124]] | -0.57 | -0.63 / -0.28 | both halves | 3e-04 |  |
| [[TRMT5]] | -0.55 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[CPSF2]] | -0.55 | -0.55 / -0.34 | both halves | 1e-04 |  |
| [[SNX5]] | -0.54 | -0.56 / -0.31 | both halves | 2e-04 |  |
| [[AVEN]] | -0.54 | -0.52 / -0.25 | both halves | 4e-04 |  |
| [[METTL8]] | -0.53 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[DNAJC11]] | -0.53 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[NIP7]] | -0.53 | -0.55 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPP1R14A]] | B | PPP1R14A activity raises PTP4A2's level | lines that do not express PPP1R14A (39) vs lines expressing it (11) | 1.40× lower at baseline in the lines without PPP1R14A | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMRN1, GCG, SFTPA2 |
| [[TOP2A]] | B | TOP2A activity raises PTP4A2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.566). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-0.8, 6.0); signed map (-30.3, -5.6). **Vector** length 115, 41.5% of its response variance represented; |z| ≥ 3 in 1,157 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +6.0 | +0.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.5 | -0.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.1 | +0.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | -2.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.1 | +8.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.9 | -0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | -0.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +0.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.6 | +0.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.3 | +0.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.8 | -9.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -7.0 | -6.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.9 | -1.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.7 | -1.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -5.5 | -6.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -1.8 |
|  | [[Budesonide (drug)]] 0.5 µM |  | -3.2 | -0.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.0 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | protein tyrosine phosphatase 4A2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.2 — chr1:31,906,421-31,944,856 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HU-PP-1, PTPCAAX2, OV-1, ptp-IV1a, PRL-2, PRL2; previously PTP4A |
| Gene groups (HGNC) | Protein tyrosine phosphatase 4A family |
| Reactome | 1 pathways, smallest: RAB geranylgeranylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12974](https://www.uniprot.org/uniprotkb/Q12974) (Protein tyrosine phosphatase type IVA 2):

> Protein tyrosine phosphatase which stimulates progression from G1 into S phase during mitosis. Promotes tumors. Inhibits geranylgeranyl transferase type II activity by blocking the association between RABGGTA and RABGGTB.

**Summary**, from NCBI Gene [8073](https://www.ncbi.nlm.nih.gov/gene/8073):

> The protein encoded by this gene belongs to a small class of the protein tyrosine phosphatase (PTP) family. PTPs are cell signaling molecules that play regulatory roles in a variety of cellular processes. PTPs in this class contain a protein tyrosine phosphatase catalytic domain and a characteristic C-terminal prenylation motif. This PTP has been shown to primarily associate with plasmic and endosomal membrane through its C-terminal prenylation. This PTP was found to interact with the …

**Accessions** — [HGNC:9635](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9635) · Entrez [8073](https://www.ncbi.nlm.nih.gov/gene/8073) · UniProt [Q12974](https://www.uniprot.org/uniprotkb/Q12974) · Ensembl [ENSG00000184007](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184007)

## Data

Gene col 11481: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11481); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11481, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11481]; `tensor/DDL_lfc|DDL_z.npy` [11481]; `embed/gene_vectors.npy` [11481]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11481 or target_col == 11481). Every well: [[PTP4A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTP4A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
