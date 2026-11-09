---
symbol: "FBXO32"
type: "gene"
col: 8015
ensembl_id: "ENSG00000156804"
name: "F-box protein 32"
location: "8q24.13"
module: 69
arm: "+"
pooled_cpm: 110.16
n_lines_expressing: 36
n_dd_up: 36
n_dd_down: 33
n_dd_up_clean: 31
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 10
direction_downstream: 22
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# FBXO32

*F-box protein 32* — 8q24.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.61× (z +9.8, q 7e-20, up in 24 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (11 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.158× (z -26.8, q 0e+00, down in 33 of 34 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.255× (z -10.4, q 1e-22, down in 31 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHL24]] (+0.68, fdr 7e-06), [[TCP11L2]] (+0.67, fdr 7e-06), [[CREBRF]] (+0.62, fdr 1e-05); moves opposite to [[RNGTT]] (-0.56, fdr 9e-06), [[HARS1]] (-0.53, fdr 2e-05), [[PDSS1]] (-0.53, fdr 3e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[MMP13]] → it (grade B ⚠); 22 go from it, the strongest it → [[POLR1A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8015.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.61×** | +9.8 | 7e-20 | 24/34 (SW1417, HS-578T, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.54×** | +8.9 | 1e-16 | 19/34 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.73×** | +7.9 | 4e-13 | 28/35 (HS-578T, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +7.7 | 1e-12 | 18/35 (HOP62, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.68×** | +7.5 | 5e-12 | 24/34 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.48×** | +5.5 | 5e-06 | 24/33 (Hs 766T, HS-578T, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.36×** | +5.3 | 1e-05 | 20/34 (SW 900, HS-578T, …) | two highest doses | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.97×** | +5.2 | 2e-05 | 23/36 (NCI-H1792, J82, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.36×** | +4.7 | 1e-04 | 22/36 (HS-578T, NCI-H460, …) | two highest doses | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | **1.23×** | +4.3 | 0.001 | 14/34 (SHP-77, J82, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.28×** | +4.2 | 0.002 | 18/35 (Hs 766T, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 5 µM |  | **1.22×** | +4.1 | 0.002 | 15/35 (NCI-H1792, HS-578T, …) | rises with dose |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.31×** | +4.0 | 0.003 | 16/34 (C32, SW 900, …) | all doses, stronger at high dose |  |
| [[Larotrectinib sulfate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +3.9 | 0.005 | 16/34 (C32, RPMI-7951, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 5 µM |  | **1.31×** | +3.7 | 0.007 | 12/34 (HOP62, LS 180, …) | top dose only |  |
| [[Sulfatinib (drug)]] 5 µM |  | **1.30×** | +3.7 | 0.007 | 11/35 (HOP62, HS-578T, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.24×** | +3.6 | 0.011 | 18/34 (Hs 766T, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8015.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.158×** | -26.8 | 0e+00 | 33/34 (C32, SW 900, …) | all doses, flat |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.255×** | -10.4 | 1e-22 | 31/34 (A549, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.484×** | -10.1 | 1e-21 | 23/31 (SNU-423, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.541×** | -8.9 | 8e-17 | 22/34 (SNU-423, NCI-H2347, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.320×** | -8.6 | 7e-16 | 30/34 (SW 900, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.446×** | -8.3 | 6e-15 | 28/34 (SW 900, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.359×** | -7.8 | 7e-13 | 29/34 (C32, SW 900, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.361×** | -7.7 | 9e-13 | 27/34 (C32, Panc 03.27, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.569×** | -7.7 | 9e-13 | 26/34 (LoVo, SW 900, …) | all doses, flat |  |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.591×** | -7.2 | 4e-11 | 22/34 (SW 900, LoVo, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.631×** | -6.7 | 1e-09 | 22/34 (NCI-H2347, SNU-423, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | **0.653×** | -6.2 | 3e-08 | 25/34 (SNU-423, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[venetoclax (drug)]] 5 µM |  | **0.449×** | -6.1 | 6e-08 | 22/34 (C32, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.707×** | -5.0 | 2e-05 | 21/34 (SW 900, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.708×** | -5.0 | 2e-05 | 16/34 (SW 900, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[EX229 (drug)]] 0.5 µM |  | **0.640×** | -4.6 | 1e-04 | 21/35 (C32, SW 900, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.574×** | -4.2 | 8e-04 | 18/34 (A549, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.814×** | -4.2 | 9e-04 | 16/34 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.777×** | -3.6 | 0.007 | 15/34 (AsPC-1, A498, …) | inconsistent across doses |  |
| [[Everolimus (drug)]] 5 µM |  | **0.716×** | -3.6 | 0.009 | 11/36 (LoVo, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Neratinib (drug)]] 5 µM |  | **0.791×** | -3.4 | 0.016 | 16/34 (LoVo, NCI-H1792, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.63 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8015. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 222 | 0 | 13 (9 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.115× (z -19.8) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 5 µM 0.251× (z -12.2) |
| [[C32 (line)]] | wt | 210 | 1 | 9 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +13.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0662× (z -23.6) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.111× (z -10.0) |
| [[LoVo (line)]] | wt | 123 | 0 | 10 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.144× (z -16.8) ⚠ unreliable plate only · without an alert: [[Neratinib (maleate) (drug)]] 5 µM 0.349× (z -12.9) |
| [[SNU-423 (line)]] | alt | 389 | 0 | 10 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.109× (z -20.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -18.2) |
| [[NCI-H1792 (line)]] | alt | 197 | 2 | 7 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +10.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.114× (z -18.9) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 759 | 0 | 8 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.201× (z -16.9) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -16.6) |
| [[A498 (line)]] | wt | 166 | 2 (1 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.73× (z +18.1) | [[Dinaciclib (drug)]] 0.5 µM 0.235× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.5 µM 0.330× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 324 | 2 | 5 (5 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.27× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.121× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[AsPC-1 (line)]] | alt | 72.7 | 0 | 6 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0966× (z -13.3) ⚠ unreliable plate only · without an alert: [[Dexamethasone (drug)]] 0.5 µM 0.165× (z -10.2) |
| [[HS-578T (line)]] | alt | 193 | 5 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +14.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.199× (z -12.4) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 70.0 | 0 | 5 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.143× (z -16.6) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.389× (z -11.4) |
| [[SK-MEL-2 (line)]] | alt | 192 | 0 | 5 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.107× (z -17.0) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.251× (z -14.9) |
| [[HOP62 (line)]] | alt | 64.6 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +15.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.229× (z -10.2) ⚠ unreliable plate only |
| [[HT-29 (line)]] | alt | 340 | 0 | 4 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0736× (z -19.7) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 32.7 | 2 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.06× (z +10.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.166× (z -11.7) ⚠ unreliable plate only |
| [[Panc 03.27 (line)]] | alt | 121 | 0 | 4 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.113× (z -17.5) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.131× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 43.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +10.6) | — |
| [[NCI-H460 (line)]] | wt | 36.4 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.150× (z -13.8) ⚠ unreliable plate only · without an alert: [[Clobetasol propionate (drug)]] 5 µM 0.304× (z -8.7) |
| [[SW1417 (line)]] | alt | 50.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +12.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.151× (z -13.5) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 60.1 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.138× (z -15.2) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0919× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 58.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +14.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.220× (z -10.8) ⚠ unreliable plate only |
| [[CHP-212 (line)]] | wt | 74.3 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.118× (z -9.2) ⚠ unreliable plate only |
| [[COLO 205 (line)]] | alt | 76.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +10.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0922× (z -13.4) ⚠ unreliable plate only |
| [[BT-474 (line)]] | alt | 150 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[H4 (line)]] | wt | 61.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.100× (z -12.9) ⚠ unreliable plate only |
| [[KATO III (line)]] | alt | 43.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.140× (z -14.0) ⚠ unreliable plate only |
| [[LS 180 (line)]] | wt | 91.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.193× (z -10.2) ⚠ unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 41.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.144× (z -12.8) ⚠ unreliable plate only |
| [[NCI-H596 (line)]] | alt | 99.0 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 5 µM 0.121× (z -9.0) |
| [[RKO (line)]] | wt | 32.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.140× (z -12.4) ⚠ unreliable plate only |
| [[SHP-77 (line)]] | alt | 67.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.176× (z -12.6) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 22.5 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 9.97 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 16.7 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 12.4 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.2 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 19.7 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 84.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 22.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[NCI-H661 (line)]] | alt | 11.9 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 23.1 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 79.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.5 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 20.2 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 20.2 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8015), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL24]] | +0.68 | +0.59 / +0.71 | both halves | 7e-06 | STRING 409 |
| [[TCP11L2]] | +0.67 | +0.58 / +0.71 | both halves | 7e-06 |  |
| [[CREBRF]] | +0.62 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[RB1CC1]] | +0.62 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[PIK3IP1]] | +0.61 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[OTUD1]] | +0.60 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[LITAF]] | +0.60 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[SLU7]] | +0.59 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[DHRS3]] | +0.59 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[GBP2]] | +0.58 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[PLD1]] | +0.58 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[SMIM14]] | +0.57 | +0.44 / +0.59 | both halves | 3e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNGTT]] | -0.56 | -0.58 / -0.57 | both halves | 9e-06 |  |
| [[HARS1]] | -0.53 | -0.46 / -0.54 | both halves | 2e-05 |  |
| [[PDSS1]] | -0.53 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[NUP205]] | -0.52 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[NAA15]] | -0.52 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[PPP5C]] | -0.52 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[EFTUD2]] | -0.51 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[FARSB]] | -0.51 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[EIPR1]] | -0.49 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[EEFSEC]] | -0.49 | -0.38 / -0.48 | both halves | 7e-05 |  |
| [[CS]] | -0.49 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[DROSHA]] | -0.48 | -0.45 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MMP13]] | B | MMP13 activity raises FBXO32's level | lines that do not express MMP13 (30) vs lines expressing it (20) | 2.46× lower at baseline in the lines without MMP13 | 0.006 | ⚠ within organs, on part of the lines; also absent: SOX11, AGT, STEAP4 |
| [[LRRN1]] | B | LRRN1 activity raises FBXO32's level | lines that do not express LRRN1 (31) vs lines expressing it (19) | 2.63× lower at baseline in the lines without LRRN1 | 0.011 | ⚠ within organs, on part of the lines; also absent: TACSTD2, PRKCH-AS1, SERPINB3; maybe low, not absent |
| [[MTOR]] | B | MTOR activity lowers FBXO32's level | compounds that target MTOR: 6 of 8 raise it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 7.3% of all compounds | 0.013 | ⚠ off-target possible; 6 compounds |
| [[PLD1]] | B | PLD1 activity raises FBXO32's level | lines that do not express PLD1 (7) vs lines expressing it (43) | 3.69× lower at baseline in the lines without PLD1 | 0.028 | ⚠ within organs, on part of the lines; also absent: DUSP1, ATP1B1, DUSP10; maybe low, not absent |
| [[GBP2]] | B | GBP2 activity raises FBXO32's level | lines that do not express GBP2 (13) vs lines expressing it (37) | 3.42× lower at baseline in the lines without GBP2 | 0.028 | ⚠ within organs, on part of the lines; also absent: GBP1, ITGA3, SH3TC1 |
| [[AHR]] | B | AHR activity raises FBXO32's level | lines that do not express AHR (7) vs lines expressing it (43) | 3.98× lower at baseline in the lines without AHR | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321, VDR, GPR39 |
| [[GATA6]] | B | GATA6 activity raises FBXO32's level | lines that do not express GATA6 (18) vs lines expressing it (32) | 2.80× lower at baseline in the lines without GATA6 | 0.056 | ⚠ within organs, on part of the lines; also absent: ENSG00000264825, CDA, SPTLC3 |
| [[C16orf74]] | B | C16orf74 activity lowers FBXO32's level | lines that do not express C16orf74 (11) vs lines expressing it (39) | 3.36× higher at baseline in the lines without C16orf74 | 0.058 | ⚠ within organs, on part of the lines; also absent: EPHA2, ABLIM2, FAM83H; maybe low, not absent |
| [[RASGEF1B]] | B | RASGEF1B activity raises FBXO32's level | lines that do not express RASGEF1B (10) vs lines expressing it (40) | 2.24× lower at baseline in the lines without RASGEF1B | 0.085 | ⚠ within organs, on part of the lines; also absent: FBXW10B; maybe low, not absent |
| [[DHRS3]] | C | DHRS3 activity raises FBXO32's level | lines that do not express DHRS3 (13) vs lines expressing it (37) | 3.60× lower at baseline in the lines without DHRS3 | 0.004 | ⚠ within organs, on part of the lines; also absent: CCDC9B, ENSG00000290729, STON2; co-absent with the target |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 21, C 1. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[POLR1A]] | B | FBXO32 activity lowers POLR1A's level | lines that do not express FBXO32 (14) vs lines expressing it (36) | 1.76× higher at baseline in the lines without FBXO32 | 0.004 | ⚠ within organs, on part of the lines; also absent: ETS2, BACE2, MLPH; maybe low, not absent |
| [[RND3]] | B | FBXO32 activity raises RND3's level | lines that do not express FBXO32 (14) vs lines expressing it (36) | 3.39× lower at baseline in the lines without FBXO32 | 0.008 | ⚠ within organs, on part of the lines; also absent: ETS2, BACE2, MLPH; maybe low, not absent |
| [[B2M]] | B | FBXO32 activity raises B2M's level | lines that do not express FBXO32 (14) vs lines expressing it (36) | 1.76× lower at baseline in the lines without FBXO32 | 0.010 | ⚠ within organs, on part of the lines; also absent: ETS2, BACE2, MLPH; maybe low, not absent |
| [[PELI2]] | B | FBXO32 activity raises PELI2's level | lines that do not express FBXO32 (14) vs lines expressing it (36) | 3.39× lower at baseline in the lines without FBXO32 | 0.012 | ⚠ within organs, on part of the lines; also absent: ETS2, BACE2, MLPH; maybe low, not absent |
| [[TCP11L2]] | B | FBXO32 activity raises TCP11L2's level | lines that do not express FBXO32 (14) vs lines expressing it (36) | 1.55× lower at baseline in the lines without FBXO32 | 0.022 | ⚠ within organs, on part of the lines; also absent: ETS2, BACE2, MLPH; maybe low, not absent |
| [[BTG1]] | B | FBXO32 activity raises BTG1's level | lines that do not express FBXO32 (14) vs lines expressing it (36) | 1.86× lower at baseline in the lines without FBXO32 | 0.026 | ⚠ within organs, on part of the lines; also absent: ETS2, BACE2, MLPH; maybe low, not absent |
| [[PRKDC]] | B | FBXO32 activity lowers PRKDC's level | lines that do not express FBXO32 (14) vs lines expressing it (36) | 1.63× higher at baseline in the lines without FBXO32 | 0.033 | ⚠ within organs, on part of the lines; also absent: ETS2, BACE2, MLPH; maybe low, not absent |
| [[PLD1]] | B | FBXO32 activity raises PLD1's level | lines that do not express FBXO32 (14) vs lines expressing it (36) | 2.10× lower at baseline in the lines without FBXO32 | 0.041 | ⚠ within organs, on part of the lines; also absent: ETS2, BACE2, MLPH; maybe low, not absent |
| [[GPX4]] | B | FBXO32 activity lowers GPX4's level | lines that do not express FBXO32 (14) vs lines expressing it (36) | 1.49× higher at baseline in the lines without FBXO32 | 0.042 | ⚠ within organs, on part of the lines; also absent: ETS2, BACE2, MLPH; maybe low, not absent |
| [[GBP2]] | B | FBXO32 activity raises GBP2's level | lines that do not express FBXO32 (14) vs lines expressing it (36) | 3.34× lower at baseline in the lines without FBXO32 | 0.044 | ⚠ within organs, on part of the lines; also absent: ETS2, BACE2, MLPH; maybe low, not absent |
| [[HARS1]] | B | FBXO32 activity lowers HARS1's level | lines that do not express FBXO32 (14) vs lines expressing it (36) | 1.27× higher at baseline in the lines without FBXO32 | 0.045 | ⚠ within organs, on part of the lines; also absent: ETS2, BACE2, MLPH; maybe low, not absent |
| [[SDAD1P1]] | B | FBXO32 activity lowers SDAD1P1's level | lines that do not express FBXO32 (14) vs lines expressing it (36) | 1.40× higher at baseline in the lines without FBXO32 | 0.048 | ⚠ within organs, on part of the lines; also absent: ETS2, BACE2, MLPH; maybe low, not absent |

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.688). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-1.3, -44.2); signed map (-12.3, 10.5). **Vector** length 130, 37.3% of its response variance represented; |z| ≥ 3 in 1,507 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +9.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.6 | +7.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.1 | +8.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +3.4 | +3.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.2 | +5.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.0 | +3.2 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +3.0 | +5.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.9 | +4.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -10.6 | -26.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -7.2 | -10.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -6.8 | -8.6 |
|  | [[EX229 (drug)]] 5 µM |  | -6.6 | -7.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -6.6 | -7.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -5.8 | -6.1 |

## What is on record

|  |  |
|---|---|
| Name | F-box protein 32 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.13 — chr8:123,497,889-123,541,206 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MAFbx, ATROGIN1, Fbx32 |
| Gene groups (HGNC) | F-boxes other |
| Reactome | 6 pathways, smallest: FOXO-mediated transcription of oxidative stress, metabolic and neuronal genes; FOXO-mediated transcription; Neddylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969P5](https://www.uniprot.org/uniprotkb/Q969P5) (F-box only protein 32):

> Substrate recognition component of a SCF (SKP1-CUL1-F-box protein) E3 ubiquitin-protein ligase complex which mediates the ubiquitination and subsequent proteasomal degradation of target proteins. Probably recognizes and binds to phosphorylated target proteins during skeletal muscle atrophy. Recognizes TERF1. Negatively regulates macrophage efferocytosis by promoting the ubiquitination of the transcription factor KLF4, suppressing the receptor tyrosine kinase MERTK transcription (By similarity). …

**Summary**, from NCBI Gene [114907](https://www.ncbi.nlm.nih.gov/gene/114907):

> This gene encodes a member of the F-box protein family which is characterized by an approximately 40 amino acid motif, the F-box. The F-box proteins constitute one of the four subunits of the ubiquitin protein ligase complex called SCFs (SKP1-cullin-F-box), which function in phosphorylation-dependent ubiquitination. The F-box proteins are divided into 3 classes: Fbws containing WD-40 domains, Fbls containing leucine-rich repeats, and Fbxs containing either different protein-protein interaction …

**Accessions** — [HGNC:16731](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16731) · Entrez [114907](https://www.ncbi.nlm.nih.gov/gene/114907) · UniProt [Q969P5](https://www.uniprot.org/uniprotkb/Q969P5) · Ensembl [ENSG00000156804](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156804)

## Data

Gene col 8015: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8015); `tables/drug_effects.parquet` (70 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8015, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8015]; `tensor/DDL_lfc|DDL_z.npy` [8015]; `embed/gene_vectors.npy` [8015]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8015 or target_col == 8015). Every well: [[FBXO32 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXO32.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
