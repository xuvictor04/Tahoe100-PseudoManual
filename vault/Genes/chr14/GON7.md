---
symbol: "GON7"
type: "gene"
col: 9925
ensembl_id: "ENSG00000170270"
name: "GON7 subunit of KEOPS complex"
location: "14q32.12"
module: 12
arm: "+"
pooled_cpm: 3.8
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# GON7

*GON7 subunit of KEOPS complex* — 14q32.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (16 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.44× (z +13.6, q 3e-39, up in 18 of 20 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.46× (z +8.2, q 2e-14, up in 34 of 42 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM251]] (+0.63, fdr 1e-05, ⚠ same locus), [[THSD8]] (+0.56, fdr 1e-05, ⚠ THSD8 in the vector space only through flagged drug-doses), [[NTMT1]] (+0.52, fdr 1e-05), [[MRPS33]] (+0.52, fdr 1e-05), [[ABT1]] (+0.50, fdr 4e-05); moves opposite to [[AP2B1]] (-0.52, fdr 2e-05), [[STIM1]] (-0.48, fdr 5e-05), [[PSAP]] (-0.47, fdr 4e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 16 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9925.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **4.44×** | +13.6 | 3e-39 | 18/20 (NCI-H460, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **4.32×** | +12.8 | 5e-35 | 6/6 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **3.23×** | +9.9 | 1e-20 | 8/10 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **2.94×** | +9.8 | 1e-20 | 40/47 (SW480, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **2.12×** | +9.7 | 4e-20 | 29/36 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.80×** | +9.4 | 7e-19 | 37/44 (NCI-H460, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.46×** | +8.2 | 2e-14 | 34/42 (NCI-H23, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.43×** | +7.8 | 6e-13 | 19/22 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +7.1 | 1e-10 | 19/36 (A549, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **2.13×** | +6.9 | 3e-10 | 29/47 (SW480, PANC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **2.06×** | +6.6 | 2e-09 | 11/21 (A549, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.97×** | +6.2 | 3e-08 | 16/34 (C32, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.94×** | +5.8 | 3e-07 | 23/41 (HEC-1-A, NCI-H460, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.81×** | +5.4 | 3e-06 | 18/47 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.74×** | +5.0 | 2e-05 | 17/44 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.42×** | +3.2 | 0.035 | 7/42 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.41×** | +3.1 | 0.047 | 11/43 (J82, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9925.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.900× | -3.3 | 0.47 | 8/48 (CFPAC-1, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.59 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9925. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 6.51 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.69× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[PANC-1 (line)]] | alt | 2.47 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.84× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[A-172 (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.76 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9925), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 5 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM251]] | +0.63 | +0.57 / +0.64 | both halves | 1e-05 | ⚠ same locus (14.4 kb: neighbours can correlate without regulation) |
| [[THSD8]] ⚠ | +0.56 | +0.54 / +0.60 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NTMT1]] | +0.52 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[MRPS33]] | +0.52 | +0.67 / +0.49 | both halves | 1e-05 |  |
| [[ABT1]] | +0.50 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[MRPL57]] | +0.50 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[EMC9]] | +0.50 | +0.63 / +0.42 | both halves | 4e-05 |  |
| [[MAGEF1]] | +0.48 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[SPA17]] | +0.48 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[XKR7]] | +0.48 | +0.31 / +0.42 | both halves | 2e-04 |  |
| [[PMVK]] | +0.48 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[EID2]] | +0.48 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[DUSP2]] | +0.48 | +0.38 / +0.52 | both halves | 6e-05 |  |
| [[FLVCR1-DT]] | +0.48 | +0.39 / +0.55 | both halves | 6e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP2B1]] | -0.52 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[STIM1]] | -0.48 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[PSAP]] | -0.47 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[MAP4]] | -0.47 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[RTN3]] | -0.46 | -0.59 / -0.33 | both halves | 1e-04 |  |
| [[EEF1G]] | -0.44 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[NUTF2]] | -0.44 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[GHITM]] | -0.43 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[ME2]] | -0.43 | -0.33 / -0.31 | both halves | 2e-04 |  |
| [[HADHA]] | -0.43 | -0.17 / -0.43 | ⚠ not reproduced | 0.001 |  |
| [[RPL14]] | -0.43 | -0.28 / -0.52 | both halves | 3e-04 |  |
| [[CLCC1]] | -0.42 | -0.27 / -0.39 | both halves | 3e-04 |  |
| [[NFE2L1]] | -0.42 | -0.47 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.376). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-52.6, -10.8); signed map (-5.3, -19.9). **Vector** length 40.6, 4.67% of its response variance represented; |z| ≥ 3 in 870 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +3.9 | +13.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +3.6 | +9.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +3.6 | +12.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +3.6 | +9.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +2.8 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.3 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.2 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -0.9 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -1.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -0.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -1.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -2.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -1.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -0.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.1 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | GON7 subunit of KEOPS complex |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.12 — chr14:93,202,894-93,207,065 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C14orf142 |
| Gene groups (HGNC) | KEOPS complex |
| Reactome | 3 pathways, smallest: tRNA modification in the nucleus and cytosol; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BXV9](https://www.uniprot.org/uniprotkb/Q9BXV9) (EKC/KEOPS complex subunit GON7):

> Component of the EKC/KEOPS complex that is required for the formation of a threonylcarbamoyl group on adenosine at position 37 (t(6)A37) in tRNAs that read codons beginning with adenine. The complex is probably involved in the transfer of the threonylcarbamoyl moiety of threonylcarbamoyl-AMP (TC-AMP) to the N6 group of A37. GON7 plays a supporting role to the catalytic subunit OSGEP in the complex.

**Summary**, from NCBI Gene [84520](https://www.ncbi.nlm.nih.gov/gene/84520):

> Involved in tRNA threonylcarbamoyladenosine modification. Located in nucleolus and nucleoplasm. Part of EKC/KEOPS complex. Implicated in Galloway-Mowat syndrome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20356](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20356) · Entrez [84520](https://www.ncbi.nlm.nih.gov/gene/84520) · UniProt [Q9BXV9](https://www.uniprot.org/uniprotkb/Q9BXV9) · Ensembl [ENSG00000170270](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170270)

## Data

Gene col 9925: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9925); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9925, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9925]; `tensor/DDL_lfc|DDL_z.npy` [9925]; `embed/gene_vectors.npy` [9925]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9925 or target_col == 9925). Every well: [[GON7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GON7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
