---
symbol: "ACD"
type: "gene"
col: 2297
ensembl_id: "ENSG00000102977"
name: "ACD shelterin complex subunit and telomerase recruitment factor"
location: "16q22.1"
module: 2
arm: "+"
pooled_cpm: 6.4
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 8
n_dd_up_clean: 3
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# ACD

*ACD shelterin complex subunit and telomerase recruitment factor* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.50× (z +8.7, q 1e-15, up in 9 of 12 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.77× (z +8.0, q 2e-13, up in 28 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.588× (z -5.3, q 6e-05, down in 22 of 45 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRWD1]] (+0.63, fdr 1e-05), [[LMF2]] (+0.60, fdr 1e-05), [[RIC8A]] (+0.59, fdr 1e-05); moves opposite to [[LUC7L3]] (-0.47, fdr 3e-04), [[ENSA]] (-0.45, fdr 2e-04), [[STAG3L4-1]] (-0.44, fdr 1e-04).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 10 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2297.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.50×** | +8.7 | 1e-15 | 9/12 (SW480, SNU-423, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **2.26×** | +8.1 | 2e-13 | 15/26 (SW1417, A498, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +8.0 | 2e-13 | 28/42 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~20% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.83×** | +6.0 | 3e-07 | 25/47 (SW480, NCI-H460, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **1.53×** | +4.2 | 0.003 | 12/34 (SW1417, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.53×** | +4.2 | 0.003 | 18/46 (SW480, NCI-H460, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **1.44×** | +3.6 | 0.023 | 12/47 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.45×** | +3.5 | 0.033 | 15/36 (RKO, A498, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.42×** | +3.3 | 0.052 | 9/45 (PANC-1, SNU-423, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.42×** | +3.3 | 0.052 | 16/40 (SW480, NCI-H460, …) | rises with dose | position effect removed |
| [[NG25 (drug)]] 0.05 µM |  | **1.40×** | +3.1 | 0.088 | 8/44 (HS-578T, SNU-423, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.25×** | +3.1 | 0.088 | 7/47 (SW480, PANC-1, …) | top dose only |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.38× | +3.0 | 0.10 | 9/45 (A-427, BT-474, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2297.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.588×** | -5.3 | 6e-05 | 22/45 (H4, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.602×** | -5.1 | 9e-05 | 24/47 (SNU-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.664×** | -4.1 | 0.007 | 17/45 (NCI-H1792, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.657×** | -4.1 | 0.007 | 16/43 (SW48, A-427, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.784×** | -3.5 | 0.057 | 18/47 (MIA PaCa-2, H4, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.713×** | -3.4 | 0.062 | 16/44 (COLO 205, HCT15, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.534×** | -3.3 | 0.081 | 10/41 (A-427, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.708×** | -3.2 | 0.092 | 7/47 (SW480, C-33 A, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.51 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2297. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 4.73 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0873× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 4.41 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0634× (z -9.9) |
| [[A-172 (line)]] | wt | 8.76 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.03 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.08 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.35 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.17 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.00 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.77 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.62 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2297), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRWD1]] | +0.63 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[LMF2]] | +0.60 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[RIC8A]] | +0.59 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[SLC10A3]] | +0.56 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[TINF2]] | +0.56 | +0.59 / +0.43 | both halves | 3e-05 | same gene group; pathway: Base Excision Repair; STRING 999 |
| [[UCK1]] | +0.56 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[DCLRE1B]] | +0.56 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[MAPK7]] | +0.54 | +0.49 / +0.44 | both halves | 3e-05 | pathway: Cellular Senescence |
| [[TEDC1]] | +0.53 | +0.46 / +0.60 | both halves | 3e-05 |  |
| [[RECQL4]] | +0.53 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[UROD]] | +0.52 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[GTF3C5]] | +0.52 | +0.44 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LUC7L3]] | -0.47 | -0.28 / -0.47 | both halves | 3e-04 |  |
| [[ENSA]] | -0.45 | -0.31 / -0.39 | both halves | 2e-04 |  |
| [[STAG3L4-1]] | -0.44 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[PABPN1]] | -0.44 | -0.43 / -0.22 | both halves | 6e-04 |  |
| [[EMC10]] | -0.44 | -0.16 / -0.56 | ⚠ one half (not replicated) | 0.001 |  |
| [[COX7B]] | -0.43 | -0.57 / -0.19 | ⚠ one half (not replicated) | 9e-04 |  |
| [[NUP42]] | -0.43 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[MED28]] | -0.42 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[PPA2]] | -0.42 | -0.35 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ACD's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.344). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-29.7, -12.3); signed map (-25.6, 3.4). **Vector** length 53.5, 7.71% of its response variance represented; |z| ≥ 3 in 728 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +8.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | +2.8 | +4.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +2.0 | +6.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +2.0 | +3.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +2.0 | +3.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.8 | +2.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +2.7 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.7 | +1.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.4 | +1.7 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.2 | +1.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -3.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -3.5 | -3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.3 | -4.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -5.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.1 | -2.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.8 | -1.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.7 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -3.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.3 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | ACD shelterin complex subunit and telomerase recruitment factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:67,657,512-67,660,810 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Ptop, Pip1, Tpp1, Tint1 |
| Gene groups (HGNC) | Shelterin complex |
| Reactome | 28 pathways, smallest: Telomere C-strand synthesis initiation; Removal of the Flap Intermediate from the C-strand; Packaging Of Telomere Ends |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96AP0](https://www.uniprot.org/uniprotkb/Q96AP0) (Adrenocortical dysplasia protein homolog):

> Component of the shelterin complex (telosome) that is involved in the regulation of telomere length and protection. Shelterin associates with arrays of double-stranded TTAGGG repeats added by telomerase and protects chromosome ends. Without its protective activity, telomeres are no longer hidden from the DNA damage surveillance and chromosome ends are inappropriately processed by DNA repair pathways. Promotes binding of POT1 to single-stranded telomeric DNA. Modulates the inhibitory effects of …

**Summary**, from NCBI Gene [65057](https://www.ncbi.nlm.nih.gov/gene/65057):

> This gene encodes a protein that is involved in telomere function. This protein is one of six core proteins in the telosome/shelterin telomeric complex, which functions to maintain telomere length and to protect telomere ends. Through its interaction with other components, this protein plays a key role in the assembly and stabilization of this complex, and it mediates the access of telomerase to the telomere. Multiple transcript variants encoding different isoforms have been found for this …

**Accessions** — [HGNC:25070](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25070) · Entrez [65057](https://www.ncbi.nlm.nih.gov/gene/65057) · UniProt [Q96AP0](https://www.uniprot.org/uniprotkb/Q96AP0) · Ensembl [ENSG00000102977](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102977)

## Data

Gene col 2297: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2297); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2297, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2297]; `tensor/DDL_lfc|DDL_z.npy` [2297]; `embed/gene_vectors.npy` [2297]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2297 or target_col == 2297). Every well: [[ACD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
