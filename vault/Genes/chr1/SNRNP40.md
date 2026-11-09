---
symbol: "SNRNP40"
type: "gene"
col: 691
ensembl_id: "ENSG00000060688"
name: "small nuclear ribonucleoprotein U5 subunit 40"
location: "1p35.2"
module: 6
arm: "+"
pooled_cpm: 39.57
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 5
n_dd_up_clean: 13
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# SNRNP40

*small nuclear ribonucleoprotein U5 subunit 40* — 1p35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.63× (z +9.8, q 3e-20, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.05 µM: 0.750× (z -4.2, q 0.009, down in 22 of 48 measured lines) ⚠ cell-cycle shift, explains ~22% of this change. The strongest without an alert is [[Filgotinib (drug)]] 0.05 µM: 0.757× (z -4.0, q 0.009, down in 23 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALG6]] (+0.72, fdr 7e-06), [[CDK5RAP1]] (+0.72, fdr 7e-06), [[NDC1]] (+0.70, fdr 7e-06); moves opposite to [[DLX2]] (-0.60, fdr 1e-05), [[KLF6]] (-0.58, fdr 1e-05), [[JUN]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LGALS3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 691.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.63×** | +9.8 | 3e-20 | 42/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.96×** | +9.8 | 3e-20 | 38/47 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.89×** | +9.3 | 3e-18 | 45/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.84×** | +8.9 | 1e-16 | 42/48 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.66×** | +7.4 | 1e-11 | 39/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.63×** | +7.4 | 1e-11 | 37/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.63×** | +7.1 | 1e-10 | 37/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.57×** | +6.6 | 4e-09 | 34/48 (HOP62, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.59×** | +6.4 | 1e-08 | 37/48 (NCI-H1792, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.55×** | +6.1 | 4e-08 | 34/46 (CFPAC-1, Hs 766T, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.48×** | +5.7 | 7e-07 | 34/48 (PANC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.39×** | +4.8 | 9e-05 | 25/48 (LoVo, LS 180, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.38×** | +4.7 | 1e-04 | 27/47 (NCI-H23, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.34×** | +4.2 | 9e-04 | 22/48 (LS 180, LoVo, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **1.35×** | +4.2 | 9e-04 | 26/47 (LoVo, NCI-H23, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.44×** | +3.8 | 0.005 | 20/48 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.028 | 21/48 (PANC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.50×** | +3.1 | 0.051 | 13/48 (PANC-1, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.48×** | +3.0 | 0.075 | 12/48 (RKO, PANC-1, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 691.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.750×** | -4.2 | 0.009 | 22/48 (H4, HEC-1-A, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.759×** | -4.1 | 0.009 | 19/45 (RKO, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.757×** | -4.0 | 0.009 | 23/48 (NCI-H1792, KATO III, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.761×** | -4.0 | 0.009 | 24/48 (NCI-H1573, HOP62, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.789×** | -3.5 | 0.057 | 20/48 (KATO III, SW 1088, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.805× | -3.2 | 0.14 | 20/47 (NCI-H460, H4, …) | two highest doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 691. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 29.7 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.64× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.181× (z -11.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 45.8 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +11.3) | — |
| [[A-427 (line)]] | wt | 52.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -11.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 26.4 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.69× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.118× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 73.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -13.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 30.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.304× (z -8.5) ⚠ cell-cycle shift, explains ~47% of this change |
| [[HCT15 (line)]] | alt | 31.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -9.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 46.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.275× (z -11.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 34.0 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.45× (z +9.0) | — |
| [[RKO (line)]] | wt | 50.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -15.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 97.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.246× (z -13.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 70.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 55.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 48.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 691), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALG6]] | +0.72 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[CDK5RAP1]] | +0.72 | +0.76 / +0.68 | both halves | 7e-06 |  |
| [[NDC1]] | +0.70 | +0.73 / +0.62 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[MTERF3]] | +0.69 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[PPIH]] | +0.69 | +0.73 / +0.63 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 928 |
| [[RFC4]] | +0.68 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[CPSF4]] | +0.66 | +0.69 / +0.62 | both halves | 7e-06 | pathway: Dengue Virus-Host Interactions |
| [[CSE1L]] | +0.64 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[DGCR8]] | +0.64 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[DDIAS]] | +0.63 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[DSCC1]] | +0.63 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[TMEM209]] | +0.63 | +0.57 / +0.65 | both halves | 9e-06 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLX2]] | -0.60 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[KLF6]] | -0.58 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[JUN]] | -0.58 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[LMNA]] | -0.57 | -0.67 / -0.45 | both halves | 3e-05 |  |
| [[LINC02901]] | -0.57 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[CPNE9]] | -0.57 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[LYST]] | -0.57 | -0.58 / -0.54 | both halves | 1e-05 | same gene group |
| [[RNF103-CHMP3]] | -0.56 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[SLC22A1]] | -0.56 | -0.54 / -0.65 | both halves | 1e-05 |  |
| [[ATF3]] | -0.56 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[IQCN]] | -0.56 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[KLF2]] | -0.56 | -0.63 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LGALS3]] | B | LGALS3 activity lowers SNRNP40's level | lines that do not express LGALS3 (11) vs lines expressing it (39) | 1.64× higher at baseline in the lines without LGALS3 | 0.008 | ⚠ within organs, on part of the lines; also absent: TNS3, STAT5A, ADGRG1 |
| [[KLF5]] | B | KLF5 activity lowers SNRNP40's level | lines that do not express KLF5 (18) vs lines expressing it (32) | 1.10× higher at baseline in the lines without KLF5 | 0.039 | ⚠ within organs, on part of the lines; also absent: LAMA3, IFNLR1, NCMAP; maybe low, not absent |
| [[RNF103-CHMP3]] | B | RNF103-CHMP3 activity lowers SNRNP40's level | lines that do not express RNF103-CHMP3 (5) vs lines expressing it (45) | 1.62× higher at baseline in the lines without RNF103-CHMP3 | 0.052 | ⚠ within organs, on part of the lines; also absent: TMEM144, YBX3, DTX4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.544). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-6.3, -16.5); signed map (-40.5, -19.0). **Vector** length 89.2, 23.0% of its response variance represented; |z| ≥ 3 in 967 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Interactions of Rev with host cellular proteins* (reactome, mean cos +0.51 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | +6.3 | +6.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | +2.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.9 | +5.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.5 | +8.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +2.2 | +4.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.1 | +3.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.0 | +3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | -0.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.9 | +3.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.7 | +2.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -7.5 | -0.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.6 | +1.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | +2.2 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | -3.2 | -4.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -2.9 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.4 | -3.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.2 | -3.2 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | -1.9 | -1.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.8 | -0.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.7 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | small nuclear ribonucleoprotein U5 subunit 40 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.2 — chr1:31,259,568-31,296,788 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PRP8BP, SPF38, PRPF8BP, HPRP8BP; previously WDR57 |
| Gene groups (HGNC) | WD repeat domain containing; U5 small nuclear ribonucleoprotein; Spliceosomal Bact complex; Spliceosomal C complex; Spliceosomal P complex |
| Reactome | 8 pathways, smallest: mRNA Splicing - Minor Pathway; mRNA Splicing - Major Pathway; mRNA Splicing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96DI7](https://www.uniprot.org/uniprotkb/Q96DI7) (U5 small nuclear ribonucleoprotein 40 kDa protein):

> Required for pre-mRNA splicing as component of the activated spliceosome. Component of the U5 small nuclear ribonucleoprotein (snRNP) complex and the U4/U6-U5 tri-snRNP complex, building blocks of the spliceosome. As a component of the minor spliceosome, involved in the splicing of U12-type introns in pre-mRNAs (Probable).

**Summary**, from NCBI Gene [9410](https://www.ncbi.nlm.nih.gov/gene/9410):

> This gene encodes a component of the U5 small nuclear ribonucleoprotein (snRNP) particle. The U5 snRNP is part of the spliceosome, a multiprotein complex that catalyzes the removal of introns from pre-messenger RNAs. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:30857](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30857) · Entrez [9410](https://www.ncbi.nlm.nih.gov/gene/9410) · UniProt [Q96DI7](https://www.uniprot.org/uniprotkb/Q96DI7) · Ensembl [ENSG00000060688](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000060688)

## Data

Gene col 691: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 691); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 691, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 691]; `tensor/DDL_lfc|DDL_z.npy` [691]; `embed/gene_vectors.npy` [691]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 691 or target_col == 691). Every well: [[SNRNP40 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNRNP40.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
