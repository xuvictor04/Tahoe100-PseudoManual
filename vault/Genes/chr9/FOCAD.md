---
symbol: "FOCAD"
type: "gene"
col: 12008
ensembl_id: "ENSG00000188352"
name: "focadhesin"
location: "9p21.3"
module: 40
arm: "+"
pooled_cpm: 101.5
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 13
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# FOCAD

*focadhesin* — 9p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.78× (z +12.6, q 6e-34, up in 38 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.485× (z -15.0, q 0e+00, down in 40 of 48 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H23 0.106×, A-427 0.180×, Panc 03.27 0.216×, SNU-1 0.189×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (LS 180 0.0266×, A498 0.268×, HEC-1-A 0.358×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 3 lines (RPMI-7951 0.324×, A549 0.391×, NCI-H1573 0.388×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H2030 0.557×, NCI-H2347 0.625×); [[Radotinib (drug)]] 0.5 µM in 1 line (SW 1271 0.0765×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (HS-578T 0.475×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COG5]] (+0.62, fdr 2e-05), [[EVI5]] (+0.61, fdr 3e-05), [[MRPL52]] (+0.52, fdr 1e-04); moves opposite to [[FOSL2]] (-0.55, fdr 2e-05), [[MLLT6]] (-0.53, fdr 3e-05), [[ZNF776]] (-0.53, fdr 6e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12008.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.78×** | +12.6 | 6e-34 | 38/47 (HOP62, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.65×** | +11.0 | 2e-25 | 38/47 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +9.9 | 9e-21 | 29/48 (A498, SNU-423, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.56×** | +9.7 | 4e-20 | 36/47 (HOP62, SNU-423, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +8.1 | 4e-14 | 27/47 (HOP62, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +7.8 | 4e-13 | 28/47 (SNU-423, A-172, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +6.4 | 1e-08 | 31/47 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.28×** | +5.2 | 2e-05 | 24/49 (RKO, HT-29, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.26×** | +5.0 | 3e-05 | 26/48 (NCI-H2347, RKO, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.21×** | +4.2 | 0.001 | 22/47 (C32, HepG2/C3A, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.44×** | +4.2 | 0.001 | 22/47 (HOP62, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.20× | +4.0 | 0.003 | 18/47 (NCI-H23, C32, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.40×** | +3.9 | 0.005 | 23/48 (HOP62, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.4 | 0.032 | 18/48 (HOP62, SW480, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.11× | +3.3 | 0.041 | 10/47 (SNU-423, HEC-1-A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 13 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12008.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H23 0.106×, A-427 0.180×, Panc 03.27 0.216×, SNU-1 0.189×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (LS 180 0.0266×, A498 0.268×, HEC-1-A 0.358×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 3 lines (RPMI-7951 0.324×, A549 0.391×, NCI-H1573 0.388×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H2030 0.557×, NCI-H2347 0.625×); [[Radotinib (drug)]] 0.5 µM in 1 line (SW 1271 0.0765×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (HS-578T 0.475×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.485×** | -15.0 | 0e+00 | 40/48 (NCI-H23, A-427, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.494×** | -14.3 | 5e-44 | 37/44 (HepG2/C3A, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.555×** | -12.4 | 4e-33 | 35/43 (LS 180, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.678×** | -8.5 | 2e-15 | 31/47 (NCI-H460, SW480, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **0.722×** | -7.1 | 1e-10 | 30/47 (LS 180, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | **0.730×** | -6.9 | 4e-10 | 31/47 (KATO III, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.814×** | -6.4 | 1e-08 | 23/47 (RPMI-7951, A549, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.748×** | -6.1 | 6e-08 | 28/47 (A498, PANC-1, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.750×** | -6.1 | 8e-08 | 26/46 (LoVo, A498, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.774×** | -5.6 | 1e-06 | 27/47 (NCI-H460, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.770×** | -5.5 | 2e-06 | 29/46 (NCI-H2030, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.810×** | -4.6 | 2e-04 | 25/47 (SW480, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.806×** | -4.5 | 4e-04 | 23/47 (A498, A549, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12008. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 103 | 4 | 6 (6 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +10.6) | [[Digitoxin (drug)]] 0.5 µM 0.421× (z -12.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A498 (line)]] | wt | 124 | 2 | 7 (7 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.268× (z -17.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 82.6 | 2 | 6 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +13.3) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.381× (z -11.8) ⚠ cell-cycle shift, explains ~23% of this change |
| [[HOP62 (line)]] | alt | 67.5 | 6 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.88× (z +15.5) | [[Dinaciclib (drug)]] 0.05 µM 0.428× (z -8.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 73.8 | 3 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 3.24× (z +12.4) | [[Digitoxin (drug)]] 5 µM 0.216× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change |
| [[J82 (line)]] | alt | 106 | 3 (1 ⚠) | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.36× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.355× (z -12.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 221 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -13.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.557× (z -9.8) |
| [[A549 (line)]] | wt | 168 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -16.9) ⚠ cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 102 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +9.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.90× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.281× (z -10.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 99.0 | 1 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.05 µM 0.435× (z -10.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 186 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0266× (z -46.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 129 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +15.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +8.8) | — |
| [[RPMI-7951 (line)]] | alt | 204 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.174× (z -20.2) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 41.6 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +13.6) | — |
| [[HEC-1-A (line)]] | alt | 163 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.358× (z -15.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 108 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.338× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.475× (z -9.0) |
| [[SW 900 (line)]] | alt | 147 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.404× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change |
| [[SW48 (line)]] | wt | 181 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -13.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 73.6 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +13.0) | [[Homoharringtonine (drug)]] 5 µM 0.541× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 183 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -10.7) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 59.5 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.00× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.0665× (z -20.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 116 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -14.9) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 74.6 | 0 | 3 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.278× (z -9.7) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.625× (z -9.7) |
| [[SHP-77 (line)]] | alt | 179 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.366× (z -12.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 84.0 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +13.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.485× (z -8.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HT-29 (line)]] | alt | 88.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +9.6) | — |
| [[SK-MEL-2 (line)]] | alt | 68.2 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.90× (z +9.5) | — |
| [[SNU-1 (line)]] | wt | 140 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.189× (z -15.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 84.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -17.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 128 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.422× (z -8.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 53.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +9.2) | — |
| [[Hs 766T (line)]] | wt | 52.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +11.2) | — |
| [[LOX-IMVI (line)]] | wt | 180 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.182× (z -9.9) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 107 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.50× (z +10.2) | — |
| [[NCI-H23 (line)]] | alt | 75.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.106× (z -20.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 97.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.216× (z -16.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 42.4 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.360× (z -11.0) ⚠ cell-cycle shift, explains ~56% of this change |
| [[SW 1271 (line)]] | alt | 68.8 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.0765× (z -9.8) |
| [[AN3 CA (line)]] | alt | 96.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 129 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.10 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 81.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 71.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12008), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COG5]] | +0.62 | +0.46 / +0.62 | both halves | 2e-05 |  |
| [[EVI5]] | +0.61 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[MRPL52]] | +0.52 | +0.49 / +0.36 | both halves | 1e-04 |  |
| [[MPZL1]] | +0.51 | +0.38 / +0.43 | both halves | 7e-05 |  |
| [[SLC37A3]] | +0.51 | +0.32 / +0.53 | both halves | 2e-04 |  |
| [[SDF2L1]] | +0.51 | +0.38 / +0.46 | both halves | 6e-05 |  |
| [[NBAS]] | +0.51 | +0.42 / +0.32 | both halves | 1e-04 |  |
| [[DYM]] | +0.50 | +0.40 / +0.40 | both halves | 5e-05 | same gene group |
| [[IL13RA2]] | +0.50 | +0.41 / +0.38 | both halves | 7e-05 |  |
| [[ERLEC1]] | +0.50 | +0.38 / +0.41 | both halves | 6e-05 |  |
| [[COP1]] | +0.49 | +0.44 / +0.41 | both halves | 4e-05 | same gene group |
| [[GDAP2]] | +0.49 | +0.53 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOSL2]] | -0.55 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[MLLT6]] | -0.53 | -0.48 / -0.46 | both halves | 3e-05 | same gene group |
| [[ZNF776]] | -0.53 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[SKIL]] | -0.52 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[ELF1]] | -0.51 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[MED12]] | -0.51 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[ZNF554]] | -0.49 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[SOCS3]] | -0.49 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[ZC3H12A]] | -0.49 | -0.43 / -0.45 | both halves | 3e-05 | same gene group |
| [[PBX2]] | -0.49 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[HNRNPH2]] | -0.48 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[PNRC2]] | -0.48 | -0.39 / -0.43 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers FOCAD's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.452). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (0.9, -21.6); signed map (-45.8, -4.0). **Vector** length 99.0, 26.4% of its response variance represented; |z| ≥ 3 in 1,183 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | +5.7 | +5.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +7.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +8.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +3.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.4 | +2.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.1 | +2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.0 | +2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.5 | +1.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.9 | -6.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -4.6 | -6.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.9 | -8.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -0.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -2.8 | -5.5 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -2.2 | +0.2 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | -2.1 | -2.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.1 | -1.2 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -2.0 | +1.5 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.9 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | focadhesin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p21.3 — chr9:20,658,309-20,995,955 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20375; previously KIAA1797 |
| Gene groups (HGNC) | Armadillo like helical domain containing; MicroRNA protein coding host genes; Small nucleolar RNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VW36](https://www.uniprot.org/uniprotkb/Q5VW36) (Focadhesin):

> Required for the maintenance of SKIC2 and SKIC3 proteostatic levels in the liver. May be involved in the regulation of RNA degradation by the exosome complex. Potential tumor suppressor in gliomas.

**Summary**, from NCBI Gene [54914](https://www.ncbi.nlm.nih.gov/gene/54914):

> Predicted to be involved in regulation of post-transcriptional gene silencing. Located in cytosol and focal adhesion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23377](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23377) · Entrez [54914](https://www.ncbi.nlm.nih.gov/gene/54914) · UniProt [Q5VW36](https://www.uniprot.org/uniprotkb/Q5VW36) · Ensembl [ENSG00000188352](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188352)

## Data

Gene col 12008: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12008); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12008, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12008]; `tensor/DDL_lfc|DDL_z.npy` [12008]; `embed/gene_vectors.npy` [12008]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12008 or target_col == 12008). Every well: [[FOCAD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FOCAD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
