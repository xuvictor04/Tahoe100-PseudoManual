---
symbol: "RPS26"
type: "gene"
col: 12449
ensembl_id: "ENSG00000197728"
name: "ribosomal protein S26"
location: "12q13.2"
module: 43
arm: "+"
pooled_cpm: 44.27
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 1
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# RPS26

*ribosomal protein S26* — 12q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.27× (z +7.0, q 1e-09, up in 44 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 2.18× (z +3.3, q 0.065, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.695× (z -7.4, q 9e-11, down in 46 of 48 measured lines) ⚠ position not correctable.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.274×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 23 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP5ME]] (+0.84, fdr 7e-06), [[RPL17]] (+0.82, fdr 7e-06), [[ATP5MJ]] (+0.82, fdr 1e-05); moves opposite to [[EIF4G2]] (-0.71, fdr 5e-05), [[FGD5-AS1]] (-0.70, fdr 2e-05), [[MOB1A]] (-0.69, fdr 3e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 8 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12449.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **3.27×** | +7.0 | 1e-09 | 44/47 (NCI-H1792, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **2.22×** | +4.7 | 7e-04 | 44/48 (SW480, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.24×** | +4.6 | 8e-04 | 42/46 (J82, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~10% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **2.13×** | +4.5 | 0.001 | 40/48 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **2.18×** | +4.4 | 0.001 | 31/39 (NCI-H460, SW480, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **2.11×** | +4.1 | 0.004 | 33/44 (HOP62, A549, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **2.00×** | +3.9 | 0.006 | 36/47 (A-172, LoVo, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.94×** | +3.9 | 0.006 | 40/48 (SW480, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.18×** | +3.3 | 0.065 | 41/47 (NCI-H460, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | 2.07× | +3.1 | 0.12 | 37/48 (A-427, SW 900, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12449.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.274×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.695×** | -7.4 | 9e-11 | 46/48 (LS 180, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.51 per unit of S-phase module lfc, +0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12449. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 51.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 47.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 48.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 92.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 78.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 47.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 86.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 104 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 47.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 71.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 59.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 37.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12449), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 23 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP5ME]] | +0.84 | +0.69 / +0.85 | both halves | 7e-06 |  |
| [[RPL17]] | +0.82 | +0.66 / +0.82 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[ATP5MJ]] | +0.82 | +0.53 / +0.83 | both halves | 1e-05 |  |
| [[RPL36]] | +0.82 | +0.63 / +0.84 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL35]] ⚠ | +0.81 | +0.67 / +0.80 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL23]] | +0.80 | +0.62 / +0.82 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[TOMM7]] | +0.79 | +0.51 / +0.84 | both halves | 1e-05 | pathway: Protein localization; STRING 408 |
| [[SF3B6]] | +0.79 | +0.68 / +0.76 | both halves | 7e-06 |  |
| [[RPS10]] | +0.78 | +0.58 / +0.79 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[COMMD6]] | +0.78 | +0.50 / +0.81 | both halves | 1e-05 |  |
| [[RBIS]] | +0.77 | +0.46 / +0.77 | both halves | 2e-05 |  |
| [[RPS17]] ⚠ | +0.77 | +0.57 / +0.80 | both halves | 9e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL31]] | +0.77 | +0.50 / +0.79 | both halves | 1e-05 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS14]] | +0.77 | +0.52 / +0.77 | both halves | 1e-05 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G2]] | -0.71 | -0.40 / -0.70 | both halves | 5e-05 | pathway: Antimicrobial mechanism of IFN-stimulated genes |
| [[FGD5-AS1]] | -0.70 | -0.47 / -0.66 | both halves | 2e-05 |  |
| [[MOB1A]] | -0.69 | -0.44 / -0.74 | both halves | 3e-05 |  |
| [[SCRN1]] | -0.68 | -0.39 / -0.65 | both halves | 5e-05 |  |
| [[CHRAC1]] | -0.67 | -0.46 / -0.64 | both halves | 3e-05 |  |
| [[NXT2]] | -0.65 | -0.40 / -0.57 | both halves | 4e-05 |  |
| [[PSME3]] | -0.64 | -0.38 / -0.68 | both halves | 6e-05 |  |
| [[TUG1]] | -0.64 | -0.26 / -0.62 | both halves | 4e-04 |  |
| [[HCFC1]] | -0.63 | -0.38 / -0.64 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers RPS26's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.736). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-44.2, -24.9); signed map (-57.9, -3.4). **Vector** length 66.5, 23.0% of its response variance represented; |z| ≥ 3 in 476 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide* (reactome, mean cos +0.66 to 34); *oxidative phosphorylation* (hallmark, mean cos +0.55 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +1.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +1.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +0.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +2.7 | +4.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +2.5 | +3.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.3 | -0.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +1.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.7 | +2.7 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | -3.8 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | -3.4 | +4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | +1.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | -3.3 | +7.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | +1.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.5 | -1.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.4 | +0.1 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.3 | -2.4 |
|  | [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | -1.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein S26 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.2 — chr12:56,041,351-56,044,697 (+) |
| Ensembl biotype | protein_coding |
| Also known as | S26, eS26 |
| Gene groups (HGNC) | S ribosomal proteins |
| Reactome | 51 pathways, smallest: SARS-CoV-1 modulates host translation machinery; SARS-CoV-2 modulates host translation machinery; Formation of the ternary complex, and subsequently, the 43S complex |
| Matched by | ensembl_id |

**Function**, from UniProt [P62854](https://www.uniprot.org/uniprotkb/P62854) (Small ribosomal subunit protein eS26):

> Component of the small ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell.

**Summary**, from NCBI Gene [6231](https://www.ncbi.nlm.nih.gov/gene/6231):

> This gene encodes a ribosomal protein that is a component of the 40S subunit. The protein belongs to the S26E family of ribosomal proteins. Mutations in this gene are found in Diamond-Blackfan anemia 10. There are multiple processed pseudogenes of this gene dispersed through the genome. [provided by RefSeq, Aug 2017]

**Accessions** — [HGNC:10414](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10414) · Entrez [6231](https://www.ncbi.nlm.nih.gov/gene/6231) · UniProt [P62854](https://www.uniprot.org/uniprotkb/P62854) · Ensembl [ENSG00000197728](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197728)

## Data

Gene col 12449: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12449); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12449, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12449]; `tensor/DDL_lfc|DDL_z.npy` [12449]; `embed/gene_vectors.npy` [12449]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12449 or target_col == 12449). Every well: [[RPS26 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPS26.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
