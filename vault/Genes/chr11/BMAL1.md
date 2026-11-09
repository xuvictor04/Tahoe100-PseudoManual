---
symbol: "BMAL1"
type: "gene"
col: 5475
ensembl_id: "ENSG00000133794"
name: "basic helix-loop-helix ARNT like 1"
location: "11p15.3"
module: 33
arm: "-"
pooled_cpm: 25.11
n_lines_expressing: 49
n_dd_up: 24
n_dd_down: 9
n_dd_up_clean: 23
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# BMAL1

*basic helix-loop-helix ARNT like 1* — 11p15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.09× (z +26.7, q 0e+00, up in 43 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.646× (z -6.7, q 6e-09, down in 24 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.800× (z -5.3, q 2e-05, down in 23 of 47 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SHOC2]] (+0.58, fdr 1e-05), [[KIF13B]] (+0.54, fdr 9e-05), [[DNAJB5]] (+0.52, fdr 4e-05); moves opposite to [[ANAPC10]] (-0.54, fdr 1e-05), [[SUPV3L1]] (-0.54, fdr 2e-05), [[QTRT2]] (-0.54, fdr 8e-05).
> It sits in the **-** arm of [[Module 033]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5475.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.09×** | +26.7 | 0e+00 | 43/46 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.43×** | +20.6 | 0e+00 | 45/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.09×** | +18.8 | 0e+00 | 46/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.64×** | +16.2 | 0e+00 | 46/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.40×** | +14.0 | 1e-42 | 39/46 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +13.3 | 3e-38 | 34/44 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.07×** | +12.2 | 4e-32 | 37/45 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.99×** | +11.5 | 1e-28 | 33/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.58×** | +10.8 | 2e-25 | 38/47 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.69×** | +8.8 | 1e-16 | 35/47 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.54×** | +7.2 | 4e-11 | 30/46 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.18×** | +6.8 | 5e-10 | 32/47 (SW480, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.50×** | +6.8 | 5e-10 | 25/47 (NCI-H460, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.48×** | +6.6 | 2e-09 | 28/46 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +6.1 | 4e-08 | 23/45 (NCI-H460, SW480, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.34×** | +4.9 | 4e-05 | 17/46 (LS 180, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5475.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.646×** | -6.7 | 6e-09 | 24/36 (Panc 03.27, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.670×** | -6.7 | 6e-09 | 25/40 (NCI-H460, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.704×** | -5.6 | 3e-06 | 17/32 (LoVo, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.800×** | -5.3 | 2e-05 | 23/47 (C32, NCI-H1792, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.774×** | -4.3 | 0.002 | 19/47 (SNU-1, HT-29, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.804×** | -3.7 | 0.023 | 15/45 (NCI-H1792, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.805×** | -3.6 | 0.023 | 17/44 (SW480, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Flutamide (drug)]] 5 µM |  | **0.821×** | -3.3 | 0.066 | 6/46 (A498, RPMI-7951, …) | top dose only |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.766×** | -3.2 | 0.094 | 9/47 (NCI-H661, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5475. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 25.9 | 13 (3 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.71× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -12.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 28.9 | 11 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +20.8) | — |
| [[HOP62 (line)]] | alt | 23.8 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +11.1) | — |
| [[A498 (line)]] | wt | 30.4 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +18.7) | — |
| [[AsPC-1 (line)]] | alt | 27.3 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +17.2) | [[Dinaciclib (drug)]] 5 µM 0.265× (z -9.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 31.4 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +14.8) | [[Lonafarnib (drug)]] 5 µM 0.0608× (z -11.7) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 17.3 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.181× (z -11.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 13.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +14.5) | — |
| [[BT-474 (line)]] | alt | 10.1 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.70× (z +11.1) | [[Decitabine (drug)]] 0.05 µM 0.0963× (z -9.8) |
| [[Hs 766T (line)]] | wt | 32.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +10.6) | — |
| [[HT-29 (line)]] | alt | 42.2 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.290× (z -9.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 28.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.101× (z -16.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 12.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.35× (z +12.2) | — |
| [[NCI-H2347 (line)]] | alt | 19.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +17.5) | — |
| [[Panc 03.27 (line)]] | alt | 31.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.26× (z +15.0) | [[Dinaciclib (drug)]] 0.05 µM 0.113× (z -12.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 24.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +11.8) | — |
| [[A-172 (line)]] | wt | 30.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +14.7) | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -10.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 22.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.68× (z +15.2) | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0919× (z -8.7) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 9.06 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +11.8) | [[Radotinib (drug)]] 0.5 µM 0.121× (z -11.8) |
| [[H4 (line)]] | wt | 16.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +9.4) | — |
| [[J82 (line)]] | alt | 51.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +12.9) | — |
| [[LOX-IMVI (line)]] | wt | 17.9 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.12× (z +9.1) | — |
| [[SHP-77 (line)]] | alt | 22.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.141× (z -11.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 28.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.167× (z -10.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 22.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +9.8) | — |
| [[C32 (line)]] | wt | 22.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +9.8) | — |
| [[HepG2_C3A (line)]] | wt | 34.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -12.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 25.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.236× (z -9.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 35.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.127× (z -11.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 74.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -13.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 33.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +12.8) | — |
| [[RPMI-7951 (line)]] | alt | 22.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.170× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 11.0 | 0 | 1 | — | [[Almonertinib (hydrochloride) (drug)]] 0.5 µM 0.0734× (z -10.1) |
| [[SW 1271 (line)]] | alt | 60.4 | 0 | 1 | — | [[Bestatin (hydrochloride) (drug)]] 0.05 µM 0.0627× (z -9.4) |
| [[AN3 CA (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.92 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.28 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.00 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 37.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5475), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*42 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHOC2]] | +0.58 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[KIF13B]] | +0.54 | +0.37 / +0.61 | both halves | 9e-05 |  |
| [[DNAJB5]] | +0.52 | +0.40 / +0.57 | both halves | 4e-05 |  |
| [[PDLIM3]] | +0.51 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[PNRC1]] | +0.51 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[CDKN1C]] | +0.51 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[SMIM14]] | +0.50 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[GPX4]] | +0.49 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[PPARG]] | +0.48 | +0.30 / +0.51 | both halves | 2e-04 | pathway: PPARA activates gene expression; STRING 590 |
| [[NCOA3]] | +0.48 | +0.36 / +0.48 | both halves | 9e-05 | same gene group; pathway: PPARA activates gene expression |
| [[LINC00598]] | +0.48 | +0.39 / +0.49 | both halves | 6e-05 |  |
| [[CAMTA1]] | +0.48 | +0.19 / +0.56 | ⚠ one half (not replicated) | 9e-04 |  |
| [[SH3GL2]] | +0.47 | +0.43 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*58 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANAPC10]] | -0.54 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[SUPV3L1]] | -0.54 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[QTRT2]] | -0.54 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[IPO11]] | -0.53 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[DNAAF5]] | -0.52 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[SAMM50]] | -0.52 | -0.43 / -0.50 | both halves | 4e-05 |  |
| [[MAFIP]] | -0.52 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[NOL10]] | -0.51 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[CDC123]] | -0.51 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[TIMM23]] | -0.51 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[ANAPC1]] | -0.50 | -0.24 / -0.54 | both halves | 5e-04 |  |
| [[ERCC3]] | -0.50 | -0.44 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **-** arm (projection on the module's main direction -0.428). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-13.0, -13.0); signed map (-2.9, 22.0). **Vector** length 76.5, 16.2% of its response variance represented; |z| ≥ 3 in 1,280 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +10.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.9 | +14.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.4 | +7.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.4 | +11.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.3 | +26.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.1 | +2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +6.8 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | +1.8 | +0.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +1.6 | +3.7 |
| fall | [[Selinexor (drug)]] 5 µM |  | -5.8 | -5.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.1 | -2.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -0.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.4 | +0.5 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -3.3 | -1.0 |
|  | [[EX229 (drug)]] 5 µM |  | -3.1 | -2.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.0 | -2.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.8 | -2.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | basic helix-loop-helix ARNT like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.3 — chr11:13,276,652-13,387,266 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MOP3, JAP3, PASD3, bHLHe5, ARNTL1; previously ARNTL |
| Gene groups (HGNC) | Basic helix-loop-helix proteins; PAS domain containing |
| Reactome | 17 pathways, smallest: Phosphorylation and nuclear translocation of BMAL1 (ARNTL) and CLOCK; Phosphorylation of CLOCK, acetylation of BMAL1 (ARNTL) at target gene promoters; The CRY:PER:kinase complex represses transactivation by the BMAL:CLOCK (ARNTL:CLOCK) complex |
| Matched by | ensembl_id |

**Function**, from UniProt [O00327](https://www.uniprot.org/uniprotkb/O00327) (Basic helix-loop-helix ARNT-like protein 1):

> Transcriptional activator which forms a core component of the circadian clock. The circadian clock, an internal time-keeping system, regulates various physiological processes through the generation of approximately 24 hour circadian rhythms in gene expression, which are translated into rhythms in metabolism and behavior. It is derived from the Latin roots 'circa' (about) and 'diem' (day) and acts as an important regulator of a wide array of physiological functions including metabolism, sleep, …

**Summary**, from NCBI Gene [406](https://www.ncbi.nlm.nih.gov/gene/406):

> The protein encoded by this gene is a basic helix-loop-helix protein that forms a heterodimer with CLOCK. This heterodimer binds E-box enhancer elements upstream of Period (PER1, PER2, PER3) and Cryptochrome (CRY1, CRY2) genes and activates transcription of these genes. PER and CRY proteins heterodimerize and repress their own transcription by interacting in a feedback loop with CLOCK/ARNTL complexes. Defects in this gene have been linked to infertility, problems with gluconeogenesis and …

**Accessions** — [HGNC:701](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:701) · Entrez [406](https://www.ncbi.nlm.nih.gov/gene/406) · UniProt [O00327](https://www.uniprot.org/uniprotkb/O00327) · Ensembl [ENSG00000133794](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133794)

## Data

Gene col 5475: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5475); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5475, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5475]; `tensor/DDL_lfc|DDL_z.npy` [5475]; `embed/gene_vectors.npy` [5475]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5475 or target_col == 5475). Every well: [[BMAL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BMAL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
