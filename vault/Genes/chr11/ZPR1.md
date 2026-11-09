---
symbol: "ZPR1"
type: "gene"
col: 3092
ensembl_id: "ENSG00000109917"
name: "ZPR1 zinc finger"
location: "11q23.3"
module: 1
arm: "+"
pooled_cpm: 26.22
n_lines_expressing: 50
n_dd_up: 39
n_dd_down: 9
n_dd_up_clean: 22
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# ZPR1

*ZPR1 zinc finger* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (17 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.16× (z +12.5, q 4e-33, up in 41 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.98× (z +11.1, q 5e-26, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.668× (z -6.3, q 1e-07, down in 22 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMYD5]] (+0.76, fdr 7e-06), [[ZNF202]] (+0.70, fdr 7e-06), [[DHX37]] (+0.70, fdr 7e-06); moves opposite to [[MTF2]] (-0.60, fdr 1e-05), [[LCORL]] (-0.59, fdr 1e-05), [[STK38]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 18 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3092.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.16×** | +12.5 | 4e-33 | 41/44 (PANC-1, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.98×** | +11.1 | 5e-26 | 40/47 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.02×** | +11.0 | 7e-26 | 25/32 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.86×** | +10.0 | 2e-21 | 42/47 (NCI-H1792, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +7.9 | 2e-13 | 31/45 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.39×** | +7.6 | 3e-12 | 30/47 (LS 180, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.58×** | +7.4 | 8e-12 | 34/47 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.62×** | +7.2 | 3e-11 | 23/38 (SW480, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **2.31×** | +7.1 | 7e-11 | 35/47 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.52×** | +6.8 | 5e-10 | 36/48 (HT-29, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.49×** | +6.2 | 3e-08 | 28/48 (SW 900, NCI-H1573, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.53×** | +6.1 | 6e-08 | 27/48 (KATO III, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.45×** | +6.0 | 7e-08 | 28/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.42×** | +5.7 | 6e-07 | 23/46 (NCI-H460, SW480, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.28×** | +5.6 | 7e-07 | 21/47 (NCI-H1792, NCI-H2347, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.82×** | +5.1 | 1e-05 | 27/46 (PANC-1, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.79×** | +4.9 | 2e-05 | 22/47 (HEC-1-A, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **1.38×** | +4.7 | 8e-05 | 19/48 (PANC-1, LoVo, …) | all doses, flat |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.69×** | +4.5 | 2e-04 | 16/46 (PANC-1, SW1417, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.32×** | +4.5 | 2e-04 | 19/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.47×** | +4.4 | 2e-04 | 18/48 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +4.4 | 2e-04 | 16/48 (BT-474, HOP62, …) | top dose only | position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **1.66×** | +4.3 | 4e-04 | 17/45 (PANC-1, NCI-H2030, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.45×** | +4.3 | 4e-04 | 22/48 (PANC-1, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3092.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.668×** | -6.3 | 1e-07 | 22/46 (AsPC-1, LoVo, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.815×** | -4.7 | 6e-04 | 21/48 (COLO 205, CHP-212, …) | all doses, stronger at high dose | position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.753×** | -4.6 | 6e-04 | 21/48 (NCI-H2347, SW 1271, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.770×** | -4.3 | 0.003 | 15/47 (LoVo, AsPC-1, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.789×** | -3.9 | 0.011 | 15/48 (PANC-1, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.791×** | -3.9 | 0.011 | 16/47 (J82, PANC-1, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.844× | -3.8 | 0.011 | 19/48 (SW480, AsPC-1, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.798×** | -3.7 | 0.015 | 15/48 (RKO, LoVo, …) | top dose only | position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.791×** | -3.6 | 0.017 | 16/48 (LoVo, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.824×** | -3.2 | 0.080 | 18/47 (CHP-212, C-33 A, …) | all doses, stronger at high dose | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | 0.703× | -3.0 | 0.13 | 8/48 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3092. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 46.2 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.89× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.58× (z +10.7) | — |
| [[A-427 (line)]] | wt | 20.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -12.5) ⚠ cell-cycle shift, explains ~34% of this change |
| [[A549 (line)]] | wt | 20.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.07× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[AsPC-1 (line)]] | alt | 36.8 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.286× (z -9.3) |
| [[BT-474 (line)]] | alt | 12.8 | 0 | 1 | — | [[Afatinib (drug)]] 0.05 µM 0.213× (z -10.5) |
| [[COLO 205 (line)]] | alt | 16.2 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.271× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 19.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.63× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[HT-29 (line)]] | alt | 21.7 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.79× (z +9.2) | — |
| [[KATO III (line)]] | alt | 57.9 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.64× (z +9.0) ⚠ toxic | — |
| [[LoVo (line)]] | wt | 26.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.99× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H1573 (line)]] | alt | 9.73 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.87× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 18.3 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.81× (z +8.9) ⚠ unreliable plate only | — |
| [[NCI-H2030 (line)]] | alt | 34.1 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.40× (z +9.0) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[SNU-1 (line)]] | wt | 23.9 | 0 | 1 | — | [[PH-797804 (drug)]] 0.5 µM 0.0607× (z -9.8) |
| [[SW 900 (line)]] | alt | 17.6 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.222× (z -8.6) ⚠ transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A-172 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.11 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 41.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3092), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMYD5]] | +0.76 | +0.74 / +0.74 | both halves | 7e-06 |  |
| [[ZNF202]] | +0.70 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[DHX37]] | +0.70 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[METTL1]] | +0.69 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[GRWD1]] | +0.69 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[ZNF783]] ⚠ | +0.68 | +0.69 / +0.60 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[DIMT1]] | +0.68 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[PUS1]] | +0.67 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[PUM3]] | +0.67 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[IPO4]] | +0.67 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[CLUH]] | +0.67 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[MAK16]] | +0.67 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[ABCF2]] | +0.66 | +0.66 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTF2]] | -0.60 | -0.64 / -0.55 | both halves | 1e-05 |  |
| [[LCORL]] | -0.59 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[STK38]] | -0.56 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[TESK2]] | -0.56 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[ELF2]] | -0.55 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[CNNM2]] | -0.55 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[PIAS1]] | -0.54 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[PLEKHH3]] | -0.54 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[CTDSPL2]] | -0.54 | -0.62 / -0.39 | both halves | 5e-05 |  |
| [[HMGN3]] | -0.53 | -0.62 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises ZPR1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.602). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-16.2, -34.9); signed map (-2.1, -45.0). **Vector** length 79.8, 17.0% of its response variance represented; |z| ≥ 3 in 1,007 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.50 to 24); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.51 to 23); *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.52 to 15).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.4 | +10.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +4.0 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +3.9 | +12.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.8 | +7.1 |
|  | [[EX229 (drug)]] 5 µM |  | +3.7 | +4.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.4 | +5.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.1 | +4.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +2.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -4.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -3.0 | -3.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | +2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.7 | -6.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.7 | -3.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | -3.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.1 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.9 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | ZPR1 zinc finger |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:116,773,799-116,788,039 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ZNF259 |
| Gene groups (HGNC) | Zinc fingers |
| Matched by | ensembl_id |

