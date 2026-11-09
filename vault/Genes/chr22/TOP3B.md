---
symbol: "TOP3B"
type: "gene"
col: 1852
ensembl_id: "ENSG00000100038"
name: "DNA topoisomerase III beta"
location: "22q11.22"
module: 127
arm: "+"
pooled_cpm: 10.07
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 6
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/127"]
generated_by: "tahoemap"
---

# TOP3B

*DNA topoisomerase III beta* — 22q11.22

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.524× (z -6.0, q 1e-06, down in 27 of 35 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.663× (z -5.4, q 2e-05, down in 27 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LS 180 0.0768×, NCI-H1792 0.0877×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (CFPAC-1 0.105×, SNU-423 0.114×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (A498 0.222×; ⚠ cell-cycle shift, explains ~0% of this change); [[Thymol (drug)]] 0.5 µM in 1 line (Hs 766T 0.131×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HOP62 0.295×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WASH8P]] (+0.69, fdr 7e-06, ⚠ WASH8P in the vector space only through flagged drug-doses), [[DHX16]] (+0.66, fdr 7e-06), [[ZNF613]] (+0.65, fdr 7e-06), [[ZSCAN22]] (+0.65, fdr 1e-05); moves opposite to [[PEAK1]] (-0.62, fdr 1e-05), [[DENND4A]] (-0.57, fdr 1e-05), [[TMTC2]] (-0.56, fdr 3e-05).
> It is in [[Module 127]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1852.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | 1.45× | +3.5 | 0.28 | 13/47 (LoVo, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | 1.26× | +3.1 | 0.41 | 15/48 (RPMI-7951, NCI-H1573, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM |  | 1.39× | +3.1 | 0.41 | 10/47 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1852.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LS 180 0.0768×, NCI-H1792 0.0877×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (CFPAC-1 0.105×, SNU-423 0.114×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (A498 0.222×; ⚠ cell-cycle shift, explains ~0% of this change); [[Thymol (drug)]] 0.5 µM in 1 line (Hs 766T 0.131×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HOP62 0.295×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.524×** | -6.0 | 1e-06 | 27/35 (LS 180, NCI-H1792, …) | all doses, flat | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.663×** | -5.4 | 2e-05 | 27/41 (HOP62, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.854× | -5.0 | 9e-05 | 22/48 (A-172, NCI-H460, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.564×** | -4.9 | 1e-04 | 17/27 (CFPAC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.592×** | -4.9 | 1e-04 | 26/46 (NCI-H2347, SW480, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.583×** | -3.6 | 0.034 | 21/45 (HT-29, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.688×** | -3.2 | 0.097 | 16/39 (NCI-H1792, NCI-H460, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.627× | -3.1 | 0.14 | 18/41 (PANC-1, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1852. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 11.0 | 0 | 2 (2 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0926× (z -10.2) ⚠ toxic |
| [[A-172 (line)]] | wt | 5.68 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.111× (z -8.8) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 9.11 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 5.70 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.104× (z -8.5) ⚠ cell-cycle shift, explains ~14% of this change |
| [[CFPAC-1 (line)]] | alt | 7.78 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.105× (z -9.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 9.84 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -8.8) |
| [[Hs 766T (line)]] | wt | 11.0 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.131× (z -9.0) |
| [[LS 180 (line)]] | wt | 13.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0768× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[MIA PaCa-2 (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[NCI-H1792 (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0877× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A-427 (line)]] | wt | 8.35 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.46 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.21 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.97 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.33 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.95 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.75 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.69 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1852), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WASH8P]] ⚠ | +0.69 | +0.63 / +0.74 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[DHX16]] | +0.66 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[ZNF613]] | +0.65 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[ZSCAN22]] | +0.65 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[MANBAL]] | +0.64 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[NUDC]] | +0.64 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[IKBKG]] | +0.64 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[DNAJC14]] | +0.62 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[ABCF3]] | +0.62 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[PRPF31]] | +0.61 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[RNF25]] | +0.61 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[ZSCAN20]] | +0.60 | +0.47 / +0.69 | both halves | 2e-05 |  |
| [[WASH9P]] | +0.60 | +0.45 / +0.66 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEAK1]] | -0.62 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[DENND4A]] | -0.57 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[TMTC2]] | -0.56 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[ARIH1]] | -0.56 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[TESK2]] | -0.53 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[BCL2L14]] | -0.53 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[PHLPP1]] | -0.52 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[KDM5B]] | -0.52 | -0.35 / -0.61 | both halves | 1e-04 |  |
| [[FBXO11]] | -0.51 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[FNBP1]] | -0.51 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[ACAP1]] | -0.51 | -0.38 / -0.58 | both halves | 7e-05 |  |
| [[CSKMT]] | -0.50 | -0.50 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 127]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.694). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-33.8, -2.1); signed map (-12.8, -29.3). **Vector** length 56.6, 8.17% of its response variance represented; |z| ≥ 3 in 885 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | +2.6 | -0.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | +2.6 | +3.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.0 | +1.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +1.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | +2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | -0.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.6 | +0.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.5 | +1.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.4 | -5.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -1.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.0 | -0.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -0.6 |
|  | [[Fumaric acid (drug)]] 0.5 µM |  | -1.5 | -1.4 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.5 | -1.2 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.3 | -2.3 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | -1.2 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | DNA topoisomerase III beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.22 — chr22:21,957,025-21,982,813 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Topoisomerases |
| Matched by | ensembl_id |

**Function**, from UniProt [O95985](https://www.uniprot.org/uniprotkb/O95985) (DNA topoisomerase 3-beta-1):

> Releases the supercoiling and torsional tension of DNA introduced during the DNA replication and transcription by transiently cleaving and rejoining one strand of the DNA duplex. Introduces a single-strand break via transesterification at a target site in duplex DNA. The scissile phosphodiester is attacked by the catalytic tyrosine of the enzyme, resulting in the formation of a DNA-(5'-phosphotyrosyl)-enzyme intermediate and the expulsion of a 3'-OH DNA strand. The free DNA strand than …

**Summary**, from NCBI Gene [8940](https://www.ncbi.nlm.nih.gov/gene/8940):

> This gene encodes a DNA topoisomerase, an enzyme that controls and alters the topologic states of DNA during transcription. This enzyme catalyzes the transient breaking and rejoining of a single strand of DNA which allows the strands to pass through one another, thus relaxing the supercoils and altering the topology of DNA. The enzyme interacts with DNA helicase SGS1 and plays a role in DNA recombination, cellular aging and maintenance of genome stability. Low expression of this gene may be …

**Accessions** — [HGNC:11993](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11993) · Entrez [8940](https://www.ncbi.nlm.nih.gov/gene/8940) · UniProt [O95985](https://www.uniprot.org/uniprotkb/O95985) · Ensembl [ENSG00000100038](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100038)

## Data

Gene col 1852: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1852); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1852, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1852]; `tensor/DDL_lfc|DDL_z.npy` [1852]; `embed/gene_vectors.npy` [1852]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1852 or target_col == 1852). Every well: [[TOP3B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TOP3B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
