---
symbol: "GID4"
type: "gene"
col: 6484
ensembl_id: "ENSG00000141034"
name: "GID complex subunit 4 homolog"
location: "17p11.2"
module: 3
arm: "+"
pooled_cpm: 14.71
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 23
n_dd_up_clean: 2
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# GID4

*GID complex subunit 4 homolog* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 0.5 µM: 1.28× (z +4.7, q 0.001, up in 13 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.284× (z -33.3, q 0e+00, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAP30L]] (+0.67, fdr 1e-05), [[WIPI2]] (+0.67, fdr 7e-06), [[CTDP1]] (+0.65, fdr 8e-06); moves opposite to [[SUB1]] (-0.63, fdr 1e-05), [[AGL]] (-0.61, fdr 1e-05), [[HNRNPD]] (-0.61, fdr 3e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RUSC2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6484.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | **1.28×** | +4.7 | 0.001 | 13/46 (HEC-1-A, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.22×** | +3.6 | 0.069 | 13/47 (A-172, HOP62, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.6 | 0.069 | 13/46 (A549, LS 180, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.20×** | +3.5 | 0.073 | 10/43 (Panc 03.27, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.29×** | +3.4 | 0.077 | 4/45 (Hs 766T, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.17× | +3.0 | 0.21 | 7/47 (HOP62, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6484.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.284×** | -33.3 | 0e+00 | 45/47 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.284×** | -22.7 | 0e+00 | 42/46 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.348×** | -19.7 | 0e+00 | 39/46 (SW 900, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.475×** | -13.9 | 6e-42 | 40/47 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.530×** | -11.8 | 3e-30 | 33/46 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.594×** | -9.7 | 2e-20 | 30/47 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.596×** | -9.7 | 4e-20 | 28/47 (NCI-H23, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.670×** | -7.4 | 7e-12 | 26/47 (LoVo, A498, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.489×** | -7.0 | 2e-10 | 22/48 (PANC-1, SNU-423, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.718×** | -6.2 | 4e-08 | 25/47 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.588×** | -5.2 | 1e-05 | 17/43 (RPMI-7951, RKO, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.754×** | -4.8 | 6e-05 | 13/33 (A498, KATO III, …) | all doses, flat | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.622×** | -4.6 | 2e-04 | 10/23 (NCI-H2030, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.624×** | -4.6 | 2e-04 | 19/45 (SNU-1, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.776×** | -4.5 | 2e-04 | 16/43 (C-33 A, SNU-423, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.844× | -4.4 | 3e-04 | 13/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.725×** | -4.3 | 7e-04 | 12/48 (NCI-H460, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.651×** | -4.2 | 9e-04 | 11/45 (PANC-1, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.658×** | -4.1 | 0.001 | 9/46 (MIA PaCa-2, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.685×** | -3.7 | 0.006 | 9/45 (A498, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.820×** | -3.7 | 0.006 | 16/47 (NCI-H460, A549, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6484. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 18.7 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -21.9) |
| [[PANC-1 (line)]] | alt | 14.7 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -19.9) |
| [[A-172 (line)]] | wt | 23.9 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -24.2) |
| [[A498 (line)]] | wt | 17.1 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.125× (z -17.2) |
| [[HOP62 (line)]] | alt | 16.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -23.1) |
| [[HS-578T (line)]] | alt | 15.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0892× (z -21.2) |
| [[SW480 (line)]] | alt | 16.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -17.5) |
| [[A549 (line)]] | wt | 18.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -16.6) |
| [[AsPC-1 (line)]] | alt | 6.45 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0793× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 13.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -12.0) |
| [[hTERT-HPNE (line)]] | wt | 17.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -12.7) |
| [[LoVo (line)]] | wt | 15.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -14.6) |
| [[MIA PaCa-2 (line)]] | alt | 21.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.102× (z -16.1) |
| [[RKO (line)]] | wt | 17.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -18.6) |
| [[CFPAC-1 (line)]] | alt | 5.24 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -13.5) |
| [[J82 (line)]] | alt | 15.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -19.8) |
| [[KATO III (line)]] | alt | 21.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.267× (z -9.8) |
| [[LS 180 (line)]] | wt | 10.9 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.214× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 21.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -13.0) |
| [[SNU-423 (line)]] | alt | 16.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -12.5) |
| [[SW 900 (line)]] | alt | 14.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0246× (z -19.3) |
| [[SW1417 (line)]] | alt | 9.02 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.159× (z -9.7) |
| [[A-427 (line)]] | wt | 18.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -15.2) |
| [[C-33 A (line)]] | alt | 38.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.139× (z -13.0) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[C32 (line)]] | wt | 11.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0966× (z -11.0) |
| [[COLO 205 (line)]] | alt | 8.27 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -9.6) |
| [[H4 (line)]] | wt | 15.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -11.9) |
| [[Hs 766T (line)]] | wt | 13.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 16.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.192× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 14.4 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0845× (z -8.5) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 4.27 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 12.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.123× (z -10.8) |
| [[SK-MEL-2 (line)]] | alt | 9.08 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -13.1) |
| [[AN3 CA (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.85 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6484), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAP30L]] | +0.67 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[WIPI2]] | +0.67 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[CTDP1]] | +0.65 | +0.66 / +0.57 | both halves | 8e-06 |  |
| [[CLPP]] | +0.64 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[FLYWCH1]] | +0.62 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[BFAR]] | +0.62 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[DEXI]] | +0.62 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[FBXW11]] | +0.61 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[ZNF250]] | +0.60 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[MPST]] | +0.60 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[DRD4]] | +0.59 | +0.42 / +0.65 | both halves | 4e-05 |  |
| [[DCUN1D2]] | +0.58 | +0.61 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUB1]] | -0.63 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[AGL]] | -0.61 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[HNRNPD]] | -0.61 | -0.43 / -0.61 | both halves | 3e-05 |  |
| [[ENPP1]] | -0.61 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[DZIP3]] | -0.60 | -0.63 / -0.57 | both halves | 1e-05 |  |
| [[GDAP1]] | -0.56 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[TIA1]] | -0.55 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[SRSF10]] | -0.54 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[ZNF518A]] | -0.53 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[AP1S3]] | -0.53 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[DPY19L2P2]] | -0.53 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[NFKB1]] | -0.53 | -0.53 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RUSC2]] | C | RUSC2 activity raises GID4's level | lines that do not express RUSC2 (4) vs lines expressing it (46) | 1.73× lower at baseline in the lines without RUSC2 | 0.096 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: ATP8B3, SOAT1, SPAG17 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.522). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-11.6, -9.6); signed map (-39.5, 2.8). **Vector** length 80.0, 15.4% of its response variance represented; |z| ≥ 3 in 958 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | +5.8 | +3.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | +1.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.6 | +4.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.2 | +3.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.2 | +3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.5 | +0.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.5 | +1.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.1 | +2.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.6 | -33.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.3 | -22.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.0 | -19.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -4.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.8 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -3.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.1 | -5.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.9 | -4.6 |
|  | [[EX229 (drug)]] 5 µM |  | -1.9 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | GID complex subunit 4 homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p11.2 — chr17:18,039,408-18,068,405 (+) |
| Ensembl biotype | protein_coding |
| Also known as | VID24; previously C17orf39 |
| Gene groups (HGNC) | CTLH complex subunits |
| Reactome | 3 pathways, smallest: Regulation of pyruvate metabolism; Pyruvate metabolism; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IVV7](https://www.uniprot.org/uniprotkb/Q8IVV7) (Glucose-induced degradation protein 4 homolog):

> Substrate-recognition subunit of the CTLH E3 ubiquitin-protein ligase complex that selectively accepts ubiquitin from UBE2H and mediates ubiquitination and subsequent proteasomal degradation of the transcription factor HBP1 (Probable). Binds proteins and peptides with a Pro/N-degron consisting of an unmodified N-terminal Pro followed by a small residue, and has the highest affinity for the peptide Pro-Gly-Leu-Trp. Binds peptides with an N-terminal sequence of the type …

**Summary**, from NCBI Gene [79018](https://www.ncbi.nlm.nih.gov/gene/79018):

> The multiprotein Mediator complex is a coactivator required for activation of RNA polymerase II transcription by DNA bound transcription factors. The protein encoded by this gene is thought to be a subunit of the Mediator complex. This gene is located within the Smith-Magenis syndrome region on chromosome 17. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:28453](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28453) · Entrez [79018](https://www.ncbi.nlm.nih.gov/gene/79018) · UniProt [Q8IVV7](https://www.uniprot.org/uniprotkb/Q8IVV7) · Ensembl [ENSG00000141034](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141034)

## Data

Gene col 6484: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6484); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6484, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6484]; `tensor/DDL_lfc|DDL_z.npy` [6484]; `embed/gene_vectors.npy` [6484]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6484 or target_col == 6484). Every well: [[GID4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GID4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
