---
symbol: "NDUFA12"
type: "gene"
col: 11573
ensembl_id: "ENSG00000184752"
name: "NADH:ubiquinone oxidoreductase subunit A12"
location: "12q22"
module: 17
arm: "+"
pooled_cpm: 37.45
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# NDUFA12

*NADH:ubiquinone oxidoreductase subunit A12* — 12q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.04× (z +7.2, q 4e-10, up in 45 of 48 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.26× (z +3.2, q 0.060, up in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 3.54×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 3.10×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DPY30]] (+0.81, fdr 7e-06), [[COMMD2]] (+0.76, fdr 7e-06), [[DNAJC19]] (+0.73, fdr 1e-05); moves opposite to [[PSMD6-AS1]] (-0.70, fdr 3e-05), [[GALNT7-DT]] (-0.67, fdr 5e-05), [[AKT1S1]] (-0.66, fdr 4e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF420]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 11 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11573.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 3.54×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 3.10×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.04×** | +7.2 | 4e-10 | 45/48 (RKO, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.93×** | +6.6 | 9e-09 | 46/48 (NCI-H1792, RKO, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | **1.86×** | +6.2 | 9e-08 | 39/44 (PANC-1, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.82×** | +6.0 | 3e-07 | 47/48 (A549, BT-474, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | **1.70×** | +5.2 | 3e-05 | 28/39 (PANC-1, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +4.4 | 0.001 | 39/47 (RKO, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~63% of this change | **1.45×** | +3.8 | 0.014 | 28/46 (KATO III, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~60% of this change | **1.46×** | +3.6 | 0.018 | 27/47 (LoVo, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.43×** | +3.6 | 0.018 | 27/48 (NCI-H1573, NCI-H460, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.40×** | +3.4 | 0.035 | 25/47 (J82, NCI-H460, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.060 | 24/48 (A-427, NCI-H1573, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.36×** | +3.1 | 0.098 | 21/47 (NCI-H1573, SW480, …) | top dose only |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11573. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 37.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.54× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | — |
| [[A-172 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 43.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 43.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 44.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 44.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11573), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPY30]] | +0.81 | +0.60 / +0.76 | both halves | 7e-06 |  |
| [[COMMD2]] | +0.76 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[DNAJC19]] | +0.73 | +0.54 / +0.66 | both halves | 1e-05 | STRING 495 |
| [[MNAT1]] | +0.72 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[MKRN2]] | +0.71 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[POLR2I]] | +0.70 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[WRAP73]] | +0.69 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[PIGH]] | +0.68 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[MFSD9]] | +0.68 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[SCRN2]] | +0.68 | +0.39 / +0.61 | both halves | 5e-05 |  |
| [[ATG4C]] | +0.68 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[THYN1]] | +0.68 | +0.49 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD6-AS1]] | -0.70 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[GALNT7-DT]] | -0.67 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[AKT1S1]] | -0.66 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[PHF8]] | -0.66 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[SPON1-AS1]] | -0.65 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[SECISBP2]] | -0.64 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[PCBP1-AS1]] | -0.64 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[EFCAB2]] | -0.63 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[CCDC90B-AS1]] | -0.62 | -0.39 / -0.26 | both halves | 3e-04 |  |
| [[MMADHC-DT]] | -0.62 | -0.40 / -0.21 | both halves | 7e-04 |  |
| [[TUG1]] | -0.62 | -0.32 / -0.52 | both halves | 2e-04 |  |
| [[FAM174B]] | -0.62 | -0.38 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF420]] | B | ZNF420 activity lowers NDUFA12's level | lines that do not express ZNF420 (7) vs lines expressing it (43) | 1.20× higher at baseline in the lines without ZNF420 | 0.094 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF850, ZNF540 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.725). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-26.5, -4.1); signed map (-22.9, -12.8). **Vector** length 68.4, 18.6% of its response variance represented; |z| ≥ 3 in 515 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.2 | +3.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +3.8 | +7.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +3.8 | +6.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +3.6 | +6.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +0.9 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.7 | +1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.4 | +0.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +1.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.4 | -2.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -0.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | +0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | +1.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -0.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.3 | -1.0 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.2 | -2.8 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.2 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | NADH:ubiquinone oxidoreductase subunit A12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q22 — chr12:94,895,297-95,003,748 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DAP13, B17.2 |
| Gene groups (HGNC) | NADH:ubiquinone oxidoreductase supernumerary subunits |
| Reactome | 3 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UI09](https://www.uniprot.org/uniprotkb/Q9UI09) (NADH dehydrogenase):

> Accessory subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I), that is believed not to be involved in catalysis. Complex I functions in the transfer of electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone.

**Summary**, from NCBI Gene [55967](https://www.ncbi.nlm.nih.gov/gene/55967):

> This gene encodes a protein which is part of mitochondrial complex 1, part of the oxidative phosphorylation system in mitochondria. Complex 1 transfers electrons to ubiquinone from NADH which establishes a proton gradient for the generation of ATP. Mutations in this gene are associated with Leigh syndrome due to mitochondrial complex 1 deficiency. Pseudogenes of this gene are located on chromosomes 5 and 13. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Apr …

**Accessions** — [HGNC:23987](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23987) · Entrez [55967](https://www.ncbi.nlm.nih.gov/gene/55967) · UniProt [Q9UI09](https://www.uniprot.org/uniprotkb/Q9UI09) · Ensembl [ENSG00000184752](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184752)

## Data

Gene col 11573: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11573); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11573, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11573]; `tensor/DDL_lfc|DDL_z.npy` [11573]; `embed/gene_vectors.npy` [11573]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11573 or target_col == 11573). Every well: [[NDUFA12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFA12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
