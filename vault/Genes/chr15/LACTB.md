---
symbol: "LACTB"
type: "gene"
col: 2387
ensembl_id: "ENSG00000103642"
name: "lactamase beta"
location: "15q22.2"
module: 59
arm: "+"
pooled_cpm: 43.49
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# LACTB

*lactamase beta* — 15q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.31× (z +15.2, q 0e+00, up in 43 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 0.248×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NEURL3]] (+0.67, fdr 7e-06), [[NINJ1]] (+0.66, fdr 7e-06), [[RRAGC]] (+0.65, fdr 1e-05); moves opposite to [[TRRAP]] (-0.65, fdr 7e-06), [[NUP155]] (-0.65, fdr 1e-05), [[EFTUD2]] (-0.63, fdr 7e-06).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[IL32]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2387.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.31×** | +15.2 | 0e+00 | 43/47 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.77×** | +7.3 | 6e-11 | 29/47 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.80×** | +7.3 | 6e-11 | 35/48 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +5.5 | 4e-06 | 34/47 (SW 900, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.9 | 1e-04 | 26/48 (LoVo, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.020 | 19/49 (CFPAC-1, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.33×** | +3.6 | 0.022 | 25/48 (SW480, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.36×** | +3.5 | 0.033 | 24/48 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Radotinib (drug)]] 5 µM |  | 1.19× | +3.1 | 0.10 | 16/48 (HT-29, hTERT-HPNE, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +3.0 | 0.13 | 16/48 (H4, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | 1.26× | +3.0 | 0.13 | 22/48 (SW480, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2387.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 0.248×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 0.05 µM |  | 0.757× | -3.4 | 0.32 | 22/47 (RKO, SW480, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.836× | -3.3 | 0.32 | 18/48 (SW 900, A498, …) | top dose only |  |
| [[Clonidine (hydrochloride) (drug)]] 5 µM |  | 0.842× | -3.1 | 0.33 | 11/48 (SK-MEL-2, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2387. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 61.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +18.5) | — |
| [[HEC-1-A (line)]] | alt | 30.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +15.6) | [[Dinaciclib (drug)]] 5 µM 0.248× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 68.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +16.6) | — |
| [[LoVo (line)]] | wt | 43.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +11.7) | — |
| [[PANC-1 (line)]] | alt | 48.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.29× (z +26.5) | — |
| [[A498 (line)]] | wt | 61.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +13.1) | — |
| [[HS-578T (line)]] | alt | 52.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +15.9) | — |
| [[A549 (line)]] | wt | 89.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +10.4) | — |
| [[C32 (line)]] | wt | 49.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +10.4) | — |
| [[CFPAC-1 (line)]] | alt | 56.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +13.9) | — |
| [[H4 (line)]] | wt | 32.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.05× (z +13.8) | — |
| [[HepG2_C3A (line)]] | wt | 36.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +10.5) | — |
| [[HOP62 (line)]] | alt | 46.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +11.7) | — |
| [[HT-29 (line)]] | alt | 27.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +8.5) | — |
| [[J82 (line)]] | alt | 60.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +17.4) | — |
| [[KATO III (line)]] | alt | 26.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +10.1) | — |
| [[NCI-H1792 (line)]] | alt | 84.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +11.1) | — |
| [[NCI-H2347 (line)]] | alt | 51.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +9.0) | — |
| [[RPMI-7951 (line)]] | alt | 67.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +12.8) | — |
| [[SK-MEL-2 (line)]] | alt | 54.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +14.4) | — |
| [[SNU-1 (line)]] | wt | 34.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +9.3) | — |
| [[SNU-423 (line)]] | alt | 66.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +17.9) | — |
| [[SW 900 (line)]] | alt | 38.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +11.9) | — |
| [[SW48 (line)]] | wt | 21.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +10.4) | — |
| [[SW480 (line)]] | alt | 20.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +8.7) | — |
| [[A-427 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 51.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 92.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2387), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEURL3]] | +0.67 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[NINJ1]] | +0.66 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[RRAGC]] | +0.65 | +0.57 / +0.72 | both halves | 1e-05 |  |
| [[OPTN]] | +0.65 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[SLC41A2]] | +0.65 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[SNHG32]] | +0.63 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[PIM3]] | +0.62 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[KMT2A]] | +0.61 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[NKAP]] | +0.60 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[TIPRL]] | +0.60 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[NBPF19]] | +0.59 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[PPP3CC]] | +0.59 | +0.40 / +0.56 | both halves | 5e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRRAP]] | -0.65 | -0.62 / -0.66 | both halves | 7e-06 |  |
| [[NUP155]] | -0.65 | -0.55 / -0.69 | both halves | 1e-05 |  |
| [[EFTUD2]] | -0.63 | -0.61 / -0.64 | both halves | 7e-06 |  |
| [[ATP2A2]] | -0.62 | -0.58 / -0.65 | both halves | 7e-06 |  |
| [[TMX3]] | -0.59 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[RTEL1]] | -0.58 | -0.57 / -0.59 | both halves | 9e-06 |  |
| [[XRCC5]] | -0.58 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[EMC1]] | -0.57 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[POLA1]] | -0.57 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[TFDP1]] | -0.57 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[HNRNPAB]] | -0.57 | -0.40 / -0.57 | both halves | 4e-05 |  |
| [[PSMD1]] | -0.57 | -0.48 / -0.61 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL32]] | B | IL32 activity raises LACTB's level | lines that do not express IL32 (18) vs lines expressing it (32) | 1.48× lower at baseline in the lines without IL32 | 0.008 | ⚠ within organs, on part of the lines; also absent: PODXL, APOL1, F3 |
| [[C15orf48]] | B | C15orf48 activity raises LACTB's level | lines that do not express C15orf48 (25) vs lines expressing it (25) | 1.60× lower at baseline in the lines without C15orf48 | 0.016 | ⚠ within organs, on part of the lines; also absent: ZNF229, HMGN2P46, RHCG |
| [[ANKRD33B]] | B | ANKRD33B activity raises LACTB's level | lines that do not express ANKRD33B (15) vs lines expressing it (35) | 1.56× lower at baseline in the lines without ANKRD33B | 0.067 | ⚠ within organs, on part of the lines; also absent: JCAD, FAT4, ARHGAP22 |
| [[SELENOM]] | B | SELENOM activity raises LACTB's level | lines that do not express SELENOM (14) vs lines expressing it (36) | 1.35× lower at baseline in the lines without SELENOM | 0.077 | ⚠ within organs, on part of the lines; also absent: PNMA2, C3orf18, RFPL1S |
| [[LRRC49]] | B | LRRC49 activity raises LACTB's level | lines that do not express LRRC49 (11) vs lines expressing it (39) | 1.60× lower at baseline in the lines without LRRC49 | 0.091 | ⚠ within organs, on part of the lines; also absent: LARP6, HEG1, FJX1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.637). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-0.6, -37.6); signed map (-9.1, 13.3). **Vector** length 112, 31.7% of its response variance represented; |z| ≥ 3 in 689 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.5 | +15.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.5 | +7.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.3 | +7.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.4 | +3.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +2.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.3 | +3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.7 | +1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.6 | +2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +2.5 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -6.9 | -1.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.8 | -1.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.6 | +0.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.5 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -2.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.6 | -3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | -0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | +0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | +1.7 |

