---
symbol: "TAS2R30"
type: "gene"
col: 14980
ensembl_id: "ENSG00000256188"
name: "taste 2 receptor member 30"
location: "12p13.2"
module: 25
arm: "+"
pooled_cpm: 3.82
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 9
n_dd_up_clean: 0
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# TAS2R30

*taste 2 receptor member 30* — 12p13.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.695× (z -10.3, q 7e-22, down in 44 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.489× (z -5.8, q 2e-06, down in 25 of 45 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SARS2]] (+0.60, fdr 1e-05), [[TAS2R14]] (+0.57, fdr 3e-05, ⚠ read-through risk), [[CAPRIN1]] (+0.54, fdr 5e-05), [[SMARCD1]] (+0.53, fdr 1e-05); moves opposite to [[BICDL2]] (-0.57, fdr 2e-05), [[PPARA]] (-0.57, fdr 5e-05), [[MARCHF9]] (-0.55, fdr 4e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[BICDL2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14980.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pentagastrin (drug)]] 5 µM |  | 1.37× | +3.5 | 0.30 | 8/48 (Hs 766T, LOX-IMVI, …) | top dose only | position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | 1.47× | +3.1 | 0.49 | 8/29 (A498, PANC-1, …) | all doses, flat | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14980.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.695×** | -10.3 | 7e-22 | 44/48 (NCI-H1573, SW480, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.489×** | -5.8 | 2e-06 | 25/45 (HCT15, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.530×** | -5.2 | 4e-05 | 24/46 (HOP62, HepG2/C3A, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.663×** | -4.6 | 6e-04 | 20/36 (NCI-H23, HOP62, …) | top dose only | cell-cycle shift (explains ~12% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.594×** | -4.3 | 0.002 | 18/47 (NCI-H1792, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.601×** | -4.2 | 0.003 | 16/43 (MIA PaCa-2, A-427, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **0.624×** | -3.8 | 0.010 | 16/21 (SW480, PANC-1, …) | inconsistent across doses | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.657×** | -3.4 | 0.043 | 15/38 (LoVo, SW 900, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.665×** | -3.2 | 0.085 | 13/21 (SK-MEL-2, A-427, …) | top dose only | cell-cycle shift (explains ~9% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14980. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 3.64 | 0 | 2 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.458× (z -8.9) ⚠ position not correctable |
| [[A549 (line)]] | wt | 4.21 | 0 | 1 | — | [[Budesonide (drug)]] 0.5 µM 0.0754× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 3.35 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.5 µM 0.0691× (z -10.0) |
| [[LoVo (line)]] | wt | 5.42 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.113× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 8.32 | 0 | 1 | — | [[Decitabine (drug)]] 0.5 µM 0.0733× (z -10.3) |
| [[PANC-1 (line)]] | alt | 3.47 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0690× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change |
| [[SW480 (line)]] | alt | 5.83 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change |
| [[A-172 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.75 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.12 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.19 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.10 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14980), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*40 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SARS2]] | +0.60 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[TAS2R14]] | +0.57 | +0.70 / +0.44 | both halves | 3e-05 | same gene group; pathway: Class C/3 (Metabotropic glutamate/pheromone receptors); STRING 478; ⚠ **readthrough risk**: this gene lies 0.0 kb 3′ of TAS2R14 on the same strand (can correlate by spillover, not regulation) |
| [[CAPRIN1]] | +0.54 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[SMARCD1]] | +0.53 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[XRCC5]] | +0.53 | +0.37 / +0.55 | both halves | 8e-05 |  |
| [[AGAP13P]] | +0.52 | +0.34 / +0.55 | both halves | 1e-04 |  |
| [[MRPS27]] | +0.52 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[EMC1]] | +0.52 | +0.32 / +0.60 | both halves | 2e-04 |  |
| [[NUP205]] | +0.51 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[DTWD2]] | +0.51 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[TMX3]] | +0.51 | +0.33 / +0.55 | both halves | 1e-04 |  |
| [[ILF3]] | +0.51 | +0.30 / +0.50 | both halves | 2e-04 |  |
| [[NUP155]] | +0.51 | +0.36 / +0.59 | both halves | 1e-04 |  |

## Genes that move opposite

*60 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BICDL2]] | -0.57 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[PPARA]] | -0.57 | -0.39 / -0.57 | both halves | 5e-05 |  |
| [[MARCHF9]] | -0.55 | -0.40 / -0.55 | both halves | 4e-05 |  |
| [[SIRT6]] | -0.55 | -0.40 / -0.55 | both halves | 4e-05 |  |
| [[GRB7]] | -0.54 | -0.36 / -0.52 | both halves | 9e-05 |  |
| [[INAFM1]] | -0.54 | -0.39 / -0.59 | both halves | 5e-05 |  |
| [[CLDN4]] | -0.54 | -0.40 / -0.58 | both halves | 5e-05 |  |
| [[UBE2B]] | -0.54 | -0.34 / -0.61 | both halves | 1e-04 |  |
| [[KCNK6]] | -0.53 | -0.32 / -0.60 | both halves | 1e-04 |  |
| [[POLD4]] | -0.53 | -0.31 / -0.60 | both halves | 2e-04 |  |
| [[ZBTB7A]] | -0.53 | -0.39 / -0.61 | both halves | 5e-05 |  |
| [[ACHE]] | -0.53 | -0.49 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BICDL2]] | B | BICDL2 activity lowers TAS2R30's level | lines that do not express BICDL2 (22) vs lines expressing it (28) | 1.18× higher at baseline in the lines without BICDL2 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CRYBG2, MAL2, TNNT2; maybe low, not absent |
| [[JUP]] | B | JUP activity lowers TAS2R30's level | lines that do not express JUP (16) vs lines expressing it (34) | 1.19× higher at baseline in the lines without JUP | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[HDAC6]] | B | HDAC6 activity raises TAS2R30's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TAS2R14]] | C | TAS2R14's natural level strengthens TAS2R30's drug response | TAS2R14's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.58; direction not clear | 0.080 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.497). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-32.4, -27.6); signed map (7.8, -43.3). **Vector** length 40.6, 3.91% of its response variance represented; |z| ≥ 3 in 1,108 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +1.1 | +1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.1 | +2.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.1 | -0.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.0 | +2.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +0.9 | +1.6 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | +0.8 | +2.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +0.8 | +2.3 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | +0.7 | +0.3 |
|  | [[Folic acid (drug)]] 5 µM |  | +0.7 | -0.3 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -2.5 | -3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | -4.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -1.9 | -4.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.5 | -0.8 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -1.2 | -1.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -1.1 | -2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.1 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | taste 2 receptor member 30 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.2 — chr12:11,132,958-11,134,644 (-) |
| Ensembl biotype | protein_coding |
| Also known as | T2R30; previously TAS2R47 |
| Gene groups (HGNC) | Taste 2 receptors |
| Reactome | 8 pathways, smallest: Class C/3 (Metabotropic glutamate/pheromone receptors); Sensory perception of sweet, bitter, and umami (glutamate) taste; Sensory perception of taste |
| Matched by | ensembl_id |

**Function**, from UniProt [P59541](https://www.uniprot.org/uniprotkb/P59541) (Taste receptor type 2 member 30):

> Receptor that may play a role in the perception of bitterness and is gustducin-linked. May play a role in sensing the chemical composition of the gastrointestinal content. The activity of this receptor may stimulate alpha gustducin, mediate PLC-beta-2 activation and lead to the gating of TRPM5 (By similarity).

**Summary**, from NCBI Gene [259293](https://www.ncbi.nlm.nih.gov/gene/259293):

> Enables bitter taste receptor activity. Involved in detection of chemical stimulus involved in sensory perception of bitter taste. Predicted to be located in plasma membrane. Predicted to be active in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19112](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19112) · Entrez [259293](https://www.ncbi.nlm.nih.gov/gene/259293) · UniProt [P59541](https://www.uniprot.org/uniprotkb/P59541) · Ensembl [ENSG00000256188](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000256188)

## Data

Gene col 14980: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14980); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14980, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14980]; `tensor/DDL_lfc|DDL_z.npy` [14980]; `embed/gene_vectors.npy` [14980]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14980 or target_col == 14980). Every well: [[TAS2R30 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAS2R30.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
