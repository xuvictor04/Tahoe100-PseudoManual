---
symbol: "IK"
type: "gene"
col: 3434
ensembl_id: "ENSG00000113141"
name: "IK cytokine"
location: "5q31.3"
module: 74
arm: "+"
pooled_cpm: 91.54
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 1
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# IK

*IK cytokine* — 5q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.15× (z +9.2, q 1e-17, up in 44 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 2.07× (z +8.8, q 4e-16, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.650× (z -5.2, q 9e-05, down in 42 of 48 measured lines) ⚠ unreliable plate only.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (AsPC-1 0.380×; ⚠ unreliable plate only).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM23]] (+0.75, fdr 7e-06), [[CIR1]] (+0.73, fdr 7e-06), [[ASB8]] (+0.73, fdr 7e-06); moves opposite to [[UBE2G2]] (-0.58, fdr 1e-05), [[NETO2]] (-0.58, fdr 1e-04), [[MRPS25]] (-0.57, fdr 8e-05).
> It is in [[Module 074]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 11 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3434.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.15×** | +9.2 | 1e-17 | 44/49 (A549, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.07×** | +8.8 | 4e-16 | 48/48 (A549, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.96×** | +8.1 | 7e-14 | 46/48 (MIA PaCa-2, SW480, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.01×** | +8.1 | 7e-14 | 36/43 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.74×** | +6.7 | 3e-09 | 46/48 (MIA PaCa-2, A549, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.67×** | +6.2 | 5e-08 | 40/48 (NCI-H1573, A549, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.42×** | +5.8 | 4e-07 | 37/48 (A549, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.64×** | +5.7 | 8e-07 | 41/48 (A549, NCI-H460, …) | rises with dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.54×** | +5.2 | 1e-05 | 37/48 (NCI-H1573, A549, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.49×** | +4.4 | 6e-04 | 29/45 (A549, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.95×** | +4.2 | 0.001 | 35/49 (COLO 205, LoVo, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +3.8 | 0.008 | 32/48 (NCI-H23, LoVo, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~75% of this change | **1.36×** | +3.7 | 0.009 | 36/48 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.4 | 0.024 | 0/50 | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.62×** | +3.0 | 0.090 | 29/47 (AsPC-1, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3434.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (AsPC-1 0.380×; ⚠ unreliable plate only).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.650×** | -5.2 | 9e-05 | 42/48 (AsPC-1, SW1417, …) | all doses, flat |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 0.829× | -3.1 | 0.58 | 22/48 (HS-578T, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3434. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 72.6 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +12.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.93× (z +9.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 81.0 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.35× (z +10.2) | — |
| [[NCI-H460 (line)]] | wt | 82.7 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.36× (z +8.6) | — |
| [[SW480 (line)]] | alt | 101 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.52× (z +9.5) | — |
| [[A-172 (line)]] | wt | 84.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[LoVo (line)]] | wt | 93.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +10.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.35× (z +8.6) | — |
| [[PANC-1 (line)]] | alt | 96.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SNU-423 (line)]] | alt | 105 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.98× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[A498 (line)]] | wt | 117 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.37× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[AsPC-1 (line)]] | alt | 99.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.380× (z -10.0) ⚠ unreliable plate only |
| [[C-33 A (line)]] | alt | 81.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[HCT15 (line)]] | alt | 102 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[HEC-1-A (line)]] | alt | 108 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[LOX-IMVI (line)]] | wt | 83.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.62× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[LS 180 (line)]] | wt | 51.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +10.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H1573 (line)]] | alt | 66.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.81× (z +8.9) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H1792 (line)]] | alt | 56.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +9.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H23 (line)]] | alt | 95.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[RKO (line)]] | wt | 48.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.97× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[A-427 (line)]] | wt | 91.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 153 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 71.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 87.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 60.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 75.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 108 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 104 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 85.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 76.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 94.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 88.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 80.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 83.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 95.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 92.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 85.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 53.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 96.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 76.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 86.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3434), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM23]] | +0.75 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[CIR1]] | +0.73 | +0.74 / +0.76 | both halves | 7e-06 |  |
| [[ASB8]] | +0.73 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[CRNKL1]] | +0.73 | +0.83 / +0.71 | both halves | 7e-06 | same gene group; pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 458 |
| [[PRPF6]] | +0.72 | +0.75 / +0.59 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 995 |
| [[GOLGB1]] | +0.72 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[PPIL4]] | +0.70 | +0.72 / +0.68 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[AKAP9]] | +0.69 | +0.58 / +0.78 | both halves | 7e-06 |  |
| [[SYF2]] | +0.69 | +0.74 / +0.70 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[FRG1]] | +0.69 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[VIRMA]] | +0.66 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[BOD1L1]] | +0.66 | +0.60 / +0.80 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2G2]] | -0.58 | -0.51 / -0.66 | both halves | 1e-05 |  |
| [[NETO2]] | -0.58 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[MRPS25]] | -0.57 | -0.37 / -0.57 | both halves | 8e-05 |  |
| [[PRPS2]] | -0.57 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[ADAT2]] | -0.56 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[SIGMAR1]] | -0.56 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[KTN1-AS1]] | -0.56 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[DHRS11]] | -0.55 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[SLC25A15]] | -0.55 | -0.54 / -0.45 | both halves | 3e-05 | same gene group |
| [[CTSC]] | -0.54 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[ADCY3]] | -0.54 | -0.53 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.764). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-3.8, -47.9); signed map (-10.9, -4.7). **Vector** length 93.9, 32.8% of its response variance represented; |z| ≥ 3 in 695 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +4.8 | +4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.4 | +1.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +4.3 | +6.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.0 | +5.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | +3.1 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +2.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.9 | +1.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.9 | -0.4 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.6 | +1.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.0 | -5.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.3 | +2.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.8 | +2.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -0.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.5 | -1.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.4 | -2.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.4 | -2.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.1 | -2.2 |
|  | [[EX229 (drug)]] 5 µM |  | -3.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | IK cytokine |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.3 — chr5:140,647,058-140,662,480 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RED, RER |
| Gene groups (HGNC) | Spliceosomal B complex; MicroRNA protein coding host genes |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13123](https://www.uniprot.org/uniprotkb/Q13123) (Protein Red):

> Involved in pre-mRNA splicing as a component of the spliceosome. Auxiliary spliceosomal protein that regulates selection of alternative splice sites in a small set of target pre-mRNA species (Probable). Required for normal mitotic cell cycle progression. Recruits MAD1L1 and MAD2L1 to kinetochores, and is required to trigger the spindle assembly checkpoint. Required for normal accumulation of SMU1.; (Microbial infection) Required, together with SMU1, for normal splicing of influenza A virus NS1 …

**Summary**, from NCBI Gene [3550](https://www.ncbi.nlm.nih.gov/gene/3550):

> The protein encoded by this gene was identified by its RED repeat, a stretch of repeated arginine, glutamic acid and aspartic acid residues. The protein localizes to discrete dots within the nucleus, excluding the nucleolus. Its function is unknown. This gene maps to chromosome 5; however, a pseudogene may exist on chromosome 2. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:5958](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5958) · Entrez [3550](https://www.ncbi.nlm.nih.gov/gene/3550) · UniProt [Q13123](https://www.uniprot.org/uniprotkb/Q13123) · Ensembl [ENSG00000113141](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113141)

## Data

Gene col 3434: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3434); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3434, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3434]; `tensor/DDL_lfc|DDL_z.npy` [3434]; `embed/gene_vectors.npy` [3434]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3434 or target_col == 3434). Every well: [[IK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
