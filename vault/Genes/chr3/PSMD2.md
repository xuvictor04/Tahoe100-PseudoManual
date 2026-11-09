---
symbol: "PSMD2"
type: "gene"
col: 10572
ensembl_id: "ENSG00000175166"
name: "proteasome 26S subunit ubiquitin receptor, non-ATPase 2"
location: "3q27.1"
module: 60
arm: "+"
pooled_cpm: 114.98
n_lines_expressing: 50
n_dd_up: 39
n_dd_down: 2
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# PSMD2

*proteasome 26S subunit ubiquitin receptor, non-ATPase 2* — 3q27.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (25 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 3.86× (z +17.4, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.710× (z -3.7, q 0.074, down in 31 of 50 measured lines) ⚠ cell-cycle shift, explains ~61% of this change. The strongest without an alert is [[Bimiralisib (drug)]] 0.05 µM: 0.712× (z -3.7, q 0.074, down in 29 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Cobimetinib (drug)]] 5 µM in 2 lines (HepG2/C3A 0.296×, RKO 0.437×); [[Trametinib (drug)]] 5 µM in 2 lines (RKO 0.388×, HepG2/C3A 0.346×; ⚠ cell-cycle shift, explains ~61% of this change); [[Trametinib (drug)]] 0.5 µM in 2 lines (HepG2/C3A 0.410×, RKO 0.535×); [[Binimetinib (drug)]] 5 µM in 2 lines (HepG2/C3A 0.367×, RKO 0.452×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STIP1]] (+0.74, fdr 7e-06), [[PSMD14]] (+0.71, fdr 7e-06), [[HSPA8]] (+0.71, fdr 7e-06); moves opposite to [[POLR1H]] (-0.66, fdr 1e-05), [[SAT2]] (-0.64, fdr 7e-06), [[CEBPD]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 25 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 25 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10572.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.86×** | +17.4 | 0e+00 | 48/48 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **3.86×** | +17.3 | 0e+00 | 48/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **3.82×** | +17.2 | 0e+00 | 48/49 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **3.72×** | +16.2 | 0e+00 | 43/44 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **3.44×** | +14.7 | 0e+00 | 45/45 (A-172, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.99×** | +11.7 | 9e-30 | 47/48 (HT-29, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **2.45×** | +11.5 | 9e-29 | 47/48 (C32, COLO 205, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **2.39×** | +11.2 | 3e-27 | 45/48 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **2.39×** | +11.2 | 3e-27 | 48/48 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **3.79×** | +9.0 | 2e-17 | 46/49 (RKO, LOX-IMVI, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.97×** | +8.7 | 2e-16 | 45/48 (SW480, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.74×** | +6.8 | 6e-10 | 41/45 (SW1417, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~58% of this change | **1.71×** | +6.6 | 1e-09 | 39/47 (LoVo, NCI-H1792, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.56×** | +6.3 | 1e-08 | 35/48 (C32, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.95×** | +6.1 | 3e-08 | 42/49 (CFPAC-1, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.36×** | +5.6 | 7e-07 | 32/49 (CFPAC-1, SK-MEL-2, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.46×** | +4.9 | 3e-05 | 36/48 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.44×** | +4.5 | 2e-04 | 31/48 (CFPAC-1, SK-MEL-2, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.41×** | +4.4 | 2e-04 | 30/47 (SK-MEL-2, C32, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.43×** | +4.4 | 3e-04 | 31/47 (SK-MEL-2, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.005 | 25/48 (A-172, COLO 205, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.29×** | +3.2 | 0.019 | 24/48 (BT-474, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10572.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Cobimetinib (drug)]] 5 µM in 2 lines (HepG2/C3A 0.296×, RKO 0.437×); [[Trametinib (drug)]] 5 µM in 2 lines (RKO 0.388×, HepG2/C3A 0.346×; ⚠ cell-cycle shift, explains ~61% of this change); [[Trametinib (drug)]] 0.5 µM in 2 lines (HepG2/C3A 0.410×, RKO 0.535×); [[Binimetinib (drug)]] 5 µM in 2 lines (HepG2/C3A 0.367×, RKO 0.452×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.710×** | -3.7 | 0.074 | 31/50 (RKO, HepG2/C3A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.05 µM |  | **0.712×** | -3.7 | 0.074 | 29/49 (HepG2/C3A, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | 0.601× | -3.4 | 0.11 | 32/50 (HepG2/C3A, J82, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.835× | -3.3 | 0.14 | 21/48 (HepG2/C3A, J82, …) | all doses, flat | position effect removed |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | 0.709× | -3.2 | 0.17 | 24/48 (HCT15, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.791× | -3.0 | 0.23 | 26/48 (hTERT-HPNE, H4, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.71 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10572. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 60.8 | 12 (8 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.84× (z +16.7) | — |
| [[KATO III (line)]] | alt | 85.2 | 11 (7 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.70× (z +15.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 116 | 11 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.66× (z +15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 4.63× (z +13.2) | — |
| [[SW480 (line)]] | alt | 101 | 10 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.33× (z +16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 4.95× (z +15.6) | — |
| [[CFPAC-1 (line)]] | alt | 69.3 | 9 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.40× (z +13.8) | — |
| [[Panc 03.27 (line)]] | alt | 104 | 9 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.07× (z +15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 4.81× (z +14.7) | — |
| [[PANC-1 (line)]] | alt | 118 | 9 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.37× (z +16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 4.89× (z +15.1) | — |
| [[COLO 205 (line)]] | alt | 39.4 | 8 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 11.4× (z +14.7) | — |
| [[HT-29 (line)]] | alt | 68.8 | 8 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.34× (z +15.3) | — |
| [[NCI-H1792 (line)]] | alt | 52.9 | 8 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.0× (z +15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 5.94× (z +11.7) | — |
| [[NCI-H460 (line)]] | wt | 63.8 | 8 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.65× (z +17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 4.54× (z +15.3) | — |
| [[SW1417 (line)]] | alt | 106 | 8 (5 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.41× (z +13.2) | — |
| [[HepG2_C3A (line)]] | wt | 206 | 0 | 7 (1 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.296× (z -11.2) |
| [[A-172 (line)]] | wt | 174 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.76× (z +10.5) | — |
| [[A-427 (line)]] | wt | 303 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.70× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.92× (z +11.5) | — |
| [[A549 (line)]] | wt | 66.0 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.11× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 4.32× (z +11.2) | — |
| [[H4 (line)]] | wt | 135 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.42× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 5.22× (z +11.8) | — |
| [[HEC-1-A (line)]] | alt | 118 | 6 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.00× (z +13.9) | — |
| [[HS-578T (line)]] | alt | 160 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.48× (z +12.0) | — |
| [[hTERT-HPNE (line)]] | wt | 104 | 6 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.01× (z +10.3) | — |
| [[LOX-IMVI (line)]] | wt | 138 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.56× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.91× (z +11.9) | — |
| [[LS 180 (line)]] | wt | 83.5 | 6 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.38× (z +12.1) | — |
| [[RKO (line)]] | wt | 427 | 1 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.15× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.501× (z -11.2) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Binimetinib (drug)]] 5 µM 0.452× (z -9.2) |
| [[SNU-1 (line)]] | wt | 72.4 | 6 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.18× (z +12.5) | — |
| [[SNU-423 (line)]] | alt | 102 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.46× (z +14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 4.74× (z +11.1) | — |
| [[A498 (line)]] | wt | 115 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.28× (z +14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.82× (z +9.2) | — |
| [[AsPC-1 (line)]] | alt | 53.0 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.78× (z +10.7) | — |
| [[C32 (line)]] | wt | 85.5 | 5 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.87× (z +14.9) | — |
| [[HCT15 (line)]] | alt | 75.5 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.53× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 6.19× (z +11.7) | — |
| [[HOP62 (line)]] | alt | 123 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.94× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 4.01× (z +11.6) | — |
| [[Hs 766T (line)]] | wt | 65.8 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.87× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.95× (z +10.9) | — |
| [[NCI-H1573 (line)]] | alt | 71.7 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 9.31× (z +18.7) | — |
| [[NCI-H23 (line)]] | alt | 67.0 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.40× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.68× (z +10.2) | — |
| [[NCI-H2347 (line)]] | alt | 153 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +10.2) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.76× (z +9.7) | — |
| [[RPMI-7951 (line)]] | alt | 96.6 | 5 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.69× (z +11.1) | — |
| [[SW 900 (line)]] | alt | 71.3 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.86× (z +11.0) | — |
| [[NCI-H2030 (line)]] | alt | 164 | 4 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.36× (z +10.5) | — |
| [[SHP-77 (line)]] | alt | 96.5 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.01× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 114 | 4 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.90× (z +12.3) | — |
| [[BT-474 (line)]] | alt | 97.3 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.99× (z +9.7) | — |
| [[C-33 A (line)]] | alt | 123 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.29× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.16× (z +9.7) | — |
| [[J82 (line)]] | alt | 245 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -13.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 116 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.68× (z +9.7) | — |
| [[SW 1088 (line)]] | alt | 71.3 | 0 | 1 (1 ⚠) | — | [[Ivabradine (hydrochloride) (drug)]] 0.05 µM 0.0613× (z -8.6) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 154 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 68.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 96.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 113 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10572), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STIP1]] | +0.74 | +0.75 / +0.68 | both halves | 7e-06 | STRING 509 |
| [[PSMD14]] | +0.71 | +0.70 / +0.73 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[HSPA8]] | +0.71 | +0.71 / +0.65 | both halves | 7e-06 | pathway: AUF1 (hnRNP D0) binds and destabilizes mRNA; STRING 466 |
| [[TCP1]] | +0.70 | +0.70 / +0.65 | both halves | 7e-06 | STRING 796 |
| [[GPN1]] | +0.69 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[PSMD1]] | +0.69 | +0.72 / +0.67 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[CCT3]] | +0.68 | +0.69 / +0.64 | both halves | 7e-06 | STRING 797 |
| [[MSN]] | +0.68 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[HSP90AA1]] | +0.67 | +0.65 / +0.64 | both halves | 7e-06 | pathway: G2/M Transition; STRING 479 |
| [[TPM3]] | +0.66 | +0.67 / +0.57 | both halves | 8e-06 |  |
| [[ARPC5]] | +0.65 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[BCAP31]] | +0.65 | +0.57 / +0.64 | both halves | 9e-06 | pathway: Apoptosis |

## Genes that move opposite

*30 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR1H]] | -0.66 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[SAT2]] | -0.64 | -0.67 / -0.64 | both halves | 7e-06 |  |
| [[CEBPD]] | -0.62 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[FMC1]] | -0.62 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[TERF2IP]] | -0.61 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[ABCA5]] | -0.60 | -0.53 / -0.58 | both halves | 1e-05 | pathway: ABC-family protein mediated transport |
| [[ZNF330]] | -0.60 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[SNHG9]] | -0.60 | -0.66 / -0.59 | both halves | 7e-06 |  |
| [[CHKB]] | -0.60 | -0.61 / -0.46 | both halves | 3e-05 |  |
| [[PIM3]] | -0.60 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[RAB9A]] | -0.59 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[PNISR]] | -0.59 | -0.59 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PSMD2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LOXL1]] | B | LOXL1 activity raises PSMD2's level | lines that do not express LOXL1 (18) vs lines expressing it (32) | 1.30× lower at baseline in the lines without LOXL1 | 0.095 | ⚠ within organs, on part of the lines; also absent: B3GALNT1, LOXL1-AS1, ENSG00000255330 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.665). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-20.7, -12.0); signed map (-27.4, -29.6). **Vector** length 110, 45.7% of its response variance represented; |z| ≥ 3 in 1,616 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Formation of tubulin folding intermediates by CCT/TriC* (reactome, mean cos +0.54 to 5); *Prefoldin mediated transfer of substrate  to CCT/TriC* (reactome, mean cos +0.54 to 5); *Folding of actin by CCT/TriC* (reactome, mean cos +0.65 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.0 | +17.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +8.4 | +17.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +8.1 | +11.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +11.5 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.9 | +6.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.5 | +4.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +6.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.0 | +2.3 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.4 | +2.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.0 | +1.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -5.7 | +3.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.6 | +2.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.0 | +1.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.2 | -1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.1 | -1.8 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.6 | +0.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.6 | +0.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | proteasome 26S subunit ubiquitin receptor, non-ATPase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q27.1 — chr3:184,299,198-184,309,050 (+) |
| Ensembl biotype | protein_coding |
| Also known as | S2, P97, TRAP2, MGC14274, Rpn1 |
| Gene groups (HGNC) | Proteasome; Armadillo like helical domain containing |
| Reactome | 170 pathways, smallest: Regulation of activated PAK-2p34 by proteasome mediated degradation; Regulation of ornithine decarboxylase (ODC); Cross-presentation of soluble exogenous antigens (endosomes) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13200](https://www.uniprot.org/uniprotkb/Q13200) (26S proteasome non-ATPase regulatory subunit 2):

> Component of the 26S proteasome, a multiprotein complex involved in the ATP-dependent degradation of ubiquitinated proteins. This complex plays a key role in the maintenance of protein homeostasis by removing misfolded or damaged proteins, which could impair cellular functions, and by removing proteins whose functions are no longer required. Therefore, the proteasome participates in numerous cellular processes, including cell cycle progression, apoptosis, or DNA damage repair.; Binds to the …

**Summary**, from NCBI Gene [5708](https://www.ncbi.nlm.nih.gov/gene/5708):

> The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, and a lid, which contains up to 10 non-ATPase subunits. Proteasomes are distributed throughout …

**Accessions** — [HGNC:9559](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9559) · Entrez [5708](https://www.ncbi.nlm.nih.gov/gene/5708) · UniProt [Q13200](https://www.uniprot.org/uniprotkb/Q13200) · Ensembl [ENSG00000175166](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175166)

## Data

Gene col 10572: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10572); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10572, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10572]; `tensor/DDL_lfc|DDL_z.npy` [10572]; `embed/gene_vectors.npy` [10572]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10572 or target_col == 10572). Every well: [[PSMD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
