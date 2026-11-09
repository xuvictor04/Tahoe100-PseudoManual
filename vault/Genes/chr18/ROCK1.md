---
symbol: "ROCK1"
type: "gene"
col: 873
ensembl_id: "ENSG00000067900"
name: "Rho associated coiled-coil containing protein kinase 1"
location: "18q11.1"
module: 12
arm: "+"
pooled_cpm: 260.81
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 8
n_dd_up_clean: 1
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# ROCK1

*Rho associated coiled-coil containing protein kinase 1* — 18q11.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.36× (z +9.2, q 2e-17, up in 37 of 47 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 1.46× (z +5.9, q 4e-07, up in 30 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 5 lines (LS 180 2.61×, PANC-1 1.91×, AsPC-1 1.74×, SW1417 1.81×, …; ⚠ cell-cycle shift, explains ~25% of this change); [[TAK-901 (drug)]] 5 µM in 4 lines (SW480 2.71×, MIA PaCa-2 2.95×, SW48 3.37×, C32 2.83×); [[Niclosamide (olamine) (drug)]] 5 µM in 3 lines (LoVo 1.91×, LS 180 1.84×, C-33 A 1.87×; ⚠ toxic); [[PH-797804 (drug)]] 5 µM in 1 line (C32 4.04×); [[Ponatinib (drug)]] 5 µM in 1 line (C32 2.04×).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.656× (z -17.8, q 0e+00, down in 43 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 15 lines (A549 0.417×, HCT15 0.479×, LOX-IMVI 0.540×, A-172 0.558×, …); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.353×, NCI-H1573 0.461×; ⚠ toxic; cell-cycle shift, explains ~26% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (AsPC-1 0.474×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TPR]] (+0.59, fdr 3e-05), [[PPP1R12A]] (+0.58, fdr 1e-05), [[SEPTIN7]] (+0.58, fdr 1e-05); moves opposite to [[SPATA2]] (-0.54, fdr 4e-05), [[ZNF587]] (-0.45, fdr 1e-04), [[CYP27B1]] (-0.44, fdr 1e-04).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 873.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 5 lines (LS 180 2.61×, PANC-1 1.91×, AsPC-1 1.74×, SW1417 1.81×, …; ⚠ cell-cycle shift, explains ~25% of this change); [[TAK-901 (drug)]] 5 µM in 4 lines (SW480 2.71×, MIA PaCa-2 2.95×, SW48 3.37×, C32 2.83×); [[Niclosamide (olamine) (drug)]] 5 µM in 3 lines (LoVo 1.91×, LS 180 1.84×, C-33 A 1.87×; ⚠ toxic); [[PH-797804 (drug)]] 5 µM in 1 line (C32 4.04×); [[Ponatinib (drug)]] 5 µM in 1 line (C32 2.04×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.36×** | +9.2 | 2e-17 | 37/47 (LS 180, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +8.3 | 3e-14 | 36/46 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.23×** | +6.2 | 1e-07 | 27/47 (LS 180, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.46×** | +5.9 | 4e-07 | 30/48 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.20×** | +5.5 | 5e-06 | 23/47 (LS 180, BT-474, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.17× | +4.7 | 2e-04 | 18/47 (NCI-H1792, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.17× | +4.6 | 3e-04 | 21/47 (LS 180, H4, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.10× | +4.0 | 0.004 | 3/48 (RKO, CHP-212, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.14× | +3.7 | 0.012 | 15/47 (HEC-1-A, SW480, …) | inconsistent across doses | composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.12× | +3.5 | 0.027 | 5/47 (HEC-1-A, CFPAC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.13× | +3.4 | 0.037 | 11/46 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 873.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 15 lines (A549 0.417×, HCT15 0.479×, LOX-IMVI 0.540×, A-172 0.558×, …); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.353×, NCI-H1573 0.461×; ⚠ toxic; cell-cycle shift, explains ~26% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (AsPC-1 0.474×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.656×** | -17.8 | 0e+00 | 43/48 (A549, HCT15, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.705×** | -10.0 | 3e-21 | 41/46 (RKO, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.730×** | -9.4 | 1e-18 | 39/47 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.772×** | -7.7 | 2e-12 | 29/47 (NCI-H1573, BT-474, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.767×** | -6.8 | 1e-09 | 38/47 (NCI-H2347, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.798×** | -6.7 | 2e-09 | 27/47 (BT-474, A549, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.822×** | -5.8 | 4e-07 | 25/47 (HOP62, AsPC-1, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.829×** | -5.4 | 5e-06 | 25/47 (A-172, HS-578T, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.841× | -5.0 | 4e-05 | 22/49 (NCI-H2347, LOX-IMVI, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.920× | -3.5 | 0.029 | 2/47 (A-172, AN3 CA) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~4% of this change | 0.894× | -3.3 | 0.042 | 11/47 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.924× | -3.3 | 0.042 | 6/47 (LOX-IMVI, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 873. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 385 | 2 (2 ⚠) | 5 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.74× (z +11.9) ⚠ cell-cycle shift, explains ~25% of this change | [[Dinaciclib (drug)]] 5 µM 0.474× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.607× (z -15.2) |
| [[NCI-H1573 (line)]] | alt | 358 | 0 | 7 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.461× (z -14.3) ⚠ toxic; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.619× (z -13.0) |
| [[SNU-1 (line)]] | wt | 498 | 2 (1 ⚠) | 4 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.58× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.520× (z -14.1) |
| [[Panc 03.27 (line)]] | alt | 340 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.579× (z -16.1) |
| [[SW480 (line)]] | alt | 275 | 2 (1 ⚠) | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 2.71× (z +10.0) | [[Panobinostat (drug)]] 5 µM 0.595× (z -10.0) ⚠ cell-cycle shift, explains ~21% of this change |
| [[A549 (line)]] | wt | 219 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -23.6) |
| [[BT-474 (line)]] | alt | 271 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.530× (z -10.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.665× (z -10.0) |
| [[HOP62 (line)]] | alt | 244 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.601× (z -14.9) |
| [[LOX-IMVI (line)]] | wt | 368 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -17.3) |
| [[LS 180 (line)]] | wt | 214 | 3 (3 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +16.2) ⚠ cell-cycle shift, explains ~25% of this change | [[Dinaciclib (drug)]] 5 µM 0.580× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 307 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.659× (z -13.4) |
| [[C32 (line)]] | wt | 228 | 3 | 0 | [[PH-797804 (drug)]] 5 µM 4.04× (z +11.8) | — |
| [[HEC-1-A (line)]] | alt | 282 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.50× (z +12.5) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.632× (z -13.9) |
| [[SW48 (line)]] | wt | 321 | 2 | 1 | [[TAK-901 (drug)]] 5 µM 3.37× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.555× (z -11.8) |
| [[A-172 (line)]] | wt | 314 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -16.3) |
| [[CFPAC-1 (line)]] | alt | 224 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.563× (z -15.2) |
| [[CHP-212 (line)]] | wt | 225 | 0 | 2 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.172× (z -10.7) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -8.5) |
| [[HCT15 (line)]] | alt | 408 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -17.3) |
| [[HepG2_C3A (line)]] | wt | 240 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.584× (z -11.7) |
| [[J82 (line)]] | alt | 212 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.623× (z -11.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.665× (z -10.1) |
| [[LoVo (line)]] | wt | 215 | 2 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 1.91× (z +11.1) ⚠ toxic | — |
| [[NCI-H1792 (line)]] | alt | 407 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.573× (z -14.9) |
| [[PANC-1 (line)]] | alt | 234 | 1 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.91× (z +12.9) ⚠ cell-cycle shift, explains ~25% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.622× (z -13.2) |
| [[A-427 (line)]] | wt | 448 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.639× (z -8.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[C-33 A (line)]] | alt | 359 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 1.87× (z +9.8) ⚠ toxic | — |
| [[Hs 766T (line)]] | wt | 215 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 1.70× (z +8.8) ⚠ toxic | — |
| [[HS-578T (line)]] | alt | 286 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.588× (z -12.9) |
| [[hTERT-HPNE (line)]] | wt | 236 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.571× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[MIA PaCa-2 (line)]] | alt | 323 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 2.95× (z +9.7) | — |
| [[NCI-H2030 (line)]] | alt | 243 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.622× (z -13.7) |
| [[RKO (line)]] | wt | 350 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.353× (z -14.4) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[SHP-77 (line)]] | alt | 274 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.606× (z -8.9) ⚠ cell-cycle shift, explains ~21% of this change |
| [[SK-MEL-2 (line)]] | alt | 224 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.583× (z -12.2) |
| [[SNU-423 (line)]] | alt | 168 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.644× (z -9.7) |
| [[SW1417 (line)]] | alt | 292 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.81× (z +11.7) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[A498 (line)]] | wt | 152 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 285 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 256 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 20.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 225 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 293 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 183 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 270 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 338 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 238 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 245 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 209 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 194 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 873), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPR]] | +0.59 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[PPP1R12A]] | +0.58 | +0.51 / +0.66 | both halves | 1e-05 | pathway: RHO GTPase Effectors; STRING 996 |
| [[SEPTIN7]] | +0.58 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[NIPBL]] | +0.57 | +0.50 / +0.66 | both halves | 1e-05 | STRING 637 |
| [[MIER1]] | +0.56 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[SMC3]] | +0.56 | +0.38 / +0.55 | both halves | 7e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[NCOR1]] | +0.55 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[TAOK3]] | +0.54 | +0.51 / +0.35 | both halves | 1e-04 |  |
| [[PRRC2C]] | +0.54 | +0.40 / +0.63 | both halves | 5e-05 |  |
| [[KTN1]] | +0.53 | +0.34 / +0.57 | both halves | 1e-04 | pathway: RHO GTPase Effectors |
| [[SSB]] | +0.53 | +0.26 / +0.49 | both halves | 3e-04 |  |
| [[ZC3H15]] | +0.53 | +0.43 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPATA2]] | -0.54 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[ZNF587]] | -0.45 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[CYP27B1]] | -0.44 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[MAN2C1]] | -0.43 | -0.30 / -0.36 | both halves | 2e-04 |  |
| [[SMG1P6]] | -0.42 | -0.27 / -0.35 | both halves | 3e-04 |  |
| [[MTX1]] | -0.41 | -0.48 / -0.18 | ⚠ not reproduced | 9e-04 |  |
| [[TRNT1]] | -0.41 | -0.33 / -0.34 | both halves | 1e-04 |  |
| [[ACAD9]] | -0.41 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[RBM4]] | -0.41 | -0.41 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises ROCK1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.331). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (1.6, -56.7); signed map (5.3, -13.7). **Vector** length 109, 33.3% of its response variance represented; |z| ≥ 3 in 991 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.2 | +1.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.4 | +1.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.4 | +8.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | -0.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.1 | +1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +4.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.8 | +3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | -1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | -3.3 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | -7.0 | -10.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -4.3 | -6.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.8 | +1.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.7 | -1.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -3.3 | -6.7 |
|  | [[Clonidine (hydrochloride) (drug)]] 5 µM |  | -2.5 | -2.1 |
|  | [[Folic acid (drug)]] 5 µM |  | -2.5 | -2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -3.5 |
|  | [[Balsalazide (sodium hydrate) (drug)]] 5 µM |  | -2.3 | -2.3 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -2.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | Rho associated coiled-coil containing protein kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q11.1 — chr18:20,944,612-21,111,813 (-) |
| Ensembl biotype | protein_coding |
| Also known as | p160ROCK |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Rho associated coiled-coil containing protein kinase family |
| Hallmark sets | APOPTOSIS, MITOTIC_SPINDLE |
| Reactome | 35 pathways, smallest: RHO GTPases Activate ROCKs; Sema4D induced cell migration and growth-cone collapse; RHOBTB1 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13464](https://www.uniprot.org/uniprotkb/Q13464) (Rho-associated protein kinase 1):

> Protein kinase which is a key regulator of the actin cytoskeleton and cell polarity. Involved in regulation of smooth muscle contraction, actin cytoskeleton organization, stress fiber and focal adhesion formation, neurite retraction, cell adhesion and motility via phosphorylation of DAPK3, GFAP, LIMK1, LIMK2, MYL9/MLC2, TPPP, PFN1 and PPP1R12A. Phosphorylates FHOD1 and acts synergistically with it to promote SRC-dependent non-apoptotic plasma membrane blebbing. Phosphorylates JIP3 and regulates …

**Summary**, from NCBI Gene [6093](https://www.ncbi.nlm.nih.gov/gene/6093):

> This gene encodes a protein serine/threonine kinase that is activated when bound to the GTP-bound form of Rho. The small GTPase Rho regulates formation of focal adhesions and stress fibers of fibroblasts, as well as adhesion and aggregation of platelets and lymphocytes by shuttling between the inactive GDP-bound form and the active GTP-bound form. Rho is also essential in cytokinesis and plays a role in transcriptional activation by serum response factor. This protein, a downstream effector of …

**Accessions** — [HGNC:10251](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10251) · Entrez [6093](https://www.ncbi.nlm.nih.gov/gene/6093) · UniProt [Q13464](https://www.uniprot.org/uniprotkb/Q13464) · Ensembl [ENSG00000067900](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000067900)

## Data

Gene col 873: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 873); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 873, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 873]; `tensor/DDL_lfc|DDL_z.npy` [873]; `embed/gene_vectors.npy` [873]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 873 or target_col == 873). Every well: [[ROCK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ROCK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
