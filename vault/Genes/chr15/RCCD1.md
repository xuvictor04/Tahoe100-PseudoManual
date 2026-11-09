---
symbol: "RCCD1"
type: "gene"
col: 9396
ensembl_id: "ENSG00000166965"
name: "RCC1 domain containing 1"
location: "15q26.1"
module: 67
arm: "+"
pooled_cpm: 11.02
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 8
n_dd_up_clean: 3
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# RCCD1

*RCC1 domain containing 1* — 15q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.60× (z +6.2, q 3e-07, up in 19 of 36 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[vincristine (drug)]] 0.5 µM: 1.45× (z +3.5, q 0.062, up in 11 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.690× (z -6.9, q 3e-09, down in 26 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AURKB]] (+0.65, fdr 1e-05), [[GTSE1]] (+0.64, fdr 1e-05), [[KIF18B]] (+0.64, fdr 8e-06); moves opposite to [[ATP6V1G1]] (-0.51, fdr 5e-05).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9396.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.60×** | +6.2 | 3e-07 | 19/36 (A498, LS 180, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.57×** | +5.5 | 1e-05 | 12/27 (HT-29, SW480, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.52×** | +5.3 | 2e-05 | 10/20 (SW1417, HS-578T, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +4.1 | 0.005 | 14/39 (NCI-H1573, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **1.45×** | +3.5 | 0.062 | 11/43 (MIA PaCa-2, SNU-423, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.44×** | +3.4 | 0.062 | 9/42 (NCI-H2030, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 1.19× | +3.3 | 0.085 | 9/47 (NCI-H2030, HOP62, …) | top dose only |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.41×** | +3.2 | 0.094 | 3/44 (NCI-H2030, HOP62, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9396.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.690×** | -6.9 | 3e-09 | 26/44 (PANC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.694×** | -4.8 | 4e-04 | 21/43 (PANC-1, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.711×** | -4.3 | 0.003 | 16/45 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.725×** | -4.2 | 0.003 | 20/46 (H4, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.515×** | -4.2 | 0.003 | 11/46 (HOP62, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.729×** | -4.2 | 0.003 | 15/46 (PANC-1, J82, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.735×** | -4.1 | 0.004 | 16/45 (H4, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.601×** | -3.2 | 0.091 | 9/42 (J82, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9396. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 9.99 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0375× (z -11.3) |
| [[PANC-1 (line)]] | alt | 12.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -11.9) |
| [[SW48 (line)]] | wt | 17.9 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0834× (z -9.4) |
| [[A-427 (line)]] | wt | 8.99 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.180× (z -8.8) |
| [[A498 (line)]] | wt | 12.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.68× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A549 (line)]] | wt | 13.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -9.4) |
| [[COLO 205 (line)]] | alt | 10.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -10.5) |
| [[HCT15 (line)]] | alt | 17.6 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.110× (z -9.9) |
| [[SK-MEL-2 (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -12.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 6.71 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0948× (z -9.6) |
| [[A-172 (line)]] | wt | 9.56 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.43 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.69 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.47 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.12 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.97 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.22 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.87 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9396), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AURKB]] | +0.65 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[GTSE1]] | +0.64 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[KIF18B]] | +0.64 | +0.63 / +0.58 | both halves | 8e-06 |  |
| [[OIP5]] | +0.62 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[PARPBP]] | +0.62 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[PAK6]] | +0.61 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[CDCA3]] | +0.61 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[KIF2C]] | +0.61 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[CIT]] | +0.60 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[DEPDC1B]] | +0.60 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[FAM83D]] | +0.60 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[CDCA8]] | +0.60 | +0.61 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V1G1]] | -0.51 | -0.49 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises RCCD1's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 1.50× lower at baseline in the lines without PIMREG | 0.027 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[NDC80]] | C | NDC80 activity raises RCCD1's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 1.95× lower at baseline in the lines without NDC80 | 0.038 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises RCCD1's level | lines that do not express AURKB (4) vs lines expressing it (46) | 1.70× lower at baseline in the lines without AURKB | 0.080 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[SAPCD2]] | C | SAPCD2 activity raises RCCD1's level | lines that do not express SAPCD2 (3) vs lines expressing it (47) | 2.07× lower at baseline in the lines without SAPCD2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.641). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-35.2, -55.7); signed map (-49.0, -41.0). **Vector** length 55.2, 7.93% of its response variance represented; |z| ≥ 3 in 761 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.54 to 12); *G2/M checkpoint* (hallmark, mean cos +0.53 to 9); *Mitotic Prometaphase* (reactome, mean cos +0.54 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.7 | +4.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +3.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +1.8 | +5.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.6 | +1.6 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +1.6 | +3.3 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +1.3 | +2.3 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.3 | +2.7 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.2 | +1.9 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.2 | +2.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.0 | -4.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.3 | -4.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.2 | -4.3 |
|  | [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -2.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -1.9 |
|  | [[Erlotinib (drug)]] 5 µM |  | -1.2 | -1.1 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.2 | -2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.1 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -1.8 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | -1.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | RCC1 domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.1 — chr15:90,954,881-90,963,125 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC14386 |
| Reactome | 2 pathways, smallest: Protein hydroxylation; Gamma carboxylation, hypusinylation, hydroxylation, and arylsulfatase activation |
| Matched by | ensembl_id |

**Function**, from UniProt [A6NED2](https://www.uniprot.org/uniprotkb/A6NED2) (RCC1 domain-containing protein 1):

> Plays a role in transcriptional repression of satellite repeats, possibly by regulating H3K36 methylation levels in centromeric regions together with KDM8. Possibly together with KDM8, is involved in proper mitotic spindle organization and chromosome segregation. Plays a role in regulating alpha-tubulin deacetylation and cytoskeletal microtubule stability, thereby promoting cell migration and TGF-beta-induced epithelial to mesenchymal transition (EMT), potentially through the inhibition of KDM8.

**Summary**, from NCBI Gene [91433](https://www.ncbi.nlm.nih.gov/gene/91433):

> Predicted to be involved in chromatin organization. Located in cytosol and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30457](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30457) · Entrez [91433](https://www.ncbi.nlm.nih.gov/gene/91433) · UniProt [A6NED2](https://www.uniprot.org/uniprotkb/A6NED2) · Ensembl [ENSG00000166965](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166965)

## Data

Gene col 9396: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9396); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9396, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9396]; `tensor/DDL_lfc|DDL_z.npy` [9396]; `embed/gene_vectors.npy` [9396]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9396 or target_col == 9396). Every well: [[RCCD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RCCD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