**Function**, from UniProt [O75312](https://www.uniprot.org/uniprotkb/O75312) (Zinc finger protein ZPR1):

> Acts as a signaling molecule that communicates proliferative growth signals from the cytoplasm to the nucleus. It is involved in the positive regulation of cell cycle progression. Plays a role for the localization and accumulation of the survival motor neuron protein SMN1 in sub-nuclear bodies, including gems and Cajal bodies. Induces neuron differentiation and stimulates axonal growth and formation of growth cone in spinal cord motor neurons. Plays a role in the splicing of cellular pre-mRNAs. …

**Summary**, from NCBI Gene [8882](https://www.ncbi.nlm.nih.gov/gene/8882):

> The protein encoded by this gene is found in the cytoplasm of quiescent cells but translocates to the nucleolus in proliferating cells. The encoded protein interacts with survival motor neuron protein (SMN1) to enhance pre-mRNA splicing and to induce neuronal differentiation and axonal growth. Defects in this gene or the SMN1 gene can cause spinal muscular atrophy. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Nov 2015]

**Accessions** — [HGNC:13051](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13051) · Entrez [8882](https://www.ncbi.nlm.nih.gov/gene/8882) · UniProt [O75312](https://www.uniprot.org/uniprotkb/O75312) · Ensembl [ENSG00000109917](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109917)

## Data

Gene col 3092: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3092); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3092, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3092]; `tensor/DDL_lfc|DDL_z.npy` [3092]; `embed/gene_vectors.npy` [3092]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3092 or target_col == 3092). Every well: [[ZPR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZPR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
