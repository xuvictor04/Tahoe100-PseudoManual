---
symbol: "MASTL"
type: "gene"
col: 4191
ensembl_id: "ENSG00000120539"
name: "microtubule associated serine/threonine kinase like"
location: "10p12.1"
module: 91
arm: "+"
pooled_cpm: 49.85
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 12
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/091"]
generated_by: "tahoemap"
---

# MASTL

*microtubule associated serine/threonine kinase like* — 10p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (16 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.59× (z +11.8, q 1e-29, up in 34 of 48 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.24× (z +3.9, q 0.003, up in 21 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (J82 2.38×, NCI-H460 2.58×, NCI-H1573 2.58×, PANC-1 1.99×, …; ⚠ cell-cycle shift, explains ~30% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (AsPC-1 4.26×, SW1417 2.51×, SNU-423 2.51×, NCI-H2347 2.17×; ⚠ cell-cycle shift, explains ~26% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (NCI-H2347 3.16×, NCI-H1573 3.36×; ⚠ cell-cycle shift, explains ~26% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H2347 2.62×).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.621× (z -8.2, q 1e-13, down in 34 of 48 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.737× (z -5.6, q 5e-06, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BRCA2]] (+0.85, fdr 7e-06), [[ESCO2]] (+0.82, fdr 7e-06), [[ZGRF1]] (+0.76, fdr 7e-06).
> It is in [[Module 091]], a single-armed module (HDR through Homologous Recombination (HRR)).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 21 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4191.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (J82 2.38×, NCI-H460 2.58×, NCI-H1573 2.58×, PANC-1 1.99×, …; ⚠ cell-cycle shift, explains ~30% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (AsPC-1 4.26×, SW1417 2.51×, SNU-423 2.51×, NCI-H2347 2.17×; ⚠ cell-cycle shift, explains ~26% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (NCI-H2347 3.16×, NCI-H1573 3.36×; ⚠ cell-cycle shift, explains ~26% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H2347 2.62×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.59×** | +11.8 | 1e-29 | 34/48 (AsPC-1, SW1417, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.57×** | +11.4 | 7e-28 | 34/48 (J82, NCI-H460, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.79×** | +10.1 | 1e-21 | 39/48 (NCI-H2347, NCI-H1573, …) | rises with dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.48×** | +7.0 | 3e-10 | 29/48 (HOP62, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.45×** | +6.4 | 2e-08 | 26/47 (HOP62, SW480, …) | rises with dose |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.25×** | +5.7 | 1e-06 | 21/48 (RKO, HT-29, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.36×** | +5.6 | 2e-06 | 27/48 (NCI-H2347, HS-578T, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.32×** | +5.0 | 3e-05 | 24/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.32×** | +5.0 | 4e-05 | 23/48 (NCI-H460, HOP62, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +4.6 | 2e-04 | 1/48 (NCI-H1792) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.29×** | +4.6 | 2e-04 | 21/47 (J82, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.27×** | +4.2 | 0.001 | 22/48 (HOP62, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.26×** | +4.2 | 0.001 | 19/47 (NCI-H460, LS 180, …) | all doses, flat |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.25×** | +4.0 | 0.003 | 16/48 (HEC-1-A, PANC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.24×** | +3.9 | 0.003 | 21/47 (NCI-H2347, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +3.7 | 0.007 | 15/48 (SW1417, NCI-H2347, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.21×** | +3.5 | 0.015 | 16/48 (MIA PaCa-2, A498, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 0.5 µM |  | 1.20× | +3.2 | 0.032 | 14/48 (NCI-H2030, A-427, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 1.19× | +3.2 | 0.038 | 8/48 (MIA PaCa-2, LoVo, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.18× | +3.0 | 0.072 | 13/48 (SW480, SW 900, …) | rises with dose |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | 1.18× | +2.9 | 0.079 | 14/48 (A-427, HepG2/C3A, …) | top dose only | plate-row cell shift |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | 1.19× | +2.9 | 0.079 | 15/48 (A-427, LS 180, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4191.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.621×** | -8.2 | 1e-13 | 34/48 (A-172, MIA PaCa-2, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.770×** | -6.8 | 4e-09 | 29/48 (A498, MIA PaCa-2, …) | rises with dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.737×** | -5.6 | 5e-06 | 26/48 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.747×** | -5.3 | 1e-05 | 29/48 (SW48, BT-474, …) | two highest doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.753×** | -5.2 | 2e-05 | 26/48 (A498, A-172, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.583×** | -5.1 | 3e-05 | 24/43 (NCI-H23, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.829×** | -4.9 | 1e-04 | 22/48 (A-172, J82, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.769×** | -4.8 | 1e-04 | 25/48 (LoVo, C-33 A, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.839× | -4.6 | 3e-04 | 21/48 (LoVo, RKO, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.783×** | -4.5 | 4e-04 | 22/48 (H4, Hs 766T, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.845× | -4.4 | 6e-04 | 19/48 (A549, NCI-H23, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.735×** | -4.0 | 0.003 | 20/48 (SW480, KATO III, …) | two highest doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.860× | -3.9 | 0.004 | 18/48 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.868× | -3.7 | 0.010 | 16/48 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.877× | -3.4 | 0.024 | 10/48 (SNU-1, SHP-77, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.831×** | -3.4 | 0.024 | 18/48 (RPMI-7951, CFPAC-1, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.841× | -3.2 | 0.048 | 18/47 (Panc 03.27, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.841× | -3.1 | 0.069 | 12/48 (A498, NCI-H1573, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.850× | -3.0 | 0.085 | 11/48 (BT-474, NCI-H2030, …) | inconsistent across doses |  |
| [[Ixazomib (drug)]] 5 µM |  | **0.733×** | -3.0 | 0.085 | 13/48 (LoVo, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.53 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4191. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 33.5 | 5 (4 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.16× (z +10.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.62× (z +9.2) | — |
| [[PANC-1 (line)]] | alt | 36.3 | 3 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +11.1) ⚠ cell-cycle shift, explains ~30% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.381× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 113 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.275× (z -15.8) ⚠ cell-cycle shift, explains ~52% of this change |
| [[H4 (line)]] | wt | 27.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.183× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 80.8 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +13.8) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H1573 (line)]] | alt | 31.8 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +11.8) ⚠ cell-cycle shift, explains ~30% of this change | [[Dinaciclib (drug)]] 5 µM 0.273× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 29.6 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +12.2) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[HCT15 (line)]] | alt | 77.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.255× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 38.4 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.05× (z +9.7) ⚠ cell-cycle shift, explains ~58% of this change | — |
| [[HS-578T (line)]] | alt | 26.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +9.9) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[A-172 (line)]] | wt | 85.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.268× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 55.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.488× (z -9.5) ⚠ cell-cycle shift, explains ~52% of this change |
| [[AN3 CA (line)]] | alt | 44.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.118× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 33.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.26× (z +13.2) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[C32 (line)]] | wt | 16.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +10.6) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[COLO 205 (line)]] | alt | 37.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 29.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0911× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 42.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.356× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 30.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +9.2) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 75.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.400× (z -9.9) ⚠ cell-cycle shift, explains ~52% of this change |
| [[NCI-H2030 (line)]] | alt | 57.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +11.0) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H23 (line)]] | alt | 68.0 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0929× (z -10.8) ⚠ toxic |
| [[RKO (line)]] | wt | 71.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.177× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 55.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.288× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 38.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +10.9) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[SW 900 (line)]] | alt | 43.5 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +8.5) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[SW1417 (line)]] | alt | 45.2 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +11.9) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[SW48 (line)]] | wt | 43.7 | 0 | 1 | — | [[OTS514 (drug)]] 5 µM 0.0759× (z -8.5) |
| [[A-427 (line)]] | wt | 85.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 76.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 71.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 50.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 44.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 48.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4191), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRCA2]] | +0.85 | +0.81 / +0.87 | both halves | 7e-06 | **novel candidate** |
| [[ESCO2]] | +0.82 | +0.81 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[ZGRF1]] | +0.76 | +0.74 / +0.78 | both halves | 7e-06 |  |
| [[KIF24]] | +0.76 | +0.73 / +0.75 | both halves | 7e-06 |  |
| [[RMI2]] | +0.75 | +0.70 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[E2F8]] | +0.74 | +0.72 / +0.76 | both halves | 7e-06 |  |
| [[BRIP1]] | +0.74 | +0.77 / +0.74 | both halves | 7e-06 |  |
| [[CENPN]] | +0.74 | +0.76 / +0.73 | both halves | 7e-06 |  |
| [[ORC6]] | +0.73 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[USP1]] | +0.73 | +0.64 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[ATAD5]] | +0.73 | +0.72 / +0.73 | both halves | 7e-06 |  |
| [[BRCA1]] | +0.73 | +0.73 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MASTL's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 091]] — HDR through Homologous Recombination (HRR); 49 genes; every member is in the + arm (projection on the module's main direction 0.791). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-39.2, -47.7); signed map (-42.4, -47.1). **Vector** length 140, 43.1% of its response variance represented; |z| ≥ 3 in 1,262 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *HDR through Homologous Recombination (HRR)* (reactome, mean cos +0.66 to 5); *Resolution of D-loop Structures through Holliday Junction Intermediates* (reactome, mean cos +0.70 to 4); *Resolution of D-Loop Structures* (reactome, mean cos +0.70 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +6.4 | +10.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +5.9 | +6.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +5.2 | +11.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +4.8 | +5.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | +4.7 | +4.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +4.0 | +3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +3.7 |
|  | [[Thymol (drug)]] 5 µM |  | +2.8 | +2.5 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.8 | +2.7 |
|  | [[Raltitrexed (drug)]] 0.5 µM |  | +2.7 | +2.3 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -7.9 | -6.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.3 | -4.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | -5.9 | -8.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | -5.3 | -5.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -5.0 | -4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.8 | -5.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.1 | -3.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.9 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | microtubule associated serine/threonine kinase like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p12.1 — chr10:27,154,824-27,187,953 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14813, THC2, Gwl |
| Gene groups (HGNC) | Microtubule associated serine/threonine kinase family |
| Reactome | 5 pathways, smallest: MASTL Facilitates Mitotic Progression; Mitotic Prophase; M Phase |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96GX5](https://www.uniprot.org/uniprotkb/Q96GX5) (Serine/threonine-protein kinase greatwall):

> Serine/threonine kinase that plays a key role in M phase by acting as a regulator of mitosis entry and maintenance. Acts by promoting the inactivation of protein phosphatase 2A (PP2A) during M phase: does not directly inhibit PP2A but acts by mediating phosphorylation and subsequent activation of ARPP19 and ENSA at 'Ser-62' and 'Ser-67', respectively. ARPP19 and ENSA are phosphatase inhibitors that specifically inhibit the PPP2R2D (PR55-delta) subunit of PP2A. Inactivation of PP2A during M …

**Summary**, from NCBI Gene [84930](https://www.ncbi.nlm.nih.gov/gene/84930):

> This gene encodes a microtubule-associated serine/threonine kinase. Mutations at this locus have been associated with autosomal dominant thrombocytopenia, also known as thrombocytopenia-2. Alternatively spliced transcript variants have been described for this locus. [provided by RefSeq, Feb 2010]

**Accessions** — [HGNC:19042](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19042) · Entrez [84930](https://www.ncbi.nlm.nih.gov/gene/84930) · UniProt [Q96GX5](https://www.uniprot.org/uniprotkb/Q96GX5) · Ensembl [ENSG00000120539](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120539)

## Data

Gene col 4191: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4191); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4191, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4191]; `tensor/DDL_lfc|DDL_z.npy` [4191]; `embed/gene_vectors.npy` [4191]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4191 or target_col == 4191). Every well: [[MASTL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MASTL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
