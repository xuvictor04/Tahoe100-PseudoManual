---
symbol: "ANAPC1P2"
type: "gene"
col: 13787
ensembl_id: "ENSG00000231259"
name: "ANAPC1 pseudogene 2"
location: "2p11.2"
module: 69
arm: "+"
pooled_cpm: 5.59
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 16
n_dd_up_clean: 13
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# ANAPC1P2

*ANAPC1 pseudogene 2* — 2p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.86× (z +10.2, q 2e-21, up in 27 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 5 µM: 0.443× (z -5.3, q 8e-05, down in 16 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHL24]] (+0.70, fdr 7e-06), [[LINC01881]] (+0.66, fdr 3e-05), [[TCP11L2]] (+0.62, fdr 1e-05); moves opposite to [[ASMTL-AS1]] (-0.57, fdr 3e-05), [[EIF4G1]] (-0.52, fdr 4e-05), [[WDR77]] (-0.52, fdr 4e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC00598]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13787.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.86×** | +10.2 | 2e-21 | 27/41 (A498, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.77×** | +7.0 | 7e-10 | 23/47 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.64×** | +6.0 | 3e-07 | 18/47 (LoVo, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +5.2 | 2e-05 | 13/33 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.9 | 1e-04 | 13/39 (A-172, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.51×** | +4.8 | 2e-04 | 17/43 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +4.7 | 3e-04 | 11/36 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.44×** | +4.5 | 5e-04 | 15/46 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.00×** | +4.4 | 6e-04 | 8/23 (LoVo, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.97×** | +4.3 | 8e-04 | 6/44 (SW480, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.42×** | +4.1 | 0.002 | 7/44 (A-427, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +3.8 | 0.007 | 9/47 (SW1417, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.34×** | +3.6 | 0.015 | 14/38 (SW1417, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.025 | 8/47 (SW1417, Panc 03.27, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.67×** | +3.3 | 0.036 | 1/43 (NCI-H23) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13787.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.443×** | -5.3 | 8e-05 | 16/36 (NCI-H2030, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.666×** | -5.0 | 1e-04 | 18/47 (A498, BT-474, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.678×** | -4.8 | 3e-04 | 15/27 (SW480, SW1417, …) | inconsistent across doses | composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.505×** | -4.4 | 0.001 | 13/38 (NCI-H460, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.554×** | -3.8 | 0.014 | 11/32 (NCI-H460, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.729×** | -3.8 | 0.014 | 6/46 (RPMI-7951, HepG2/C3A, …) | inconsistent across doses | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.561×** | -3.7 | 0.014 | 8/36 (A498, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.747×** | -3.5 | 0.038 | 6/46 (CHP-212, RKO, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.753×** | -3.4 | 0.046 | 12/43 (MIA PaCa-2, NCI-H1573, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.598×** | -3.3 | 0.046 | 5/43 (AsPC-1, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.750×** | -3.3 | 0.046 | 13/39 (A549, SNU-423, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[EX229 (drug)]] 0.5 µM |  | **0.681×** | -3.3 | 0.046 | 7/45 (LOX-IMVI, SW1417, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Allantoin (drug)]] 0.5 µM |  | **0.777×** | -3.2 | 0.070 | 11/39 (LS 180, Panc 03.27, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.695×** | -3.1 | 0.071 | 2/47 (AsPC-1, A498) | rises with dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.833×** | -3.0 | 0.090 | 11/48 (A498, NCI-H1573, …) | top dose only |  |
| [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM |  | **0.770×** | -3.0 | 0.091 | 9/42 (BT-474, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13787. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 5.73 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.103× (z -9.1) ⚠ transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.05 µM 0.105× (z -8.8) |
| [[SW480 (line)]] | alt | 8.53 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0946× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[CFPAC-1 (line)]] | alt | 3.37 | 0 | 1 | — | [[Sulfatinib (drug)]] 0.05 µM 0.0649× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 8.02 | 0 | 1 | — | [[Bimatoprost (drug)]] 0.5 µM 0.0794× (z -8.7) |
| [[J82 (line)]] | alt | 3.06 | 0 | 1 | — | [[Ligustrazine (drug)]] 0.05 µM 0.0463× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 4.01 | 0 | 1 | — | [[Regorafenib (drug)]] 0.05 µM 0.0517× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 5.92 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0719× (z -10.5) |
| [[SNU-423 (line)]] | alt | 5.39 | 0 | 1 | — | [[Penfluridol (drug)]] 0.5 µM 0.0913× (z -9.1) |
| [[SW1417 (line)]] | alt | 13.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[A-172 (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.84 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.36 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.37 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.17 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.56 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.74 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13787), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL24]] | +0.70 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[LINC01881]] | +0.66 | +0.46 / +0.74 | both halves | 3e-05 |  |
| [[TCP11L2]] | +0.62 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[FBXO25]] | +0.62 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[PIK3CA]] | +0.61 | +0.67 / +0.49 | both halves | 1e-05 |  |
| [[UBR2]] | +0.61 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[JMY]] | +0.61 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[FBXL20]] | +0.60 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[HACL1]] | +0.58 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[HDAC5]] | +0.57 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[KBTBD3]] | +0.57 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[SARAF]] | +0.57 | +0.36 / +0.64 | both halves | 1e-04 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASMTL-AS1]] | -0.57 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[EIF4G1]] | -0.52 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[WDR77]] | -0.52 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[TTPAL]] | -0.52 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[GRWD1]] | -0.51 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[SOCS4]] | -0.50 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[EBNA1BP2]] | -0.50 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[PPIL1]] | -0.50 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[EIPR1]] | -0.50 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[HARS1]] | -0.49 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[AP1B1]] | -0.49 | -0.41 / -0.38 | both halves | 6e-05 |  |
| [[SNRPB]] | -0.48 | -0.50 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00598]] | B | LINC00598 activity raises ANAPC1P2's level | lines that do not express LINC00598 (5) vs lines expressing it (45) | 1.27× lower at baseline in the lines without LINC00598 | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000288542, FOXO1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.625). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (4.5, -45.2); signed map (-18.3, 10.7). **Vector** length 51.0, 6.54% of its response variance represented; |z| ≥ 3 in 859 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[GSK1059615 (drug)]] 5 µM |  | +1.5 | +4.3 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +1.3 | +0.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.2 | +1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +1.1 | +1.2 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +1.1 | +2.6 |
|  | [[Terfenadine (drug)]] 5 µM |  | +0.9 | +1.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.1 | -5.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.0 | -4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -3.0 |
|  | [[EX229 (drug)]] 5 µM |  | -2.8 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -3.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.6 | -5.3 |

## What is on record

|  |  |
|---|---|
| Name | ANAPC1 pseudogene 2 |
| Locus type | pseudogene |
| Location | 2p11.2 — chr2:87,031,815-87,052,992 (-) |
| Ensembl biotype | unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:54708](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:54708) · Entrez [285074](https://www.ncbi.nlm.nih.gov/gene/285074) · Ensembl [ENSG00000231259](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000231259)

## Data

Gene col 13787: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13787); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13787, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13787]; `tensor/DDL_lfc|DDL_z.npy` [13787]; `embed/gene_vectors.npy` [13787]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13787 or target_col == 13787). Every well: [[ANAPC1P2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANAPC1P2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
