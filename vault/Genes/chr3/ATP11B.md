---
symbol: "ATP11B"
type: "gene"
col: 655
ensembl_id: "ENSG00000058063"
name: "ATPase phospholipid transporting 11B (putative)"
location: "3q26.33"
module: 233
arm: "+"
pooled_cpm: 195.33
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 7
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/233"]
generated_by: "tahoemap"
---

# ATP11B

*ATPase phospholipid transporting 11B (putative)* — 3q26.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.43× (z +7.5, q 4e-11, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.666× (z -8.6, q 6e-15, down in 40 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 6 lines (SW480 0.450×, MIA PaCa-2 0.420×, HOP62 0.417×, SNU-423 0.459×, …); [[Dinaciclib (drug)]] 5 µM in 5 lines (SHP-77 0.229×, SW1417 0.331×, A-427 0.380×, AsPC-1 0.309×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2347 0.300×, J82 0.433×; ⚠ toxic; transcription drop); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (HOP62 0.583×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPB41L5]] (+0.66, fdr 1e-05), [[PPP1R2]] (+0.62, fdr 1e-05), [[KCTD9]] (+0.61, fdr 1e-05); moves opposite to [[RPTOR]] (-0.59, fdr 1e-05), [[DUS3L]] (-0.57, fdr 3e-05), [[CPSF7]] (-0.57, fdr 4e-05).
> It is in [[Module 233]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 655.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.43×** | +7.5 | 4e-11 | 39/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +6.3 | 7e-08 | 32/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.31×** | +5.4 | 1e-05 | 28/48 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.26×** | +4.9 | 2e-04 | 28/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.25×** | +4.7 | 2e-04 | 27/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 1.16× | +4.4 | 9e-04 | 22/48 (SW1417, PANC-1, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.4 | 0.054 | 15/48 (H4, PANC-1, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.054 | 23/49 (NCI-H1573, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tomivosertib (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.054 | 24/48 (MIA PaCa-2, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.18× | +3.3 | 0.054 | 20/47 (COLO 205, A-172, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 655.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 6 lines (SW480 0.450×, MIA PaCa-2 0.420×, HOP62 0.417×, SNU-423 0.459×, …); [[Dinaciclib (drug)]] 5 µM in 5 lines (SHP-77 0.229×, SW1417 0.331×, A-427 0.380×, AsPC-1 0.309×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2347 0.300×, J82 0.433×; ⚠ toxic; transcription drop); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (HOP62 0.583×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.666×** | -8.6 | 6e-15 | 40/48 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.659×** | -8.1 | 1e-13 | 35/45 (NCI-H2347, J82, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.685×** | -7.7 | 3e-12 | 39/47 (NCI-H1573, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.701×** | -7.2 | 9e-11 | 33/43 (SHP-77, SW1417, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.722×** | -6.9 | 7e-10 | 38/49 (NCI-H2347, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.840× | -5.2 | 2e-05 | 22/48 (SW480, NCI-H661, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.846× | -5.0 | 5e-05 | 19/48 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.807×** | -4.5 | 4e-04 | 27/48 (NCI-H2347, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.828×** | -4.0 | 0.004 | 26/48 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.896× | -3.2 | 0.078 | 10/49 (NCI-H2347, C32, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.863× | -3.1 | 0.082 | 14/48 (HEC-1-A, NCI-H460, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.859× | -3.1 | 0.082 | 18/48 (NCI-H2347, RKO, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.864× | -3.1 | 0.082 | 10/48 (AsPC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.963× | -3.1 | 0.082 | 0/50 | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.865× | -3.1 | 0.082 | 14/49 (AsPC-1, LS 180, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.904× | -3.0 | 0.089 | 4/48 (CHP-212, AN3 CA, …) | rises with dose |  |
| [[Mifepristone (drug)]] 0.5 µM |  | 0.868× | -3.0 | 0.089 | 9/48 (SW1417, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 655. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 307 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -15.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 212 | 5 (4 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +17.7) ⚠ cell-cycle shift, explains ~3% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.45× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.331× (z -14.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 206 | 7 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.22× (z +21.7) | — |
| [[KATO III (line)]] | alt | 196 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.22× (z +17.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 219 | 4 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +11.9) ⚠ cell-cycle shift, explains ~3% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 1.99× (z +9.8) | [[Auranofin (drug)]] 5 µM 0.420× (z -12.9) |
| [[BT-474 (line)]] | alt | 173 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +11.2) ⚠ cell-cycle shift, explains ~3% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +11.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.551× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 311 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.299× (z -11.2) ⚠ toxic |
| [[HOP62 (line)]] | alt | 205 | 0 | 4 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.417× (z -12.8) |
| [[LoVo (line)]] | wt | 182 | 2 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.90× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.506× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.593× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 235 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.406× (z -11.5) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 173 | 3 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.229× (z -18.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 165 | 3 (1 ⚠) | 0 | [[Daptomycin (drug)]] 5 µM 2.21× (z +8.8) ⚠ unreliable plate only · without an alert: [[Peretinoin (drug)]] 5 µM 2.23× (z +8.6) | — |
| [[HepG2_C3A (line)]] | wt | 85.5 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.91× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.335× (z -10.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 156 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +14.1) ⚠ cell-cycle shift, explains ~3% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 1.75× (z +11.1) | [[Auranofin (drug)]] 5 µM 0.450× (z -16.4) |
| [[A-172 (line)]] | wt | 233 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.505× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.536× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 244 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.309× (z -13.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 260 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.19× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.498× (z -8.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 209 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.433× (z -11.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 195 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.97× (z +9.3) | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.259× (z -9.7) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 113 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.11× (z +10.7) | — |
| [[Panc 03.27 (line)]] | alt | 352 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +10.5) ⚠ cell-cycle shift, explains ~3% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.447× (z -10.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 183 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.459× (z -9.7) |
| [[SW 900 (line)]] | alt | 174 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.03× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.465× (z -9.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 239 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.380× (z -13.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 145 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.65× (z +10.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A549 (line)]] | wt | 132 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.593× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 156 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.25× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 131 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +10.6) ⚠ cell-cycle shift, explains ~3% of this change | — |
| [[NCI-H23 (line)]] | alt | 52.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +12.7) ⚠ cell-cycle shift, explains ~3% of this change | — |
| [[AN3 CA (line)]] | alt | 217 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 189 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 108 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 221 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 143 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 237 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 192 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 211 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 223 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 199 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 220 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 214 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 149 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 263 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 655), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPB41L5]] | +0.66 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[PPP1R2]] | +0.62 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[KCTD9]] | +0.61 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[OSTF1]] | +0.61 | +0.68 / +0.45 | both halves | 3e-05 |  |
| [[KATNA1]] | +0.60 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[RAP1A]] | +0.59 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[FNBP1L]] | +0.58 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[ZC2HC1A]] | +0.57 | +0.31 / +0.52 | both halves | 2e-04 |  |
| [[ABI1]] | +0.57 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[AP3S1]] | +0.57 | +0.67 / +0.46 | both halves | 3e-05 |  |
| [[TBC1D12]] | +0.57 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[ARL3]] | +0.56 | +0.52 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPTOR]] | -0.59 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[DUS3L]] | -0.57 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[CPSF7]] | -0.57 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[SNHG26]] | -0.56 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[GRWD1]] | -0.56 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[LTV1]] | -0.56 | -0.64 / -0.45 | both halves | 3e-05 |  |
| [[LSG1]] | -0.55 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[GTPBP4]] | -0.54 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[ZNF507]] | -0.53 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[DNAJC11]] | -0.53 | -0.62 / -0.39 | both halves | 5e-05 |  |
| [[ZNF268]] | -0.53 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[ZNF202]] | -0.53 | -0.50 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 233]]; 6 genes; every member is in the + arm (projection on the module's main direction 0.785). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (4.7, -12.7); signed map (-23.2, 16.8). **Vector** length 105, 33.6% of its response variance represented; |z| ≥ 3 in 1,171 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.9 | +0.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +2.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +1.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +2.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | +3.2 | +3.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.9 | +1.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.9 | +2.7 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +2.5 | +1.8 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.4 | +0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.3 | +2.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -9.9 | -8.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -7.5 | +0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.4 | +1.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.8 | -1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.1 | -5.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.3 | -1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | ATPase phospholipid transporting 11B (putative) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q26.33 — chr3:182,793,503-182,921,629 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ATPIF, ATPIR, KIAA0956 |
| Gene groups (HGNC) | ATPase phospholipid transporting |
| Reactome | 5 pathways, smallest: Ion transport by P-type ATPases; Ion channel transport; Neutrophil degranulation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2G3](https://www.uniprot.org/uniprotkb/Q9Y2G3) (Phospholipid-transporting ATPase IF):

> Catalytic component of a P4-ATPase flippase complex which catalyzes the hydrolysis of ATP coupled to the transport of aminophospholipids, phosphatidylserines (PS) and phosphatidylethanolamines (PE), from the outer to the inner leaflet of intracellular membranes. May contribute to the maintenance of membrane lipid asymmetry in endosome compartment.

**Summary**, from NCBI Gene [23200](https://www.ncbi.nlm.nih.gov/gene/23200):

> P-type ATPases, such as ATP11B, are phosphorylated in their intermediate state and drive uphill transport of ions across membranes. Several subfamilies of P-type ATPases have been identified. One subfamily transports heavy metal ions, such as Cu(2+) or Cd(2+). Another subfamily transports non-heavy metal ions, such as H(+), Na(+), K(+), or Ca(+). A third subfamily transports amphipaths, such as phosphatidylserine.[supplied by OMIM, Feb 2005]

**Accessions** — [HGNC:13553](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13553) · Entrez [23200](https://www.ncbi.nlm.nih.gov/gene/23200) · UniProt [Q9Y2G3](https://www.uniprot.org/uniprotkb/Q9Y2G3) · Ensembl [ENSG00000058063](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000058063)

## Data

Gene col 655: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 655); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 655, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 655]; `tensor/DDL_lfc|DDL_z.npy` [655]; `embed/gene_vectors.npy` [655]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 655 or target_col == 655). Every well: [[ATP11B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP11B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
