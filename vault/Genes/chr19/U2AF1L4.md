---
symbol: "U2AF1L4"
type: "gene"
col: 8425
ensembl_id: "ENSG00000161265"
name: "U2 small nuclear RNA auxiliary factor 1 like 4"
location: "19q13.12"
module: 12
arm: "+"
pooled_cpm: 3.16
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 7
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# U2AF1L4

*U2 small nuclear RNA auxiliary factor 1 like 4* — 19q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.05× (z +9.5, q 2e-18, up in 23 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.601× (z -6.8, q 6e-09, down in 25 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF446]] (+0.68, fdr 8e-06), [[DXO]] (+0.67, fdr 1e-05), [[OGFOD2]] (+0.65, fdr 2e-05); moves opposite to [[ATP5MC3]] (-0.56, fdr 4e-05, ⚠ ATP5MC3 in the vector space only through flagged drug-doses), [[BRI3BP]] (-0.53, fdr 8e-05), [[C1QBP]] (-0.51, fdr 1e-04), [[CHML]] (-0.51, fdr 9e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8425.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.05×** | +9.5 | 2e-18 | 23/32 (NCI-H2030, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.69×** | +9.0 | 8e-17 | 2/5 (PANC-1, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.08×** | +6.9 | 1e-09 | 6/16 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.67×** | +4.8 | 2e-04 | 8/19 (PANC-1, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.40×** | +4.4 | 0.001 | 10/35 (NCI-H1573, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.40×** | +4.3 | 0.002 | 1/5 (PANC-1) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.54×** | +3.7 | 0.016 | 2/5 (HS-578T, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.77×** | +3.6 | 0.027 | 2/28 (PANC-1, BT-474) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.64× | +3.1 | 0.12 | 2/31 (HEC-1-A, SW480) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 1.87× | +3.1 | 0.12 | 0/6 | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8425.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.601×** | -6.8 | 6e-09 | 25/44 (A498, NCI-H1573, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.500×** | -6.6 | 1e-08 | 23/46 (HS-578T, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.594×** | -5.0 | 1e-04 | 19/44 (H4, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.638×** | -4.3 | 0.003 | 17/42 (PANC-1, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.689×** | -3.6 | 0.042 | 13/44 (SW1417, NCI-H2347, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.514×** | -3.3 | 0.082 | 6/29 (NCI-H2347, HS-578T, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.709×** | -3.3 | 0.082 | 11/46 (SW1417, C-33 A, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | 0.721× | -3.1 | 0.12 | 11/39 (C32, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8425. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 4.64 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0676× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change |
| [[HT-29 (line)]] | alt | 4.64 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0795× (z -9.5) ⚠ cell-cycle shift, explains ~13% of this change |
| [[LOX-IMVI (line)]] | wt | 2.14 | 0 | 1 | — | [[Clotrimazole (drug)]] 5 µM 0.113× (z -8.8) |
| [[A-172 (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.70 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.954 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.57 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8425), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF446]] | +0.68 | +0.58 / +0.67 | both halves | 8e-06 |  |
| [[DXO]] | +0.67 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[OGFOD2]] | +0.65 | +0.48 / +0.72 | both halves | 2e-05 |  |
| [[ZNF213]] | +0.63 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[PEF1]] | +0.62 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[ZFAND2B]] | +0.62 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[ARFGAP2]] | +0.61 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[WASHC1]] | +0.60 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[C19orf54]] | +0.60 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[CCDC115]] | +0.59 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[CIRBP]] | +0.59 | +0.63 / +0.49 | both halves | 1e-05 | same gene group |
| [[SH2B1]] | +0.57 | +0.50 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP5MC3]] ⚠ | -0.56 | -0.54 / -0.41 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[BRI3BP]] | -0.53 | -0.58 / -0.37 | both halves | 8e-05 |  |
| [[C1QBP]] | -0.51 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[CHML]] | -0.51 | -0.36 / -0.49 | both halves | 9e-05 |  |
| [[DCBLD1]] | -0.50 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[GLO1]] | -0.50 | -0.20 / -0.66 | both halves | 7e-04 |  |
| [[HPSE]] | -0.49 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[RAB10]] | -0.48 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[FKBP1A]] | -0.48 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[CMTM1]] | -0.48 | -0.43 / -0.43 | both halves | 4e-05 |  |
| [[SERBP1]] | -0.48 | -0.25 / -0.47 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises U2AF1L4's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises U2AF1L4's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.398). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-12.3, 6.1); signed map (-7.1, -4.3). **Vector** length 49.0, 6.29% of its response variance represented; |z| ≥ 3 in 856 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +9.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +3.0 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +2.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.0 | +4.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.0 | +9.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +2.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.6 | +3.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +2.0 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.5 | +2.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -6.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.7 | -3.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -4.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.5 | -6.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | -2.4 |
|  | [[vincristine (drug)]] 0.05 µM |  | -1.1 | -2.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -1.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | U2 small nuclear RNA auxiliary factor 1 like 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.12 — chr19:35,742,464-35,745,445 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC33901, U2af26; previously U2AF1L3 |
| Gene groups (HGNC) | Zinc fingers CCCH-type; RNA binding motif containing |
| Reactome | 11 pathways, smallest: Transport of Mature mRNA derived from an Intron-Containing Transcript; Transport of Mature Transcript to Cytoplasm; mRNA Polyadenylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WU68](https://www.uniprot.org/uniprotkb/Q8WU68) (Splicing factor U2AF 26 kDa subunit):

> RNA-binding protein that function as a pre-mRNA splicing factor. Plays a critical role in both constitutive and enhancer-dependent splicing by mediating protein-protein interactions and protein-RNA interactions required for accurate 3'-splice site selection. Acts by enhancing the binding of U2AF2 to weak pyrimidine tracts. Also participates in the regulation of alternative pre-mRNA splicing. Activates exon 5 skipping of PTPRC during T-cell activation; an event reversed by GFI1. Binds to RNA at …

**Summary**, from NCBI Gene [199746](https://www.ncbi.nlm.nih.gov/gene/199746):

> Predicted to enable pre-mRNA 3'-splice site binding activity. Predicted to be involved in mRNA splicing, via spliceosome. Predicted to be located in nucleoplasm. Predicted to be part of U2AF complex and spliceosomal complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23020](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23020) · Entrez [199746](https://www.ncbi.nlm.nih.gov/gene/199746) · UniProt [Q8WU68](https://www.uniprot.org/uniprotkb/Q8WU68) · Ensembl [ENSG00000161265](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161265)

## Data

Gene col 8425: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8425); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8425, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8425]; `tensor/DDL_lfc|DDL_z.npy` [8425]; `embed/gene_vectors.npy` [8425]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8425 or target_col == 8425). Every well: [[U2AF1L4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/U2AF1L4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
