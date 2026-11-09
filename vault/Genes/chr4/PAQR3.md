---
symbol: "PAQR3"
type: "gene"
col: 8662
ensembl_id: "ENSG00000163291"
name: "progestin and adipoQ receptor family member 3"
location: "4q21.21"
module: 190
arm: "+"
pooled_cpm: 26.79
n_lines_expressing: 50
n_dd_up: 40
n_dd_down: 0
n_dd_up_clean: 28
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/190"]
generated_by: "tahoemap"
---

# PAQR3

*progestin and adipoQ receptor family member 3* — 4q21.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 40 drug-doses (12 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 2.09× (z +9.0, q 9e-17, up in 40 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (NCI-H2030 0.0772×, SW48 0.163×, C-33 A 0.236×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (SNU-1 0.0952×, SW48 0.162×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SNU-1 0.0559×; ⚠ toxic; transcription drop); [[Atazanavir (sulfate) (drug)]] 0.5 µM in 1 line (AN3 CA 0.0904×); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (HCT15 0.125×); [[Irinotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (COLO 205 0.0761×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC35G1]] (+0.68, fdr 7e-06), [[NAPB]] (+0.64, fdr 7e-06), [[NAE1]] (+0.63, fdr 7e-06); moves opposite to [[BPTF]] (-0.60, fdr 2e-05), [[ZNF324]] (-0.58, fdr 1e-05), [[HES1]] (-0.57, fdr 2e-05).
> It is in [[Module 190]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PALS2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 40 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8662.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **2.09×** | +9.0 | 9e-17 | 40/48 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.59×** | +8.0 | 4e-13 | 33/47 (A-172, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.87×** | +7.7 | 3e-12 | 37/48 (LS 180, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.82×** | +7.3 | 3e-11 | 34/47 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +7.2 | 5e-11 | 29/48 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.80×** | +7.2 | 6e-11 | 37/48 (CFPAC-1, LS 180, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.88×** | +6.8 | 8e-10 | 32/42 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.48×** | +6.7 | 1e-09 | 33/48 (J82, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.76×** | +6.7 | 2e-09 | 33/46 (NCI-H2030, MIA PaCa-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.67×** | +6.3 | 2e-08 | 34/48 (SHP-77, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.65×** | +6.2 | 4e-08 | 32/48 (NCI-H1792, SW480, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.63×** | +6.0 | 1e-07 | 29/48 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.60×** | +5.8 | 3e-07 | 27/47 (A-172, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +5.6 | 8e-07 | 28/47 (SW480, SHP-77, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.61×** | +5.5 | 1e-06 | 25/48 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +5.0 | 2e-05 | 25/48 (HT-29, C32, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.44×** | +4.5 | 2e-04 | 25/47 (NCI-H460, NCI-H1792, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.66×** | +4.4 | 3e-04 | 25/48 (A498, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.43×** | +4.4 | 3e-04 | 25/48 (NCI-H23, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~5% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.29×** | +4.4 | 3e-04 | 23/48 (H4, SHP-77, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8662.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (NCI-H2030 0.0772×, SW48 0.163×, C-33 A 0.236×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (SNU-1 0.0952×, SW48 0.162×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SNU-1 0.0559×; ⚠ toxic; transcription drop); [[Atazanavir (sulfate) (drug)]] 0.5 µM in 1 line (AN3 CA 0.0904×); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (HCT15 0.125×); [[Irinotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (COLO 205 0.0761×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.768× | -3.3 | 0.28 | 9/48 (HEC-1-A, J82, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.771× | -3.2 | 0.28 | 12/47 (NCI-H2030, Panc 03.27, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 0.778× | -3.1 | 0.28 | 17/43 (SNU-1, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Apalutamide (drug)]] 0.5 µM |  | 0.781× | -3.1 | 0.28 | 17/48 (SW 1088, AsPC-1, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.786× | -3.0 | 0.28 | 14/47 (hTERT-HPNE, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8662. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 19.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +11.8) | — |
| [[A498 (line)]] | wt | 49.2 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.26× (z +10.0) | — |
| [[SHP-77 (line)]] | alt | 42.0 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.14× (z +11.3) | — |
| [[HOP62 (line)]] | alt | 15.8 | 2 | 0 | [[Auranofin (drug)]] 5 µM 6.64× (z +11.3) | — |
| [[NCI-H460 (line)]] | wt | 20.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +9.9) | — |
| [[SNU-1 (line)]] | wt | 142 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0559× (z -20.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 28.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +8.7) | — |
| [[SW48 (line)]] | wt | 42.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.162× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 30.0 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.5 µM 0.0904× (z -9.5) |
| [[AsPC-1 (line)]] | alt | 29.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +9.2) | — |
| [[C-33 A (line)]] | alt | 39.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.236× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change |
| [[C32 (line)]] | wt | 19.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.40× (z +10.6) | — |
| [[CFPAC-1 (line)]] | alt | 12.7 | 1 | 0 | [[Belinostat (drug)]] 5 µM 5.08× (z +8.5) | — |
| [[COLO 205 (line)]] | alt | 8.77 | 0 | 1 | — | [[Irinotecan (hydrochloride) (drug)]] 0.05 µM 0.0761× (z -8.8) |
| [[H4 (line)]] | wt | 22.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.66× (z +9.4) | — |
| [[HCT15 (line)]] | alt | 14.5 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.125× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 21.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0772× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change |
| [[NCI-H2347 (line)]] | alt | 54.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +9.5) | — |
| [[RKO (line)]] | wt | 37.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +10.4) | — |
| [[RPMI-7951 (line)]] | alt | 39.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.33× (z +8.8) | — |
| [[SW480 (line)]] | alt | 24.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.12× (z +13.6) | — |
| [[A-427 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 34.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8662), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35G1]] | +0.68 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[NAPB]] | +0.64 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[NAE1]] | +0.63 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[ME2]] | +0.63 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[FAM219B]] | +0.59 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[HPRT1]] | +0.59 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[CHORDC1]] | +0.58 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[FHIP2A]] | +0.56 | +0.57 / +0.34 | both halves | 1e-04 |  |
| [[USP46]] | +0.56 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[C1orf216]] | +0.55 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[MIR29B2CHG]] | +0.55 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[SEC61A2]] | +0.54 | +0.62 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BPTF]] | -0.60 | -0.46 / -0.68 | both halves | 2e-05 |  |
| [[ZNF324]] | -0.58 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[HES1]] | -0.57 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[GPATCH8]] | -0.55 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[THRAP3]] | -0.55 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[XRN1]] | -0.53 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[ZC3H18]] | -0.53 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[GPATCH1]] | -0.51 | -0.40 / -0.47 | both halves | 4e-05 |  |
| [[RSPRY1]] | -0.51 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[PDPK1]] | -0.50 | -0.47 / -0.40 | both halves | 4e-05 |  |
| [[ZZEF1]] | -0.50 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[TOGARAM1]] | -0.50 | -0.46 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PALS2]] | C | PALS2 activity raises PAQR3's level | lines that do not express PALS2 (3) vs lines expressing it (47) | 2.18× lower at baseline in the lines without PALS2 | 0.087 | ⚠ few lines (3 vs 47); across organs; also absent: TMCC2, SACS, ANKRD44; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 190]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.647). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-10.0, -9.9); signed map (-31.6, -18.2). **Vector** length 81.6, 19.0% of its response variance represented; |z| ≥ 3 in 1,131 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.6 | +6.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | +5.9 | +6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.8 | +5.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.0 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change | +3.8 | +1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +5.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.9 | +4.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.6 | +4.5 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.0 | +0.8 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -7.2 | -1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.1 | +0.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.4 | +8.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.1 | +3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.7 | +6.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.8 | -1.2 |
|  | [[Mifepristone (drug)]] 0.5 µM |  | -1.8 | -2.1 |
|  | [[Apalutamide (drug)]] 0.5 µM |  | -1.8 | -3.1 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -1.7 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | progestin and adipoQ receptor family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.21 — chr4:78,887,127-78,939,438 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Progestin and adipoQ receptor family |
| Reactome | 4 pathways, smallest: Negative regulation of MAPK pathway; RAF/MAP kinase cascade; MAPK1/MAPK3 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6TCH7](https://www.uniprot.org/uniprotkb/Q6TCH7) (Progestin and adipoQ receptor family member 3):

> Golgi-scaffold protein which modulates its interactors activities by anchoring them to the Golgi apparatus. Functions as a spatial regulator of RAF1 kinase by sequestrating it to the Golgi apparatus. Acts as a positive regulator of cholesterol biosynthesis by mediating the anchoring of the SCAP:SREBP complex in the Golgi apparatus, thereby promoting SCAP:SREBF2 complex formation, potentiating SREBF2 and SREBF1 processing and enhancing lipid synthesis. Also regulates PPARA and PPARG functions by …

**Summary**, from NCBI Gene [152559](https://www.ncbi.nlm.nih.gov/gene/152559):

> This gene encodes a seven-transmembrane protein localized in the Golgi apparatus in mammalian cells. The encoded protein belongs to the progestin and adipoQ receptor (PAQR) family. This protein functions as a tumor suppressor by inhibiting the Raf/MEK/ERK signaling cascade. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Apr 2017]

**Accessions** — [HGNC:30130](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30130) · Entrez [152559](https://www.ncbi.nlm.nih.gov/gene/152559) · UniProt [Q6TCH7](https://www.uniprot.org/uniprotkb/Q6TCH7) · Ensembl [ENSG00000163291](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163291)

## Data

Gene col 8662: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8662); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8662, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8662]; `tensor/DDL_lfc|DDL_z.npy` [8662]; `embed/gene_vectors.npy` [8662]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8662 or target_col == 8662). Every well: [[PAQR3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAQR3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
