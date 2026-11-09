---
symbol: "MLST8"
type: "gene"
col: 9562
ensembl_id: "ENSG00000167965"
name: "MTOR associated protein MLST8"
location: "16p13.3"
module: 12
arm: "+"
pooled_cpm: 5.95
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 10
n_dd_up_clean: 2
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# MLST8

*MTOR associated protein MLST8* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.86× (z +11.9, q 7e-30, up in 10 of 11 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Pralsetinib (drug)]] 5 µM: 2.20× (z +3.8, q 0.018, up in 6 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.546× (z -7.8, q 3e-12, down in 30 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL40]] (+0.68, fdr 7e-06), [[DECR2]] (+0.67, fdr 1e-05), [[THYN1]] (+0.65, fdr 1e-05); moves opposite to [[TPTEP2-CSNK1E]] (-0.51, fdr 3e-05), [[NFATC2IP]] (-0.51, fdr 6e-05), [[TMED7-TICAM2]] (-0.50, fdr 3e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FAR2P1]], [[POTEF]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9562.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.86×** | +11.9 | 7e-30 | 10/11 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.24×** | +10.8 | 1e-24 | 25/28 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.71×** | +4.6 | 1e-03 | 12/17 (NCI-H2030, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **1.59×** | +4.3 | 0.003 | 16/30 (PANC-1, SHP-77, …) | inconsistent across doses | low cells (technical?) |
| [[Pralsetinib (drug)]] 5 µM |  | **2.20×** | +3.8 | 0.018 | 6/31 (PANC-1, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.47×** | +3.4 | 0.059 | 15/44 (NCI-H460, C32, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9562.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.546×** | -7.8 | 3e-12 | 30/40 (HT-29, LS 180, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.480×** | -6.7 | 5e-09 | 28/46 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.547×** | -5.5 | 6e-06 | 25/46 (C32, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.578×** | -5.0 | 7e-05 | 24/46 (CFPAC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.692×** | -4.8 | 2e-04 | 18/41 (AsPC-1, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.5 µM |  | **0.625×** | -4.3 | 0.002 | 19/46 (HEC-1-A, SW48, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.691×** | -3.4 | 0.056 | 14/43 (SW480, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.685×** | -3.3 | 0.074 | 12/45 (SK-MEL-2, LOX-IMVI, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.705×** | -3.2 | 0.084 | 14/46 (CHP-212, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.707×** | -3.2 | 0.085 | 14/46 (NCI-H2030, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.718× | -3.0 | 0.12 | 11/46 (SW1417, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9562. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 5.96 | 0 | 2 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0567× (z -10.1) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.0680× (z -10.0) |
| [[A549 (line)]] | wt | 4.88 | 0 | 1 | — | [[Erlotinib (drug)]] 5 µM 0.0705× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 4.71 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -9.1) |
| [[C32 (line)]] | wt | 3.87 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0347× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 4.73 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0931× (z -9.5) |
| [[A-172 (line)]] | wt | 5.01 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.43 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.32 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.44 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.45 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.75 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.72 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.30 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.46 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9562), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL40]] | +0.68 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[DECR2]] | +0.67 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[THYN1]] | +0.65 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[SNAPIN]] | +0.63 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[UROS]] | +0.61 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[CUEDC2]] | +0.60 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[SURF2]] | +0.59 | +0.41 / +0.64 | both halves | 4e-05 |  |
| [[NDUFB10]] | +0.59 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[GPS1]] | +0.59 | +0.60 / +0.56 | both halves | 1e-05 | STRING 437 |
| [[THEM6]] | +0.59 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[COMMD8]] | +0.58 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[IFTAP]] | +0.58 | +0.44 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPTEP2-CSNK1E]] | -0.51 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[NFATC2IP]] | -0.51 | -0.50 / -0.39 | both halves | 6e-05 |  |
| [[TMED7-TICAM2]] | -0.50 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[CCDC168]] | -0.49 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[TMEM11-DT]] | -0.49 | -0.38 / -0.40 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAR2P1]], [[POTEF]] | B | FAR2P1, POTEF activity raises MLST8's level | lines that do not express FAR2P1, POTEF (29) vs lines expressing them (21) | 1.19× lower at baseline in the lines without FAR2P1, POTEF | 0.037 | ⚠ within organs, on part of the lines; also absent: POTEE, ENSG00000264660, ENSG00000286329; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.433). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-31.6, 2.0); signed map (-13.3, -22.5). **Vector** length 48.1, 6.33% of its response variance represented; |z| ≥ 3 in 788 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +0.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.6 | +1.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.0 | +10.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.9 | +11.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | -2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.7 | +3.4 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.5 | +3.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.4 | +1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | +0.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +2.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.3 | -7.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.0 | -5.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.9 | -5.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.4 | -6.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.3 | -3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.8 | -1.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.1 | -0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.0 | -0.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.0 | -3.3 |
|  | [[Gallic acid (hydrate) (drug)]] 5 µM |  | -0.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | MTOR associated protein MLST8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:2,204,248-2,209,453 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Lst8, Pop3, GBL, GbetaL |
| Gene groups (HGNC) | WD repeat domain containing; MTOR complex 1; MTOR complex 2 |
| Reactome | 38 pathways, smallest: Dengue virus modulates apoptosis; CD28 dependent PI3K/Akt signaling; mTORC1-mediated signalling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BVC4](https://www.uniprot.org/uniprotkb/Q9BVC4) (Target of rapamycin complex subunit LST8):

> Subunit of both mTORC1 and mTORC2, which regulates cell growth and survival in response to nutrient and hormonal signals. mTORC1 is activated in response to growth factors or amino acids. In response to nutrients, mTORC1 is recruited to the lysosome membrane and promotes protein, lipid and nucleotide synthesis by phosphorylating several substrates, such as ribosomal protein S6 kinase (RPS6KB1 and RPS6KB2) and EIF4EBP1 (4E-BP1). In the same time, it inhibits catabolic pathways by phosphorylating …

**Summary**, from NCBI Gene [64223](https://www.ncbi.nlm.nih.gov/gene/64223):

> Enables protein serine/threonine kinase activator activity and protein-macromolecule adaptor activity. Contributes to protein serine/threonine kinase activity. Involved in TOR signaling; positive regulation of TOR signaling; and regulation of actin cytoskeleton organization. Part of TORC1 complex and TORC2 complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24825](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24825) · Entrez [64223](https://www.ncbi.nlm.nih.gov/gene/64223) · UniProt [Q9BVC4](https://www.uniprot.org/uniprotkb/Q9BVC4) · Ensembl [ENSG00000167965](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167965)

## Data

Gene col 9562: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9562); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9562, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9562]; `tensor/DDL_lfc|DDL_z.npy` [9562]; `embed/gene_vectors.npy` [9562]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9562 or target_col == 9562). Every well: [[MLST8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MLST8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
