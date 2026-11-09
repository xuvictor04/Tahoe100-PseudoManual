---
symbol: "PHC1"
type: "gene"
col: 3276
ensembl_id: "ENSG00000111752"
name: "polyhomeotic homolog 1"
location: "12p13.31"
module: 57
arm: "+"
pooled_cpm: 9.74
n_lines_expressing: 46
n_dd_up: 3
n_dd_down: 3
n_dd_up_clean: 2
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# PHC1

*polyhomeotic homolog 1* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.32× (z +4.7, q 0.002, up in 14 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 1.28× (z +4.3, q 0.005, up in 10 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.545× (z -10.3, q 3e-22, down in 22 of 40 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB4A]] (+0.58, fdr 2e-05), [[SPATA6]] (+0.57, fdr 1e-05), [[SLC25A27]] (+0.57, fdr 4e-05); moves opposite to [[LINC03016]] (-0.53, fdr 5e-05), [[C3orf20]] (-0.53, fdr 9e-05), [[MIRLET7IHG]] (-0.53, fdr 6e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ASIC1]] → it (grade C ⚠); 3 go from it, the strongest it → [[TUBG2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3276.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.32×** | +4.7 | 0.002 | 14/41 (NCI-H1573, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.28×** | +4.3 | 0.005 | 10/43 (SW480, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.37×** | +3.8 | 0.023 | 4/39 (NCI-H460, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | 1.31× | +3.3 | 0.14 | 6/30 (NCI-H23, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[OTS514 (drug)]] 5 µM |  | 1.41× | +3.1 | 0.25 | 2/30 (NCI-H460, RKO) | inconsistent across doses | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | 1.28× | +3.0 | 0.25 | 4/39 (PANC-1, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3276.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.545×** | -10.3 | 3e-22 | 22/40 (HS-578T, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.715×** | -8.1 | 2e-13 | 20/41 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.903× | -6.1 | 2e-07 | 12/44 (LoVo, AN3 CA, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.804×** | -3.7 | 0.029 | 11/43 (NCI-H460, RKO, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.822× | -3.3 | 0.10 | 9/43 (HEC-1-A, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3276. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 35.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.131× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 6.93 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0878× (z -10.5) |
| [[NCI-H1573 (line)]] | alt | 13.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -11.9) |
| [[NCI-H23 (line)]] | alt | 33.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -14.7) |
| [[NCI-H460 (line)]] | wt | 6.62 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.201× (z -10.0) |
| [[AN3 CA (line)]] | alt | 23.4 | 0 | 1 (1 ⚠) | — | [[Fingolimod (hydrochloride) (drug)]] 5 µM 0.0559× (z -9.7) ⚠ toxic |
| [[C-33 A (line)]] | alt | 22.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.282× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 8.37 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.0867× (z -9.2) ⚠ toxic; unreliable plate only |
| [[PANC-1 (line)]] | alt | 7.42 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -10.5) |
| [[RPMI-7951 (line)]] | alt | 7.98 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.118× (z -8.5) |
| [[SHP-77 (line)]] | alt | 15.6 | 0 | 1 | — | [[ULK-101 (drug)]] 0.5 µM 0.0814× (z -9.5) |
| [[SNU-1 (line)]] | wt | 12.2 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.0994× (z -9.1) |
| [[SW480 (line)]] | alt | 8.54 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.242× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.66 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.63 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.54 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 8.56 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.37 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3276), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB4A]] | +0.58 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[SPATA6]] | +0.57 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[SLC25A27]] | +0.57 | +0.52 / +0.40 | both halves | 4e-05 |  |
| [[ZDHHC20]] | +0.57 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[ASIC1]] | +0.55 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[TBC1D2B]] | +0.55 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[C20orf96]] | +0.55 | +0.60 / +0.40 | both halves | 5e-05 |  |
| [[TM7SF3]] | +0.53 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[SSBP4]] | +0.53 | +0.63 / +0.34 | both halves | 1e-04 |  |
| [[FBXO44]] | +0.53 | +0.56 / +0.40 | both halves | 4e-05 |  |
| [[PCGF2]] | +0.52 | +0.66 / +0.41 | both halves | 4e-05 | pathway: SUMO E3 ligases SUMOylate target proteins; STRING 999 |
| [[PGAP1]] | +0.52 | +0.50 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC03016]] | -0.53 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[C3orf20]] | -0.53 | -0.61 / -0.36 | both halves | 9e-05 |  |
| [[MIRLET7IHG]] | -0.53 | -0.59 / -0.38 | both halves | 6e-05 |  |
| [[TMEM217]] | -0.52 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[SGSM3-AS1]] | -0.52 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[HCLS1]] | -0.51 | -0.59 / -0.37 | both halves | 8e-05 |  |
| [[SMIM12]] | -0.51 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[MYOCOS]] | -0.51 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[SLC22A1]] | -0.50 | -0.61 / -0.31 | both halves | 2e-04 |  |
| [[BTG3-AS1]] | -0.49 | -0.58 / -0.32 | both halves | 2e-04 |  |
| [[CHRNA10]] | -0.49 | -0.57 / -0.36 | both halves | 1e-04 |  |
| [[GARIN1A]] | -0.49 | -0.50 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASIC1]] | C | ASIC1 activity raises PHC1's level | lines that do not express ASIC1 (3) vs lines expressing it (47) | 2.84× lower at baseline in the lines without ASIC1 | 0.087 | ⚠ few lines (3 vs 47); across organs; also absent: TBC1D19, C1orf216, ZNF391 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TUBG2]] | C | PHC1 activity raises TUBG2's level | lines that do not express PHC1 (4) vs lines expressing it (46) | 1.95× lower at baseline in the lines without PHC1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HECTD2, TPST1, TBKBP1; its own permutation p |
| [[PILRA]] | C | PHC1 activity raises PILRA's level | lines that do not express PHC1 (4) vs lines expressing it (46) | 1.98× lower at baseline in the lines without PHC1 | 0.081 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HECTD2, TPST1, TBKBP1 |
| [[TMOD2]] | C | PHC1 activity raises TMOD2's level | lines that do not express PHC1 (4) vs lines expressing it (46) | 3.34× lower at baseline in the lines without PHC1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HECTD2, TPST1, TBKBP1; its own permutation p |

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.448). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (26.6, -8.3); signed map (-35.6, -11.9). **Vector** length 51.9, 6.78% of its response variance represented; |z| ≥ 3 in 702 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +2.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.3 | +2.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.1 | +4.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | +2.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.1 | +2.2 |
|  | [[Afatinib (drug)]] 5 µM |  | +1.0 | +1.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.0 | -8.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.7 | -10.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | -2.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.8 | -2.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.7 | -1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.5 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | polyhomeotic homolog 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:8,913,896-8,941,467 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HPH1, RAE28; previously EDR1 |
| Gene groups (HGNC) | Sterile alpha motif domain containing |
| Reactome | 20 pathways, smallest: SUMOylation of DNA methylation proteins; Transcriptional Regulation by E2F6; RUNX1 interacts with co-factors whose precise effect on RUNX1 targets is not known |
| Matched by | ensembl_id |

