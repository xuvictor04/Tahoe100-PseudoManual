---
symbol: "PINX1"
type: "gene"
col: 14855
ensembl_id: "ENSG00000254093"
name: "PIN2 (TERF1) interacting telomerase inhibitor 1"
location: "8p23.1"
module: 5
arm: "+"
pooled_cpm: 17.18
n_lines_expressing: 50
n_dd_up: 50
n_dd_down: 0
n_dd_up_clean: 33
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# PINX1

*PIN2 (TERF1) interacting telomerase inhibitor 1* — 8p23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 50 drug-doses (17 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.12× (z +20.6, q 0e+00, up in 45 of 47 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.28× (z +14.9, q 0e+00, up in 38 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR4]] (+0.77, fdr 7e-06), [[RRS1]] (+0.76, fdr 7e-06), [[LETM1]] (+0.75, fdr 7e-06); moves opposite to [[GNAS]] (-0.66, fdr 7e-06), [[AAMDC]] (-0.62, fdr 1e-05), [[FAM117A]] (-0.62, fdr 6e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LDLRAD3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 67 in all, 21 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 50 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14855.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **3.12×** | +20.6 | 0e+00 | 45/47 (AsPC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.76×** | +18.4 | 0e+00 | 45/47 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.76×** | +18.4 | 0e+00 | 44/47 (AsPC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.28×** | +14.9 | 0e+00 | 38/46 (A-172, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.26×** | +14.7 | 0e+00 | 45/47 (MIA PaCa-2, NCI-H460, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.89×** | +11.5 | 1e-28 | 36/47 (A-172, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.86×** | +11.3 | 2e-27 | 41/47 (HS-578T, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.49×** | +10.1 | 4e-22 | 28/47 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.73×** | +9.9 | 3e-21 | 37/47 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.43×** | +9.1 | 8e-18 | 23/47 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.75×** | +8.8 | 6e-17 | 30/47 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.62×** | +8.7 | 1e-16 | 34/47 (NCI-H460, HOP62, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **1.61×** | +7.5 | 3e-12 | 26/43 (A-172, A498, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.11×** | +7.0 | 7e-11 | 25/47 (MIA PaCa-2, SHP-77, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.07×** | +6.9 | 3e-10 | 26/46 (NCI-H460, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +6.7 | 8e-10 | 21/48 (HEC-1-A, Panc 03.27, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **2.02×** | +6.7 | 9e-10 | 16/43 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.48×** | +6.7 | 9e-10 | 20/47 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.44×** | +6.6 | 1e-09 | 22/47 (MIA PaCa-2, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **2.01×** | +6.6 | 1e-09 | 23/46 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **2.01×** | +6.6 | 1e-09 | 25/48 (AsPC-1, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +6.2 | 1e-08 | 19/47 (MIA PaCa-2, AsPC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14855.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | 0.874× | -3.5 | 0.22 | 11/48 (A-427, COLO 205, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.815× | -3.3 | 0.22 | 14/47 (HepG2/C3A, SK-MEL-2, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | 0.817× | -3.2 | 0.22 | 5/47 (A-427, RKO, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.841× | -3.2 | 0.22 | 9/48 (SNU-1, A-427, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 0.848× | -3.0 | 0.24 | 14/47 (LS 180, H4, …) | inconsistent across doses |  |
| [[Rifaximin (drug)]] 0.5 µM |  | 0.848× | -3.0 | 0.24 | 7/47 (A498, NCI-H2347, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.62 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14855. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 14.7 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.6× (z +19.9) | — |
| [[AsPC-1 (line)]] | alt | 10.7 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 8.83× (z +10.6) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[Hs 766T (line)]] | wt | 17.3 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.50× (z +9.6) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[HOP62 (line)]] | alt | 8.35 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.96× (z +9.7) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[HS-578T (line)]] | alt | 14.1 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.75× (z +9.0) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[LS 180 (line)]] | wt | 16.3 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +8.8) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H2347 (line)]] | alt | 8.34 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.09× (z +9.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.58× (z +8.7) | — |
| [[SW480 (line)]] | alt | 19.6 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.06× (z +9.2) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 35.3 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.98× (z +10.8) ⚠ unreliable plate only | — |
| [[NCI-H1792 (line)]] | alt | 14.7 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.08× (z +9.1) | — |
| [[NCI-H23 (line)]] | alt | 29.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.44× (z +9.1) | — |
| [[NCI-H460 (line)]] | wt | 20.2 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.29× (z +9.9) ⚠ unreliable plate only | — |
| [[A-427 (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.90 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.21 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14855), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR4]] | +0.77 | +0.78 / +0.74 | both halves | 7e-06 |  |
| [[RRS1]] | +0.76 | +0.79 / +0.68 | both halves | 7e-06 | STRING 703 |
| [[LETM1]] | +0.75 | +0.70 / +0.76 | both halves | 7e-06 |  |
| [[POLR1A]] | +0.75 | +0.73 / +0.75 | both halves | 7e-06 |  |
| [[URB2]] | +0.74 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[PINX1-1]] | +0.74 | +0.73 / +0.72 | both halves | 7e-06 | ⚠ **readthrough risk**: PINX1-1 lies 0.0 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[PUS1]] | +0.74 | +0.74 / +0.74 | both halves | 7e-06 |  |
| [[PDCD11]] | +0.74 | +0.71 / +0.73 | both halves | 7e-06 | same gene group; STRING 417 |
| [[MYBBP1A]] | +0.73 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[DDX31]] | +0.72 | +0.73 / +0.72 | both halves | 7e-06 | STRING 432 |
| [[BYSL]] | +0.72 | +0.77 / +0.66 | both halves | 7e-06 | same gene group; STRING 972 |
| [[PGAM5]] | +0.72 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[DDX21]] | +0.72 | +0.74 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAS]] | -0.66 | -0.68 / -0.67 | both halves | 7e-06 |  |
| [[AAMDC]] | -0.62 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[FAM117A]] | -0.62 | -0.38 / -0.56 | both halves | 6e-05 |  |
| [[RSRP1]] | -0.61 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[TMEM59]] | -0.61 | -0.57 / -0.63 | both halves | 1e-05 |  |
| [[TXNDC16]] | -0.60 | -0.41 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LDLRAD3]] | B | LDLRAD3 activity raises PINX1's level | lines that do not express LDLRAD3 (7) vs lines expressing it (43) | 1.58× lower at baseline in the lines without LDLRAD3 | 0.058 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers PINX1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 9.2% of all compounds | 0.095 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.738). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-13.7, -37.4); signed map (-3.2, -48.4). **Vector** length 79.8, 17.2% of its response variance represented; |z| ≥ 3 in 1,151 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.62 to 13); *rRNA processing* (reactome, mean cos +0.56 to 20); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.56 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.6 | +14.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.8 | +11.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.4 | +6.6 |
|  | [[EX229 (drug)]] 5 µM |  | +3.8 | +6.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.7 | +5.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.6 | +6.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.3 | +6.2 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | +0.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.0 | +9.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -2.3 | -3.0 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | -2.0 | -3.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.8 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -1.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.7 | -3.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.6 | -1.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.6 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | PIN2 (TERF1) interacting telomerase inhibitor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p23.1 — chr8:10,764,961-10,839,884 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LPTL, LPTS, FLJ20565, MGC8850, Gno1, Pxr1 |
| Gene groups (HGNC) | G-patch domain containing; SSU processome; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96BK5](https://www.uniprot.org/uniprotkb/Q96BK5) (PIN2/TERF1-interacting telomerase inhibitor 1):

> Microtubule-binding protein essential for faithful chromosome segregation. Mediates TRF1 and TERT accumulation in nucleolus and enhances TRF1 binding to telomeres. Inhibits telomerase activity. May inhibit cell proliferation and act as tumor suppressor.

**Summary**, from NCBI Gene [54984](https://www.ncbi.nlm.nih.gov/gene/54984):

> Enables telomerase RNA binding activity and telomerase inhibitor activity. Involved in several processes, including negative regulation of telomere maintenance via telomerase; positive regulation of protein localization to nucleolus; and protein localization to nucleolus. Acts upstream of or within telomere maintenance via telomerase. Located in chromosomal region; nuclear lumen; and spindle. Implicated in hepatocellular carcinoma. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30046](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30046) · Entrez [54984](https://www.ncbi.nlm.nih.gov/gene/54984) · UniProt [Q96BK5](https://www.uniprot.org/uniprotkb/Q96BK5) · Ensembl [ENSG00000254093](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000254093)

## Data

Gene col 14855: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14855); `tables/drug_effects.parquet` (73 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14855, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14855]; `tensor/DDL_lfc|DDL_z.npy` [14855]; `embed/gene_vectors.npy` [14855]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14855 or target_col == 14855). Every well: [[PINX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PINX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
