---
symbol: "PCDHGA2"
type: "gene"
col: 1327
ensembl_id: "ENSG00000081853"
name: "protocadherin gamma subfamily A, 2"
location: "5q31.3"
module: 13
arm: "+"
pooled_cpm: 34.55
n_lines_expressing: 43
n_dd_up: 1
n_dd_down: 40
n_dd_up_clean: 1
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 13
direction_downstream: 2
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# PCDHGA2

*protocadherin gamma subfamily A, 2* — 5q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[TAK-901 (drug)]] 0.05 µM: 1.40× (z +4.4, q 0.006, up in 20 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 5.83×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 40 drug-doses (17 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.366× (z -13.8, q 2e-40, down in 39 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC102B]] (+0.56, fdr 1e-05), [[PCDHGC3]] (+0.55, fdr 1e-05, ⚠ read-through risk), [[SETBP1]] (+0.53, fdr 1e-05), [[SDC2]] (+0.53, fdr 3e-05); moves opposite to [[LONRF1]] (-0.43, fdr 2e-04), [[DUSP22]] (-0.42, fdr 2e-04), [[GAN]] (-0.41, fdr 5e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[FRMD4A]] → it (grade B ⚠); 2 go from it, the strongest it → [[IHO1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1327.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 5.83×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 0.05 µM |  | **1.40×** | +4.4 | 0.006 | 20/40 (HEC-1-A, A-172, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.27× | +3.3 | 0.20 | 12/41 (MIA PaCa-2, RPMI-7951, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 1.27× | +3.3 | 0.20 | 12/41 (CFPAC-1, SNU-423, …) | inconsistent across doses |  |
| [[Omeprazole (drug)]] 5 µM |  | 1.26× | +3.2 | 0.21 | 11/41 (CFPAC-1, SNU-423, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | 1.24× | +3.0 | 0.30 | 8/41 (Panc 03.27, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 17 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 40 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1327.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.366×** | -13.8 | 2e-40 | 39/41 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.512×** | -12.9 | 7e-36 | 32/41 (SNU-423, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.453×** | -10.8 | 4e-25 | 37/41 (LOX-IMVI, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.476×** | -10.2 | 4e-22 | 36/41 (NCI-H460, RKO, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.490×** | -9.8 | 2e-20 | 38/41 (SW 1271, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.499×** | -9.1 | 6e-18 | 33/41 (NCI-H1792, SNU-423, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.546×** | -8.3 | 1e-14 | 28/41 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.547×** | -7.9 | 1e-13 | 29/40 (NCI-H23, LOX-IMVI, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.676×** | -7.5 | 3e-12 | 27/41 (Panc 03.27, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.601×** | -6.9 | 2e-10 | 25/41 (HS-578T, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.590×** | -6.9 | 2e-10 | 27/41 (C32, Panc 03.27, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.618×** | -6.6 | 2e-09 | 29/41 (SW480, AN3 CA, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.639×** | -6.1 | 4e-08 | 23/41 (AN3 CA, Panc 03.27, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.662×** | -5.6 | 8e-07 | 25/41 (SW 900, Hs 766T, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.679×** | -5.3 | 5e-06 | 24/41 (CFPAC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.669×** | -4.5 | 2e-04 | 26/41 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.721×** | -4.5 | 3e-04 | 20/41 (LOX-IMVI, SNU-1, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.793×** | -4.4 | 3e-04 | 23/41 (A-172, H4, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.736×** | -4.2 | 8e-04 | 21/41 (SW 1088, C32, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.579×** | -3.9 | 0.002 | 17/41 (NCI-H460, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.758×** | -3.6 | 0.008 | 18/41 (AN3 CA, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.762×** | -3.6 | 0.008 | 16/41 (MIA PaCa-2, LOX-IMVI, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.611×** | -3.5 | 0.009 | 16/41 (C32, NCI-H23, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.41 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1327. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 26.4 | 0 | 7 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.197× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.151× (z -12.3) |
| [[LOX-IMVI (line)]] | wt | 52.4 | 0 | 6 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.116× (z -15.1) |
| [[Panc 03.27 (line)]] | alt | 85.8 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -20.3) |
| [[PANC-1 (line)]] | alt | 22.6 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.234× (z -11.6) |
| [[SW 900 (line)]] | alt | 94.9 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -11.3) |
| [[Hs 766T (line)]] | wt | 46.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -15.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -12.9) |
| [[A-427 (line)]] | wt | 20.4 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.135× (z -13.2) |
| [[C32 (line)]] | wt | 90.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -15.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -11.0) |
| [[LoVo (line)]] | wt | 12.6 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.83× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 5 µM 0.166× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.199× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 18.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -12.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.173× (z -10.8) |
| [[RPMI-7951 (line)]] | alt | 134 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -15.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -10.0) |
| [[SNU-1 (line)]] | wt | 27.8 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.210× (z -11.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.127× (z -10.3) |
| [[SNU-423 (line)]] | alt | 110 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -18.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -8.7) |
| [[A-172 (line)]] | wt | 59.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -16.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.301× (z -9.8) |
| [[A498 (line)]] | wt | 74.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -11.2) ⚠ cell-cycle shift, explains ~27% of this change |
| [[AN3 CA (line)]] | alt | 79.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.162× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 48.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -11.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -9.0) |
| [[H4 (line)]] | wt | 61.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0924× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 24.4 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.1000× (z -14.6) ⚠ toxic; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -10.9) |
| [[SW480 (line)]] | alt | 13.5 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.243× (z -9.9) |
| [[AsPC-1 (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -9.4) ⚠ cell-cycle shift, explains ~27% of this change |
| [[BT-474 (line)]] | alt | 18.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.155× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[hTERT-HPNE (line)]] | wt | 55.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -15.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H1792 (line)]] | alt | 23.0 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.135× (z -11.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H2030 (line)]] | alt | 49.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -8.5) |
| [[RKO (line)]] | wt | 23.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.149× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SK-MEL-2 (line)]] | alt | 83.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -10.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW 1271 (line)]] | alt | 53.1 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0729× (z -9.1) |
| [[A549 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.88 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.08 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.54 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.91 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.63 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 91.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.77 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.03 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1327), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC102B]] | +0.56 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[PCDHGC3]] | +0.55 | +0.52 / +0.56 | both halves | 1e-05 | same gene group; ⚠ **readthrough risk**: PCDHGC3 lies 0.0 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[SETBP1]] | +0.53 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[SDC2]] | +0.53 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[LINC01013]] | +0.51 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[RHOJ]] | +0.50 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[DCTN4]] | +0.50 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[TCF4]] | +0.49 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[LAMA4]] | +0.49 | +0.39 / +0.41 | both halves | 5e-05 |  |
| [[ADAMTS12]] | +0.49 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[PDE3A]] | +0.49 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[CTHRC1]] | +0.48 | +0.41 / +0.43 | both halves | 4e-05 |  |
| [[COL15A1]] | +0.48 | +0.46 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LONRF1]] | -0.43 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[DUSP22]] | -0.42 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[GAN]] | -0.41 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[REPS2]] | -0.41 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[TMEM125]] | -0.39 | -0.39 / -0.31 | both halves | 2e-04 |  |
| [[SLC15A2]] | -0.39 | -0.38 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 13, C 0. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FRMD4A]] | B | FRMD4A activity raises PCDHGA2's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 2.72× lower at baseline in the lines without FRMD4A | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6 |
| [[PCDHGC3]] | B | PCDHGC3 activity raises PCDHGA2's level | lines that do not express PCDHGC3 (18) vs lines expressing it (32) | 3.55× lower at baseline in the lines without PCDHGC3 | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, ITGB3, EGFEM1P |
| [[LINC02813]] | B | LINC02813 activity raises PCDHGA2's level | lines that do not express LINC02813 (26) vs lines expressing it (24) | 2.30× lower at baseline in the lines without LINC02813 | 0.038 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, ENSG00000260517, CUBN |
| [[EHD3]] | B | EHD3 activity raises PCDHGA2's level | lines that do not express EHD3 (14) vs lines expressing it (36) | 2.78× lower at baseline in the lines without EHD3 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: MAP9, EVC, AKR1B1 |
| [[ANTXR1]] | B | ANTXR1 activity raises PCDHGA2's level | lines that do not express ANTXR1 (17) vs lines expressing it (33) | 2.89× lower at baseline in the lines without ANTXR1 | 0.069 | ⚠ within organs, on part of the lines; also absent: VASH1, RFLNB, ENSG00000285804 |
| [[ZNF883]] | B | ZNF883 activity raises PCDHGA2's level | lines that do not express ZNF883 (22) vs lines expressing it (28) | 2.15× lower at baseline in the lines without ZNF883 | 0.069 | ⚠ within organs, on part of the lines; also absent: AK5, SOX5, GAP43 |
| [[ARHGEF6]] | B | ARHGEF6 activity raises PCDHGA2's level | lines that do not express ARHGEF6 (20) vs lines expressing it (30) | 2.23× lower at baseline in the lines without ARHGEF6 | 0.073 | ⚠ within organs, on part of the lines; also absent: SRPX, MSRB3, ENSG00000230615; maybe low, not absent |
| [[TRIM9]] | B | TRIM9 activity raises PCDHGA2's level | lines that do not express TRIM9 (16) vs lines expressing it (34) | 2.65× lower at baseline in the lines without TRIM9 | 0.083 | ⚠ within organs, on part of the lines; also absent: NRG1, DPYSL3, WIPF1 |
| [[ITGA11]] | B | ITGA11 activity raises PCDHGA2's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 2.13× lower at baseline in the lines without ITGA11 | 0.083 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411 |
| [[ZNF354C]] | B | ZNF354C activity raises PCDHGA2's level | lines that do not express ZNF354C (23) vs lines expressing it (27) | 2.27× lower at baseline in the lines without ZNF354C | 0.085 | ⚠ within organs, on part of the lines; also absent: CPEB1, MPDZ, NALCN |
| [[ATRNL1]] | B | ATRNL1 activity raises PCDHGA2's level | lines that do not express ATRNL1 (21) vs lines expressing it (29) | 2.28× lower at baseline in the lines without ATRNL1 | 0.091 | ⚠ within organs, on part of the lines; also absent: CAMK4, BVES, NEGR1; maybe low, not absent |
| [[ZNF385D]] | B | ZNF385D activity raises PCDHGA2's level | lines that do not express ZNF385D (25) vs lines expressing it (25) | 2.29× lower at baseline in the lines without ZNF385D | 0.094 | ⚠ within organs, on part of the lines; also absent: ARMCX1, LINC03047, ITGA4; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IHO1]] | B | PCDHGA2 activity raises IHO1's level | lines that do not express PCDHGA2 (7) vs lines expressing it (43) | 1.15× lower at baseline in the lines without PCDHGA2 | 0.014 | ⚠ within organs, on part of the lines; also absent: ZNF134, SYDE1, SIX1; maybe low, not absent |
| [[LINC01013]] | B | PCDHGA2 activity raises LINC01013's level | lines that do not express PCDHGA2 (7) vs lines expressing it (43) | 1.80× lower at baseline in the lines without PCDHGA2 | 0.033 | ⚠ within organs, on part of the lines; also absent: ZNF134, SYDE1, SIX1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.500). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (55.1, 19.7); signed map (27.5, 42.1). **Vector** length 79.0, 18.4% of its response variance represented; |z| ≥ 3 in 1,027 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.5 | +1.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.3 | -0.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.1 | +0.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | -2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | -0.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.3 | +4.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.5 | +3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | -4.2 |
| fall | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.4 | -4.4 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -2.9 | -3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.6 | -3.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.3 | -3.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.1 | -3.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.1 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | protocadherin gamma subfamily A, 2 |
| Locus type | complex locus constituent (other) |
| Location | 5q31.3 — chr5:141,338,760-141,512,975 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PCDH-GAMMA-A2 |
| Gene groups (HGNC) | Clustered protocadherins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5H1](https://www.uniprot.org/uniprotkb/Q9Y5H1) (Protocadherin gamma-A2):

> Potential calcium-dependent cell-adhesion protein. May be involved in the establishment and maintenance of specific neuronal connections in the brain.

**Summary**, from NCBI Gene [56113](https://www.ncbi.nlm.nih.gov/gene/56113):

> This gene is a member of the protocadherin gamma gene cluster, one of three related clusters tandemly linked on chromosome five. These gene clusters have an immunoglobulin-like organization, suggesting that a novel mechanism may be involved in their regulation and expression. The gamma gene cluster includes 22 genes divided into 3 subfamilies. Subfamily A contains 12 genes, subfamily B contains 7 genes and 2 pseudogenes, and the more distantly related subfamily C contains 3 genes. The tandem …

**Accessions** — [HGNC:8700](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8700) · Entrez [56113](https://www.ncbi.nlm.nih.gov/gene/56113) · UniProt [Q9Y5H1](https://www.uniprot.org/uniprotkb/Q9Y5H1) · Ensembl [ENSG00000081853](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000081853)

## Data

Gene col 1327: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1327); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1327, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1327]; `tensor/DDL_lfc|DDL_z.npy` [1327]; `embed/gene_vectors.npy` [1327]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1327 or target_col == 1327). Every well: [[PCDHGA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCDHGA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
