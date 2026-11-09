---
symbol: "MYH10"
type: "gene"
col: 5403
ensembl_id: "ENSG00000133026"
name: "myosin heavy chain 10"
location: "17p13.1"
module: 164
arm: "+"
pooled_cpm: 104.66
n_lines_expressing: 40
n_dd_up: 11
n_dd_down: 16
n_dd_up_clean: 1
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 4
direction_downstream: 3
tags: ["gene", "module/164"]
generated_by: "tahoemap"
---

# MYH10

*myosin heavy chain 10* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.38× (z +11.2, q 3e-26, up in 24 of 39 measured lines) ⚠ cell-cycle shift, explains ~23% of this change. The strongest without an alert is [[Brivudine (drug)]] 5 µM: 1.69× (z +6.8, q 1e-09, up in 26 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Panobinostat (drug)]] 5 µM in 5 lines (PANC-1 2.50×, LoVo 2.71×, NCI-H460 2.96×, A549 2.15×, …; ⚠ cell-cycle shift, explains ~51% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SHP-77 1.81×, HEC-1-A 1.66×, SW480 1.83×; ⚠ cell-cycle shift, explains ~23% of this change); [[Panobinostat (drug)]] 0.5 µM in 3 lines (PANC-1 2.22×, LoVo 2.58×, NCI-H1573 2.73×; ⚠ cell-cycle shift, explains ~45% of this change).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.438× (z -19.6, q 0e+00, down in 35 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMAP2]] (+0.63, fdr 1e-05), [[P3H1]] (+0.62, fdr 1e-05), [[LNPK]] (+0.61, fdr 1e-05); moves opposite to [[SLC9A8]] (-0.63, fdr 1e-05), [[ZC3HC1]] (-0.62, fdr 8e-06), [[RPP38]] (-0.60, fdr 1e-05).
> It is in [[Module 164]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[ZNF594]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 10 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5403.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Panobinostat (drug)]] 5 µM in 5 lines (PANC-1 2.50×, LoVo 2.71×, NCI-H460 2.96×, A549 2.15×, …; ⚠ cell-cycle shift, explains ~51% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SHP-77 1.81×, HEC-1-A 1.66×, SW480 1.83×; ⚠ cell-cycle shift, explains ~23% of this change); [[Panobinostat (drug)]] 0.5 µM in 3 lines (PANC-1 2.22×, LoVo 2.58×, NCI-H1573 2.73×; ⚠ cell-cycle shift, explains ~45% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.38×** | +11.2 | 3e-26 | 24/39 (SHP-77, HEC-1-A, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.45×** | +9.2 | 1e-17 | 28/38 (PANC-1, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.44×** | +8.9 | 8e-17 | 25/38 (PANC-1, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.41×** | +8.5 | 3e-15 | 29/38 (PANC-1, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **1.34×** | +7.2 | 7e-11 | 21/39 (PANC-1, C32, …) | two highest doses | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.69×** | +6.8 | 1e-09 | 26/39 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **1.28×** | +5.9 | 2e-07 | 20/36 (C32, NCI-H1573, …) | two highest doses | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.26×** | +5.6 | 1e-06 | 23/38 (NCI-H460, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.25×** | +5.4 | 3e-06 | 20/38 (NCI-H23, A-427, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.23×** | +4.8 | 7e-05 | 18/38 (SW480, HEC-1-A, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.21×** | +4.5 | 3e-04 | 17/40 (SW480, C32, …) | top dose only |  |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 1.16× | +3.5 | 0.026 | 2/38 (NCI-H23, NCI-H1573) | top dose only | plate-row cell shift |
| [[Radotinib (drug)]] 5 µM |  | 1.10× | +3.4 | 0.033 | 5/38 (RPMI-7951, SK-MEL-2, …) | top dose only |  |
| [[Roxadustat (drug)]] 5 µM |  | 1.14× | +3.2 | 0.055 | 9/38 (SNU-423, HOP62, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.14× | +3.1 | 0.063 | 14/37 (LoVo, NCI-H2030, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5403.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.438×** | -19.6 | 0e+00 | 35/38 (SNU-423, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.648×** | -15.1 | 0e+00 | 31/38 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.614×** | -11.6 | 1e-28 | 29/38 (SW 900, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.615×** | -11.5 | 2e-28 | 33/37 (C32, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.651×** | -10.6 | 4e-24 | 26/38 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.666×** | -10.0 | 1e-21 | 25/38 (NCI-H2030, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.687×** | -9.3 | 2e-18 | 26/38 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.693×** | -9.1 | 1e-17 | 27/38 (SW 900, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.694×** | -9.0 | 2e-17 | 30/38 (A-172, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.707×** | -8.6 | 7e-16 | 29/38 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.814×** | -5.1 | 2e-05 | 19/38 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.866× | -5.0 | 3e-05 | 16/38 (A-172, C32, …) | rises with dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.838× | -4.4 | 6e-04 | 14/38 (C32, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.830×** | -4.3 | 6e-04 | 18/38 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.834× | -4.2 | 9e-04 | 14/37 (HEC-1-A, A-172, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.841× | -4.1 | 0.001 | 16/38 (NCI-H23, A-172, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 0.847× | -4.1 | 0.001 | 16/38 (RPMI-7951, HCT15, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.890× | -4.1 | 0.001 | 10/38 (A-172, C32, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.795×** | -4.0 | 0.002 | 14/38 (HOP62, HS-578T, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.865× | -3.6 | 0.009 | 14/38 (HOP62, C32, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5403. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 176 | 1 (1 ⚠) | 10 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.56× (z +8.6) ⚠ cell-cycle shift, explains ~23% of this change | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -18.3) |
| [[A549 (line)]] | wt | 109 | 2 (2 ⚠) | 6 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.15× (z +10.0) ⚠ cell-cycle shift, explains ~51% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.364× (z -12.7) |
| [[C32 (line)]] | wt | 257 | 2 (2 ⚠) | 6 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.26× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.351× (z -12.9) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.512× (z -12.2) |
| [[NCI-H460 (line)]] | wt | 47.9 | 3 (3 ⚠) | 5 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.96× (z +11.0) ⚠ cell-cycle shift, explains ~51% of this change | [[Homoharringtonine (drug)]] 0.05 µM 0.319× (z -11.6) |
| [[PANC-1 (line)]] | alt | 64.6 | 4 (4 ⚠) | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.50× (z +13.0) ⚠ cell-cycle shift, explains ~51% of this change | [[Digitoxin (drug)]] 0.5 µM 0.501× (z -9.8) |
| [[SNU-423 (line)]] | alt | 158 | 1 (1 ⚠) | 6 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.92× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.273× (z -16.5) |
| [[SW 900 (line)]] | alt | 168 | 0 | 6 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.249× (z -15.8) |
| [[HOP62 (line)]] | alt | 149 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -24.9) |
| [[NCI-H2030 (line)]] | alt | 125 | 2 (2 ⚠) | 3 | [[Panobinostat (drug)]] 5 µM 2.22× (z +10.0) ⚠ cell-cycle shift, explains ~51% of this change | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -13.2) |
| [[H4 (line)]] | wt | 95.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.173× (z -14.2) |
| [[J82 (line)]] | alt | 212 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.423× (z -12.8) |
| [[LoVo (line)]] | wt | 46.1 | 3 (3 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.71× (z +11.4) ⚠ cell-cycle shift, explains ~51% of this change | [[Digitoxin (drug)]] 0.5 µM 0.457× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 302 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.400× (z -13.6) |
| [[NCI-H1573 (line)]] | alt | 46.9 | 3 (3 ⚠) | 1 | [[Panobinostat (drug)]] 0.5 µM 2.73× (z +10.0) ⚠ cell-cycle shift, explains ~45% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.365× (z -10.0) |
| [[SNU-1 (line)]] | wt | 103 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.274× (z -10.0) |
| [[HCT15 (line)]] | alt | 135 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -11.2) |
| [[HEC-1-A (line)]] | alt | 237 | 2 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.66× (z +13.0) ⚠ cell-cycle shift, explains ~23% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.596× (z -9.1) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 79.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.268× (z -13.6) |
| [[SW480 (line)]] | alt | 196 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +13.0) ⚠ cell-cycle shift, explains ~23% of this change | — |
| [[A-427 (line)]] | wt | 158 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.504× (z -10.0) |
| [[AN3 CA (line)]] | alt | 244 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.299× (z -10.1) |
| [[NCI-H23 (line)]] | alt | 129 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.282× (z -13.9) |
| [[NCI-H2347 (line)]] | alt | 56.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.428× (z -10.3) |
| [[RPMI-7951 (line)]] | alt | 96.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -11.5) |
| [[BT-474 (line)]] | alt | 74.6 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.187× (z -9.0) ⚠ toxic |
| [[C-33 A (line)]] | alt | 292 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.67× (z +9.8) ⚠ cell-cycle shift, explains ~23% of this change | — |
| [[CFPAC-1 (line)]] | alt | 60.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.463× (z -8.6) |
| [[CHP-212 (line)]] | wt | 248 | 0 | 1 | — | [[DT-061 (drug)]] 5 µM 0.0644× (z -11.7) |
| [[HS-578T (line)]] | alt | 112 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.354× (z -12.0) |
| [[hTERT-HPNE (line)]] | wt | 49.3 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.327× (z -8.8) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 66.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.353× (z -10.4) |
| [[SHP-77 (line)]] | alt | 307 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +13.7) ⚠ cell-cycle shift, explains ~23% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 97.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.444× (z -9.2) |
| [[A498 (line)]] | wt | 19.1 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 11.8 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 103 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.9 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 22.7 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 11.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 98.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 225 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.0 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 76.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 83.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.7 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 12.9 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5403), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMAP2]] | +0.63 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[P3H1]] | +0.62 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[LNPK]] | +0.61 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[HERC3]] | +0.61 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[DPYSL2]] | +0.60 | +0.55 / +0.47 | both halves | 2e-05 | pathway: Semaphorin interactions |
| [[SETD3]] | +0.60 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[DDHD2]] | +0.60 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[BPNT2]] | +0.60 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[PGM2]] | +0.60 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[TMEM106C]] | +0.60 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[IDH2]] | +0.60 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[CCDC47]] | +0.60 | +0.46 / +0.60 | both halves | 3e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC9A8]] | -0.63 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[ZC3HC1]] | -0.62 | -0.57 / -0.58 | both halves | 8e-06 |  |
| [[RPP38]] | -0.60 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[MED18]] | -0.59 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[LIPT1]] | -0.58 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[ZNF594]] | -0.58 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[XIAP]] | -0.57 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[ZNF302]] | -0.57 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[N4BP2L2]] | -0.56 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[PHYKPL]] | -0.56 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[YTHDF2]] | -0.56 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[ITPA]] | -0.56 | -0.60 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MYH10's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity lowers MYH10's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZNF594]] | B | ZNF594 activity raises MYH10's level | lines that do not express ZNF594 (6) vs lines expressing it (44) | 3.52× lower at baseline in the lines without ZNF594 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with NF1; also absent: ZNF594-DT, MIR3659HG, SYNGR1 |
| [[HLTF]] | C | HLTF activity raises MYH10's level | lines that do not express HLTF (8) vs lines expressing it (42) | 6.01× lower at baseline in the lines without HLTF | 0.047 | ⚠ within organs, on part of the lines; also absent: HDGFL3, ZNF512B, FERMT2; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF594]] | B | MYH10 activity raises ZNF594's level | lines that do not express MYH10 (10) vs lines expressing it (40) | 2.45× lower at baseline in the lines without MYH10 | 0.015 | ⚠ within organs, on part of the lines; also absent: MAPT, MOCS1, GAMT |
| [[LAMB2P1]] | B | MYH10 activity raises LAMB2P1's level | lines that do not express MYH10 (10) vs lines expressing it (40) | 1.36× lower at baseline in the lines without MYH10 | 0.042 | ⚠ within organs, on part of the lines; also absent: MAPT, MOCS1, GAMT |
| [[SPICE1]] | B | MYH10 activity raises SPICE1's level | lines that do not express MYH10 (10) vs lines expressing it (40) | 1.14× lower at baseline in the lines without MYH10 | 0.089 | ⚠ within organs, on part of the lines; also absent: MAPT, MOCS1, GAMT |

