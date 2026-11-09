---
symbol: "CDHR3"
type: "gene"
col: 4890
ensembl_id: "ENSG00000128536"
name: "cadherin related family member 3"
location: "7q22.3"
module: 18
arm: "+"
pooled_cpm: 49.23
n_lines_expressing: 47
n_dd_up: 5
n_dd_down: 18
n_dd_up_clean: 4
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# CDHR3

*cadherin related family member 3* — 7q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 1.41× (z +4.3, q 0.007, up in 23 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.280× (z -22.9, q 0e+00, down in 41 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC88C]] (+0.55, fdr 1e-05), [[FXN]] (+0.53, fdr 1e-05), [[NUDT3]] (+0.52, fdr 3e-05); moves opposite to [[SELENOK]] (-0.54, fdr 4e-05), [[TRAFD1]] (-0.49, fdr 3e-05), [[AP1G1]] (-0.48, fdr 3e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DDAH1]] → it (grade C ⚠); 2 go from it, the strongest it → [[GOSR1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4890.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.41×** | +4.3 | 0.007 | 23/45 (KATO III, RKO, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.39×** | +4.2 | 0.007 | 27/45 (AsPC-1, SW48, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.39×** | +4.1 | 0.007 | 25/45 (KATO III, COLO 205, …) | rises with dose |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.33×** | +3.6 | 0.043 | 17/45 (KATO III, LoVo, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +3.4 | 0.070 | 21/45 (C32, BT-474, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | 1.32× | +3.2 | 0.12 | 17/45 (A498, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4890.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.280×** | -22.9 | 0e+00 | 41/44 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.344×** | -13.6 | 2e-39 | 45/45 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.422×** | -10.6 | 8e-24 | 36/45 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.457×** | -10.0 | 3e-21 | 38/44 (SW48, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.507×** | -8.7 | 6e-16 | 36/44 (LOX-IMVI, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.512×** | -8.5 | 2e-15 | 32/45 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.514×** | -8.5 | 2e-15 | 34/45 (NCI-H23, HOP62, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.516×** | -8.4 | 2e-15 | 40/45 (NCI-H460, C32, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.505×** | -7.9 | 2e-13 | 39/45 (HepG2/C3A, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.565×** | -7.3 | 2e-11 | 34/45 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.575×** | -6.8 | 6e-10 | 27/44 (NCI-H23, SNU-423, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.720×** | -5.9 | 1e-07 | 25/45 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.433×** | -5.6 | 1e-06 | 30/46 (SW48, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.686×** | -4.5 | 3e-04 | 24/45 (NCI-H460, C-33 A, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | **0.725×** | -4.1 | 0.002 | 25/44 (SW480, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.842× | -3.1 | 0.056 | 13/45 (A-427, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4890. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 49.3 | 0 | 13 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0672× (z -22.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.151× (z -22.2) |
| [[SW480 (line)]] | alt | 156 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -17.5) |
| [[MIA PaCa-2 (line)]] | alt | 69.6 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -24.6) |
| [[LOX-IMVI (line)]] | wt | 40.4 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -24.2) |
| [[NCI-H23 (line)]] | alt | 60.2 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -19.6) |
| [[HepG2_C3A (line)]] | wt | 92.2 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -12.3) |
| [[SNU-1 (line)]] | wt | 63.5 | 0 | 7 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0900× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.125× (z -13.0) |
| [[SW48 (line)]] | wt | 152 | 0 | 7 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0240× (z -25.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.231× (z -14.4) |
| [[C32 (line)]] | wt | 71.4 | 1 | 4 | [[Tucidinostat (drug)]] 5 µM 2.60× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -12.4) |
| [[HT-29 (line)]] | alt | 60.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -13.9) |
| [[RKO (line)]] | wt | 26.9 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -11.8) |
| [[HEC-1-A (line)]] | alt | 56.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -22.5) |
| [[NCI-H2030 (line)]] | alt | 50.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -20.3) |
| [[PANC-1 (line)]] | alt | 42.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -23.5) |
| [[SNU-423 (line)]] | alt | 47.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -13.9) |
| [[AsPC-1 (line)]] | alt | 45.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -16.2) |
| [[CFPAC-1 (line)]] | alt | 57.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -14.7) |
| [[HOP62 (line)]] | alt | 20.0 | 0 | 3 | — | [[Digitoxin (drug)]] 0.5 µM 0.236× (z -10.2) |
| [[Hs 766T (line)]] | wt | 82.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -14.7) |
| [[LoVo (line)]] | wt | 33.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -12.2) |
| [[LS 180 (line)]] | wt | 33.9 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -9.5) |
| [[SW1417 (line)]] | alt | 105 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -15.9) |
| [[A-427 (line)]] | wt | 51.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -17.9) |
| [[A498 (line)]] | wt | 26.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -9.8) |
| [[J82 (line)]] | alt | 45.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 78.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -13.8) |
| [[A549 (line)]] | wt | 33.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -15.6) |
| [[AN3 CA (line)]] | alt | 29.6 | 0 | 1 | — | [[Phenytoin (sodium) (drug)]] 0.05 µM 0.0643× (z -8.9) |
| [[HCT15 (line)]] | alt | 50.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.245× (z -8.6) |
| [[KATO III (line)]] | alt | 34.9 | 1 | 0 | [[Ponatinib (drug)]] 5 µM 3.23× (z +8.9) | — |
| [[NCI-H1573 (line)]] | alt | 20.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -11.2) |
| [[NCI-H661 (line)]] | alt | 48.9 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0759× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 41.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -13.0) |
| [[A-172 (line)]] | wt | 9.93 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 75.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.12 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.93 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4890), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC88C]] | +0.55 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[FXN]] | +0.53 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[NUDT3]] | +0.52 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[ADGRA3]] | +0.51 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[LINC02595]] | +0.51 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[OSBPL10]] | +0.51 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[DDAH1]] | +0.50 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[CDK6]] | +0.50 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[DLC1]] | +0.49 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[TARBP1]] | +0.49 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[G3BP1]] | +0.49 | +0.40 / +0.44 | both halves | 5e-05 |  |
| [[ZNF704]] | +0.48 | +0.46 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SELENOK]] | -0.54 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[TRAFD1]] | -0.49 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[AP1G1]] | -0.48 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[CCS]] | -0.48 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[CDC37L1]] | -0.48 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[SYNRG]] | -0.47 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[TMEM106A]] | -0.47 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[STX12]] | -0.46 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[GOLGA2]] | -0.46 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[TOX4]] | -0.46 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[TBRG1]] | -0.46 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[TMEM165]] | -0.45 | -0.40 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DDAH1]] | C | DDAH1 activity raises CDHR3's level | lines that do not express DDAH1 (3) vs lines expressing it (47) | 3.06× lower at baseline in the lines without DDAH1 | 0.046 | ⚠ few lines (3 vs 47); across organs; also absent: MMP25, KDELR3, BCL2L1; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GOSR1]] | C | CDHR3 activity raises GOSR1's level | lines that do not express CDHR3 (3) vs lines expressing it (47) | 1.28× lower at baseline in the lines without CDHR3 | 0.063 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MMP25, MPP4, ABCA10 |
| [[ZNF704]] | C | CDHR3 activity raises ZNF704's level | lines that do not express CDHR3 (3) vs lines expressing it (47) | 4.36× lower at baseline in the lines without CDHR3 | 0.092 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MMP25, MPP4, ABCA10 |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.456). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-12.6, -46.1); signed map (-8.1, -59.5). **Vector** length 80.9, 20.6% of its response variance represented; |z| ≥ 3 in 1,200 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +3.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.1 | +3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | -2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +4.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.8 | +4.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.7 | +2.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.5 | -5.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.0 | -7.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.9 | -22.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -1.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.3 | -0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -8.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.1 | +0.1 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -2.0 | -1.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.9 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | cadherin related family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.3 — chr7:105,876,796-106,036,432 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ44366, FLJ23834, CDH28 |
| Gene groups (HGNC) | Cadherin related |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZTQ4](https://www.uniprot.org/uniprotkb/Q6ZTQ4) (Cadherin-related family member 3):

> Cadherins are calcium-dependent cell adhesion proteins. They preferentially interact with themselves in a homophilic manner in connecting cells; cadherins may thus contribute to the sorting of heterogeneous cell types.; (Microbial infection) Acts as a receptor for human rhinovirus C.

**Summary**, from NCBI Gene [222256](https://www.ncbi.nlm.nih.gov/gene/222256):

> Predicted to enable beta-catenin binding activity and cadherin binding activity. Predicted to be involved in several processes, including calcium-dependent cell-cell adhesion; cell-cell adhesion mediated by cadherin; and cell-cell junction organization. Located in plasma membrane. Implicated in allergic disease (multiple); bacterial infectious disease; bronchial disease (multiple); and obstructive lung disease. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26308](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26308) · Entrez [222256](https://www.ncbi.nlm.nih.gov/gene/222256) · UniProt [Q6ZTQ4](https://www.uniprot.org/uniprotkb/Q6ZTQ4) · Ensembl [ENSG00000128536](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128536)

## Data

Gene col 4890: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4890); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4890, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4890]; `tensor/DDL_lfc|DDL_z.npy` [4890]; `embed/gene_vectors.npy` [4890]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4890 or target_col == 4890). Every well: [[CDHR3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDHR3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
