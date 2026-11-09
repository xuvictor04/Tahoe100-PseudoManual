---
symbol: "TVP23C-CDRT4"
type: "gene"
col: 15163
ensembl_id: "ENSG00000259024"
name: "TVP23C-CDRT4 readthrough"
location: "17p12"
module: 56
arm: "+"
pooled_cpm: 38.69
n_lines_expressing: 48
n_dd_up: 2
n_dd_down: 39
n_dd_up_clean: 1
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# TVP23C-CDRT4

*TVP23C-CDRT4 readthrough* — 17p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.29× (z +4.2, q 0.015, up in 21 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (C32 4.98×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change).
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (22 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.346× (z -15.3, q 0e+00, down in 40 of 46 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.201× (z -14.1, q 9e-43, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDRT4]] (+0.92, fdr 7e-06, ⚠ same locus), [[TVP23C]] (+0.82, fdr 7e-06, ⚠ same locus), [[LINC02804]] (+0.66, fdr 4e-05), [[IL20RB]] (+0.66, fdr 7e-06), [[DHDDS]] (+0.65, fdr 7e-06); moves opposite to [[THAP12]] (-0.59, fdr 1e-05), [[SINHCAF]] (-0.59, fdr 1e-05), [[YAP1]] (-0.55, fdr 2e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15163.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (C32 4.98×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +4.2 | 0.015 | 21/46 (HT-29, SW1417, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.24×** | +3.6 | 0.095 | 12/46 (HCT15, NCI-H460, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~89% of this change | 1.23× | +3.4 | 0.11 | 14/46 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.21× | +3.2 | 0.22 | 14/46 (A-172, HOP62, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 0.05 µM |  | 1.21× | +3.0 | 0.23 | 9/46 (LoVo, SW480, …) | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 1.23× | +3.0 | 0.23 | 8/47 (MIA PaCa-2, HEC-1-A, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 23 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15163.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.346×** | -15.3 | 0e+00 | 40/46 (A-172, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.409×** | -15.0 | 0e+00 | 33/46 (HS-578T, LoVo, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.540×** | -14.6 | 0e+00 | 39/45 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.426×** | -14.3 | 2e-44 | 40/46 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.201×** | -14.1 | 9e-43 | 42/47 (A-172, A549, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.447×** | -13.5 | 1e-39 | 36/46 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.583×** | -12.8 | 2e-35 | 36/46 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.480×** | -10.6 | 2e-24 | 28/35 (HEC-1-A, KATO III, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.520×** | -10.1 | 2e-22 | 31/39 (CFPAC-1, HOP62, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.570×** | -9.4 | 2e-19 | 30/46 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **0.540×** | -8.9 | 3e-17 | 32/45 (MIA PaCa-2, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.611×** | -8.3 | 7e-15 | 33/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.574×** | -8.0 | 4e-14 | 31/45 (KATO III, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **0.621×** | -8.0 | 5e-14 | 29/45 (HS-578T, HCT15, …) | inconsistent across doses | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **0.403×** | -8.0 | 7e-14 | 32/45 (A-172, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.730×** | -4.5 | 1e-04 | 21/46 (NCI-H1792, A549, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.596×** | -4.5 | 1e-04 | 21/45 (SNU-423, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.766×** | -4.5 | 2e-04 | 23/46 (A549, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.756×** | -4.3 | 3e-04 | 21/45 (NCI-H460, SW48, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Budesonide (drug)]] 0.05 µM |  | **0.792×** | -3.9 | 0.002 | 18/46 (NCI-H1792, A549, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.741×** | -3.6 | 0.006 | 16/46 (HCT15, NCI-H460, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.861× | -3.6 | 0.006 | 19/46 (LoVo, CFPAC-1, …) | top dose only |  |
| [[vincristine (drug)]] 5 µM |  | **0.669×** | -3.5 | 0.007 | 14/42 (NCI-H460, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.801×** | -3.5 | 0.007 | 14/45 (HEC-1-A, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **0.678×** | -3.4 | 0.010 | 11/46 (CFPAC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.801×** | -3.2 | 0.020 | 12/46 (NCI-H460, A-172, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15163. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 62.3 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -20.2) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -15.0) |
| [[PANC-1 (line)]] | alt | 22.2 | 0 | 11 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -21.5) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.301× (z -11.3) |
| [[A-172 (line)]] | wt | 56.6 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -19.2) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.175× (z -17.0) |
| [[NCI-H460 (line)]] | wt | 50.5 | 0 | 10 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -16.4) |
| [[A498 (line)]] | wt | 66.8 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -17.6) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -12.9) |
| [[HS-578T (line)]] | alt | 58.4 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -18.2) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -12.4) |
| [[KATO III (line)]] | alt | 48.8 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.108× (z -9.4) |
| [[SNU-423 (line)]] | alt | 45.9 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -16.6) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -11.8) |
| [[HOP62 (line)]] | alt | 75.0 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.167× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -12.3) |
| [[NCI-H1573 (line)]] | alt | 27.8 | 0 | 5 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.146× (z -15.2) ⚠ cell-cycle shift, explains ~37% of this change |
| [[AsPC-1 (line)]] | alt | 23.6 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.225× (z -13.4) |
| [[H4 (line)]] | wt | 50.5 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -11.5) |
| [[Hs 766T (line)]] | wt | 33.1 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.110× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0766× (z -9.3) |
| [[LoVo (line)]] | wt | 67.4 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[LS 180 (line)]] | wt | 34.8 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -11.4) ⚠ cell-cycle shift, explains ~53% of this change |
| [[MIA PaCa-2 (line)]] | alt | 53.0 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.158× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.314× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 30.1 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.215× (z -11.1) ⚠ cell-cycle shift, explains ~37% of this change |
| [[NCI-H23 (line)]] | alt | 40.5 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 40.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.130× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.133× (z -8.5) |
| [[J82 (line)]] | alt | 47.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -10.4) |
| [[RPMI-7951 (line)]] | alt | 38.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.102× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[SW480 (line)]] | alt | 31.4 | 0 | 3 (2 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.151× (z -9.5) |
| [[HCT15 (line)]] | alt | 89.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0896× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[HEC-1-A (line)]] | alt | 38.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[hTERT-HPNE (line)]] | wt | 26.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.129× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[Panc 03.27 (line)]] | alt | 38.3 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.213× (z -9.9) ⚠ toxic |
| [[A-427 (line)]] | wt | 19.5 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.205× (z -10.6) |
| [[C32 (line)]] | wt | 20.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.98× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[CHP-212 (line)]] | wt | 32.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0402× (z -10.7) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HT-29 (line)]] | alt | 16.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.183× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[RKO (line)]] | wt | 46.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0612× (z -19.0) ⚠ cell-cycle shift, explains ~38% of this change |
| [[SW1417 (line)]] | alt | 17.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -9.0) ⚠ cell-cycle shift, explains ~53% of this change |
| [[AN3 CA (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.55 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 87.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 35.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15163), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDRT4]] | +0.92 | +0.91 / +0.92 | both halves | 7e-06 | STRING 737; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[TVP23C]] | +0.82 | +0.78 / +0.83 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[LINC02804]] | +0.66 | +0.41 / +0.63 | both halves | 4e-05 |  |
| [[IL20RB]] | +0.66 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[DHDDS]] | +0.65 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[TMED3]] | +0.64 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[PGM3]] | +0.63 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[KCNQ1OT1]] | +0.63 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[MYDGF]] | +0.63 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[GOSR2]] | +0.61 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[COPE]] | +0.61 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[KDELR2]] | +0.61 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[ARFGAP3]] | +0.60 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[FAM114A1]] | +0.60 | +0.57 / +0.62 | both halves | 9e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THAP12]] | -0.59 | -0.49 / -0.66 | both halves | 1e-05 |  |
| [[SINHCAF]] | -0.59 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[YAP1]] | -0.55 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[ARPIN]] | -0.52 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[MAP3K1]] | -0.50 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[RNF138]] | -0.50 | -0.33 / -0.60 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.613). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.2, -33.8); signed map (-55.8, 16.6). **Vector** length 94.7, 26.3% of its response variance represented; |z| ≥ 3 in 1,215 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Synthesis of substrates in N-glycan biosythesis* (reactome, mean cos +0.51 to 6); *Biosynthesis of the N-glycan precursor (dolichol lipid-linked oligosaccharide, LLO) and transfer to a nascent protein* (reactome, mean cos +0.51 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.7 | +4.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.2 | +1.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | -2.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.4 | +1.8 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +2.2 | +3.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.9 | -0.3 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.8 | +1.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.2 | -12.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.0 | -14.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | -4.1 | -10.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | -4.1 | -15.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | -3.4 | -10.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.2 | -3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.1 | -8.0 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -3.0 | -3.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.0 | -4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | TVP23C-CDRT4 readthrough |
| Locus type | readthrough (other) |
| Location | 17p12 — chr17:15,436,021-15,563,561 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously FAM18B2-CDRT4 |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100533496](https://www.ncbi.nlm.nih.gov/gene/100533496):

> This locus represents naturally occurring readthrough transcription between the neighboring TVP23C (trans-golgi network vesicle protein 23 homolog) and CDRT4 (CMT1A duplicated region transcript 4) genes on chromosome 17. Alternative splicing results in multiple transcript variants, one of which encodes a protein that shares sequence identity with the upstream gene product, but its C-terminus is distinct due to frameshifts relative to the downstream gene. [provided by RefSeq, Apr 2014]

**Accessions** — [HGNC:42961](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:42961) · Entrez [100533496](https://www.ncbi.nlm.nih.gov/gene/100533496) · Ensembl [ENSG00000259024](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000259024)

## Data

Gene col 15163: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15163); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15163, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15163]; `tensor/DDL_lfc|DDL_z.npy` [15163]; `embed/gene_vectors.npy` [15163]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15163 or target_col == 15163). Every well: [[TVP23C-CDRT4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TVP23C-CDRT4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
