---
symbol: "TTC28"
type: "gene"
col: 1882
ensembl_id: "ENSG00000100154"
name: "tetratricopeptide repeat domain 28"
location: "22q12.1"
module: 207
arm: "-"
pooled_cpm: 176.59
n_lines_expressing: 35
n_dd_up: 0
n_dd_down: 27
n_dd_up_clean: 0
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 20
direction_downstream: 38
tags: ["gene", "module/207"]
generated_by: "tahoemap"
---

# TTC28

*tetratricopeptide repeat domain 28* — 22q12.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (HOP62 2.95×; ⚠ cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (HOP62 2.84×; ⚠ cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (HOP62 2.66×; ⚠ cell-cycle shift, would explain all of this change); [[Tucidinostat (drug)]] 5 µM in 1 line (BT-474 2.60×).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (14 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.322× (z -22.0, q 0e+00, down in 33 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTC7B]] (+0.54, fdr 1e-05), [[BNC2]] (+0.54, fdr 2e-05), [[NBEA]] (+0.54, fdr 1e-05); moves opposite to [[ARHGAP1]] (-0.51, fdr 3e-05), [[INAVA]] (-0.51, fdr 2e-05), [[MYO7B]] (-0.51, fdr 2e-05).
> It sits in the **-** arm of [[Module 207]].
> Probable direction (from the cell lines, not proof of direct regulation): 20 arrows point to it, the strongest [[ST14]] → it (grade B ⚠); 38 go from it, the strongest it → [[ESRP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1882.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (HOP62 2.95×; ⚠ cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (HOP62 2.84×; ⚠ cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (HOP62 2.66×; ⚠ cell-cycle shift, would explain all of this change); [[Tucidinostat (drug)]] 5 µM in 1 line (BT-474 2.60×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bimiralisib (drug)]] 5 µM |  | 1.65× | +3.6 | 0.13 | 23/35 (MIA PaCa-2, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 1.29× | +3.5 | 0.13 | 17/34 (BT-474, HOP62, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 5 µM |  | 1.57× | +3.2 | 0.18 | 21/34 (HS-578T, HOP62, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.28× | +3.2 | 0.18 | 18/32 (MIA PaCa-2, A549, …) | rises with dose |  |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.26× | +3.1 | 0.19 | 17/33 (RPMI-7951, SW 900, …) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | 1.54× | +3.1 | 0.19 | 21/33 (HS-578T, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 14 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1882.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.322×** | -22.0 | 0e+00 | 33/34 (NCI-H23, C-33 A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.323×** | -14.9 | 0e+00 | 29/30 (SNU-1, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.508×** | -13.2 | 2e-37 | 26/33 (NCI-H1792, NCI-H23, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.387×** | -12.6 | 5e-34 | 30/32 (MIA PaCa-2, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.454×** | -10.5 | 2e-23 | 30/35 (SW 900, C-33 A, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.448×** | -10.2 | 2e-22 | 28/31 (C-33 A, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.469×** | -10.0 | 1e-21 | 31/33 (NCI-H23, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.499×** | -9.6 | 8e-20 | 28/33 (NCI-H460, MIA PaCa-2, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.516×** | -9.1 | 5e-18 | 29/33 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.524×** | -8.9 | 3e-17 | 25/33 (MIA PaCa-2, NCI-H460, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.406×** | -8.2 | 8e-15 | 28/34 (C-33 A, SNU-1, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.546×** | -8.0 | 6e-14 | 26/33 (C32, A-427, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | **0.609×** | -6.6 | 2e-09 | 27/32 (NCI-H23, MIA PaCa-2, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.416×** | -6.3 | 1e-08 | 25/34 (SNU-1, C-33 A, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | **0.663×** | -5.7 | 6e-07 | 26/33 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.690×** | -5.1 | 1e-05 | 20/33 (C32, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.777×** | -4.9 | 3e-05 | 20/33 (SNU-423, NCI-H661, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.759×** | -3.8 | 0.004 | 22/34 (SNU-423, NCI-H1792, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.593×** | -3.8 | 0.005 | 19/33 (SNU-1, C-33 A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.594×** | -3.8 | 0.005 | 25/33 (J82, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | **0.768×** | -3.6 | 0.007 | 21/33 (SW 900, NCI-H1792, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.769×** | -3.6 | 0.007 | 17/33 (C-33 A, Hs 766T, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.780×** | -3.3 | 0.022 | 19/33 (SW 900, A-172, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.782×** | -3.1 | 0.036 | 19/32 (RKO, hTERT-HPNE, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.47 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1882. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 245 | 0 | 14 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -23.2) |
| [[MIA PaCa-2 (line)]] | alt | 356 | 0 | 12 (9 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0647× (z -26.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -19.9) |
| [[A498 (line)]] | wt | 295 | 0 | 10 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -18.0) |
| [[C-33 A (line)]] | alt | 769 | 0 | 10 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -22.8) |
| [[NCI-H2030 (line)]] | alt | 532 | 0 | 10 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -20.7) |
| [[SNU-1 (line)]] | wt | 557 | 0 | 10 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0969× (z -24.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -19.6) |
| [[SNU-423 (line)]] | alt | 192 | 0 | 9 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.233× (z -17.7) |
| [[SW 900 (line)]] | alt | 341 | 0 | 9 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -19.7) |
| [[A-427 (line)]] | wt | 150 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.335× (z -11.6) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -11.4) |
| [[C32 (line)]] | wt | 171 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -13.3) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.249× (z -12.9) |
| [[NCI-H460 (line)]] | wt | 437 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -20.3) |
| [[NCI-H1792 (line)]] | alt | 385 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -21.5) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -20.1) |
| [[PANC-1 (line)]] | alt | 276 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -19.1) |
| [[A549 (line)]] | wt | 296 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -17.6) |
| [[AN3 CA (line)]] | alt | 382 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -14.0) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -12.1) |
| [[HOP62 (line)]] | alt | 114 | 4 (4 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.95× (z +11.8) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -11.5) |
| [[HepG2_C3A (line)]] | wt | 338 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -17.7) |
| [[Hs 766T (line)]] | wt | 240 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -12.4) |
| [[HS-578T (line)]] | alt | 233 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -13.6) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -12.1) |
| [[hTERT-HPNE (line)]] | wt | 207 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -14.3) |
| [[LOX-IMVI (line)]] | wt | 133 | 0 | 4 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.233× (z -14.6) |
| [[NCI-H1573 (line)]] | alt | 130 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -17.5) |
| [[RKO (line)]] | wt | 58.5 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.245× (z -11.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.309× (z -9.7) |
| [[A-172 (line)]] | wt | 69.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.274× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[BT-474 (line)]] | alt | 59.9 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.60× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -11.2) ⚠ cell-cycle shift, explains ~38% of this change |
| [[J82 (line)]] | alt | 165 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -16.2) |
| [[RPMI-7951 (line)]] | alt | 129 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -9.7) |
| [[SHP-77 (line)]] | alt | 248 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -15.6) |
| [[SK-MEL-2 (line)]] | alt | 151 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.248× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[SW 1271 (line)]] | alt | 177 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.154× (z -8.9) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.282× (z -8.8) |
| [[CHP-212 (line)]] | wt | 148 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -8.9) |
| [[NCI-H661 (line)]] | alt | 427 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.219× (z -11.0) |
| [[AsPC-1 (line)]] | alt | 15.3 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 30.6 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 15.2 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 33.9 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 25.9 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 19.5 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 21.1 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 16.0 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 14.2 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 13.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 34.2 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.0 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.1 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 18.8 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 26.9 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1882), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC7B]] | +0.54 | +0.50 / +0.53 | both halves | 1e-05 | same gene group |
| [[BNC2]] | +0.54 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[NBEA]] | +0.54 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[NINL]] | +0.54 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[MPDZ]] | +0.52 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[CASC15]] | +0.49 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[DENND5B]] | +0.49 | +0.56 / +0.37 | both halves | 8e-05 |  |
| [[MMP16]] | +0.49 | +0.38 / +0.46 | both halves | 6e-05 |  |
| [[RAB31]] | +0.49 | +0.48 / +0.39 | both halves | 6e-05 |  |
| [[MIR99AHG]] | +0.49 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[SNCA]] | +0.48 | +0.44 / +0.43 | both halves | 3e-05 |  |
| [[LINC01203]] | +0.48 | +0.35 / +0.54 | both halves | 1e-04 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP1]] | -0.51 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[INAVA]] | -0.51 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[MYO7B]] | -0.51 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[LASTR]] | -0.51 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[TLDC2]] | -0.49 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[FUT3]] | -0.49 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[TMC4]] | -0.47 | -0.46 / -0.46 | both halves | 2e-05 |  |
| [[ESRP1]] | -0.46 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[APAF1]] | -0.44 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[EPS8L3]] | -0.44 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[TMEM125]] | -0.44 | -0.40 / -0.37 | both halves | 8e-05 |  |
| [[KLHL28]] | -0.44 | -0.53 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 17, C 3. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ST14]] | B | ST14 activity lowers TTC28's level | lines that do not express ST14 (32) vs lines expressing it (18) | 7.02× higher at baseline in the lines without ST14 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |
| [[ESRP1]] | B | ESRP1 activity lowers TTC28's level | lines that do not express ESRP1 (31) vs lines expressing it (19) | 6.54× higher at baseline in the lines without ESRP1 | 3e-04 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7 |
| [[CDH1]] | B | CDH1 activity lowers TTC28's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 6.10× higher at baseline in the lines without CDH1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[INAVA]] | B | INAVA activity lowers TTC28's level | lines that do not express INAVA (29) vs lines expressing it (21) | 4.58× higher at baseline in the lines without INAVA | 0.001 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[B3GNT3]] | B | B3GNT3 activity lowers TTC28's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 4.53× higher at baseline in the lines without B3GNT3 | 0.001 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[TMEM125]] | B | TMEM125 activity lowers TTC28's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 6.25× higher at baseline in the lines without TMEM125 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14 |
| [[ADCY4]] | B | ADCY4 activity lowers TTC28's level | lines that do not express ADCY4 (33) vs lines expressing it (17) | 3.97× higher at baseline in the lines without ADCY4 | 0.013 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, CLIC5 |
| [[GALNT3]] | B | GALNT3 activity lowers TTC28's level | lines that do not express GALNT3 (30) vs lines expressing it (20) | 4.25× higher at baseline in the lines without GALNT3 | 0.013 | ⚠ within organs, on part of the lines; also absent: TMEM125, GRHL2, SKAP1 |
| [[SLC5A1]] | B | SLC5A1 activity lowers TTC28's level | lines that do not express SLC5A1 (36) vs lines expressing it (14) | 5.21× higher at baseline in the lines without SLC5A1 | 0.015 | ⚠ within organs, on part of the lines; also absent: TMEM30B, TMPRSS2, TMEM125 |
| [[FUT3]] | B | FUT3 activity lowers TTC28's level | lines that do not express FUT3 (29) vs lines expressing it (21) | 3.39× higher at baseline in the lines without FUT3 | 0.016 | ⚠ within organs, on part of the lines; also absent: ATP2C2, TMEM125, ENSG00000243004 |
| [[ARHGEF38]] | B | ARHGEF38 activity lowers TTC28's level | lines that do not express ARHGEF38 (36) vs lines expressing it (14) | 5.07× higher at baseline in the lines without ARHGEF38 | 0.022 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, TMEM125, SLC5A1 |
| [[HSD17B2]] | B | HSD17B2 activity lowers TTC28's level | lines that do not express HSD17B2 (35) vs lines expressing it (15) | 3.22× higher at baseline in the lines without HSD17B2 | 0.030 | ⚠ within organs, on part of the lines; also absent: KRT23, S100P, TFF2 |

