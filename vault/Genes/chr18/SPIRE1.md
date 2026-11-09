---
symbol: "SPIRE1"
type: "gene"
col: 5535
ensembl_id: "ENSG00000134278"
name: "spire type actin nucleation factor 1"
location: "18p11.21"
module: 227
arm: "+"
pooled_cpm: 168.58
n_lines_expressing: 47
n_dd_up: 14
n_dd_down: 12
n_dd_up_clean: 12
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 8
tags: ["gene", "module/227"]
generated_by: "tahoemap"
---

# SPIRE1

*spire type actin nucleation factor 1* — 18p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Daptomycin (drug)]] 5 µM: 1.39× (z +7.7, q 7e-12, up in 35 of 45 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.39× (z +7.4, q 4e-11, up in 30 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.641× (z -14.6, q 1e-45, down in 35 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CSGALNACT2]] (+0.63, fdr 1e-05), [[GAB2]] (+0.59, fdr 1e-05), [[DOP1B]] (+0.59, fdr 2e-05); moves opposite to [[HFE]] (-0.63, fdr 3e-05), [[C5orf15]] (-0.59, fdr 3e-05), [[BCLAF1]] (-0.57, fdr 3e-05).
> It is in [[Module 227]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 8 go from it, the strongest it → [[LARP6]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 17 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5535.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.39×** | +7.7 | 7e-12 | 35/45 (BT-474, NCI-H23, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.39×** | +7.4 | 4e-11 | 30/44 (hTERT-HPNE, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.21×** | +6.3 | 6e-08 | 26/46 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 1.19× | +5.7 | 2e-06 | 20/45 (BT-474, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.27×** | +5.5 | 5e-06 | 24/45 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.26×** | +5.4 | 6e-06 | 28/45 (HEC-1-A, Hs 766T, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.26×** | +5.4 | 7e-06 | 27/44 (hTERT-HPNE, A-172, …) | rises with dose | low cells (technical?) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.25×** | +5.2 | 1e-05 | 26/44 (BT-474, NCI-H460, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.17× | +5.2 | 1e-05 | 20/45 (SK-MEL-2, LoVo, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.16× | +4.9 | 6e-05 | 12/45 (HepG2/C3A, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.23×** | +4.9 | 6e-05 | 23/45 (BT-474, MIA PaCa-2, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.21×** | +4.3 | 8e-04 | 22/44 (NCI-H23, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.22×** | +4.3 | 8e-04 | 20/45 (MIA PaCa-2, H4, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 5 µM |  | 1.14× | +4.3 | 8e-04 | 8/46 (HepG2/C3A, NCI-H1573, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.48×** | +4.2 | 9e-04 | 23/45 (AsPC-1, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (drug)]] 5 µM |  | 1.19× | +4.0 | 0.002 | 18/45 (SK-MEL-2, NCI-H460, …) | top dose only |  |
| [[Artesunate (drug)]] 0.5 µM |  | 1.19× | +4.0 | 0.002 | 16/45 (BT-474, J82, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.44×** | +3.9 | 0.002 | 23/46 (LoVo, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5535.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.641×** | -14.6 | 1e-45 | 35/46 (HS-578T, PANC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.566×** | -13.2 | 2e-37 | 40/46 (PANC-1, HOP62, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.568×** | -12.2 | 8e-32 | 36/43 (C32, PANC-1, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.583×** | -12.1 | 3e-31 | 35/42 (PANC-1, C-33 A, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.640×** | -10.0 | 2e-21 | 33/44 (HepG2/C3A, A498, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.658×** | -9.4 | 7e-19 | 38/47 (HS-578T, HOP62, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.693×** | -8.2 | 2e-14 | 31/45 (HS-578T, NCI-H2030, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.471×** | -8.1 | 5e-14 | 31/46 (RKO, HS-578T, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.827×** | -6.2 | 3e-08 | 22/45 (A-172, HOP62, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **0.777×** | -5.9 | 3e-07 | 26/45 (SW 1271, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.825×** | -4.5 | 4e-04 | 20/45 (NCI-H1792, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.05 µM |  | 0.851× | -3.7 | 0.008 | 14/45 (H4, AsPC-1, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.713×** | -3.6 | 0.012 | 18/44 (NCI-H23, NCI-H460, …) | top dose only | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.857× | -3.6 | 0.014 | 15/45 (NCI-H460, HT-29, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | 0.858× | -3.4 | 0.022 | 19/45 (HS-578T, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.867× | -3.3 | 0.031 | 12/45 (AsPC-1, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5535. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 176 | 0 | 13 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -20.6) |
| [[A-172 (line)]] | wt | 275 | 0 | 9 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -15.6) |
| [[MIA PaCa-2 (line)]] | alt | 309 | 4 (2 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.57× (z +14.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 1.83× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.332× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.568× (z -9.4) |
| [[HOP62 (line)]] | alt | 273 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.297× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -12.2) |
| [[C32 (line)]] | wt | 189 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.265× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -12.3) |
| [[NCI-H1792 (line)]] | alt | 231 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -15.3) |
| [[A498 (line)]] | wt | 164 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.436× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.617× (z -9.9) |
| [[BT-474 (line)]] | alt | 140 | 5 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.54× (z +9.2) | — |
| [[J82 (line)]] | alt | 204 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -13.6) |
| [[NCI-H23 (line)]] | alt | 160 | 3 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.81× (z +11.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 1.79× (z +9.2) | [[Adagrasib (drug)]] 0.05 µM 0.584× (z -20.3) ⚠ position not correctable |
| [[PANC-1 (line)]] | alt | 292 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.306× (z -19.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -19.0) |
| [[AsPC-1 (line)]] | alt | 158 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -14.3) |
| [[hTERT-HPNE (line)]] | wt | 171 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.292× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -10.0) |
| [[A-427 (line)]] | wt | 283 | 2 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.83× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.371× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[Hs 766T (line)]] | wt | 210 | 1 | 2 (2 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 1.84× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.349× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[LOX-IMVI (line)]] | wt | 135 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.52× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.532× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H2030 (line)]] | alt | 318 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -13.7) |
| [[SW 900 (line)]] | alt | 253 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.423× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.623× (z -8.5) |
| [[SW480 (line)]] | alt | 124 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +11.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -10.1) ⚠ cell-cycle shift, explains ~33% of this change |
| [[A549 (line)]] | wt | 126 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.614× (z -8.6) |
| [[C-33 A (line)]] | alt | 200 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.296× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[HepG2_C3A (line)]] | wt | 222 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.211× (z -17.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -11.4) |
| [[NCI-H460 (line)]] | wt | 158 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.447× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[SNU-423 (line)]] | alt | 115 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -10.8) ⚠ cell-cycle shift, explains ~33% of this change |
| [[CFPAC-1 (line)]] | alt | 85.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.577× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 60.6 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.11× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LoVo (line)]] | wt | 178 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.385× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[LS 180 (line)]] | wt | 93.5 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.403× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 200 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.59× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2347 (line)]] | alt | 128 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.528× (z -12.2) |
| [[RKO (line)]] | wt | 175 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.183× (z -10.5) |
| [[SW 1271 (line)]] | alt | 168 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0697× (z -14.3) ⚠ transcription drop; cell-cycle shift, explains ~44% of this change |
| [[AN3 CA (line)]] | alt | 201 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.3 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 90.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 74.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 91.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 78.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 123 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 74.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.4 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5535), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSGALNACT2]] | +0.63 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[GAB2]] | +0.59 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[DOP1B]] | +0.59 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[PFDN2]] | +0.58 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[WIPI1]] | +0.57 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[CCDC112]] | +0.57 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[LRRFIP1]] | +0.57 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[AAK1]] | +0.57 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[RUSC2]] | +0.57 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[MARK3]] | +0.55 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[ARHGEF2]] | +0.55 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[SLC25A29]] | +0.54 | +0.52 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HFE]] | -0.63 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[C5orf15]] | -0.59 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[BCLAF1]] | -0.57 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[RBM4]] | -0.57 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[TET2]] | -0.56 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[FUBP1]] | -0.53 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[MINDY1]] | -0.53 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[DUSP19]] | -0.52 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[KLHL3]] | -0.52 | -0.40 / -0.38 | both halves | 6e-05 |  |
| [[SNHG31]] | -0.51 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[RPRD1B]] | -0.51 | -0.37 / -0.39 | both halves | 7e-05 |  |
| [[WBP11]] | -0.51 | -0.39 / -0.49 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SPIRE1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FSD1L]] | C | FSD1L activity raises SPIRE1's level | lines that do not express FSD1L (3) vs lines expressing it (47) | 4.79× lower at baseline in the lines without FSD1L | 0.003 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: DPF1, PPP2R3A, NKAIN1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LARP6]] | C | SPIRE1 activity raises LARP6's level | lines that do not express SPIRE1 (3) vs lines expressing it (47) | 6.22× lower at baseline in the lines without SPIRE1 | 0.014 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: NME4, CIBAR1, BMS1P23 |
| [[FSD1L]] | C | [[DENND5A]], SPIRE1 activity raises FSD1L's level | lines that do not express DENND5A, SPIRE1 (3) vs lines expressing them (47) | 4.09× lower at baseline in the lines without DENND5A, SPIRE1 | 0.015 | ⚠ few lines (3 vs 47); across organs; co-occurs with CTNNB1; also absent: NME4, CIBAR1, BMS1P23; co-absent with the target; co-absent genes |
| [[TTC7B]] | C | [[DENND5A]], SPIRE1 activity raises TTC7B's level | lines that do not express DENND5A, SPIRE1 (3) vs lines expressing them (47) | 6.81× lower at baseline in the lines without DENND5A, SPIRE1 | 0.023 | ⚠ few lines (3 vs 47); across organs; co-occurs with CTNNB1; also absent: NME4, CIBAR1, BMS1P23; co-absent genes |
| cells under [[Lonafarnib (drug)]] 5 µM | C | [[DENND5A]], [[FRMD6-AS2]], SPIRE1 activity raises the cells' numbers under Lonafarnib 5 µM (protects the cells) | lines that do not express DENND5A, FRMD6-AS2, SPIRE1 (3) vs lines expressing them (45) | the lines without DENND5A, FRMD6-AS2, SPIRE1: 0.11× the cells of the other lines | 0.027 | ⚠ few lines (3 vs 47); across organs; co-occurs with CTNNB1; also absent: NME4, CIBAR1, BMS1P23; co-absent genes |
| [[CLTCL1]] | C | SPIRE1 activity raises CLTCL1's level | lines that do not express SPIRE1 (3) vs lines expressing it (47) | 3.90× lower at baseline in the lines without SPIRE1 | 0.034 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: NME4, CIBAR1, BMS1P23; co-absent with the target |
| [[MPST]] | C | SPIRE1 activity lowers MPST's level | lines that do not express SPIRE1 (3) vs lines expressing it (47) | 2.35× higher at baseline in the lines without SPIRE1 | 0.039 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: NME4, CIBAR1, BMS1P23 |
| [[PPP2R3A]] | C | SPIRE1 activity raises PPP2R3A's level | lines that do not express SPIRE1 (3) vs lines expressing it (47) | 3.65× lower at baseline in the lines without SPIRE1 | 0.069 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: NME4, CIBAR1, BMS1P23 |
| [[BCLAF1]] | C | SPIRE1 activity lowers BCLAF1's level | lines that do not express SPIRE1 (3) vs lines expressing it (47) | 1.63× higher at baseline in the lines without SPIRE1 | 0.083 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: NME4, CIBAR1, BMS1P23 |