## Where it sits

- **Module**: [[Module 164]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.566). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.37; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (8.0, -18.1); signed map (-51.6, -14.1). **Vector** length 119, 32.8% of its response variance represented; |z| ≥ 3 in 1,038 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | +5.4 | +7.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | +4.9 | +5.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +4.4 | +11.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +4.3 | +4.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +4.2 | +8.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.6 | +6.8 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +2.2 | +2.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +3.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.1 | +2.8 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | +1.9 | +2.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.6 | -19.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.8 | -11.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.1 | -9.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.5 | -11.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -5.4 | -5.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.2 | -8.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.4 | -4.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.2 | -4.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.2 | -2.4 |
|  | [[Temsirolimus (drug)]] 5 µM |  | -2.8 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | myosin heavy chain 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:8,474,207-8,631,376 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NMMHCB |
| Gene groups (HGNC) | Myosin heavy chains, class II |
| Hallmark sets | APICAL_JUNCTION, MITOTIC_SPINDLE |
| Reactome | 14 pathways, smallest: RHO GTPases Activate ROCKs; RHO GTPases activate CIT; Sema4D induced cell migration and growth-cone collapse |
| Matched by | ensembl_id |

**Function**, from UniProt [P35580](https://www.uniprot.org/uniprotkb/P35580) (Myosin-10):

> Cellular myosin that appears to play a role in cytokinesis, cell shape, and specialized functions such as secretion and capping. Involved with LARP6 in the stabilization of type I collagen mRNAs for CO1A1 and CO1A2. Plays a role in regulated exocytosis, probably by controlling early membrane remodeling of secretory granules after fusion with the cell membrane (By similarity). During cell spreading, plays an important role in cytoskeleton reorganization, focal contacts formation (in the central …

**Summary**, from NCBI Gene [4628](https://www.ncbi.nlm.nih.gov/gene/4628):

> This gene encodes a member of the myosin superfamily. The protein represents a conventional non-muscle myosin; it should not be confused with the unconventional myosin-10 (MYO10). Myosins are actin-dependent motor proteins with diverse functions including regulation of cytokinesis, cell motility, and cell polarity. Mutations in this gene have been associated with May-Hegglin anomaly and developmental defects in brain and heart. Multiple transcript variants encoding different isoforms have been …

**Accessions** — [HGNC:7568](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7568) · Entrez [4628](https://www.ncbi.nlm.nih.gov/gene/4628) · UniProt [P35580](https://www.uniprot.org/uniprotkb/P35580) · Ensembl [ENSG00000133026](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133026)

## Data

Gene col 5403: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5403); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5403, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5403]; `tensor/DDL_lfc|DDL_z.npy` [5403]; `embed/gene_vectors.npy` [5403]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5403 or target_col == 5403). Every well: [[MYH10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYH10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
