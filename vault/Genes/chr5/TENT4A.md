---
symbol: "TENT4A"
type: "gene"
col: 3418
ensembl_id: "ENSG00000112941"
name: "terminal nucleotidyltransferase 4A"
location: "5p15.31"
module: 134
arm: "+"
pooled_cpm: 128.22
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 16
n_dd_up_clean: 4
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/134"]
generated_by: "tahoemap"
---

# TENT4A

*terminal nucleotidyltransferase 4A* — 5p15.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 1.61× (z +5.8, q 4e-06, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.333× (z -12.8, q 5e-35, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.626× (z -8.1, q 1e-13, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDC1]] (+0.75, fdr 7e-06), [[PDXP]] (+0.73, fdr 7e-06), [[PLEKHA8]] (+0.69, fdr 7e-06); moves opposite to [[LARP7]] (-0.64, fdr 7e-06), [[CHURC1]] (-0.62, fdr 1e-05), [[ZNF776]] (-0.61, fdr 1e-05).
> It is in [[Module 134]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[P3H3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3418.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **1.61×** | +5.8 | 4e-06 | 38/48 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.57×** | +5.4 | 2e-05 | 34/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +4.0 | 0.013 | 29/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.38×** | +3.9 | 0.016 | 26/47 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | 1.31× | +3.3 | 0.12 | 27/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | 1.66× | +3.2 | 0.12 | 28/48 (HOP62, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | 1.52× | +3.1 | 0.14 | 33/48 (C-33 A, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3418.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.333×** | -12.8 | 5e-35 | 43/44 (NCI-H23, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.413×** | -10.7 | 2e-24 | 46/49 (CHP-212, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.626×** | -8.1 | 1e-13 | 34/48 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.506×** | -8.0 | 3e-13 | 42/48 (NCI-H23, A-172, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.563×** | -7.0 | 3e-10 | 40/48 (A-427, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.553×** | -6.7 | 3e-09 | 33/45 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.585×** | -6.5 | 6e-09 | 43/48 (AsPC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.580×** | -6.4 | 1e-08 | 41/47 (RKO, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.610×** | -6.0 | 1e-07 | 43/48 (BT-474, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.727×** | -5.5 | 2e-06 | 38/48 (A-427, AsPC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.697×** | -4.4 | 6e-04 | 32/48 (NCI-H23, AsPC-1, …) | top dose only | cell-cycle shift (explains ~17% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.715×** | -4.1 | 0.002 | 33/48 (NCI-H1573, A-172, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.802×** | -3.8 | 0.007 | 32/48 (A-172, A498, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.760×** | -3.2 | 0.055 | 23/48 (SNU-1, NCI-H2347, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.775×** | -3.1 | 0.073 | 30/48 (HOP62, RKO, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.781×** | -3.0 | 0.093 | 27/48 (A-427, A498, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3418. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 128 | 6 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 0.05 µM 3.18× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.312× (z -12.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 65.7 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0947× (z -20.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.321× (z -10.4) |
| [[NCI-H2347 (line)]] | alt | 140 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.303× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.465× (z -11.2) |
| [[A-172 (line)]] | wt | 131 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -15.8) |
| [[J82 (line)]] | alt | 187 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.469× (z -10.9) |
| [[LOX-IMVI (line)]] | wt | 138 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.402× (z -12.1) |
| [[NCI-H23 (line)]] | alt | 123 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0959× (z -22.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.308× (z -16.5) |
| [[A-427 (line)]] | wt | 161 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -21.2) |
| [[A549 (line)]] | wt | 142 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.227× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.434× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 103 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.332× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.387× (z -9.5) |
| [[LoVo (line)]] | wt | 147 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.334× (z -11.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 115 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.252× (z -13.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 203 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.152× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.301× (z -9.1) |
| [[SNU-1 (line)]] | wt | 209 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0623× (z -21.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.403× (z -10.2) |
| [[AN3 CA (line)]] | alt | 272 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.192× (z -9.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 150 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0650× (z -18.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 180 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.332× (z -10.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 141 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.195× (z -14.2) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 184 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.260× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 177 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.288× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 140 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.471× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 124 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.83× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.334× (z -9.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 79.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.306× (z -13.0) |
| [[SNU-423 (line)]] | alt | 111 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -10.1) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 132 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.343× (z -9.6) |
| [[CHP-212 (line)]] | wt | 151 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0733× (z -14.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 62.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +10.5) | — |
| [[HCT15 (line)]] | alt | 126 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 83.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.443× (z -8.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 102 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0803× (z -17.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 71.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.337× (z -9.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 113 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.264× (z -10.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 162 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -10.4) |
| [[Panc 03.27 (line)]] | alt | 114 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.312× (z -10.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 80.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.415× (z -9.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 110 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.226× (z -12.5) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 108 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.296× (z -9.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 167 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -13.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 140 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -9.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 137 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.417× (z -8.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 154 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.225× (z -10.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 85.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 160 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 96.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 109 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 130 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3418), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDC1]] | +0.75 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[PDXP]] | +0.73 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[PLEKHA8]] | +0.69 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[CHSY1]] | +0.67 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[PDE7A]] | +0.66 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[POC1A]] | +0.66 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[KIAA1958]] | +0.65 | +0.77 / +0.54 | both halves | 1e-05 |  |
| [[CABIN1]] | +0.64 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[WRNIP1]] | +0.63 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[POM121]] | +0.62 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[CCSAP]] | +0.62 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[STK32C]] | +0.62 | +0.69 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LARP7]] | -0.64 | -0.67 / -0.59 | both halves | 7e-06 |  |
| [[CHURC1]] | -0.62 | -0.68 / -0.56 | both halves | 1e-05 |  |
| [[ZNF776]] | -0.61 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[ZNF140]] | -0.60 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[LINC00174]] | -0.60 | -0.67 / -0.49 | both halves | 1e-05 |  |
| [[ZNF268]] | -0.60 | -0.67 / -0.50 | both halves | 1e-05 |  |
| [[MRFAP1L1]] | -0.59 | -0.73 / -0.53 | both halves | 1e-05 |  |
| [[LYRM2]] | -0.59 | -0.66 / -0.54 | both halves | 1e-05 |  |
| [[ZMYM4]] | -0.59 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[C11orf58]] | -0.59 | -0.61 / -0.62 | both halves | 7e-06 |  |
| [[ZNF189]] | -0.58 | -0.69 / -0.54 | both halves | 1e-05 |  |
| [[FCF1]] | -0.58 | -0.66 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[P3H3]] | B | P3H3 activity raises TENT4A's level | lines that do not express P3H3 (10) vs lines expressing it (40) | 1.42× lower at baseline in the lines without P3H3 | 0.036 | ⚠ within organs, on part of the lines; also absent: STARD9, GSTA4, CTXN1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 134]]; 35 genes; every member is in the + arm (projection on the module's main direction 0.734). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (9.3, -16.8); signed map (-39.5, 23.2). **Vector** length 111, 42.5% of its response variance represented; |z| ≥ 3 in 1,038 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.6 | -2.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.3 | +2.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | -0.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | -0.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.3 | -0.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.1 | +0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | -0.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.8 | +1.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.5 | +3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +0.1 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -8.8 | -8.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.6 | -7.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.4 | -8.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.9 | -4.1 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.9 | -5.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.0 | -3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -3.0 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.6 | -2.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.5 | -1.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.5 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | terminal nucleotidyltransferase 4A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.31 — chr5:6,713,432-6,757,044 (+) |
| Ensembl biotype | protein_coding |
| Also known as | POLK, TRF4, LAK-1, TRF4-1; previously POLS, PAPD7 |
| Gene groups (HGNC) | Non-canonical poly(A) polymerases; Terminal nucleotidyltransferases |
| Hallmark sets | UV_RESPONSE_DN, G2M_CHECKPOINT |
| Reactome | 5 pathways, smallest: Nuclear RNA decay; Signaling by BRAF and RAF1 fusions; Oncogenic MAPK signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5XG87](https://www.uniprot.org/uniprotkb/Q5XG87) (Terminal nucleotidyltransferase 4A):

> Terminal nucleotidyltransferase that catalyzes preferentially the transfer of ATP and GTP on RNA 3' poly(A) tail creating a heterogeneous 3' poly(A) tail leading to mRNAs stabilization by protecting mRNAs from active deadenylation. Also functions as a catalytic subunit of a TRAMP-like complex which has a poly(A) RNA polymerase activity and is involved in a post-transcriptional quality control mechanism. Polyadenylation with short oligo(A) tails is required for the degradative activity of the …

**Summary**, from NCBI Gene [11044](https://www.ncbi.nlm.nih.gov/gene/11044):

> The protein encoded by this gene is a DNA polymerase that is likely involved in DNA repair. In addition, the encoded protein may be required for sister chromatid adhesion. Alternatively spliced transcript variants that encode different isoforms have been described. [provided by RefSeq, Jan 2010]

**Accessions** — [HGNC:16705](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16705) · Entrez [11044](https://www.ncbi.nlm.nih.gov/gene/11044) · UniProt [Q5XG87](https://www.uniprot.org/uniprotkb/Q5XG87) · Ensembl [ENSG00000112941](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112941)

## Data

Gene col 3418: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3418); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3418, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3418]; `tensor/DDL_lfc|DDL_z.npy` [3418]; `embed/gene_vectors.npy` [3418]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3418 or target_col == 3418). Every well: [[TENT4A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TENT4A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
