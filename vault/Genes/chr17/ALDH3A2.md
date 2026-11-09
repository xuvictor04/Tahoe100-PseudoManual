---
symbol: "ALDH3A2"
type: "gene"
col: 1013
ensembl_id: "ENSG00000072210"
name: "aldehyde dehydrogenase 3 family member A2"
location: "17p11.2"
module: 35
arm: "-"
pooled_cpm: 46.81
n_lines_expressing: 48
n_dd_up: 20
n_dd_down: 3
n_dd_up_clean: 15
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# ALDH3A2

*aldehyde dehydrogenase 3 family member A2* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.62× (z +20.3, q 0e+00, up in 43 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.802× (z -4.9, q 5e-04, down in 23 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 9 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (SNU-1 0.135×, NCI-H23 0.376×, LS 180 0.524×, SK-MEL-2 0.477×, …); [[Dinaciclib (drug)]] 5 µM in 1 line (C-33 A 0.183×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change); [[Selinexor (drug)]] 5 µM in 1 line (MIA PaCa-2 0.321×; ⚠ cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 1 line (SK-MEL-2 0.379×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GDE1]] (+0.65, fdr 6e-05), [[PPP1CC]] (+0.63, fdr 1e-05), [[CLSTN1]] (+0.62, fdr 7e-05); moves opposite to [[UBE2CP5]] (-0.62, fdr 1e-05), [[NOXRED1]] (-0.61, fdr 4e-05), [[ACTR3-AS1]] (-0.60, fdr 4e-05).
> It sits in the **-** arm of [[Module 035]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1013.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.62×** | +20.3 | 0e+00 | 43/46 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.42×** | +19.4 | 0e+00 | 45/46 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.52×** | +14.6 | 1e-45 | 43/46 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.03×** | +11.2 | 6e-27 | 43/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.93×** | +10.4 | 4e-23 | 28/44 (A549, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.52×** | +9.3 | 1e-18 | 40/46 (HepG2/C3A, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.76×** | +8.6 | 5e-16 | 29/39 (A549, A498, …) | all doses, stronger at high dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.05×** | +5.9 | 2e-07 | 34/47 (AsPC-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +5.8 | 5e-07 | 27/46 (A498, LS 180, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +5.4 | 3e-06 | 25/45 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **1.42×** | +5.1 | 2e-05 | 19/41 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.37×** | +4.9 | 4e-05 | 24/46 (Hs 766T, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.44×** | +4.5 | 2e-04 | 24/46 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.22×** | +4.4 | 5e-04 | 20/46 (SW480, AsPC-1, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.31×** | +4.2 | 1e-03 | 15/47 (PANC-1, HOP62, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.27×** | +3.7 | 0.007 | 19/46 (PANC-1, J82, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.53×** | +3.5 | 0.015 | 13/45 (SW480, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **1.21×** | +2.9 | 0.097 | 9/45 (RKO, AN3 CA, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1013.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 9 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (SNU-1 0.135×, NCI-H23 0.376×, LS 180 0.524×, SK-MEL-2 0.477×, …); [[Dinaciclib (drug)]] 5 µM in 1 line (C-33 A 0.183×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change); [[Selinexor (drug)]] 5 µM in 1 line (MIA PaCa-2 0.321×; ⚠ cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 1 line (SK-MEL-2 0.379×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.802×** | -4.9 | 5e-04 | 23/46 (SNU-1, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.813×** | -4.6 | 0.001 | 23/47 (A498, MIA PaCa-2, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.787×** | -3.8 | 0.030 | 20/46 (PANC-1, C32, …) | inconsistent across doses |  |
| [[Tadalafil (drug)]] 5 µM |  | 0.812× | -3.2 | 0.22 | 10/45 (A-172, SW480, …) | top dose only | position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.821× | -3.1 | 0.22 | 15/46 (NCI-H23, A498, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.816× | -3.0 | 0.23 | 18/46 (A498, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1013. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 330 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -21.3) |
| [[SW480 (line)]] | alt | 34.6 | 8 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.81× (z +16.4) | — |
| [[SK-MEL-2 (line)]] | alt | 85.1 | 5 | 2 | [[Panobinostat (drug)]] 5 µM 5.26× (z +15.9) | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -10.1) |
| [[A549 (line)]] | wt | 55.7 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.44× (z +12.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 36.2 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.12× (z +13.2) | [[Selinexor (drug)]] 5 µM 0.321× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 68.3 | 4 | 1 | [[Panobinostat (drug)]] 0.5 µM 3.78× (z +13.9) | [[Homoharringtonine (drug)]] 5 µM 0.532× (z -9.4) |
| [[HOP62 (line)]] | alt | 22.9 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 7.58× (z +13.0) | — |
| [[HepG2_C3A (line)]] | wt | 54.2 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 3.33× (z +12.0) | — |
| [[HS-578T (line)]] | alt | 21.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.17× (z +10.8) | — |
| [[LOX-IMVI (line)]] | wt | 17.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 8.41× (z +12.7) | — |
| [[NCI-H23 (line)]] | alt | 48.3 | 2 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.91× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -11.8) |
| [[PANC-1 (line)]] | alt | 25.2 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.72× (z +12.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.382× (z -9.0) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 27.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.21× (z +9.5) | — |
| [[A-172 (line)]] | wt | 34.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.19× (z +10.7) | — |
| [[A-427 (line)]] | wt | 45.5 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.52× (z +8.5) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 40.7 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.43× (z +10.6) | — |
| [[AsPC-1 (line)]] | alt | 37.9 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.59× (z +11.6) | — |
| [[HEC-1-A (line)]] | alt | 69.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.14× (z +9.6) | — |
| [[J82 (line)]] | alt | 29.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.40× (z +10.8) | — |
| [[LoVo (line)]] | wt | 35.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.63× (z +11.0) | — |
| [[NCI-H2030 (line)]] | alt | 46.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.03× (z +10.2) | — |
| [[NCI-H2347 (line)]] | alt | 19.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.62× (z +10.6) | — |
| [[SHP-77 (line)]] | alt | 119 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.57× (z +10.1) | — |
| [[SNU-423 (line)]] | alt | 15.9 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.62× (z +9.0) | — |
| [[SW1417 (line)]] | alt | 18.4 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.50× (z +10.5) | — |
| [[C-33 A (line)]] | alt | 69.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.183× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[LS 180 (line)]] | wt | 160 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.524× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 12.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.48× (z +9.8) | — |
| [[AN3 CA (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.2 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.1 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 86.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 66.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1013), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GDE1]] | +0.65 | +0.38 / +0.68 | both halves | 6e-05 |  |
| [[PPP1CC]] | +0.63 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[CLSTN1]] | +0.62 | +0.38 / +0.53 | both halves | 7e-05 |  |
| [[PDHB]] | +0.61 | +0.43 / +0.53 | both halves | 3e-05 | pathway: HALLMARK_FATTY_ACID_METABOLISM |
| [[ABCD3]] | +0.60 | +0.46 / +0.60 | both halves | 3e-05 | pathway: Class I peroxisomal membrane protein import; STRING 551 |
| [[HLTF]] | +0.59 | +0.28 / +0.63 | both halves | 3e-04 |  |
| [[PRKAR2B]] | +0.58 | +0.42 / +0.57 | both halves | 4e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |
| [[SSX2IP]] | +0.58 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[ATP8A1]] | +0.55 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[NDRG3]] | +0.55 | +0.32 / +0.51 | both halves | 2e-04 |  |
| [[BTBD3]] | +0.54 | +0.32 / +0.45 | both halves | 2e-04 |  |
| [[C1GALT1C1]] | +0.54 | +0.42 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2CP5]] | -0.62 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[NOXRED1]] | -0.61 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[ACTR3-AS1]] | -0.60 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[LINC01772]] | -0.59 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[RECQL5]] | -0.58 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[GSK3B-DT]] | -0.57 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[ZNF621]] | -0.56 | -0.31 / -0.53 | both halves | 2e-04 |  |
| [[ZNF547]] | -0.55 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[TAS2R4]] | -0.55 | -0.36 / -0.32 | both halves | 2e-04 |  |
| [[ZNF778]] | -0.53 | -0.26 / -0.50 | both halves | 3e-04 |  |
| [[TRIM39]] | -0.53 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[LINC02936]] | -0.53 | -0.38 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **-** arm (projection on the module's main direction -0.473). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (23.8, -13.2); signed map (-31.7, -36.0). **Vector** length 96.8, 24.2% of its response variance represented; |z| ≥ 3 in 1,040 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.0 | +9.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.0 | +4.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.4 | +19.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.4 | +11.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.8 | +20.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.6 | +5.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +4.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.6 | +4.4 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +2.2 | +2.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -8.0 | -2.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.3 | -4.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | +2.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.6 | -0.7 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -3.3 | -2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.1 | -4.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.0 | -2.4 |
|  | [[EX229 (drug)]] 5 µM |  | -2.9 | -2.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.6 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | aldehyde dehydrogenase 3 family member A2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p11.2 — chr17:19,648,136-19,685,760 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FALDH; previously SLS, ALDH10 |
| Gene groups (HGNC) | Aldehyde dehydrogenases |
| Hallmark sets | FATTY_ACID_METABOLISM, ESTROGEN_RESPONSE_LATE |
| Reactome | 14 pathways, smallest: Alpha-oxidation of phytanate; Sphingolipid catabolism; Class I peroxisomal membrane protein import |
| Matched by | ensembl_id |

**Function**, from UniProt [P51648](https://www.uniprot.org/uniprotkb/P51648) (Aldehyde dehydrogenase family 3 member A2):

> Catalyzes the oxidation of medium and long chain aliphatic aldehydes to fatty acids. Active on a variety of saturated and unsaturated aliphatic aldehydes between 6 and 24 carbons in length. Responsible for conversion of the sphingosine 1-phosphate (S1P) degradation product hexadecenal to hexadecenoic acid.

**Summary**, from NCBI Gene [224](https://www.ncbi.nlm.nih.gov/gene/224):

> Aldehyde dehydrogenase isozymes are thought to play a major role in the detoxification of aldehydes generated by alcohol metabolism and lipid peroxidation. This gene product catalyzes the oxidation of long-chain aliphatic aldehydes to fatty acid. Mutations in the gene cause Sjogren-Larsson syndrome. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:403](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:403) · Entrez [224](https://www.ncbi.nlm.nih.gov/gene/224) · UniProt [P51648](https://www.uniprot.org/uniprotkb/P51648) · Ensembl [ENSG00000072210](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000072210)

## Data

Gene col 1013: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1013); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1013, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1013]; `tensor/DDL_lfc|DDL_z.npy` [1013]; `embed/gene_vectors.npy` [1013]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1013 or target_col == 1013). Every well: [[ALDH3A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALDH3A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
