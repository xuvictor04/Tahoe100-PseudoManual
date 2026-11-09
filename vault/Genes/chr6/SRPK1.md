---
symbol: "SRPK1"
type: "gene"
col: 1760
ensembl_id: "ENSG00000096063"
name: "SRSF protein kinase 1"
location: "6p21.31"
module: 59
arm: "-"
pooled_cpm: 157.04
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 15
n_dd_up_clean: 9
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# SRPK1

*SRSF protein kinase 1* — 6p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (18 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.67× (z +13.5, q 1e-38, up in 39 of 48 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 1.55× (z +11.6, q 5e-29, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Trametinib (drug)]] 0.5 µM: 0.752× (z -9.1, q 7e-17, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTL]] (+0.67, fdr 7e-06), [[PLGRKT]] (+0.65, fdr 1e-05), [[STK39]] (+0.64, fdr 7e-06); moves opposite to [[CLIP3]] (-0.63, fdr 7e-06), [[VIRMA]] (-0.59, fdr 8e-06), [[PI4KB]] (-0.58, fdr 1e-05).
> It sits in the **-** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[BMAL2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 21 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1760.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.67×** | +13.5 | 1e-38 | 39/48 (PANC-1, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +13.1 | 1e-36 | 42/47 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.59×** | +12.2 | 9e-32 | 37/48 (PANC-1, SNU-423, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.55×** | +11.6 | 5e-29 | 39/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.51×** | +10.9 | 2e-25 | 40/48 (SW480, SNU-423, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.48×** | +9.9 | 3e-21 | 38/48 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.42×** | +9.2 | 3e-18 | 37/48 (HT-29, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.36×** | +8.0 | 7e-14 | 31/48 (HT-29, SW1417, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.35×** | +7.9 | 2e-13 | 37/48 (SNU-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.35×** | +7.7 | 1e-12 | 32/48 (C32, H4, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.34×** | +7.7 | 1e-12 | 33/47 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.31×** | +7.2 | 4e-11 | 31/48 (SW1417, HT-29, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.21×** | +7.0 | 8e-11 | 24/48 (CFPAC-1, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.29×** | +6.7 | 1e-09 | 27/48 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.28×** | +6.5 | 2e-09 | 27/48 (SW 900, H4, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +6.2 | 2e-08 | 22/49 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.26×** | +6.1 | 3e-08 | 26/48 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.26×** | +5.9 | 1e-07 | 26/47 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +5.8 | 2e-07 | 28/48 (HT-29, MIA PaCa-2, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 1.19× | +4.5 | 1e-04 | 22/48 (H4, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.19× | +4.5 | 1e-04 | 21/48 (MIA PaCa-2, A498, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 1.19× | +4.5 | 1e-04 | 23/48 (MIA PaCa-2, NCI-H23, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.16× | +3.9 | 0.002 | 19/47 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.21×** | +3.9 | 0.002 | 20/48 (SNU-423, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.14× | +3.4 | 0.011 | 17/48 (LOX-IMVI, NCI-H1573, …) | top dose only |  |
| [[vincristine (drug)]] 5 µM |  | **1.27×** | +2.8 | 0.080 | 12/46 (NCI-H23, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.27×** | +2.8 | 0.086 | 10/48 (RPMI-7951, HOP62, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1760.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.5 µM |  | **0.752×** | -9.1 | 7e-17 | 33/48 (NCI-H23, BT-474, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.739×** | -7.7 | 5e-12 | 36/48 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.760×** | -7.2 | 1e-10 | 30/48 (KATO III, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.763×** | -7.1 | 2e-10 | 32/49 (NCI-H23, BT-474, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.778×** | -6.9 | 6e-10 | 31/50 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.783×** | -6.4 | 1e-08 | 31/47 (NCI-H23, SW480, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.786×** | -6.2 | 4e-08 | 28/49 (NCI-H23, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.825×** | -6.1 | 1e-07 | 23/48 (NCI-H23, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.602×** | -5.9 | 2e-07 | 32/47 (RKO, A549, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.797×** | -5.7 | 6e-07 | 28/47 (NCI-H23, BT-474, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | **0.798×** | -5.5 | 2e-06 | 25/47 (RKO, NCI-H23, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.848× | -5.4 | 3e-06 | 18/49 (NCI-H23, SW480, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.871× | -4.8 | 6e-05 | 19/48 (NCI-H23, SW480, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.820×** | -4.8 | 6e-05 | 25/48 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | 0.881× | -4.7 | 9e-05 | 19/48 (A-427, RKO, …) | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.841× | -4.6 | 2e-04 | 22/48 (KATO III, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Ixazomib (drug)]] 5 µM |  | **0.716×** | -3.9 | 0.003 | 20/48 (NCI-H23, A498, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1760. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 318 | 1 (1 ⚠) | 14 (3 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.89× (z +9.7) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -26.3) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Trametinib (drug)]] 0.5 µM 0.469× (z -14.6) |
| [[HT-29 (line)]] | alt | 110 | 8 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +15.1) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.19× (z +10.0) | — |
| [[SW480 (line)]] | alt | 161 | 8 (6 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.23× (z +12.2) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.93× (z +10.4) | — |
| [[H4 (line)]] | wt | 93.2 | 7 (5 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.50× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.10× (z +9.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 268 | 7 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.02× (z +10.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.95× (z +10.0) | — |
| [[PANC-1 (line)]] | alt | 176 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +13.4) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.78× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 142 | 6 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +10.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.08× (z +9.0) | — |
| [[CFPAC-1 (line)]] | alt | 140 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +15.9) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[NCI-H460 (line)]] | wt | 125 | 5 (4 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.53× (z +12.2) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 1.98× (z +9.3) | — |
| [[Hs 766T (line)]] | wt | 92.4 | 4 (4 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.83× (z +10.6) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[RKO (line)]] | wt | 312 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.316× (z -16.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 107 | 4 (4 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.10× (z +10.5) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[A-427 (line)]] | wt | 147 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.426× (z -12.6) ⚠ cell-cycle shift, explains ~5% of this change |
| [[A498 (line)]] | wt | 128 | 2 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.90× (z +10.5) ⚠ cell-cycle shift, explains ~28% of this change | [[Selinexor (drug)]] 5 µM 0.660× (z -9.5) ⚠ cell-cycle shift, explains ~72% of this change |
| [[HOP62 (line)]] | alt | 139 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +12.7) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[KATO III (line)]] | alt | 140 | 0 | 3 | — | [[Ponatinib (drug)]] 5 µM 0.434× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 139 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.527× (z -10.5) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.516× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 109 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +10.8) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[BT-474 (line)]] | alt | 149 | 0 | 2 | — | [[Cobimetinib (drug)]] 5 µM 0.453× (z -9.0) |
| [[COLO 205 (line)]] | alt | 74.3 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 2.94× (z +8.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.89× (z +8.7) | — |
| [[LS 180 (line)]] | wt | 197 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.22× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[SNU-1 (line)]] | wt | 186 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.19× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.396× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 97.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.69× (z +9.9) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[A549 (line)]] | wt | 190 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.550× (z -11.1) ⚠ cell-cycle shift, explains ~63% of this change |
| [[C32 (line)]] | wt | 82.0 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +8.6) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 80.3 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +9.3) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[LoVo (line)]] | wt | 175 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.05× (z +9.9) ⚠ toxic | — |
| [[Panc 03.27 (line)]] | alt | 199 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +10.0) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[SHP-77 (line)]] | alt | 139 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.89× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[AN3 CA (line)]] | alt | 202 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 207 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 124 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 192 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 281 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 144 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 193 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 76.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 256 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1760), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTL]] | +0.67 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[PLGRKT]] | +0.65 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[STK39]] | +0.64 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[GART]] | +0.62 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[THSD4]] | +0.61 | +0.57 / +0.61 | both halves | 8e-06 |  |
| [[SCLY]] | +0.61 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[CDH4]] | +0.60 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[MTAP]] | +0.60 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[ASAP2]] | +0.60 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[CBFB]] | +0.59 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[DOCK1]] | +0.59 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[LYAR]] | +0.59 | +0.61 / +0.51 | both halves | 1e-05 | STRING 531 |

## Genes that move opposite

*33 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLIP3]] | -0.63 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[VIRMA]] | -0.59 | -0.58 / -0.61 | both halves | 8e-06 |  |
| [[PI4KB]] | -0.58 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[SPOP]] | -0.57 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[THAP8]] | -0.57 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[OSCP1]] | -0.57 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[TSC1]] | -0.57 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[IQUB]] | -0.57 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[DNAJC27]] | -0.56 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[KLC4]] | -0.56 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[ARMCX3]] | -0.56 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[SECISBP2L]] | -0.55 | -0.57 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises SRPK1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[PHLDA3]] | B | PHLDA3 activity lowers SRPK1's level | lines that do not express PHLDA3 (8) vs lines expressing it (42) | 1.49× higher at baseline in the lines without PHLDA3 | 0.062 | ⚠ within organs, on part of the lines; also absent: EFNB2, PELI1, RPLP0P2 |
| [[ABCA3]] | B | ABCA3 activity raises SRPK1's level | lines that do not express ABCA3 (9) vs lines expressing it (41) | 1.43× lower at baseline in the lines without ABCA3 | 0.068 | ⚠ within organs, on part of the lines; also absent: SLC37A1, CCDC88C, GRTP1; maybe low, not absent |
| [[ATL1]] | B | ATL1 activity lowers SRPK1's level | lines that do not express ATL1 (7) vs lines expressing it (43) | 1.44× higher at baseline in the lines without ATL1 | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000236283, LSMEM2; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BMAL2]] | C | SRPK1's natural level strengthens BMAL2's drug response | SRPK1's natural level across 42 lines (lineage-adjusted; a glimpse) | r +0.71, reverse -0.19; direction not clear | 0.040 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **-** arm (projection on the module's main direction -0.618). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (40.6, 8.0); signed map (7.7, 43.4). **Vector** length 124, 44.0% of its response variance represented; |z| ≥ 3 in 1,710 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +6.0 | +7.7 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +5.5 | +6.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +5.2 | +6.3 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +5.0 | +5.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.8 | +3.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.8 | +5.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.7 | +6.2 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.8 | +3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.6 | +6.1 |
|  | [[vincristine (drug)]] 5 µM |  | +3.2 | +2.8 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -7.6 | +0.1 |
|  | [[NG25 (drug)]] 5 µM |  | -7.3 | -5.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -6.4 | -7.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -6.3 | -9.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | -5.8 | -4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.3 | -7.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.2 | +1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -5.0 | -7.7 |

## What is on record

|  |  |
|---|---|
| Name | SRSF protein kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.31 — chr6:35,832,966-35,921,342 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SFRSK1 |
| Gene groups (HGNC) | SRSF protein kinase family |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 8 pathways, smallest: Replacement of protamines by nucleosomes in the male pronucleus; Maturation of nucleoprotein_9694631; Translation of Structural Proteins_9694635 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96SB4](https://www.uniprot.org/uniprotkb/Q96SB4) (SRSF protein kinase 1):

> Serine/arginine-rich protein-specific kinase which specifically phosphorylates its substrates at serine residues located in regions rich in arginine/serine dipeptides, known as RS domains and is involved in the phosphorylation of SR splicing factors and the regulation of splicing. Plays a central role in the regulatory network for splicing, controlling the intranuclear distribution of splicing factors in interphase cells and the reorganization of nuclear speckles during mitosis. Can influence …

**Summary**, from NCBI Gene [6732](https://www.ncbi.nlm.nih.gov/gene/6732):

> This gene encodes a serine/arginine protein kinase specific for the SR (serine/arginine-rich domain) family of splicing factors. The protein localizes to the nucleus and the cytoplasm. It is thought to play a role in regulation of both constitutive and alternative splicing by regulating intracellular localization of splicing factors. Alternative splicing of this gene results in multiple transcript variants. Additional alternatively spliced transcript variants have been described for this gene, …

**Accessions** — [HGNC:11305](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11305) · Entrez [6732](https://www.ncbi.nlm.nih.gov/gene/6732) · UniProt [Q96SB4](https://www.uniprot.org/uniprotkb/Q96SB4) · Ensembl [ENSG00000096063](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000096063)

## Data

Gene col 1760: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1760); `tables/drug_effects.parquet` (66 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1760, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1760]; `tensor/DDL_lfc|DDL_z.npy` [1760]; `embed/gene_vectors.npy` [1760]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1760 or target_col == 1760). Every well: [[SRPK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRPK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
