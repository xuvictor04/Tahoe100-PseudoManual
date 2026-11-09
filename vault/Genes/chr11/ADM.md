---
symbol: "ADM"
type: "gene"
col: 7327
ensembl_id: "ENSG00000148926"
name: "adrenomedullin"
location: "11p15.4"
module: 79
arm: "+"
pooled_cpm: 170.4
n_lines_expressing: 44
n_dd_up: 6
n_dd_down: 9
n_dd_up_clean: 4
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 7
direction_downstream: 5
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# ADM

*adrenomedullin* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 2.49× (z +6.6, q 2e-08, up in 40 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.444× (z -5.8, q 4e-06, down in 34 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTR9]] (+0.73, fdr 7e-06), [[DEPP1]] (+0.71, fdr 7e-06), [[RLF]] (+0.69, fdr 1e-05); moves opposite to [[ARMC6]] (-0.59, fdr 1e-05), [[MACROH2A1]] (-0.56, fdr 3e-05), [[LY6G5B]] (-0.56, fdr 5e-05).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[PLIN2]] → it (grade B ⚠); 5 go from it, the strongest it → [[DDIT4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7327.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **2.49×** | +6.6 | 2e-08 | 40/42 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.20×** | +4.8 | 4e-04 | 33/42 (A-427, MIA PaCa-2, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **3.44×** | +4.7 | 5e-04 | 35/43 (NCI-H23, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.76×** | +4.1 | 0.005 | 31/42 (AsPC-1, PANC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.74×** | +3.7 | 0.020 | 29/41 (MIA PaCa-2, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.64×** | +3.6 | 0.027 | 26/42 (AsPC-1, PANC-1, …) | inconsistent across doses | composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | 1.51× | +3.0 | 0.20 | 23/42 (HS-578T, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7327.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.444×** | -5.8 | 4e-06 | 34/42 (J82, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.435×** | -5.4 | 2e-05 | 28/39 (SNU-423, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.483×** | -5.2 | 4e-05 | 36/42 (J82, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.624×** | -4.7 | 3e-04 | 38/42 (SNU-423, A549, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.493×** | -4.6 | 6e-04 | 29/42 (SNU-423, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~22% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.539×** | -4.4 | 9e-04 | 27/42 (J82, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.504×** | -4.4 | 9e-04 | 35/41 (NCI-H2347, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.695×** | -3.6 | 0.019 | 24/43 (SNU-423, HS-578T, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.636×** | -3.2 | 0.080 | 24/43 (SNU-423, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | 0.655× | -3.0 | 0.15 | 25/42 (BT-474, J82, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.43 per unit of S-phase module lfc, +0.73 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7327. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 634 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0523× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0772× (z -15.9) |
| [[NCI-H2347 (line)]] | alt | 157 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -14.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.306× (z -8.7) |
| [[PANC-1 (line)]] | alt | 231 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +12.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 4.48× (z +9.0) | — |
| [[A498 (line)]] | wt | 280 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.275× (z -9.1) |
| [[hTERT-HPNE (line)]] | wt | 518 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0948× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.136× (z -10.7) |
| [[J82 (line)]] | alt | 566 | 1 | 4 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.25× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.177× (z -13.0) |
| [[A-172 (line)]] | wt | 181 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0900× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.153× (z -10.1) |
| [[C32 (line)]] | wt | 323 | 0 | 4 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.120× (z -11.4) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.197× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 126 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +14.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H1792 (line)]] | alt | 281 | 1 | 2 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.55× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.253× (z -9.3) |
| [[HOP62 (line)]] | alt | 408 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.149× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 88.2 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 6.90× (z +10.1) | — |
| [[A-427 (line)]] | wt | 55.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.62× (z +10.3) | — |
| [[BT-474 (line)]] | alt | 93.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -9.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 258 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -9.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 117 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.47× (z +9.8) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[HCT15 (line)]] | alt | 82.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 162 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0892× (z -12.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 337 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -11.6) ⚠ cell-cycle shift, explains ~33% of this change |
| [[Panc 03.27 (line)]] | alt | 141 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -9.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 240 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -9.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 180 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.102× (z -15.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 258 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 172 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.6 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 76.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 221 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 68.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 114 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 92.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 65.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 186 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 62.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 67.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 60.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 75.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 39.4 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 15.5 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.9 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 14.2 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 417 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 67.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 50.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7327), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTR9]] | +0.73 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[DEPP1]] | +0.71 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[RLF]] | +0.69 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[HILPDA]] | +0.69 | +0.65 / +0.75 | both halves | 7e-06 |  |
| [[RYBP]] | +0.68 | +0.57 / +0.66 | both halves | 9e-06 |  |
| [[RNF113A]] | +0.66 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[DDIT4]] | +0.65 | +0.58 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[WSB1]] | +0.64 | +0.64 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[FAM53C]] | +0.64 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[ANKRD37]] | +0.63 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[BTG1]] | +0.63 | +0.50 / +0.68 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[FAM13A]] | +0.63 | +0.66 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARMC6]] | -0.59 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[MACROH2A1]] | -0.56 | -0.45 / -0.60 | both halves | 3e-05 |  |
| [[LY6G5B]] | -0.56 | -0.39 / -0.55 | both halves | 5e-05 |  |
| [[TMX3]] | -0.56 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[XRCC5]] | -0.55 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[NUP188]] | -0.55 | -0.46 / -0.54 | both halves | 2e-05 |  |
| [[GNL3L]] | -0.54 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[RCC2]] | -0.54 | -0.58 / -0.46 | both halves | 2e-05 |  |
| [[NUP50]] | -0.54 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[SAE1]] | -0.54 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[CAPRIN1]] | -0.53 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[NUDT3]] | -0.53 | -0.42 / -0.55 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLIN2]] | B | PLIN2 activity raises ADM's level | lines that do not express PLIN2 (17) vs lines expressing it (33) | 2.50× lower at baseline in the lines without PLIN2 | 0.032 | ⚠ within organs, on part of the lines; also absent: AXL, UBE2Q2P13, SLC2A3 |
| [[TOP2A]] | B | TOP2A activity raises ADM's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PLOD2]] | B | PLOD2 activity raises ADM's level | lines that do not express PLOD2 (15) vs lines expressing it (35) | 2.60× lower at baseline in the lines without PLOD2 | 0.059 | ⚠ within organs, on part of the lines; also absent: ITGA1, TMEM92-AS1, RGS17 |
| [[LRCH2]] | B | LRCH2 activity raises ADM's level | lines that do not express LRCH2 (27) vs lines expressing it (23) | 2.07× lower at baseline in the lines without LRCH2 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PDGFRA, ENSG00000263655, PCDH17 |
| [[HDAC6]] | B | HDAC6 activity raises ADM's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity raises ADM's level | compounds that target TOP2B: 2 of 2 lower it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[DDIT4]] | C | DDIT4 activity raises ADM's level | lines that do not express DDIT4 (3) vs lines expressing it (47) | 3.84× lower at baseline in the lines without DDIT4 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: B4GALT1, TIMP1, UGDH; maybe low, not absent; its own permutation p |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DDIT4]] | B | ADM activity raises DDIT4's level | lines that do not express ADM (6) vs lines expressing it (44) | 2.55× lower at baseline in the lines without ADM | 0.060 | ⚠ within organs, on part of the lines; also absent: FTH1, CDC42EP1, ENSG00000284716; its own permutation p |
| [[GNL3L]] | B | ADM activity lowers GNL3L's level | lines that do not express ADM (6) vs lines expressing it (44) | 1.87× higher at baseline in the lines without ADM | 0.060 | ⚠ within organs, on part of the lines; also absent: FTH1, CDC42EP1, ENSG00000284716; its own permutation p |
| [[P4HA1]] | B | ADM activity raises P4HA1's level | lines that do not express ADM (6) vs lines expressing it (44) | 1.53× lower at baseline in the lines without ADM | 0.060 | ⚠ within organs, on part of the lines; also absent: FTH1, CDC42EP1, ENSG00000284716; its own permutation p |
| [[PFKFB3]] | B | ADM activity raises PFKFB3's level | lines that do not express ADM (6) vs lines expressing it (44) | 1.43× lower at baseline in the lines without ADM | 0.089 | ⚠ within organs, on part of the lines; also absent: FTH1, CDC42EP1, ENSG00000284716; its own permutation p |
| [[PSME3]] | B | ADM activity lowers PSME3's level | lines that do not express ADM (6) vs lines expressing it (44) | 1.45× higher at baseline in the lines without ADM | 0.098 | ⚠ within organs, on part of the lines; also absent: FTH1, CDC42EP1, ENSG00000284716 |

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.738). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.7, -13.6); signed map (-33.1, 24.7). **Vector** length 133, 50.5% of its response variance represented; |z| ≥ 3 in 861 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *glycolysis* (hallmark, mean cos +0.56 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.3 | +6.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.3 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +1.4 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.9 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.5 | +4.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.1 | +2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.0 | +1.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.9 | +1.0 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -10.5 | -4.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -10.3 | -5.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -9.7 | -3.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -8.6 | -2.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.9 | -4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -4.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.1 | -2.4 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.7 | -2.0 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -2.4 | -1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | adrenomedullin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:10,305,073-10,307,397 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AM |
| Gene groups (HGNC) | Neuropeptides |
| Hallmark sets | INFLAMMATORY_RESPONSE, HYPOXIA |
| Reactome | 10 pathways, smallest: Calcitonin-like ligand receptors; Class B/2 (Secretin family receptors); High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells |
| Matched by | ensembl_id |

**Function**, from UniProt [P35318](https://www.uniprot.org/uniprotkb/P35318) (Pro-adrenomedullin):

> Adrenomedullin/ADM and proadrenomedullin N-20 terminal peptide/PAMP are peptide hormones that act as potent hypotensive and vasodilatator agents. Numerous actions have been reported most related to the physiologic control of fluid and electrolyte homeostasis. In the kidney, ADM is diuretic and natriuretic, and both ADM and PAMP inhibit aldosterone secretion by direct adrenal actions. In pituitary gland, both peptides at physiologically relevant doses inhibit basal ACTH secretion. Both peptides …

**Summary**, from NCBI Gene [133](https://www.ncbi.nlm.nih.gov/gene/133):

> The protein encoded by this gene is a preprohormone which is cleaved to form two biologically active peptides, adrenomedullin and proadrenomedullin N-terminal 20 peptide. Adrenomedullin is a 52 aa peptide with several functions, including vasodilation, regulation of hormone secretion, promotion of angiogenesis, and antimicrobial activity. The antimicrobial activity is antibacterial, as the peptide has been shown to kill E. coli and S. aureus at low concentration. [provided by RefSeq, Aug 2014]

**Accessions** — [HGNC:259](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:259) · Entrez [133](https://www.ncbi.nlm.nih.gov/gene/133) · UniProt [P35318](https://www.uniprot.org/uniprotkb/P35318) · Ensembl [ENSG00000148926](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148926)

## Data

Gene col 7327: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7327); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7327, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7327]; `tensor/DDL_lfc|DDL_z.npy` [7327]; `embed/gene_vectors.npy` [7327]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7327 or target_col == 7327). Every well: [[ADM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
