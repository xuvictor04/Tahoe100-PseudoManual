---
symbol: "MIEN1"
type: "gene"
col: 6571
ensembl_id: "ENSG00000141741"
name: "migration and invasion enhancer 1"
location: "17q12"
module: 24
arm: "+"
pooled_cpm: 18.44
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# MIEN1

*migration and invasion enhancer 1* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.10× (z +7.6, q 2e-11, up in 31 of 36 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 8.39×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 0.305× (z -4.2, q 0.018, down in 34 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (C32 0.0552×); [[Tadalafil (drug)]] 5 µM in 1 line (SNU-423 0.104×); [[TAK-901 (drug)]] 0.05 µM in 1 line (BT-474 0.223×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 17 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C4orf48]] (+0.78, fdr 1e-05), [[LAGE3]] (+0.78, fdr 7e-06), [[RNF114]] (+0.78, fdr 7e-06); moves opposite to [[EIF4G1]] (-0.67, fdr 1e-05), [[DARS2]] (-0.66, fdr 2e-05), [[U2AF2]] (-0.65, fdr 5e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HES6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 9 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6571.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 8.39×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **3.10×** | +7.6 | 2e-11 | 31/36 (A-427, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **2.57×** | +6.1 | 4e-07 | 20/28 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.32×** | +5.4 | 1e-05 | 35/40 (HOP62, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.18×** | +5.2 | 3e-05 | 41/47 (HEC-1-A, BT-474, …) | two highest doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **2.07×** | +4.9 | 1e-04 | 34/41 (HOP62, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **1.82×** | +4.0 | 0.006 | 34/46 (SW480, NCI-H460, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.76×** | +3.8 | 0.013 | 28/47 (HEC-1-A, HOP62, …) | two highest doses | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.81×** | +3.6 | 0.020 | 15/30 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.61×** | +3.2 | 0.094 | 23/45 (LoVo, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6571.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (C32 0.0552×); [[Tadalafil (drug)]] 5 µM in 1 line (SNU-423 0.104×); [[TAK-901 (drug)]] 0.05 µM in 1 line (BT-474 0.223×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.305×** | -4.2 | 0.018 | 34/43 (BT-474, HT-29, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.595× | -3.3 | 0.28 | 23/47 (BT-474, SW480, …) | inconsistent across doses |  |
| [[Baicalin (drug)]] 5 µM |  | 0.721× | -3.1 | 0.35 | 24/48 (A549, HCT15, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, +0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6571. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 18.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.39× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[BT-474 (line)]] | alt | 159 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.223× (z -9.5) |
| [[C32 (line)]] | wt | 8.80 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0552× (z -10.7) |
| [[SNU-423 (line)]] | alt | 13.8 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.104× (z -9.6) |
| [[A-172 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.48 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.80 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.48 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.86 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 14.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6571), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 17 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C4orf48]] | +0.78 | +0.57 / +0.81 | both halves | 1e-05 |  |
| [[LAGE3]] | +0.78 | +0.63 / +0.79 | both halves | 7e-06 |  |
| [[RNF114]] | +0.78 | +0.62 / +0.75 | both halves | 7e-06 |  |
| [[CIAO2B]] | +0.77 | +0.59 / +0.75 | both halves | 7e-06 |  |
| [[IFI27L2]] | +0.76 | +0.54 / +0.82 | both halves | 1e-05 |  |
| [[ELOB]] | +0.76 | +0.56 / +0.77 | both halves | 1e-05 |  |
| [[MRPL41]] ⚠ | +0.76 | +0.55 / +0.78 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[LAMTOR5]] | +0.76 | +0.49 / +0.79 | both halves | 1e-05 |  |
| [[POLR2J]] ⚠ | +0.74 | +0.55 / +0.74 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[GABARAPL2]] | +0.74 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[KRT10]] ⚠ | +0.74 | +0.61 / +0.78 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[DPM3]] | +0.73 | +0.54 / +0.75 | both halves | 1e-05 |  |
| [[LAMTOR4]] | +0.73 | +0.67 / +0.76 | both halves | 7e-06 |  |
| [[TMEM256]] | +0.73 | +0.52 / +0.74 | both halves | 1e-05 |  |
| [[DCTN6-DT]] | +0.73 | +0.62 / +0.75 | both halves | 7e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G1]] | -0.67 | -0.55 / -0.65 | both halves | 1e-05 |  |
| [[DARS2]] | -0.66 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[U2AF2]] | -0.65 | -0.39 / -0.67 | both halves | 5e-05 |  |
| [[ILF3]] | -0.65 | -0.47 / -0.66 | both halves | 2e-05 |  |
| [[IPO5]] | -0.65 | -0.46 / -0.76 | both halves | 3e-05 |  |
| [[NUP155]] | -0.65 | -0.64 / -0.70 | both halves | 7e-06 |  |
| [[ZMPSTE24]] | -0.64 | -0.39 / -0.63 | both halves | 5e-05 |  |
| [[MCM3AP]] | -0.63 | -0.44 / -0.62 | both halves | 3e-05 |  |
| [[SUPT16H]] | -0.63 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[XRCC5]] | -0.62 | -0.47 / -0.68 | both halves | 2e-05 |  |
| [[MAPKAPK5]] | -0.62 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[UCHL5]] | -0.62 | -0.57 / -0.62 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HES6]] | B | HES6 activity raises MIEN1's level | lines that do not express HES6 (8) vs lines expressing it (42) | 1.62× lower at baseline in the lines without HES6 | 0.013 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.805). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-43.4, -19.8); signed map (-30.8, 9.0). **Vector** length 67.6, 18.3% of its response variance represented; |z| ≥ 3 in 515 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.52 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | +3.0 | +4.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.0 | +5.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +2.5 | +3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +1.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.4 | +2.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.2 | +2.1 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +1.2 | +2.2 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -3.6 | -4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | -0.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -2.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | -2.8 | +3.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | -2.4 | +6.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.1 | -3.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.8 | -1.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | migration and invasion enhancer 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:39,728,496-39,730,532 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC14832, ORB3, XTP4, C35, Rdx12; previously C17orf37 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRT3](https://www.uniprot.org/uniprotkb/Q9BRT3) (Migration and invasion enhancer 1):

> Increases cell migration by inducing filopodia formation at the leading edge of migrating cells. Plays a role in regulation of apoptosis, possibly through control of CASP3. May be involved in a redox-related process.

**Summary**, from NCBI Gene [84299](https://www.ncbi.nlm.nih.gov/gene/84299):

> Involved in negative regulation of apoptotic process; positive regulation of cell migration; and positive regulation of filopodium assembly. Located in cytoplasmic side of plasma membrane and cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28230](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28230) · Entrez [84299](https://www.ncbi.nlm.nih.gov/gene/84299) · UniProt [Q9BRT3](https://www.uniprot.org/uniprotkb/Q9BRT3) · Ensembl [ENSG00000141741](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141741)

## Data

Gene col 6571: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6571); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6571, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6571]; `tensor/DDL_lfc|DDL_z.npy` [6571]; `embed/gene_vectors.npy` [6571]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6571 or target_col == 6571). Every well: [[MIEN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIEN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
