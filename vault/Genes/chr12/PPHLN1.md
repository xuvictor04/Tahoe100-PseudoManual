---
symbol: "PPHLN1"
type: "gene"
col: 5536
ensembl_id: "ENSG00000134283"
name: "periphilin 1"
location: "12q12"
module: 169
arm: "+"
pooled_cpm: 149.9
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 3
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/169"]
generated_by: "tahoemap"
---

# PPHLN1

*periphilin 1* — 12q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (5 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.77× (z +16.4, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.696× (z -10.1, q 4e-21, down in 31 of 44 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (NCI-H23 0.402×, A-427 0.472×, SW 900 0.400×, AsPC-1 0.491×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (HCT15 0.258×, Panc 03.27 0.398×, NCI-H23 0.587×, CFPAC-1 0.520×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 0.704×, SNU-423 0.637×; ⚠ cell-cycle shift, explains ~89% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFAF7]] (+0.73, fdr 7e-06), [[MED17]] (+0.66, fdr 7e-06), [[ARHGEF7]] (+0.66, fdr 1e-05); moves opposite to [[VEZF1]] (-0.64, fdr 7e-06), [[SKIL]] (-0.61, fdr 1e-05), [[THAP5]] (-0.59, fdr 1e-05).
> It is in [[Module 169]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[BSN]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5536.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.77×** | +16.4 | 0e+00 | 47/48 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +16.2 | 0e+00 | 40/49 (A498, SHP-77, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +16.0 | 0e+00 | 41/48 (MIA PaCa-2, NCI-H23, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.66×** | +14.7 | 0e+00 | 47/48 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.63×** | +14.0 | 9e-43 | 43/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.66×** | +13.8 | 4e-41 | 47/48 (A498, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.45×** | +13.5 | 8e-40 | 46/49 (LoVo, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.57×** | +13.0 | 1e-36 | 44/48 (HT-29, LoVo, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.56×** | +12.8 | 7e-36 | 47/48 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +12.5 | 2e-34 | 42/50 (NCI-H23, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +11.1 | 4e-27 | 34/48 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.42×** | +10.2 | 1e-22 | 44/48 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.92×** | +9.9 | 2e-21 | 41/48 (LS 180, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +9.8 | 5e-21 | 33/48 (A498, A549, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.35×** | +8.7 | 1e-16 | 37/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.26×** | +6.7 | 7e-10 | 26/48 (LoVo, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5536.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (NCI-H23 0.402×, A-427 0.472×, SW 900 0.400×, AsPC-1 0.491×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (HCT15 0.258×, Panc 03.27 0.398×, NCI-H23 0.587×, CFPAC-1 0.520×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 0.704×, SNU-423 0.637×; ⚠ cell-cycle shift, explains ~89% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.696×** | -10.1 | 4e-21 | 31/44 (NCI-H23, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.757×** | -8.1 | 2e-13 | 33/49 (HCT15, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.816×** | -5.7 | 3e-06 | 25/48 (H4, CFPAC-1, …) | rises with dose | composition shift |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.872× | -4.0 | 0.011 | 12/48 (NCI-H1792, AsPC-1, …) | inconsistent across doses |  |
| [[L-Eflornithine (monohydrochloride) (drug)]] 5 µM |  | 0.880× | -3.7 | 0.021 | 7/48 (LoVo, AsPC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.880× | -3.7 | 0.021 | 16/48 (NCI-H460, A-427, …) | rises with dose |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.883× | -3.6 | 0.027 | 6/48 (C32, AsPC-1, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.892× | -3.3 | 0.068 | 8/47 (A498, LOX-IMVI, …) | top dose only |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.895× | -3.2 | 0.087 | 6/48 (LOX-IMVI, HT-29, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.898× | -3.1 | 0.11 | 6/48 (NCI-H2347, HCT15, …) | top dose only |  |
| [[Apalutamide (drug)]] 0.5 µM |  | 0.902× | -3.0 | 0.14 | 6/48 (NCI-H1573, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5536. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 182 | 13 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +14.7) | [[Dinaciclib (drug)]] 5 µM 0.571× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 307 | 9 (3 ⚠) | 2 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +15.7) | [[Dinaciclib (drug)]] 5 µM 0.402× (z -16.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 170 | 11 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.97× (z +13.8) | — |
| [[NCI-H460 (line)]] | wt | 186 | 10 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.49× (z +16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.00× (z +13.2) | — |
| [[A498 (line)]] | wt | 128 | 9 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +18.8) | — |
| [[HT-29 (line)]] | alt | 118 | 9 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.34× (z +12.7) | — |
| [[PANC-1 (line)]] | alt | 146 | 9 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.20× (z +15.9) | — |
| [[HEC-1-A (line)]] | alt | 147 | 7 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +13.2) | — |
| [[AsPC-1 (line)]] | alt | 164 | 5 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.55× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.491× (z -9.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 106 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.60× (z +10.2) | — |
| [[Panc 03.27 (line)]] | alt | 159 | 5 | 1 (1 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.398× (z -15.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 95.0 | 5 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +13.9) | — |
| [[A-427 (line)]] | wt | 135 | 4 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.472× (z -11.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 124 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.01× (z +10.5) | — |
| [[C32 (line)]] | wt | 129 | 5 | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +11.0) | — |
| [[KATO III (line)]] | alt | 145 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +14.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 122 | 5 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.41× (z +17.4) | — |
| [[NCI-H1573 (line)]] | alt | 130 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +12.1) | — |
| [[NCI-H1792 (line)]] | alt | 92.9 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.73× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +11.0) | — |
| [[HS-578T (line)]] | alt | 84.7 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +14.6) | — |
| [[NCI-H2030 (line)]] | alt | 175 | 4 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +11.6) | — |
| [[RKO (line)]] | wt | 196 | 4 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +12.8) | — |
| [[SHP-77 (line)]] | alt | 170 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +15.0) | — |
| [[COLO 205 (line)]] | alt | 125 | 3 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.61× (z +10.6) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.25× (z +9.3) | — |
| [[LS 180 (line)]] | wt | 145 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +11.0) | — |
| [[SK-MEL-2 (line)]] | alt | 162 | 2 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.502× (z -9.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 156 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.54× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.637× (z -9.4) ⚠ cell-cycle shift, explains ~89% of this change |
| [[SW 900 (line)]] | alt | 189 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.400× (z -10.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 154 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.520× (z -10.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 180 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +10.8) | — |
| [[LOX-IMVI (line)]] | wt | 186 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.23× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.528× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 165 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.83× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.552× (z -9.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 123 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +10.0) | — |
| [[SW1417 (line)]] | alt | 140 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +12.6) | — |
| [[BT-474 (line)]] | alt | 127 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.495× (z -8.8) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 164 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.339× (z -9.6) ⚠ transcription drop |
| [[HCT15 (line)]] | alt | 197 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -16.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 116 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +11.2) | — |
| [[J82 (line)]] | alt | 130 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 1.73× (z +8.6) | — |
| [[SW48 (line)]] | wt | 134 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.70× (z +8.9) | — |
| [[AN3 CA (line)]] | alt | 178 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 199 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 154 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 92.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 146 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 163 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5536), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFAF7]] | +0.73 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[MED17]] | +0.66 | +0.66 / +0.62 | both halves | 7e-06 | pathway: Epigenetic regulation of gene expression; STRING 584 |
| [[ARHGEF7]] | +0.66 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[TNPO3]] | +0.65 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[MTPN]] | +0.64 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[SNHG30]] | +0.62 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[ASB7]] | +0.62 | +0.60 / +0.58 | both halves | 8e-06 |  |
| [[SEC24B]] | +0.62 | +0.72 / +0.50 | both halves | 1e-05 |  |
| [[RNF4]] | +0.61 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[REXO2]] | +0.61 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[POLR2B]] | +0.60 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[ANAPC10]] | +0.60 | +0.64 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VEZF1]] | -0.64 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[SKIL]] | -0.61 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[THAP5]] | -0.59 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[BHLHE41]] | -0.59 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[ZNF641]] | -0.59 | -0.57 / -0.59 | both halves | 9e-06 |  |
| [[ZNF318]] | -0.59 | -0.63 / -0.57 | both halves | 1e-05 |  |
| [[LGALSL]] | -0.59 | -0.65 / -0.48 | both halves | 2e-05 |  |
| [[SYNPO]] | -0.59 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[RTL6]] | -0.59 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[MDC1]] | -0.58 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[TNKS1BP1]] | -0.56 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[SLC35A4]] | -0.56 | -0.58 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BSN]] | B | BSN activity raises PPHLN1's level | lines that do not express BSN (17) vs lines expressing it (33) | 1.25× lower at baseline in the lines without BSN | 0.071 | ⚠ within organs, on part of the lines; also absent: HRK, SPTB, CACNA2D2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 169]]; 25 genes; every member is in the + arm (projection on the module's main direction 0.746). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-12.6, -12.0); signed map (-35.8, -8.3). **Vector** length 114, 38.8% of its response variance represented; |z| ≥ 3 in 1,387 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +9.0 | +9.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +8.3 | +16.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +12.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +16.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.3 | +13.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.8 | +13.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +3.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.9 | +6.1 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.8 | +0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +5.3 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -14.7 | -5.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | -13.5 | -2.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -10.3 | +1.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | -9.7 | -3.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | -2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.9 | -2.4 |
|  | [[Posaconazole (drug)]] 5 µM |  | -1.9 | -1.2 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.6 | -2.4 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | -1.6 | -0.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.6 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | periphilin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q12 — chr12:42,238,447-42,459,715 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | HUSH complex |
| Reactome | 3 pathways, smallest: Regulation of endogenous retroelements by the Human Silencing Hub (HUSH) complex; Regulation of endogenous retroelements; Epigenetic regulation of gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NEY8](https://www.uniprot.org/uniprotkb/Q8NEY8) (Periphilin-1):

> RNA-binding component of the HUSH complex, a multiprotein complex that mediates epigenetic repression of mobile genetic elements, such as retroviruses and transposable elements. The HUSH complex mainly represses LINE-1 (L1) retrotransposons that are still capable of transposition. The HUSH complex is recruited to genomic loci rich in H3K9me3 and is probably required to maintain transcriptional silencing by promoting recruitment of SETDB1, a histone methyltransferase that mediates further …

**Summary**, from NCBI Gene [51535](https://www.ncbi.nlm.nih.gov/gene/51535):

> The protein encoded by this gene is one of the several proteins that become sequentially incorporated into the cornified cell envelope during the terminal differentiation of keratinocyte at the outer layers of epidermis. This protein interacts with periplakin, which is known as a precursor of the cornified cell envelope. The cellular localization pattern and insolubility of this protein suggest that it may play a role in epithelial differentiation and contribute to epidermal integrity and …

**Accessions** — [HGNC:19369](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19369) · Entrez [51535](https://www.ncbi.nlm.nih.gov/gene/51535) · UniProt [Q8NEY8](https://www.uniprot.org/uniprotkb/Q8NEY8) · Ensembl [ENSG00000134283](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134283)

## Data

Gene col 5536: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5536); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5536, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5536]; `tensor/DDL_lfc|DDL_z.npy` [5536]; `embed/gene_vectors.npy` [5536]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5536 or target_col == 5536). Every well: [[PPHLN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPHLN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
