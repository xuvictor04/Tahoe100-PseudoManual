---
symbol: "SLC9A1"
type: "gene"
col: 1608
ensembl_id: "ENSG00000090020"
name: "solute carrier family 9 member A1"
location: "1p36.11"
module: 93
arm: "+"
pooled_cpm: 64.85
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 5
n_dd_up_clean: 20
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# SLC9A1

*solute carrier family 9 member A1* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.51× (z +19.8, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.634× (z -4.1, q 0.024, down in 25 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Cabozantinib (S-malate) (drug)]] 5 µM: 0.674× (z -3.7, q 0.063, down in 35 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (HT-29 0.146×, SW1417 0.156×, COLO 205 0.122×, HepG2/C3A 0.134×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HepG2/C3A 0.0540×, SW480 0.315×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (LoVo 0.250×, KATO III 0.252×; ⚠ toxic; transcription drop); [[Verteporfin (drug)]] 5 µM in 1 line (HepG2/C3A 0.215×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POR]] (+0.72, fdr 7e-06), [[LRRC23]] (+0.71, fdr 7e-06), [[FAM53C]] (+0.69, fdr 7e-06); moves opposite to [[NDUFAF5]] (-0.63, fdr 7e-06), [[RPP30]] (-0.56, fdr 1e-05), [[GUSBP2-1]] (-0.54, fdr 1e-05).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1608.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.51×** | +19.8 | 0e+00 | 46/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **5.97×** | +16.6 | 0e+00 | 48/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **3.70×** | +12.1 | 1e-31 | 48/48 (SW480, A-427, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.49×** | +12.0 | 6e-31 | 40/47 (AsPC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.11×** | +10.1 | 6e-22 | 44/48 (SW480, HS-578T, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **4.01×** | +9.2 | 4e-18 | 48/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.58×** | +8.5 | 2e-15 | 44/50 (SW480, HS-578T, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.74×** | +7.3 | 2e-11 | 43/48 (LS 180, SK-MEL-2, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.76×** | +5.2 | 1e-05 | 34/47 (J82, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.71×** | +5.0 | 4e-05 | 38/48 (SW480, NCI-H2030, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.70×** | +4.9 | 5e-05 | 30/47 (HOP62, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.72×** | +4.8 | 6e-05 | 29/48 (NCI-H1573, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.68×** | +4.8 | 7e-05 | 33/48 (HS-578T, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.63×** | +4.5 | 3e-04 | 35/48 (LS 180, H4, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.61×** | +4.4 | 3e-04 | 32/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.63×** | +4.3 | 5e-04 | 31/47 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.56×** | +4.1 | 0.001 | 25/48 (AsPC-1, LS 180, …) | top dose only | cell-cycle shift (explains ~19% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.51×** | +3.8 | 0.004 | 27/49 (LS 180, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.49×** | +3.5 | 0.013 | 24/48 (SW480, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.97×** | +3.3 | 0.025 | 26/48 (PANC-1, A-427, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1608.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (HT-29 0.146×, SW1417 0.156×, COLO 205 0.122×, HepG2/C3A 0.134×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HepG2/C3A 0.0540×, SW480 0.315×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (LoVo 0.250×, KATO III 0.252×; ⚠ toxic; transcription drop); [[Verteporfin (drug)]] 5 µM in 1 line (HepG2/C3A 0.215×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.634×** | -4.1 | 0.024 | 25/40 (LoVo, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.674×** | -3.7 | 0.063 | 35/48 (LoVo, HS-578T, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.666×** | -3.5 | 0.080 | 25/44 (HepG2/C3A, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.498×** | -3.4 | 0.080 | 28/47 (NCI-H23, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.686×** | -3.4 | 0.080 | 27/47 (AN3 CA, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | 0.715× | -3.1 | 0.16 | 25/48 (NCI-H23, LOX-IMVI, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.74 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1608. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 46.2 | 7 (3 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.30× (z +20.7) | [[Dinaciclib (drug)]] 0.05 µM 0.315× (z -8.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 57.7 | 6 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.46× (z +18.5) | — |
| [[HS-578T (line)]] | alt | 45.7 | 6 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.51× (z +18.4) | — |
| [[HOP62 (line)]] | alt | 59.4 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.64× (z +16.1) | — |
| [[Hs 766T (line)]] | wt | 51.5 | 5 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.65× (z +18.0) | — |
| [[NCI-H1573 (line)]] | alt | 78.8 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +13.9) | — |
| [[NCI-H23 (line)]] | alt | 103 | 3 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 5.05× (z +11.4) | [[Adagrasib (drug)]] 0.05 µM 0.490× (z -17.2) ⚠ position not correctable |
| [[H4 (line)]] | wt | 45.2 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.68× (z +13.1) | — |
| [[HT-29 (line)]] | alt | 127 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.02× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 67.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.96× (z +12.4) | — |
| [[KATO III (line)]] | alt | 108 | 3 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.76× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.252× (z -10.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 52.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +15.7) | — |
| [[PANC-1 (line)]] | alt | 64.8 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.18× (z +16.7) | — |
| [[SK-MEL-2 (line)]] | alt | 37.4 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +14.9) | — |
| [[SW 900 (line)]] | alt | 46.1 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.54× (z +13.8) | — |
| [[A-172 (line)]] | wt | 24.3 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.92× (z +14.2) | — |
| [[A-427 (line)]] | wt | 50.7 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 10.3× (z +15.4) | — |
| [[A498 (line)]] | wt | 38.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +11.9) | — |
| [[A549 (line)]] | wt | 27.0 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.98× (z +14.8) | — |
| [[COLO 205 (line)]] | alt | 88.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.09× (z +14.9) | [[Dinaciclib (drug)]] 0.5 µM 0.122× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 118 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0540× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Verteporfin (drug)]] 5 µM 0.215× (z -9.0) |
| [[J82 (line)]] | alt | 74.2 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.18× (z +13.5) | — |
| [[LoVo (line)]] | wt | 133 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.250× (z -11.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 94.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.28× (z +12.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 38.0 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.5× (z +17.5) | — |
| [[NCI-H1792 (line)]] | alt | 48.1 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.62× (z +10.7) | — |
| [[NCI-H460 (line)]] | wt | 77.2 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +13.0) | — |
| [[Panc 03.27 (line)]] | alt | 47.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.53× (z +14.3) | — |
| [[SHP-77 (line)]] | alt | 21.0 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 8.30× (z +11.6) | — |
| [[SW1417 (line)]] | alt | 69.3 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.61× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 45.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.10× (z +13.7) | — |
| [[C32 (line)]] | wt | 118 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +9.5) | — |
| [[CFPAC-1 (line)]] | alt | 44.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.35× (z +15.3) | — |
| [[HCT15 (line)]] | alt | 76.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.86× (z +12.9) | — |
| [[NCI-H2030 (line)]] | alt | 79.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.87× (z +10.7) | — |
| [[NCI-H2347 (line)]] | alt | 53.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.63× (z +9.6) | — |
| [[RPMI-7951 (line)]] | alt | 55.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.00× (z +13.0) | — |
| [[SNU-423 (line)]] | alt | 48.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.80× (z +11.7) | — |
| [[SW48 (line)]] | wt | 56.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.37× (z +15.1) | — |
| [[BT-474 (line)]] | alt | 96.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +11.8) | — |
| [[HEC-1-A (line)]] | alt | 39.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.85× (z +15.1) | — |
| [[RKO (line)]] | wt | 126 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.37× (z +15.4) | — |
| [[AN3 CA (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 88.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 89.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 76.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1608), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POR]] | +0.72 | +0.72 / +0.67 | both halves | 7e-06 |  |
| [[LRRC23]] | +0.71 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[FAM53C]] | +0.69 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[LINC00910]] | +0.67 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[PYGM]] | +0.66 | +0.68 / +0.61 | both halves | 7e-06 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |
| [[GTF2B]] | +0.66 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[RAB7A]] | +0.65 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[NABP1]] | +0.65 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[ERN1]] | +0.63 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[SPSB1]] | +0.63 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[TEX14]] | +0.62 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[FAM222A]] | +0.62 | +0.68 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFAF5]] | -0.63 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[RPP30]] | -0.56 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[GUSBP2-1]] | -0.54 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[KAT7]] | -0.54 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[AIFM1]] | -0.53 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[TMEM218]] | -0.53 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[C5orf22]] | -0.51 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[ABHD13]] | -0.51 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[MSL2]] | -0.51 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[KCTD3]] | -0.51 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[HSF2]] | -0.50 | -0.52 / -0.37 | both halves | 8e-05 |  |
| [[ATG3]] | -0.50 | -0.45 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SLC9A1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[C21orf91-OT1]] | B | C21orf91-OT1 activity raises SLC9A1's level | lines that do not express C21orf91-OT1 (5) vs lines expressing it (45) | 1.72× lower at baseline in the lines without C21orf91-OT1 | 0.053 | ⚠ within organs, on part of the lines; co-absent genes; also absent: USP25, GSDMD, RALGPS2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.774). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.1, -25.8); signed map (3.7, 16.9). **Vector** length 130, 47.8% of its response variance represented; |z| ≥ 3 in 1,329 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[PF-06260933 (drug)]] 5 µM |  | +5.6 | +2.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.5 | +4.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +5.4 | +5.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +5.3 | +3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +7.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +3.2 | +2.9 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.5 | -3.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.9 | -0.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.5 | -2.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.3 | -0.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.2 | -3.5 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -4.9 | -3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.7 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.3 | -1.6 |
|  | [[Doxycycline (monohydrate) (drug)]] 5 µM |  | -3.2 | -2.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.0 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 9 member A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:27,098,809-27,166,981 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PPP1R143; previously APNH, NHE1, NHE-1 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; Solute carrier family 9 |
| Reactome | 8 pathways, smallest: Sodium/Proton exchangers; Hyaluronan degradation; Hyaluronan metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P19634](https://www.uniprot.org/uniprotkb/P19634) (Sodium/hydrogen exchanger 1):

> Electroneutral Na(+) /H(+) antiporter that extrudes Na(+) in exchange for external protons driven by the inward sodium ion chemical gradient, protecting cells from acidification that occurs from metabolism. Exchanges intracellular H(+) ions for extracellular Na(+) in 1:1 stoichiometry (By similarity). Plays a key role in maintening intracellular pH neutral and cell volume, and thus is important for cell growth, proliferation, migration and survival. In addition, can transport lithium Li(+) and …

**Summary**, from NCBI Gene [6548](https://www.ncbi.nlm.nih.gov/gene/6548):

> This gene encodes a Na+/H+ antiporter that is a member of the solute carrier family 9. The encoded protein is a plasma membrane transporter that is expressed in the kidney and intestine. This protein plays a central role in regulating pH homeostasis, cell migration and cell volume. This protein may also be involved in tumor growth. [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:11071](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11071) · Entrez [6548](https://www.ncbi.nlm.nih.gov/gene/6548) · UniProt [P19634](https://www.uniprot.org/uniprotkb/P19634) · Ensembl [ENSG00000090020](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000090020)

## Data

Gene col 1608: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1608); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1608, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1608]; `tensor/DDL_lfc|DDL_z.npy` [1608]; `embed/gene_vectors.npy` [1608]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1608 or target_col == 1608). Every well: [[SLC9A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC9A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
