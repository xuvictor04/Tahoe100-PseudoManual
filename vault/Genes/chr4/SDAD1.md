---
symbol: "SDAD1"
type: "gene"
col: 12569
ensembl_id: "ENSG00000198301"
name: "SDA1 domain containing 1"
location: "4q21.1"
module: 5
arm: "+"
pooled_cpm: 59.12
n_lines_expressing: 50
n_dd_up: 38
n_dd_down: 0
n_dd_up_clean: 23
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# SDAD1

*SDA1 domain containing 1* — 4q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.77× (z +11.2, q 3e-26, up in 38 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 0.296×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 0.455×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change); [[Abiraterone acetate (drug)]] 0.5 µM in 1 line (SW 1088 0.0687×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDX31]] (+0.82, fdr 7e-06), [[UTP14A]] (+0.80, fdr 7e-06), [[MRTO4]] (+0.79, fdr 7e-06); moves opposite to [[TWSG1]] (-0.60, fdr 1e-05), [[PHF1]] (-0.59, fdr 7e-06).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 21 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12569.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.77×** | +11.2 | 3e-26 | 38/48 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.70×** | +10.4 | 7e-23 | 44/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.42×** | +9.8 | 3e-20 | 35/48 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.57×** | +8.5 | 3e-15 | 37/48 (HCT15, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.46×** | +7.4 | 2e-11 | 30/48 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.28×** | +6.8 | 7e-10 | 25/48 (NCI-H1792, NCI-H2347, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.94×** | +6.8 | 1e-09 | 38/48 (PANC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +6.5 | 6e-09 | 31/48 (CFPAC-1, A-172, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.40×** | +6.3 | 3e-08 | 35/48 (LOX-IMVI, NCI-H1792, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.37×** | +6.2 | 3e-08 | 30/48 (CFPAC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.36×** | +6.0 | 1e-07 | 36/48 (A-172, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +5.9 | 2e-07 | 1/49 (SW 1088) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.77×** | +5.8 | 2e-07 | 36/48 (PANC-1, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **1.35×** | +5.6 | 9e-07 | 24/44 (NCI-H2347, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.71×** | +5.5 | 2e-06 | 27/48 (RPMI-7951, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.68×** | +5.3 | 3e-06 | 28/48 (PANC-1, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.62×** | +4.9 | 2e-05 | 29/48 (NCI-H460, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.27×** | +4.7 | 6e-05 | 27/48 (NCI-H1573, A549, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[venetoclax (drug)]] 5 µM |  | **1.53×** | +4.4 | 3e-04 | 24/48 (HEC-1-A, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.24×** | +4.3 | 5e-04 | 25/48 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.5 µM |  | **1.35×** | +4.1 | 9e-04 | 21/48 (PANC-1, NCI-H1792, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12569.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 0.296×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 0.455×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change); [[Abiraterone acetate (drug)]] 0.5 µM in 1 line (SW 1088 0.0687×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.853× | -3.2 | 0.86 | 11/49 (MIA PaCa-2, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12569. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 53.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change | — |
| [[CFPAC-1 (line)]] | alt | 27.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +11.0) | — |
| [[HT-29 (line)]] | alt | 46.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 60.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +11.5) | — |
| [[NCI-H1792 (line)]] | alt | 40.5 | 2 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.12× (z +9.6) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.78× (z +8.6) | — |
| [[A-427 (line)]] | wt | 96.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.296× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[A549 (line)]] | wt | 40.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +9.6) | — |
| [[AsPC-1 (line)]] | alt | 33.5 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.28× (z +8.8) ⚠ unreliable plate only | — |
| [[H4 (line)]] | wt | 51.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +9.7) | — |
| [[LoVo (line)]] | wt | 64.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.455× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[NCI-H2030 (line)]] | alt | 38.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +8.8) | — |
| [[NCI-H23 (line)]] | alt | 86.8 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.24× (z +9.1) | — |
| [[NCI-H460 (line)]] | wt | 49.9 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.29× (z +8.9) ⚠ unreliable plate only | — |
| [[Panc 03.27 (line)]] | alt | 51.4 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.54× (z +8.8) | — |
| [[SW 1088 (line)]] | alt | 60.3 | 0 | 1 | — | [[Abiraterone acetate (drug)]] 0.5 µM 0.0687× (z -8.5) |
| [[A-172 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 74.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 88.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 84.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 53.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 75.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 46.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 43.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 59.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 41.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 60.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 73.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 102 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 79.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 79.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 78.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12569), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX31]] | +0.82 | +0.74 / +0.83 | both halves | 7e-06 | STRING 749 |
| [[UTP14A]] | +0.80 | +0.82 / +0.80 | both halves | 7e-06 | STRING 834 |
| [[MRTO4]] | +0.79 | +0.77 / +0.75 | both halves | 7e-06 | STRING 978 |
| [[LTV1]] | +0.75 | +0.74 / +0.74 | both halves | 7e-06 | STRING 921 |
| [[GTPBP4]] | +0.74 | +0.75 / +0.66 | both halves | 7e-06 | STRING 997 |
| [[MAK16]] | +0.74 | +0.75 / +0.69 | both halves | 7e-06 | STRING 893 |
| [[DHX37]] | +0.73 | +0.73 / +0.72 | both halves | 7e-06 | STRING 402 |
| [[DNAJC11]] | +0.72 | +0.79 / +0.68 | both halves | 7e-06 |  |
| [[PUS1]] | +0.72 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[DDX10]] | +0.71 | +0.72 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 917 |
| [[GPATCH4]] | +0.70 | +0.76 / +0.67 | both halves | 7e-06 | STRING 665 |
| [[NOP16]] | +0.70 | +0.68 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TWSG1]] | -0.60 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[PHF1]] | -0.59 | -0.62 / -0.59 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SDAD1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.8% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.734). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-15.7, -36.8); signed map (-0.2, -45.1). **Vector** length 109, 30.2% of its response variance represented; |z| ≥ 3 in 1,063 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.60 to 13); *rRNA processing* (reactome, mean cos +0.57 to 20); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.57 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.7 | +10.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.2 | +11.2 |
|  | [[EX229 (drug)]] 5 µM |  | +5.4 | +6.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.8 | +5.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.6 | +5.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.1 | +5.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.7 | +4.3 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -3.3 | +6.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -2.9 | +7.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.8 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.5 | -2.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.3 | -2.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.0 | -1.4 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -1.9 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | SDA1 domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.1 — chr4:75,940,950-75,990,962 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10498, Sda1, hSDA |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVU7](https://www.uniprot.org/uniprotkb/Q9NVU7) (Protein SDA1 homolog):

> Required for 60S pre-ribosomal subunits export to the cytoplasm.

**Summary**, from NCBI Gene [55153](https://www.ncbi.nlm.nih.gov/gene/55153):

> Predicted to be involved in ribosomal large subunit biogenesis and ribosomal large subunit export from nucleus. Predicted to act upstream of or within cellular response to leukemia inhibitory factor. Located in nucleolus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25537](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25537) · Entrez [55153](https://www.ncbi.nlm.nih.gov/gene/55153) · UniProt [Q9NVU7](https://www.uniprot.org/uniprotkb/Q9NVU7) · Ensembl [ENSG00000198301](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198301)

## Data

Gene col 12569: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12569); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12569, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12569]; `tensor/DDL_lfc|DDL_z.npy` [12569]; `embed/gene_vectors.npy` [12569]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12569 or target_col == 12569). Every well: [[SDAD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SDAD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
