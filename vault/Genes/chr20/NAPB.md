---
symbol: "NAPB"
type: "gene"
col: 4665
ensembl_id: "ENSG00000125814"
name: "NSF attachment protein beta"
location: "20p11.21"
module: 190
arm: "+"
pooled_cpm: 25.35
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/190"]
generated_by: "tahoemap"
---

# NAPB

*NSF attachment protein beta* — 20p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.83× (z +6.5, q 5e-08, up in 41 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SW48 0.121×, RPMI-7951 0.175×, H4 0.144×, NCI-H1573 0.341×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change); [[Thymol (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0664×); [[Canagliflozin (drug)]] 0.05 µM in 1 line (BT-474 0.0982×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PMS2P3-1]] (+0.74, fdr 7e-06), [[WWP1]] (+0.72, fdr 7e-06), [[SEC61A2]] (+0.72, fdr 7e-06); moves opposite to [[PPP1R10]] (-0.69, fdr 7e-06), [[HES1]] (-0.68, fdr 7e-06), [[HELQ]] (-0.65, fdr 1e-05).
> It is in [[Module 190]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[FJX1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4665.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.83×** | +6.5 | 5e-08 | 41/47 (HOP62, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.76×** | +6.0 | 4e-07 | 32/48 (HOP62, PANC-1, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.68×** | +5.3 | 2e-05 | 35/48 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **1.53×** | +4.5 | 8e-04 | 27/48 (COLO 205, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.38×** | +3.5 | 0.063 | 21/48 (SNU-423, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.36×** | +3.3 | 0.075 | 16/47 (LOX-IMVI, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **1.80×** | +3.3 | 0.075 | 20/48 (SNU-1, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.38×** | +3.2 | 0.092 | 14/48 (MIA PaCa-2, NCI-H1573, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +3.2 | 0.092 | 15/48 (NCI-H2347, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | 1.33× | +3.1 | 0.11 | 16/48 (CFPAC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4665.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SW48 0.121×, RPMI-7951 0.175×, H4 0.144×, NCI-H1573 0.341×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change); [[Thymol (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0664×); [[Canagliflozin (drug)]] 0.05 µM in 1 line (BT-474 0.0982×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | 0.715× | -3.4 | 0.23 | 16/34 (MIA PaCa-2, SNU-423, …) | top dose only | composition shift |
| [[Carbamazepine (drug)]] 5 µM |  | 0.734× | -3.3 | 0.23 | 21/47 (NCI-H1573, J82, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 0.806× | -3.2 | 0.23 | 14/48 (RPMI-7951, C32, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.748× | -3.1 | 0.28 | 18/48 (A498, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4665. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 13.6 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0982× (z -9.9) |
| [[H4 (line)]] | wt | 20.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.144× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change |
| [[NCI-H1573 (line)]] | alt | 97.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.341× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change |
| [[NCI-H1792 (line)]] | alt | 16.3 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0664× (z -12.4) |
| [[RPMI-7951 (line)]] | alt | 42.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change |
| [[SW48 (line)]] | wt | 24.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change |
| [[A-172 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 62.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 37.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4665), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PMS2P3-1]] | +0.74 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[WWP1]] | +0.72 | +0.76 / +0.61 | both halves | 7e-06 |  |
| [[SEC61A2]] | +0.72 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[FHIP2A]] | +0.72 | +0.86 / +0.54 | both halves | 1e-05 |  |
| [[COPS7B]] | +0.67 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[RTCA]] | +0.67 | +0.73 / +0.51 | both halves | 1e-05 |  |
| [[RNPEP]] | +0.66 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[PMS2P3]] | +0.66 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[OTULIN]] | +0.65 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[CRYBB2P1]] | +0.65 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[PAQR3]] | +0.64 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[FBXO44]] | +0.64 | +0.72 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R10]] | -0.69 | -0.68 / -0.64 | both halves | 7e-06 |  |
| [[HES1]] | -0.68 | -0.63 / -0.64 | both halves | 7e-06 |  |
| [[HELQ]] | -0.65 | -0.71 / -0.55 | both halves | 1e-05 |  |
| [[DPH1-AS1]] | -0.65 | -0.69 / -0.60 | both halves | 7e-06 |  |
| [[BPTF]] | -0.64 | -0.62 / -0.63 | both halves | 7e-06 |  |
| [[EPC2]] | -0.64 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[ZNF274]] | -0.62 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[ZBTB38]] | -0.62 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[ARMC5]] | -0.62 | -0.67 / -0.60 | both halves | 7e-06 |  |
| [[ZNF75A]] | -0.61 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[EGR2]] | -0.60 | -0.67 / -0.50 | both halves | 1e-05 |  |
| [[RELB]] | -0.59 | -0.59 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FJX1]] | B | FJX1 activity raises NAPB's level | lines that do not express FJX1 (11) vs lines expressing it (39) | 1.31× lower at baseline in the lines without FJX1 | 0.029 | ⚠ within organs, on part of the lines; also absent: DYNC2H1, GIHCG, HDGFL3 |
| [[HDAC6]] | B | HDAC6 activity lowers NAPB's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers NAPB's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 190]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.873). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-9.0, -9.5); signed map (-31.2, -17.7). **Vector** length 84.6, 19.3% of its response variance represented; |z| ≥ 3 in 767 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +4.3 | +6.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | +4.1 | +5.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.9 | +6.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +2.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.8 | +1.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.2 | +2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +3.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -7.3 | -2.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.1 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.0 | -0.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -0.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -2.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.6 | -2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | +0.7 |
|  | [[Thymol (drug)]] 5 µM |  | -2.1 | -2.6 |
|  | [[Estrone sulfate (potassium) (drug)]] 5 µM |  | -2.0 | -1.9 |
|  | [[Apalutamide (drug)]] 0.5 µM |  | -2.0 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | NSF attachment protein beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p11.21 — chr20:23,374,519-23,421,519 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SNAP-BETA, SNAPB |
| Reactome | 12 pathways, smallest: Intra-Golgi traffic; Retrograde transport at the Trans-Golgi-Network; COPII-mediated vesicle transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H115](https://www.uniprot.org/uniprotkb/Q9H115) (Beta-soluble NSF attachment protein):

> Required for vesicular transport between the endoplasmic reticulum and the Golgi apparatus.

**Summary**, from NCBI Gene [63908](https://www.ncbi.nlm.nih.gov/gene/63908):

> This gene encodes a member of the soluble N-ethyl-maleimide-sensitive fusion attachment protein (SNAP) family. SNAP proteins play a critical role in the docking and fusion of vesicles to target membranes as part of the 20S NSF-SNAP-SNARE complex. This gene encodes the SNAP beta isoform which has been shown to be preferentially expressed in brain tissue. The encoded protein also interacts with the GluR2 &#945;-amino-3-hydroxy-5-methyl-4-isoxazolepropionate (AMPA) receptor subunit C-terminus and …

**Accessions** — [HGNC:15751](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15751) · Entrez [63908](https://www.ncbi.nlm.nih.gov/gene/63908) · UniProt [Q9H115](https://www.uniprot.org/uniprotkb/Q9H115) · Ensembl [ENSG00000125814](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125814)

## Data

Gene col 4665: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4665); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4665, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4665]; `tensor/DDL_lfc|DDL_z.npy` [4665]; `embed/gene_vectors.npy` [4665]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4665 or target_col == 4665). Every well: [[NAPB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NAPB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
