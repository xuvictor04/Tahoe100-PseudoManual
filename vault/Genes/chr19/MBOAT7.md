---
symbol: "MBOAT7"
type: "gene"
col: 4626
ensembl_id: "ENSG00000125505"
name: "membrane bound acylglycerophosphatidylinositol O-acyltransferase MBOAT7"
location: "19q13.42"
module: 72
arm: "+"
pooled_cpm: 52.14
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 15
n_dd_up_clean: 11
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# MBOAT7

*membrane bound acylglycerophosphatidylinositol O-acyltransferase MBOAT7* — 19q13.42

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 3.12× (z +20.2, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.402× (z -23.0, q 0e+00, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UFD1]] (+0.74, fdr 7e-06), [[KLHL25]] (+0.67, fdr 8e-06), [[SAP130]] (+0.67, fdr 7e-06); moves opposite to [[AASDHPPT]] (-0.71, fdr 7e-06), [[EBAG9]] (-0.67, fdr 7e-06), [[C12orf29]] (-0.64, fdr 7e-06).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[BIRC3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4626.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **3.12×** | +20.2 | 0e+00 | 48/48 (MIA PaCa-2, HEC-1-A, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +10.1 | 2e-21 | 39/48 (A549, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.74×** | +9.9 | 1e-20 | 39/48 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.78×** | +9.8 | 1e-20 | 33/39 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.45×** | +6.6 | 4e-09 | 33/48 (NCI-H2347, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.45×** | +6.6 | 5e-09 | 25/48 (NCI-H2347, A498, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.99×** | +6.0 | 2e-07 | 33/44 (A-427, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.47×** | +5.4 | 4e-06 | 28/48 (A498, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | **1.38×** | +5.3 | 8e-06 | 25/44 (J82, A498, …) | all doses, stronger at high dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +5.0 | 3e-05 | 1/49 (NCI-H661) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +4.2 | 0.001 | 20/47 (NCI-H2347, HT-29, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.2 | 0.001 | 24/49 (A-172, C32, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.23×** | +3.7 | 0.009 | 17/48 (Panc 03.27, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.016 | 14/48 (HS-578T, LOX-IMVI, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.51×** | +3.5 | 0.016 | 19/48 (MIA PaCa-2, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Infigratinib (drug)]] 5 µM |  | **1.44×** | +3.2 | 0.055 | 12/48 (BT-474, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 1.13× | +3.0 | 0.074 | 6/49 (RKO, LS 180, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.42×** | +3.0 | 0.079 | 9/47 (A-427, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.41×** | +3.0 | 0.081 | 14/47 (J82, HOP62, …) | top dose only | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4626.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.402×** | -23.0 | 0e+00 | 47/47 (HOP62, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.319×** | -20.4 | 0e+00 | 46/47 (CFPAC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.574×** | -9.5 | 3e-19 | 37/48 (SW 900, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.652×** | -7.6 | 3e-12 | 37/48 (SW 900, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.508×** | -5.9 | 4e-07 | 32/48 (HOP62, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.730×** | -5.6 | 2e-06 | 29/48 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.553×** | -5.2 | 2e-05 | 26/49 (A-427, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.816×** | -5.1 | 2e-05 | 21/48 (SNU-1, NCI-H1792, …) | rises with dose | low cells (technical?) |
| [[Verteporfin (drug)]] 5 µM |  | **0.773×** | -4.4 | 6e-04 | 21/48 (HOP62, A-172, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.779×** | -4.1 | 0.002 | 21/48 (PANC-1, NCI-H23, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | **0.759×** | -4.0 | 0.003 | 16/49 (MIA PaCa-2, A-172, …) | rises with dose | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.810×** | -3.8 | 0.007 | 18/48 (A498, HEC-1-A, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.824×** | -3.5 | 0.022 | 19/48 (SNU-1, A-172, …) | rises with dose |  |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | **0.822×** | -3.2 | 0.051 | 10/48 (HEC-1-A, RPMI-7951, …) | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.824×** | -3.2 | 0.053 | 8/48 (NCI-H460, HOP62, …) | inconsistent across doses | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | 0.835× | -3.1 | 0.066 | 14/48 (NCI-H23, A-172, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.844× | -3.0 | 0.078 | 12/48 (A-427, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4626. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 94.6 | 4 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +11.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.73× (z +11.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.292× (z -13.7) |
| [[NCI-H2347 (line)]] | alt | 37.0 | 4 | 2 | [[Ixazomib citrate (drug)]] 5 µM 2.65× (z +9.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.341× (z -10.8) |
| [[A-172 (line)]] | wt | 151 | 3 (2 ⚠) | 2 | [[Auranofin (drug)]] 5 µM 3.56× (z +14.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.331× (z -12.3) |
| [[HOP62 (line)]] | alt | 48.0 | 3 (2 ⚠) | 2 | [[Auranofin (drug)]] 5 µM 6.03× (z +17.0) | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -23.9) |
| [[SW 900 (line)]] | alt | 90.5 | 1 | 4 | [[Auranofin (drug)]] 5 µM 3.13× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -12.7) |
| [[HS-578T (line)]] | alt | 70.4 | 2 (1 ⚠) | 2 | [[Auranofin (drug)]] 5 µM 3.74× (z +12.3) | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -11.6) |
| [[J82 (line)]] | alt | 95.1 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.23× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.92× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -12.6) |
| [[LOX-IMVI (line)]] | wt | 50.2 | 1 | 3 | [[Auranofin (drug)]] 5 µM 4.68× (z +15.0) | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -19.7) |
| [[NCI-H2030 (line)]] | alt | 36.7 | 2 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -15.4) |
| [[NCI-H23 (line)]] | alt | 48.7 | 1 | 3 | [[Auranofin (drug)]] 5 µM 3.25× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -18.8) |
| [[Panc 03.27 (line)]] | alt | 34.6 | 1 | 3 | [[Auranofin (drug)]] 5 µM 4.01× (z +11.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.190× (z -13.8) |
| [[SW1417 (line)]] | alt | 54.6 | 2 | 2 | [[Auranofin (drug)]] 5 µM 3.11× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -12.6) |
| [[SW480 (line)]] | alt | 31.7 | 2 (1 ⚠) | 2 | [[Auranofin (drug)]] 5 µM 2.46× (z +9.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.244× (z -15.1) |
| [[A-427 (line)]] | wt | 60.4 | 1 | 2 | [[Auranofin (drug)]] 5 µM 4.08× (z +14.7) | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -23.7) |
| [[C32 (line)]] | wt | 32.9 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 7.42× (z +15.1) | — |
| [[H4 (line)]] | wt | 125 | 1 | 2 | [[Auranofin (drug)]] 5 µM 4.62× (z +12.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.195× (z -13.7) |
| [[HT-29 (line)]] | alt | 64.5 | 1 | 2 | [[Auranofin (drug)]] 5 µM 3.81× (z +13.1) | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -15.7) |
| [[LoVo (line)]] | wt | 34.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.278× (z -11.9) |
| [[NCI-H460 (line)]] | wt | 24.8 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -9.5) |
| [[PANC-1 (line)]] | alt | 64.9 | 1 | 2 | [[Auranofin (drug)]] 5 µM 2.77× (z +11.8) | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -14.8) |
| [[RKO (line)]] | wt | 43.3 | 1 | 2 | [[Auranofin (drug)]] 5 µM 3.57× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -12.0) |
| [[RPMI-7951 (line)]] | alt | 74.3 | 1 | 2 | [[Auranofin (drug)]] 5 µM 2.95× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -15.0) |
| [[A549 (line)]] | wt | 41.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +9.9) | — |
| [[BT-474 (line)]] | alt | 37.6 | 1 | 1 | [[Auranofin (drug)]] 5 µM 9.07× (z +16.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.312× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 36.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -16.1) |
| [[COLO 205 (line)]] | alt | 41.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.205× (z -10.4) |
| [[HCT15 (line)]] | alt | 59.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -13.7) |
| [[Hs 766T (line)]] | wt | 26.8 | 1 | 1 | [[Auranofin (drug)]] 5 µM 4.27× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -14.4) |
| [[hTERT-HPNE (line)]] | wt | 49.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.142× (z -14.6) |
| [[LS 180 (line)]] | wt | 47.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -11.1) |
| [[MIA PaCa-2 (line)]] | alt | 54.8 | 1 | 1 | [[Auranofin (drug)]] 5 µM 5.52× (z +17.2) | [[Homoharringtonine (drug)]] 0.5 µM 0.211× (z -15.6) |
| [[NCI-H1573 (line)]] | alt | 23.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -13.5) |
| [[SK-MEL-2 (line)]] | alt | 63.7 | 1 | 1 | [[Auranofin (drug)]] 5 µM 3.25× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -20.6) |
| [[SNU-423 (line)]] | alt | 27.2 | 1 | 1 | [[Auranofin (drug)]] 5 µM 6.22× (z +13.8) | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -11.1) |
| [[AsPC-1 (line)]] | alt | 38.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -10.6) |
| [[C-33 A (line)]] | alt | 96.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -11.3) |
| [[HEC-1-A (line)]] | alt | 64.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.48× (z +17.0) | — |
| [[KATO III (line)]] | alt | 42.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.21× (z +9.8) | — |
| [[NCI-H1792 (line)]] | alt | 43.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.311× (z -9.9) |
| [[SHP-77 (line)]] | alt | 23.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change |
| [[SNU-1 (line)]] | wt | 47.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.350× (z -8.9) ⚠ cell-cycle shift, explains ~34% of this change |
| [[AN3 CA (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 45.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4626), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UFD1]] | +0.74 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[KLHL25]] | +0.67 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[SAP130]] | +0.67 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[SPINDOC]] | +0.67 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[TNPO3]] | +0.65 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[PLOD3]] | +0.65 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[SNHG30]] | +0.64 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[MTCH1]] | +0.64 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[RAB43]] | +0.64 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[RAD9A]] | +0.63 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[CCDC32]] | +0.63 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[SS18L1]] | +0.62 | +0.69 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AASDHPPT]] | -0.71 | -0.71 / -0.74 | both halves | 7e-06 |  |
| [[EBAG9]] | -0.67 | -0.73 / -0.62 | both halves | 7e-06 |  |
| [[C12orf29]] | -0.64 | -0.69 / -0.62 | both halves | 7e-06 |  |
| [[POLR1F]] | -0.64 | -0.63 / -0.67 | both halves | 7e-06 |  |
| [[ZNF252P-1]] | -0.64 | -0.70 / -0.61 | both halves | 7e-06 |  |
| [[PEX1]] | -0.63 | -0.71 / -0.57 | both halves | 1e-05 |  |
| [[PCLO]] | -0.62 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[TIGD2]] | -0.62 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[MTPAP]] | -0.62 | -0.59 / -0.63 | both halves | 7e-06 |  |
| [[SMARCE1]] | -0.61 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[STK33]] | -0.61 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[RAD50]] | -0.61 | -0.65 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BIRC3]] | B | BIRC3 activity raises MBOAT7's level | lines that do not express BIRC3 (5) vs lines expressing it (45) | 1.22× lower at baseline in the lines without BIRC3 | 0.062 | ⚠ within organs, on part of the lines; also absent: LRRC8E, TRIM34, IFI35 |
| [[TEAD2]] | B | TEAD2 activity raises MBOAT7's level | lines that do not express TEAD2 (9) vs lines expressing it (41) | 1.32× lower at baseline in the lines without TEAD2 | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000197813, SLC6A16, FBXO17 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.614). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.0, -6.7); signed map (-43.2, 3.4). **Vector** length 109, 30.5% of its response variance represented; |z| ≥ 3 in 926 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +11.7 | +20.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.4 | +6.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.1 | +5.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.0 | +6.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +10.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.4 | +3.5 |
|  | [[Infigratinib (drug)]] 5 µM |  | +1.9 | +3.2 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.9 | +1.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -10.9 | -20.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -9.3 | -7.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -8.3 | -23.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.6 | -5.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.5 | -9.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.8 | -3.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.3 | -1.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.2 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | membrane bound acylglycerophosphatidylinositol O-acyltransferase MBOAT7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.42 — chr19:54,173,412-54,189,882 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BB1, hMBOA-7, LPLAT, LPIAT1, LPLAT11; previously LENG4 |
| Gene groups (HGNC) | Membrane bound O-acyltransferase family; Lysophospholipid acyltransferases |
| Reactome | 4 pathways, smallest: Acyl chain remodelling of PI; Glycerophospholipid biosynthesis; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96N66](https://www.uniprot.org/uniprotkb/Q96N66) (Membrane-bound acylglycerophosphatidylinositol O-acyltransferase MBOAT7):

> Acyltransferase which catalyzes the transfer of an acyl group from an acyl-CoA to a lysophosphatidylinositol (1-acylglycerophosphatidylinositol or LPI) leading to the production of a phosphatidylinositol (1,2-diacyl-sn-glycero-3-phosphoinositol or PI) and participates in the reacylation step of the phospholipid remodeling pathway also known as the Lands cycle. Prefers arachidonoyl-CoA as the acyl donor, thus contributing to the regulation of free levels arachidonic acid in cell. In liver, …

**Summary**, from NCBI Gene [79143](https://www.ncbi.nlm.nih.gov/gene/79143):

> This gene encodes a member of the membrane-bound O-acyltransferases family of integral membrane proteins that have acyltransferase activity. The encoded protein is a lysophosphatidylinositol acyltransferase that has specificity for arachidonoyl-CoA as an acyl donor. This protein is involved in the reacylation of phospholipids as part of the phospholipid remodeling pathway known as the Land cycle. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:15505](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15505) · Entrez [79143](https://www.ncbi.nlm.nih.gov/gene/79143) · UniProt [Q96N66](https://www.uniprot.org/uniprotkb/Q96N66) · Ensembl [ENSG00000125505](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125505)

## Data

Gene col 4626: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4626); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4626, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4626]; `tensor/DDL_lfc|DDL_z.npy` [4626]; `embed/gene_vectors.npy` [4626]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4626 or target_col == 4626). Every well: [[MBOAT7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MBOAT7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