### Downstream of this gene

*38 arrows, 38 of them with an alert ⚠; grade A 0, B 34, C 4. Shown: the 12 strongest; 26 more arrows (26 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ESRP1]] | B | TTC28 activity lowers ESRP1's level | lines that do not express TTC28 (15) vs lines expressing it (35) | 13.97× higher at baseline in the lines without TTC28 | 2e-04 | ⚠ within organs, on part of the lines; also absent: SAMD11, RASSF8-AS1, AOX1 |
| [[ST14]] | B | TTC28 activity lowers ST14's level | lines that do not express TTC28 (15) vs lines expressing it (35) | 14.83× higher at baseline in the lines without TTC28 | 4e-04 | ⚠ within organs, on part of the lines; also absent: SAMD11, RASSF8-AS1, AOX1 |
| [[TMC4]] | B | TTC28 activity lowers TMC4's level | lines that do not express TTC28 (15) vs lines expressing it (35) | 7.26× higher at baseline in the lines without TTC28 | 4e-04 | ⚠ within organs, on part of the lines; also absent: SAMD11, RASSF8-AS1, AOX1 |
| [[INAVA]] | B | TTC28 activity lowers INAVA's level | lines that do not express TTC28 (15) vs lines expressing it (35) | 8.47× higher at baseline in the lines without TTC28 | 5e-04 | ⚠ within organs, on part of the lines; also absent: SAMD11, RASSF8-AS1, AOX1 |
| [[CDH1]] | B | TTC28 activity lowers CDH1's level | lines that do not express TTC28 (15) vs lines expressing it (35) | 12.62× higher at baseline in the lines without TTC28 | 6e-04 | ⚠ within organs, on part of the lines; also absent: SAMD11, RASSF8-AS1, AOX1 |
| [[ANXA11]] | B | TTC28 activity lowers ANXA11's level | lines that do not express TTC28 (15) vs lines expressing it (35) | 3.83× higher at baseline in the lines without TTC28 | 0.001 | ⚠ within organs, on part of the lines; also absent: SAMD11, RASSF8-AS1, AOX1 |
| [[B3GNT3]] | B | TTC28 activity lowers B3GNT3's level | lines that do not express TTC28 (15) vs lines expressing it (35) | 7.60× higher at baseline in the lines without TTC28 | 0.001 | ⚠ within organs, on part of the lines; also absent: SAMD11, RASSF8-AS1, AOX1 |
| [[GALNT3]] | B | TTC28 activity lowers GALNT3's level | lines that do not express TTC28 (15) vs lines expressing it (35) | 7.03× higher at baseline in the lines without TTC28 | 0.005 | ⚠ within organs, on part of the lines; also absent: SAMD11, RASSF8-AS1, AOX1 |
| [[ZNF8]] | B | TTC28 activity raises ZNF8's level | lines that do not express TTC28 (15) vs lines expressing it (35) | 1.41× lower at baseline in the lines without TTC28 | 0.005 | ⚠ within organs, on part of the lines; also absent: SAMD11, RASSF8-AS1, AOX1 |
| [[TMEM125]] | B | TTC28 activity lowers TMEM125's level | lines that do not express TTC28 (15) vs lines expressing it (35) | 3.88× higher at baseline in the lines without TTC28 | 0.006 | ⚠ within organs, on part of the lines; also absent: SAMD11, RASSF8-AS1, AOX1 |
| [[GPR35]] | B | TTC28 activity lowers GPR35's level | lines that do not express TTC28 (15) vs lines expressing it (35) | 4.87× higher at baseline in the lines without TTC28 | 0.015 | ⚠ within organs, on part of the lines; also absent: SAMD11, RASSF8-AS1, AOX1 |
| [[TLDC2]] | B | TTC28 activity lowers TLDC2's level | lines that do not express TTC28 (15) vs lines expressing it (35) | 2.68× higher at baseline in the lines without TTC28 | 0.015 | ⚠ within organs, on part of the lines; also absent: SAMD11, RASSF8-AS1, AOX1 |

