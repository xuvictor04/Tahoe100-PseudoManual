---
symbol: "C2orf76"
type: "gene"
col: 11781
ensembl_id: "ENSG00000186132"
name: "chromosome 2 open reading frame 76"
location: "2q14.2"
module: 15
arm: "+"
pooled_cpm: 13.6
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 4
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# C2orf76

*chromosome 2 open reading frame 76* — 2q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.99× (z +37.8, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.754× (z -5.4, q 3e-05, down in 18 of 47 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 8 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SW 900 0.0761×, A-427 0.201×, PANC-1 0.463×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2030 0.283×, A549 0.198×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[AZD2858 (drug)]] 0.5 µM in 1 line (HOP62 0.0655×; ⚠ toxic); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.227×); [[Finasteride (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0595×); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (SNU-423 0.125×).
> Its strongest partners by |cos| (85 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSTD3]] (+0.74, fdr 1e-05), [[MAILR]] (+0.72, fdr 4e-05), [[UBE3B]] (+0.69, fdr 6e-05); moves opposite to [[NAA40]] (-0.64, fdr 4e-05), [[RRP1B]] (-0.63, fdr 5e-05), [[GPRIN1]] (-0.60, fdr 4e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11781.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.99×** | +37.8 | 0e+00 | 46/47 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.07×** | +20.8 | 0e+00 | 39/46 (SW480, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.47×** | +16.8 | 0e+00 | 36/48 (SW480, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.59×** | +12.6 | 3e-34 | 28/46 (J82, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +9.2 | 4e-18 | 27/48 (SW1417, HOP62, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.41×** | +6.7 | 2e-09 | 25/48 (SK-MEL-2, J82, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.34×** | +5.4 | 5e-06 | 15/46 (SK-MEL-2, LOX-IMVI, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +5.3 | 7e-06 | 15/42 (A498, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.32×** | +5.3 | 8e-06 | 16/47 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.19× | +4.8 | 7e-05 | 6/48 (BT-474, MIA PaCa-2, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.20× | +4.8 | 7e-05 | 6/48 (NCI-H460, SW480, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.26×** | +4.3 | 9e-04 | 17/46 (HEC-1-A, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.50×** | +4.1 | 0.002 | 13/48 (A498, J82, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.25×** | +4.0 | 0.002 | 6/47 (SK-MEL-2, C32, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.23×** | +4.0 | 0.002 | 12/47 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | **1.22×** | +3.8 | 0.005 | 6/46 (CFPAC-1, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11781.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 8 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SW 900 0.0761×, A-427 0.201×, PANC-1 0.463×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2030 0.283×, A549 0.198×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[AZD2858 (drug)]] 0.5 µM in 1 line (HOP62 0.0655×; ⚠ toxic); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.227×); [[Finasteride (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0595×); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (SNU-423 0.125×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.754×** | -5.4 | 3e-05 | 18/47 (NCI-H460, SW480, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.779×** | -4.8 | 4e-04 | 18/48 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.788×** | -4.6 | 8e-04 | 17/47 (H4, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **0.796×** | -4.4 | 0.002 | 15/46 (PANC-1, A549, …) | two highest doses |  |
| [[8-Hydroxyquinoline (drug)]] 5 µM |  | 0.884× | -3.4 | 0.087 | 2/48 (NCI-H1573, C-33 A) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | 0.790× | -3.2 | 0.11 | 10/45 (hTERT-HPNE, COLO 205, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | 0.841× | -3.2 | 0.11 | 8/24 (PANC-1, LOX-IMVI, …) | top dose only | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.853× | -3.1 | 0.16 | 6/47 (PANC-1, SNU-423, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11781. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 32.0 | 1 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +12.4) | [[Digitoxin (drug)]] 5 µM 0.422× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[HOP62 (line)]] | alt | 11.0 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.52× (z +13.4) | [[AZD2858 (drug)]] 0.5 µM 0.0655× (z -12.2) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 13.9 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.85× (z +15.3) | [[Digitoxin (drug)]] 0.5 µM 0.317× (z -9.2) ⚠ cell-cycle shift, explains ~37% of this change |
| [[RKO (line)]] | wt | 11.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.93× (z +11.1) | — |
| [[SW480 (line)]] | alt | 11.0 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.56× (z +16.7) | — |
| [[A-427 (line)]] | wt | 25.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.201× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.227× (z -11.6) |
| [[A498 (line)]] | wt | 10.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.14× (z +17.9) | — |
| [[A549 (line)]] | wt | 12.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.198× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 14.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.38× (z +15.5) | — |
| [[HS-578T (line)]] | alt | 10.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.95× (z +12.4) | — |
| [[hTERT-HPNE (line)]] | wt | 7.35 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.54× (z +8.8) | [[Finasteride (drug)]] 5 µM 0.0595× (z -9.9) |
| [[J82 (line)]] | alt | 8.37 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.15× (z +12.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 20.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.26× (z +13.7) | — |
| [[NCI-H2030 (line)]] | alt | 21.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +14.0) | [[Dinaciclib (drug)]] 0.05 µM 0.283× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 13.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.44× (z +8.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0984× (z -10.9) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 7.25 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.09× (z +9.2) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.125× (z -9.7) |
| [[SW 900 (line)]] | alt | 14.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.23× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.0761× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 16.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.18× (z +13.7) | — |
| [[AsPC-1 (line)]] | alt | 5.97 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.34× (z +9.5) | — |
| [[C32 (line)]] | wt | 17.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +9.6) | — |
| [[CFPAC-1 (line)]] | alt | 6.35 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.84× (z +13.4) | — |
| [[COLO 205 (line)]] | alt | 6.93 | 0 | 1 | — | [[Procainamide (hydrochloride) (drug)]] 5 µM 0.0678× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 12.5 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.105× (z -9.4) |
| [[Hs 766T (line)]] | wt | 7.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.04× (z +10.2) | — |
| [[HT-29 (line)]] | alt | 8.50 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.85× (z +8.8) | — |
| [[LoVo (line)]] | wt | 8.15 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.22× (z +11.1) | — |
| [[LOX-IMVI (line)]] | wt | 11.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.21× (z +9.1) | — |
| [[LS 180 (line)]] | wt | 8.82 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.09× (z +9.9) | — |
| [[NCI-H1792 (line)]] | alt | 9.99 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.38× (z +11.5) | — |
| [[NCI-H23 (line)]] | alt | 25.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.79× (z +13.6) | — |
| [[NCI-H2347 (line)]] | alt | 7.11 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +8.7) | — |
| [[Panc 03.27 (line)]] | alt | 7.00 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.82× (z +11.5) | — |
| [[SW1417 (line)]] | alt | 11.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.40× (z +13.9) | — |
| [[SW48 (line)]] | wt | 9.32 | 0 | 1 | — | [[Riluzole hydrochloride (drug)]] 0.5 µM 0.0722× (z -8.5) |
| [[AN3 CA (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.73 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11781), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 15 of them with an alert (⚠; 15 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSTD3]] | +0.74 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[MAILR]] | +0.72 | +0.73 / +0.41 | both halves | 4e-05 |  |
| [[UBE3B]] | +0.69 | +0.68 / +0.39 | both halves | 6e-05 |  |
| [[SEC24B-AS1]] | +0.69 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[TP53]] | +0.69 | +0.72 / +0.37 | both halves | 8e-05 |  |
| [[CFAP418-AS1]] | +0.69 | +0.70 / +0.34 | both halves | 1e-04 |  |
| [[DNASE1]] | +0.69 | +0.69 / +0.42 | both halves | 4e-05 |  |
| [[SENP8]] | +0.68 | +0.66 / +0.43 | both halves | 3e-05 |  |
| [[CHD1-DT]] | +0.68 | +0.64 / +0.37 | both halves | 8e-05 |  |
| [[SPESP1]] | +0.68 | +0.62 / +0.42 | both halves | 4e-05 |  |
| [[ERCC6L2-AS1]] | +0.68 | +0.70 / +0.24 | both halves | 5e-04 |  |
| [[MAIP1]] | +0.67 | +0.60 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAA40]] | -0.64 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[RRP1B]] | -0.63 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[GPRIN1]] | -0.60 | -0.48 / -0.26 | both halves | 4e-04 |  |
| [[MOCS1]] | -0.59 | -0.38 / -0.44 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers C2orf76's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.650). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (1.5, 19.1); signed map (23.9, -10.6). **Vector** length 79.9, 14.6% of its response variance represented; |z| ≥ 3 in 995 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.5 | +37.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +20.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +16.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +9.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.1 | +4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +6.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +4.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.0 | +5.4 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.2 | -3.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.1 | -0.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.6 | -1.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.2 | +3.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | +1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | +0.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -2.7 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.3 | -2.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | chromosome 2 open reading frame 76 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.2 — chr2:119,302,225-119,366,834 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC104437, LOC130355, AIM29 |
| Matched by | ensembl_id |

UniProt [Q3KRA6](https://www.uniprot.org/uniprotkb/Q3KRA6) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27017](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27017) · Entrez [130355](https://www.ncbi.nlm.nih.gov/gene/130355) · UniProt [Q3KRA6](https://www.uniprot.org/uniprotkb/Q3KRA6) · Ensembl [ENSG00000186132](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186132)

## Data

Gene col 11781: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11781); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11781, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11781]; `tensor/DDL_lfc|DDL_z.npy` [11781]; `embed/gene_vectors.npy` [11781]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11781 or target_col == 11781). Every well: [[C2orf76 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C2orf76.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
