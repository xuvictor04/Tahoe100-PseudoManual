---
symbol: "TFCP2"
type: "gene"
col: 5709
ensembl_id: "ENSG00000135457"
name: "transcription factor CP2"
location: "12q13.12-q13.13"
module: 156
arm: "+"
pooled_cpm: 112.26
n_lines_expressing: 48
n_dd_up: 2
n_dd_down: 9
n_dd_up_clean: 2
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/156"]
generated_by: "tahoemap"
---

# TFCP2

*transcription factor CP2* — 12q13.12-q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 1.95× (z +9.1, q 7e-17, up in 34 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 3 lines (SW480 3.42×, LoVo 3.12×, COLO 205 4.68×); [[PH-797804 (drug)]] 5 µM in 2 lines (SW480 2.36×, A-427 2.92×); [[Homoharringtonine (drug)]] 5 µM in 1 line (CFPAC-1 2.03×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.437× (z -21.9, q 0e+00, down in 43 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.778× (z -9.3, q 2e-18, down in 33 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 9 lines (LOX-IMVI 0.399×, A549 0.460×, H4 0.403×, SNU-1 0.480×, …); [[Dinaciclib (drug)]] 0.05 µM in 6 lines (NCI-H460 0.145×, SW480 0.271×, KATO III 0.165×, LoVo 0.238×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H1573 0.119×, LoVo 0.215×, A-427 0.230×, NCI-H460 0.242×, …; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 3 lines (A-172 0.420×, HT-29 0.513×, MIA PaCa-2 0.511×); [[Ponatinib (drug)]] 5 µM in 2 lines (C32 0.442×, HepG2/C3A 0.413×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[METTL16]] (+0.66, fdr 7e-06), [[ZNF3]] (+0.65, fdr 7e-06), [[GMEB1]] (+0.65, fdr 8e-06); moves opposite to [[LAMP2]] (-0.54, fdr 4e-05), [[CREG1]] (-0.53, fdr 2e-05), [[CNN3]] (-0.53, fdr 1e-05).
> It is in [[Module 156]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[CSRP2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5709.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 3 lines (SW480 3.42×, LoVo 3.12×, COLO 205 4.68×); [[PH-797804 (drug)]] 5 µM in 2 lines (SW480 2.36×, A-427 2.92×); [[Homoharringtonine (drug)]] 5 µM in 1 line (CFPAC-1 2.03×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.95×** | +9.1 | 7e-17 | 34/47 (SW480, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.62×** | +6.5 | 2e-08 | 25/46 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | 1.16× | +3.7 | 0.046 | 11/46 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.14× | +3.5 | 0.058 | 13/46 (J82, LoVo, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.14× | +3.4 | 0.078 | 9/46 (NCI-H2347, SW1417, …) | inconsistent across doses |  |
| [[Berbamine (dihydrochloride) (drug)]] 0.05 µM |  | 1.13× | +3.0 | 0.23 | 6/46 (hTERT-HPNE, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 15 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5709.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 9 lines (LOX-IMVI 0.399×, A549 0.460×, H4 0.403×, SNU-1 0.480×, …); [[Dinaciclib (drug)]] 0.05 µM in 6 lines (NCI-H460 0.145×, SW480 0.271×, KATO III 0.165×, LoVo 0.238×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H1573 0.119×, LoVo 0.215×, A-427 0.230×, NCI-H460 0.242×, …; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 3 lines (A-172 0.420×, HT-29 0.513×, MIA PaCa-2 0.511×); [[Ponatinib (drug)]] 5 µM in 2 lines (C32 0.442×, HepG2/C3A 0.413×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.437×** | -21.9 | 0e+00 | 43/47 (NCI-H1573, LoVo, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.449×** | -19.6 | 0e+00 | 39/43 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.481×** | -18.6 | 0e+00 | 38/42 (NCI-H23, C32, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.778×** | -9.3 | 2e-18 | 33/47 (LOX-IMVI, A549, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.706×** | -9.2 | 4e-18 | 31/46 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.710×** | -8.7 | 3e-16 | 35/45 (AsPC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.804×** | -5.8 | 6e-07 | 25/46 (NCI-H1573, A-427, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.857× | -5.6 | 1e-06 | 18/46 (COLO 205, LoVo, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.665×** | -5.5 | 2e-06 | 21/36 (SW480, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | 0.836× | -4.7 | 1e-04 | 22/46 (NCI-H460, KATO III, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 0.837× | -4.7 | 1e-04 | 21/46 (A-172, HT-29, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.848× | -4.3 | 7e-04 | 18/46 (NCI-H1573, NCI-H2030, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.850× | -4.3 | 7e-04 | 20/46 (A549, LoVo, …) | two highest doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.771×** | -4.3 | 7e-04 | 21/45 (HepG2/C3A, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | 0.851× | -4.3 | 7e-04 | 18/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 0.911× | -3.4 | 0.020 | 4/47 (SNU-1, PANC-1, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.881× | -3.3 | 0.026 | 15/46 (SW48, PANC-1, …) | inconsistent across doses |  |
| [[Gefitinib (drug)]] 5 µM |  | 0.896× | -2.9 | 0.095 | 9/46 (NCI-H460, hTERT-HPNE, …) | rises with dose |  |
| [[Imiquimod (maleate) (drug)]] 0.05 µM |  | 0.888× | -2.9 | 0.095 | 6/45 (A-427, HCT15, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5709. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 144 | 0 | 10 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.145× (z -28.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.658× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 135 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -16.4) |
| [[PANC-1 (line)]] | alt | 154 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.347× (z -17.3) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 99.4 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -12.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -10.3) |
| [[KATO III (line)]] | alt | 145 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.165× (z -26.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 214 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.119× (z -28.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 171 | 2 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.42× (z +14.0) | [[Dinaciclib (drug)]] 0.05 µM 0.271× (z -26.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 85.8 | 0 | 5 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.308× (z -10.8) ⚠ toxic; cell-cycle shift, explains ~12% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -8.5) |
| [[LoVo (line)]] | wt | 188 | 1 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.12× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -27.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 217 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.216× (z -23.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 149 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -11.3) |
| [[A-427 (line)]] | wt | 184 | 1 | 3 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 2.92× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -23.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 117 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.234× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -14.6) |
| [[SW1417 (line)]] | alt | 132 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -15.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 139 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.321× (z -12.8) ⚠ toxic |
| [[H4 (line)]] | wt | 117 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -12.2) |
| [[J82 (line)]] | alt | 87.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.344× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.549× (z -8.9) |
| [[LS 180 (line)]] | wt | 100 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.336× (z -14.4) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 109 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.435× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 120 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.368× (z -12.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 175 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.380× (z -12.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 86.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -21.4) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.442× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 73.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +10.1) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.425× (z -8.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 132 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.68× (z +10.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.482× (z -9.0) ⚠ toxic |
| [[HT-29 (line)]] | alt | 123 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.304× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.513× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 96.8 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.377× (z -12.0) ⚠ toxic; cell-cycle shift, explains ~12% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.511× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 111 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.443× (z -9.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 107 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.289× (z -14.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 66.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.420× (z -10.3) |
| [[AN3 CA (line)]] | alt | 131 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0844× (z -18.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 77.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.420× (z -8.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 96.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.278× (z -13.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 121 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.376× (z -13.2) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 108 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -9.1) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 144 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.100× (z -13.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 46.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 85.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 98.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.14 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 63.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 82.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 75.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 100 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5709), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL16]] | +0.66 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[ZNF3]] | +0.65 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[GMEB1]] | +0.65 | +0.65 / +0.58 | both halves | 8e-06 |  |
| [[ZC3H18]] | +0.64 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[FAF2]] | +0.63 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[QRICH1]] | +0.63 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[UBE2J2]] | +0.63 | +0.58 / +0.65 | both halves | 8e-06 |  |
| [[GPATCH8]] | +0.63 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[GON4L]] | +0.62 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[FBXO28]] | +0.62 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[RPP14]] | +0.62 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[ALKBH1]] | +0.61 | +0.60 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAMP2]] | -0.54 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[CREG1]] | -0.53 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[CNN3]] | -0.53 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[FAM199X]] | -0.52 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[ACADVL]] | -0.52 | -0.48 / -0.52 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CSRP2]] | C | TFCP2's natural level strengthens CSRP2's drug response | TFCP2's natural level across 40 lines (lineage-adjusted; a glimpse) | r +0.71, reverse -0.42; direction not clear | 0.054 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 156]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.821). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-42.5, 3.6); signed map (-4.8, -16.0). **Vector** length 111, 30.9% of its response variance represented; |z| ≥ 3 in 963 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +8.4 | +9.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +6.1 | +2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.0 | +6.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +2.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.7 | +1.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.6 | +1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +1.6 |
|  | [[Azithromycin (hydrate) (drug)]] 5 µM |  | +2.3 | +0.8 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.6 | -19.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -5.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.2 | -3.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.5 | -18.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.4 | -8.7 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -2.8 | -0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | +0.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.3 | -1.2 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -2.2 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | transcription factor CP2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.12-q13.13 — chr12:51,093,656-51,173,135 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SEF, CP2, LSF, LBP-1C, TFCP2C |
| Gene groups (HGNC) | Transcription factor CP2 family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12800](https://www.uniprot.org/uniprotkb/Q12800) (Alpha-globin transcription factor CP2):

> Binds a variety of cellular and viral promoters including fibrinogen, alpha-globin, SV40 and HIV-1 promoters. Activation of the alpha-globin promoter in erythroid cells is via synergistic interaction with UBP1 (By similarity). Functions as part of the SSP (stage selector protein) complex. Facilitates the interaction of the gamma-globin genes with enhancer elements contained in the locus control region in fetal erythroid cells. Interacts by binding to the stage selector element (SSE) in the …

**Summary**, from NCBI Gene [7024](https://www.ncbi.nlm.nih.gov/gene/7024):

> This gene encodes a transcription factor that binds the alpha-globin promoter and activates transcription of the alpha-globin gene. The encoded protein regulates erythroid gene expression, plays a role in the transcriptional switch of globin gene promoters, and it activates many other cellular and viral gene promoters. The gene product interacts with certain inflammatory response factors, and polymorphisms of this gene may be involved in the pathogenesis of Alzheimer's disease. [provided by …

**Accessions** — [HGNC:11748](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11748) · Entrez [7024](https://www.ncbi.nlm.nih.gov/gene/7024) · UniProt [Q12800](https://www.uniprot.org/uniprotkb/Q12800) · Ensembl [ENSG00000135457](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135457)

## Data

Gene col 5709: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5709); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5709, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5709]; `tensor/DDL_lfc|DDL_z.npy` [5709]; `embed/gene_vectors.npy` [5709]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5709 or target_col == 5709). Every well: [[TFCP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TFCP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
