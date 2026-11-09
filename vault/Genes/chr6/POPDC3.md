---
symbol: "POPDC3"
type: "gene"
col: 5318
ensembl_id: "ENSG00000132429"
name: "popeye domain cAMP effector 3"
location: "6q21"
module: 60
arm: "+"
pooled_cpm: 9.18
n_lines_expressing: 32
n_dd_up: 11
n_dd_down: 12
n_dd_up_clean: 5
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 6
direction_downstream: 4
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# POPDC3

*popeye domain cAMP effector 3* — 6q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.03× (z +10.8, q 2e-24, up in 20 of 21 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 2.86× (z +10.2, q 4e-22, up in 28 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.452× (z -7.7, q 6e-12, down in 21 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHORDC1]] (+0.62, fdr 1e-05), [[NXPE3]] (+0.61, fdr 1e-05), [[NSFL1C]] (+0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[HEG1]] → it (grade B ⚠); 4 go from it, the strongest it → [[DYNC1I1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5318.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.03×** | +10.8 | 2e-24 | 20/21 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.86×** | +10.2 | 4e-22 | 28/30 (PANC-1, LOX-IMVI, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **2.32×** | +8.2 | 5e-14 | 26/30 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.26×** | +7.9 | 3e-13 | 24/30 (SW480, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.23×** | +7.5 | 8e-12 | 13/18 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.18×** | +5.9 | 3e-07 | 22/29 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.94×** | +5.9 | 3e-07 | 15/19 (NCI-H2030, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +3.4 | 0.055 | 11/27 (HOP62, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.92×** | +3.3 | 0.057 | 7/22 (LoVo, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.40×** | +3.2 | 0.084 | 10/30 (HOP62, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.38×** | +3.1 | 0.095 | 6/30 (NCI-H1573, H4, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5318.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.452×** | -7.7 | 6e-12 | 21/30 (NCI-H1792, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.594×** | -7.2 | 2e-10 | 23/30 (hTERT-HPNE, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.479×** | -7.2 | 2e-10 | 20/30 (NCI-H1792, HOP62, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.503×** | -6.7 | 3e-09 | 19/30 (SW 900, HOP62, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.520×** | -6.4 | 2e-08 | 18/30 (NCI-H1792, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.613×** | -4.8 | 2e-04 | 14/30 (NCI-H2030, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.633×** | -4.5 | 7e-04 | 15/30 (SNU-423, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.641×** | -4.3 | 0.001 | 17/29 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.746×** | -4.0 | 0.003 | 13/28 (H4, NCI-H1792, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.665×** | -4.0 | 0.004 | 19/30 (LoVo, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.490×** | -3.6 | 0.014 | 13/29 (A-427, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | **0.715×** | -3.3 | 0.052 | 6/30 (H4, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5318. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 14.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -9.3) |
| [[A498 (line)]] | wt | 19.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -11.9) |
| [[NCI-H1573 (line)]] | alt | 3.32 | 0 | 2 | — | [[Acetazolamide (drug)]] 0.05 µM 0.0516× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 29.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -10.4) |
| [[A549 (line)]] | wt | 13.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -8.5) |
| [[H4 (line)]] | wt | 21.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.201× (z -9.6) ⚠ cell-cycle shift, explains ~24% of this change |
| [[HS-578T (line)]] | alt | 8.39 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 18.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -14.1) |
| [[LOX-IMVI (line)]] | wt | 16.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -11.5) |
| [[NCI-H2030 (line)]] | alt | 14.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.53× (z +9.3) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 11.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -8.5) |
| [[PANC-1 (line)]] | alt | 22.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 21.9 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.102× (z -12.8) ⚠ cell-cycle shift, explains ~66% of this change |
| [[SNU-423 (line)]] | alt | 20.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.167× (z -10.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 17.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -9.4) |
| [[A-172 (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.718 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.655 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.97 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.74 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.624 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.668 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.778 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.799 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.687 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.605 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.910 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.844 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.676 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.747 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.788 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.68 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5318), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHORDC1]] | +0.62 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[NXPE3]] | +0.61 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[NSFL1C]] | +0.61 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[MAP1B]] | +0.60 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[CACYBP]] | +0.60 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[CASP6]] | +0.58 | +0.60 / +0.37 | both halves | 9e-05 |  |
| [[ZFAND2A]] | +0.58 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[HSP90AA2P]] | +0.58 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[PLAA]] | +0.58 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[TXNL1]] | +0.57 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[ATP2C1]] | +0.57 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[MLLT11]] | +0.56 | +0.53 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HEG1]] | B | HEG1 activity raises POPDC3's level | lines that do not express HEG1 (11) vs lines expressing it (39) | 3.33× lower at baseline in the lines without HEG1 | 0.085 | ⚠ within organs, on part of the lines; also absent: CCDC88A, STARD9, RECK |
| [[PSMB5]] | B | PSMB5 activity lowers POPDC3's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MAP1B]] | C | MAP1B activity raises POPDC3's level | lines that do not express MAP1B (16) vs lines expressing it (34) | 4.65× lower at baseline in the lines without MAP1B | 0.012 | ⚠ within organs, on part of the lines; also absent: MPDZ, GNB4, EVL; co-absent with the target |
| [[LAYN]] | C | LAYN activity raises POPDC3's level | lines that do not express LAYN (31) vs lines expressing it (19) | 3.36× lower at baseline in the lines without LAYN | 0.018 | ⚠ within organs, on part of the lines; also absent: COL1A1, ITGA11, LUM; co-absent with the target |
| [[MLLT11]] | C | MLLT11 activity raises POPDC3's level | lines that do not express MLLT11 (21) vs lines expressing it (29) | 3.57× lower at baseline in the lines without MLLT11 | 0.024 | ⚠ within organs, on part of the lines; also absent: DZIP1, ADAMTS18, KCNJ6; maybe low, not absent; co-absent with the target |
| [[MAP1A]] | C | MAP1A activity raises POPDC3's level | lines that do not express MAP1A (17) vs lines expressing it (33) | 3.37× lower at baseline in the lines without MAP1A | 0.063 | ⚠ within organs, on part of the lines; also absent: HMCN1, HOXB-AS1, LINC02269; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DYNC1I1]] | B | POPDC3 activity raises DYNC1I1's level | lines that do not express POPDC3 (18) vs lines expressing it (32) | 1.96× lower at baseline in the lines without POPDC3 | 0.073 | ⚠ within organs, on part of the lines; also absent: WIPF1, WDR17, BVES-AS1 |
| [[LARP6]] | B | POPDC3 activity raises LARP6's level | lines that do not express POPDC3 (18) vs lines expressing it (32) | 2.28× lower at baseline in the lines without POPDC3 | 0.079 | ⚠ within organs, on part of the lines; also absent: WIPF1, WDR17, BVES-AS1 |
| [[MLLT11]] | C | POPDC3 activity raises MLLT11's level | lines that do not express POPDC3 (18) vs lines expressing it (32) | 2.83× lower at baseline in the lines without POPDC3 | 0.019 | ⚠ within organs, on part of the lines; also absent: WIPF1, WDR17, BVES-AS1; co-absent with the target |
| [[MAP1B]] | C | POPDC3 activity raises MAP1B's level | lines that do not express POPDC3 (18) vs lines expressing it (32) | 5.52× lower at baseline in the lines without POPDC3 | 0.032 | ⚠ within organs, on part of the lines; also absent: WIPF1, WDR17, BVES-AS1; co-absent with the target |

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.623). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-19.7, -8.4); signed map (-27.8, -23.1). **Vector** length 59.9, 13.5% of its response variance represented; |z| ≥ 3 in 597 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +5.2 | +5.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.1 | +7.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.1 | +10.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +8.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +3.5 | +3.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.5 | +1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +0.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +3.0 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.5 | -6.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | -4.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.3 | -4.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.3 | -4.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -1.9 | -7.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -0.9 | -1.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -0.8 | -0.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.8 | -1.4 |
|  | [[Tetracycline (hydrochloride) (drug)]] 5 µM |  | -0.8 | -1.3 |
|  | [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | -0.8 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | popeye domain cAMP effector 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q21 — chr6:105,157,900-105,180,014 (-) |
| Ensembl biotype | protein_coding |
| Also known as | POP3, MGC22671, bA355M14.1 |
| Gene groups (HGNC) | Popeye domain cAMP effector family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HBV1](https://www.uniprot.org/uniprotkb/Q9HBV1) (Popeye domain-containing protein 3):

> May play a role in the maintenance of heart function mediated, at least in part, through cAMP-binding. May play a role in the regulation of KCNK2/TREK-1-mediated current amplitude.

**Summary**, from NCBI Gene [64208](https://www.ncbi.nlm.nih.gov/gene/64208):

> This gene encodes a member of the POP family of proteins containing three putative transmembrane domains. This gene is expressed in cardiac and skeletal muscle and may play an important role in these tissues during development. Alternatively spliced transcript variants have been found. [provided by RefSeq, Nov 2008]

**Accessions** — [HGNC:17649](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17649) · Entrez [64208](https://www.ncbi.nlm.nih.gov/gene/64208) · UniProt [Q9HBV1](https://www.uniprot.org/uniprotkb/Q9HBV1) · Ensembl [ENSG00000132429](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132429)

## Data

Gene col 5318: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5318); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5318, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5318]; `tensor/DDL_lfc|DDL_z.npy` [5318]; `embed/gene_vectors.npy` [5318]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5318 or target_col == 5318). Every well: [[POPDC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POPDC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
