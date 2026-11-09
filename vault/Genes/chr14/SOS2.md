---
symbol: "SOS2"
type: "gene"
col: 1972
ensembl_id: "ENSG00000100485"
name: "SOS Ras/Rho guanine nucleotide exchange factor 2"
location: "14q21.3"
module: 234
arm: "+"
pooled_cpm: 139.18
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 24
n_dd_up_clean: 4
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/234"]
generated_by: "tahoemap"
---

# SOS2

*SOS Ras/Rho guanine nucleotide exchange factor 2* — 14q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 1.30× (z +5.3, q 6e-05, up in 28 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.380× (z -20.3, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HERPUD2]] (+0.67, fdr 7e-06), [[CDK13]] (+0.60, fdr 1e-05), [[USP34-DT]] (+0.59, fdr 4e-05); moves opposite to [[NEK6]] (-0.58, fdr 3e-05), [[STXBP6]] (-0.55, fdr 1e-05), [[FAT1]] (-0.54, fdr 1e-05).
> It is in [[Module 234]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1972.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +5.3 | 6e-05 | 28/48 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.59×** | +4.9 | 2e-04 | 32/49 (LoVo, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.27×** | +4.9 | 2e-04 | 30/47 (COLO 205, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | 1.15× | +4.2 | 0.004 | 20/48 (SNU-1, NCI-H2030, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.22×** | +4.1 | 0.005 | 24/47 (NCI-H23, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Artesunate (drug)]] 0.5 µM |  | **1.20×** | +3.9 | 0.009 | 24/48 (HEC-1-A, SNU-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.8 | 0.010 | 19/49 (NCI-H460, HepG2/C3A, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.19× | +3.6 | 0.022 | 20/47 (HEC-1-A, SNU-1, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +3.6 | 0.022 | 15/49 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.17× | +3.4 | 0.040 | 19/48 (NCI-H2030, KATO III, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.12× | +3.3 | 0.057 | 3/48 (AsPC-1, NCI-H1573, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.11× | +3.2 | 0.071 | 7/48 (NCI-H2030, A-427, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.1 | 0.080 | 18/50 (NCI-H460, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 14 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1972.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.380×** | -20.3 | 0e+00 | 48/48 (BT-474, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.373×** | -19.8 | 0e+00 | 43/44 (NCI-H1573, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.401×** | -19.1 | 0e+00 | 48/48 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.427×** | -17.8 | 0e+00 | 48/49 (NCI-H1792, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.472×** | -15.7 | 0e+00 | 47/48 (NCI-H1792, BT-474, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.494×** | -13.6 | 2e-40 | 39/45 (HEC-1-A, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.541×** | -12.3 | 4e-33 | 40/48 (A-172, A498, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.596×** | -10.8 | 2e-25 | 43/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.657×** | -8.8 | 1e-16 | 40/48 (NCI-H1792, SW1417, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.663×** | -8.6 | 5e-16 | 40/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.751×** | -8.4 | 2e-15 | 28/48 (A-172, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.728×** | -6.6 | 2e-09 | 30/48 (PANC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.734×** | -6.5 | 5e-09 | 34/48 (SHP-77, NCI-H1792, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.746×** | -6.1 | 4e-08 | 27/48 (A-172, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~53% of this change | **0.756×** | -5.8 | 2e-07 | 32/48 (SW 900, SW 1271, …) | inconsistent across doses | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.611×** | -5.2 | 6e-06 | 31/48 (AsPC-1, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.611×** | -5.2 | 6e-06 | 34/48 (AsPC-1, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.856× | -4.6 | 1e-04 | 20/48 (NCI-H2347, SHP-77, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.796×** | -4.6 | 1e-04 | 27/48 (NCI-H1792, NCI-H2347, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.806×** | -4.5 | 2e-04 | 27/48 (BT-474, SW 1271, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.796×** | -4.4 | 3e-04 | 31/47 (NCI-H460, SW48, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.662×** | -4.4 | 3e-04 | 31/48 (AsPC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.688×** | -4.0 | 0.002 | 26/48 (AsPC-1, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.725×** | -3.4 | 0.013 | 24/48 (AsPC-1, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.850× | -3.4 | 0.015 | 21/48 (CFPAC-1, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1972. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 270 | 0 | 14 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -22.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.223× (z -18.0) |
| [[NCI-H460 (line)]] | wt | 116 | 3 (2 ⚠) | 10 (6 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.381× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.450× (z -11.6) |
| [[A549 (line)]] | wt | 201 | 0 | 11 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.183× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.261× (z -14.8) |
| [[A-172 (line)]] | wt | 86.5 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -24.8) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.223× (z -19.7) |
| [[A498 (line)]] | wt | 86.7 | 1 (1 ⚠) | 9 (7 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.56× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.335× (z -15.4) |
| [[BT-474 (line)]] | alt | 307 | 0 | 10 (8 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.142× (z -20.5) |
| [[CFPAC-1 (line)]] | alt | 168 | 0 | 10 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.351× (z -13.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.381× (z -12.0) |
| [[PANC-1 (line)]] | alt | 129 | 0 | 10 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.343× (z -16.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.356× (z -15.6) |
| [[NCI-H2347 (line)]] | alt | 158 | 0 | 9 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.325× (z -16.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.405× (z -13.0) |
| [[SNU-423 (line)]] | alt | 134 | 0 | 9 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.282× (z -14.0) |
| [[AsPC-1 (line)]] | alt | 177 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.268× (z -15.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.305× (z -13.7) |
| [[HOP62 (line)]] | alt | 124 | 2 (1 ⚠) | 6 (5 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.341× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.371× (z -13.7) |
| [[J82 (line)]] | alt | 106 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.369× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.418× (z -11.8) |
| [[NCI-H23 (line)]] | alt | 189 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -15.4) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.370× (z -10.7) |
| [[SW 900 (line)]] | alt | 150 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.406× (z -11.2) |
| [[LS 180 (line)]] | wt | 164 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.244× (z -13.4) |
| [[MIA PaCa-2 (line)]] | alt | 240 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.210× (z -20.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.232× (z -18.9) |
| [[SW1417 (line)]] | alt | 122 | 0 | 6 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.394× (z -11.7) ⚠ unreliable plate only · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.474× (z -9.4) |
| [[SW480 (line)]] | alt | 112 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.280× (z -19.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.319× (z -17.0) |
| [[Hs 766T (line)]] | wt | 122 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.255× (z -15.2) |
| [[HS-578T (line)]] | alt | 79.1 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.221× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.346× (z -12.2) |
| [[HT-29 (line)]] | alt | 95.7 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.266× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.281× (z -14.2) |
| [[hTERT-HPNE (line)]] | wt | 113 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.171× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.410× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 252 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.260× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.456× (z -10.7) |
| [[Panc 03.27 (line)]] | alt | 151 | 0 | 5 (4 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.105× (z -14.7) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.368× (z -12.8) |
| [[SHP-77 (line)]] | alt | 128 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.349× (z -13.7) |
| [[A-427 (line)]] | wt | 115 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.265× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.511× (z -8.7) |
| [[C32 (line)]] | wt | 157 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.357× (z -10.9) |
| [[HepG2_C3A (line)]] | wt | 107 | 1 (1 ⚠) | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.385× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.405× (z -9.3) |
| [[KATO III (line)]] | alt | 103 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.321× (z -12.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.341× (z -11.8) |
| [[LoVo (line)]] | wt | 120 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.313× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.378× (z -10.5) |
| [[LOX-IMVI (line)]] | wt | 93.4 | 1 | 3 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.472× (z -10.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.489× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 146 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -20.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.470× (z -8.5) |
| [[SNU-1 (line)]] | wt | 136 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -19.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.365× (z -9.7) |
| [[COLO 205 (line)]] | alt | 114 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.285× (z -11.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.386× (z -9.0) |
| [[H4 (line)]] | wt | 119 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.224× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.367× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 123 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.301× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.511× (z -10.2) |
| [[RKO (line)]] | wt | 164 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.301× (z -13.7) |
| [[RPMI-7951 (line)]] | alt | 105 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.371× (z -10.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.426× (z -9.0) |
| [[AN3 CA (line)]] | alt | 163 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.232× (z -11.2) |
| [[SW 1271 (line)]] | alt | 203 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.237× (z -9.3) |
| [[SW48 (line)]] | wt | 130 | 1 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.96× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.196× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[C-33 A (line)]] | alt | 131 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.366× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[SK-MEL-2 (line)]] | alt | 101 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.354× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[CHP-212 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 109 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1972), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HERPUD2]] | +0.67 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[CDK13]] | +0.60 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[USP34-DT]] | +0.59 | +0.40 / +0.61 | both halves | 4e-05 |  |
| [[PPM1B]] | +0.59 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[TPTEP2-CSNK1E]] | +0.59 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[WDR20]] | +0.58 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[PPP2CB]] | +0.58 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[KPNB1-DT]] | +0.58 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[KIAA2026]] | +0.57 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[PIK3CA]] | +0.56 | +0.52 / +0.51 | both halves | 1e-05 | pathway: Interleukin-2 family signaling; STRING 860 |
| [[LINC00685]] | +0.56 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[CDC37L1]] | +0.56 | +0.32 / +0.53 | both halves | 2e-04 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEK6]] | -0.58 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[STXBP6]] | -0.55 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[FAT1]] | -0.54 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[PFAS]] | -0.54 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[G3BP1]] | -0.52 | -0.40 / -0.56 | both halves | 4e-05 |  |
| [[RUVBL1]] | -0.52 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[BMS1]] | -0.51 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[TTC5]] | -0.51 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[FARSB]] | -0.51 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[THEM6]] | -0.51 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[FIGNL1]] | -0.50 | -0.36 / -0.49 | both halves | 1e-04 |  |
| [[PFKM]] | -0.49 | -0.41 / -0.53 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 234]]; 5 genes; every member is in the + arm (projection on the module's main direction 0.778). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-12.0, -19.1); signed map (4.8, 1.9). **Vector** length 118, 41.2% of its response variance represented; |z| ≥ 3 in 1,533 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +12.0 | +3.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +11.4 | +5.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +9.2 | +3.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.4 | +3.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +4.3 | +3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.2 | +3.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.7 | +4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | -2.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -7.0 | -10.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.4 | -6.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.3 | -8.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.8 | -4.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.9 | -5.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.4 | -2.3 |
|  | [[EX229 (drug)]] 5 µM |  | -3.1 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | SOS Ras/Rho guanine nucleotide exchange factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q21.3 — chr14:50,117,130-50,231,578 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Dbl family Rho GEFs |
| Reactome | 19 pathways, smallest: Activation of RAC1; Interleukin-15 signaling; Interleukin-2 family signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q07890](https://www.uniprot.org/uniprotkb/Q07890) (Son of sevenless homolog 2):

> Acts as guanine nucleotide exchange factor (GEF) for RAS proteins. Catalyzes the GDP-to-GTP exchange, resulting in an increase of the active GTP-bound form of HRAS. Acts as a key modulator of PI3K-AKT signaling.

**Summary**, from NCBI Gene [6655](https://www.ncbi.nlm.nih.gov/gene/6655):

> This gene encodes a regulatory protein that is involved in the positive regulation of ras proteins. Mutations in this gene are associated with Noonan Syndrome-9. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:11188](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11188) · Entrez [6655](https://www.ncbi.nlm.nih.gov/gene/6655) · UniProt [Q07890](https://www.uniprot.org/uniprotkb/Q07890) · Ensembl [ENSG00000100485](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100485)

## Data

Gene col 1972: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1972); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1972, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1972]; `tensor/DDL_lfc|DDL_z.npy` [1972]; `embed/gene_vectors.npy` [1972]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1972 or target_col == 1972). Every well: [[SOS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SOS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
