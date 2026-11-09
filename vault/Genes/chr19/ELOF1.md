---
symbol: "ELOF1"
type: "gene"
col: 5028
ensembl_id: "ENSG00000130165"
name: "elongation factor 1"
location: "19p13.2"
module: 12
arm: "+"
pooled_cpm: 10.19
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# ELOF1

*elongation factor 1* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 3.19× (z +12.4, q 1e-32, up in 47 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM in 1 line (Hs 766T 0.0531×); [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM in 1 line (Hs 766T 0.0654×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (RKO 0.0802×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL10]] (+0.76, fdr 7e-06), [[C18orf21]] (+0.70, fdr 7e-06), [[MED19]] (+0.69, fdr 7e-06); moves opposite to [[HNRNPA3]] (-0.62, fdr 5e-05), [[RBBP4]] (-0.58, fdr 3e-05), [[CPSF6]] (-0.58, fdr 7e-06).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[KRT19]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5028.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **3.19×** | +12.4 | 1e-32 | 47/47 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.16×** | +12.3 | 2e-32 | 46/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.19×** | +11.9 | 4e-30 | 43/46 (A498, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.90×** | +11.4 | 7e-28 | 46/47 (SW480, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.31×** | +9.0 | 4e-17 | 40/43 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.20×** | +8.1 | 5e-14 | 34/39 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.20×** | +8.0 | 7e-14 | 39/47 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +7.8 | 4e-13 | 35/44 (PANC-1, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~16% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.12×** | +7.7 | 7e-13 | 39/46 (NCI-H460, LS 180, …) | rises with dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.81×** | +6.3 | 1e-08 | 34/46 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change | **1.56×** | +4.8 | 1e-04 | 13/34 (NCI-H460, A498, …) | all doses, flat | composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.52×** | +4.5 | 3e-04 | 23/44 (SNU-423, SW1417, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.46×** | +4.0 | 0.003 | 20/47 (C32, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.42×** | +3.8 | 0.006 | 18/47 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.43×** | +3.7 | 0.008 | 14/45 (NCI-H23, HEC-1-A, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.41×** | +3.4 | 0.021 | 16/45 (LS 180, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.025 | 16/47 (LoVo, PANC-1, …) | rises with dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.67×** | +3.3 | 0.029 | 11/44 (SW480, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM in 1 line (Hs 766T 0.0531×); [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM in 1 line (Hs 766T 0.0654×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (RKO 0.0802×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5028. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 11.1 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.07× (z +9.1) | — |
| [[Hs 766T (line)]] | wt | 7.71 | 0 | 2 | — | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM 0.0531× (z -11.7) |
| [[A498 (line)]] | wt | 11.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +8.9) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[AsPC-1 (line)]] | alt | 9.19 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +8.6) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[PANC-1 (line)]] | alt | 7.51 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +8.7) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[RKO (line)]] | wt | 13.7 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0802× (z -10.7) |
| [[A-172 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.16 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.31 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.92 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.74 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.65 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.72 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.98 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.08 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.33 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5028), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL10]] | +0.76 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[C18orf21]] | +0.70 | +0.72 / +0.58 | both halves | 7e-06 |  |
| [[MED19]] | +0.69 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[SNAPIN]] | +0.68 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[LENG1]] | +0.68 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[R3HCC1]] | +0.66 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[POLD4]] | +0.66 | +0.39 / +0.63 | both halves | 6e-05 |  |
| [[NRBF2]] | +0.66 | +0.73 / +0.53 | both halves | 1e-05 |  |
| [[DNTTIP1]] | +0.65 | +0.61 / +0.34 | both halves | 1e-04 |  |
| [[NAA30]] | +0.63 | +0.60 / +0.58 | both halves | 8e-06 |  |
| [[RNF113A]] | +0.63 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[ASB8]] | +0.63 | +0.67 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPA3]] | -0.62 | -0.39 / -0.76 | both halves | 5e-05 |  |
| [[RBBP4]] | -0.58 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[CPSF6]] | -0.58 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[RCC2]] | -0.57 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[NUDT3]] | -0.55 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[SNX5]] | -0.53 | -0.19 / -0.51 | ⚠ one half (not replicated) | 8e-04 |  |
| [[ATP1B3]] | -0.53 | -0.67 / -0.22 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KRT19]] | B | KRT19 activity lowers ELOF1's level | lines that do not express KRT19 (22) vs lines expressing it (28) | 1.09× higher at baseline in the lines without KRT19 | 0.070 | ⚠ within organs, on part of the lines; also absent: RNF223, TINAGL1, CLDN4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.677). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-40.1, -8.2); signed map (-15.6, -7.1). **Vector** length 52.8, 8.28% of its response variance represented; |z| ≥ 3 in 816 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +2.8 | +8.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +2.8 | +7.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +2.4 | +11.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.2 | +9.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.1 | +6.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.9 | +2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | +1.6 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.4 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.3 | +4.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +1.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -0.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | +0.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.5 | +1.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change | -2.4 | +3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | +1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.3 | +2.7 |
|  | [[Encorafenib (drug)]] 5 µM |  | -0.9 | -1.8 |
|  | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.5 µM |  | -0.8 | -1.9 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -0.8 | -1.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -0.8 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | elongation factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:11,551,147-11,559,230 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC4549, ELF1 |
| Matched by | ensembl_id |

**Function**, from UniProt [P60002](https://www.uniprot.org/uniprotkb/P60002) (Transcription elongation factor 1 homolog):

> Factor involved in transcription-coupled nucleotide excision repair (TC-NER), a mechanism that rapidly removes RNA polymerase II-blocking lesions from the transcribed strand of active genes. Acts as a key adapter required to anchor TC-NER factors to RNA polymerase II: stably positions UVSSA and the DCX(ERCC8) complex (also named CSA complex) on arrested RNA polymerase II, leading to neddylation and activation of the DCX(ERCC8) complex and ubiquitination of RNA polymerase II.

**Summary**, from NCBI Gene [84337](https://www.ncbi.nlm.nih.gov/gene/84337):

> Enables RNA polymerase II complex binding activity and protein-macromolecule adaptor activity. Involved in transcription-coupled nucleotide-excision repair. Is active in chromosome and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28691](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28691) · Entrez [84337](https://www.ncbi.nlm.nih.gov/gene/84337) · UniProt [P60002](https://www.uniprot.org/uniprotkb/P60002) · Ensembl [ENSG00000130165](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130165)

## Data

Gene col 5028: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5028); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5028, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5028]; `tensor/DDL_lfc|DDL_z.npy` [5028]; `embed/gene_vectors.npy` [5028]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5028 or target_col == 5028). Every well: [[ELOF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ELOF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