## Where it sits

- **Module**: [[Module 227]]; 9 genes; every member is in the + arm (projection on the module's main direction 0.735). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (14.7, 3.3); signed map (-27.4, 4.5). **Vector** length 124, 39.1% of its response variance represented; |z| ≥ 3 in 1,522 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +7.6 | +6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.1 | +4.9 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +7.0 | +7.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +6.3 | +5.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +6.0 | +4.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +5.5 | +3.6 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -7.8 | -8.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -14.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.2 | -0.5 |
|  | [[NG25 (drug)]] 5 µM |  | -4.6 | -3.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -4.3 | -8.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.8 | -6.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.0 | -2.0 |
|  | [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | -2.5 | -1.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.4 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | spire type actin nucleation factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.21 — chr18:12,446,512-12,658,107 (-) |
| Ensembl biotype | protein_coding |
| Also known as | spir-1, KIAA1135 |
| Gene groups (HGNC) | KIND domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q08AE8](https://www.uniprot.org/uniprotkb/Q08AE8) (Protein spire homolog 1):

> Acts as an actin nucleation factor, remains associated with the slow-growing pointed end of the new filament. Involved in intracellular vesicle transport along actin fibers, providing a novel link between actin cytoskeleton dynamics and intracellular transport. Required for asymmetric spindle positioning and asymmetric cell division during meiosis. Required for normal formation of the cleavage furrow and for polar body extrusion during female germ cell meiosis. Also acts in the nucleus: …

**Summary**, from NCBI Gene [56907](https://www.ncbi.nlm.nih.gov/gene/56907):

> Spire proteins, such as SPIRE1, are highly conserved between species. They belong to the family of Wiskott-Aldrich homology region-2 (WH2) proteins, which are involved in actin organization (Kerkhoff et al., 2001 [PubMed 11747823]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:30622](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30622) · Entrez [56907](https://www.ncbi.nlm.nih.gov/gene/56907) · UniProt [Q08AE8](https://www.uniprot.org/uniprotkb/Q08AE8) · Ensembl [ENSG00000134278](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134278)

## Data

Gene col 5535: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5535); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5535, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5535]; `tensor/DDL_lfc|DDL_z.npy` [5535]; `embed/gene_vectors.npy` [5535]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5535 or target_col == 5535). Every well: [[SPIRE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPIRE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
