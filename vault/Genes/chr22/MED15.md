---
symbol: "MED15"
type: "gene"
col: 1829
ensembl_id: "ENSG00000099917"
name: "mediator complex subunit 15"
location: "22q11.21"
module: 20
arm: "-"
pooled_cpm: 125.29
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 9
n_dd_up_clean: 10
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# MED15

*mediator complex subunit 15* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.33× (z +12.3, q 8e-32, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.594× (z -10.1, q 2e-21, down in 38 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.714× (z -6.6, q 9e-09, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLEKHG3]] (+0.48, fdr 2e-04), [[LIMS2]] (+0.45, fdr 5e-05), [[HSPG2]] (+0.45, fdr 3e-05); moves opposite to [[KLHL8]] (-0.46, fdr 3e-05), [[MTFR1]] (-0.44, fdr 1e-04), [[TXNDC12]] (-0.44, fdr 1e-04).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ATG9B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1829.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.33×** | +12.3 | 8e-32 | 46/49 (NCI-H1573, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.48×** | +10.8 | 6e-25 | 37/48 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.86×** | +10.7 | 1e-24 | 43/48 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.53×** | +8.4 | 9e-15 | 40/48 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.44×** | +7.1 | 2e-10 | 35/48 (LS 180, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.45×** | +7.0 | 2e-10 | 39/48 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.39×** | +6.5 | 9e-09 | 30/48 (LS 180, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.35×** | +5.5 | 3e-06 | 31/48 (SW480, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.30×** | +5.2 | 1e-05 | 26/48 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.26×** | +4.5 | 3e-04 | 23/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +4.5 | 3e-04 | 25/48 (LS 180, KATO III, …) | rises with dose |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.19× | +3.4 | 0.038 | 16/48 (HS-578T, HOP62, …) | rises with dose | plate-row cell shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.38×** | +3.3 | 0.040 | 18/38 (NCI-H1573, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +3.2 | 0.058 | 14/49 (HT-29, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.18× | +3.2 | 0.058 | 22/48 (A498, PANC-1, …) | rises with dose |  |
| [[Hexylresorcinol (drug)]] 5 µM |  | 1.11× | +3.0 | 0.090 | 2/49 (A-172, A498) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1829.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.594×** | -10.1 | 2e-21 | 38/49 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.590×** | -9.9 | 1e-20 | 36/44 (A549, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.714×** | -6.6 | 9e-09 | 35/48 (A-172, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.716×** | -6.5 | 1e-08 | 33/48 (A-172, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.830×** | -5.1 | 3e-05 | 17/48 (CFPAC-1, LoVo, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.927× | -5.0 | 6e-05 | 1/50 (CHP-212) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change | **0.789×** | -4.3 | 0.002 | 23/45 (A-172, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.823×** | -3.7 | 0.014 | 24/48 (A549, NCI-H2347, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~20% of this change | **0.826×** | -3.6 | 0.021 | 22/47 (HepG2/C3A, MIA PaCa-2, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.878× | -3.6 | 0.021 | 16/48 (NCI-H1573, HOP62, …) | rises with dose | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.881× | -3.5 | 0.027 | 8/48 (CFPAC-1, SK-MEL-2, …) | top dose only |  |
| [[AZD-7648 (drug)]] 5 µM |  | **0.738×** | -3.1 | 0.094 | 18/48 (C32, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1829. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 145 | 6 (2 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.74× (z +14.1) | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -15.7) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 96.1 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +13.9) | — |
| [[SW480 (line)]] | alt | 111 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +12.4) | — |
| [[BT-474 (line)]] | alt | 104 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +14.1) | — |
| [[LS 180 (line)]] | wt | 121 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.52× (z +14.2) | — |
| [[PANC-1 (line)]] | alt | 61.0 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +19.1) | — |
| [[SW48 (line)]] | wt | 121 | 5 (1 ⚠) | 0 | [[TAK-901 (drug)]] 0.05 µM 3.98× (z +11.1) | — |
| [[A-172 (line)]] | wt | 115 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.355× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.377× (z -10.9) |
| [[A498 (line)]] | wt | 126 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +13.4) | — |
| [[HS-578T (line)]] | alt | 168 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -12.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 215 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.44× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.335× (z -13.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 99.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -12.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 126 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.212× (z -16.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 174 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.460× (z -9.5) |
| [[C32 (line)]] | wt | 160 | 1 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 6.45× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.409× (z -8.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 172 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.207× (z -15.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 170 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.14× (z +10.4) | — |
| [[J82 (line)]] | alt | 107 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +11.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 162 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.330× (z -14.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 98.9 | 0 | 2 (2 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0766× (z -14.4) ⚠ toxic |
| [[C-33 A (line)]] | alt | 102 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.345× (z -10.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 171 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +11.7) | — |
| [[COLO 205 (line)]] | alt | 120 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +11.9) | — |
| [[HepG2_C3A (line)]] | wt | 114 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +12.7) | — |
| [[HOP62 (line)]] | alt | 97.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +12.0) | — |
| [[hTERT-HPNE (line)]] | wt | 108 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +14.0) | — |
| [[KATO III (line)]] | alt | 110 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.25× (z +9.4) | — |
| [[LoVo (line)]] | wt | 114 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.54× (z +10.9) | — |
| [[NCI-H2030 (line)]] | alt | 130 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +10.9) | — |
| [[NCI-H23 (line)]] | alt | 80.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.433× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change |
| [[NCI-H2347 (line)]] | alt | 170 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.50× (z +8.5) | — |
| [[RPMI-7951 (line)]] | alt | 122 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.342× (z -11.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 112 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.548× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 117 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +13.5) | — |
| [[SW 900 (line)]] | alt | 102 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +9.7) | — |
| [[SW1417 (line)]] | alt | 228 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.37× (z +8.8) | — |
| [[A-427 (line)]] | wt | 49.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 108 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 112 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 81.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 174 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 103 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 86.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 108 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 101 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1829), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLEKHG3]] | +0.48 | +0.29 / +0.54 | both halves | 2e-04 |  |
| [[LIMS2]] | +0.45 | +0.42 / +0.40 | both halves | 5e-05 |  |
| [[HSPG2]] | +0.45 | +0.52 / +0.45 | both halves | 3e-05 | pathway: RSV-host interactions |
| [[MYH16]] | +0.45 | +0.40 / +0.39 | both halves | 6e-05 |  |
| [[PRECSIT]] | +0.44 | +0.33 / +0.42 | both halves | 1e-04 |  |
| [[SNX33]] | +0.44 | +0.52 / +0.40 | both halves | 5e-05 |  |
| [[NOP14-AS1]] | +0.44 | +0.37 / +0.34 | both halves | 1e-04 |  |
| [[CBR3]] | +0.43 | +0.37 / +0.23 | both halves | 5e-04 |  |
| [[UNC13D]] | +0.43 | +0.45 / +0.35 | both halves | 1e-04 |  |
| [[PKP3]] | +0.42 | +0.35 / +0.46 | both halves | 1e-04 |  |
| [[CIC]] | +0.42 | +0.39 / +0.40 | both halves | 6e-05 |  |
| [[RNF167]] | +0.42 | +0.41 / +0.40 | both halves | 4e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL8]] | -0.46 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[MTFR1]] | -0.44 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[TXNDC12]] | -0.44 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[PIKFYVE]] | -0.42 | -0.22 / -0.47 | both halves | 6e-04 |  |
| [[UBAC2]] | -0.40 | -0.18 / -0.35 | ⚠ not reproduced | 0.001 |  |
| [[ATP1B3]] | -0.39 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[CLASP2]] | -0.39 | -0.44 / -0.23 | both halves | 5e-04 |  |
| [[CMSS1]] | -0.38 | -0.41 / -0.27 | both halves | 3e-04 |  |
| [[ZBTB44]] | -0.38 | -0.41 / -0.28 | both halves | 3e-04 |  |
| [[FDX1]] | -0.38 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[TUT4]] | -0.37 | -0.22 / -0.37 | both halves | 6e-04 |  |
| [[EEF1E1]] | -0.37 | -0.31 / -0.36 | both halves | 2e-04 |  |
| [[TAF8]] | -0.37 | -0.44 / -0.30 | both halves | 2e-04 | STRING 850 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATG9B]] | B | ATG9B activity raises MED15's level | lines that do not express ATG9B (20) vs lines expressing it (30) | 1.30× lower at baseline in the lines without ATG9B | 0.014 | ⚠ within organs, on part of the lines; also absent: AFAP1L2, GJB3, EREG |
| [[SEMA3B]] | B | SEMA3B activity raises MED15's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 1.33× lower at baseline in the lines without SEMA3B | 0.031 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[ABTB2]] | B | ABTB2 activity raises MED15's level | lines that do not express ABTB2 (7) vs lines expressing it (43) | 1.44× lower at baseline in the lines without ABTB2 | 0.043 | ⚠ within organs, on part of the lines; also absent: ZNF341-AS1, ENSG00000283511, CD59; maybe low, not absent |
| [[WNT7A]] | B | WNT7A activity raises MED15's level | lines that do not express WNT7A (39) vs lines expressing it (11) | 1.37× lower at baseline in the lines without WNT7A | 0.046 | ⚠ within organs, on part of the lines; also absent: KRT5, GSDMC, CST6 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises MED15's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.0625). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (16.3, 13.8); signed map (25.2, 10.7). **Vector** length 81.7, 22.5% of its response variance represented; |z| ≥ 3 in 1,091 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.6 | +10.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | +0.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.9 | +12.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | -1.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | +4.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.6 | +1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | -1.9 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.0 | -0.1 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.7 | +1.1 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.4 | +4.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.4 | +5.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.6 | +7.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.0 | +6.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.9 | +1.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | -0.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.7 | +0.9 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.5 | +1.1 |
|  | [[Penfluridol (drug)]] 5 µM |  | -1.5 | -0.9 |
|  | [[Terfenadine (drug)]] 5 µM |  | -1.5 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | mediator complex subunit 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.21 — chr22:20,495,913-20,587,632 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TIG-1, CAG7A, Arc105; previously TNRC7, PCQAP |
| Gene groups (HGNC) | Mediator complex |
| Reactome | 8 pathways, smallest: Transcriptional regulation of white adipocyte differentiation; RSV-host interactions; Adipogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96RN5](https://www.uniprot.org/uniprotkb/Q96RN5) (Mediator of RNA polymerase II transcription subunit 15):

> Component of the Mediator complex, a coactivator involved in the regulated transcription of nearly all RNA polymerase II-dependent genes. Mediator functions as a bridge to convey information from gene-specific regulatory proteins to the basal RNA polymerase II transcription machinery. Mediator is recruited to promoters by direct interactions with regulatory proteins and serves as a scaffold for the assembly of a functional pre-initiation complex with RNA polymerase II and the general …

**Summary**, from NCBI Gene [51586](https://www.ncbi.nlm.nih.gov/gene/51586):

> The protein encoded by this gene is a subunit of the multiprotein complexes PC2 and ARC/DRIP and may function as a transcriptional coactivator in RNA polymerase II transcription. This gene contains stretches of trinucleotide repeats and is located in the chromosome 22 region which is deleted in DiGeorge syndrome. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jun 2014]

**Accessions** — [HGNC:14248](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14248) · Entrez [51586](https://www.ncbi.nlm.nih.gov/gene/51586) · UniProt [Q96RN5](https://www.uniprot.org/uniprotkb/Q96RN5) · Ensembl [ENSG00000099917](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099917)

## Data

Gene col 1829: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1829); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1829, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1829]; `tensor/DDL_lfc|DDL_z.npy` [1829]; `embed/gene_vectors.npy` [1829]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1829 or target_col == 1829). Every well: [[MED15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MED15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