## What is on record

|  |  |
|---|---|
| Name | lactamase beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.2 — chr15:63,121,833-63,142,061 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14902; previously MRPL56 |
| Gene groups (HGNC) | Serine beta lactamase family |
| Matched by | ensembl_id |

**Function**, from UniProt [P83111](https://www.uniprot.org/uniprotkb/P83111) (Serine beta-lactamase-like protein LACTB, mitochondrial):

> Mitochondrial serine protease that acts as a regulator of mitochondrial lipid metabolism. Acts by decreasing protein levels of PISD, a mitochondrial enzyme that converts phosphatidylserine (PtdSer) to phosphatidylethanolamine (PtdEtn), thereby affecting mitochondrial lipid metabolism. It is unclear whether it acts directly by mediating proteolysis of PISD or by mediating proteolysis of another lipid metabolism protein. Acts as a tumor suppressor that has the ability to inhibit proliferation of …

**Summary**, from NCBI Gene [114294](https://www.ncbi.nlm.nih.gov/gene/114294):

> This gene encodes a mitochondrially-localized protein that has sequence similarity to prokaryotic beta-lactamases. Many of the residues responsible for beta-lactamase activity are not conserved in this protein, suggesting it may have a different enzymatic function. Increased expression of the related mouse gene was found to be associated with obesity. Alternative splicing results in multiple transcript variants encoding different protein isoforms. [provided by RefSeq, Dec 2013]

**Accessions** — [HGNC:16468](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16468) · Entrez [114294](https://www.ncbi.nlm.nih.gov/gene/114294) · UniProt [P83111](https://www.uniprot.org/uniprotkb/P83111) · Ensembl [ENSG00000103642](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103642)

## Data

Gene col 2387: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2387); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2387, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2387]; `tensor/DDL_lfc|DDL_z.npy` [2387]; `embed/gene_vectors.npy` [2387]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2387 or target_col == 2387). Every well: [[LACTB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LACTB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
