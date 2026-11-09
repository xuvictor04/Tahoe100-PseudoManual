---
symbol: "IQCK"
type: "gene"
col: 10509
ensembl_id: "ENSG00000174628"
name: "IQ motif containing K"
location: "16p12.3"
module: 89
arm: "+"
pooled_cpm: 20.86
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 19
n_dd_up_clean: 7
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/089"]
generated_by: "tahoemap"
---

# IQCK

*IQ motif containing K* — 16p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.43× (z +4.8, q 9e-04, up in 17 of 41 measured lines) ⚠ toxic. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.35× (z +4.5, q 0.001, up in 19 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.554× (z -8.8, q 7e-16, down in 34 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.716× (z -7.0, q 5e-10, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BBOF1]] (+0.60, fdr 1e-05), [[WDR73]] (+0.58, fdr 9e-06), [[OSCP1]] (+0.57, fdr 1e-05); moves opposite to [[ERRFI1]] (-0.55, fdr 1e-05), [[KLHL29]] (-0.54, fdr 7e-05), [[DISP3]] (-0.51, fdr 5e-04).
> It is in [[Module 089]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LPAR3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10509.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +4.8 | 9e-04 | 17/41 (NCI-H2030, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.25×** | +4.7 | 9e-04 | 18/48 (J82, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +4.5 | 0.001 | 19/48 (J82, CFPAC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.24×** | +4.4 | 0.001 | 20/48 (Hs 766T, A498, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.36×** | +4.1 | 0.006 | 19/48 (A549, SW480, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.29×** | +3.7 | 0.017 | 15/47 (A-172, A498, …) | two highest doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.20× | +3.7 | 0.017 | 14/48 (C32, Hs 766T, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.30×** | +3.5 | 0.039 | 12/48 (A-172, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.25×** | +3.3 | 0.059 | 8/48 (COLO 205, HEC-1-A, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.22×** | +3.3 | 0.059 | 12/48 (A549, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 5 µM |  | 1.17× | +3.3 | 0.059 | 12/48 (A498, NCI-H1792, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.50×** | +3.1 | 0.079 | 8/47 (A-172, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10509.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.554×** | -8.8 | 7e-16 | 34/46 (SW480, COLO 205, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.555×** | -8.7 | 7e-16 | 30/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.716×** | -7.0 | 5e-10 | 30/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.652×** | -6.3 | 3e-08 | 28/48 (CHP-212, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.637×** | -6.0 | 3e-07 | 25/48 (SW480, BT-474, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.643×** | -5.9 | 4e-07 | 24/44 (LoVo, RPMI-7951, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.678×** | -5.8 | 7e-07 | 23/48 (A498, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.508×** | -5.3 | 1e-05 | 26/45 (SW480, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.786×** | -5.0 | 3e-05 | 25/48 (LOX-IMVI, KATO III, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **0.719×** | -4.9 | 6e-05 | 21/45 (CFPAC-1, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.744×** | -4.4 | 6e-04 | 19/48 (Hs 766T, NCI-H1573, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.611×** | -3.8 | 0.006 | 20/44 (HOP62, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.785×** | -3.6 | 0.015 | 9/48 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.773×** | -3.4 | 0.028 | 15/47 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.803×** | -3.2 | 0.044 | 13/48 (H4, HT-29, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.663×** | -3.2 | 0.051 | 12/44 (HCT15, SNU-423, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.808×** | -3.2 | 0.053 | 16/45 (HT-29, NCI-H23, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.797×** | -3.0 | 0.086 | 9/47 (CFPAC-1, NCI-H23, …) | rises with dose |  |
| [[Clopidogrel (drug)]] 0.05 µM |  | **0.818×** | -3.0 | 0.091 | 11/48 (SK-MEL-2, H4, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10509. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 24.7 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.236× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[PF-06260933 (drug)]] 5 µM 0.130× (z -10.5) |
| [[Hs 766T (line)]] | wt | 76.8 | 0 | 3 | — | [[Triamcinolone (drug)]] 0.5 µM 0.242× (z -10.4) |
| [[A549 (line)]] | wt | 26.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -11.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 15.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0786× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0850× (z -11.3) |
| [[LoVo (line)]] | wt | 12.9 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0950× (z -12.8) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 31.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.283× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[A498 (line)]] | wt | 59.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 13.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0889× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[LOX-IMVI (line)]] | wt | 17.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.190× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H2030 (line)]] | alt | 18.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H460 (line)]] | wt | 16.1 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.319× (z -9.0) ⚠ cell-cycle shift, explains ~29% of this change |
| [[RPMI-7951 (line)]] | alt | 17.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0833× (z -11.3) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[SNU-423 (line)]] | alt | 15.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.182× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A-427 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.63 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.66 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10509), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BBOF1]] | +0.60 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[WDR73]] | +0.58 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[OSCP1]] | +0.57 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[MOK]] | +0.55 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[VPS33A]] | +0.54 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[BBS1]] | +0.54 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[C12orf4]] | +0.54 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[DNAAF4]] | +0.53 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[SETD4]] | +0.53 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[TCTN2]] | +0.53 | +0.34 / +0.62 | both halves | 1e-04 |  |
| [[DNAL1]] | +0.52 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[CCDC191]] | +0.52 | +0.49 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERRFI1]] | -0.55 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[KLHL29]] | -0.54 | -0.38 / -0.56 | both halves | 7e-05 |  |
| [[DISP3]] | -0.51 | -0.23 / -0.54 | both halves | 5e-04 |  |
| [[PTPRU]] | -0.51 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[MMP15]] | -0.50 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[HERC3]] | -0.49 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[TFRC]] | -0.48 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[RREB1]] | -0.48 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[SLC16A3]] | -0.47 | -0.30 / -0.52 | both halves | 2e-04 |  |
| [[MT1A]] | -0.47 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[P4HA1]] | -0.47 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[RAB6B]] | -0.47 | -0.46 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LPAR3]] | B | LPAR3 activity raises IQCK's level | lines that do not express LPAR3 (16) vs lines expressing it (34) | 1.17× lower at baseline in the lines without LPAR3 | 0.091 | ⚠ within organs, on part of the lines; also absent: BEX4, ADAMTS18, GAB3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 089]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.447). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-41.6, 19.9); signed map (-11.0, -17.9). **Vector** length 81.9, 16.2% of its response variance represented; |z| ≥ 3 in 944 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.4 | +2.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +0.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.2 | +4.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +4.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.3 | +4.1 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +1.6 | +3.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.6 | +1.9 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +1.5 | +3.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -9.7 | -7.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.4 | -6.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -1.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.2 | -0.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.9 | -5.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.5 | -2.3 |
|  | [[Budesonide (drug)]] 0.5 µM |  | -2.1 | -0.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.9 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | IQ motif containing K |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.3 — chr16:19,716,456-19,858,467 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC35048, FLJ36575 |
| Matched by | ensembl_id |

UniProt [Q8N0W5](https://www.uniprot.org/uniprotkb/Q8N0W5) carries no function annotation.

**Summary**, from NCBI Gene [124152](https://www.ncbi.nlm.nih.gov/gene/124152):

> This gene belongs to the IQ motif-containing family of proteins. The IQ motif serves as a binding site for different EF-hand proteins such as calmodulin. This gene was identified as a potential candidate gene for obsessive-compulsive disorder in a genome-wide association study. Alternative splicing of this gene results in multiple transcript variants. [provided by RefSeq, Feb 2015]

**Accessions** — [HGNC:28556](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28556) · Entrez [124152](https://www.ncbi.nlm.nih.gov/gene/124152) · UniProt [Q8N0W5](https://www.uniprot.org/uniprotkb/Q8N0W5) · Ensembl [ENSG00000174628](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174628)

## Data

Gene col 10509: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10509); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10509, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10509]; `tensor/DDL_lfc|DDL_z.npy` [10509]; `embed/gene_vectors.npy` [10509]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10509 or target_col == 10509). Every well: [[IQCK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IQCK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
