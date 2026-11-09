---
symbol: "GORASP2"
type: "gene"
col: 3720
ensembl_id: "ENSG00000115806"
name: "golgi reassembly stacking protein 2"
location: "2q31.1"
module: 49
arm: "+"
pooled_cpm: 119.2
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 32
n_dd_up_clean: 2
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# GORASP2

*golgi reassembly stacking protein 2* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 2.84× (z +8.4, q 2e-14, up in 41 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 4 lines (SW480 4.46×, BT-474 6.55×, NCI-H2347 3.41×, HOP62 4.23×); [[PH-797804 (drug)]] 5 µM in 3 lines (SW480 3.98×, RKO 5.74×, PANC-1 4.39×).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.543× (z -11.6, q 3e-28, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRRC1]] (+0.86, fdr 7e-06), [[TMEM39A]] (+0.84, fdr 7e-06), [[PDIA5]] (+0.83, fdr 7e-06).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3720.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 4 lines (SW480 4.46×, BT-474 6.55×, NCI-H2347 3.41×, HOP62 4.23×); [[PH-797804 (drug)]] 5 µM in 3 lines (SW480 3.98×, RKO 5.74×, PANC-1 4.39×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **2.84×** | +8.4 | 2e-14 | 41/48 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.74×** | +8.1 | 1e-13 | 40/49 (SW480, BT-474, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 16 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3720.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.543×** | -11.6 | 3e-28 | 39/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.545×** | -11.4 | 1e-27 | 46/49 (AsPC-1, A549, …) | rises with dose | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.482×** | -11.2 | 5e-27 | 43/49 (NCI-H2347, AsPC-1, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.477×** | -10.5 | 9e-24 | 40/45 (NCI-H2347, BT-474, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.513×** | -9.9 | 7e-21 | 39/44 (SW1417, AsPC-1, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.549×** | -8.9 | 7e-17 | 39/48 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.660×** | -8.5 | 2e-15 | 43/48 (HOP62, HS-578T, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.583×** | -8.3 | 8e-15 | 38/48 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.621×** | -7.3 | 2e-11 | 36/48 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.632×** | -6.8 | 7e-10 | 41/48 (SW 900, A-172, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.654×** | -6.5 | 3e-09 | 36/48 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.675×** | -6.0 | 7e-08 | 33/48 (A-172, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.677×** | -6.0 | 9e-08 | 33/48 (A-172, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.677×** | -5.8 | 3e-07 | 39/50 (SW48, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.702×** | -5.4 | 2e-06 | 29/48 (KATO III, SW 900, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.743×** | -4.6 | 2e-04 | 31/48 (NCI-H1573, HOP62, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **0.783×** | -4.5 | 2e-04 | 29/48 (NCI-H1792, HS-578T, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.743×** | -4.4 | 3e-04 | 31/48 (NCI-H23, LoVo, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.749×** | -4.1 | 0.001 | 31/47 (A-172, C32, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.777×** | -3.9 | 0.003 | 29/49 (SW1417, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.795×** | -3.5 | 0.010 | 26/48 (hTERT-HPNE, A549, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.812×** | -3.2 | 0.029 | 25/48 (SW1417, A549, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.830×** | -2.9 | 0.083 | 19/48 (Panc 03.27, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3720. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 147 | 1 | 13 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 3.41× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -17.4) |
| [[A498 (line)]] | wt | 188 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -19.0) |
| [[A-172 (line)]] | wt | 97.7 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -19.9) |
| [[NCI-H1573 (line)]] | alt | 184 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.425× (z -11.8) |
| [[SW 900 (line)]] | alt | 136 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.249× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.374× (z -12.7) |
| [[CFPAC-1 (line)]] | alt | 149 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.290× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.494× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 161 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -13.8) |
| [[AsPC-1 (line)]] | alt | 168 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -18.8) |
| [[HS-578T (line)]] | alt | 132 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -15.4) |
| [[RPMI-7951 (line)]] | alt | 129 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -15.5) |
| [[A549 (line)]] | wt | 143 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -13.6) |
| [[H4 (line)]] | wt | 161 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -12.9) |
| [[HOP62 (line)]] | alt | 126 | 1 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.23× (z +8.7) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.472× (z -11.8) |
| [[LoVo (line)]] | wt | 147 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -13.2) |
| [[SW1417 (line)]] | alt | 159 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -19.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.523× (z -8.9) |
| [[SW480 (line)]] | alt | 131 | 2 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.46× (z +11.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 84.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.292× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[hTERT-HPNE (line)]] | wt | 113 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.360× (z -11.3) |
| [[NCI-H460 (line)]] | wt | 88.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -8.9) |
| [[A-427 (line)]] | wt | 70.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.288× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[BT-474 (line)]] | alt | 105 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.55× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.306× (z -11.3) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 114 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.470× (z -10.6) |
| [[LS 180 (line)]] | wt | 126 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.292× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -8.9) |
| [[NCI-H1792 (line)]] | alt | 106 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -11.5) |
| [[NCI-H23 (line)]] | alt | 137 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -11.4) |
| [[PANC-1 (line)]] | alt | 76.2 | 1 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 4.39× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.424× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[SNU-1 (line)]] | wt | 115 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.139× (z -15.9) |
| [[SNU-423 (line)]] | alt | 95.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -12.6) |
| [[SW 1271 (line)]] | alt | 99.1 | 0 | 2 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.0696× (z -11.3) |
| [[AN3 CA (line)]] | alt | 72.8 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 5 µM 0.0583× (z -8.5) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 118 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -10.2) |
| [[Hs 766T (line)]] | wt | 99.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -11.1) |
| [[KATO III (line)]] | alt | 117 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.302× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[Panc 03.27 (line)]] | alt | 102 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.327× (z -10.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 113 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 5.74× (z +9.3) | — |
| [[SK-MEL-2 (line)]] | alt | 89.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -8.8) |
| [[SW 1088 (line)]] | alt | 139 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -9.4) |
| [[C-33 A (line)]] | alt | 73.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 67.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 72.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 62.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 86.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 96.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 119 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3720), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRRC1]] | +0.86 | +0.88 / +0.80 | both halves | 7e-06 |  |
| [[TMEM39A]] | +0.84 | +0.89 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[PDIA5]] | +0.83 | +0.85 / +0.75 | both halves | 7e-06 |  |
| [[SSR2]] | +0.82 | +0.84 / +0.69 | both halves | 7e-06 |  |
| [[NUS1]] | +0.81 | +0.84 / +0.68 | both halves | 7e-06 |  |
| [[SEC24D]] | +0.80 | +0.82 / +0.75 | both halves | 7e-06 | STRING 401 |
| [[SEC13]] | +0.78 | +0.82 / +0.69 | both halves | 7e-06 | pathway: Mitotic Prophase; STRING 637 |
| [[IER3IP1]] | +0.76 | +0.82 / +0.73 | both halves | 7e-06 |  |
| [[TXNDC11]] | +0.76 | +0.76 / +0.73 | both halves | 7e-06 |  |
| [[COG6]] | +0.76 | +0.79 / +0.65 | both halves | 7e-06 |  |
| [[SEC23A]] | +0.76 | +0.78 / +0.66 | both halves | 7e-06 | STRING 500 |
| [[RARS1]] | +0.75 | +0.67 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises GORASP2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MCTP2]] | B | MCTP2 activity raises GORASP2's level | lines that do not express MCTP2 (20) vs lines expressing it (30) | 1.32× lower at baseline in the lines without MCTP2 | 0.077 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, ENSG00000284644, MPZL3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.857). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.5, -33.1); signed map (-51.4, 9.6). **Vector** length 124, 45.7% of its response variance represented; |z| ≥ 3 in 1,161 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *XBP1(S) activates chaperone genes* (reactome, mean cos +0.57 to 8); *IRE1alpha activates chaperones* (reactome, mean cos +0.57 to 8); *Unfolded Protein Response (UPR)* (reactome, mean cos +0.57 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.1 | +8.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +5.0 | -7.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.0 | +8.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | -0.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | +4.5 | -4.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.8 | +1.3 |
|  | [[EX229 (drug)]] 0.5 µM |  | +2.7 | +1.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.6 | +2.7 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -6.7 | -4.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.4 | -1.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -6.2 | -3.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | -5.9 | -5.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.3 | -6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.5 | -8.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.0 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | -4.6 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.0 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | golgi reassembly stacking protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.1 — chr2:170,928,464-170,967,130 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GRASP55, GRS2, GOLPH6 |
| Gene groups (HGNC) | PDZ domain containing |
| Reactome | 5 pathways, smallest: Golgi Cisternae Pericentriolar Stack Reorganization; Mitotic Prophase; M Phase |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H8Y8](https://www.uniprot.org/uniprotkb/Q9H8Y8) (Golgi reassembly-stacking protein 2):

> Key structural protein of the Golgi apparatus. The membrane cisternae of the Golgi apparatus adhere to each other to form stacks, which are aligned side by side to form the Golgi ribbon. Acting in concert with GORASP1/GRASP65, is required for the formation and maintenance of the Golgi ribbon, and may be dispensable for the formation of stacks. However, other studies suggest that GORASP2 plays a role in the assembly and membrane stacking of the Golgi cisternae, and in the process by which Golgi …

**Summary**, from NCBI Gene [26003](https://www.ncbi.nlm.nih.gov/gene/26003):

> This gene encodes a member of the Golgi reassembly stacking protein family. These proteins may play a role in the stacking of Golgi cisternae and Golgi ribbon formation, as well as Golgi fragmentation during apoptosis or mitosis. The encoded protein also plays a role in the intracellular transport of transforming growth factor alpha and may function as a molecular chaperone. A pseudogene of this gene is located on the short arm of chromosome 2. Alternatively spliced transcript variants encoding …

**Accessions** — [HGNC:17500](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17500) · Entrez [26003](https://www.ncbi.nlm.nih.gov/gene/26003) · UniProt [Q9H8Y8](https://www.uniprot.org/uniprotkb/Q9H8Y8) · Ensembl [ENSG00000115806](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115806)

## Data

Gene col 3720: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3720); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3720, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3720]; `tensor/DDL_lfc|DDL_z.npy` [3720]; `embed/gene_vectors.npy` [3720]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3720 or target_col == 3720). Every well: [[GORASP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GORASP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
