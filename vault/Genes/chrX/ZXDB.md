---
symbol: "ZXDB"
type: "gene"
col: 12594
ensembl_id: "ENSG00000198455"
name: "zinc finger X-linked duplicated B"
location: "Xp11.21"
module: 7
arm: "+"
pooled_cpm: 7.67
n_lines_expressing: 49
n_dd_up: 9
n_dd_down: 12
n_dd_up_clean: 9
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# ZXDB

*zinc finger X-linked duplicated B* — Xp11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.55× (z +10.0, q 1e-20, up in 35 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.242× (z -15.1, q 0e+00, down in 44 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZXDA]] (+0.88, fdr 7e-06), [[POLR2M]] (+0.78, fdr 7e-06), [[ZNF543]] (+0.77, fdr 7e-06); moves opposite to [[METRN]] (-0.76, fdr 7e-06), [[CBFA2T2]] (-0.76, fdr 7e-06), [[COX6A1]] (-0.75, fdr 7e-06).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ZNF391]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12594.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.55×** | +10.0 | 1e-20 | 35/41 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.75×** | +8.4 | 9e-15 | 28/42 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.89×** | +6.8 | 2e-09 | 31/45 (HOP62, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.70×** | +5.7 | 2e-06 | 27/44 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.55×** | +4.7 | 3e-04 | 17/45 (KATO III, NCI-H460, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.53×** | +4.4 | 0.001 | 18/44 (A498, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.96×** | +3.8 | 0.014 | 13/44 (MIA PaCa-2, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Folic acid (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.027 | 8/47 (NCI-H1573, NCI-H1792, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.39×** | +3.3 | 0.068 | 15/42 (A-172, RKO, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | 1.74× | +3.1 | 0.11 | 8/42 (MIA PaCa-2, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12594.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.242×** | -15.1 | 0e+00 | 44/46 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.250×** | -14.7 | 0e+00 | 45/45 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.302×** | -12.7 | 8e-35 | 42/46 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.495×** | -7.5 | 1e-11 | 36/46 (LoVo, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.524×** | -6.9 | 8e-10 | 24/41 (HepG2/C3A, LS 180, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.828×** | -6.8 | 1e-09 | 32/47 (SHP-77, RPMI-7951, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.676×** | -5.9 | 3e-07 | 25/42 (Hs 766T, NCI-H23, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.725×** | -4.8 | 1e-04 | 24/46 (MIA PaCa-2, PANC-1, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.644×** | -4.7 | 2e-04 | 19/41 (KATO III, SNU-1, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.488×** | -4.0 | 0.004 | 16/45 (MIA PaCa-2, Hs 766T, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.700×** | -3.6 | 0.015 | 18/43 (RKO, NCI-H23, …) | top dose only |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **0.665×** | -3.1 | 0.096 | 8/43 (KATO III, LoVo, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | 0.743× | -3.0 | 0.11 | 13/42 (A-427, SNU-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.56 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12594. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 15.8 | 0 | 4 | — | [[Belinostat (drug)]] 0.5 µM 0.138× (z -11.1) |
| [[HOP62 (line)]] | alt | 6.25 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 5.10× (z +10.2) | [[Belinostat (drug)]] 5 µM 0.109× (z -9.8) |
| [[LoVo (line)]] | wt | 8.93 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.0980× (z -12.4) |
| [[MIA PaCa-2 (line)]] | alt | 13.4 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.104× (z -12.2) |
| [[NCI-H460 (line)]] | wt | 7.43 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.159× (z -10.6) |
| [[SW480 (line)]] | alt | 11.1 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.105× (z -14.6) |
| [[HepG2_C3A (line)]] | wt | 12.1 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0306× (z -13.8) |
| [[RKO (line)]] | wt | 12.0 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0647× (z -11.5) |
| [[A-172 (line)]] | wt | 7.44 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.150× (z -9.0) |
| [[A498 (line)]] | wt | 6.27 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +9.8) | — |
| [[A549 (line)]] | wt | 7.22 | 0 | 1 | — | [[Mifepristone (drug)]] 0.05 µM 0.0544× (z -10.9) |
| [[HEC-1-A (line)]] | alt | 6.01 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0463× (z -14.5) |
| [[Hs 766T (line)]] | wt | 12.1 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0922× (z -10.3) |
| [[LS 180 (line)]] | wt | 6.67 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.130× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[Panc 03.27 (line)]] | alt | 8.64 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0793× (z -11.6) |
| [[PANC-1 (line)]] | alt | 7.50 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.204× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 6.29 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0876× (z -8.8) |
| [[SHP-77 (line)]] | alt | 10.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.138× (z -8.5) |
| [[SNU-423 (line)]] | alt | 11.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.105× (z -10.2) |
| [[A-427 (line)]] | wt | 7.68 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.08 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.613 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.67 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12594), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZXDA]] | +0.88 | +0.84 / +0.79 | both halves | 7e-06 | same gene group |
| [[POLR2M]] | +0.78 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[ZNF543]] | +0.77 | +0.72 / +0.74 | both halves | 7e-06 | same gene group |
| [[UBQLN2]] | +0.77 | +0.77 / +0.70 | both halves | 7e-06 |  |
| [[ZNF507]] | +0.76 | +0.70 / +0.66 | both halves | 7e-06 | same gene group |
| [[TRMT5]] | +0.76 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[KICS2]] | +0.75 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[CENPBD1P]] | +0.75 | +0.77 / +0.62 | both halves | 7e-06 |  |
| [[RIMOC1]] | +0.75 | +0.79 / +0.68 | both halves | 7e-06 |  |
| [[ZBTB33]] | +0.74 | +0.60 / +0.76 | both halves | 7e-06 | same gene group |
| [[RNF6]] | +0.74 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[ZNF614]] | +0.73 | +0.72 / +0.64 | both halves | 7e-06 | same gene group |

## Genes that move opposite

*29 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METRN]] | -0.76 | -0.73 / -0.61 | both halves | 7e-06 |  |
| [[CBFA2T2]] | -0.76 | -0.72 / -0.60 | both halves | 7e-06 |  |
| [[COX6A1]] | -0.75 | -0.66 / -0.61 | both halves | 7e-06 |  |
| [[SDHAP2]] | -0.75 | -0.72 / -0.65 | both halves | 7e-06 |  |
| [[UQCRH]] | -0.72 | -0.63 / -0.66 | both halves | 7e-06 |  |
| [[SEC11A]] | -0.72 | -0.67 / -0.60 | both halves | 7e-06 |  |
| [[SDHAP1]] | -0.70 | -0.68 / -0.55 | both halves | 1e-05 |  |
| [[UBL5]] | -0.70 | -0.68 / -0.60 | both halves | 7e-06 |  |
| [[GMCL1]] | -0.70 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[PTMAP2]] ⚠ | -0.69 | -0.71 / -0.63 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[HDAC3]] | -0.69 | -0.66 / -0.55 | both halves | 1e-05 |  |
| [[SH3GL1]] | -0.69 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[PTMA]] | -0.69 | -0.66 / -0.60 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF391]] | B | ZNF391 activity raises ZXDB's level | lines that do not express ZNF391 (5) vs lines expressing it (45) | 1.27× lower at baseline in the lines without ZNF391 | 0.080 | ⚠ within organs, on part of the lines; also absent: LINC00159, ENSG00000283491, ASIC1; maybe low, not absent |
| [[ZNF528]] | B | ZNF528 activity raises ZXDB's level | lines that do not express ZNF528 (21) vs lines expressing it (29) | 1.15× lower at baseline in the lines without ZNF528 | 0.099 | ⚠ within organs, on part of the lines; also absent: ZNF528-AS1, ZNF625, ZNF880 |
| [[ZNF710-AS1]] | C | ZNF710-AS1's natural level strengthens ZXDB's drug response | ZNF710-AS1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.26; direction not clear | 0.041 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[CFL2]] | C | CFL2 activity raises ZXDB's level | lines that do not express CFL2 (4) vs lines expressing it (45) | 2.01× lower at baseline in the lines without CFL2 | 0.089 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: TPST1, SLC35F1, ITGA2B; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.684). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-32.3, 12.7); signed map (3.7, -30.0). **Vector** length 85.7, 16.7% of its response variance represented; |z| ≥ 3 in 1,016 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.8 | +10.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.9 | +8.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.5 | +6.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.2 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.4 | +5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | -0.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.1 | +4.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.9 | +3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.8 | +3.1 |
| fall | [[Belinostat (drug)]] 5 µM |  | -4.5 | -12.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.4 | -15.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.2 | -14.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | -4.0 | -6.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.4 | -7.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -4.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.5 | -2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | -4.0 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -1.9 | -2.3 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -1.9 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger X-linked duplicated B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.21 — chrX:57,592,011-57,597,477 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ZNF905 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Matched by | ensembl_id |

**Function**, from UniProt [P98169](https://www.uniprot.org/uniprotkb/P98169) (Zinc finger X-linked protein ZXDB):

> Cooperates with CIITA to promote transcription of MHC class I and MHC class II genes.

**Summary**, from NCBI Gene [158586](https://www.ncbi.nlm.nih.gov/gene/158586):

> The ZXDB gene is one of a pair of duplicated zinc finger genes on chromosome Xp11.21 (Greig et al., 1993 [PubMed 8268913]); see also ZXDA (MIM 300235).[supplied by OMIM, Jul 2010]

**Accessions** — [HGNC:13199](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13199) · Entrez [158586](https://www.ncbi.nlm.nih.gov/gene/158586) · UniProt [P98169](https://www.uniprot.org/uniprotkb/P98169) · Ensembl [ENSG00000198455](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198455)

## Data

Gene col 12594: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12594); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12594, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12594]; `tensor/DDL_lfc|DDL_z.npy` [12594]; `embed/gene_vectors.npy` [12594]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12594 or target_col == 12594). Every well: [[ZXDB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZXDB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
