---
symbol: "ZSWIM9"
type: "gene"
col: 11679
ensembl_id: "ENSG00000185453"
name: "zinc finger SWIM-type containing 9"
location: "19q13.33"
module: 12
arm: "+"
pooled_cpm: 19.45
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 16
n_dd_up_clean: 6
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# ZSWIM9

*zinc finger SWIM-type containing 9* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.40× (z +5.0, q 3e-04, up in 19 of 44 measured lines) ⚠ transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.38× (z +4.8, q 4e-04, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.554× (z -8.9, q 4e-16, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PELP1]] (+0.70, fdr 1e-05), [[TAB1]] (+0.64, fdr 7e-06), [[SRSF11]] (+0.60, fdr 7e-06, ⚠ SRSF11 in the vector space only through flagged drug-doses), [[CBY1]] (+0.59, fdr 1e-05); moves opposite to [[IL13RA1]] (-0.52, fdr 5e-05), [[MARCKSL1]] (-0.52, fdr 1e-05), [[CD164]] (-0.52, fdr 6e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF329]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11679.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +5.0 | 3e-04 | 19/44 (PANC-1, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +4.8 | 4e-04 | 25/48 (KATO III, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.36×** | +4.6 | 9e-04 | 21/48 (SNU-1, SW48, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.53×** | +4.5 | 9e-04 | 17/45 (COLO 205, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.32×** | +3.9 | 0.013 | 14/45 (LoVo, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.26×** | +3.4 | 0.057 | 13/47 (NCI-H1792, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.068 | 17/48 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | 1.23× | +3.1 | 0.13 | 14/48 (LoVo, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.23× | +3.1 | 0.13 | 12/47 (C-33 A, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11679.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.554×** | -8.9 | 4e-16 | 38/48 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.609×** | -7.5 | 2e-11 | 33/47 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.643×** | -6.6 | 6e-09 | 29/46 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.433×** | -6.6 | 7e-09 | 29/48 (Panc 03.27, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.742×** | -6.4 | 2e-08 | 25/47 (PANC-1, NCI-H460, …) | top dose only | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.746×** | -6.3 | 4e-08 | 29/47 (RPMI-7951, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.489×** | -5.6 | 2e-06 | 28/45 (A-427, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.727×** | -4.8 | 1e-04 | 21/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.742×** | -4.5 | 4e-04 | 22/47 (HT-29, HepG2/C3A, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.738×** | -4.4 | 6e-04 | 24/46 (COLO 205, SHP-77, …) | top dose only | cell-cycle shift (explains ~19% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.749×** | -4.4 | 7e-04 | 20/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.743×** | -4.3 | 8e-04 | 24/47 (A-172, COLO 205, …) | top dose only | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.589×** | -4.2 | 0.001 | 13/27 (MIA PaCa-2, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.791×** | -3.5 | 0.016 | 17/47 (H4, SW 1271, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.796×** | -3.5 | 0.021 | 14/47 (MIA PaCa-2, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.812×** | -3.0 | 0.089 | 15/48 (RKO, C-33 A, …) | top dose only | cell-cycle shift (explains ~6% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11679. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 16.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.325× (z -9.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 13.0 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.205× (z -9.4) |
| [[A-427 (line)]] | wt | 24.1 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0883× (z -9.8) |
| [[COLO 205 (line)]] | alt | 19.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.181× (z -8.6) ⚠ toxic |
| [[HCT15 (line)]] | alt | 35.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[HepG2_C3A (line)]] | wt | 10.2 | 0 | 1 | — | [[Vandetanib (drug)]] 0.5 µM 0.0797× (z -9.7) |
| [[Hs 766T (line)]] | wt | 14.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -9.5) |
| [[KATO III (line)]] | alt | 21.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.201× (z -11.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 24.2 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0590× (z -11.3) ⚠ toxic |
| [[RKO (line)]] | wt | 17.3 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0921× (z -12.5) |
| [[RPMI-7951 (line)]] | alt | 23.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -11.1) |
| [[SHP-77 (line)]] | alt | 42.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 13.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.101× (z -11.2) ⚠ toxic; cell-cycle shift, explains ~86% of this change |
| [[SW48 (line)]] | wt | 19.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.139× (z -8.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 26.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11679), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PELP1]] | +0.70 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[TAB1]] | +0.64 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[SRSF11]] ⚠ | +0.60 | +0.60 / +0.59 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[CBY1]] | +0.59 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[C1orf35]] | +0.59 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[FRA10AC1]] | +0.59 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[RBMX2]] | +0.59 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[NISCH]] | +0.58 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[PRPF6]] | +0.58 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[ZC3H13]] | +0.56 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[PPIG]] | +0.56 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[RNF214]] | +0.56 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[DDRGK1]] | +0.56 | +0.45 / +0.58 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IL13RA1]] | -0.52 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[MARCKSL1]] | -0.52 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[CD164]] | -0.52 | -0.39 / -0.60 | both halves | 6e-05 |  |
| [[NXT2]] | -0.52 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[PGRMC1]] | -0.49 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[FKBP1A]] | -0.49 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[YWHAZ]] | -0.48 | -0.40 / -0.55 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF329]] | B | ZNF329 activity raises ZSWIM9's level | lines that do not express ZNF329 (7) vs lines expressing it (43) | 1.49× lower at baseline in the lines without ZNF329 | 0.073 | ⚠ within organs, on part of the lines; also absent: C2orf27A |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.538). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-35.1, -8.4); signed map (-16.9, -13.3). **Vector** length 70.4, 12.0% of its response variance represented; |z| ≥ 3 in 841 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +4.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +4.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +4.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.8 | +3.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.5 | +3.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.2 | -6.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.4 | -3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -0.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -1.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -1.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.8 | -1.0 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.6 | -2.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.6 | -1.8 |
|  | [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | -1.6 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger SWIM-type containing 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:48,170,680-48,197,620 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LOC374920; previously C19orf68 |
| Gene groups (HGNC) | Zinc fingers SWIM-type |
| Matched by | ensembl_id |

UniProt [Q86XI8](https://www.uniprot.org/uniprotkb/Q86XI8) carries no function annotation.

**Summary**, from NCBI Gene [374920](https://www.ncbi.nlm.nih.gov/gene/374920):

> Predicted to act upstream of or within hematopoietic progenitor cell differentiation. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:34495](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34495) · Entrez [374920](https://www.ncbi.nlm.nih.gov/gene/374920) · UniProt [Q86XI8](https://www.uniprot.org/uniprotkb/Q86XI8) · Ensembl [ENSG00000185453](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185453)

## Data

Gene col 11679: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11679); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11679, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11679]; `tensor/DDL_lfc|DDL_z.npy` [11679]; `embed/gene_vectors.npy` [11679]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11679 or target_col == 11679). Every well: [[ZSWIM9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZSWIM9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
