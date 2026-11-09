---
symbol: "SDHAP2"
type: "gene"
col: 13277
ensembl_id: "ENSG00000215837"
name: "SDHA pseudogene 2"
location: "3q29"
module: 3
arm: "+"
pooled_cpm: 37.92
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 27
n_dd_up_clean: 1
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 7
direction_downstream: 1
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# SDHAP2

*SDHA pseudogene 2* — 3q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 1.30× (z +4.1, q 0.019, up in 21 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.313× (z -18.4, q 0e+00, down in 43 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SDHAP1]] (+0.96, fdr 7e-06), [[SDHAP4-1]] (+0.88, fdr 7e-06), [[TMEM120B]] (+0.78, fdr 7e-06); moves opposite to [[HNRNPK]] (-0.81, fdr 7e-06), [[ZXDB]] (-0.75, fdr 7e-06), [[KRT8P12]] (-0.74, fdr 7e-06).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[EREG]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SDHAP1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13277.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.30×** | +4.1 | 0.019 | 21/48 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13277.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.313×** | -18.4 | 0e+00 | 43/46 (LOX-IMVI, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.321×** | -18.0 | 0e+00 | 39/44 (NCI-H2347, J82, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.448×** | -17.9 | 0e+00 | 39/47 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.373×** | -15.0 | 0e+00 | 45/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.404×** | -13.2 | 5e-38 | 30/40 (NCI-H2030, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.469×** | -12.0 | 6e-31 | 43/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.468×** | -11.5 | 7e-29 | 28/36 (J82, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.635×** | -7.2 | 6e-11 | 33/48 (A-172, HS-578T, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.725×** | -7.1 | 6e-11 | 27/47 (HS-578T, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.766×** | -5.9 | 2e-07 | 27/48 (HS-578T, CFPAC-1, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.726×** | -4.9 | 6e-05 | 28/48 (HS-578T, NCI-H2347, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.827×** | -4.2 | 0.001 | 19/48 (SNU-1, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Berbamine (drug)]] 0.05 µM |  | **0.779×** | -3.9 | 0.004 | 18/48 (A549, SW1417, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **0.781×** | -3.9 | 0.004 | 24/45 (Panc 03.27, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.775×** | -3.9 | 0.004 | 22/48 (A-172, SK-MEL-2, …) | top dose only | position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.784×** | -3.8 | 0.005 | 17/48 (SW 900, SW1417, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.789×** | -3.7 | 0.007 | 15/48 (COLO 205, NCI-H1573, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.791×** | -3.7 | 0.007 | 18/48 (A-172, HEC-1-A, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.803×** | -3.4 | 0.016 | 16/48 (SW480, SW 900, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.815×** | -3.2 | 0.035 | 15/48 (SW1417, NCI-H661, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13277. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 53.6 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -26.3) |
| [[HS-578T (line)]] | alt | 73.9 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.103× (z -20.3) |
| [[NCI-H2347 (line)]] | alt | 76.9 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -22.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.230× (z -21.9) |
| [[CFPAC-1 (line)]] | alt | 46.7 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -21.3) |
| [[HOP62 (line)]] | alt | 47.3 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -21.4) |
| [[Panc 03.27 (line)]] | alt | 55.8 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0972× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.240× (z -16.9) |
| [[A498 (line)]] | wt | 31.8 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.178× (z -14.7) |
| [[HEC-1-A (line)]] | alt | 78.9 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.323× (z -15.9) |
| [[J82 (line)]] | alt | 52.9 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0762× (z -22.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.428× (z -10.8) |
| [[A549 (line)]] | wt | 31.7 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.254× (z -10.3) |
| [[hTERT-HPNE (line)]] | wt | 39.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -15.0) |
| [[LS 180 (line)]] | wt | 40.3 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.158× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.408× (z -10.7) |
| [[SNU-1 (line)]] | wt | 55.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -17.5) |
| [[SNU-423 (line)]] | alt | 44.4 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.316× (z -8.7) |
| [[LoVo (line)]] | wt | 50.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.199× (z -15.2) |
| [[NCI-H1573 (line)]] | alt | 21.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0547× (z -19.8) |
| [[RPMI-7951 (line)]] | alt | 50.9 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.276× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 30.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -17.6) |
| [[SW 900 (line)]] | alt | 30.9 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.179× (z -10.9) |
| [[A-427 (line)]] | wt | 14.4 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.163× (z -9.6) |
| [[AsPC-1 (line)]] | alt | 36.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.134× (z -16.7) |
| [[C32 (line)]] | wt | 31.8 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.180× (z -10.4) |
| [[HCT15 (line)]] | alt | 40.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.141× (z -11.5) |
| [[Hs 766T (line)]] | wt | 25.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -13.1) |
| [[KATO III (line)]] | alt | 41.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.204× (z -11.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 40.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.280× (z -10.3) |
| [[NCI-H2030 (line)]] | alt | 22.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0780× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.449× (z -8.6) |
| [[SW480 (line)]] | alt | 26.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -10.7) |
| [[COLO 205 (line)]] | alt | 100 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -10.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 38.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -10.6) |
| [[LOX-IMVI (line)]] | wt | 18.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0377× (z -21.8) |
| [[NCI-H460 (line)]] | wt | 20.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -11.3) |
| [[RKO (line)]] | wt | 14.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0904× (z -12.3) |
| [[SHP-77 (line)]] | alt | 18.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -9.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 35.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.207× (z -11.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13277), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAP1]] | +0.96 | +0.96 / +0.93 | both halves | 7e-06 |  |
| [[SDHAP4-1]] | +0.88 | +0.90 / +0.90 | both halves | 7e-06 |  |
| [[TMEM120B]] | +0.78 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[IER3IP1]] | +0.76 | +0.79 / +0.71 | both halves | 7e-06 |  |
| [[CBFA2T2]] | +0.76 | +0.81 / +0.62 | both halves | 7e-06 |  |
| [[GMCL1]] | +0.76 | +0.81 / +0.59 | both halves | 7e-06 |  |
| [[MYPOP]] | +0.76 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[LCMT1]] | +0.76 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[ATP5MJ]] | +0.74 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[CCZ1B]] | +0.74 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[SDHAP1-1]] | +0.74 | +0.61 / +0.73 | both halves | 7e-06 |  |
| [[RAB40C]] | +0.73 | +0.74 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPK]] | -0.81 | -0.69 / -0.74 | both halves | 7e-06 |  |
| [[ZXDB]] | -0.75 | -0.72 / -0.65 | both halves | 7e-06 |  |
| [[KRT8P12]] | -0.74 | -0.74 / -0.65 | both halves | 7e-06 |  |
| [[TASOR]] | -0.73 | -0.76 / -0.62 | both halves | 7e-06 |  |
| [[IL6ST]] | -0.72 | -0.65 / -0.67 | both halves | 7e-06 |  |
| [[CPSF2]] | -0.71 | -0.71 / -0.56 | both halves | 1e-05 |  |
| [[ZNF655]] | -0.71 | -0.71 / -0.54 | both halves | 1e-05 |  |
| [[EIF4G2]] | -0.71 | -0.67 / -0.57 | both halves | 1e-05 |  |
| [[TRIM44]] | -0.70 | -0.70 / -0.61 | both halves | 7e-06 |  |
| [[LIG4]] | -0.70 | -0.71 / -0.61 | both halves | 7e-06 |  |
| [[ST7L]] | -0.69 | -0.74 / -0.48 | both halves | 2e-05 |  |
| [[LEKR1]] | -0.69 | -0.72 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EREG]] | B | EREG activity raises SDHAP2's level | lines that do not express EREG (26) vs lines expressing it (24) | 1.35× lower at baseline in the lines without EREG | 0.022 | ⚠ within organs, on part of the lines; also absent: DPP4, IL20RA, HS3ST1 |
| [[TOP2A]] | B | TOP2A activity raises SDHAP2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PARVA]] | B | PARVA activity raises SDHAP2's level | lines that do not express PARVA (6) vs lines expressing it (44) | 1.75× lower at baseline in the lines without PARVA | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000284969 |
| [[ME3]] | B | ME3 activity raises SDHAP2's level | lines that do not express ME3 (13) vs lines expressing it (37) | 1.40× lower at baseline in the lines without ME3 | 0.062 | ⚠ within organs, on part of the lines; also absent: PLAAT3 |
| [[TSPAN33]] | B | TSPAN33 activity lowers SDHAP2's level | lines that do not express TSPAN33 (12) vs lines expressing it (38) | 1.30× higher at baseline in the lines without TSPAN33 | 0.088 | ⚠ within organs, on part of the lines; also absent: SRCIN1, CRACD, GNAZ; maybe low, not absent |
| [[DHRS1]] | C | DHRS1's natural level strengthens SDHAP2's drug response | DHRS1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.69, reverse -0.09; direction not clear | 0.017 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[SDHAP4-1]] | C | SDHAP4-1's natural level strengthens SDHAP2's drug response | SDHAP4-1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.25; direction not clear | 0.073 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SDHAP1]] | C | SDHAP2's natural level strengthens SDHAP1's drug response | SDHAP2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.51; direction not clear | 0.050 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.802). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (0.3, -14.6); signed map (-37.9, 1.1). **Vector** length 116, 31.2% of its response variance represented; |z| ≥ 3 in 972 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +6.6 | +4.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.6 | +1.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.5 | +2.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +1.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.0 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +2.5 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.7 | +1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | +2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | +1.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -9.1 | -12.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.0 | -18.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -8.4 | -15.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.1 | -17.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.2 | -7.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.9 | -5.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.5 | -3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.2 | -4.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -3.0 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | SDHA pseudogene 2 |
| Locus type | pseudogene |
| Location | 3q29 — chr3:195,658,096-195,685,904 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | ; previously SDHAL2, SDHALP2 |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27408](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27408) · Entrez [727956](https://www.ncbi.nlm.nih.gov/gene/727956) · Ensembl [ENSG00000215837](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000215837)

## Data

Gene col 13277: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13277); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13277, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13277]; `tensor/DDL_lfc|DDL_z.npy` [13277]; `embed/gene_vectors.npy` [13277]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13277 or target_col == 13277). Every well: [[SDHAP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SDHAP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
