---
symbol: "TCEAL8"
type: "gene"
col: 11151
ensembl_id: "ENSG00000180964"
name: "transcription elongation factor A like 8"
location: "Xq22.1"
module: 12
arm: "+"
pooled_cpm: 29.43
n_lines_expressing: 49
n_dd_up: 1
n_dd_down: 16
n_dd_up_clean: 0
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# TCEAL8

*transcription elongation factor A like 8* — Xq22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.52× (z +3.8, q 0.090, up in 28 of 45 measured lines) ⚠ transcription drop; cell-cycle shift, explains ~43% of this change.
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.465× (z -6.8, q 5e-09, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF113A]] (+0.77, fdr 7e-06), [[TCEAL9]] (+0.76, fdr 7e-06), [[SMIM26]] (+0.71, fdr 1e-05, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[IFI27L2]] (+0.71, fdr 1e-05); moves opposite to [[UBE2G2]] (-0.66, fdr 7e-06), [[SMG1P3]] (-0.65, fdr 3e-05), [[AKT1]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11151.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **1.52×** | +3.8 | 0.090 | 28/45 (PANC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 1.53× | +3.4 | 0.19 | 19/42 (LoVo, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); composition shift |
| [[Arbutin (drug)]] 5 µM |  | 1.42× | +3.0 | 0.49 | 22/47 (COLO 205, SW 900, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11151.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.465×** | -6.8 | 5e-09 | 41/47 (SNU-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.510×** | -6.0 | 6e-07 | 39/47 (H4, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.524×** | -5.7 | 2e-06 | 36/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.679×** | -4.8 | 2e-04 | 27/46 (SK-MEL-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.591×** | -4.7 | 3e-04 | 27/46 (RPMI-7951, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.594×** | -4.6 | 3e-04 | 29/47 (A-172, HCT15, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.607×** | -4.4 | 7e-04 | 29/46 (SW 900, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.608×** | -4.4 | 7e-04 | 27/47 (SW 900, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.461×** | -3.6 | 0.020 | 18/31 (LOX-IMVI, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.668×** | -3.6 | 0.020 | 29/47 (H4, AsPC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.677×** | -3.5 | 0.024 | 25/47 (HS-578T, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.475×** | -3.5 | 0.024 | 23/45 (NCI-H1573, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.667×** | -3.5 | 0.024 | 25/47 (SW 900, NCI-H460, …) | top dose only | cell-cycle shift (explains ~19% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.486×** | -3.3 | 0.033 | 26/47 (Panc 03.27, SNU-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | **0.699×** | -3.2 | 0.057 | 22/47 (HEC-1-A, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11151. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 32.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.158× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.183× (z -9.6) |
| [[SW480 (line)]] | alt | 31.4 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.261× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 34.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 28.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.211× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 15.6 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.249× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 30.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.190× (z -8.6) |
| [[SHP-77 (line)]] | alt | 16.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.157× (z -9.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 46.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -12.1) |
| [[SNU-1 (line)]] | wt | 42.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.137× (z -10.0) |
| [[A-172 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 42.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 49.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.47 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 53.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11151), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF113A]] | +0.77 | +0.63 / +0.77 | both halves | 7e-06 |  |
| [[TCEAL9]] | +0.76 | +0.67 / +0.80 | both halves | 7e-06 | same gene group; STRING 533 |
| [[SMIM26]] ⚠ | +0.71 | +0.52 / +0.78 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[IFI27L2]] | +0.71 | +0.57 / +0.74 | both halves | 1e-05 |  |
| [[KRT10]] ⚠ | +0.71 | +0.57 / +0.81 | both halves | 9e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[NKAP]] | +0.71 | +0.52 / +0.77 | both halves | 1e-05 |  |
| [[MED19]] | +0.70 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[SNRPB2]] | +0.70 | +0.52 / +0.79 | both halves | 1e-05 |  |
| [[SCAND1]] | +0.67 | +0.48 / +0.76 | both halves | 2e-05 |  |
| [[PIGBOS1]] | +0.67 | +0.45 / +0.75 | both halves | 3e-05 |  |
| [[ZNF622]] | +0.66 | +0.50 / +0.72 | both halves | 1e-05 |  |
| [[RBMX2]] | +0.66 | +0.50 / +0.70 | both halves | 1e-05 |  |
| [[KBTBD7]] | +0.66 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[ACBD3]] | +0.66 | +0.52 / +0.68 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2G2]] | -0.66 | -0.60 / -0.64 | both halves | 7e-06 |  |
| [[SMG1P3]] | -0.65 | -0.45 / -0.71 | both halves | 3e-05 |  |
| [[AKT1]] | -0.64 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[CERS2]] | -0.63 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[TTL]] | -0.63 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[MOB1A]] | -0.62 | -0.49 / -0.67 | both halves | 1e-05 |  |
| [[IPO5]] | -0.62 | -0.42 / -0.69 | both halves | 4e-05 |  |
| [[MACROH2A1]] | -0.62 | -0.45 / -0.69 | both halves | 3e-05 |  |
| [[PSME3]] | -0.61 | -0.46 / -0.63 | both halves | 3e-05 |  |
| [[CTSZ]] | -0.60 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[TARDBP]] | -0.60 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[DHFR]] | -0.59 | -0.28 / -0.74 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.726). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-40.2, -12.3); signed map (-12.5, -3.3). **Vector** length 74.6, 20.4% of its response variance represented; |z| ≥ 3 in 608 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | -1.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +1.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +0.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.2 | -4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | -0.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.9 | +1.5 |
|  | [[Adagrasib (drug)]] 5 µM |  | +1.7 | +2.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.6 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +1.4 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.5 | -1.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.6 | +0.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.5 | +3.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.2 | -5.7 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -2.2 | -3.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.7 | -1.1 |
|  | [[Clonidine (hydrochloride) (drug)]] 5 µM |  | -1.5 | -2.6 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.3 | -2.3 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | -1.3 | -1.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.2 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | transcription elongation factor A like 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.1 — chrX:103,252,995-103,255,192 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC45400, WEX3 |
| Gene groups (HGNC) | Transcription elongation factor A like family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IYN2](https://www.uniprot.org/uniprotkb/Q8IYN2) (Transcription elongation factor A protein-like 8):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [90843](https://www.ncbi.nlm.nih.gov/gene/90843):

> This gene encodes a member of the transcription elongation factor A (SII)-like (TCEAL) gene family. Members of this family contain TFA domains and may function as nuclear phosphoproteins that modulate transcription in a promoter context-dependent manner. Multiple family members are located on the X chromosome. Alternative splicing results in multiple transcript variants encoding a single isoform. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:28683](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28683) · Entrez [90843](https://www.ncbi.nlm.nih.gov/gene/90843) · UniProt [Q8IYN2](https://www.uniprot.org/uniprotkb/Q8IYN2) · Ensembl [ENSG00000180964](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180964)

## Data

Gene col 11151: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11151); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11151, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11151]; `tensor/DDL_lfc|DDL_z.npy` [11151]; `embed/gene_vectors.npy` [11151]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11151 or target_col == 11151). Every well: [[TCEAL8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TCEAL8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
