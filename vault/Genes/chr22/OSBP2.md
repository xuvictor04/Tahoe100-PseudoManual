---
symbol: "OSBP2"
type: "gene"
col: 11577
ensembl_id: "ENSG00000184792"
name: "oxysterol binding protein 2"
location: "22q12.2"
module: 160
arm: "+"
pooled_cpm: 53.18
n_lines_expressing: 48
n_dd_up: 13
n_dd_down: 12
n_dd_up_clean: 10
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/160"]
generated_by: "tahoemap"
---

# OSBP2

*oxysterol binding protein 2* — 22q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.65× (z +15.0, q 0e+00, up in 33 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.576× (z -11.6, q 3e-28, down in 28 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 0.702× (z -7.1, q 1e-10, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OLFM2]] (+0.66, fdr 7e-06), [[ZBTB46]] (+0.61, fdr 7e-06), [[RPLP0P2]] (+0.60, fdr 1e-05); moves opposite to [[WBP11]] (-0.58, fdr 1e-05), [[NUDT21]] (-0.55, fdr 1e-05), [[CTDSPL2]] (-0.52, fdr 1e-05).
> It sits in the **+** arm of [[Module 160]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[DOCK3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11577.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.65×** | +15.0 | 0e+00 | 33/46 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +7.9 | 9e-13 | 27/46 (A498, hTERT-HPNE, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +7.0 | 7e-10 | 25/46 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +6.7 | 2e-09 | 25/46 (SW480, Hs 766T, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.30×** | +5.6 | 2e-06 | 23/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.27×** | +5.1 | 3e-05 | 20/46 (SHP-77, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.26×** | +4.9 | 6e-05 | 19/45 (H4, NCI-H460, …) | two highest doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM |  | **1.24×** | +4.4 | 7e-04 | 24/46 (PANC-1, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.21×** | +4.0 | 0.003 | 20/46 (SW480, Hs 766T, …) | inconsistent across doses |  |
| [[ULK-101 (drug)]] 0.05 µM |  | **1.22×** | +3.9 | 0.005 | 15/47 (MIA PaCa-2, NCI-H1573, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.21×** | +3.8 | 0.006 | 18/45 (NCI-H460, H4, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.18× | +3.6 | 0.015 | 18/46 (COLO 205, SHP-77, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.18× | +3.5 | 0.020 | 14/46 (A498, LS 180, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.12× | +3.4 | 0.029 | 7/46 (NCI-H2030, SHP-77, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.3 | 0.038 | 17/46 (A498, RPMI-7951, …) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.33×** | +3.1 | 0.065 | 11/46 (SW480, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 10 with an alert ⚠; shown: the 15 strongest. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11577.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.576×** | -11.6 | 3e-28 | 28/46 (AsPC-1, SNU-1, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **0.670×** | -8.4 | 1e-14 | 33/45 (NCI-H661, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.677×** | -7.9 | 7e-13 | 24/44 (NCI-H2030, HS-578T, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.672×** | -7.7 | 2e-12 | 28/42 (C-33 A, A-427, …) | all doses, flat | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.702×** | -7.1 | 1e-10 | 24/48 (RPMI-7951, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.547×** | -6.6 | 3e-09 | 26/47 (LoVo, LS 180, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **0.747×** | -5.9 | 4e-07 | 23/45 (LoVo, SNU-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.820×** | -5.8 | 4e-07 | 24/46 (AsPC-1, NCI-H2030, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.761×** | -5.5 | 3e-06 | 19/46 (MIA PaCa-2, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.634×** | -5.0 | 3e-05 | 20/45 (SHP-77, HS-578T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.684×** | -4.2 | 0.002 | 19/46 (SNU-1, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.880× | -3.8 | 0.008 | 13/46 (LoVo, AsPC-1, …) | top dose only |  |
| [[Budesonide (drug)]] 0.05 µM |  | 0.843× | -3.6 | 0.016 | 14/46 (NCI-H1573, HS-578T, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.954× | -3.4 | 0.026 | 4/47 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.734×** | -3.4 | 0.027 | 10/32 (SK-MEL-2, HOP62, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11577. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 292 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -21.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SW480 (line)]] | alt | 63.0 | 3 | 2 (2 ⚠) | [[PF-06260933 (drug)]] 5 µM 3.33× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.382× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[LoVo (line)]] | wt | 116 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.198× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 58.1 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.228× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Betamethasone dipropionate (drug)]] 0.5 µM 0.417× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 95.7 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -16.6) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -12.0) |
| [[A-172 (line)]] | wt | 29.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.79× (z +21.1) | — |
| [[A-427 (line)]] | wt | 43.6 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.216× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[MIA PaCa-2 (line)]] | alt | 41.3 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.221× (z -13.0) |
| [[RKO (line)]] | wt | 112 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -11.8) |
| [[SHP-77 (line)]] | alt | 64.5 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.150× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change |
| [[SW48 (line)]] | wt | 130 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0860× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -8.9) |
| [[A498 (line)]] | wt | 19.2 | 2 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.17× (z +10.7) | — |
| [[COLO 205 (line)]] | alt | 18.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.15× (z +12.9) | — |
| [[H4 (line)]] | wt | 20.6 | 2 (1 ⚠) | 0 | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 9.84× (z +9.8) | — |
| [[HEC-1-A (line)]] | alt | 42.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.54× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -10.1) |
| [[J82 (line)]] | alt | 38.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +9.8) | — |
| [[NCI-H460 (line)]] | wt | 45.1 | 2 (1 ⚠) | 0 | [[Pitavastatin (Calcium) (drug)]] 5 µM 3.43× (z +11.1) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.50× (z +8.6) | — |
| [[PANC-1 (line)]] | alt | 24.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +14.7) | — |
| [[SK-MEL-2 (line)]] | alt | 34.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +13.9) | — |
| [[A549 (line)]] | wt | 44.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +9.1) | — |
| [[AN3 CA (line)]] | alt | 129 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.250× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change |
| [[C-33 A (line)]] | alt | 73.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.115× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[C32 (line)]] | wt | 18.0 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0909× (z -11.0) |
| [[HCT15 (line)]] | alt | 71.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HT-29 (line)]] | alt | 39.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.387× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[hTERT-HPNE (line)]] | wt | 55.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.172× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[KATO III (line)]] | alt | 24.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -10.1) |
| [[NCI-H23 (line)]] | alt | 39.6 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -9.8) |
| [[NCI-H2347 (line)]] | alt | 17.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +13.3) | — |
| [[NCI-H661 (line)]] | alt | 44.8 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.05 µM 0.0597× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 48.6 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.178× (z -11.8) |
| [[SNU-1 (line)]] | wt | 72.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.122× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SNU-423 (line)]] | alt | 20.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.67× (z +16.8) | — |
| [[SW 1271 (line)]] | alt | 64.8 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.05 µM 0.0909× (z -8.9) |
| [[SW1417 (line)]] | alt | 138 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -10.5) ⚠ cell-cycle shift, explains ~10% of this change |
| [[BT-474 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.00 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 84.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 89.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.24 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 47.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 91.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11577), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OLFM2]] | +0.66 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[ZBTB46]] | +0.61 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[RPLP0P2]] | +0.60 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[ATP9B]] | +0.59 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[TMC7]] | +0.59 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[TNFRSF12A]] | +0.58 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[CFAP46]] | +0.57 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[CLCF1]] | +0.57 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[ARHGEF4]] | +0.57 | +0.53 / +0.61 | both halves | 1e-05 | same gene group |
| [[ZNF83]] | +0.57 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[IL1R2]] | +0.56 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[GPR153]] | +0.56 | +0.53 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WBP11]] | -0.58 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[NUDT21]] | -0.55 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[CTDSPL2]] | -0.52 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[IARS2]] | -0.51 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[WHAMMP1]] | -0.51 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[MTRR]] | -0.51 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[CEP43]] | -0.50 | -0.40 / -0.55 | both halves | 4e-05 |  |
| [[COPS7B]] | -0.49 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[DDOST]] | -0.49 | -0.56 / -0.38 | both halves | 7e-05 |  |
| [[COPS4]] | -0.49 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[CIAO2A]] | -0.48 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[KCTD3]] | -0.48 | -0.49 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DOCK3]] | B | DOCK3 activity raises OSBP2's level | lines that do not express DOCK3 (22) vs lines expressing it (28) | 1.49× lower at baseline in the lines without DOCK3 | 0.055 | ⚠ within organs, on part of the lines; also absent: RBM20, LHX2, ADCY1 |
| [[CLSTN2]] | B | CLSTN2 activity raises OSBP2's level | lines that do not express CLSTN2 (30) vs lines expressing it (20) | 1.21× lower at baseline in the lines without CLSTN2 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TENM2, CCDC144NL-AS1, ENSG00000264660 |
| [[GNG4]] | B | GNG4 activity raises OSBP2's level | lines that do not express GNG4 (20) vs lines expressing it (30) | 1.40× lower at baseline in the lines without GNG4 | 0.072 | ⚠ within organs, on part of the lines; also absent: OLFM1, JPH3, LRRC4B |
| [[TOP2A]] | B | TOP2A activity raises OSBP2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[NKAIN1]] | C | NKAIN1 activity raises OSBP2's level | lines that do not express NKAIN1 (4) vs lines expressing it (46) | 1.48× lower at baseline in the lines without NKAIN1 | 0.086 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; co-occurs with CTNNB1; also absent: TPST1, CPLANE1, SOAT1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 160]]; 27 genes; this gene is in the **+** arm (projection on the module's main direction 0.466). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (20.9, 10.6); signed map (0.5, 34.3). **Vector** length 107, 25.8% of its response variance represented; |z| ≥ 3 in 1,221 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.6 | +15.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.5 | +6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.8 | +7.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.2 | +4.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.7 | +5.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.2 | +4.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.1 | +2.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | +3.0 | +3.4 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.6 | -6.6 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -4.3 | -5.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.1 | -4.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.0 | -7.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.6 | -5.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.5 | -1.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.5 | -3.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.4 | -2.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | oxysterol binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.2 — chr22:30,693,782-30,907,824 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1664, ORP-4, ORP4; previously OSBPL1 |
| Gene groups (HGNC) | Oxysterol binding proteins; Pleckstrin homology domain containing; MicroRNA protein coding host genes |
| Hallmark sets | HEME_METABOLISM |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969R2](https://www.uniprot.org/uniprotkb/Q969R2) (Oxysterol-binding protein 2):

> Mediates the bidirectional lipid exchange between intracellular compartments and the plasma membrane, delivering cholesterol to the plasma membrane while transferring PI(4,5)P(2) to internal organelles, thereby modulating membrane lipid composition and associated signaling pathways. Binds 7-ketocholesterol. Acts during spermatid development where its function is required prior to the removal of cytoplasm from the sperm head (By similarity).

**Summary**, from NCBI Gene [23762](https://www.ncbi.nlm.nih.gov/gene/23762):

> The protein encoded by this gene contains a pleckstrin homology (PH) domain and an oxysterol-binding region. It binds oxysterols such as 7-ketocholesterol and may inhibit their cytotoxicity. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Sep 2013]

**Accessions** — [HGNC:8504](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8504) · Entrez [23762](https://www.ncbi.nlm.nih.gov/gene/23762) · UniProt [Q969R2](https://www.uniprot.org/uniprotkb/Q969R2) · Ensembl [ENSG00000184792](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184792)

## Data

Gene col 11577: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11577); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11577, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11577]; `tensor/DDL_lfc|DDL_z.npy` [11577]; `embed/gene_vectors.npy` [11577]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11577 or target_col == 11577). Every well: [[OSBP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OSBP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
