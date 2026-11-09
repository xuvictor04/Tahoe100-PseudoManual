---
symbol: "VAT1"
type: "gene"
col: 3000
ensembl_id: "ENSG00000108828"
name: "vesicle amine transport 1"
location: "17q21.31"
module: 30
arm: "+"
pooled_cpm: 52.54
n_lines_expressing: 47
n_dd_up: 11
n_dd_down: 9
n_dd_up_clean: 7
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 4
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# VAT1

*vesicle amine transport 1* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.64× (z +13.8, q 3e-40, up in 40 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.46× (z +5.3, q 1e-05, up in 28 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.660× (z -8.3, q 4e-14, down in 30 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAPK3]] (+0.66, fdr 9e-06), [[PSAP]] (+0.65, fdr 7e-06), [[STX7]] (+0.65, fdr 7e-06); moves opposite to [[LRR1]] (-0.57, fdr 2e-05), [[ALG8]] (-0.56, fdr 3e-05), [[ASAH2B]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 4 go from it, the strongest it → [[RHOA]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3000.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.64×** | +13.8 | 3e-40 | 40/43 (SK-MEL-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.53×** | +12.7 | 3e-34 | 38/41 (C32, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.77×** | +7.2 | 1e-10 | 34/42 (SK-MEL-2, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.48×** | +5.6 | 4e-06 | 29/44 (PANC-1, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.46×** | +5.3 | 1e-05 | 28/45 (KATO III, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +5.0 | 4e-05 | 3/46 (NCI-H2030, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +4.5 | 4e-04 | 26/45 (RKO, HOP62, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.34×** | +4.2 | 0.002 | 25/45 (SNU-423, RPMI-7951, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.53×** | +3.8 | 0.010 | 23/44 (HOP62, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.45×** | +3.3 | 0.056 | 20/44 (COLO 205, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.18× | +3.3 | 0.056 | 17/45 (SK-MEL-2, RKO, …) | top dose only |  |
| [[4EGI-1 (drug)]] 5 µM |  | **1.53×** | +3.1 | 0.079 | 22/44 (LoVo, H4, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.097 | 18/45 (H4, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3000.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.660×** | -8.3 | 4e-14 | 30/45 (A-427, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.563×** | -8.2 | 1e-13 | 33/45 (LOX-IMVI, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.678×** | -5.3 | 2e-05 | 23/45 (LOX-IMVI, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.700×** | -4.8 | 2e-04 | 28/44 (HEC-1-A, Panc 03.27, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.737×** | -4.3 | 0.002 | 24/44 (HOP62, J82, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.608×** | -3.7 | 0.021 | 22/45 (HCT15, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.767×** | -3.6 | 0.024 | 20/45 (SNU-423, NCI-H23, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.624×** | -3.5 | 0.033 | 20/46 (Panc 03.27, CHP-212, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **0.789×** | -3.2 | 0.075 | 19/44 (SK-MEL-2, A-427, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.804× | -3.1 | 0.11 | 22/45 (MIA PaCa-2, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3000. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 66.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.26× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 53.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0924× (z -19.4) |
| [[NCI-H2347 (line)]] | alt | 86.9 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.43× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -11.8) |
| [[PANC-1 (line)]] | alt | 31.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.96× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -11.5) |
| [[SK-MEL-2 (line)]] | alt | 109 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.24× (z +15.8) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 117 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.79× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -20.0) |
| [[A498 (line)]] | wt | 69.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +11.1) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 57.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.97× (z +12.0) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 47.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -13.7) |
| [[LoVo (line)]] | wt | 19.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.66× (z +10.5) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 65.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -14.4) |
| [[SW48 (line)]] | wt | 67.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -11.4) |
| [[AsPC-1 (line)]] | alt | 45.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.87× (z +9.0) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 54.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 93.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.44× (z +10.1) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 61.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +8.7) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 60.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.21× (z +10.4) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 29.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.15× (z +9.2) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 48.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.274× (z -10.7) |
| [[NCI-H1792 (line)]] | alt | 38.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 72.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -12.0) |
| [[Panc 03.27 (line)]] | alt | 59.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -17.5) |
| [[SHP-77 (line)]] | alt | 37.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.90× (z +11.1) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 70.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 39.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 38.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.00× (z +9.6) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 116 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.58 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 121 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 62.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 65.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 44.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 46.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 65.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 50.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.4 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3000), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPK3]] | +0.66 | +0.60 / +0.57 | both halves | 9e-06 |  |
| [[PSAP]] | +0.65 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[STX7]] | +0.65 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[SLC25A23]] | +0.62 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[SNX30]] | +0.62 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[SNN]] | +0.62 | +0.58 / +0.46 | both halves | 2e-05 |  |
| [[NPC2]] | +0.60 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[GLMP]] | +0.60 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[GET1]] | +0.60 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[MTURN]] | +0.60 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[RETREG2]] | +0.60 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[NTAN1]] | +0.59 | +0.57 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRR1]] | -0.57 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[ALG8]] | -0.56 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[ASAH2B]] | -0.56 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[ZNF41]] | -0.54 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[TOE1]] | -0.53 | -0.43 / -0.48 | both halves | 4e-05 |  |
| [[GEN1]] | -0.53 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[ZNF724]] | -0.52 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[ZNF689]] | -0.52 | -0.44 / -0.40 | both halves | 4e-05 |  |
| [[MIS12]] | -0.52 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[BRCA2]] | -0.51 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[BMS1P4-1]] | -0.51 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[CPSF3]] | -0.51 | -0.58 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RHOA]] | C | VAT1 activity strengthens RHOA's drug response | lines that do not express VAT1 (3) vs lines expressing it (46) | the lines without VAT1 respond 0.57× as strongly (z diff +1.43); strongest at Dinaciclib 5 µM: 0.94x vs 2.43x (z diff +8.4) | 0.059 | ⚠ few lines (3 vs 47); across organs; also absent: SH2B3, C12orf75, SKAP2; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[ERP29]] | C | VAT1 activity weakens ERP29's drug response | lines that do not express VAT1 (3) vs lines expressing it (45) | the lines without VAT1 respond 1.09× as strongly (z diff -0.80); strongest at Dinaciclib 0.05 µM: 3.25x vs 2.14x (z diff -3.2) | 0.064 | ⚠ few lines (3 vs 47); across organs; also absent: SH2B3, C12orf75, SKAP2; maybe low, not absent; target measured in part of the lines; the reference differs; artifact flags |
| [[FAM161A]] | C | VAT1 activity raises FAM161A's level | lines that do not express VAT1 (3) vs lines expressing it (47) | 3.02× lower at baseline in the lines without VAT1 | 0.079 | ⚠ few lines (3 vs 47); across organs; also absent: SH2B3, C12orf75, SKAP2; maybe low, not absent |
| [[HECTD3]] | C | VAT1 activity raises HECTD3's level | lines that do not express VAT1 (3) vs lines expressing it (47) | 1.68× lower at baseline in the lines without VAT1 | 0.082 | ⚠ few lines (3 vs 47); across organs; also absent: SH2B3, C12orf75, SKAP2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.479). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (1.9, -7.3); signed map (-29.4, -4.4). **Vector** length 112, 32.9% of its response variance represented; |z| ≥ 3 in 869 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 0.5 µM |  | +4.4 | +3.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.1 | +4.5 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.9 | +2.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +2.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +3.7 | +3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.4 | +1.6 |
|  | [[Rapamycin (drug)]] 5 µM |  | +3.3 | +2.5 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +3.3 | +1.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.2 | +1.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.7 | -8.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | -5.4 | -3.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.3 | -2.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.0 | -8.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.4 | -5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.4 | -1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.9 | -2.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.6 | -1.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.8 | -4.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.7 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | vesicle amine transport 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:43,014,607-43,025,123 (-) |
| Ensembl biotype | protein_coding |
| Also known as | VATI, FLJ20230 |
| Gene groups (HGNC) | Oxidoreductases |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99536](https://www.uniprot.org/uniprotkb/Q99536) (NADPH-dependent quinone oxidoreductase VAT1):

> Multifunctional protein with enzymatic and transport activities. Probable NADPH-dependent quinone oxidoreductase which physiological substrates and function are unclear. Alternatively, has also been suggested to mediate the transfer of negatively charged phospholipids including phosphatidic acid (PA), phosphatidylserine (PS) and phosphatidylglycerol (PG) between endoplasmic reticulum and mitochondrial membranes. Could regulate mitochondrial fusion through its interaction with mitofusins.

**Summary**, from NCBI Gene [10493](https://www.ncbi.nlm.nih.gov/gene/10493):

> Synaptic vesicles are responsible for regulating the storage and release of neurotransmitters in the nerve terminal. The protein encoded by this gene is an abundant integral membrane protein of cholinergic synaptic vesicles and is thought to be involved in vesicular transport. It belongs to the quinone oxidoreductase subfamily of zinc-containing alcohol dehydrogenase proteins. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:16919](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16919) · Entrez [10493](https://www.ncbi.nlm.nih.gov/gene/10493) · UniProt [Q99536](https://www.uniprot.org/uniprotkb/Q99536) · Ensembl [ENSG00000108828](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108828)

## Data

Gene col 3000: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3000); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3000, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3000]; `tensor/DDL_lfc|DDL_z.npy` [3000]; `embed/gene_vectors.npy` [3000]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3000 or target_col == 3000). Every well: [[VAT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VAT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
