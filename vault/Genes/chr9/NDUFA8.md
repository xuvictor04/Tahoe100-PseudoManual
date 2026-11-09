---
symbol: "NDUFA8"
type: "gene"
col: 4067
ensembl_id: "ENSG00000119421"
name: "NADH:ubiquinone oxidoreductase subunit A8"
location: "9q33.2"
module: 12
arm: "+"
pooled_cpm: 17.12
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 6
n_dd_up_clean: 0
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# NDUFA8

*NADH:ubiquinone oxidoreductase subunit A8* — 9q33.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.28× (z +7.1, q 6e-10, up in 34 of 39 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.573× (z -4.8, q 8e-04, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CINP]] (+0.82, fdr 7e-06), [[COA3]] (+0.75, fdr 7e-06), [[MRPL57]] (+0.74, fdr 7e-06); moves opposite to [[CERS2]] (-0.57, fdr 3e-05), [[SRSF5]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4067.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **2.28×** | +7.1 | 6e-10 | 34/39 (A-172, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **2.21×** | +6.6 | 1e-08 | 24/29 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | **1.65×** | +4.3 | 0.003 | 29/42 (HEC-1-A, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.48×** | +3.4 | 0.087 | 22/48 (NCI-H1792, A549, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.48×** | +3.4 | 0.087 | 20/48 (SW480, A549, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM |  | 1.30× | +3.0 | 0.23 | 22/48 (NCI-H2347, KATO III, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4067.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.573×** | -4.8 | 8e-04 | 37/47 (NCI-H460, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.658×** | -4.7 | 8e-04 | 30/46 (NCI-H460, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.595×** | -4.5 | 0.001 | 29/48 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.674×** | -4.4 | 0.001 | 29/47 (SK-MEL-2, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.673×** | -3.4 | 0.069 | 19/46 (HT-29, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.682×** | -3.3 | 0.091 | 20/47 (NCI-H460, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4067. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 25.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4067), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CINP]] | +0.82 | +0.78 / +0.76 | both halves | 7e-06 |  |
| [[COA3]] | +0.75 | +0.61 / +0.79 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 738 |
| [[MRPL57]] | +0.74 | +0.58 / +0.75 | both halves | 7e-06 |  |
| [[C18orf21]] | +0.73 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[VTA1]] | +0.72 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[TRAPPC5]] | +0.71 | +0.46 / +0.71 | both halves | 3e-05 |  |
| [[ISCA2]] | +0.70 | +0.56 / +0.67 | both halves | 1e-05 | pathway: Aerobic respiration and respiratory electron transport |
| [[ATP5PO]] ⚠ | +0.69 | +0.44 / +0.73 | both halves | 3e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 852; ⚠ in the vector space only through flagged drug-doses |
| [[AGGF1]] | +0.69 | +0.59 / +0.73 | both halves | 7e-06 |  |
| [[ARFIP1]] | +0.69 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[KBTBD6]] | +0.68 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[NDUFB10]] | +0.68 | +0.37 / +0.71 | both halves | 7e-05 | same gene group; pathway: Aerobic respiration and respiratory electron transport; STRING 999 |
| [[NDUFA12]] | +0.68 | +0.43 / +0.71 | both halves | 3e-05 | same gene group; pathway: Aerobic respiration and respiratory electron transport; STRING 999 |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CERS2]] | -0.57 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[SRSF5]] | -0.57 | -0.43 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.683). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-42.7, -6.8); signed map (-17.7, -8.1). **Vector** length 65.2, 15.8% of its response variance represented; |z| ≥ 3 in 473 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +5.3 | +2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.8 | +0.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.7 | +3.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +3.5 | +3.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +2.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.6 | +1.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.4 | -0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.4 | +0.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.3 | -4.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -2.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -1.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.9 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | +0.6 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -0.9 | -0.4 |
|  | [[Encorafenib (drug)]] 5 µM |  | -0.8 | -2.2 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.7 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | NADH:ubiquinone oxidoreductase subunit A8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.2 — chr9:122,144,058-122,159,779 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PGIV, MGC793 |
| Gene groups (HGNC) | NADH:ubiquinone oxidoreductase supernumerary subunits |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 3 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P51970](https://www.uniprot.org/uniprotkb/P51970) (NADH dehydrogenase):

> Accessory subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I), that is believed not to be involved in catalysis. Complex I functions in the transfer of electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone.

**Summary**, from NCBI Gene [4702](https://www.ncbi.nlm.nih.gov/gene/4702):

> The protein encoded by this gene belongs to the complex I 19 kDa subunit family. Mammalian complex I is composed of 45 different subunits. This protein has NADH dehydrogenase activity and oxidoreductase activity. It plays an important role in transfering electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone. Alternative splicing of this gene results in multiple transcript variants encoding different isoforms. [provided by …

**Accessions** — [HGNC:7692](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7692) · Entrez [4702](https://www.ncbi.nlm.nih.gov/gene/4702) · UniProt [P51970](https://www.uniprot.org/uniprotkb/P51970) · Ensembl [ENSG00000119421](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119421)

## Data

Gene col 4067: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4067); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4067, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4067]; `tensor/DDL_lfc|DDL_z.npy` [4067]; `embed/gene_vectors.npy` [4067]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4067 or target_col == 4067). Every well: [[NDUFA8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFA8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
