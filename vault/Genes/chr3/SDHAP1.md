---
symbol: "SDHAP1"
type: "gene"
col: 11686
ensembl_id: "ENSG00000185485"
name: "SDHA pseudogene 1"
location: "3q29"
module: 40
arm: "+"
pooled_cpm: 22.55
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 22
n_dd_up_clean: 0
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# SDHAP1

*SDHA pseudogene 1* — 3q29

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.355× (z -14.5, q 1e-44, down in 41 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SDHAP2]] (+0.96, fdr 7e-06), [[SDHAP4-1]] (+0.86, fdr 7e-06), [[SDHAP4]] (+0.83, fdr 7e-06); moves opposite to [[ERCC6L2]] (-0.75, fdr 7e-06), [[HNRNPK]] (-0.73, fdr 7e-06), [[ST7L]] (-0.73, fdr 1e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11686.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | 1.27× | +3.3 | 0.34 | 15/48 (PANC-1, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | 1.26× | +3.2 | 0.34 | 10/48 (SW480, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11686.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.355×** | -14.5 | 1e-44 | 41/46 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.356×** | -14.4 | 1e-44 | 35/39 (A-172, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.483×** | -13.3 | 8e-38 | 39/47 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.390×** | -12.6 | 2e-34 | 39/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.475×** | -10.4 | 3e-23 | 42/48 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.501×** | -9.3 | 2e-18 | 26/32 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.599×** | -7.2 | 7e-11 | 34/48 (A-172, HS-578T, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.588×** | -6.8 | 5e-10 | 24/34 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.757×** | -5.1 | 2e-05 | 26/47 (NCI-H2347, HS-578T, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.711×** | -4.6 | 3e-04 | 23/48 (A-172, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.729×** | -4.2 | 0.001 | 20/46 (SK-MEL-2, HS-578T, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Filgotinib (drug)]] 5 µM |  | **0.741×** | -4.2 | 0.001 | 17/48 (COLO 205, LoVo, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.744×** | -4.1 | 0.002 | 21/48 (RKO, KATO III, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.743×** | -4.0 | 0.003 | 18/48 (HCT15, NCI-H2347, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.772×** | -3.6 | 0.011 | 15/48 (SW 1271, HS-578T, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.757×** | -3.6 | 0.011 | 15/46 (RPMI-7951, hTERT-HPNE, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.827×** | -3.6 | 0.011 | 17/48 (NCI-H2347, A-172, …) | top dose only |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.797×** | -3.2 | 0.046 | 13/48 (MIA PaCa-2, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11686. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 27.6 | 0 | 9 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0464× (z -22.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.109× (z -21.2) |
| [[NCI-H2347 (line)]] | alt | 38.8 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.147× (z -16.4) |
| [[CFPAC-1 (line)]] | alt | 26.5 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.225× (z -13.4) |
| [[HOP62 (line)]] | alt | 39.3 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.120× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.228× (z -15.6) |
| [[HS-578T (line)]] | alt | 36.3 | 0 | 6 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.325× (z -11.1) |
| [[A498 (line)]] | wt | 23.5 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.143× (z -14.1) |
| [[AsPC-1 (line)]] | alt | 20.8 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0978× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.245× (z -13.4) |
| [[H4 (line)]] | wt | 37.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0751× (z -12.4) |
| [[J82 (line)]] | alt | 32.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 32.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.237× (z -9.8) |
| [[SW 900 (line)]] | alt | 30.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0316× (z -20.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.229× (z -8.9) |
| [[A549 (line)]] | wt | 15.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -9.5) |
| [[COLO 205 (line)]] | alt | 59.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.236× (z -9.8) |
| [[hTERT-HPNE (line)]] | wt | 21.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.124× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 17.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.136× (z -12.5) |
| [[PANC-1 (line)]] | alt | 13.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -14.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 16.8 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0750× (z -13.0) |
| [[SNU-423 (line)]] | alt | 18.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.141× (z -11.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 37.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -11.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 14.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.191× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 22.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0338× (z -20.1) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 32.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -10.6) |
| [[SW480 (line)]] | alt | 27.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -11.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.98 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11686), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAP2]] | +0.96 | +0.96 / +0.93 | both halves | 7e-06 |  |
| [[SDHAP4-1]] | +0.86 | +0.89 / +0.85 | both halves | 7e-06 |  |
| [[SDHAP4]] | +0.83 | +0.88 / +0.75 | both halves | 7e-06 |  |
| [[IER3IP1]] | +0.83 | +0.85 / +0.74 | both halves | 7e-06 |  |
| [[GMCL1]] | +0.79 | +0.85 / +0.59 | both halves | 7e-06 |  |
| [[HSPB11]] | +0.79 | +0.78 / +0.69 | both halves | 7e-06 |  |
| [[MYPOP]] | +0.79 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[SDHAP1-1]] | +0.76 | +0.64 / +0.79 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[MMS19]] | +0.75 | +0.78 / +0.62 | both halves | 7e-06 |  |
| [[TMEM120B]] | +0.75 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[SEC11A]] | +0.75 | +0.76 / +0.64 | both halves | 7e-06 |  |
| [[PMS2P3-1]] | +0.74 | +0.80 / +0.65 | both halves | 7e-06 |  |
| [[LCMT1]] | +0.74 | +0.73 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERCC6L2]] | -0.75 | -0.77 / -0.60 | both halves | 7e-06 |  |
| [[HNRNPK]] | -0.73 | -0.58 / -0.66 | both halves | 7e-06 |  |
| [[ST7L]] | -0.73 | -0.79 / -0.51 | both halves | 1e-05 |  |
| [[CPSF2]] | -0.72 | -0.72 / -0.55 | both halves | 1e-05 |  |
| [[TASOR]] | -0.71 | -0.73 / -0.58 | both halves | 7e-06 |  |
| [[LZIC]] | -0.71 | -0.77 / -0.53 | both halves | 1e-05 |  |
| [[LEKR1]] | -0.70 | -0.75 / -0.49 | both halves | 1e-05 |  |
| [[CACNA2D1]] | -0.70 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[ZXDB]] | -0.70 | -0.68 / -0.55 | both halves | 1e-05 |  |
| [[LIG4]] | -0.70 | -0.73 / -0.55 | both halves | 1e-05 |  |
| [[ZNF462]] | -0.69 | -0.65 / -0.59 | both halves | 7e-06 |  |
| [[SKIL]] | -0.69 | -0.65 / -0.64 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 4, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SDHAP1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ZNF141]] | B | ZNF141 activity raises SDHAP1's level | lines that do not express ZNF141 (12) vs lines expressing it (38) | 1.26× lower at baseline in the lines without ZNF141 | 0.055 | ⚠ within organs, on part of the lines; also absent: SLC1A3 |
| [[HCG11]] | B | HCG11 activity raises SDHAP1's level | lines that do not express HCG11 (21) vs lines expressing it (29) | 1.14× lower at baseline in the lines without HCG11 | 0.061 | ⚠ within organs, on part of the lines; also absent: HEYL, GAL, PDLIM4 |
| [[TRIP6]] | B | TRIP6 activity raises SDHAP1's level | lines that do not express TRIP6 (12) vs lines expressing it (38) | 1.58× lower at baseline in the lines without TRIP6 | 0.083 | ⚠ within organs, on part of the lines; also absent: EFNB2, PLAC4 |
| [[SDHAP4-1]] | C | SDHAP4-1's natural level strengthens SDHAP1's drug response | SDHAP4-1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.78, reverse +0.29; direction not clear | 6e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[SDHAP1-1]] | C | SDHAP1-1's natural level strengthens SDHAP1's drug response | SDHAP1-1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.75, reverse -0.03; direction clear | 0.003 | ⚠ tissue can mimic it; precision caveat |
| [[SDHAP4]] | C | SDHAP4's natural level strengthens SDHAP1's drug response | SDHAP4's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.71, reverse +0.35; direction not clear | 0.009 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[SDHAP2]] | C | SDHAP2's natural level strengthens SDHAP1's drug response | SDHAP2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.51; direction not clear | 0.050 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.866). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-0.3, -14.8); signed map (-38.4, 0.7). **Vector** length 99.9, 23.4% of its response variance represented; |z| ≥ 3 in 902 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +5.2 | +3.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +2.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.5 | +3.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +1.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.3 | +0.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +1.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.8 | +0.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.7 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +0.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.6 | +0.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.4 | -14.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -8.3 | -12.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.7 | -10.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.7 | -13.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.6 | -7.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.7 | -3.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.0 | -3.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.6 | -4.0 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.5 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | SDHA pseudogene 1 |
| Locus type | pseudogene |
| Location | 3q29 — chr3:195,963,335-195,990,258 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | ; previously SDHAL1, SDHALP1 |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:32455](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32455) · Entrez [255812](https://www.ncbi.nlm.nih.gov/gene/255812) · Ensembl [ENSG00000185485](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185485)

## Data

Gene col 11686: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11686); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11686, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11686]; `tensor/DDL_lfc|DDL_z.npy` [11686]; `embed/gene_vectors.npy` [11686]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11686 or target_col == 11686). Every well: [[SDHAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SDHAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
