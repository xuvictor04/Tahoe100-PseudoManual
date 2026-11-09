---
symbol: "NDUFA11"
type: "gene"
col: 10536
ensembl_id: "ENSG00000174886"
name: "NADH:ubiquinone oxidoreductase subunit A11"
location: "19p13.3"
module: 48
arm: "+"
pooled_cpm: 19.19
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/048", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# NDUFA11

*NADH:ubiquinone oxidoreductase subunit A11* — 19p13.3

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.95× (z +10.2, q 1e-21, up in 41 of 42 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (SHP-77 9.57×, A-172 5.04×, PANC-1 4.72×, LS 180 5.53×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H460 6.62×, SW480 4.91×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.279×, RKO 0.288×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (NCI-H23 0.151×; ⚠ toxic; cell-cycle shift, explains ~91% of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 17 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UQCR11]] (+0.78, fdr 7e-06), [[MICOS13]] (+0.77, fdr 1e-05), [[C4orf48]] (+0.76, fdr 1e-05); moves opposite to [[EIF4G2]] (-0.59, fdr 8e-05), [[CFAP97]] (-0.57, fdr 6e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10536.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (SHP-77 9.57×, A-172 5.04×, PANC-1 4.72×, LS 180 5.53×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H460 6.62×, SW480 4.91×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **3.95×** | +10.2 | 1e-21 | 41/42 (SHP-77, A-172, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.99×** | +7.5 | 2e-11 | 35/37 (MIA PaCa-2, SW480, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **2.68×** | +7.0 | 4e-10 | 31/34 (NCI-H460, SW480, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **1.87×** | +4.6 | 5e-04 | 33/46 (NCI-H460, SW480, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **1.73×** | +4.1 | 0.005 | 30/44 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +4.0 | 0.005 | 28/45 (CFPAC-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.57×** | +3.3 | 0.068 | 24/48 (LOX-IMVI, LS 180, …) | two highest doses | position effect removed |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.279×, RKO 0.288×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (NCI-H23 0.151×; ⚠ toxic; cell-cycle shift, explains ~91% of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10536. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 19.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.91× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[A-172 (line)]] | wt | 22.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.04× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[A-427 (line)]] | wt | 26.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -9.5) |
| [[A498 (line)]] | wt | 22.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.36× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[LS 180 (line)]] | wt | 22.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.53× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H23 (line)]] | alt | 19.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.151× (z -9.5) ⚠ toxic; cell-cycle shift, explains ~91% of this change |
| [[NCI-H460 (line)]] | wt | 13.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.62× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[PANC-1 (line)]] | alt | 19.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[RKO (line)]] | wt | 28.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -9.2) |
| [[SHP-77 (line)]] | alt | 18.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.57× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 22.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.34× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[A549 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10536), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 17 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UQCR11]] | +0.78 | +0.66 / +0.77 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 990 |
| [[MICOS13]] | +0.77 | +0.53 / +0.76 | both halves | 1e-05 | STRING 641 |
| [[C4orf48]] | +0.76 | +0.55 / +0.74 | both halves | 1e-05 |  |
| [[ATP5MJ]] | +0.76 | +0.56 / +0.74 | both halves | 1e-05 | pathway: Aerobic respiration and respiratory electron transport |
| [[COX6C]] | +0.75 | +0.66 / +0.69 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 785 |
| [[UQCRQ]] ⚠ | +0.75 | +0.63 / +0.71 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 997; ⚠ in the vector space only through flagged drug-doses |
| [[NDUFB11]] ⚠ | +0.74 | +0.69 / +0.79 | both halves | 7e-06 | same gene group; pathway: Aerobic respiration and respiratory electron transport; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[COX6B1]] | +0.74 | +0.64 / +0.76 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 945 |
| [[ELOB]] | +0.73 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[ATP5MK]] | +0.73 | +0.62 / +0.68 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport |
| [[UBL5]] | +0.73 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[ROMO1]] | +0.73 | +0.63 / +0.71 | both halves | 7e-06 | same gene group; STRING 638 |
| [[COX6A1]] | +0.73 | +0.64 / +0.62 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 737 |
| [[TMEM256]] | +0.72 | +0.39 / +0.75 | both halves | 6e-05 | STRING 489 |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G2]] | -0.59 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[CFAP97]] | -0.57 | -0.56 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.808). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-46.8, -20.0); signed map (-34.1, 7.9). **Vector** length 45.0, 9.04% of its response variance represented; |z| ≥ 3 in 444 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *oxidative phosphorylation* (hallmark, mean cos +0.62 to 24); *Complex IV assembly* (reactome, mean cos +0.61 to 11); *Formation of ATP by chemiosmotic coupling* (reactome, mean cos +0.66 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | +2.4 | +4.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +2.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +2.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | +1.9 | +3.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.8 | +0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.3 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +1.9 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.1 | +1.3 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +1.0 | +1.2 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +0.9 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | +1.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | +1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | +0.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.5 | -0.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -2.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.1 | -2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.0 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | NADH:ubiquinone oxidoreductase subunit A11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:5,891,276-5,904,006 (-) |
| Ensembl biotype | protein_coding |
| Also known as | B14.7 |
| Gene groups (HGNC) | NADH:ubiquinone oxidoreductase supernumerary subunits; Tim17 family |
| Reactome | 3 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86Y39](https://www.uniprot.org/uniprotkb/Q86Y39) (NADH dehydrogenase):

> Accessory subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I), that is believed not to be involved in catalysis. Complex I functions in the transfer of electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone.

**Summary**, from NCBI Gene [126328](https://www.ncbi.nlm.nih.gov/gene/126328):

> This gene encodes a subunit of the membrane-bound mitochondrial complex I. Complex I is composed of numerous subunits and functions as the NADH-ubiquinol reductase of the mitochondrial electron transport chain. Mutations in this gene are associated with severe mitochondrial complex I deficiency. Alternate splicing results in multiple transcript variants.[provided by RefSeq, Oct 2010]

**Accessions** — [HGNC:20371](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20371) · Entrez [126328](https://www.ncbi.nlm.nih.gov/gene/126328) · UniProt [Q86Y39](https://www.uniprot.org/uniprotkb/Q86Y39) · Ensembl [ENSG00000174886](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174886)

## Data

Gene col 10536: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10536); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10536, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10536]; `tensor/DDL_lfc|DDL_z.npy` [10536]; `embed/gene_vectors.npy` [10536]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10536 or target_col == 10536). Every well: [[NDUFA11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFA11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
