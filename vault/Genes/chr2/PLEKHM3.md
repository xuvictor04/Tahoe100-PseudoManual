---
symbol: "PLEKHM3"
type: "gene"
col: 10921
ensembl_id: "ENSG00000178385"
name: "pleckstrin homology domain containing M3"
location: "2q33.3"
module: 76
arm: "+"
pooled_cpm: 46.85
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 29
n_dd_up_clean: 14
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# PLEKHM3

*pleckstrin homology domain containing M3* — 2q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.38× (z +16.9, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (14 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.224× (z -29.2, q 0e+00, down in 48 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.534× (z -17.3, q 0e+00, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HACL1]] (+0.71, fdr 1e-05), [[TFDP2]] (+0.71, fdr 1e-05), [[MED30]] (+0.69, fdr 1e-05); moves opposite to [[ALG13]] (-0.53, fdr 4e-05), [[SECISBP2]] (-0.53, fdr 4e-05), [[KRBOX5]] (-0.52, fdr 6e-05).
> It is in [[Module 076]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10921.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.38×** | +16.9 | 0e+00 | 46/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.19×** | +15.3 | 0e+00 | 45/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.00×** | +13.6 | 1e-39 | 44/48 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.77×** | +11.1 | 1e-26 | 40/47 (HOP62, C32, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.80×** | +10.8 | 3e-25 | 39/48 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.73×** | +10.7 | 2e-24 | 38/48 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.68×** | +10.1 | 3e-22 | 38/48 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.46×** | +7.4 | 7e-12 | 29/47 (NCI-H460, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.89×** | +6.5 | 5e-09 | 36/49 (LoVo, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.36×** | +6.1 | 7e-08 | 35/48 (J82, NCI-H2030, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~95% of this change | **1.21×** | +5.3 | 8e-06 | 21/48 (RKO, LS 180, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +4.1 | 0.002 | 16/48 (SW 900, LS 180, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.16× | +4.0 | 0.002 | 9/48 (SW480, HepG2/C3A, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.26×** | +3.9 | 0.003 | 16/49 (SW480, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.46×** | +3.9 | 0.004 | 21/49 (CFPAC-1, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.20×** | +3.6 | 0.011 | 15/48 (AsPC-1, HT-29, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.19× | +3.5 | 0.017 | 18/48 (J82, SW480, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.035 | 8/49 (HepG2/C3A, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10921.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.224×** | -29.2 | 0e+00 | 48/48 (NCI-H460, SW1417, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.534×** | -17.3 | 0e+00 | 40/48 (HepG2/C3A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.221×** | -15.4 | 0e+00 | 47/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.251×** | -14.1 | 9e-43 | 45/48 (SNU-1, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.265×** | -13.5 | 1e-39 | 47/47 (NCI-H460, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.508×** | -12.7 | 8e-35 | 34/42 (A549, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[EX229 (drug)]] 5 µM |  | **0.302×** | -12.2 | 3e-32 | 42/48 (NCI-H2030, SW48, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.535×** | -12.2 | 3e-32 | 40/48 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[venetoclax (drug)]] 5 µM |  | **0.313×** | -11.8 | 2e-30 | 43/47 (NCI-H1792, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.539×** | -11.1 | 6e-27 | 36/44 (MIA PaCa-2, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.567×** | -10.6 | 1e-24 | 35/47 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.491×** | -9.9 | 2e-21 | 43/48 (NCI-H460, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **0.740×** | -8.3 | 6e-15 | 26/48 (A498, PANC-1, …) | rises with dose | composition shift |
| [[EX229 (drug)]] 0.05 µM |  | **0.650×** | -7.9 | 9e-14 | 35/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.579×** | -7.6 | 1e-12 | 37/48 (NCI-H1792, A498, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.698×** | -6.7 | 5e-10 | 29/49 (SNU-1, C32, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.702×** | -6.6 | 1e-09 | 28/47 (RKO, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.716×** | -6.5 | 2e-09 | 27/48 (MIA PaCa-2, C-33 A, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.660×** | -5.8 | 2e-07 | 30/48 (A498, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.619×** | -4.9 | 3e-05 | 24/46 (PANC-1, RKO, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.829×** | -3.4 | 0.011 | 14/48 (PANC-1, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10921. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 46.5 | 6 (1 ⚠) | 17 (10 ⚠) | [[Panobinostat (drug)]] 5 µM 2.82× (z +12.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.131× (z -24.7) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -15.4) |
| [[PANC-1 (line)]] | alt | 30.7 | 2 | 12 (10 ⚠) | [[Panobinostat (drug)]] 5 µM 2.80× (z +9.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.121× (z -20.2) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.0800× (z -12.7) |
| [[NCI-H2030 (line)]] | alt | 81.7 | 0 | 12 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -20.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -13.1) |
| [[SW480 (line)]] | alt | 52.9 | 2 | 8 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.21× (z +9.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.182× (z -19.8) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.190× (z -10.1) |
| [[A498 (line)]] | wt | 67.8 | 1 (1 ⚠) | 8 (5 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.77× (z +10.9) ⚠ cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -20.5) ⚠ cell-cycle shift, explains ~93% of this change · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.198× (z -9.6) |
| [[A549 (line)]] | wt | 48.8 | 3 | 6 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.76× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.0803× (z -24.4) ⚠ toxic; transcription drop · without an alert: [[Abemaciclib (drug)]] 5 µM 0.166× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 31.4 | 1 | 7 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 3.92× (z +10.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.118× (z -15.9) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -12.9) |
| [[HOP62 (line)]] | alt | 32.2 | 5 (1 ⚠) | 3 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 4.69× (z +13.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -13.0) |
| [[HT-29 (line)]] | alt | 53.5 | 0 | 8 (6 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.156× (z -17.0) ⚠ unreliable plate only · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.158× (z -8.8) |
| [[LS 180 (line)]] | wt | 40.2 | 5 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.62× (z +11.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.332× (z -9.9) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 54.7 | 1 | 6 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.70× (z +9.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.166× (z -16.5) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.0964× (z -11.3) |
| [[SW1417 (line)]] | alt | 69.2 | 0 | 7 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.107× (z -23.3) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -14.8) |
| [[C32 (line)]] | wt | 45.1 | 3 (1 ⚠) | 3 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 5.96× (z +12.2) | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -11.7) ⚠ cell-cycle shift, explains ~93% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 60.6 | 0 | 6 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.141× (z -19.6) ⚠ unreliable plate only · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.170× (z -9.3) |
| [[J82 (line)]] | alt | 47.9 | 3 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.21× (z +11.5) | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -11.9) ⚠ cell-cycle shift, explains ~93% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -10.4) |
| [[LoVo (line)]] | wt | 38.2 | 3 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.70× (z +12.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.160× (z -17.8) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 0.05 µM 0.273× (z -11.9) |
| [[RKO (line)]] | wt | 40.5 | 0 | 6 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.150× (z -15.3) ⚠ unreliable plate only · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.142× (z -15.1) |
| [[CFPAC-1 (line)]] | alt | 42.1 | 1 | 4 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.70× (z +9.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.231× (z -13.3) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.113× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 51.4 | 0 | 5 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.238× (z -14.7) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -11.5) |
| [[SK-MEL-2 (line)]] | alt | 52.2 | 2 | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.64× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.220× (z -13.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 47.4 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 4.25× (z +11.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.243× (z -10.8) ⚠ unreliable plate only |
| [[HepG2_C3A (line)]] | wt | 91.3 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.236× (z -16.0) |
| [[MIA PaCa-2 (line)]] | alt | 40.4 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.107× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.241× (z -11.9) |
| [[NCI-H23 (line)]] | alt | 76.1 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Abemaciclib (drug)]] 5 µM 0.191× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 32.9 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.91× (z +10.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.217× (z -14.8) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -12.5) |
| [[Panc 03.27 (line)]] | alt | 54.9 | 0 | 4 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.162× (z -16.3) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -12.4) |
| [[RPMI-7951 (line)]] | alt | 50.8 | 1 | 3 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.54× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.288× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[TAK-733 (drug)]] 5 µM 0.117× (z -9.0) |
| [[A-172 (line)]] | wt | 34.0 | 1 (1 ⚠) | 2 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.66× (z +10.1) ⚠ cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -15.0) ⚠ cell-cycle shift, explains ~93% of this change |
| [[CHP-212 (line)]] | wt | 55.4 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.203× (z -10.6) |
| [[H4 (line)]] | wt | 21.5 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 11.8× (z +11.0) | — |
| [[HS-578T (line)]] | alt | 38.8 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.12× (z +10.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.266× (z -12.1) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 49.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H661 (line)]] | alt | 125 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.137× (z -10.6) ⚠ unreliable plate only · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.0483× (z -8.5) |
| [[SNU-1 (line)]] | wt | 49.8 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 5 µM 0.0344× (z -11.8) |
| [[SW 900 (line)]] | alt | 51.9 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.156× (z -16.0) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -9.9) |
| [[A-427 (line)]] | wt | 53.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -16.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 20.8 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.46× (z +8.9) | — |
| [[SHP-77 (line)]] | alt | 63.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -13.9) |
| [[SNU-423 (line)]] | alt | 40.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -14.3) ⚠ cell-cycle shift, explains ~93% of this change |
| [[SW48 (line)]] | wt | 34.7 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0923× (z -13.1) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.0266× (z -10.4) |
| [[C-33 A (line)]] | alt | 45.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.218× (z -10.4) |
| [[Hs 766T (line)]] | wt | 17.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -10.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 32.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -11.9) ⚠ cell-cycle shift, explains ~93% of this change |
| [[KATO III (line)]] | alt | 29.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.243× (z -10.7) ⚠ unreliable plate only |
| [[SW 1271 (line)]] | alt | 75.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.119× (z -8.5) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10921), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HACL1]] | +0.71 | +0.53 / +0.73 | both halves | 1e-05 |  |
| [[TFDP2]] | +0.71 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[MED30]] | +0.69 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[CRBN]] | +0.67 | +0.42 / +0.75 | both halves | 4e-05 |  |
| [[NIPAL3]] | +0.63 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[STX18]] | +0.63 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[DPY30]] | +0.63 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[MBTPS1]] | +0.63 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[OSBPL9]] | +0.63 | +0.47 / +0.61 | both halves | 2e-05 | same gene group |
| [[CCDC28A]] | +0.62 | +0.32 / +0.66 | both halves | 2e-04 |  |
| [[FBXO3]] | +0.61 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[CAMK2G]] | +0.61 | +0.64 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALG13]] | -0.53 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[SECISBP2]] | -0.53 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[KRBOX5]] | -0.52 | -0.40 / -0.38 | both halves | 6e-05 |  |
| [[DGKH]] | -0.51 | -0.51 / -0.36 | both halves | 1e-04 | same gene group |
| [[SNX5]] | -0.50 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[P2RY11]] | -0.49 | -0.29 / -0.47 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.621). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (5.1, -46.8); signed map (-19.5, 8.5). **Vector** length 127, 42.4% of its response variance represented; |z| ≥ 3 in 1,640 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +10.2 | +11.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +10.0 | +10.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | +9.5 | +10.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.8 | +15.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.6 | +13.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.5 | +3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.4 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.1 | +6.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +2.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -16.1 | -29.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -12.3 | -17.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -10.5 | -15.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -10.5 | -13.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | -9.7 | -8.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -9.6 | -14.1 |
|  | [[EX229 (drug)]] 5 µM |  | -9.6 | -12.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -8.2 | -11.8 |

## What is on record

|  |  |
|---|---|
| Name | pleckstrin homology domain containing M3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.3 — chr2:207,821,288-208,025,527 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DAPR; previously PLEKHM1L |
| Gene groups (HGNC) | Pleckstrin homology domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZWE6](https://www.uniprot.org/uniprotkb/Q6ZWE6) (Pleckstrin homology domain-containing family M member 3):

> Involved in skeletal muscle differentiation. May act as a scaffold protein for AKT1 during muscle differentiation.

**Summary**, from NCBI Gene [389072](https://www.ncbi.nlm.nih.gov/gene/389072):

> Predicted to enable zinc ion binding activity. Predicted to be involved in myoblast differentiation. Predicted to be located in Golgi apparatus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:34006](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34006) · Entrez [389072](https://www.ncbi.nlm.nih.gov/gene/389072) · UniProt [Q6ZWE6](https://www.uniprot.org/uniprotkb/Q6ZWE6) · Ensembl [ENSG00000178385](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178385)

## Data

Gene col 10921: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10921); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10921, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10921]; `tensor/DDL_lfc|DDL_z.npy` [10921]; `embed/gene_vectors.npy` [10921]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10921 or target_col == 10921). Every well: [[PLEKHM3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLEKHM3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
