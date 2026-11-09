---
symbol: "SLC39A4"
type: "gene"
col: 7222
ensembl_id: "ENSG00000147804"
name: "solute carrier family 39 member 4"
location: "8q24.3"
module: 58
arm: "+"
pooled_cpm: 6.86
n_lines_expressing: 44
n_dd_up: 7
n_dd_down: 2
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 4
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# SLC39A4

*solute carrier family 39 member 4* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.51× (z +10.6, q 2e-23, up in 23 of 23 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.574× (z -5.6, q 2e-05, down in 24 of 36 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (PANC-1 0.0410×, Panc 03.27 0.0468×, RKO 0.0553×); [[Homoharringtonine (drug)]] 5 µM in 3 lines (PANC-1 0.132×, SW480 0.189×, NCI-H23 0.164×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MICOS13]] (+0.74, fdr 7e-06), [[CYBA]] (+0.74, fdr 7e-06), [[METRN]] (+0.66, fdr 1e-05); moves opposite to [[ARMT1]] (-0.53, fdr 2e-04), [[RNF6]] (-0.52, fdr 1e-04), [[VBP1]] (-0.49, fdr 9e-05).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 4 go from it, the strongest it → [[C4orf48]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7222.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.51×** | +10.6 | 2e-23 | 23/23 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.06×** | +9.5 | 8e-19 | 10/10 (NCI-H2030, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.48×** | +5.7 | 2e-06 | 11/15 (CFPAC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **2.01×** | +4.9 | 2e-04 | 20/29 (CFPAC-1, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +4.1 | 0.005 | 13/28 (CFPAC-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.79×** | +4.1 | 0.005 | 17/33 (KATO III, NCI-H460, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.69×** | +3.5 | 0.031 | 12/32 (A498, CFPAC-1, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | 1.57× | +3.0 | 0.17 | 10/36 (SW480, NCI-H1573, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7222.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (PANC-1 0.0410×, Panc 03.27 0.0468×, RKO 0.0553×); [[Homoharringtonine (drug)]] 5 µM in 3 lines (PANC-1 0.132×, SW480 0.189×, NCI-H23 0.164×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.574×** | -5.6 | 2e-05 | 24/36 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.503×** | -4.9 | 3e-04 | 21/34 (PANC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.598× | -3.3 | 0.21 | 13/41 (LS 180, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7222. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 6.58 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0410× (z -16.9) |
| [[NCI-H23 (line)]] | alt | 6.96 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -9.4) |
| [[Panc 03.27 (line)]] | alt | 6.23 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0468× (z -11.3) |
| [[RKO (line)]] | wt | 11.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0553× (z -10.9) |
| [[SW480 (line)]] | alt | 6.29 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -11.3) |
| [[A-172 (line)]] | wt | 0.541 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.964 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.31 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.784 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.717 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.65 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7222), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 8 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MICOS13]] | +0.74 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[CYBA]] | +0.74 | +0.73 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[METRN]] | +0.66 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[TMEM276]] | +0.66 | +0.51 / +0.63 | both halves | 1e-05 | ⚠ same locus (47.0 kb, same strand: neighbours can correlate without regulation) |
| [[NME3]] | +0.65 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[TSTD1]] | +0.64 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[ANTKMT]] | +0.64 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[COMTD1]] | +0.64 | +0.43 / +0.71 | both halves | 3e-05 |  |
| [[FAAP20]] | +0.63 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[APRT]] | +0.63 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[DUS1L]] | +0.61 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[MRPL41]] ⚠ | +0.61 | +0.40 / +0.56 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TNNI3]] | +0.60 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[CHCHD10]] | +0.60 | +0.37 / +0.62 | both halves | 7e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARMT1]] | -0.53 | -0.59 / -0.29 | both halves | 2e-04 |  |
| [[RNF6]] | -0.52 | -0.54 / -0.33 | both halves | 1e-04 |  |
| [[VBP1]] | -0.49 | -0.49 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C4orf48]] | B | SLC39A4 activity lowers C4orf48's level | lines that do not express SLC39A4 (6) vs lines expressing it (44) | 1.52× higher at baseline in the lines without SLC39A4 | 0.023 | ⚠ within organs, on part of the lines; also absent: LRRC8B |
| [[JMJD8]] | B | SLC39A4 activity raises JMJD8's level | lines that do not express SLC39A4 (6) vs lines expressing it (44) | 2.01× lower at baseline in the lines without SLC39A4 | 0.026 | ⚠ within organs, on part of the lines; also absent: LRRC8B |
| [[REX1BD]] | B | SLC39A4 activity lowers REX1BD's level | lines that do not express SLC39A4 (6) vs lines expressing it (44) | 1.49× higher at baseline in the lines without SLC39A4 | 0.047 | ⚠ within organs, on part of the lines; also absent: LRRC8B |
| [[SPATS2L]] | B | SLC39A4 activity raises SPATS2L's level | lines that do not express SLC39A4 (6) vs lines expressing it (44) | 1.37× lower at baseline in the lines without SLC39A4 | 0.072 | ⚠ within organs, on part of the lines; also absent: LRRC8B |

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.737). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-46.8, -17.2); signed map (-31.9, 6.3). **Vector** length 47.3, 8.37% of its response variance represented; |z| ≥ 3 in 527 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cristae formation* (reactome, mean cos +0.50 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +1.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +0.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | +2.8 | +4.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | +2.7 | +3.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.6 | +10.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +1.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.2 | +2.2 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.2 | +1.9 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.2 | +1.9 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.1 | +1.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.5 | -4.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | +0.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -1.8 | -5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.6 | -1.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -2.9 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.3 | -2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.2 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 39 member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:144,409,742-144,416,844 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZIP4, ZIP-4, AWMS2; previously AEZ |
| Gene groups (HGNC) | Solute carrier family 39 |
| Reactome | 7 pathways, smallest: Zinc influx into cells by the SLC39 gene family; Zinc transporters; Metal ion SLC transporters |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P5W5](https://www.uniprot.org/uniprotkb/Q6P5W5) (Zinc transporter ZIP4):

> Selective transporter that mediates the uptake of Zn(2+). Plays an essential role for dietary zinc uptake from small intestine (By similarity). The Zn(2+) uniporter activity is regulated by zinc availability. Also exhibits polyspecific binding and transport of Cu(2+), Cd(2+) and possibly Ni(2+) but at higher concentrations.

**Summary**, from NCBI Gene [55630](https://www.ncbi.nlm.nih.gov/gene/55630):

> This gene encodes a member of the zinc/iron-regulated transporter-like protein (ZIP) family. The encoded protein localizes to cell membranes and is required for zinc uptake in the intestine. Mutations in this gene result in acrodermatitis enteropathica. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:17129](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17129) · Entrez [55630](https://www.ncbi.nlm.nih.gov/gene/55630) · UniProt [Q6P5W5](https://www.uniprot.org/uniprotkb/Q6P5W5) · Ensembl [ENSG00000147804](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147804)

## Data

Gene col 7222: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7222); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7222, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7222]; `tensor/DDL_lfc|DDL_z.npy` [7222]; `embed/gene_vectors.npy` [7222]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7222 or target_col == 7222). Every well: [[SLC39A4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC39A4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
