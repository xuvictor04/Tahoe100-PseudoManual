---
symbol: "LRPAP1"
type: "gene"
col: 8822
ensembl_id: "ENSG00000163956"
name: "LDL receptor related protein associated protein 1"
location: "4p16.3"
module: 50
arm: "+"
pooled_cpm: 42.23
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 6
n_dd_up_clean: 11
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# LRPAP1

*LDL receptor related protein associated protein 1* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (17 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.65× (z +14.9, q 0e+00, up in 47 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.64× (z +10.8, q 5e-25, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Verteporfin (drug)]] 5 µM: 0.680× (z -5.7, q 7e-06, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BSG]] (+0.70, fdr 7e-06), [[GANAB]] (+0.68, fdr 7e-06), [[ATP6AP1]] (+0.65, fdr 7e-06); moves opposite to [[NIFK]] (-0.56, fdr 3e-05), [[BRIX1]] (-0.55, fdr 2e-05), [[RDH14]] (-0.55, fdr 3e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 19 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8822.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.65×** | +14.9 | 0e+00 | 47/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **2.36×** | +13.2 | 5e-37 | 46/48 (SW480, LS 180, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.29×** | +12.7 | 1e-34 | 47/48 (SW480, KATO III, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.30×** | +12.3 | 2e-32 | 40/40 (KATO III, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.30×** | +11.0 | 5e-26 | 40/44 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +10.8 | 5e-25 | 39/48 (LS 180, A498, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.66×** | +7.4 | 9e-12 | 39/48 (LS 180, NCI-H460, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.63×** | +7.2 | 5e-11 | 42/47 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.58×** | +7.0 | 2e-10 | 40/48 (SW480, KATO III, …) | rises with dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.60×** | +6.9 | 3e-10 | 35/48 (LS 180, A498, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +6.1 | 7e-08 | 33/48 (A498, A-172, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **1.47×** | +5.8 | 2e-07 | 30/47 (HOP62, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +5.1 | 2e-05 | 1/48 (NCI-H661) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.40×** | +4.5 | 3e-04 | 35/48 (HOP62, HT-29, …) | inconsistent across doses | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.32×** | +4.2 | 8e-04 | 24/48 (SW480, CFPAC-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +4.0 | 0.002 | 23/48 (BT-474, RKO, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.41×** | +3.8 | 0.005 | 21/47 (HOP62, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[OTS514 (drug)]] 5 µM |  | **1.59×** | +3.7 | 0.005 | 22/46 (PANC-1, A-427, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.35×** | +3.3 | 0.023 | 16/48 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.23×** | +3.2 | 0.036 | 15/48 (NCI-H460, RPMI-7951, …) | inconsistent across doses | position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.30×** | +2.8 | 0.093 | 10/48 (A498, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Minodronic acid (drug)]] 5 µM |  | **1.42×** | +2.8 | 0.093 | 4/48 (J82, SNU-423, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8822.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.680×** | -5.7 | 7e-06 | 30/48 (HepG2/C3A, C32, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.694×** | -5.6 | 7e-06 | 29/47 (SK-MEL-2, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.705×** | -5.3 | 2e-05 | 26/48 (A-427, C32, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.714×** | -5.2 | 3e-05 | 24/48 (H4, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.678×** | -5.1 | 3e-05 | 28/47 (C32, HOP62, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.800×** | -3.3 | 0.099 | 20/47 (C-33 A, SNU-1, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8822. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 48.6 | 10 (9 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.08× (z +13.4) ⚠ cell-cycle shift, explains ~80% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +10.2) | — |
| [[A-427 (line)]] | wt | 48.7 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.39× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -21.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.230× (z -13.9) |
| [[A498 (line)]] | wt | 37.1 | 5 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +11.7) | — |
| [[A549 (line)]] | wt | 23.8 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +10.1) | — |
| [[KATO III (line)]] | alt | 57.6 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.73× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[LS 180 (line)]] | wt | 60.5 | 5 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +14.4) | — |
| [[SW480 (line)]] | alt | 38.5 | 5 (5 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.96× (z +18.4) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H460 (line)]] | wt | 60.5 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +11.1) | — |
| [[PANC-1 (line)]] | alt | 29.7 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[HEC-1-A (line)]] | alt | 41.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[HOP62 (line)]] | alt | 48.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[LoVo (line)]] | wt | 45.8 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +11.6) | — |
| [[AsPC-1 (line)]] | alt | 20.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +9.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HepG2_C3A (line)]] | wt | 41.7 | 1 (1 ⚠) | 1 | [[Panobinostat (drug)]] 0.5 µM 3.38× (z +8.7) ⚠ cell-cycle shift, explains ~34% of this change | [[Verteporfin (drug)]] 5 µM 0.128× (z -14.1) |
| [[HS-578T (line)]] | alt | 40.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.21× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[HT-29 (line)]] | alt | 37.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.61× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[LOX-IMVI (line)]] | wt | 40.3 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.32× (z +10.6) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 57.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.121× (z -16.7) |
| [[BT-474 (line)]] | alt | 34.5 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.51× (z +9.1) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[CFPAC-1 (line)]] | alt | 52.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[CHP-212 (line)]] | wt | 37.8 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.110× (z -8.7) ⚠ cell-cycle shift, explains ~13% of this change |
| [[HCT15 (line)]] | alt | 40.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[J82 (line)]] | alt | 46.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 25.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.39× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[NCI-H1792 (line)]] | alt | 23.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.54× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[NCI-H2030 (line)]] | alt | 29.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[NCI-H23 (line)]] | alt | 35.4 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.97× (z +9.1) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H2347 (line)]] | alt | 56.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[NCI-H661 (line)]] | alt | 40.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0558× (z -10.1) |
| [[Panc 03.27 (line)]] | alt | 38.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[SNU-1 (line)]] | wt | 39.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.261× (z -8.5) |
| [[SNU-423 (line)]] | alt | 40.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.35× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[SW 900 (line)]] | alt | 38.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.49× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[A-172 (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 76.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 89.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 47.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 54.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 45.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8822), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BSG]] | +0.70 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[GANAB]] | +0.68 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[ATP6AP1]] | +0.65 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[LAMP1]] | +0.64 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[APLP1]] | +0.63 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[PLOD1]] | +0.61 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[MAN2B2]] | +0.61 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[GRN]] | +0.61 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[SELENON]] | +0.61 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[CTSA]] | +0.61 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[ECM1]] | +0.60 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[PRKCSH]] | +0.60 | +0.59 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NIFK]] | -0.56 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[BRIX1]] | -0.55 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[RDH14]] | -0.55 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[PDCD5]] | -0.55 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[MRPL15]] | -0.52 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[IWS1]] | -0.50 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[C15orf40]] | -0.50 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[EIF5B]] | -0.50 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[NSRP1]] | -0.50 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[RP9]] | -0.50 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[PPIG]] | -0.50 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[GSTO2]] | -0.49 | -0.38 / -0.40 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LRPAP1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.731). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-21.1, -21.6); signed map (-26.9, -37.9). **Vector** length 96.5, 25.9% of its response variance represented; |z| ≥ 3 in 1,047 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Glycosphingolipid catabolism* (reactome, mean cos +0.50 to 5); *Degradation of the extracellular matrix* (reactome, mean cos +0.51 to 7); *Glycosphingolipid metabolism* (reactome, mean cos +0.50 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | +3.7 | +4.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | +3.6 | +14.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | +3.6 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +3.4 | +11.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +6.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.9 | +0.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.8 | +2.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.8 | +1.5 |
|  | [[Posaconazole (drug)]] 5 µM |  | +1.6 | +0.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -8.3 | -5.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.5 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.3 | -5.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.0 | -5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.4 | +1.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.7 | -5.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.5 | -5.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | LDL receptor related protein associated protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.3 — chr4:3,503,612-3,532,446 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HBP44, Alpha-2-MRAP; previously A2MRAP, RAP |
| Hallmark sets | ANGIOGENESIS |
| Matched by | ensembl_id |

**Function**, from UniProt [P30533](https://www.uniprot.org/uniprotkb/P30533) (Alpha-2-macroglobulin receptor-associated protein):

> Molecular chaperone for LDL receptor-related proteins that may regulate their ligand binding activity along the secretory pathway.

**Summary**, from NCBI Gene [4043](https://www.ncbi.nlm.nih.gov/gene/4043):

> This gene encodes a protein that interacts with the low density lipoprotein (LDL) receptor-related protein and facilitates its proper folding and localization by preventing the binding of ligands. Mutations in this gene have been identified in individuals with myopia 23. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2013]

**Accessions** — [HGNC:6701](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6701) · Entrez [4043](https://www.ncbi.nlm.nih.gov/gene/4043) · UniProt [P30533](https://www.uniprot.org/uniprotkb/P30533) · Ensembl [ENSG00000163956](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163956)

## Data

Gene col 8822: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8822); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8822, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8822]; `tensor/DDL_lfc|DDL_z.npy` [8822]; `embed/gene_vectors.npy` [8822]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8822 or target_col == 8822). Every well: [[LRPAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRPAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
