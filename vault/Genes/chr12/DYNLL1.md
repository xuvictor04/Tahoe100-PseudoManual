---
symbol: "DYNLL1"
type: "gene"
col: 1556
ensembl_id: "ENSG00000088986"
name: "dynein light chain LC8-type 1"
location: "12q24.31"
module: 20
arm: "-"
pooled_cpm: 54.75
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# DYNLL1

*dynein light chain LC8-type 1* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.64× (z +7.2, q 3e-10, up in 45 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.49× (z +7.1, q 5e-10, up in 42 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MED19]] (+0.69, fdr 7e-06), [[TOPORS]] (+0.69, fdr 7e-06), [[TUBB2A]] (+0.65, fdr 7e-06); moves opposite to [[EIF2S3]] (-0.69, fdr 7e-06), [[HNRNPA3]] (-0.67, fdr 7e-06), [[IPO5]] (-0.62, fdr 3e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PDLIM2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1556.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.64×** | +7.2 | 3e-10 | 45/47 (MIA PaCa-2, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.49×** | +7.1 | 5e-10 | 42/48 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.87×** | +6.9 | 1e-09 | 37/48 (AsPC-1, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.23×** | +6.2 | 8e-08 | 45/48 (NCI-H1792, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.04×** | +5.5 | 4e-06 | 43/48 (HS-578T, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **1.97×** | +5.3 | 1e-05 | 40/48 (NCI-H460, A498, …) | two highest doses | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.93×** | +4.9 | 8e-05 | 36/48 (AsPC-1, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **1.86×** | +4.6 | 3e-04 | 29/41 (NCI-H460, PANC-1, …) | two highest doses | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~58% of this change | **1.81×** | +4.6 | 3e-04 | 44/48 (HOP62, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +4.5 | 4e-04 | 34/48 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **1.67×** | +4.0 | 0.004 | 31/48 (SHP-77, COLO 205, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.55×** | +3.4 | 0.029 | 32/48 (NCI-H460, A498, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.65×** | +3.4 | 0.029 | 29/47 (HS-578T, C32, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.50×** | +3.2 | 0.065 | 30/48 (NCI-H460, SW 900, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1556.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | 0.418× | -3.5 | 0.18 | 38/48 (C-33 A, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | 0.430× | -3.4 | 0.18 | 39/48 (NCI-H2347, BT-474, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | 0.440× | -3.3 | 0.18 | 31/49 (RKO, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | 0.471× | -3.0 | 0.34 | 34/49 (J82, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.64 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1556. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 74.7 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +14.4) ⚠ cell-cycle shift, explains ~80% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.01× (z +9.3) | — |
| [[NCI-H460 (line)]] | wt | 34.1 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +10.8) ⚠ cell-cycle shift, explains ~80% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.25× (z +8.9) | — |
| [[C32 (line)]] | wt | 31.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +9.3) ⚠ cell-cycle shift, explains ~80% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.90× (z +9.3) | — |
| [[HOP62 (line)]] | alt | 50.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +11.1) ⚠ cell-cycle shift, explains ~80% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.49× (z +10.0) | — |
| [[NCI-H1792 (line)]] | alt | 44.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.45× (z +13.0) ⚠ cell-cycle shift, explains ~80% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.14× (z +9.8) | — |
| [[SW 900 (line)]] | alt | 49.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +8.7) ⚠ cell-cycle shift, explains ~80% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.24× (z +8.5) | — |
| [[Hs 766T (line)]] | wt | 59.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +11.4) ⚠ cell-cycle shift, explains ~80% of this change | — |
| [[LoVo (line)]] | wt | 66.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +9.3) ⚠ cell-cycle shift, explains ~80% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 56.2 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.65× (z +9.2) ⚠ toxic | — |
| [[NCI-H1573 (line)]] | alt | 47.8 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.26× (z +8.5) ⚠ toxic | — |
| [[RKO (line)]] | wt | 39.4 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.81× (z +8.7) ⚠ toxic | — |
| [[A-172 (line)]] | wt | 76.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 71.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 52.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 78.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 58.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 49.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 64.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 44.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 60.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 54.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 79.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 68.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 86.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 50.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1556), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED19]] | +0.69 | +0.64 / +0.74 | both halves | 7e-06 |  |
| [[TOPORS]] | +0.69 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[TUBB2A]] | +0.65 | +0.65 / +0.63 | both halves | 7e-06 | pathway: Affinity selection of immunoglobulins; STRING 626 |
| [[RSF1]] | +0.64 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[AK6]] | +0.64 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[MRPS18C]] | +0.64 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[KRTCAP2]] | +0.63 | +0.52 / +0.73 | both halves | 1e-05 |  |
| [[NKAP]] | +0.63 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[EIF1B]] | +0.63 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[BTG1]] | +0.62 | +0.40 / +0.69 | both halves | 5e-05 |  |
| [[ERVK3-1]] | +0.62 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[THAP1]] | +0.61 | +0.67 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF2S3]] | -0.69 | -0.65 / -0.63 | both halves | 7e-06 |  |
| [[HNRNPA3]] | -0.67 | -0.62 / -0.71 | both halves | 7e-06 |  |
| [[IPO5]] | -0.62 | -0.46 / -0.68 | both halves | 3e-05 |  |
| [[TXNDC5]] | -0.61 | -0.56 / -0.65 | both halves | 1e-05 |  |
| [[RNPS1]] | -0.61 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[ARF3]] | -0.60 | -0.58 / -0.61 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 556 |
| [[FKBP9]] | -0.60 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[RPSA]] | -0.60 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[NSUN2]] | -0.59 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[TFDP1]] | -0.59 | -0.51 / -0.58 | both halves | 1e-05 | pathway: Activation of BH3-only proteins |
| [[COLGALT1]] | -0.59 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[CPSF6]] | -0.59 | -0.49 / -0.67 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDLIM2]] | C | PDLIM2 activity raises DYNLL1's level | lines that do not express PDLIM2 (4) vs lines expressing it (46) | 1.38× lower at baseline in the lines without PDLIM2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FSTL3, BIRC3, BOK; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.713). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-29.1, -27.6); signed map (-2.4, 10.7). **Vector** length 88.4, 32.8% of its response variance represented; |z| ≥ 3 in 693 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.9 | +7.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | +5.7 | +6.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.2 | +6.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.6 | +5.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | +4.1 | +4.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +3.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | -0.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.4 | -0.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.4 | +2.0 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.3 | +0.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | -6.6 | +5.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -6.5 | -0.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | -6.2 | +4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.2 | -0.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.2 | -3.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.0 | -0.5 |
|  | [[EX229 (drug)]] 5 µM |  | -1.8 | -1.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.8 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | dynein light chain LC8-type 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:120,469,850-120,498,493 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hdlc1, DLC1, PIN, LC8, DLC8; previously DNCL1 |
| Gene groups (HGNC) | Dynein 1 complex subunits; Dynein 2 complex subunits; Dyneins, axonemal outer arm complex subunits; Dyneins, axonemal inner arm I1/f complex subunits; Dynein light chain LC8-type family |
| Reactome | 62 pathways, smallest: Activation of BIM and translocation to mitochondria; Activation of BH3-only proteins; Aggrephagy |
| Matched by | ensembl_id |

