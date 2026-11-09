---
symbol: "FMNL1"
type: "gene"
col: 11591
ensembl_id: "ENSG00000184922"
name: "formin like 1"
location: "17q21.31"
module: 13
arm: "+"
pooled_cpm: 18.85
n_lines_expressing: 32
n_dd_up: 8
n_dd_down: 24
n_dd_up_clean: 2
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 5
direction_downstream: 5
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# FMNL1

*formin like 1* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.56× (z +5.9, q 2e-06, up in 12 of 28 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.46× (z +3.6, q 0.052, up in 8 of 25 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 10 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H460 3.86×, HepG2/C3A 14.7×, A-172 2.38×, PANC-1 2.69×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (NCI-H460 6.15×, PANC-1 5.12×; ⚠ cell-cycle shift, explains ~55% of this change); [[Harringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 6.50×; ⚠ cell-cycle shift, explains ~20% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 4.75×); [[Gefitinib (drug)]] 5 µM in 1 line (NCI-H460 2.35×).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.347× (z -14.1, q 1e-42, down in 24 of 30 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 0.568× (z -7.6, q 4e-12, down in 21 of 30 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FMNL1-DT]] (+0.71, fdr 7e-06, ⚠ same locus), [[TSPAN4]] (+0.57, fdr 1e-05), [[PIK3CD]] (+0.56, fdr 3e-05), [[SLC9A3R2]] (+0.53, fdr 3e-05); moves opposite to [[MFSD14A]] (-0.43, fdr 5e-04), [[ADIPOR2]] (-0.43, fdr 1e-04), [[ATP2A2]] (-0.42, fdr 2e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 5 go from it, the strongest it → [[PIK3CD]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11591.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 10 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H460 3.86×, HepG2/C3A 14.7×, A-172 2.38×, PANC-1 2.69×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (NCI-H460 6.15×, PANC-1 5.12×; ⚠ cell-cycle shift, explains ~55% of this change); [[Harringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 6.50×; ⚠ cell-cycle shift, explains ~20% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 4.75×); [[Gefitinib (drug)]] 5 µM in 1 line (NCI-H460 2.35×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.56×** | +5.9 | 2e-06 | 12/28 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.47×** | +5.1 | 9e-05 | 10/23 (PANC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.46×** | +4.7 | 6e-04 | 6/19 (NCI-H2030, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.46×** | +3.6 | 0.052 | 8/25 (H4, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.30×** | +3.4 | 0.073 | 4/18 (LOX-IMVI, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.30×** | +3.3 | 0.073 | 13/30 (NCI-H460, PANC-1, …) | all doses, flat | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | **1.28×** | +3.3 | 0.073 | 6/25 (HOP62, A498, …) | inconsistent across doses | low cells (technical?) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.41×** | +3.3 | 0.073 | 10/28 (NCI-H460, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.28× | +3.1 | 0.11 | 10/30 (NCI-H460, PANC-1, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 12 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11591.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.347×** | -14.1 | 1e-42 | 24/30 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.361×** | -13.6 | 1e-39 | 26/30 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.418×** | -11.6 | 5e-29 | 24/29 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.606×** | -9.4 | 8e-19 | 20/29 (HOP62, Panc 03.27, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.539×** | -8.0 | 2e-13 | 22/28 (HOP62, NCI-H1792, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.568×** | -7.6 | 4e-12 | 21/30 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.582×** | -7.2 | 4e-11 | 21/30 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.584×** | -6.9 | 3e-10 | 18/29 (CFPAC-1, SW480, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.617×** | -6.5 | 7e-09 | 16/29 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.469×** | -5.3 | 7e-06 | 18/30 (HOP62, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.680×** | -5.2 | 1e-05 | 18/28 (NCI-H460, H4, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~66% of this change | **0.670×** | -5.2 | 1e-05 | 17/25 (HOP62, NCI-H460, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.526×** | -4.5 | 3e-04 | 17/27 (PANC-1, A549, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.723×** | -4.3 | 6e-04 | 13/29 (NCI-H460, CFPAC-1, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.724×** | -4.3 | 6e-04 | 14/28 (C-33 A, NCI-H460, …) | all doses, flat |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.769×** | -3.5 | 0.014 | 10/30 (SK-MEL-2, SW480, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.835× | -3.4 | 0.019 | 12/30 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.765×** | -3.4 | 0.019 | 9/28 (CFPAC-1, SW480, …) | inconsistent across doses | position effect removed |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.779×** | -3.4 | 0.021 | 5/28 (NCI-H460, NCI-H2030, …) | all doses, flat | position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.773×** | -3.2 | 0.035 | 9/27 (SW 900, NCI-H460, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.800×** | -3.0 | 0.064 | 12/29 (SK-MEL-2, H4, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.852× | -3.0 | 0.064 | 6/30 (HOP62, SW480, …) | inconsistent across doses |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **0.804×** | -2.9 | 0.074 | 6/30 (NCI-H460, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.65 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11591. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 46.7 | 13 (11 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +18.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 4.75× (z +15.5) | [[Panobinostat (drug)]] 5 µM 0.118× (z -21.3) ⚠ cell-cycle shift, explains ~34% of this change |
| [[CFPAC-1 (line)]] | alt | 57.3 | 0 | 11 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -15.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.317× (z -10.0) |
| [[HOP62 (line)]] | alt | 59.5 | 0 | 10 (9 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.101× (z -18.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.277× (z -10.5) |
| [[NCI-H1792 (line)]] | alt | 38.3 | 0 | 8 (8 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.108× (z -13.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SW480 (line)]] | alt | 29.6 | 0 | 7 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.132× (z -16.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H2347 (line)]] | alt | 25.1 | 0 | 6 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.228× (z -10.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[Panc 03.27 (line)]] | alt | 38.0 | 0 | 5 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -16.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A-172 (line)]] | wt | 43.5 | 2 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +9.3) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 0.5 µM 0.227× (z -11.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[MIA PaCa-2 (line)]] | alt | 13.6 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.229× (z -11.2) ⚠ cell-cycle shift, explains ~32% of this change |
| [[PANC-1 (line)]] | alt | 9.87 | 3 (3 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 5.12× (z +10.4) ⚠ cell-cycle shift, explains ~55% of this change | [[Panobinostat (drug)]] 0.5 µM 0.228× (z -9.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A549 (line)]] | wt | 30.8 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.153× (z -14.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SNU-423 (line)]] | alt | 36.9 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.225× (z -10.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[H4 (line)]] | wt | 27.2 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0902× (z -11.5) ⚠ cell-cycle shift, explains ~34% of this change |
| [[J82 (line)]] | alt | 18.7 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.225× (z -9.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H2030 (line)]] | alt | 51.9 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.288× (z -11.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A-427 (line)]] | wt | 22.1 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.250× (z -8.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[C-33 A (line)]] | alt | 13.3 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.5 µM 0.106× (z -9.7) |
| [[HepG2_C3A (line)]] | wt | 5.83 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.7× (z +10.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SK-MEL-2 (line)]] | alt | 8.90 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.107× (z -9.0) ⚠ cell-cycle shift, explains ~34% of this change |
| [[A498 (line)]] | wt | 8.90 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.74 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.29 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.53 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.86 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.98 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.27 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.86 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11591), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FMNL1-DT]] | +0.71 | +0.69 / +0.75 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[TSPAN4]] | +0.57 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[PIK3CD]] | +0.56 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[SLC9A3R2]] | +0.53 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[VAV1]] | +0.51 | +0.39 / +0.40 | both halves | 6e-05 | pathway: RAC1 GTPase cycle |
| [[FMNL3]] | +0.51 | +0.40 / +0.52 | both halves | 5e-05 | same gene group; pathway: CDC42 GTPase cycle |
| [[PAEP]] | +0.50 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[RAP1GAP]] | +0.50 | +0.46 / +0.37 | both halves | 7e-05 |  |
| [[ADGRG1]] | +0.50 | +0.29 / +0.53 | both halves | 2e-04 |  |
| [[PPP1R18]] | +0.50 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[STMN3]] | +0.49 | +0.40 / +0.49 | both halves | 5e-05 |  |
| [[GPR68]] | +0.49 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[N4BP3]] | +0.48 | +0.44 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFSD14A]] | -0.43 | -0.31 / -0.23 | both halves | 5e-04 |  |
| [[ADIPOR2]] | -0.43 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[ATP2A2]] | -0.42 | -0.39 / -0.30 | both halves | 2e-04 |  |
| [[PRR5L]] | -0.42 | -0.38 / -0.31 | both halves | 2e-04 |  |
| [[ORC2]] | -0.42 | -0.31 / -0.38 | both halves | 2e-04 |  |
| [[MCM9]] | -0.40 | -0.30 / -0.39 | both halves | 2e-04 |  |
| [[PHKA1]] | -0.39 | -0.27 / -0.48 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises FMNL1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[IL11]] | B | IL11 activity raises FMNL1's level | lines that do not express IL11 (27) vs lines expressing it (23) | 2.33× lower at baseline in the lines without IL11 | 0.067 | ⚠ within organs, on part of the lines; also absent: EDNRA, LINC00973, LINC01583 |
| [[FMNL1-DT]] | C | FMNL1-DT activity raises FMNL1's level | lines that do not express FMNL1-DT (23) vs lines expressing it (27) | 5.90× lower at baseline in the lines without FMNL1-DT | 5e-05 | ⚠ within organs, on part of the lines; also absent: CACNG6, FMNL1, SLFN11; maybe low, not absent; co-absent with the target |
| [[LINC00973]] | C | LINC00973 activity raises FMNL1's level | lines that do not express LINC00973 (23) vs lines expressing it (27) | 3.01× lower at baseline in the lines without LINC00973 | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000239462, IL11, BICC1; co-absent with the target |
| [[COL7A1]] | C | COL7A1 activity raises FMNL1's level | lines that do not express COL7A1 (24) vs lines expressing it (26) | 2.57× lower at baseline in the lines without COL7A1 | 0.090 | ⚠ within organs, on part of the lines; also absent: DKK3, ABI3BP, COL5A1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIK3CD]] | B | FMNL1 activity raises PIK3CD's level | lines that do not express FMNL1 (18) vs lines expressing it (32) | 2.93× lower at baseline in the lines without FMNL1 | 0.017 | ⚠ within organs, on part of the lines; also absent: FMNL1-DT, WIPF1, SOGA3 |
| [[PDLIM4]] | B | FMNL1 activity raises PDLIM4's level | lines that do not express FMNL1 (18) vs lines expressing it (32) | 2.27× lower at baseline in the lines without FMNL1 | 0.069 | ⚠ within organs, on part of the lines; also absent: FMNL1-DT, WIPF1, SOGA3 |
| [[ZNF697]] | B | FMNL1 activity raises ZNF697's level | lines that do not express FMNL1 (18) vs lines expressing it (32) | 1.81× lower at baseline in the lines without FMNL1 | 0.082 | ⚠ within organs, on part of the lines; also absent: FMNL1-DT, WIPF1, SOGA3 |
| [[LINC00973]] | C | FMNL1 activity raises LINC00973's level | lines that do not express FMNL1 (18) vs lines expressing it (32) | 2.30× lower at baseline in the lines without FMNL1 | 0.005 | ⚠ within organs, on part of the lines; also absent: FMNL1-DT, WIPF1, SOGA3; co-absent with the target |
| [[FMNL1-DT]] | C | FMNL1 activity raises FMNL1-DT's level | lines that do not express FMNL1 (18) vs lines expressing it (32) | 3.57× lower at baseline in the lines without FMNL1 | 0.009 | ⚠ within organs, on part of the lines; also absent: FMNL1-DT, WIPF1, SOGA3; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.198). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (51.9, 1.2); signed map (-1.8, 44.0). **Vector** length 72.0, 16.7% of its response variance represented; |z| ≥ 3 in 819 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +3.7 | +3.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.3 | +2.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.9 | +0.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +2.4 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +1.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.4 | +0.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.4 | +1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | -1.0 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -2.3 | -8.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.3 | -1.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -1.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -2.1 | -6.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -6.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.8 | -2.2 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.6 | -1.3 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -1.6 | -0.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.5 | -5.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.4 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | formin like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:45,221,444-45,247,319 (+) |
| Ensembl biotype | protein_coding |
| Also known as | C17orf1; previously C17orf1B, FMNL |
| Gene groups (HGNC) | Armadillo like helical domain containing; Formins |
| Reactome | 7 pathways, smallest: RHO GTPases Activate Formins; CDC42 GTPase cycle; RAC1 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [O95466](https://www.uniprot.org/uniprotkb/O95466) (Formin-like protein 1):

> Plays a role in actin cytoskeleton dynamics and regulation of cell shape.

**Summary**, from NCBI Gene [752](https://www.ncbi.nlm.nih.gov/gene/752):

> This gene encodes a formin-related protein. Formin-related proteins have been implicated in morphogenesis, cytokinesis, and cell polarity. An alternative splice variant has been described but its full length sequence has not been determined. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1212](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1212) · Entrez [752](https://www.ncbi.nlm.nih.gov/gene/752) · UniProt [O95466](https://www.uniprot.org/uniprotkb/O95466) · Ensembl [ENSG00000184922](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184922)

## Data

Gene col 11591: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11591); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11591, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11591]; `tensor/DDL_lfc|DDL_z.npy` [11591]; `embed/gene_vectors.npy` [11591]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11591 or target_col == 11591). Every well: [[FMNL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FMNL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
