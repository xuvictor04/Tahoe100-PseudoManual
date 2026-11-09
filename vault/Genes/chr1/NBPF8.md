---
symbol: "NBPF8"
type: "gene"
col: 15657
ensembl_id: "ENSG00000270231"
name: "NBPF member 8"
location: "1p11.2"
module: 110
arm: "+"
pooled_cpm: 21.87
n_lines_expressing: 48
n_dd_up: 8
n_dd_down: 16
n_dd_up_clean: 5
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/110"]
generated_by: "tahoemap"
---

# NBPF8

*NBPF member 8* — 1p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Daptomycin (drug)]] 5 µM: 1.44× (z +5.7, q 7e-06, up in 21 of 46 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Vinblastine (sulfate) (drug)]] 0.5 µM: 1.32× (z +4.3, q 0.002, up in 16 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.560× (z -9.2, q 2e-17, down in 29 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NBPF9]] (+0.81, fdr 7e-06), [[NBPF15]] (+0.81, fdr 7e-06), [[NBPF20]] (+0.68, fdr 7e-06); moves opposite to [[EFNA1]] (-0.54, fdr 1e-05), [[CTNND1]] (-0.52, fdr 3e-05), [[GBP2]] (-0.49, fdr 3e-05).
> It is in [[Module 110]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[ELF3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15657.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.44×** | +5.7 | 7e-06 | 21/46 (NCI-H460, C32, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +5.0 | 1e-04 | 19/46 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.35×** | +4.7 | 4e-04 | 20/45 (C32, NCI-H1573, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.32×** | +4.3 | 0.002 | 16/44 (NCI-H1792, C32, …) | two highest doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.28×** | +3.8 | 0.018 | 15/45 (C32, NCI-H1792, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.076 | 12/46 (NCI-H2030, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **1.49×** | +3.3 | 0.078 | 10/44 (A-427, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.23×** | +3.3 | 0.078 | 8/45 (HOP62, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | 1.22× | +3.1 | 0.12 | 14/46 (NCI-H2030, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15657.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.560×** | -9.2 | 2e-17 | 29/46 (J82, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.619×** | -7.6 | 1e-11 | 28/46 (MIA PaCa-2, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.670×** | -6.3 | 4e-08 | 24/46 (J82, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.725×** | -6.1 | 2e-07 | 25/46 (SK-MEL-2, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.717×** | -5.3 | 2e-05 | 21/46 (SK-MEL-2, AsPC-1, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.803×** | -4.9 | 8e-05 | 24/45 (SK-MEL-2, LOX-IMVI, …) | rises with dose | composition shift |
| [[Binimetinib (drug)]] 5 µM |  | **0.794×** | -3.9 | 0.008 | 18/46 (SK-MEL-2, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.816×** | -3.6 | 0.023 | 15/46 (SK-MEL-2, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Capmatinib (drug)]] 5 µM |  | **0.650×** | -3.6 | 0.023 | 8/42 (AsPC-1, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.794×** | -3.4 | 0.039 | 7/46 (AsPC-1, SW 1088, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.857× | -3.4 | 0.041 | 15/46 (AsPC-1, A-427, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.811×** | -3.3 | 0.042 | 12/45 (CHP-212, SK-MEL-2, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.863× | -3.3 | 0.045 | 13/46 (SK-MEL-2, BT-474, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.808×** | -3.3 | 0.045 | 17/45 (HCT15, SK-MEL-2, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.813×** | -3.2 | 0.058 | 17/42 (J82, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.816×** | -3.0 | 0.082 | 12/46 (Hs 766T, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15657. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 35.9 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.260× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.292× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 109 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -14.6) ⚠ cell-cycle shift, explains ~61% of this change |
| [[H4 (line)]] | wt | 31.2 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.102× (z -12.2) ⚠ transcription drop; cell-cycle shift, explains ~83% of this change |
| [[MIA PaCa-2 (line)]] | alt | 33.9 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.267× (z -9.7) |
| [[SW480 (line)]] | alt | 22.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.285× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change |
| [[A549 (line)]] | wt | 14.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.228× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 48.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.333× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 32.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0945× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change |
| [[NCI-H23 (line)]] | alt | 31.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 21.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.196× (z -9.0) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SNU-423 (line)]] | alt | 24.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.19 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.54 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.10 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.05 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.48 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15657), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBPF9]] | +0.81 | +0.81 / +0.78 | both halves | 7e-06 | same gene group |
| [[NBPF15]] | +0.81 | +0.81 / +0.77 | both halves | 7e-06 | same gene group |
| [[NBPF20]] | +0.68 | +0.62 / +0.66 | both halves | 7e-06 | same gene group |
| [[FXYD5]] | +0.59 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[TM4SF19]] | +0.59 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[PDE4DIPP2]] | +0.58 | +0.54 / +0.63 | both halves | 1e-05 | ⚠ same locus (20.2 kb: neighbours can correlate without regulation) |
| [[PARVB]] | +0.57 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[ARHGAP22]] | +0.57 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[CORO2B]] | +0.56 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[RPSAP52]] | +0.55 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[PNP]] | +0.55 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[METTL3]] | +0.54 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[LRRC8C]] | +0.54 | +0.55 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFNA1]] | -0.54 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[CTNND1]] | -0.52 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[GBP2]] | -0.49 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[MAP3K8]] | -0.46 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[ELF3]] | -0.46 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[FRK]] | -0.46 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[RBM47]] | -0.46 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[ABHD16A]] | -0.46 | -0.40 / -0.48 | both halves | 4e-05 |  |
| [[MTUS1]] | -0.45 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[KIAA1522]] | -0.45 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[TOB1]] | -0.44 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[GAREM1]] | -0.44 | -0.33 / -0.47 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELF3]] | B | ELF3 activity lowers NBPF8's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 2.25× higher at baseline in the lines without ELF3 | 5e-04 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |
| [[PARVB]] | B | PARVB activity raises NBPF8's level | lines that do not express PARVB (13) vs lines expressing it (37) | 2.18× lower at baseline in the lines without PARVB | 0.015 | ⚠ within organs, on part of the lines; also absent: PARVG, MSRB3, RASSF8 |
| [[RBM47]] | B | RBM47 activity lowers NBPF8's level | lines that do not express RBM47 (20) vs lines expressing it (30) | 2.12× higher at baseline in the lines without RBM47 | 0.020 | ⚠ within organs, on part of the lines; also absent: FA2H, MISP, ELF3 |
| [[FRK]] | B | FRK activity lowers NBPF8's level | lines that do not express FRK (22) vs lines expressing it (28) | 1.79× higher at baseline in the lines without FRK | 0.037 | ⚠ within organs, on part of the lines; also absent: GOLT1A, MYO5B, NCMAP |
| [[FLI1]] | B | FLI1 activity raises NBPF8's level | lines that do not express FLI1 (31) vs lines expressing it (19) | 1.98× lower at baseline in the lines without FLI1 | 0.043 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, LINC01615 |
| [[MAP2K1]] | B | MAP2K1 activity raises NBPF8's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[ZEB1]] | B | ZEB1 activity strengthens NBPF8's drug response | lines that do not express ZEB1 (9) vs lines expressing it (37) | the lines without ZEB1 respond 0.20× as strongly (z diff +2.14); rises at some drug-doses, falls at others (27% from rises): Panobinostat 5 µM: 0.99x vs 0.52x (z diff +4.1); Panobinostat 0.5 µM: 0.94x vs 0.54x (z diff +3.7); Daptomycin 5 µM: 1.11x vs 1.43x (z diff +1.8) | 0.060 | ⚠ within organs, on part of the lines; also absent: ITGA10, LIX1L, BRSK1; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[EFNA1]] | B | EFNA1 activity lowers NBPF8's level | lines that do not express EFNA1 (13) vs lines expressing it (37) | 1.72× higher at baseline in the lines without EFNA1 | 0.081 | ⚠ within organs, on part of the lines; also absent: ELF3-AS1, ANO9, GPRC5A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 110]]; 43 genes; every member is in the + arm (projection on the module's main direction 0.704). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.0, -25.2); signed map (-17.3, 47.3). **Vector** length 85.4, 17.2% of its response variance represented; |z| ≥ 3 in 891 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.8 | +5.0 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +3.1 | +5.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | -0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | +2.9 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +2.3 | +4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +1.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.2 | +3.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.0 | +4.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.0 | +2.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | -3.9 | -4.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.8 | -6.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.2 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.1 | -5.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.9 | -3.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.6 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | NBPF member 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p11.2 — chr1:120,415,035-120,469,676 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously NBPF8P |
| Gene groups (HGNC) | NBPF members |
| Matched by | ensembl_id |

UniProt [Q3BBV2](https://www.uniprot.org/uniprotkb/Q3BBV2) carries no function annotation.

**Summary**, from NCBI Gene [728841](https://www.ncbi.nlm.nih.gov/gene/728841):

> This gene is a member of the neuroblastoma breakpoint family (NBPF) which consists of dozens of recently duplicated genes primarily located in segmental duplications on human chromosome 1. This gene family has experienced its greatest expansion within the human lineage and has expanded, to a lesser extent, among primates in general. Members of this gene family are characterized by tandemly repeated copies of DUF1220 protein domains. Gene copy number variations in the human chromosomal region …

**Accessions** — [HGNC:31990](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31990) · Entrez [728841](https://www.ncbi.nlm.nih.gov/gene/728841) · UniProt [Q3BBV2](https://www.uniprot.org/uniprotkb/Q3BBV2) · Ensembl [ENSG00000270231](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000270231)

## Data

Gene col 15657: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15657); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15657, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15657]; `tensor/DDL_lfc|DDL_z.npy` [15657]; `embed/gene_vectors.npy` [15657]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15657 or target_col == 15657). Every well: [[NBPF8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NBPF8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
