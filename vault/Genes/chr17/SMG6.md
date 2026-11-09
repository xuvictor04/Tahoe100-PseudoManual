---
symbol: "SMG6"
type: "gene"
col: 945
ensembl_id: "ENSG00000070366"
name: "SMG6 nonsense mediated mRNA decay factor"
location: "17p13.3"
module: 3
arm: "+"
pooled_cpm: 167.3
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 12
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# SMG6

*SMG6 nonsense mediated mRNA decay factor* — 17p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.47× (z +9.1, q 7e-17, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.480× (z -17.3, q 0e+00, down in 44 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.834× (z -6.0, q 1e-07, down in 22 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (NCI-H23 0.138×, HCT15 0.0989×, A-172 0.230×, A549 0.223×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (SNU-1 0.106×, LOX-IMVI 0.192×, Hs 766T 0.233×; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 0.5 µM in 3 lines (MIA PaCa-2 0.543×, CFPAC-1 0.503×, J82 0.580×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KATNIP]] (+0.63, fdr 1e-05), [[ERC1]] (+0.58, fdr 1e-05), [[CHMP1A]] (+0.57, fdr 3e-05); moves opposite to [[TLCD4]] (-0.50, fdr 5e-05), [[NBN]] (-0.49, fdr 3e-05), [[DCAF17]] (-0.49, fdr 1e-04).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 945.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.47×** | +9.1 | 7e-17 | 38/48 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.29×** | +5.8 | 2e-06 | 32/47 (HS-578T, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.24×** | +4.9 | 1e-04 | 24/48 (PANC-1, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.23×** | +4.9 | 2e-04 | 25/48 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.19× | +4.1 | 0.005 | 21/47 (H4, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~55% of this change | 1.19× | +4.0 | 0.005 | 16/49 (CFPAC-1, LoVo, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +4.0 | 0.005 | 0/50 | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.055 | 20/50 (HS-578T, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.055 | 18/49 (A498, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.15× | +3.3 | 0.057 | 7/48 (LoVo, A498, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | 1.16× | +3.2 | 0.059 | 7/48 (A498, LoVo, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.19× | +3.2 | 0.059 | 21/50 (LOX-IMVI, HS-578T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.14× | +3.0 | 0.11 | 15/48 (A-172, NCI-H460, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 11 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 945.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (NCI-H23 0.138×, HCT15 0.0989×, A-172 0.230×, A549 0.223×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (SNU-1 0.106×, LOX-IMVI 0.192×, Hs 766T 0.233×; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 0.5 µM in 3 lines (MIA PaCa-2 0.543×, CFPAC-1 0.503×, J82 0.580×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.480×** | -17.3 | 0e+00 | 44/49 (NCI-H23, HCT15, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.471×** | -16.4 | 0e+00 | 41/45 (MIA PaCa-2, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.507×** | -15.4 | 0e+00 | 40/44 (SNU-1, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.576×** | -12.5 | 1e-33 | 44/47 (CFPAC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.681×** | -8.7 | 5e-16 | 37/48 (SNU-423, LS 180, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **0.747×** | -6.9 | 7e-10 | 35/48 (J82, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.834× | -6.0 | 1e-07 | 22/48 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.787×** | -5.7 | 1e-06 | 34/49 (COLO 205, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.791×** | -5.5 | 2e-06 | 25/48 (CFPAC-1, A-172, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.800×** | -5.3 | 8e-06 | 30/48 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **0.801×** | -5.0 | 3e-05 | 27/47 (LOX-IMVI, NCI-H1792, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.809×** | -5.0 | 3e-05 | 27/48 (MIA PaCa-2, C32, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.884× | -4.1 | 0.002 | 21/48 (A-172, SNU-423, …) | two highest doses | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.721×** | -3.8 | 0.007 | 20/38 (Panc 03.27, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.836× | -3.0 | 0.096 | 18/47 (CHP-212, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 945. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 303 | 0 | 13 (13 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.192× (z -20.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 275 | 1 (1 ⚠) | 8 (8 ⚠) | [[Selinexor (drug)]] 5 µM 1.51× (z +8.7) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -22.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[MIA PaCa-2 (line)]] | alt | 236 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.269× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.543× (z -9.4) |
| [[J82 (line)]] | alt | 187 | 0 | 7 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.423× (z -12.9) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.580× (z -8.5) |
| [[SNU-423 (line)]] | alt | 189 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.295× (z -15.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 151 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.385× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[CFPAC-1 (line)]] | alt | 118 | 0 | 6 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.188× (z -21.2) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.503× (z -9.1) |
| [[HOP62 (line)]] | alt | 209 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.379× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[NCI-H1792 (line)]] | alt | 152 | 1 (1 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +13.1) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.05 µM 0.285× (z -17.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 220 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -19.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[AsPC-1 (line)]] | alt | 137 | 0 | 5 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.381× (z -13.0) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 197 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.138× (z -31.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SW480 (line)]] | alt | 248 | 1 (1 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.67× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.369× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[Hs 766T (line)]] | wt | 146 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.233× (z -17.7) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 205 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.339× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[LoVo (line)]] | wt | 180 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +13.4) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.405× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[LS 180 (line)]] | wt | 139 | 1 (1 ⚠) | 3 (3 ⚠) | [[Selinexor (drug)]] 5 µM 1.61× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | [[Harringtonine (drug)]] 5 µM 0.413× (z -11.6) ⚠ cell-cycle shift, explains ~45% of this change |
| [[NCI-H460 (line)]] | wt | 175 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.51× (z +10.0) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.353× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[Panc 03.27 (line)]] | alt | 133 | 0 | 4 (4 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.110× (z -14.5) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 204 | 2 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +12.1) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.312× (z -17.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 188 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.306× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[HS-578T (line)]] | alt | 212 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.345× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SNU-1 (line)]] | wt | 151 | 2 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.106× (z -23.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 189 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[COLO 205 (line)]] | alt | 188 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -19.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[KATO III (line)]] | alt | 172 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.83× (z +9.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.434× (z -12.3) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 76.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.276× (z -14.1) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 173 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.345× (z -12.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 88.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +14.5) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.426× (z -9.1) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 131 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0986× (z -13.9) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 224 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.260× (z -9.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 238 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0989× (z -28.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[HepG2_C3A (line)]] | wt | 109 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.239× (z -12.7) ⚠ toxic |
| [[NCI-H596 (line)]] | alt | 167 | 0 | 1 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.271× (z -8.5) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H661 (line)]] | alt | 160 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.171× (z -10.6) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 101 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.419× (z -12.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 202 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SW 900 (line)]] | alt | 194 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.454× (z -10.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 125 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.411× (z -11.6) ⚠ toxic |
| [[A-427 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 183 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 143 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 137 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 174 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 945), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 4 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KATNIP]] | +0.63 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[ERC1]] | +0.58 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[CHMP1A]] | +0.57 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[IFT43]] | +0.56 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[EMC3]] | +0.56 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[MYO9B]] | +0.55 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[TRIR]] ⚠ | +0.54 | +0.50 / +0.49 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CEP89]] | +0.54 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[MEX3D]] | +0.54 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[RGS12]] | +0.54 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[VTI1A]] | +0.53 | +0.39 / +0.60 | both halves | 5e-05 |  |
| [[POLR2J4]] | +0.53 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[SIRT7]] | +0.53 | +0.35 / +0.49 | both halves | 1e-04 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLCD4]] | -0.50 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[NBN]] | -0.49 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[DCAF17]] | -0.49 | -0.57 / -0.36 | both halves | 1e-04 |  |
| [[ALDH9A1]] | -0.49 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[NAPEPLD]] | -0.49 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[GTF3A]] ⚠ | -0.49 | -0.44 / -0.46 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[DIS3L]] | -0.48 | -0.49 / -0.33 | both halves | 1e-04 | STRING 472 |
| [[LRRC58]] | -0.48 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[TTPA]] | -0.47 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[MANEA]] | -0.46 | -0.38 / -0.40 | both halves | 6e-05 |  |
| [[AGAP13P]] | -0.46 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[TIFA]] | -0.46 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[QPCT]] | -0.45 | -0.33 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers SMG6's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LLGL2]] | B | LLGL2 activity lowers SMG6's level | lines that do not express LLGL2 (12) vs lines expressing it (38) | 1.26× higher at baseline in the lines without LLGL2 | 0.094 | ⚠ within organs, on part of the lines; also absent: GRTP1, FGFR4, LSR |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.393). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-27.4, -12.0); signed map (-18.6, 2.7). **Vector** length 110, 35.1% of its response variance represented; |z| ≥ 3 in 1,224 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +6.5 | +9.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.4 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.4 | -0.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.2 | -2.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.1 | +4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.0 | -0.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.8 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +0.4 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +2.3 | +1.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -9.3 | -6.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -8.5 | -5.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.5 | -12.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -5.2 | -5.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -3.7 | -5.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -3.2 | -2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.5 | -2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | +0.8 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -2.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | SMG6 nonsense mediated mRNA decay factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.3 — chr17:2,059,839-2,303,785 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0732, SMG-6, EST1A; previously C17orf31 |
| Gene groups (HGNC) | Endoribonucleases; PIN-like domain superfamily |
| Reactome | 3 pathways, smallest: Nonsense Mediated Decay (NMD) enhanced by the Exon Junction Complex (EJC); Nonsense-Mediated Decay (NMD); Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86US8](https://www.uniprot.org/uniprotkb/Q86US8) (Telomerase-binding protein EST1A):

> Component of the telomerase ribonucleoprotein (RNP) complex that is essential for the replication of chromosome termini. May have a general role in telomere regulation. Promotes in vitro the ability of TERT to elongate telomeres. Overexpression induces telomere uncapping, chromosomal end-to-end fusions (telomeric DNA persists at the fusion points) and did not perturb TRF2 telomeric localization. Binds to the single-stranded 5'-(GTGTGG)(4)GTGT-3' telomeric DNA, but not to a telomerase RNA …

**Summary**, from NCBI Gene [23293](https://www.ncbi.nlm.nih.gov/gene/23293):

> This gene encodes a component of the telomerase ribonucleoprotein complex responsible for the replication and maintenance of chromosome ends. The encoded protein also plays a role in the nonsense-mediated mRNA decay (NMD) pathway, providing the endonuclease activity near the premature translation termination codon that is needed to initiate NMD. Alternatively spliced transcript variants encoding distinct protein isoforms have been described. [provided by RefSeq, Feb 2014]

**Accessions** — [HGNC:17809](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17809) · Entrez [23293](https://www.ncbi.nlm.nih.gov/gene/23293) · UniProt [Q86US8](https://www.uniprot.org/uniprotkb/Q86US8) · Ensembl [ENSG00000070366](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000070366)

## Data

Gene col 945: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 945); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 945, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 945]; `tensor/DDL_lfc|DDL_z.npy` [945]; `embed/gene_vectors.npy` [945]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 945 or target_col == 945). Every well: [[SMG6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMG6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
