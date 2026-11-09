---
symbol: "SNU13"
type: "gene"
col: 1875
ensembl_id: "ENSG00000100138"
name: "small nuclear ribonucleoprotein 13"
location: "22q13.2"
module: 54
arm: "+"
pooled_cpm: 71.32
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 7
n_dd_up_clean: 2
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# SNU13

*small nuclear ribonucleoprotein 13* — 22q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.03× (z +6.7, q 1e-08, up in 43 of 46 measured lines) ⚠ toxic. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.52× (z +4.7, q 6e-04, up in 40 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Trametinib (drug)]] 5 µM: 0.601× (z -4.7, q 0.001, down in 43 of 50 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPS21]] (+0.75, fdr 7e-06), [[NAT9]] (+0.74, fdr 7e-06), [[CTU1]] (+0.71, fdr 7e-06); moves opposite to [[UBE2A]] (-0.69, fdr 7e-06), [[EIF4G2]] (-0.68, fdr 1e-05), [[SCRN1]] (-0.67, fdr 1e-05).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1875.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.03×** | +6.7 | 1e-08 | 43/46 (Hs 766T, HOP62, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.52×** | +4.7 | 6e-04 | 40/49 (COLO 205, LS 180, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.57×** | +4.4 | 0.002 | 34/48 (LS 180, NCI-H2030, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.04×** | +3.7 | 0.036 | 30/48 (RKO, LS 180, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.41×** | +3.3 | 0.095 | 26/48 (A-172, SNU-423, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 1.84× | +3.1 | 0.17 | 21/36 (NCI-H2347, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~52% of this change | 1.38× | +3.0 | 0.21 | 27/47 (LoVo, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1875.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.601×** | -4.7 | 0.001 | 43/50 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.660×** | -3.9 | 0.025 | 34/47 (A-427, PANC-1, …) | rises with dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.473×** | -3.8 | 0.025 | 37/48 (A-427, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.761×** | -3.6 | 0.044 | 33/48 (SW480, SHP-77, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.675×** | -3.5 | 0.044 | 35/48 (NCI-H23, C32, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.511×** | -3.4 | 0.058 | 36/50 (A-427, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.787×** | -3.3 | 0.079 | 24/48 (SNU-1, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 5 µM |  | 0.728× | -3.2 | 0.10 | 28/49 (C32, LoVo, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1875. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 94.4 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -9.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.468× (z -8.9) |
| [[A-427 (line)]] | wt | 78.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 124 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -8.8) |
| [[SNU-1 (line)]] | wt | 74.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -10.5) |
| [[A-172 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 87.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 43.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 75.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 81.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 73.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 75.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 90.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 59.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 82.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 81.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 70.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 68.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 89.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 47.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 85.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 64.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 50.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 72.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 87.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 40.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 79.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 71.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 75.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 225 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 76.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 72.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 82.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 107 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1875), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS21]] | +0.75 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[NAT9]] | +0.74 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[CTU1]] | +0.71 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[SF3B6]] | +0.70 | +0.66 / +0.64 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 870 |
| [[TOMM5]] | +0.69 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[ANKS3]] | +0.68 | +0.62 / +0.57 | both halves | 8e-06 |  |
| [[DHX57]] | +0.68 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[MINCR]] | +0.68 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[TFB2M]] | +0.67 | +0.66 / +0.62 | both halves | 7e-06 | STRING 498 |
| [[RPS26]] | +0.67 | +0.57 / +0.59 | both halves | 1e-05 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 793 |
| [[DDX55]] | +0.66 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[POP7]] | +0.66 | +0.50 / +0.63 | both halves | 1e-05 | STRING 732 |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2A]] | -0.69 | -0.64 / -0.62 | both halves | 7e-06 |  |
| [[EIF4G2]] | -0.68 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[SCRN1]] | -0.67 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[CHD3]] | -0.65 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[NXT2]] | -0.63 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[HMGN2]] | -0.63 | -0.56 / -0.49 | both halves | 1e-05 | STRING 628 |
| [[NCOA4]] | -0.62 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[MOB1A]] | -0.60 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[GBA1]] | -0.60 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[HUWE1]] | -0.58 | -0.44 / -0.70 | both halves | 3e-05 |  |
| [[MED12]] | -0.58 | -0.48 / -0.43 | both halves | 4e-05 |  |
| [[TAPBP]] | -0.57 | -0.52 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.709). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-0.1, -19.2); signed map (-53.9, -1.7). **Vector** length 97.8, 36.7% of its response variance represented; |z| ≥ 3 in 653 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Mitochondrial ribosome-associated quality control* (reactome, mean cos +0.55 to 9); *Mitochondrial translation* (reactome, mean cos +0.55 to 9); *Mitochondrial translation elongation* (reactome, mean cos +0.54 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | +3.9 | +3.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | +3.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.4 | +4.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +3.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +2.3 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +2.0 | +2.1 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.9 | +1.8 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.8 | +2.3 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -5.0 | +0.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.9 | -3.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -0.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.8 | +2.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | +1.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.3 | -3.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.0 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.8 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.8 | -3.5 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -2.8 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | small nuclear ribonucleoprotein 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.2 — chr22:41,673,933-41,690,504 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FA-1, SPAG12, SNRNP15-5, 15.5K; previously SSFA1, NHP2L1 |
| Gene groups (HGNC) | U3 small nucleolar ribonucleoprotein; U4/U6 small nuclear ribonucleoprotein particle |
| Reactome | 8 pathways, smallest: rRNA modification in the nucleus and cytosol; Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [P55769](https://www.uniprot.org/uniprotkb/P55769) (NHP2-like protein 1):

> Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, rearrangements and cleavage as well as targeted degradation of pre-ribosomal RNA by the RNA exosome. Involved in pre-mRNA splicing as component of the spliceosome. …

**Summary**, from NCBI Gene [4809](https://www.ncbi.nlm.nih.gov/gene/4809):

> Originally named because of its sequence similarity to the Saccharomyces cerevisiae NHP2 (non-histone protein 2), this protein appears to be a highly conserved nuclear protein that is a component of the [U4/U6.U5] tri-snRNP. It binds to the 5' stem-loop of U4 snRNA. Two transcript variants encoding the same protein have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7819](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7819) · Entrez [4809](https://www.ncbi.nlm.nih.gov/gene/4809) · UniProt [P55769](https://www.uniprot.org/uniprotkb/P55769) · Ensembl [ENSG00000100138](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100138)

## Data

Gene col 1875: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1875); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1875, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1875]; `tensor/DDL_lfc|DDL_z.npy` [1875]; `embed/gene_vectors.npy` [1875]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1875 or target_col == 1875). Every well: [[SNU13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNU13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
