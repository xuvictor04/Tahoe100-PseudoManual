---
symbol: "RILPL2"
type: "gene"
col: 7471
ensembl_id: "ENSG00000150977"
name: "Rab interacting lysosomal protein like 2"
location: "12q24.31"
module: 40
arm: "+"
pooled_cpm: 18.03
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 3
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# RILPL2

*Rab interacting lysosomal protein like 2* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.46× (z +6.7, q 2e-08, up in 29 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.757× (z -4.8, q 7e-04, down in 22 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GLRX]] (+0.62, fdr 1e-05), [[NCK1]] (+0.57, fdr 1e-05), [[NRTN]] (+0.57, fdr 9e-05); moves opposite to [[SDCBP2-AS1]] (-0.58, fdr 2e-05), [[SNX19]] (-0.56, fdr 3e-05), [[LIG4]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[SMIM3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7471.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +6.7 | 2e-08 | 29/47 (A549, A-172, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.54×** | +5.4 | 2e-05 | 25/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.40×** | +4.2 | 0.005 | 24/48 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +4.0 | 0.006 | 15/45 (NCI-H460, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~16% here); position effect removed |
| [[Budesonide (drug)]] 0.05 µM |  | **1.38×** | +4.0 | 0.006 | 20/48 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.36×** | +3.9 | 0.010 | 19/48 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.018 | 19/48 (LoVo, HT-29, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.052 | 20/48 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | 1.28× | +3.1 | 0.13 | 13/48 (NCI-H1792, CFPAC-1, …) | all doses, flat |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.41× | +3.1 | 0.13 | 11/44 (HCT15, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7471.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.757×** | -4.8 | 7e-04 | 22/47 (RKO, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.693×** | -4.5 | 0.002 | 24/47 (COLO 205, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.716×** | -4.0 | 0.013 | 18/47 (AsPC-1, A549, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.764× | -3.3 | 0.13 | 20/48 (NCI-H460, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.779× | -3.1 | 0.22 | 12/47 (SW 900, SNU-423, …) | rises with dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7471. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 18.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -11.9) |
| [[LOX-IMVI (line)]] | wt | 12.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -9.0) |
| [[PANC-1 (line)]] | alt | 17.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +8.8) | — |
| [[A-172 (line)]] | wt | 18.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +9.6) | — |
| [[A549 (line)]] | wt | 7.94 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.54× (z +10.3) | — |
| [[AsPC-1 (line)]] | alt | 16.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -11.7) |
| [[C32 (line)]] | wt | 8.53 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0730× (z -10.9) |
| [[H4 (line)]] | wt | 38.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0788× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 10.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 16.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -12.4) |
| [[RKO (line)]] | wt | 37.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -15.1) |
| [[A-427 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 39.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 20.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7471), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLRX]] | +0.62 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[NCK1]] | +0.57 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[NRTN]] | +0.57 | +0.37 / +0.66 | both halves | 9e-05 |  |
| [[CBLB]] | +0.56 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[COX14]] | +0.56 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[ELP2]] | +0.55 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[MT1X]] | +0.55 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[MHENCR]] | +0.54 | +0.40 / +0.57 | both halves | 5e-05 |  |
| [[MAPKAPK5-AS1]] | +0.54 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[CNOT8]] | +0.53 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[MPST]] | +0.53 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[TMEM63C]] | +0.53 | +0.36 / +0.55 | both halves | 1e-04 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDCBP2-AS1]] | -0.58 | -0.46 / -0.56 | both halves | 2e-05 |  |
| [[SNX19]] | -0.56 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[LIG4]] | -0.54 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[BMPR1B]] | -0.53 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[TUG1]] | -0.53 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[MAPRE1]] | -0.53 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[RBM12]] | -0.51 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[ANAPC7]] | -0.51 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[DHRS12]] | -0.51 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[ZNF518B]] | -0.51 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[DST]] | -0.51 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[WDR1]] | -0.50 | -0.42 / -0.53 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMIM3]] | B | SMIM3 activity raises RILPL2's level | lines that do not express SMIM3 (11) vs lines expressing it (39) | 1.37× lower at baseline in the lines without SMIM3 | 0.008 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[WNT5A]] | B | WNT5A activity raises RILPL2's level | lines that do not express WNT5A (30) vs lines expressing it (20) | 1.45× lower at baseline in the lines without WNT5A | 0.018 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13 |
| [[WNT5A]] | B | WNT5A activity weakens RILPL2's drug response | lines that do not express WNT5A (30) vs lines expressing it (18) | the lines without WNT5A respond 1.13× as strongly (z diff -0.51); strongest at Panobinostat 0.5 µM: 1.68x vs 1.07x (z diff -2.1) | 0.055 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13; target measured in part of the lines; artifact flags |
| [[GYPC]] | B | GYPC activity raises RILPL2's level | lines that do not express GYPC (35) vs lines expressing it (15) | 1.24× lower at baseline in the lines without GYPC | 0.062 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PHACTR1, ANKRD30B, PLPP4 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers RILPL2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers RILPL2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.566). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (2.6, -18.5); signed map (-41.8, 11.4). **Vector** length 101, 23.5% of its response variance represented; |z| ≥ 3 in 865 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +6.7 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +3.4 | +3.4 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +3.3 | +4.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +3.0 | +2.9 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +3.0 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +3.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.8 | -4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.5 | -2.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -3.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.2 | -4.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.9 | -1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | -2.1 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | Rab interacting lysosomal protein like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:123,415,039-123,436,684 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC7036, FLJ30380, FLJ32372 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969X0](https://www.uniprot.org/uniprotkb/Q969X0) (RILP-like protein 2):

> Involved in cell shape and neuronal morphogenesis, positively regulating the establishment and maintenance of dendritic spines (By similarity). Plays a role in cellular protein transport, including protein transport away from primary cilia (By similarity). May function via activation of RAC1 and PAK1 (By similarity).

**Summary**, from NCBI Gene [196383](https://www.ncbi.nlm.nih.gov/gene/196383):

> This gene encodes a protein that contains a rab-interacting lysosomal protein-like domain. This protein may be involved in regulating lysosome morphology. This protein may also be a target for the Hepatitis C virus and assist in viral replication. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Jan 2015]

**Accessions** — [HGNC:28787](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28787) · Entrez [196383](https://www.ncbi.nlm.nih.gov/gene/196383) · UniProt [Q969X0](https://www.uniprot.org/uniprotkb/Q969X0) · Ensembl [ENSG00000150977](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150977)

## Data

Gene col 7471: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7471); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7471, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7471]; `tensor/DDL_lfc|DDL_z.npy` [7471]; `embed/gene_vectors.npy` [7471]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7471 or target_col == 7471). Every well: [[RILPL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RILPL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
