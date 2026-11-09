---
symbol: "BTN3A1"
type: "gene"
col: 375
ensembl_id: "ENSG00000026950"
name: "butyrophilin subfamily 3 member A1"
location: "6p22.2"
module: 70
arm: "+"
pooled_cpm: 21.71
n_lines_expressing: 49
n_dd_up: 20
n_dd_down: 56
n_dd_up_clean: 16
n_dd_down_clean: 36
in_vector_space: true
direction_upstream: 10
direction_downstream: 1
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# BTN3A1

*butyrophilin subfamily 3 member A1* — 6p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.15× (z +7.3, q 2e-10, up in 6 of 47 measured lines) ⚠ position not correctable. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 1.61× (z +7.0, q 9e-10, up in 27 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 56 drug-doses (20 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.308× (z -17.9, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BTN3A3]] (+0.74, fdr 7e-06, ⚠ same locus), [[BTN3A2]] (+0.73, fdr 7e-06, ⚠ same locus), [[TLR3]] (+0.68, fdr 7e-06), [[DHX58]] (+0.65, fdr 7e-06), [[PSMB8]] (+0.64, fdr 7e-06); moves opposite to [[ZBED4]] (-0.64, fdr 1e-05), [[TTL]] (-0.62, fdr 1e-05), [[GATAD2A]] (-0.61, fdr 1e-05).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[GBP4]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PSMB9]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 375.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +7.3 | 2e-10 | 6/47 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.61×** | +7.0 | 9e-10 | 27/46 (CFPAC-1, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.51×** | +6.1 | 2e-07 | 25/47 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.31×** | +5.3 | 2e-05 | 21/47 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.38×** | +5.2 | 2e-05 | 23/47 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.30×** | +5.1 | 3e-05 | 22/47 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.25×** | +4.8 | 1e-04 | 18/46 (HOP62, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 5 µM |  | **1.32×** | +4.7 | 2e-04 | 19/47 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.22×** | +4.2 | 0.001 | 20/47 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +4.1 | 0.003 | 19/47 (A-172, KATO III, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.30×** | +4.0 | 0.003 | 18/46 (MIA PaCa-2, NCI-H23, …) | rises with dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.30×** | +4.0 | 0.003 | 15/47 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.32×** | +4.0 | 0.003 | 14/47 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.31×** | +3.9 | 0.004 | 14/46 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.28×** | +3.8 | 0.006 | 17/47 (H4, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.029 | 6/47 (C32, AsPC-1, …) | top dose only | plate-row cell shift |
| [[Relugolix (drug)]] 5 µM |  | 1.16× | +3.3 | 0.029 | 4/47 (H4, J82, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 61 in all, 22 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 56 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 375.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.308×** | -17.9 | 0e+00 | 44/47 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.330×** | -16.9 | 0e+00 | 44/47 (KATO III, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.344×** | -16.2 | 0e+00 | 36/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.386×** | -14.5 | 3e-45 | 41/47 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.427×** | -12.9 | 3e-36 | 39/47 (COLO 205, H4, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.448×** | -12.2 | 3e-32 | 40/47 (HS-578T, COLO 205, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.463×** | -11.7 | 1e-29 | 39/47 (H4, COLO 205, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.438×** | -11.6 | 3e-29 | 25/33 (MIA PaCa-2, KATO III, …) | all doses, flat | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.466×** | -11.4 | 2e-28 | 42/47 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.461×** | -11.3 | 6e-28 | 32/43 (HS-578T, COLO 205, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.590×** | -11.3 | 6e-28 | 31/45 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.532×** | -9.6 | 4e-20 | 31/47 (SNU-423, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **0.563×** | -8.7 | 1e-16 | 27/40 (COLO 205, A498, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.358×** | -8.2 | 1e-14 | 32/47 (HS-578T, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.575×** | -8.1 | 3e-14 | 26/42 (SW1417, COLO 205, …) | top dose only | cell-cycle shift (explains ~22% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.591×** | -8.0 | 5e-14 | 31/47 (RPMI-7951, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.713×** | -7.2 | 2e-11 | 25/47 (H4, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.624×** | -7.2 | 3e-11 | 30/47 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.410×** | -7.1 | 4e-11 | 32/46 (SW 900, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.670×** | -6.1 | 3e-08 | 29/46 (H4, AN3 CA, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.467×** | -6.1 | 3e-08 | 27/46 (A498, A549, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.674×** | -6.0 | 5e-08 | 24/44 (COLO 205, A498, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.675×** | -5.9 | 5e-08 | 25/46 (SW480, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.497×** | -5.6 | 6e-07 | 25/45 (Panc 03.27, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.46 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 375. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 74.5 | 0 | 13 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -20.5) |
| [[KATO III (line)]] | alt | 30.4 | 0 | 9 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0699× (z -19.0) |
| [[H4 (line)]] | wt | 37.6 | 0 | 8 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0691× (z -15.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.101× (z -12.9) |
| [[NCI-H460 (line)]] | wt | 19.0 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -13.8) |
| [[PANC-1 (line)]] | alt | 16.8 | 0 | 8 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.163× (z -14.9) |
| [[A498 (line)]] | wt | 33.8 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -14.4) |
| [[HS-578T (line)]] | alt | 49.1 | 0 | 7 (6 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.124× (z -16.1) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.348× (z -8.5) |
| [[LoVo (line)]] | wt | 32.2 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.275× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 24.2 | 1 (1 ⚠) | 5 (3 ⚠) | [[Adagrasib (drug)]] 0.05 µM 2.15× (z +15.7) ⚠ position not correctable | [[Dinaciclib (drug)]] 0.05 µM 0.0527× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.171× (z -10.3) |
| [[SNU-423 (line)]] | alt | 42.0 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.188× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.252× (z -10.5) |
| [[SW1417 (line)]] | alt | 13.0 | 0 | 5 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0856× (z -13.6) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.203× (z -13.0) |
| [[SW480 (line)]] | alt | 15.3 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.212× (z -11.6) |
| [[NCI-H1573 (line)]] | alt | 17.2 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0735× (z -17.1) |
| [[RPMI-7951 (line)]] | alt | 44.3 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0639× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.215× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 35.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.274× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 19.7 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +8.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.228× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 29.2 | 0 | 3 | — | [[PH-797804 (drug)]] 5 µM 0.0241× (z -13.4) |
| [[SW48 (line)]] | wt | 17.9 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 5.58× (z +10.0) | [[Bendamustine (drug)]] 5 µM 0.0932× (z -9.4) |
| [[HCT15 (line)]] | alt | 23.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.130× (z -9.2) ⚠ toxic; transcription drop · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.144× (z -8.7) |
| [[Hs 766T (line)]] | wt | 26.3 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.196× (z -9.4) ⚠ unreliable plate only · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.216× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 18.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.93× (z +12.2) ⚠ position not correctable | [[Niclosamide (olamine) (drug)]] 5 µM 0.122× (z -10.5) ⚠ toxic |
| [[SW 900 (line)]] | alt | 19.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.162× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change · without an alert: [[EX229 (drug)]] 5 µM 0.0419× (z -9.8) |
| [[A-427 (line)]] | wt | 15.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.222× (z -9.3) |
| [[A549 (line)]] | wt | 15.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.108× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HOP62 (line)]] | alt | 10.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +12.5) | — |
| [[HT-29 (line)]] | alt | 14.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.146× (z -11.1) |
| [[J82 (line)]] | alt | 29.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +9.2) | — |
| [[LOX-IMVI (line)]] | wt | 9.08 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.137× (z -9.1) |
| [[SHP-77 (line)]] | alt | 8.69 | 0 | 1 | — | [[Alpelisib (drug)]] 0.05 µM 0.0877× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 16.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +10.5) | — |
| [[A-172 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.18 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.63 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.78 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 375), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTN3A3]] | +0.74 | +0.65 / +0.86 | both halves | 7e-06 | same gene group; pathway: Butyrophilin (BTN) family interactions; STRING 966; ⚠ same locus (25.3 kb, same strand: neighbours can correlate without regulation) |
| [[BTN3A2]] | +0.73 | +0.59 / +0.82 | both halves | 7e-06 | same gene group; pathway: Butyrophilin (BTN) family interactions; STRING 993; ⚠ same locus (23.9 kb, same strand: neighbours can correlate without regulation) |
| [[TLR3]] | +0.68 | +0.58 / +0.74 | both halves | 7e-06 | same gene group |
| [[DHX58]] | +0.65 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[PSMB8]] | +0.64 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[TRANK1]] | +0.64 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[TRAFD1]] | +0.63 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[GBP2]] | +0.63 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[TRIM5]] | +0.63 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[FAM111A-DT]] | +0.63 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[PAXIP1-AS2]] | +0.63 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[BTN2A2]] | +0.63 | +0.69 / +0.51 | both halves | 1e-05 | same gene group; pathway: Butyrophilin (BTN) family interactions; STRING 585; ⚠ same locus (7.4 kb, same strand: neighbours can correlate without regulation) |
| [[IFIH1]] | +0.62 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[GBP4]] | +0.62 | +0.47 / +0.72 | both halves | 2e-05 |  |
| [[PSMB9]] | +0.61 | +0.57 / +0.65 | both halves | 1e-05 | STRING 675 |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBED4]] | -0.64 | -0.69 / -0.53 | both halves | 1e-05 |  |
| [[TTL]] | -0.62 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[GATAD2A]] | -0.61 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[RAP1GDS1]] | -0.60 | -0.60 / -0.57 | both halves | 9e-06 |  |
| [[BCAR3]] | -0.59 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[CAP1]] | -0.57 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[LYPLA1]] | -0.56 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[PACS2]] | -0.55 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[FMNL2]] | -0.55 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[TEX2]] | -0.54 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[SEPTIN10]] | -0.54 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[SLC27A4]] | -0.54 | -0.55 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 5, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GBP4]] | B | GBP4 activity raises BTN3A1's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 1.82× lower at baseline in the lines without GBP4 | 0.019 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[GBP4]] | B | GBP4 activity strengthens BTN3A1's drug response | lines that do not express GBP4 (19) vs lines expressing it (28) | the lines without GBP4 respond 0.66× as strongly (z diff +1.69); strongest at Dinaciclib 0.05 µM: 0.63x vs 0.36x (z diff +3.1) | 0.034 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1; target measured in part of the lines; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity lowers BTN3A1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[GBP1]] | B | GBP1 activity raises BTN3A1's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 1.68× lower at baseline in the lines without GBP1 | 0.085 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[HLA-F]] | B | HLA-F activity raises BTN3A1's level | lines that do not express HLA-F (10) vs lines expressing it (40) | 1.89× lower at baseline in the lines without HLA-F | 0.095 | ⚠ within organs, on part of the lines; also absent: DUSP23, HLA-B, ENSG00000290574; maybe low, not absent |
| [[PSMB9]] | C | PSMB9's natural level strengthens BTN3A1's drug response | PSMB9's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.69, reverse +0.63; direction not clear | 0.027 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PSMB8]] | C | PSMB8's natural level strengthens BTN3A1's drug response | PSMB8's natural level across 43 lines (lineage-adjusted; a glimpse) | r +0.68, reverse +0.52; direction not clear | 0.060 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IRF1]] | C | IRF1's natural level strengthens BTN3A1's drug response | IRF1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.63, reverse -0.26; direction not clear | 0.080 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[NMI]] | C | NMI activity raises BTN3A1's level | lines that do not express NMI (4) vs lines expressing it (46) | 1.71× lower at baseline in the lines without NMI | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: NABP1, LGI4, C21orf91 |
| [[BTN2A2]] | C | BTN2A2 activity raises BTN3A1's level | lines that do not express BTN2A2 (3) vs lines expressing it (47) | 1.88× lower at baseline in the lines without BTN2A2 | 0.099 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DNAJC18, TBKBP1, TTC23L |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB9]] | C | BTN3A1's natural level strengthens PSMB9's drug response | BTN3A1's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.69; direction not clear | 0.089 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.672). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.5, 52.2); signed map (59.8, 30.0). **Vector** length 98.4, 27.4% of its response variance represented; |z| ≥ 3 in 1,536 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *allograft rejection* (hallmark, mean cos +0.51 to 11); *Non-canonical inflammasome activation* (reactome, mean cos +0.57 to 4); *Antigen processing: Ub, ATP-independent proteasomal degradation* (reactome, mean cos +0.53 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.3 | +4.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.0 | -6.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +4.7 | -8.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.7 | +7.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.6 | +5.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.3 | +4.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.1 | +3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.9 | +5.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.0 | -11.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.8 | -17.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.2 | -14.5 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -4.2 | -5.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.9 | -5.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.7 | -7.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.5 | -5.0 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.5 | -2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -9.6 |

## What is on record

|  |  |
|---|---|
| Name | butyrophilin subfamily 3 member A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.2 — chr6:26,402,237-26,415,208 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BT3.1, BTF5, CD277, BTN3.1 |
| Gene groups (HGNC) | Butyrophilins; CD molecules; V-set domain containing; C2-set domain containing |
| Reactome | 2 pathways, smallest: Butyrophilin (BTN) family interactions; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [O00481](https://www.uniprot.org/uniprotkb/O00481) (Butyrophilin subfamily 3 member A1):

> Plays a role in T-cell activation and in the adaptive immune response. Regulates the proliferation of activated T-cells. Regulates the release of cytokines and IFNG by activated T-cells. Mediates the response of T-cells toward infected and transformed cells that are characterized by high levels of phosphorylated metabolites, such as isopentenyl pyrophosphate.

**Summary**, from NCBI Gene [11119](https://www.ncbi.nlm.nih.gov/gene/11119):

> The butyrophilin (BTN) genes are a group of major histocompatibility complex (MHC)-associated genes that encode type I membrane proteins with 2 extracellular immunoglobulin (Ig) domains and an intracellular B30.2 (PRYSPRY) domain. Three subfamilies of human BTN genes are located in the MHC class I region: the single-copy BTN1A1 gene (MIM 601610) and the BTN2 (e.g., BTN2A1; MIM 613590) and BTN3 (e.g., BNT3A1) genes, which have undergone tandem duplication, resulting in 3 copies of each (summary …

**Accessions** — [HGNC:1138](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1138) · Entrez [11119](https://www.ncbi.nlm.nih.gov/gene/11119) · UniProt [O00481](https://www.uniprot.org/uniprotkb/O00481) · Ensembl [ENSG00000026950](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000026950)

## Data

Gene col 375: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 375); `tables/drug_effects.parquet` (85 rows, flagged included); `relations/gene_relations.parquet` (col_a == 375, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 375]; `tensor/DDL_lfc|DDL_z.npy` [375]; `embed/gene_vectors.npy` [375]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 375 or target_col == 375). Every well: [[BTN3A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BTN3A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