**Function**, from UniProt [P78364](https://www.uniprot.org/uniprotkb/P78364) (Polyhomeotic-like protein 1):

> Component of a Polycomb group (PcG) multiprotein PRC1-like complex, a complex class required to maintain the transcriptionally repressive state of many genes, including Hox genes, throughout development. PcG PRC1 complex acts via chromatin remodeling and modification of histones; it mediates monoubiquitination of histone H2A 'Lys-119', rendering chromatin heritably changed in its expressibility. Required for proper control of cellular levels of GMNN expression.

**Summary**, from NCBI Gene [1911](https://www.ncbi.nlm.nih.gov/gene/1911):

> This gene is a homolog of the Drosophila polyhomeotic gene, which is a member of the Polycomb group of genes. The gene product is a component of a multimeric protein complex that contains EDR2 and the vertebrate Polycomb protein BMH1. The gene product, the EDR2 protein, and the Drosophila polyhomeotic protein share 2 highly conserved domains, named homology domains I and II. These domains are involved in protein-protein interactions and may mediate heterodimerization of the protein encoded by …

**Accessions** — [HGNC:3182](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3182) · Entrez [1911](https://www.ncbi.nlm.nih.gov/gene/1911) · UniProt [P78364](https://www.uniprot.org/uniprotkb/P78364) · Ensembl [ENSG00000111752](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111752)

## Data

Gene col 3276: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3276); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3276, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3276]; `tensor/DDL_lfc|DDL_z.npy` [3276]; `embed/gene_vectors.npy` [3276]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3276 or target_col == 3276). Every well: [[PHC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
