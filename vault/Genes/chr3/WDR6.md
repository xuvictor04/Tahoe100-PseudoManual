---
symbol: "WDR6"
type: "gene"
col: 10913
ensembl_id: "ENSG00000178252"
name: "WD repeat domain 6"
location: "3p21.31"
module: 96
arm: "+"
pooled_cpm: 17.57
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 20
n_dd_up_clean: 0
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/096"]
generated_by: "tahoemap"
---

# WDR6

*WD repeat domain 6* — 3p21.31

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SHP-77 4.52×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.476× (z -9.7, q 2e-19, down in 41 of 47 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.488× (z -9.4, q 2e-18, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OPLAH]] (+0.70, fdr 7e-06, ⚠ OPLAH in the vector space only through flagged drug-doses), [[MED16]] (+0.69, fdr 1e-05), [[USP19]] (+0.68, fdr 7e-06), [[TAF1C]] (+0.67, fdr 7e-06).
> It is in [[Module 096]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10913.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SHP-77 4.52×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 1.29× | +3.4 | 0.42 | 14/47 (KATO III, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | 1.28× | +3.1 | 0.42 | 10/47 (NCI-H2347, RKO, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10913.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.476×** | -9.7 | 2e-19 | 41/47 (NCI-H2030, hTERT-HPNE, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.488×** | -9.4 | 2e-18 | 41/48 (SW1417, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~24% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.610×** | -9.1 | 1e-17 | 34/47 (MIA PaCa-2, SW480, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.670×** | -7.4 | 2e-11 | 25/47 (HS-578T, A-427, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.588×** | -6.9 | 5e-10 | 35/48 (NCI-H1792, NCI-H2347, …) | all doses, flat | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.587×** | -6.7 | 2e-09 | 34/47 (A-427, LS 180, …) | rises with dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.627×** | -6.1 | 9e-08 | 36/48 (RKO, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~17% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.435×** | -5.7 | 9e-07 | 29/48 (NCI-H23, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.658×** | -5.4 | 3e-06 | 26/47 (H4, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.683×** | -5.0 | 4e-05 | 27/48 (NCI-H1792, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.683×** | -5.0 | 4e-05 | 21/47 (A-427, KATO III, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **0.693×** | -4.8 | 9e-05 | 26/46 (BT-474, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.697×** | -4.7 | 1e-04 | 24/48 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.698×** | -4.7 | 1e-04 | 25/47 (AN3 CA, SW480, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.712×** | -4.4 | 4e-04 | 21/47 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.532×** | -4.3 | 6e-04 | 24/44 (SW48, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.560×** | -4.0 | 0.003 | 19/48 (CHP-212, SW48, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **0.784×** | -3.0 | 0.067 | 12/48 (J82, SW480, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10913. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 24.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.158× (z -13.4) |
| [[PANC-1 (line)]] | alt | 17.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.238× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[A-172 (line)]] | wt | 17.4 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.242× (z -8.6) ⚠ toxic |
| [[BT-474 (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0509× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[HepG2_C3A (line)]] | wt | 14.9 | 0 | 1 | — | [[Tadalafil (drug)]] 0.05 µM 0.0889× (z -9.7) |
| [[HS-578T (line)]] | alt | 25.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -16.8) ⚠ cell-cycle shift, explains ~50% of this change |
| [[KATO III (line)]] | alt | 17.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.260× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[MIA PaCa-2 (line)]] | alt | 19.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 14.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.176× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 24.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.372× (z -8.6) |
| [[SHP-77 (line)]] | alt | 20.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.52× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[SW1417 (line)]] | alt | 29.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.235× (z -11.5) |
| [[SW48 (line)]] | wt | 29.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -8.9) |
| [[SW480 (line)]] | alt | 22.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -9.4) |
| [[A498 (line)]] | wt | 7.64 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.32 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.88 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.14 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.39 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.45 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10913), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OPLAH]] ⚠ | +0.70 | +0.70 / +0.66 | both halves | 7e-06 | **novel candidate**; ⚠ in the vector space only through flagged drug-doses |
| [[MED16]] | +0.69 | +0.56 / +0.63 | both halves | 1e-05 | same gene group |
| [[USP19]] | +0.68 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[TAF1C]] | +0.67 | +0.60 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[STRN4]] | +0.66 | +0.63 / +0.54 | both halves | 1e-05 | same gene group |
| [[WIZ]] | +0.65 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[ANAPC2]] | +0.65 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[BAP1]] | +0.64 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[TEPSIN]] | +0.63 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[DUS3L]] | +0.62 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[RHOT2]] | +0.62 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[EME2]] | +0.62 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[DTX3]] | +0.61 | +0.52 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.733). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-13.5, -24.1); signed map (-10.4, -32.0). **Vector** length 74.7, 13.6% of its response variance represented; |z| ≥ 3 in 917 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +3.9 | +3.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.6 | +2.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.1 | -0.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +0.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.9 | +2.3 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.5 | +2.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.2 | +1.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +2.2 | +2.5 |
|  | [[crizotinib (drug)]] 5 µM |  | +2.1 | +1.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +3.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.5 | -9.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.3 | -6.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.9 | -2.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.7 | -5.4 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -2.5 | -2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | -4.0 |
|  | [[Arbutin (drug)]] 5 µM |  | -2.0 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:49,007,062-49,015,953 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Trm734 |
| Gene groups (HGNC) | WD repeat domain containing |
| Reactome | 8 pathways, smallest: RHOV GTPase cycle; RHOU GTPase cycle; RND1 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NNW5](https://www.uniprot.org/uniprotkb/Q9NNW5) (tRNA):

> Together with methyltransferase FTSJ1, methylates the 2'-O-ribose of nucleotides at position 34 of the tRNA anticodon loop of substrate tRNAs. Required for the correct positioning of the substrate tRNA for methylation. Required to suppress amino acid starvation-induced autophagy. Enhances the STK11/LKB1-induced cell growth suppression activity.

**Summary**, from NCBI Gene [11180](https://www.ncbi.nlm.nih.gov/gene/11180):

> This gene encodes a member of the WD repeat protein family. WD repeats are minimally conserved regions of approximately 40 amino acids typically bracketed by gly-his and trp-asp (GH-WD), which may facilitate formation of heterotrimeric or multiprotein complexes. The encoded protein interacts with serine/threonine kinase 11, and is implicated in cell growth arrest. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Feb 2016]

**Accessions** — [HGNC:12758](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12758) · Entrez [11180](https://www.ncbi.nlm.nih.gov/gene/11180) · UniProt [Q9NNW5](https://www.uniprot.org/uniprotkb/Q9NNW5) · Ensembl [ENSG00000178252](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178252)

## Data

Gene col 10913: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10913); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10913, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10913]; `tensor/DDL_lfc|DDL_z.npy` [10913]; `embed/gene_vectors.npy` [10913]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10913 or target_col == 10913). Every well: [[WDR6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
