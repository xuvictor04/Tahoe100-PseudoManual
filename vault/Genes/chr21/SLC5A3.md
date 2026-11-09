---
symbol: "SLC5A3"
type: "gene"
col: 12664
ensembl_id: "ENSG00000198743"
name: "solute carrier family 5 member 3"
location: "21q22.11"
module: 1
arm: "-"
pooled_cpm: 221.09
n_lines_expressing: 48
n_dd_up: 15
n_dd_down: 32
n_dd_up_clean: 12
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# SLC5A3

*solute carrier family 5 member 3* — 21q22.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 1.94× (z +9.2, q 3e-17, up in 34 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (11 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.296× (z -9.1, q 4e-17, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPS6]] (+0.90, fdr 7e-06, ⚠ same locus), [[LINC00310]] (+0.74, fdr 7e-06), [[NPTX1]] (+0.56, fdr 1e-05), [[SERINC5]] (+0.53, fdr 3e-05); moves opposite to [[ARMC8]] (-0.62, fdr 7e-06), [[RIOK1]] (-0.54, fdr 2e-05), [[MAOA]] (-0.54, fdr 1e-05).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MT1M]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12664.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.94×** | +9.2 | 3e-17 | 34/46 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +8.5 | 4e-15 | 30/47 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.45×** | +7.6 | 5e-12 | 39/46 (A498, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +7.4 | 2e-11 | 31/48 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.66×** | +7.3 | 3e-11 | 29/46 (BT-474, A-427, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.44×** | +5.3 | 1e-05 | 32/46 (BT-474, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.33×** | +4.1 | 0.003 | 29/45 (NCI-H460, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.30×** | +3.8 | 0.010 | 28/47 (LS 180, SW1417, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.30×** | +3.7 | 0.012 | 23/46 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.29×** | +3.6 | 0.016 | 29/46 (A-172, hTERT-HPNE, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.27×** | +3.5 | 0.023 | 24/46 (A498, LS 180, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +3.5 | 0.023 | 26/46 (LOX-IMVI, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.58×** | +3.5 | 0.023 | 23/46 (LS 180, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Infigratinib (drug)]] 5 µM |  | **1.54×** | +3.3 | 0.045 | 19/46 (BT-474, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Roxadustat (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.076 | 19/46 (PANC-1, COLO 205, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12664.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.296×** | -9.1 | 4e-17 | 47/47 (NCI-H1792, CFPAC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **0.635×** | -6.5 | 2e-08 | 28/47 (C32, HOP62, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.649×** | -6.2 | 1e-07 | 37/46 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.649×** | -6.0 | 3e-07 | 33/46 (CFPAC-1, AsPC-1, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.663×** | -5.9 | 4e-07 | 28/46 (C32, CFPAC-1, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.655×** | -5.8 | 5e-07 | 26/43 (C32, A-172, …) | all doses, flat | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.496×** | -5.3 | 1e-05 | 34/46 (SNU-1, C32, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.677×** | -5.2 | 2e-05 | 27/44 (C32, HS-578T, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.711×** | -4.9 | 6e-05 | 27/46 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.711×** | -4.9 | 6e-05 | 27/46 (C32, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.727×** | -4.6 | 2e-04 | 28/46 (NCI-H1792, HS-578T, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.734×** | -4.4 | 5e-04 | 26/46 (HOP62, HS-578T, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.743×** | -4.3 | 9e-04 | 23/46 (A498, NCI-H1792, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **0.746×** | -4.2 | 0.001 | 26/46 (A498, HS-578T, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.739×** | -4.2 | 0.001 | 24/47 (HOP62, HS-578T, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.819×** | -4.1 | 0.002 | 26/46 (NCI-H1792, SW480, …) | rises with dose | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.778×** | -3.6 | 0.009 | 24/46 (HS-578T, NCI-H1792, …) | all doses, flat |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.679×** | -3.6 | 0.011 | 26/46 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.783×** | -3.5 | 0.012 | 22/46 (A498, NCI-H1573, …) | top dose only |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | **0.786×** | -3.4 | 0.015 | 22/46 (A498, HS-578T, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.845× | -3.4 | 0.016 | 21/46 (HS-578T, A498, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12664. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 431 | 0 | 25 (9 ⚠) | — | [[Clobetasol propionate (drug)]] 0.5 µM 0.220× (z -12.7) |
| [[NCI-H1792 (line)]] | alt | 427 | 0 | 24 (8 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0612× (z -13.7) |
| [[NCI-H2347 (line)]] | alt | 331 | 0 | 20 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.250× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change · without an alert: [[Budesonide (drug)]] 0.05 µM 0.263× (z -11.2) |
| [[A498 (line)]] | wt | 255 | 3 (3 ⚠) | 16 | [[Selinexor (drug)]] 5 µM 3.28× (z +14.4) ⚠ cell-cycle shift, explains ~37% of this change | [[Triamcinolone (drug)]] 0.5 µM 0.230× (z -12.6) |
| [[HOP62 (line)]] | alt | 305 | 0 | 17 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change · without an alert: [[Budesonide (drug)]] 0.05 µM 0.262× (z -11.6) |
| [[C32 (line)]] | wt | 621 | 0 | 14 (12 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.161× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 252 | 0 | 12 | — | [[Budesonide (drug)]] 5 µM 0.263× (z -10.7) |
| [[BT-474 (line)]] | alt | 57.9 | 10 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 14.7× (z +22.0) | — |
| [[CFPAC-1 (line)]] | alt | 777 | 1 (1 ⚠) | 8 (7 ⚠) | [[Selinexor (drug)]] 5 µM 2.13× (z +10.3) ⚠ cell-cycle shift, explains ~37% of this change | [[Panobinostat (drug)]] 0.5 µM 0.241× (z -13.9) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.113× (z -11.1) |
| [[A-172 (line)]] | wt | 361 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.217× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 0.369× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 279 | 0 | 7 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.301× (z -9.6) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Budesonide (drug)]] 0.05 µM 0.319× (z -9.1) |
| [[SW 900 (line)]] | alt | 391 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.221× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change · without an alert: [[Budesonide (drug)]] 0.05 µM 0.298× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 151 | 6 (2 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.81× (z +16.6) | — |
| [[HEC-1-A (line)]] | alt | 91.8 | 4 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +15.3) | [[Belinostat (drug)]] 0.5 µM 0.470× (z -8.6) |
| [[COLO 205 (line)]] | alt | 127 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +15.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 3.87× (z +10.6) | — |
| [[HT-29 (line)]] | alt | 78.2 | 4 | 0 | [[Auranofin (drug)]] 5 µM 5.40× (z +15.9) | — |
| [[NCI-H23 (line)]] | alt | 66.8 | 4 | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.75× (z +11.6) | — |
| [[NCI-H460 (line)]] | wt | 74.3 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.47× (z +20.6) | — |
| [[Panc 03.27 (line)]] | alt | 116 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +13.7) | — |
| [[RKO (line)]] | wt | 86.8 | 3 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.81× (z +17.8) | [[PH-797804 (drug)]] 5 µM 0.163× (z -8.8) |
| [[A-427 (line)]] | wt | 70.3 | 3 | 0 | [[Auranofin (drug)]] 5 µM 6.37× (z +17.5) | — |
| [[LoVo (line)]] | wt | 155 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +13.5) | — |
| [[LOX-IMVI (line)]] | wt | 158 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +11.8) | — |
| [[SW1417 (line)]] | alt | 139 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +10.0) | — |
| [[H4 (line)]] | wt | 119 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 6.30× (z +12.9) | — |
| [[HepG2_C3A (line)]] | wt | 91.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +12.1) | [[Dinaciclib (drug)]] 0.05 µM 0.232× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[J82 (line)]] | alt | 72.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +13.7) | — |
| [[KATO III (line)]] | alt | 62.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +10.2) | — |
| [[SHP-77 (line)]] | alt | 214 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 277 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.310× (z -8.8) ⚠ cell-cycle shift, explains ~18% of this change |
| [[AsPC-1 (line)]] | alt | 379 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.343× (z -9.6) ⚠ cell-cycle shift, explains ~38% of this change |
| [[C-33 A (line)]] | alt | 127 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.69× (z +11.9) | — |
| [[CHP-212 (line)]] | wt | 134 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.93× (z +8.7) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[HCT15 (line)]] | alt | 140 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.07× (z +8.6) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[Hs 766T (line)]] | wt | 511 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 207 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.63× (z +11.0) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[PANC-1 (line)]] | alt | 146 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.406× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[SK-MEL-2 (line)]] | alt | 128 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.93× (z +14.4) | — |
| [[SNU-1 (line)]] | wt | 201 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0770× (z -11.4) |
| [[SNU-423 (line)]] | alt | 109 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.28× (z +11.0) | — |
| [[SW480 (line)]] | alt | 384 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.336× (z -10.4) ⚠ cell-cycle shift, explains ~18% of this change |
| [[A549 (line)]] | wt | 55.1 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 129 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 325 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 223 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 388 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 88.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 240 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12664), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*44 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS6]] | +0.90 | +0.93 / +0.87 | both halves | 7e-06 | STRING 695; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[LINC00310]] | +0.74 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[NPTX1]] | +0.56 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[SERINC5]] | +0.53 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[CXCR4]] | +0.53 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[SMIM4]] | +0.51 | +0.34 / +0.44 | both halves | 1e-04 |  |
| [[ADCY10]] | +0.50 | +0.38 / +0.38 | both halves | 7e-05 |  |
| [[GDNF-AS1]] | +0.50 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[ARHGAP21]] | +0.49 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[CYP27C1]] | +0.48 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[METTL21A]] | +0.48 | +0.35 / +0.47 | both halves | 1e-04 |  |
| [[LSMEM1]] | +0.48 | +0.29 / +0.42 | both halves | 3e-04 |  |
| [[VAMP1]] | +0.47 | +0.39 / +0.44 | both halves | 5e-05 |  |

## Genes that move opposite

*56 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARMC8]] | -0.62 | -0.59 / -0.69 | both halves | 7e-06 |  |
| [[RIOK1]] | -0.54 | -0.46 / -0.51 | both halves | 2e-05 |  |
| [[MAOA]] | -0.54 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[FAM222B]] | -0.54 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[BTF3L4]] | -0.53 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[SCAP]] | -0.53 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[SMIM8]] | -0.51 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[COG2]] | -0.50 | -0.46 / -0.46 | both halves | 2e-05 |  |
| [[BTBD2]] | -0.50 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[DAW1]] | -0.49 | -0.55 / -0.35 | both halves | 1e-04 |  |
| [[SLC25A12]] | -0.49 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[WDR7]] | -0.48 | -0.45 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MT1M]] | B | MT1M activity raises SLC5A3's level | lines that do not express MT1M (29) vs lines expressing it (21) | 1.88× lower at baseline in the lines without MT1M | 0.062 | ⚠ within organs, on part of the lines; also absent: IRAK3, MIR155HG, G0S2 |
| [[TOP2A]] | B | TOP2A activity lowers SLC5A3's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[NR3C1]] | B | NR3C1 activity lowers SLC5A3's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.9% of all compounds | 0.079 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.401). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (44.3, -10.7); signed map (9.3, 18.3). **Vector** length 144, 49.6% of its response variance represented; |z| ≥ 3 in 1,785 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.3 | +7.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +9.7 | +9.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +9.6 | +7.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +9.2 | +7.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.2 | +8.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.5 | +0.7 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.6 | +3.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.5 | +2.3 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +2.3 | +1.7 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -11.1 | -9.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -7.6 | -5.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -6.8 | -3.6 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -6.7 | -2.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.3 | -6.2 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | -5.9 | -4.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -5.9 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 5 member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.11 — chr21:34,073,578-34,106,260 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SMIT, SMIT1 |
| Gene groups (HGNC) | Solute carrier family 5 |
| Reactome | 3 pathways, smallest: Inositol transporters; SLC-mediated transmembrane transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [P53794](https://www.uniprot.org/uniprotkb/P53794) (Sodium/myo-inositol cotransporter):

> Electrogenic Na(+)-coupled sugar symporter that actively transports myo-inositol and its stereoisomer scyllo-inositol across the plasma membrane, with a Na(+) to sugar coupling ratio of 2:1 (By similarity). Maintains myo-inositol concentration gradient that defines cell volume and fluid balance during osmotic stress, in particular in the fetoplacental unit and central nervous system (By similarity). Forms coregulatory complexes with voltage-gated K(+) ion channels, allosterically altering ion …

**Summary**, from NCBI Gene [6526](https://www.ncbi.nlm.nih.gov/gene/6526):

> Enables myo-inositol:sodium symporter activity; potassium channel regulator activity; and transmembrane transporter binding activity. Predicted to be involved in monosaccharide transmembrane transport and myo-inositol import across plasma membrane. Predicted to act upstream of or within several processes, including inositol metabolic process; positive regulation of reactive oxygen species biosynthetic process; and regulation of respiratory gaseous exchange. Located in perinuclear region of …

**Accessions** — [HGNC:11038](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11038) · Entrez [6526](https://www.ncbi.nlm.nih.gov/gene/6526) · UniProt [P53794](https://www.uniprot.org/uniprotkb/P53794) · Ensembl [ENSG00000198743](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198743)

## Data

Gene col 12664: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12664); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12664, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12664]; `tensor/DDL_lfc|DDL_z.npy` [12664]; `embed/gene_vectors.npy` [12664]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12664 or target_col == 12664). Every well: [[SLC5A3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC5A3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