**Function**, from UniProt [P63167](https://www.uniprot.org/uniprotkb/P63167) (Dynein light chain 1, cytoplasmic):

> Component of dynein, a family of motor proteins essential for movement along microtubules (By similarity). Required for structural and functional integrity of cilia (By similarity). Acts as one of several non-catalytic accessory components of the cytoplasmic dynein 1 complex that are thought to be involved in linking dynein to cargos and to adapter proteins that regulate dynein function (By similarity). Cytoplasmic dynein 1 acts as a motor for the intracellular retrograde motility of vesicles …

**Summary**, from NCBI Gene [8655](https://www.ncbi.nlm.nih.gov/gene/8655):

> Cytoplasmic dyneins are large enzyme complexes with a molecular mass of about 1,200 kD. They contain two force-producing heads formed primarily from dynein heavy chains, and stalks linking the heads to a basal domain, which contains a varying number of accessory intermediate chains. The complex is involved in intracellular transport and motility. The protein described in this record is a light chain and exists as part of this complex but also physically interacts with and inhibits the activity …

**Accessions** — [HGNC:15476](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15476) · Entrez [8655](https://www.ncbi.nlm.nih.gov/gene/8655) · UniProt [P63167](https://www.uniprot.org/uniprotkb/P63167) · Ensembl [ENSG00000088986](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000088986)

## Data

Gene col 1556: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1556); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1556, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1556]; `tensor/DDL_lfc|DDL_z.npy` [1556]; `embed/gene_vectors.npy` [1556]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1556 or target_col == 1556). Every well: [[DYNLL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DYNLL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