## Where it sits

- **Module**: [[Module 207]]; 15 genes; this gene is in the **-** arm (projection on the module's main direction -0.466). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (31.3, 30.3); signed map (29.1, 32.9). **Vector** length 109, 36.4% of its response variance represented; |z| ≥ 3 in 950 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.3 | -3.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.8 | -0.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.7 | +0.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.7 | -0.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.2 | -1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.9 | +0.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | +1.2 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.4 | -10.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.7 | -10.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.4 | -2.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.2 | -6.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.1 | -3.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.0 | -3.8 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.9 | -2.8 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | -1.9 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | tetratricopeptide repeat domain 28 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.1 — chr22:27,978,014-28,679,840 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1043 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96AY4](https://www.uniprot.org/uniprotkb/Q96AY4) (Tetratricopeptide repeat protein 28):

> During mitosis, may be involved in the condensation of spindle midzone microtubules, leading to the formation of midbody.

**Summary**, from NCBI Gene [23331](https://www.ncbi.nlm.nih.gov/gene/23331):

> Enables kinase binding activity. Involved in regulation of mitotic cell cycle. Located in midbody. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29179](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29179) · Entrez [23331](https://www.ncbi.nlm.nih.gov/gene/23331) · UniProt [Q96AY4](https://www.uniprot.org/uniprotkb/Q96AY4) · Ensembl [ENSG00000100154](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100154)

## Data

Gene col 1882: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1882); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1882, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1882]; `tensor/DDL_lfc|DDL_z.npy` [1882]; `embed/gene_vectors.npy` [1882]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1882 or target_col == 1882). Every well: [[TTC28 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTC28.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
