---
symbol: "CDC34"
type: "gene"
col: 1813
ensembl_id: "ENSG00000099804"
name: "cell division cycle 34, ubiquitin conjugating enzyme"
location: "19p13.3"
module: 3
arm: "+"
pooled_cpm: 13.75
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 4
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# CDC34

*cell division cycle 34, ubiquitin conjugating enzyme* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.95× (z +6.4, q 7e-08, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.462× (z -3.9, q 0.055, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RCE1]] (+0.73, fdr 7e-06), [[PIP5K1C]] (+0.73, fdr 7e-06), [[MEX3D]] (+0.71, fdr 1e-05); moves opposite to [[MTMR2]] (-0.66, fdr 4e-05), [[BCLAF1]] (-0.66, fdr 1e-05), [[PUS7L]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1813.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.95×** | +6.4 | 7e-08 | 37/48 (HEC-1-A, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.79×** | +5.6 | 7e-06 | 35/48 (LoVo, SW480, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.73×** | +5.2 | 3e-05 | 31/46 (PANC-1, NCI-H460, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.64×** | +4.7 | 3e-04 | 29/47 (MIA PaCa-2, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.60×** | +4.5 | 7e-04 | 29/46 (NCI-H1792, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.60×** | +4.5 | 7e-04 | 25/42 (PANC-1, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +4.3 | 0.002 | 27/47 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.50×** | +3.7 | 0.013 | 11/28 (SW 900, NCI-H460, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +3.7 | 0.013 | 18/41 (CFPAC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.93×** | +3.5 | 0.023 | 19/43 (LoVo, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.40×** | +3.2 | 0.064 | 15/48 (SW1417, NCI-H23, …) | rises with dose | composition shift |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.40×** | +3.2 | 0.068 | 17/47 (LoVo, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.38×** | +3.1 | 0.082 | 13/44 (Panc 03.27, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1813.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.462×** | -3.9 | 0.055 | 26/48 (A498, SNU-423, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.690×** | -3.6 | 0.083 | 14/48 (NCI-H2030, SW480, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.498×** | -3.5 | 0.083 | 19/43 (LS 180, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.779×** | -3.4 | 0.085 | 19/48 (NCI-H661, hTERT-HPNE, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1813. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 18.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.165× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 17.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.170× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 15.6 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.5 µM 0.143× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 18.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 11.1 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0678× (z -10.2) |
| [[A-172 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.93 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.24 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.61 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.68 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 17.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1813), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RCE1]] | +0.73 | +0.59 / +0.77 | both halves | 7e-06 |  |
| [[PIP5K1C]] | +0.73 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[MEX3D]] | +0.71 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[ARID3A]] | +0.70 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[ATG2A]] | +0.70 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[TRAPPC4]] | +0.70 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[RBM38]] | +0.69 | +0.51 / +0.70 | both halves | 1e-05 | STRING 485 |
| [[CCNQ]] | +0.68 | +0.46 / +0.67 | both halves | 2e-05 |  |
| [[SIRT7]] | +0.68 | +0.37 / +0.76 | both halves | 8e-05 |  |
| [[ULK1]] | +0.68 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[RPL36AL]] ⚠ | +0.68 | +0.49 / +0.72 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[BRI3]] | +0.67 | +0.50 / +0.70 | both halves | 1e-05 |  |
| [[ATG4B]] | +0.67 | +0.44 / +0.63 | both halves | 3e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTMR2]] | -0.66 | -0.43 / -0.66 | both halves | 4e-05 |  |
| [[BCLAF1]] | -0.66 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[PUS7L]] | -0.64 | -0.53 / -0.66 | both halves | 1e-05 |  |
| [[ATP5PB]] | -0.64 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[MBTPS2]] | -0.63 | -0.52 / -0.65 | both halves | 1e-05 |  |
| [[POGLUT3]] | -0.63 | -0.49 / -0.63 | both halves | 1e-05 |  |
| [[COPS3]] | -0.63 | -0.53 / -0.65 | both halves | 1e-05 |  |
| [[YWHAE]] | -0.62 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[PRTFDC1]] | -0.62 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[NBN]] | -0.62 | -0.60 / -0.63 | both halves | 7e-06 |  |
| [[ACADM]] | -0.61 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[FUBP1]] | -0.61 | -0.45 / -0.61 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.779). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-33.4, -25.9); signed map (-27.5, 14.7). **Vector** length 75.4, 16.7% of its response variance represented; |z| ≥ 3 in 607 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +3.4 | +5.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.3 | +6.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.2 | +3.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.1 | +4.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.8 | +4.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.2 | +3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.0 | +1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.9 | +2.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.9 | +0.5 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.4 | -3.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.3 | -0.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.2 | +2.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | -3.1 | +3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -3.5 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.9 | -3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -2.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -2.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | cell division cycle 34, ubiquitin conjugating enzyme |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:531,760-542,092 (+) |
| Ensembl biotype | protein_coding |
| Also known as | E2-CDC34, UBE2R1, UBC3 |
| Gene groups (HGNC) | Ubiquitin conjugating enzymes E2 |
| Hallmark sets | UV_RESPONSE_UP |
| Reactome | 12 pathways, smallest: Synthesis of active ubiquitin: roles of E1 and E2 enzymes; FCERI mediated NF-kB activation; Downstream TCR signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P49427](https://www.uniprot.org/uniprotkb/P49427) (Ubiquitin-conjugating enzyme E2 R1):

> E2 ubiquitin-conjugating enzyme that accepts ubiquitin from an E1 ubiquitin-activating protein, and catalyzes its covalent attachment to other proteins by an E3 ubiquitin-protein ligase complex. In vitro catalyzes 'Lys-48'-linked polyubiquitination. Cooperates with the E2 UBCH5C and the SCF(FBXW11) E3 ligase complex for the polyubiquitination of NFKBIA leading to its subsequent proteasomal degradation. Performs ubiquitin chain elongation building ubiquitin chains from the UBE2D3-primed …

**Summary**, from NCBI Gene [997](https://www.ncbi.nlm.nih.gov/gene/997):

> The protein encoded by this gene is a member of the ubiquitin-conjugating enzyme family. Ubiquitin-conjugating enzyme catalyzes the covalent attachment of ubiquitin to other proteins. This protein is a part of the large multiprotein complex, which is required for ubiquitin-mediated degradation of cell cycle G1 regulators, and for the initiation of DNA replication. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1734](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1734) · Entrez [997](https://www.ncbi.nlm.nih.gov/gene/997) · UniProt [P49427](https://www.uniprot.org/uniprotkb/P49427) · Ensembl [ENSG00000099804](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099804)

## Data

Gene col 1813: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1813); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1813, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1813]; `tensor/DDL_lfc|DDL_z.npy` [1813]; `embed/gene_vectors.npy` [1813]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1813 or target_col == 1813). Every well: [[CDC34 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDC34.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
