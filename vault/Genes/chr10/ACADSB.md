---
symbol: "ACADSB"
type: "gene"
col: 12147
ensembl_id: "ENSG00000196177"
name: "acyl-CoA dehydrogenase short/branched chain"
location: "10q26.13"
module: 5
arm: "-"
pooled_cpm: 27.02
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 20
n_dd_up_clean: 17
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# ACADSB

*acyl-CoA dehydrogenase short/branched chain* — 10q26.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.03× (z +29.4, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.393× (z -19.6, q 0e+00, down in 46 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.445× (z -17.0, q 0e+00, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (80 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 20 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRCP]] (+0.67, fdr 7e-06), [[HADHB]] (+0.62, fdr 7e-06), [[PCBP2]] (+0.58, fdr 1e-05); moves opposite to [[ZNF8]] (-0.57, fdr 2e-05), [[TOMM40L]] (-0.56, fdr 3e-05), [[NUTM2A-AS1]] (-0.55, fdr 1e-05).
> It sits in the **-** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ENTPD1-AS1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12147.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.03×** | +29.4 | 0e+00 | 48/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.50×** | +27.3 | 0e+00 | 44/47 (HEC-1-A, SW1417, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.36×** | +25.5 | 0e+00 | 48/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.66×** | +20.6 | 0e+00 | 46/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.78×** | +17.3 | 0e+00 | 30/48 (LS 180, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.87×** | +13.2 | 1e-37 | 37/43 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.89×** | +12.9 | 2e-36 | 24/36 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +11.9 | 8e-31 | 31/47 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.63×** | +10.3 | 5e-23 | 35/48 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.39×** | +9.8 | 6e-21 | 32/48 (HS-578T, Hs 766T, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +8.4 | 2e-15 | 29/48 (HS-578T, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.54×** | +8.4 | 2e-15 | 21/40 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.38×** | +6.8 | 6e-10 | 26/48 (PANC-1, HT-29, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.81×** | +6.6 | 2e-09 | 28/48 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.33×** | +6.0 | 9e-08 | 23/47 (SW1417, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.32×** | +5.9 | 1e-07 | 22/48 (KATO III, PANC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +5.1 | 1e-05 | 18/48 (HT-29, HEC-1-A, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.53×** | +4.7 | 7e-05 | 15/47 (PANC-1, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.22×** | +4.3 | 6e-04 | 10/48 (KATO III, LS 180, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12147.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.393×** | -19.6 | 0e+00 | 46/47 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.445×** | -17.0 | 0e+00 | 40/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.502×** | -14.5 | 3e-45 | 43/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.522×** | -13.6 | 3e-40 | 39/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.573×** | -11.7 | 2e-29 | 37/48 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.663×** | -8.6 | 6e-16 | 30/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.668×** | -8.5 | 2e-15 | 30/48 (SW480, NCI-H23, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.726×** | -6.7 | 2e-09 | 22/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.551×** | -6.5 | 4e-09 | 26/48 (SW480, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.570×** | -6.2 | 4e-08 | 23/48 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.750×** | -5.8 | 3e-07 | 23/47 (SW480, NCI-H460, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.638×** | -4.9 | 4e-05 | 21/42 (A549, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.794×** | -4.8 | 7e-05 | 20/48 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.797×** | -4.7 | 8e-05 | 14/48 (SW480, HepG2/C3A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.800×** | -4.7 | 1e-04 | 15/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 0.5 µM |  | **0.806×** | -4.5 | 2e-04 | 16/48 (NCI-H661, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.817×** | -4.0 | 0.002 | 13/48 (HS-578T, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.875× | -3.9 | 0.003 | 12/48 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | 0.845× | -3.5 | 0.013 | 13/48 (SW 1271, H4, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.843× | -3.4 | 0.015 | 10/48 (SW480, MIA PaCa-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12147. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 35.8 | 7 | 11 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 4.76× (z +18.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.272× (z -15.1) |
| [[NCI-H460 (line)]] | wt | 35.7 | 5 (1 ⚠) | 9 (4 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.66× (z +14.6) | [[Digitoxin (drug)]] 0.5 µM 0.251× (z -15.5) |
| [[PANC-1 (line)]] | alt | 32.3 | 6 (1 ⚠) | 6 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.60× (z +19.6) | [[Digitoxin (drug)]] 5 µM 0.184× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.258× (z -15.4) |
| [[A549 (line)]] | wt | 28.6 | 4 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.06× (z +13.4) | [[Bortezomib (drug)]] 5 µM 0.0840× (z -10.8) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.342× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 22.6 | 6 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.25× (z +15.9) | — |
| [[HT-29 (line)]] | alt | 15.6 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 9.62× (z +13.2) | [[Digitoxin (drug)]] 5 µM 0.207× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 28.6 | 2 | 4 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.16× (z +9.2) | [[Digitoxin (drug)]] 5 µM 0.139× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.211× (z -12.4) |
| [[C32 (line)]] | wt | 33.6 | 2 | 3 | [[Panobinostat (drug)]] 5 µM 3.77× (z +9.5) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.276× (z -9.3) |
| [[LoVo (line)]] | wt | 29.4 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 4.39× (z +14.3) | — |
| [[LS 180 (line)]] | wt | 29.8 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +14.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 32.4 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.82× (z +15.4) | — |
| [[NCI-H1792 (line)]] | alt | 26.2 | 5 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +13.7) | — |
| [[SW1417 (line)]] | alt | 39.6 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.54× (z +16.2) | [[Digitoxin (drug)]] 5 µM 0.387× (z -9.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 7.91 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 16.1× (z +12.6) | — |
| [[HS-578T (line)]] | alt | 16.8 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.98× (z +13.1) | — |
| [[KATO III (line)]] | alt | 26.2 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.46× (z +14.6) | [[Digitoxin (drug)]] 5 µM 0.312× (z -9.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 19.6 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.46× (z +11.9) | [[Digitoxin (drug)]] 5 µM 0.252× (z -9.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 29.1 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.85× (z +10.6) | [[Digitoxin (drug)]] 5 µM 0.189× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.264× (z -8.9) |
| [[H4 (line)]] | wt | 32.9 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.10× (z +9.0) | [[Harringtonine (drug)]] 5 µM 0.177× (z -9.4) ⚠ cell-cycle shift, explains ~98% of this change |
| [[J82 (line)]] | alt | 10.0 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.44× (z +9.7) | [[Digitoxin (drug)]] 5 µM 0.161× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 26.5 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.04× (z +11.0) | [[Digitoxin (drug)]] 5 µM 0.335× (z -8.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 42.7 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +10.1) | [[Digitoxin (drug)]] 5 µM 0.103× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.286× (z -10.2) |
| [[A-172 (line)]] | wt | 14.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.15× (z +13.0) | — |
| [[A-427 (line)]] | wt | 31.1 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.21× (z +10.1) | [[Harringtonine (drug)]] 5 µM 0.183× (z -14.2) ⚠ cell-cycle shift, explains ~98% of this change |
| [[A498 (line)]] | wt | 11.0 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.94× (z +12.6) | — |
| [[C-33 A (line)]] | alt | 38.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +10.0) | [[Digitoxin (drug)]] 5 µM 0.288× (z -8.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 69.6 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.284× (z -9.2) |
| [[Hs 766T (line)]] | wt | 23.9 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.97× (z +9.9) | — |
| [[NCI-H2347 (line)]] | alt | 12.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.48× (z +11.4) | — |
| [[SHP-77 (line)]] | alt | 45.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +10.2) | — |
| [[SK-MEL-2 (line)]] | alt | 29.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.67× (z +10.8) | — |
| [[CFPAC-1 (line)]] | alt | 24.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.313× (z -8.5) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 21.3 | 0 | 1 | — | [[Pralsetinib (drug)]] 0.05 µM 0.0540× (z -8.5) |
| [[COLO 205 (line)]] | alt | 18.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +8.6) | — |
| [[HCT15 (line)]] | alt | 41.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.207× (z -9.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 18.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +8.9) | — |
| [[hTERT-HPNE (line)]] | wt | 21.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.92× (z +9.3) | — |
| [[NCI-H23 (line)]] | alt | 23.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.39× (z +10.2) | — |
| [[Panc 03.27 (line)]] | alt | 23.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +9.8) | — |
| [[RKO (line)]] | wt | 37.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +12.0) | — |
| [[RPMI-7951 (line)]] | alt | 20.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.70× (z +10.5) | — |
| [[SNU-1 (line)]] | wt | 34.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.135× (z -11.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 35.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.44× (z +10.4) | — |
| [[AN3 CA (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12147), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRCP]] | +0.67 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[HADHB]] | +0.62 | +0.67 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 986 |
| [[PCBP2]] | +0.58 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[OAT]] | +0.58 | +0.47 / +0.60 | both halves | 2e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[ALDH6A1]] | +0.58 | +0.43 / +0.54 | both halves | 3e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 755 |
| [[STYX]] | +0.58 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[CHCHD7]] | +0.54 | +0.72 / +0.50 | both halves | 1e-05 |  |
| [[CPNE3]] | +0.54 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[KIAA1191]] | +0.54 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[ZNF490]] | +0.52 | +0.73 / +0.49 | both halves | 1e-05 |  |
| [[YME1L1]] | +0.51 | +0.60 / +0.38 | both halves | 7e-05 | pathway: Mitochondrial protein degradation |
| [[MAN1B1]] | +0.50 | +0.21 / +0.46 | both halves | 6e-04 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF8]] | -0.57 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[TOMM40L]] | -0.56 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[NUTM2A-AS1]] | -0.55 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[RRP7A]] | -0.54 | -0.25 / -0.61 | both halves | 4e-04 |  |
| [[UBL4A]] | -0.52 | -0.42 / -0.63 | both halves | 4e-05 |  |
| [[EXOSC4]] | -0.52 | -0.30 / -0.49 | both halves | 2e-04 |  |
| [[FADD]] | -0.51 | -0.23 / -0.59 | both halves | 5e-04 |  |
| [[RASAL2]] | -0.51 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[C1orf159]] | -0.51 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[RRS1]] | -0.50 | -0.20 / -0.53 | both halves | 7e-04 |  |
| [[MRPL20-AS1]] | -0.50 | -0.13 / -0.56 | ⚠ one half (not replicated) | 0.002 |  |
| [[NIP7]] | -0.49 | -0.21 / -0.57 | both halves | 6e-04 |  |
| [[SFMBT1]] | -0.49 | -0.42 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ENTPD1-AS1]] | C | ENTPD1-AS1 activity raises ACADSB's level | lines that do not express ENTPD1-AS1 (3) vs lines expressing it (47) | 1.91× lower at baseline in the lines without ENTPD1-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LRRIQ3, WDR35, ENSG00000287400; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **-** arm (projection on the module's main direction -0.381). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-23.5, -19.1); signed map (-15.3, 3.5). **Vector** length 78.2, 18.4% of its response variance represented; |z| ≥ 3 in 1,376 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.7 | +17.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +13.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +12.9 |
|  | [[NG25 (drug)]] 5 µM |  | +2.3 | +3.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +2.3 | +9.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.2 | +4.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.0 | +6.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +1.7 | -0.9 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | +1.6 | -1.5 |
|  | [[Cloxacillin (sodium) (drug)]] 0.05 µM |  | +1.4 | -0.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.7 | -8.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.3 | -11.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.0 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.6 | -4.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.1 | -19.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.8 | -6.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.3 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | acyl-CoA dehydrogenase short/branched chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.13 — chr10:123,008,979-123,058,290 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SBCAD, ACAD7 |
| Gene groups (HGNC) | Acyl-CoA dehydrogenase family; Flavoproteins |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 3 pathways, smallest: Branched-chain amino acid catabolism; Mitochondrial protein degradation; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P45954](https://www.uniprot.org/uniprotkb/P45954) (Short/branched chain specific acyl-CoA dehydrogenase, mitochondrial):

> Short and branched chain specific acyl-CoA dehydrogenase that catalyzes the proR-proR stereospecific alpha,beta-dehydrogenation of fatty acyl-CoA thioesters using the electron transfer flavoprotein (ETF) as their physiologic electron acceptor, resulting in the formation of trans-2-enoyl-CoA ((2E)-enoyl-CoA). Among the different mitochondrial acyl-CoA dehydrogenases, acts specifically on short and branched chain acyl-CoA derivatives such as (S)-2-methylbutyryl-CoA as well as short straight chain …

**Summary**, from NCBI Gene [36](https://www.ncbi.nlm.nih.gov/gene/36):

> Short/branched chain acyl-CoA dehydrogenase(ACADSB) is a member of the acyl-CoA dehydrogenase family of enzymes that catalyze the dehydrogenation of acyl-CoA derivatives in the metabolism of fatty acids or branch chained amino acids. Substrate specificity is the primary characteristic used to define members of this gene family. The ACADSB gene product has the greatest activity towards the short branched chain acyl-CoA derivative, (S)-2-methylbutyryl-CoA, but also reacts significantly with other …

**Accessions** — [HGNC:91](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:91) · Entrez [36](https://www.ncbi.nlm.nih.gov/gene/36) · UniProt [P45954](https://www.uniprot.org/uniprotkb/P45954) · Ensembl [ENSG00000196177](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196177)

## Data

Gene col 12147: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12147); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12147, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12147]; `tensor/DDL_lfc|DDL_z.npy` [12147]; `embed/gene_vectors.npy` [12147]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12147 or target_col == 12147). Every well: [[ACADSB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACADSB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
