---
symbol: "LSM2"
type: "gene"
col: 12867
ensembl_id: "ENSG00000204392"
name: "LSM2 homolog, U6 small nuclear RNA and mRNA degradation associated"
location: "6p21.33"
module: 54
arm: "+"
pooled_cpm: 19.71
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 6
n_dd_up_clean: 0
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# LSM2

*LSM2 homolog, U6 small nuclear RNA and mRNA degradation associated* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.94× (z +4.7, q 0.001, up in 33 of 43 measured lines) ⚠ transcription drop; cell-cycle shift, explains ~43% of this change. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.442× (z -8.2, q 2e-13, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C15orf61]] (+0.81, fdr 7e-06, ⚠ C15orf61 in the vector space only through flagged drug-doses), [[ANAPC11]] (+0.81, fdr 7e-06), [[MRPL41]] (+0.77, fdr 1e-05, ⚠ MRPL41 in the vector space only through flagged drug-doses), [[ATP5MJ]] (+0.77, fdr 7e-06), [[C4orf48]] (+0.76, fdr 2e-05); moves opposite to [[EIF4G2]] (-0.70, fdr 1e-05), [[ZNF655]] (-0.69, fdr 7e-06), [[KRT8P12]] (-0.68, fdr 1e-05).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12867.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **1.94×** | +4.7 | 0.001 | 33/43 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +4.3 | 0.006 | 31/44 (CFPAC-1, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **1.78×** | +4.1 | 0.007 | 26/42 (NCI-H23, CFPAC-1, …) | two highest doses | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | 1.59× | +3.2 | 0.17 | 18/30 (Hs 766T, KATO III, …) | two highest doses | composition shift |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.56× | +3.2 | 0.17 | 25/46 (LoVo, HEC-1-A, …) | top dose only |  |
| [[Bendamustine (drug)]] 5 µM |  | 1.55× | +3.0 | 0.21 | 20/46 (A-172, NCI-H23, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 1.34× | +3.0 | 0.21 | 25/48 (HCT15, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12867.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.442×** | -8.2 | 2e-13 | 41/47 (NCI-H23, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.515×** | -4.7 | 7e-04 | 30/47 (SNU-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.665×** | -4.1 | 0.009 | 26/47 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.308×** | -3.9 | 0.013 | 31/48 (LoVo, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.342×** | -3.6 | 0.041 | 25/46 (LS 180, HT-29, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.602×** | -3.4 | 0.067 | 29/48 (SK-MEL-2, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.57 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12867. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 16.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -8.6) |
| [[A-427 (line)]] | wt | 27.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -13.2) |
| [[HepG2_C3A (line)]] | wt | 20.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.128× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~52% of this change |
| [[HOP62 (line)]] | alt | 16.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -8.6) |
| [[HS-578T (line)]] | alt | 19.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -8.8) |
| [[J82 (line)]] | alt | 32.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 36.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 36.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -16.6) |
| [[NCI-H661 (line)]] | alt | 25.5 | 0 | 1 | — | [[Asciminib (drug)]] 0.05 µM 0.0509× (z -8.8) |
| [[SW1417 (line)]] | alt | 21.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[A498 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.73 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 20.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12867), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 15 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C15orf61]] ⚠ | +0.81 | +0.58 / +0.81 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[ANAPC11]] | +0.81 | +0.66 / +0.80 | both halves | 7e-06 |  |
| [[MRPL41]] ⚠ | +0.77 | +0.52 / +0.78 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ATP5MJ]] | +0.77 | +0.60 / +0.75 | both halves | 7e-06 |  |
| [[C4orf48]] | +0.76 | +0.47 / +0.76 | both halves | 2e-05 |  |
| [[CHCHD1]] | +0.76 | +0.55 / +0.83 | both halves | 1e-05 |  |
| [[MRPL34]] | +0.76 | +0.64 / +0.78 | both halves | 7e-06 |  |
| [[MALSU1]] | +0.75 | +0.57 / +0.72 | both halves | 8e-06 |  |
| [[POP7]] | +0.75 | +0.56 / +0.78 | both halves | 1e-05 |  |
| [[LAMTOR5]] | +0.75 | +0.53 / +0.77 | both halves | 1e-05 |  |
| [[SAC3D1]] | +0.73 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[DPM3]] | +0.73 | +0.61 / +0.76 | both halves | 7e-06 |  |
| [[MICOS13]] | +0.72 | +0.51 / +0.69 | both halves | 1e-05 |  |
| [[CCDC107]] | +0.72 | +0.57 / +0.70 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G2]] | -0.70 | -0.51 / -0.64 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[ZNF655]] | -0.69 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[KRT8P12]] | -0.68 | -0.72 / -0.49 | both halves | 1e-05 |  |
| [[CCDC200]] | -0.67 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[TUG1]] | -0.65 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[PARD6G-AS1]] | -0.65 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[NRAS]] | -0.65 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[PSME3IP1]] | -0.64 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[VPS52]] | -0.63 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[DBNL]] | -0.63 | -0.60 / -0.65 | both halves | 7e-06 |  |
| [[EXOC7]] | -0.63 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[CROCC]] | -0.62 | -0.39 / -0.56 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.862). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-45.5, -18.7); signed map (-33.5, 5.0). **Vector** length 77.6, 22.7% of its response variance represented; |z| ≥ 3 in 505 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Mitochondrial ribosome-associated quality control* (reactome, mean cos +0.62 to 9); *Mitochondrial translation* (reactome, mean cos +0.62 to 9); *Mitochondrial translation elongation* (reactome, mean cos +0.60 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +0.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +0.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +0.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.7 | +2.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.7 | +4.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.5 | +0.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.3 | -0.6 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +1.3 | +2.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.2 | +1.7 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +1.2 | +1.3 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.7 | +1.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | -4.9 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | -4.7 | +4.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.4 | -4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.6 | -1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -3.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.6 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | LSM2 homolog, U6 small nuclear RNA and mRNA degradation associated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:31,797,396-31,806,966 (-) |
| Ensembl biotype | protein_coding |
| Also known as | G7b, YBL026W; previously C6orf28 |
| Gene groups (HGNC) | LSm proteins |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 6 pathways, smallest: mRNA decay by 5' to 3' exoribonuclease; Deadenylation-dependent mRNA decay; mRNA Splicing - Major Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y333](https://www.uniprot.org/uniprotkb/Q9Y333) (U6 snRNA-associated Sm-like protein LSm2):

> Plays a role in pre-mRNA splicing as component of the U4/U6-U5 tri-snRNP complex that is involved in spliceosome assembly, and as component of the precatalytic spliceosome (spliceosome B complex). The heptameric LSM2-8 complex binds specifically to the 3'-terminal U-tract of U6 snRNA.

**Summary**, from NCBI Gene [57819](https://www.ncbi.nlm.nih.gov/gene/57819):

> This gene encodes a member of the LSm family of RNA-binding proteins. LSm proteins form stable heteromers that bind specifically to the 3'-terminal oligo(U) tract of U6 snRNA and may play a role in pre-mRNA splicing by mediating U4/U6 snRNP formation. Pseudogenes of this gene are located on the short arm of chromosomes 6 and 19. [provided by RefSeq, Nov 2011]

**Accessions** — [HGNC:13940](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13940) · Entrez [57819](https://www.ncbi.nlm.nih.gov/gene/57819) · UniProt [Q9Y333](https://www.uniprot.org/uniprotkb/Q9Y333) · Ensembl [ENSG00000204392](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204392)

## Data

Gene col 12867: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12867); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12867, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12867]; `tensor/DDL_lfc|DDL_z.npy` [12867]; `embed/gene_vectors.npy` [12867]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12867 or target_col == 12867). Every well: [[LSM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LSM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
