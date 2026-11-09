---
symbol: "TMEM106A"
type: "gene"
col: 11602
ensembl_id: "ENSG00000184988"
name: "transmembrane protein 106A"
location: "17q21.31"
module: 4
arm: "-"
pooled_cpm: 14.77
n_lines_expressing: 45
n_dd_up: 3
n_dd_down: 23
n_dd_up_clean: 3
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 4
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# TMEM106A

*transmembrane protein 106A* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.67× (z +9.7, q 2e-19, up in 23 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.441× (z -10.2, q 1e-21, down in 21 of 27 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.309× (z -8.3, q 2e-14, down in 30 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SELENOK]] (+0.68, fdr 7e-06), [[INAFM1]] (+0.68, fdr 7e-06), [[STX5-DT]] (+0.67, fdr 7e-06); moves opposite to [[PRKDC]] (-0.72, fdr 7e-06), [[MRPL42]] (-0.66, fdr 8e-06), [[RPE]] (-0.66, fdr 7e-06).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LAMB1]] → it (grade B ⚠); 4 go from it, the strongest it → [[TULP3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11602.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.67×** | +9.7 | 2e-19 | 23/39 (CFPAC-1, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +3.8 | 0.046 | 15/41 (LoVo, NCI-H23, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.31×** | +3.7 | 0.046 | 5/41 (SK-MEL-2, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11602.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.441×** | -10.2 | 1e-21 | 21/27 (LoVo, A-172, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.513×** | -9.0 | 6e-17 | 22/31 (A-172, A498, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.309×** | -8.3 | 2e-14 | 30/40 (KATO III, A-172, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.359×** | -7.2 | 7e-11 | 25/39 (A-172, Hs 766T, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.614×** | -6.6 | 5e-09 | 25/43 (HS-578T, A-172, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.653×** | -5.5 | 3e-06 | 18/23 (HS-578T, NCI-H1792, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.670×** | -5.4 | 5e-06 | 21/42 (LOX-IMVI, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.699×** | -4.8 | 9e-05 | 17/41 (HS-578T, A-172, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.733×** | -4.0 | 0.003 | 19/40 (NCI-H23, NCI-H2030, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.744×** | -4.0 | 0.004 | 14/40 (hTERT-HPNE, NCI-H460, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.757×** | -3.8 | 0.009 | 14/43 (HS-578T, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.758×** | -3.7 | 0.009 | 18/43 (HS-578T, H4, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.760×** | -3.7 | 0.009 | 16/42 (COLO 205, KATO III, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.774×** | -3.5 | 0.022 | 15/41 (H4, A-172, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.778×** | -3.4 | 0.026 | 13/42 (NCI-H2347, A498, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.769×** | -3.3 | 0.035 | 12/37 (LoVo, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.793×** | -3.1 | 0.053 | 7/42 (MIA PaCa-2, SW 1088, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.642×** | -3.1 | 0.053 | 11/40 (RKO, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Busulfan (drug)]] 5 µM |  | 0.852× | -3.0 | 0.065 | 9/42 (SNU-1, LS 180, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.801×** | -3.0 | 0.066 | 15/40 (A549, LoVo, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.856× | -3.0 | 0.071 | 14/43 (HS-578T, A-172, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 0.857× | -2.9 | 0.076 | 10/42 (NCI-H1573, NCI-H23, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11602. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 21.4 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0674× (z -20.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0739× (z -10.3) |
| [[HS-578T (line)]] | alt | 28.6 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[A498 (line)]] | wt | 34.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.154× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[A549 (line)]] | wt | 24.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[AsPC-1 (line)]] | alt | 19.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.193× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[CFPAC-1 (line)]] | alt | 23.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.53× (z +17.1) | [[Dinaciclib (drug)]] 0.05 µM 0.230× (z -9.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 29.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0753× (z -12.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 23.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.264× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[KATO III (line)]] | alt | 16.0 | 0 | 2 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0217× (z -12.4) |
| [[NCI-H2347 (line)]] | alt | 23.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.273× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SK-MEL-2 (line)]] | alt | 21.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +9.4) | [[Selinexor (drug)]] 5 µM 0.323× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 13.9 | 0 | 1 | — | [[Radotinib (drug)]] 5 µM 0.0909× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 5.94 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0901× (z -10.4) ⚠ toxic; cell-cycle shift, explains ~39% of this change |
| [[HT-29 (line)]] | alt | 12.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[hTERT-HPNE (line)]] | wt | 33.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0647× (z -15.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 24.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0937× (z -16.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 20.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.128× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[NCI-H23 (line)]] | alt | 10.00 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +9.8) | — |
| [[NCI-H460 (line)]] | wt | 14.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.178× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[RPMI-7951 (line)]] | alt | 19.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.136× (z -9.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.07 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.01 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.66 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 10.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11602), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SELENOK]] | +0.68 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[INAFM1]] | +0.68 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[STX5-DT]] | +0.67 | +0.60 / +0.74 | both halves | 7e-06 |  |
| [[APBA3]] | +0.66 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[SELENOM]] | +0.65 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[FAM177A1]] | +0.63 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[GOLGA2]] | +0.63 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[ZNF547]] | +0.61 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[AKAP17A]] | +0.61 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[ZMYM5]] | +0.61 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[PLPP5]] | +0.61 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[STX5]] | +0.61 | +0.58 / +0.62 | both halves | 8e-06 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKDC]] | -0.72 | -0.69 / -0.70 | both halves | 7e-06 |  |
| [[MRPL42]] | -0.66 | -0.58 / -0.66 | both halves | 8e-06 |  |
| [[RPE]] | -0.66 | -0.63 / -0.67 | both halves | 7e-06 |  |
| [[ATIC]] | -0.65 | -0.55 / -0.72 | both halves | 1e-05 |  |
| [[TMEM33]] | -0.64 | -0.60 / -0.65 | both halves | 7e-06 |  |
| [[RUVBL1]] | -0.64 | -0.60 / -0.64 | both halves | 7e-06 |  |
| [[GOT2]] | -0.63 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[MTHFD1]] | -0.61 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[NUP155]] | -0.61 | -0.62 / -0.59 | both halves | 7e-06 |  |
| [[TUBGCP3]] | -0.61 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[G3BP1]] | -0.61 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[TMX3]] | -0.60 | -0.61 / -0.58 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAMB1]] | B | LAMB1 activity raises TMEM106A's level | lines that do not express LAMB1 (7) vs lines expressing it (43) | 2.84× lower at baseline in the lines without LAMB1 | 0.013 | ⚠ within organs, on part of the lines; also absent: TGFBR2, SDC4, VDR |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TULP3]] | B | TMEM106A activity raises TULP3's level | lines that do not express TMEM106A (5) vs lines expressing it (45) | 1.47× lower at baseline in the lines without TMEM106A | 0.060 | ⚠ within organs, on part of the lines; maybe low, not absent; its own permutation p |
| [[PPP5C]] | B | TMEM106A activity lowers PPP5C's level | lines that do not express TMEM106A (5) vs lines expressing it (45) | 1.68× higher at baseline in the lines without TMEM106A | 0.070 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[BET1]] | B | TMEM106A activity raises BET1's level | lines that do not express TMEM106A (5) vs lines expressing it (45) | 1.76× lower at baseline in the lines without TMEM106A | 0.089 | ⚠ within organs, on part of the lines; maybe low, not absent; its own permutation p |
| [[NPIPB14P]] | B | TMEM106A activity raises NPIPB14P's level | lines that do not express TMEM106A (5) vs lines expressing it (45) | 1.32× lower at baseline in the lines without TMEM106A | 0.089 | ⚠ within organs, on part of the lines; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.670). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-22.6, -34.3); signed map (-11.4, -0.1). **Vector** length 95.9, 22.1% of its response variance represented; |z| ≥ 3 in 877 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.0 | +9.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | +1.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.4 | +1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +3.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.9 | +3.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +2.0 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.9 | +2.1 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.8 | +3.0 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.8 | -8.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.8 | -7.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.8 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -3.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.0 | -10.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.6 | -3.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.5 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 106A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:43,211,835-43,220,041 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC20235 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96A25](https://www.uniprot.org/uniprotkb/Q96A25) (Transmembrane protein 106A):

> Activates macrophages and polarizes them into M1-like macrophages through the activation of the MAPK and NF-kappaB signaling pathway. Upon activation, up-regulates the expression of CD80, CD86, CD69 and MHC II on macrophages, and induces the release of pro-inflammatory cytokines such as TNF, IL1B, IL6, CCL2 and nitric oxide (By similarity). May play a role in inhibition of proliferation and migration.

**Summary**, from NCBI Gene [113277](https://www.ncbi.nlm.nih.gov/gene/113277):

> Predicted to be involved in several processes, including positive regulation of MHC class II biosynthetic process; positive regulation of cytokine production; and positive regulation of intracellular signal transduction. Predicted to be located in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28288](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28288) · Entrez [113277](https://www.ncbi.nlm.nih.gov/gene/113277) · UniProt [Q96A25](https://www.uniprot.org/uniprotkb/Q96A25) · Ensembl [ENSG00000184988](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184988)

## Data

Gene col 11602: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11602); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11602, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11602]; `tensor/DDL_lfc|DDL_z.npy` [11602]; `embed/gene_vectors.npy` [11602]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11602 or target_col == 11602). Every well: [[TMEM106A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM106A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
