---
symbol: "FKBP11"
type: "gene"
col: 5537
ensembl_id: "ENSG00000134285"
name: "FKBP prolyl isomerase 11"
location: "12q13.12"
module: 49
arm: "+"
pooled_cpm: 28.0
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 5
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# FKBP11

*FKBP prolyl isomerase 11* — 12q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.76× (z +7.6, q 2e-11, up in 34 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.35× (z +5.6, q 3e-06, up in 25 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H23 2.87×, LoVo 4.05×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.664× (z -7.8, q 3e-12, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC65]] (+0.71, fdr 1e-05, ⚠ same locus), [[MYDGF]] (+0.67, fdr 7e-06), [[TMED7-TICAM2]] (+0.65, fdr 7e-06), [[TTLL3]] (+0.62, fdr 1e-05); moves opposite to [[TRIM68]] (-0.58, fdr 1e-05), [[BBS10]] (-0.58, fdr 3e-05), [[PEX1]] (-0.57, fdr 3e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5537.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H23 2.87×, LoVo 4.05×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.76×** | +7.6 | 2e-11 | 34/44 (NCI-H23, LoVo, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +6.4 | 3e-08 | 21/34 (LoVo, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.64×** | +6.1 | 2e-07 | 24/40 (LOX-IMVI, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +5.6 | 3e-06 | 25/47 (PANC-1, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.61×** | +3.6 | 0.033 | 14/46 (LoVo, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.29× | +3.3 | 0.10 | 20/45 (RKO, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | 1.51× | +3.1 | 0.14 | 12/48 (J82, KATO III, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5537.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.664×** | -7.8 | 3e-12 | 28/47 (RKO, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.645×** | -5.7 | 3e-06 | 25/47 (H4, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.663×** | -5.6 | 5e-06 | 27/47 (A498, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.740×** | -4.1 | 0.007 | 24/48 (RPMI-7951, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.759×** | -3.7 | 0.022 | 20/48 (A-427, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | 0.790× | -3.2 | 0.13 | 17/48 (A498, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.790× | -3.2 | 0.13 | 14/48 (PANC-1, KATO III, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.791× | -3.1 | 0.16 | 9/47 (HEC-1-A, BT-474, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5537. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 50.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -14.4) |
| [[A-427 (line)]] | wt | 34.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -13.7) |
| [[AsPC-1 (line)]] | alt | 17.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -10.4) |
| [[H4 (line)]] | wt | 31.2 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.203× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 49.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -10.8) |
| [[KATO III (line)]] | alt | 42.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -12.9) |
| [[LoVo (line)]] | wt | 51.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 33.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -10.4) |
| [[NCI-H23 (line)]] | alt | 50.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +9.2) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 43.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -17.9) |
| [[RPMI-7951 (line)]] | alt | 38.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -8.5) |
| [[A-172 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 36.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5537), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC65]] | +0.71 | +0.56 / +0.73 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[MYDGF]] | +0.67 | +0.59 / +0.75 | both halves | 7e-06 |  |
| [[TMED7-TICAM2]] | +0.65 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[TTLL3]] | +0.62 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[SPACDR]] | +0.62 | +0.51 / +0.73 | both halves | 1e-05 |  |
| [[UBE2CP5]] | +0.61 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[ATP2A1]] | +0.61 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[SSR4]] | +0.60 | +0.61 / +0.57 | both halves | 9e-06 | STRING 423 |
| [[NDUFA1]] | +0.60 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[SWI5]] | +0.60 | +0.50 / +0.71 | both halves | 1e-05 |  |
| [[MARK4]] | +0.60 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[SLC37A3]] | +0.60 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[MUC20-OT1]] | +0.59 | +0.58 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM68]] | -0.58 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[BBS10]] | -0.58 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[PEX1]] | -0.57 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[DCLRE1A]] | -0.57 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[THNSL1]] | -0.56 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[PDAP1]] | -0.55 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[IPO8]] | -0.55 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[COPS6]] | -0.54 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[NELFCD]] | -0.54 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[N6AMT1]] | -0.54 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[AASDHPPT]] | -0.54 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[PABIR1]] | -0.54 | -0.44 / -0.54 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.436). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.0, -28.7); signed map (-45.4, 10.6). **Vector** length 75.4, 15.2% of its response variance represented; |z| ≥ 3 in 683 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.8 | +2.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +5.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +1.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | -0.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +0.2 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.0 | +2.8 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +1.9 | +0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +3.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.7 | +2.9 |
|  | [[EX229 (drug)]] 0.5 µM |  | +1.6 | +2.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.3 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.3 | -4.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.3 | -2.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.2 | -7.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.0 | -5.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.0 | -1.6 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.9 | +0.5 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.5 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | FKBP prolyl isomerase 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.12 — chr12:48,921,518-48,926,474 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FKBP19 |
| Gene groups (HGNC) | FKBP prolyl isomerase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NYL4](https://www.uniprot.org/uniprotkb/Q9NYL4) (Peptidyl-prolyl cis-trans isomerase FKBP11):

> PPIases accelerate the folding of proteins during protein synthesis.

**Summary**, from NCBI Gene [51303](https://www.ncbi.nlm.nih.gov/gene/51303):

> FKBP11 belongs to the FKBP family of peptidyl-prolyl cis/trans isomerases, which catalyze the folding of proline-containing polypeptides. The peptidyl-prolyl isomerase activity of FKBP proteins is inhibited by the immunosuppressant compounds FK506 and rapamycin (Rulten et al., 2006 [PubMed 16596453]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:18624](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18624) · Entrez [51303](https://www.ncbi.nlm.nih.gov/gene/51303) · UniProt [Q9NYL4](https://www.uniprot.org/uniprotkb/Q9NYL4) · Ensembl [ENSG00000134285](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134285)

## Data

Gene col 5537: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5537); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5537, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5537]; `tensor/DDL_lfc|DDL_z.npy` [5537]; `embed/gene_vectors.npy` [5537]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5537 or target_col == 5537). Every well: [[FKBP11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FKBP11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
