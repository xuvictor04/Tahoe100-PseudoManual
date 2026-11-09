---
symbol: "NFU1"
type: "gene"
col: 9823
ensembl_id: "ENSG00000169599"
name: "NFU1 iron-sulfur cluster scaffold"
location: "2p13.3"
module: 12
arm: "+"
pooled_cpm: 17.42
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 8
n_dd_up_clean: 6
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# NFU1

*NFU1 iron-sulfur cluster scaffold* — 2p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.62× (z +7.3, q 2e-10, up in 27 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 1.47× (z +5.6, q 5e-06, up in 23 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.577× (z -8.2, q 1e-13, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNRNP27]] (+0.71, fdr 1e-05), [[DCTN6]] (+0.65, fdr 7e-06), [[UBXN4]] (+0.64, fdr 1e-05); moves opposite to [[GLB1L2]] (-0.63, fdr 1e-05), [[PODXL2]] (-0.57, fdr 1e-04), [[BRI3BP]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZDBF2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9823.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.62×** | +7.3 | 2e-10 | 27/39 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +6.7 | 7e-09 | 15/31 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.47×** | +5.6 | 5e-06 | 23/47 (A-427, LS 180, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.44×** | +5.5 | 6e-06 | 27/47 (LoVo, HT-29, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.35×** | +4.5 | 8e-04 | 21/47 (A-427, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.012 | 12/48 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.8 | 0.013 | 18/48 (LS 180, Panc 03.27, …) | rises with dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.27×** | +3.4 | 0.040 | 16/44 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Amsacrine (drug)]] 5 µM |  | 1.17× | +3.4 | 0.040 | 15/48 (A498, SW480, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.061 | 11/47 (SW1417, RPMI-7951, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.26×** | +3.2 | 0.061 | 9/48 (LoVo, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9823.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.577×** | -8.2 | 1e-13 | 30/48 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.604×** | -7.5 | 1e-11 | 32/48 (SNU-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.689×** | -5.6 | 5e-06 | 25/46 (HS-578T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.710×** | -5.1 | 4e-05 | 18/48 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.546×** | -4.7 | 3e-04 | 20/46 (A-427, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.579×** | -4.3 | 0.002 | 17/48 (SNU-1, AsPC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.773×** | -3.8 | 0.010 | 19/47 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.778×** | -3.7 | 0.013 | 13/48 (KATO III, HepG2/C3A, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | 0.816× | -3.0 | 0.16 | 10/48 (SW 900, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9823. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 34.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.267× (z -9.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 20.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.23× (z +8.5) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 10.4 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.106× (z -12.1) ⚠ transcription drop; cell-cycle shift, explains ~7% of this change |
| [[COLO 205 (line)]] | alt | 14.5 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.140× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 21.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +9.7) ⚠ cell-cycle shift, explains ~17% of this change | — |
| [[HS-578T (line)]] | alt | 19.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.186× (z -11.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 11.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.29× (z +9.8) | — |
| [[LoVo (line)]] | wt | 14.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.26× (z +9.9) | — |
| [[NCI-H1792 (line)]] | alt | 18.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -9.6) ⚠ cell-cycle shift, explains ~17% of this change |
| [[NCI-H460 (line)]] | wt | 15.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.43× (z +9.3) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 14.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 20.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +10.1) ⚠ cell-cycle shift, explains ~17% of this change | — |
| [[A-172 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9823), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNRNP27]] | +0.71 | +0.75 / +0.56 | both halves | 1e-05 |  |
| [[DCTN6]] | +0.65 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[UBXN4]] | +0.64 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[OCIAD1]] | +0.61 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[FUNDC1]] | +0.61 | +0.70 / +0.43 | both halves | 3e-05 |  |
| [[STK16]] | +0.61 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[C15orf40]] | +0.61 | +0.61 / +0.57 | both halves | 8e-06 |  |
| [[COPS5]] | +0.61 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[MDP1]] | +0.60 | +0.68 / +0.48 | both halves | 2e-05 |  |
| [[PSMD4]] | +0.60 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[ZNF197]] | +0.60 | +0.71 / +0.44 | both halves | 3e-05 |  |
| [[NUDT9]] | +0.59 | +0.59 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLB1L2]] | -0.63 | -0.64 / -0.49 | both halves | 1e-05 |  |
| [[PODXL2]] | -0.57 | -0.62 / -0.33 | both halves | 1e-04 |  |
| [[BRI3BP]] | -0.57 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[IMPA2]] | -0.56 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[FANCA]] | -0.55 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[AHCY]] | -0.55 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[TUFM]] | -0.54 | -0.53 / -0.39 | both halves | 6e-05 |  |
| [[AKAP1]] | -0.53 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[URB1]] | -0.53 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[CCDC88C]] | -0.53 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[COLGALT1]] | -0.53 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[SMARCD2]] | -0.53 | -0.60 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZDBF2]] | B | ZDBF2 activity raises NFU1's level | lines that do not express ZDBF2 (14) vs lines expressing it (36) | 1.27× lower at baseline in the lines without ZDBF2 | 0.098 | ⚠ within organs, on part of the lines; also absent: WIPF1, MICU3, POPDC3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.615). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-30.7, 5.3); signed map (8.1, -22.3). **Vector** length 71.0, 12.7% of its response variance represented; |z| ≥ 3 in 720 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +6.0 | +2.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.4 | +5.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.2 | +4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +5.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +6.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +1.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +3.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.8 | +3.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -4.0 | -7.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.5 | -8.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.3 | -3.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.1 | -5.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | -5.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.5 | -4.7 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.2 | -1.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.1 | -1.8 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.1 | -1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.1 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | NFU1 iron-sulfur cluster scaffold |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.3 — chr2:69,396,113-69,437,628 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-33, NifU, NIFUC; previously HIRIP5 |
| Gene groups (HGNC) | Mitochondrial iron-sulfur assembly components |
| Reactome | 1 pathways, smallest: Protein lipoylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UMS0](https://www.uniprot.org/uniprotkb/Q9UMS0) (NFU1 iron-sulfur cluster scaffold homolog, mitochondrial):

> Iron-sulfur cluster scaffold protein which can assemble [4Fe-4S] clusters and deliver them to target proteins.

**Summary**, from NCBI Gene [27247](https://www.ncbi.nlm.nih.gov/gene/27247):

> This gene encodes a protein that is localized to mitochondria and plays a critical role in iron-sulfur cluster biogenesis. The encoded protein assembles and transfers 4Fe-4S clusters to target apoproteins including succinate dehydrogenase and lipoic acid synthase. Mutations in this gene are a cause of multiple mitochondrial dysfunctions syndrome-1, and pseudogenes of this gene are located on the short arms of chromosomes 1 and 3. Alternatively spliced transcript variants encoding multiple …

**Accessions** — [HGNC:16287](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16287) · Entrez [27247](https://www.ncbi.nlm.nih.gov/gene/27247) · UniProt [Q9UMS0](https://www.uniprot.org/uniprotkb/Q9UMS0) · Ensembl [ENSG00000169599](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169599)

## Data

Gene col 9823: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9823); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9823, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9823]; `tensor/DDL_lfc|DDL_z.npy` [9823]; `embed/gene_vectors.npy` [9823]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9823 or target_col == 9823). Every well: [[NFU1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NFU1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
