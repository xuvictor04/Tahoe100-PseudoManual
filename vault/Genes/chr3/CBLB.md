---
symbol: "CBLB"
type: "gene"
col: 3552
ensembl_id: "ENSG00000114423"
name: "Cbl proto-oncogene B"
location: "3q13.11"
module: 40
arm: "+"
pooled_cpm: 373.18
n_lines_expressing: 49
n_dd_up: 0
n_dd_down: 47
n_dd_up_clean: 0
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# CBLB

*Cbl proto-oncogene B* — 3q13.11

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Trametinib (drug)]] 5 µM in 1 line (LOX-IMVI 2.78×; ⚠ cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (C32 2.09×; ⚠ cell-cycle shift, explains ~50% of this change); [[Cobimetinib (drug)]] 5 µM in 1 line (LOX-IMVI 2.23×).
> Pooled over the cell lines (median), lowered significantly by 47 drug-doses (20 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.281× (z -30.2, q 0e+00, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TXNDC11]] (+0.71, fdr 8e-06), [[ELP2]] (+0.68, fdr 7e-06), [[EIF2AK3]] (+0.68, fdr 7e-06); moves opposite to [[MED1]] (-0.64, fdr 2e-05), [[ZNF507]] (-0.61, fdr 1e-05), [[NSD1]] (-0.59, fdr 5e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[GLRX]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3552.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Trametinib (drug)]] 5 µM in 1 line (LOX-IMVI 2.78×; ⚠ cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (C32 2.09×; ⚠ cell-cycle shift, explains ~50% of this change); [[Cobimetinib (drug)]] 5 µM in 1 line (LOX-IMVI 2.23×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Budesonide (drug)]] 5 µM |  | 1.22× | +3.4 | 0.14 | 23/47 (AsPC-1, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Sapanisertib (drug)]] 5 µM |  | 1.46× | +3.4 | 0.14 | 23/48 (BT-474, C32, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~78% of this change | 1.34× | +3.4 | 0.14 | 25/47 (HT-29, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ciclopirox (drug)]] 5 µM |  | 1.14× | +3.1 | 0.24 | 7/47 (CFPAC-1, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 58 in all, 21 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 47 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3552.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.281×** | -30.2 | 0e+00 | 47/47 (NCI-H1792, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.229×** | -24.8 | 0e+00 | 47/48 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.220×** | -24.5 | 0e+00 | 46/47 (NCI-H1573, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.244×** | -22.8 | 0e+00 | 43/43 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.299×** | -20.4 | 0e+00 | 47/47 (HS-578T, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.358×** | -17.3 | 0e+00 | 45/47 (HS-578T, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.368×** | -15.6 | 0e+00 | 39/44 (HS-578T, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.525×** | -15.3 | 0e+00 | 40/48 (NCI-H1792, HS-578T, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.469×** | -12.2 | 1e-32 | 44/46 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.525×** | -10.8 | 1e-25 | 45/47 (A549, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.564×** | -9.6 | 3e-20 | 33/47 (NCI-H1792, SW1417, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.583×** | -9.1 | 6e-18 | 34/47 (KATO III, AsPC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.596×** | -8.7 | 1e-16 | 35/47 (AsPC-1, SW1417, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.699×** | -8.5 | 9e-16 | 38/47 (SNU-1, CFPAC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **0.605×** | -8.4 | 1e-15 | 44/47 (SW 900, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.613×** | -8.2 | 6e-15 | 44/47 (SK-MEL-2, RPMI-7951, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.653×** | -7.2 | 3e-11 | 35/47 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.479×** | -6.5 | 3e-09 | 35/47 (AsPC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.687×** | -6.3 | 8e-09 | 35/47 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.727×** | -5.3 | 2e-06 | 33/47 (A-172, SW480, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.734×** | -5.2 | 4e-06 | 28/48 (A-172, SW480, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.732×** | -5.0 | 1e-05 | 32/47 (NCI-H1792, PANC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.744×** | -4.6 | 8e-05 | 29/46 (HT-29, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.53 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3552. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 3,082 | 0 | 18 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0929× (z -25.0) |
| [[NCI-H2347 (line)]] | alt | 553 | 0 | 18 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -33.2) |
| [[KATO III (line)]] | alt | 351 | 0 | 17 (12 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.136× (z -21.4) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.153× (z -19.3) |
| [[AsPC-1 (line)]] | alt | 584 | 0 | 16 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0881× (z -42.5) |
| [[HS-578T (line)]] | alt | 964 | 0 | 16 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -36.8) |
| [[CFPAC-1 (line)]] | alt | 404 | 0 | 15 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -29.1) |
| [[SW 900 (line)]] | alt | 582 | 0 | 15 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -31.0) |
| [[H4 (line)]] | wt | 395 | 0 | 12 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.274× (z -17.2) |
| [[NCI-H1792 (line)]] | alt | 687 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0728× (z -48.2) |
| [[SW1417 (line)]] | alt | 222 | 0 | 12 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -19.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.426× (z -14.9) |
| [[HT-29 (line)]] | alt | 264 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.215× (z -18.5) |
| [[LOX-IMVI (line)]] | wt | 211 | 2 (1 ⚠) | 9 (3 ⚠) | [[Trametinib (drug)]] 5 µM 2.78× (z +12.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 2.23× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -25.8) |
| [[RKO (line)]] | wt | 819 | 0 | 11 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -15.9) |
| [[SW480 (line)]] | alt | 178 | 0 | 11 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.250× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.294× (z -13.8) |
| [[A549 (line)]] | wt | 355 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0852× (z -39.6) |
| [[LS 180 (line)]] | wt | 481 | 0 | 10 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0980× (z -19.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.133× (z -17.1) |
| [[NCI-H460 (line)]] | wt | 430 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -36.4) |
| [[SNU-423 (line)]] | alt | 399 | 0 | 10 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -20.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.295× (z -18.3) |
| [[NCI-H1573 (line)]] | alt | 299 | 0 | 9 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0749× (z -28.6) |
| [[RPMI-7951 (line)]] | alt | 653 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -27.2) |
| [[A498 (line)]] | wt | 330 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.206× (z -18.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.202× (z -18.0) |
| [[HOP62 (line)]] | alt | 301 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -18.4) |
| [[Hs 766T (line)]] | wt | 192 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -19.7) |
| [[J82 (line)]] | alt | 436 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -19.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.312× (z -17.1) |
| [[Panc 03.27 (line)]] | alt | 248 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.182× (z -20.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.220× (z -17.4) |
| [[PANC-1 (line)]] | alt | 209 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -23.4) |
| [[A-172 (line)]] | wt | 421 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.123× (z -20.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.245× (z -12.9) |
| [[CHP-212 (line)]] | wt | 441 | 0 | 7 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.236× (z -17.8) |
| [[HepG2_C3A (line)]] | wt | 270 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -20.8) |
| [[NCI-H2030 (line)]] | alt | 255 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -25.2) |
| [[NCI-H23 (line)]] | alt | 177 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0661× (z -26.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.238× (z -20.5) |
| [[C32 (line)]] | wt | 781 | 1 (1 ⚠) | 5 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +9.8) ⚠ cell-cycle shift, explains ~50% of this change | [[Dinaciclib (drug)]] 5 µM 0.176× (z -22.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.339× (z -20.2) |
| [[SHP-77 (line)]] | alt | 240 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -16.1) |
| [[SK-MEL-2 (line)]] | alt | 501 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0955× (z -24.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.278× (z -18.6) |
| [[A-427 (line)]] | wt | 180 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.214× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.479× (z -12.1) |
| [[COLO 205 (line)]] | alt | 157 | 0 | 5 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.200× (z -13.8) |
| [[SW48 (line)]] | wt | 170 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -16.9) |
| [[BT-474 (line)]] | alt | 162 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -15.5) |
| [[C-33 A (line)]] | alt | 160 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -13.7) |
| [[HCT15 (line)]] | alt | 224 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.150× (z -13.4) |
| [[HEC-1-A (line)]] | alt | 132 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -15.0) |
| [[SNU-1 (line)]] | wt | 156 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -12.8) |
| [[LoVo (line)]] | wt | 137 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.164× (z -16.7) |
| [[SW 1088 (line)]] | alt | 477 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -12.4) |
| [[AN3 CA (line)]] | alt | 224 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0564× (z -20.2) |
| [[MIA PaCa-2 (line)]] | alt | 53.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 731 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 552 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 167 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3552), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNDC11]] | +0.71 | +0.77 / +0.58 | both halves | 8e-06 |  |
| [[ELP2]] | +0.68 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[EIF2AK3]] | +0.68 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[YIPF2]] | +0.66 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[HEATR5B]] | +0.66 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[GMCL1]] | +0.65 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[REPS2]] | +0.65 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[SEC23A]] | +0.64 | +0.75 / +0.51 | both halves | 1e-05 |  |
| [[SRP54]] | +0.64 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[COG6]] | +0.64 | +0.72 / +0.52 | both halves | 1e-05 |  |
| [[WIPI1]] | +0.64 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[MAX]] | +0.63 | +0.63 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED1]] | -0.64 | -0.74 / -0.48 | both halves | 2e-05 |  |
| [[ZNF507]] | -0.61 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[NSD1]] | -0.59 | -0.61 / -0.40 | both halves | 5e-05 |  |
| [[ZNF629]] | -0.58 | -0.66 / -0.42 | both halves | 4e-05 |  |
| [[UTP20]] | -0.58 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[CSTF2T]] | -0.58 | -0.61 / -0.57 | both halves | 1e-05 |  |
| [[ANAPC7]] | -0.58 | -0.63 / -0.50 | both halves | 1e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[ZNF702P]] | -0.58 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[ZNF462]] | -0.58 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[DDX20]] | -0.57 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[ZC3H4]] | -0.57 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[ZNF518B]] | -0.57 | -0.63 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GLRX]] | B | GLRX activity raises CBLB's level | lines that do not express GLRX (10) vs lines expressing it (40) | 2.59× lower at baseline in the lines without GLRX | 0.007 | ⚠ within organs, on part of the lines; also absent: DUSP10, FES, DGKG; maybe low, not absent |
| [[ME3]] | B | ME3 activity raises CBLB's level | lines that do not express ME3 (13) vs lines expressing it (37) | 1.48× lower at baseline in the lines without ME3 | 0.052 | ⚠ within organs, on part of the lines; also absent: PLAAT3 |
| [[TOP2A]] | B | TOP2A activity raises CBLB's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 9.5% of all compounds | 0.095 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RPS6KA2]] | B | RPS6KA2 activity raises CBLB's level | lines that do not express RPS6KA2 (6) vs lines expressing it (44) | 1.33× lower at baseline in the lines without RPS6KA2 | 0.099 | ⚠ within organs, on part of the lines; also absent: RAB20, FAM102A, LINC02100 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.716). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (8.3, -33.5); signed map (-42.2, 11.7). **Vector** length 125, 49.0% of its response variance represented; |z| ≥ 3 in 2,109 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +7.3 | -4.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | +6.7 | -6.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | +6.0 | -7.1 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +5.2 | +2.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.4 | -1.0 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +4.2 | +1.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +3.8 | +1.5 |
|  | [[Terfenadine (drug)]] 5 µM |  | +3.5 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +0.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -8.2 | -17.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.9 | -10.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.5 | -24.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.6 | -4.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.5 | -9.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.0 | -6.5 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -3.9 | -3.5 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -3.8 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | Cbl proto-oncogene B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.11 — chr3:105,655,461-105,869,552 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RNF56, Cbl-b |
| Gene groups (HGNC) | Ring finger proteins; Cbl proto-oncogene family |
| Hallmark sets | COMPLEMENT |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13191](https://www.uniprot.org/uniprotkb/Q13191) (E3 ubiquitin-protein ligase CBL-B):

> E3 ubiquitin-protein ligase which accepts ubiquitin from specific E2 ubiquitin-conjugating enzymes, and transfers it to substrates, generally promoting their degradation by the proteasome. Negatively regulates TCR (T-cell receptor), BCR (B-cell receptor) and FCER1 (high affinity immunoglobulin epsilon receptor) signal transduction pathways. In naive T-cells, inhibits VAV1 activation upon TCR engagement and imposes a requirement for CD28 costimulation for proliferation and IL-2 production (By …

**Summary**, from NCBI Gene [868](https://www.ncbi.nlm.nih.gov/gene/868):

> This gene encodes an E3 ubiquitin-protein ligase which promotes proteosome-mediated protein degradation by transferring ubiquitin from an E2 ubiquitin-conjugating enzyme to a substrate. The encoded protein is involved in the regulation of immune response by limiting T-cell receptor, B-cell receptor, and high affinity immunoglobulin epsilon receptor activation. Studies in mouse suggest that this gene is involved in antifungal host defense and that its inhibition leads to increased fungal …

**Accessions** — [HGNC:1542](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1542) · Entrez [868](https://www.ncbi.nlm.nih.gov/gene/868) · UniProt [Q13191](https://www.uniprot.org/uniprotkb/Q13191) · Ensembl [ENSG00000114423](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114423)

## Data

Gene col 3552: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3552); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3552, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3552]; `tensor/DDL_lfc|DDL_z.npy` [3552]; `embed/gene_vectors.npy` [3552]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3552 or target_col == 3552). Every well: [[CBLB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CBLB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
