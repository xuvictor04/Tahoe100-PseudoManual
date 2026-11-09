---
symbol: "UBE2V2"
type: "gene"
col: 9761
ensembl_id: "ENSG00000169139"
name: "ubiquitin conjugating enzyme E2 V2"
location: "8q11.21"
module: 28
arm: "+"
pooled_cpm: 100.38
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 6
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# UBE2V2

*ubiquitin conjugating enzyme E2 V2* — 8q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.66× (z +10.9, q 7e-25, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.827× (z -5.8, q 5e-06, down in 25 of 48 measured lines) ⚠ cell-cycle shift, explains ~79% of this change. The strongest without an alert is [[GSK1059615 (drug)]] 5 µM: 0.656× (z -4.7, q 4e-04, down in 34 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNG1A]] (+0.63, fdr 7e-06), [[DDX50]] (+0.63, fdr 7e-06), [[ZNG1B]] (+0.60, fdr 1e-05); moves opposite to [[H3-3A]] (-0.53, fdr 2e-05), [[MARCHF6]] (-0.53, fdr 2e-05), [[PPT2]] (-0.52, fdr 2e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MTOR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9761.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.66×** | +10.9 | 7e-25 | 45/48 (HOP62, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.62×** | +10.4 | 1e-22 | 39/49 (A498, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.63×** | +10.1 | 8e-22 | 36/44 (A-172, A498, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.49×** | +8.6 | 7e-16 | 44/48 (LOX-IMVI, NCI-H460, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.46×** | +7.5 | 5e-12 | 37/47 (A549, LOX-IMVI, …) | all doses, flat | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.39×** | +7.1 | 1e-10 | 34/48 (NCI-H23, Hs 766T, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **1.37×** | +6.8 | 1e-09 | 31/48 (HCT15, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.34×** | +6.1 | 6e-08 | 34/48 (HOP62, COLO 205, …) | all doses, flat | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.28×** | +5.4 | 5e-06 | 31/48 (NCI-H2347, C32, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.30×** | +5.3 | 8e-06 | 26/45 (SNU-423, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.19× | +5.2 | 8e-06 | 21/48 (COLO 205, NCI-H1573, …) | all doses, flat | composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | **1.56×** | +5.0 | 2e-05 | 33/48 (HT-29, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.46×** | +4.3 | 9e-04 | 25/48 (PANC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | 1.18× | +3.6 | 0.012 | 23/48 (LoVo, RKO, …) | two highest doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.18× | +3.6 | 0.014 | 16/47 (HOP62, NCI-H23, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 1.18× | +3.5 | 0.015 | 20/48 (Panc 03.27, A-427, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.063 | 17/48 (A-172, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9761.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.827×** | -5.8 | 5e-06 | 25/48 (C32, RPMI-7951, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.934× | -5.0 | 2e-04 | 0/50 | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.656×** | -4.7 | 4e-04 | 34/49 (NCI-H460, CHP-212, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.796×** | -4.7 | 4e-04 | 26/47 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.839× | -3.8 | 0.019 | 20/48 (HEC-1-A, RKO, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.818×** | -3.6 | 0.026 | 18/48 (HS-578T, J82, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.735×** | -3.4 | 0.046 | 23/50 (NCI-H596, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.853× | -3.4 | 0.047 | 16/48 (C32, HepG2/C3A, …) | rises with dose | position effect removed |
| [[Sapanisertib (drug)]] 5 µM |  | **0.740×** | -3.4 | 0.047 | 19/49 (HEC-1-A, J82, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9761. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 128 | 4 (3 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 2.93× (z +16.0) | — |
| [[LoVo (line)]] | wt | 84.7 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +10.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 1.90× (z +8.6) | — |
| [[NCI-H596 (line)]] | alt | 94.8 | 1 | 3 | [[Salicylic acid (drug)]] 0.5 µM 3.33× (z +9.4) | [[Canagliflozin (hemihydrate) (drug)]] 5 µM 0.0836× (z -19.3) |
| [[A549 (line)]] | wt | 100 | 3 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.29× (z +9.9) | — |
| [[C32 (line)]] | wt | 172 | 0 | 3 (2 ⚠) | — | [[Ponatinib (drug)]] 5 µM 0.376× (z -11.5) |
| [[LOX-IMVI (line)]] | wt | 113 | 3 | 0 | [[Homoharringtonine (drug)]] 0.05 µM 2.43× (z +11.5) | — |
| [[SW480 (line)]] | alt | 91.4 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.28× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 1.92× (z +9.5) | — |
| [[A498 (line)]] | wt | 122 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.48× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[Hs 766T (line)]] | wt | 69.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | [[Allantoin (drug)]] 0.5 µM 0.351× (z -11.9) |
| [[NCI-H460 (line)]] | wt | 99.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 1.95× (z +9.7) | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.542× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 110 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.01× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.01× (z +10.4) | — |
| [[SNU-423 (line)]] | alt | 91.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.40× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[A-172 (line)]] | wt | 90.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.18× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[COLO 205 (line)]] | alt | 53.3 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.05× (z +9.1) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[HS-578T (line)]] | alt | 123 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.23× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[HT-29 (line)]] | alt | 101 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.95× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 97.1 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.56× (z +9.8) | — |
| [[NCI-H1573 (line)]] | alt | 66.7 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.54× (z +11.0) | — |
| [[NCI-H1792 (line)]] | alt | 104 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.81× (z +11.0) | — |
| [[NCI-H23 (line)]] | alt | 148 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 1.89× (z +8.5) | — |
| [[Panc 03.27 (line)]] | alt | 66.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.39× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[SW 1088 (line)]] | alt | 76.3 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 5 µM 0.0750× (z -8.5) |
| [[A-427 (line)]] | wt | 99.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 107 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 80.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 71.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 118 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 89.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 95.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 95.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 77.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 107 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 89.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 93.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 82.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 148 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 85.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 99.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 87.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 96.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9761), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNG1A]] | +0.63 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[DDX50]] | +0.63 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[ZNG1B]] | +0.60 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[GOLGA1]] | +0.58 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[NCBP2]] | +0.56 | +0.61 / +0.46 | both halves | 2e-05 |  |
| [[TBC1D9B]] | +0.55 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[RBAK]] | +0.54 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[ZNF770]] | +0.53 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[ZNF160]] | +0.53 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[ZNF638]] | +0.53 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[CRYBG3]] | +0.52 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[THUMPD3]] | +0.52 | +0.59 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[H3-3A]] | -0.53 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[MARCHF6]] | -0.53 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[PPT2]] | -0.52 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[SMG1P1]] | -0.51 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[MARCHF8]] | -0.49 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[CHASERR]] | -0.49 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[TMEM131L]] | -0.49 | -0.55 / -0.39 | both halves | 6e-05 |  |
| [[ASAH1]] | -0.48 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[MFSD14CP]] | -0.48 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[SPPL3]] | -0.47 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[LAPTM4A]] | -0.47 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[ANXA11]] | -0.47 | -0.56 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTOR]] | B | MTOR activity raises UBE2V2's level | compounds that target MTOR: 3 of 8 lower it (Bimiralisib, GSK1059615, Sapanisertib) | 38% of the class's compounds vs 1.4% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.259). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-24.5, 17.7); signed map (8.6, -15.9). **Vector** length 113, 33.4% of its response variance represented; |z| ≥ 3 in 946 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +8.6 | +10.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.5 | +8.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +5.4 | +7.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +5.1 | +7.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.0 | +5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +2.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.3 | +1.5 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -7.5 | -4.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | -6.9 | -5.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.0 | -1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.8 | -3.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -2.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.6 | -3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.5 | -1.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.5 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin conjugating enzyme E2 V2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q11.21 — chr8:48,008,415-48,064,708 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UEV-2, DDVit-1, EDPF-1, MMS2, UEV2, EDPF1, DDVIT1, EDAF-1 |
| Gene groups (HGNC) | Ubiquitin conjugating enzymes E2 |
| Reactome | 20 pathways, smallest: Formation of Incision Complex in GG-NER; Nonhomologous End-Joining (NHEJ); E3 ubiquitin ligases ubiquitinate target proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15819](https://www.uniprot.org/uniprotkb/Q15819) (Ubiquitin-conjugating enzyme E2 variant 2):

> Has no ubiquitin ligase activity on its own. The UBE2V2/UBE2N heterodimer catalyzes the synthesis of non-canonical poly-ubiquitin chains that are linked through 'Lys-63'. This type of poly-ubiquitination does not lead to protein degradation by the proteasome. Mediates transcriptional activation of target genes. Plays a role in the control of progress through the cell cycle and differentiation. Plays a role in the error-free DNA repair pathway and contributes to the survival of cells after DNA …

**Summary**, from NCBI Gene [7336](https://www.ncbi.nlm.nih.gov/gene/7336):

> Ubiquitin-conjugating enzyme E2 variant proteins constitute a distinct subfamily within the E2 protein family. They have sequence similarity to other ubiquitin-conjugating enzymes but lack the conserved cysteine residue that is critical for the catalytic activity of E2s. The protein encoded by this gene also shares homology with ubiquitin-conjugating enzyme E2 variant 1 and yeast MMS2 gene product. It may be involved in the differentiation of monocytes and enterocytes. [provided by RefSeq, Jul …

**Accessions** — [HGNC:12495](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12495) · Entrez [7336](https://www.ncbi.nlm.nih.gov/gene/7336) · UniProt [Q15819](https://www.uniprot.org/uniprotkb/Q15819) · Ensembl [ENSG00000169139](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169139)

## Data

Gene col 9761: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9761); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9761, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9761]; `tensor/DDL_lfc|DDL_z.npy` [9761]; `embed/gene_vectors.npy` [9761]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9761 or target_col == 9761). Every well: [[UBE2V2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE2V2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
