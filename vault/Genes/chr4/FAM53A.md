---
symbol: "FAM53A"
type: "gene"
col: 10466
ensembl_id: "ENSG00000174137"
name: "family with sequence similarity 53 member A"
location: "4p16.3"
module: 47
arm: "+"
pooled_cpm: 6.82
n_lines_expressing: 49
n_dd_up: 13
n_dd_down: 9
n_dd_up_clean: 4
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# FAM53A

*family with sequence similarity 53 member A* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.51× (z +10.5, q 5e-23, up in 35 of 46 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.37× (z +9.8, q 2e-20, up in 26 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.446× (z -8.9, q 3e-16, down in 24 of 44 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.617× (z -5.5, q 8e-06, down in 21 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPIEL]] (+0.70, fdr 7e-06), [[CSPG5]] (+0.69, fdr 7e-06), [[PYGM]] (+0.68, fdr 7e-06); moves opposite to [[UBA3]] (-0.60, fdr 1e-05), [[XPA]] (-0.60, fdr 3e-05), [[PHC3]] (-0.50, fdr 3e-05).
> It is in [[Module 047]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10466.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.51×** | +10.5 | 5e-23 | 35/46 (KATO III, SW480, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.37×** | +9.8 | 2e-20 | 26/44 (HOP62, HT-29, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.07×** | +8.3 | 2e-14 | 30/46 (KATO III, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **1.98×** | +7.5 | 9e-12 | 15/29 (A-172, NCI-H1573, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.50×** | +6.5 | 1e-08 | 22/41 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.76×** | +6.4 | 1e-08 | 22/46 (KATO III, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.78×** | +6.1 | 1e-07 | 5/13 (LOX-IMVI, NCI-H460, …) | inconsistent across doses | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.69×** | +6.0 | 2e-07 | 20/46 (LOX-IMVI, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.44×** | +4.2 | 0.002 | 7/46 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.45×** | +4.1 | 0.003 | 3/11 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.36×** | +3.4 | 0.037 | 7/39 (SW480, H4, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.34×** | +3.3 | 0.043 | 3/43 (RKO, HCT15, …) | inconsistent across doses |  |
| [[Silodosin (drug)]] 5 µM |  | **1.35×** | +3.2 | 0.051 | 5/40 (BT-474, HT-29, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10466.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.446×** | -8.9 | 3e-16 | 24/44 (A-427, PANC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.617×** | -5.5 | 8e-06 | 21/45 (PANC-1, C-33 A, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.402×** | -5.5 | 9e-06 | 17/33 (LS 180, J82, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.634×** | -5.2 | 2e-05 | 22/46 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.677×** | -4.5 | 8e-04 | 19/45 (A-427, SNU-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.702×** | -4.1 | 0.005 | 20/44 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.720×** | -3.6 | 0.024 | 15/32 (NCI-H23, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Benproperine (phosphate) (drug)]] 5 µM |  | **0.744×** | -3.3 | 0.076 | 11/43 (SHP-77, SW48, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.750×** | -3.2 | 0.090 | 12/42 (SW48, SW 900, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.763× | -3.1 | 0.11 | 16/43 (PANC-1, NCI-H23, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.56 per unit of S-phase module lfc, -0.54 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10466. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 12.2 | 0 | 10 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.162× (z -13.0) |
| [[A-427 (line)]] | wt | 26.6 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -15.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.323× (z -8.5) |
| [[C-33 A (line)]] | alt | 16.5 | 0 | 2 (1 ⚠) | — | [[Canagliflozin (drug)]] 0.05 µM 0.112× (z -9.2) |
| [[LoVo (line)]] | wt | 6.71 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0733× (z -11.9) ⚠ toxic · without an alert: [[Canagliflozin (drug)]] 0.05 µM 0.0681× (z -11.7) |
| [[NCI-H23 (line)]] | alt | 17.6 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.112× (z -12.7) ⚠ toxic |
| [[A-172 (line)]] | wt | 6.31 | 0 | 1 | — | [[Silodosin (drug)]] 0.05 µM 0.0845× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 6.82 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0877× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 5.71 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0953× (z -9.3) ⚠ transcription drop; cell-cycle shift, explains ~91% of this change |
| [[NCI-H2030 (line)]] | alt | 6.60 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 7.59 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.116× (z -8.7) ⚠ toxic |
| [[A498 (line)]] | wt | 8.32 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.24 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.93 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.04 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.12 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.17 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10466), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPIEL]] | +0.70 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[CSPG5]] | +0.69 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[PYGM]] | +0.68 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[AZU1]] | +0.67 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[VWCE]] | +0.67 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[SLC27A5]] | +0.66 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[SMIM41]] | +0.66 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[HPX]] | +0.64 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[FERMT3]] | +0.64 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[LINC02236]] | +0.63 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[CCDC138]] | +0.62 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[RRP7BP]] | +0.60 | +0.47 / +0.63 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBA3]] | -0.60 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[XPA]] | -0.60 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[PHC3]] | -0.50 | -0.44 / -0.54 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.631). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (38.3, -21.9); signed map (16.0, 13.2). **Vector** length 71.3, 11.5% of its response variance represented; |z| ≥ 3 in 1,221 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.5 | +9.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.5 | +1.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | +2.4 | +7.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.2 | +1.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +2.2 | +6.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.2 | +2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +1.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +2.7 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -4.6 | -8.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.3 | -2.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -3.0 | -5.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.9 | -5.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.8 | -4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.1 | -2.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.9 | -1.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.8 | -0.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.7 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 53 member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.3 — chr4:1,617,915-1,684,313 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DNTNP |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6NSI3](https://www.uniprot.org/uniprotkb/Q6NSI3) (Protein FAM53A):

> May play an important role in neural development; the dorsomedial roof of the third ventricle.

**Summary**, from NCBI Gene [152877](https://www.ncbi.nlm.nih.gov/gene/152877):

> Predicted to be involved in protein import into nucleus. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:31860](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31860) · Entrez [152877](https://www.ncbi.nlm.nih.gov/gene/152877) · UniProt [Q6NSI3](https://www.uniprot.org/uniprotkb/Q6NSI3) · Ensembl [ENSG00000174137](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174137)

## Data

Gene col 10466: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10466); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10466, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10466]; `tensor/DDL_lfc|DDL_z.npy` [10466]; `embed/gene_vectors.npy` [10466]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10466 or target_col == 10466). Every well: [[FAM53A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM53A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
