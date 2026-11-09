---
symbol: "CDC26"
type: "gene"
col: 10707
ensembl_id: "ENSG00000176386"
name: "cell division cycle 26"
location: "9q32"
module: 179
arm: "+"
pooled_cpm: 6.05
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 4
n_dd_up_clean: 11
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/179"]
generated_by: "tahoemap"
---

# CDC26

*cell division cycle 26* — 9q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.91× (z +9.5, q 7e-19, up in 32 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.602× (z -6.6, q 3e-08, down in 18 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAPN10-DT]] (+0.73, fdr 1e-05), [[HYPK]] (+0.72, fdr 7e-06), [[C12orf73]] (+0.72, fdr 2e-05); moves opposite to [[ROCK2]] (-0.59, fdr 1e-05), [[YTHDC2]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 179]] (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[ERK5-IN-2 (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10707.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.91×** | +9.5 | 7e-19 | 32/42 (SW480, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +7.6 | 7e-12 | 4/9 (HT-29, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.74×** | +7.4 | 2e-11 | 25/45 (NCI-H23, HT-29, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +7.1 | 2e-10 | 20/42 (J82, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.17× | +7.1 | 2e-10 | 13/48 (SW480, NCI-H2347, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.65×** | +6.7 | 2e-09 | 16/37 (HEC-1-A, NCI-H1573, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.58×** | +6.1 | 9e-08 | 14/28 (A549, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.25×** | +5.7 | 1e-06 | 16/40 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.50×** | +5.5 | 3e-06 | 14/47 (HT-29, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.50×** | +5.0 | 3e-05 | 6/20 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +4.1 | 0.002 | 14/41 (AsPC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Almonertinib (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.009 | 8/45 (Hs 766T, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.32×** | +3.5 | 0.018 | 5/43 (PANC-1, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.034 | 8/47 (LoVo, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.063 | 11/44 (NCI-H1792, COLO 205, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.27×** | +3.1 | 0.077 | 4/43 (NCI-H23, HEC-1-A, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.26×** | +3.0 | 0.077 | 4/45 (RKO, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10707.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.602×** | -6.6 | 3e-08 | 18/46 (RKO, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.678×** | -5.2 | 4e-05 | 15/46 (RKO, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.801×** | -4.2 | 0.006 | 20/42 (RKO, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | **0.814×** | -3.9 | 0.015 | 16/47 (LS 180, H4, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.791× | -3.2 | 0.17 | 12/41 (KATO III, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10707. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 5.53 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0831× (z -11.2) |
| [[Hs 766T (line)]] | wt | 8.43 | 0 | 1 | — | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM 0.0901× (z -10.7) |
| [[KATO III (line)]] | alt | 9.70 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 3.28 | 0 | 1 | — | [[Dexamethasone (drug)]] 0.05 µM 0.0813× (z -9.6) |
| [[RKO (line)]] | wt | 10.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -8.7) |
| [[SHP-77 (line)]] | alt | 7.71 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0806× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 5.78 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0844× (z -9.2) |
| [[A-427 (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.12 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.18 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.01 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.04 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.23 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.56 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.97 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.67 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.80 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.83 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10707), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAPN10-DT]] | +0.73 | +0.56 / +0.79 | both halves | 1e-05 |  |
| [[HYPK]] | +0.72 | +0.59 / +0.79 | both halves | 7e-06 |  |
| [[C12orf73]] | +0.72 | +0.47 / +0.80 | both halves | 2e-05 |  |
| [[CRELD1]] | +0.70 | +0.59 / +0.76 | both halves | 7e-06 |  |
| [[TMED7-TICAM2]] | +0.69 | +0.57 / +0.72 | both halves | 9e-06 |  |
| [[COPA]] | +0.69 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[SEC61A1]] | +0.68 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[GPR107]] | +0.68 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[DERL1]] | +0.67 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[COX7A2L]] | +0.66 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[KDELR1]] | +0.66 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[SURF4]] | +0.66 | +0.58 / +0.68 | both halves | 8e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ROCK2]] | -0.59 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[YTHDC2]] | -0.58 | -0.60 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[ERK5-IN-2 (drug)]] 5 µM | C | CDC26's natural level raises the cells' numbers under ERK5-IN-2 5 µM (protects the cells) | CDC26's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.65 | 0.360 over the table, 0.096 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 179]] — RHOA GTPase cycle; 22 genes; this gene is in the **+** arm (projection on the module's main direction 0.827). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (17.2, -28.7); signed map (-46.5, 10.4). **Vector** length 54.8, 6.98% of its response variance represented; |z| ≥ 3 in 875 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.9 | +7.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +7.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +7.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.0 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.8 | +5.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | +5.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | -0.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +1.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.3 | -6.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.6 | -5.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.6 | -3.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.3 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.7 | -1.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.6 | -1.1 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.5 | -1.7 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.4 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | cell division cycle 26 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q32 — chr9:113,255,835-113,275,572 (-) |
| Ensembl biotype | protein_coding |
| Also known as | APC12, ANAPC12; previously C9orf17 |
| Gene groups (HGNC) | Anaphase promoting complex |
| Reactome | 42 pathways, smallest: Aberrant regulation of mitotic exit in cancer due to RB1 defects; Conversion from APC/C:Cdc20 to APC/C:Cdh1 in late anaphase; Phosphorylation of the APC/C |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NHZ8](https://www.uniprot.org/uniprotkb/Q8NHZ8) (Anaphase-promoting complex subunit CDC26):

> Component of the anaphase promoting complex/cyclosome (APC/C), a cell cycle-regulated E3 ubiquitin ligase that controls progression through the cell cycle. Together with the RING-H2 protein ANAPC11, forms the catalytic component of the E3 ubiquitin ligase complex. APC/C acts by mediating ubiquitination and subsequent degradation of target proteins: it mainly mediates the formation of 'Lys-11'-linked polyubiquitin chains and, to a lower extent, the formation of 'Lys-48'- and 'Lys-63'-linked …

**Summary**, from NCBI Gene [246184](https://www.ncbi.nlm.nih.gov/gene/246184):

> The protein encoded by this gene is highly similar to Saccharomyces cerevisiae Cdc26, a component of cell cycle anaphase-promoting complex (APC). APC is composed of a group of highly conserved proteins and functions as a cell cycle-regulated ubiquitin-protein ligase. APC thus is responsible for the cell cycle regulated proteolysis of various proteins. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17839](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17839) · Entrez [246184](https://www.ncbi.nlm.nih.gov/gene/246184) · UniProt [Q8NHZ8](https://www.uniprot.org/uniprotkb/Q8NHZ8) · Ensembl [ENSG00000176386](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176386)

## Data

Gene col 10707: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10707); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10707, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10707]; `tensor/DDL_lfc|DDL_z.npy` [10707]; `embed/gene_vectors.npy` [10707]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10707 or target_col == 10707). Every well: [[CDC26 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDC26.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
