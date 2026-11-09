---
symbol: "GTF2H2"
type: "gene"
col: 7020
ensembl_id: "ENSG00000145736"
name: "general transcription factor IIH subunit 2"
location: "5q13.2"
module: 54
arm: "+"
pooled_cpm: 5.67
n_lines_expressing: 48
n_dd_up: 9
n_dd_down: 1
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# GTF2H2

*general transcription factor IIH subunit 2* — 5q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.96× (z +7.9, q 1e-12, up in 27 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.796× (z -3.8, q 0.077, down in 16 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.5 µM in 1 line (LoVo 0.123×; ⚠ cell-cycle shift, explains ~0% of this change); [[Trimetrexate (drug)]] 0.5 µM in 1 line (KATO III 0.0478×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (KATO III 0.138×); [[Azithromycin (hydrate) (drug)]] 0.5 µM in 1 line (SHP-77 0.0907×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GTF2H2B]] (+0.74, fdr 7e-06), [[GTF2H2C]] (+0.72, fdr 7e-06), [[PET117]] (+0.71, fdr 2e-05); moves opposite to [[NXT2]] (-0.63, fdr 3e-05), [[EIF4G2]] (-0.60, fdr 1e-04), [[ATN1]] (-0.60, fdr 2e-05).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7020.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.96×** | +7.9 | 1e-12 | 27/45 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.89×** | +7.5 | 1e-11 | 24/45 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.88×** | +7.5 | 1e-11 | 11/23 (SW480, LoVo, …) | two highest doses | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +7.2 | 1e-10 | 19/29 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.78×** | +6.8 | 1e-09 | 24/45 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.55×** | +5.0 | 6e-05 | 3/9 (NCI-H2347, HOP62, …) | two highest doses | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.46×** | +4.5 | 6e-04 | 10/45 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.033 | 7/45 (SW1417, HOP62, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.33×** | +3.4 | 0.047 | 10/45 (SW480, SW 900, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | 1.29× | +3.0 | 0.13 | 7/44 (AsPC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~13% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7020.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.5 µM in 1 line (LoVo 0.123×; ⚠ cell-cycle shift, explains ~0% of this change); [[Trimetrexate (drug)]] 0.5 µM in 1 line (KATO III 0.0478×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (KATO III 0.138×); [[Azithromycin (hydrate) (drug)]] 0.5 µM in 1 line (SHP-77 0.0907×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.796×** | -3.8 | 0.077 | 16/42 (KATO III, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.773× | -3.0 | 0.68 | 8/45 (NCI-H460, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7020. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 3.08 | 0 | 2 | — | [[Trimetrexate (drug)]] 0.5 µM 0.0478× (z -9.7) |
| [[A-172 (line)]] | wt | 4.09 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.117× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 4.83 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.123× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 5.67 | 0 | 1 | — | [[Azithromycin (hydrate) (drug)]] 0.5 µM 0.0907× (z -8.5) |
| [[A-427 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.01 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.22 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.96 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.34 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.742 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.970 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.88 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.54 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.23 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.90 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.51 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7020), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2H2B]] | +0.74 | +0.60 / +0.73 | both halves | 7e-06 |  |
| [[GTF2H2C]] | +0.72 | +0.69 / +0.66 | both halves | 7e-06 | STRING 986 |
| [[PET117]] | +0.71 | +0.46 / +0.68 | both halves | 2e-05 |  |
| [[DHX57]] | +0.70 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[PUS3]] | +0.66 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[ZNF74]] | +0.66 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[DDX55]] | +0.65 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[NOL7]] ⚠ | +0.64 | +0.47 / +0.61 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ORC5]] | +0.63 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[FRA10AC1]] | +0.63 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[AP3S2]] | +0.63 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[KNOP1]] | +0.63 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[RPP21]] | +0.62 | +0.43 / +0.59 | both halves | 3e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NXT2]] | -0.63 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[EIF4G2]] | -0.60 | -0.33 / -0.57 | both halves | 1e-04 |  |
| [[ATN1]] | -0.60 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[MOB1A]] | -0.60 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[PRKAR1A]] | -0.59 | -0.38 / -0.56 | both halves | 7e-05 |  |
| [[NID1]] | -0.59 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[PDIA3P1]] | -0.59 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[PAPOLA]] | -0.59 | -0.36 / -0.59 | both halves | 9e-05 |  |
| [[CCDC200]] | -0.58 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[STARD4-AS1]] | -0.57 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[TAPBP]] | -0.57 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[TUG1]] | -0.56 | -0.26 / -0.56 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers GTF2H2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PRELID3A]] | C | PRELID3A activity raises GTF2H2's level | lines that do not express PRELID3A (3) vs lines expressing it (47) | 1.85× lower at baseline in the lines without PRELID3A | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SLC4A7, HCN2, USP31 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.642). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-35.9, -9.3); signed map (-19.6, -12.0). **Vector** length 49.5, 6.18% of its response variance represented; |z| ≥ 3 in 805 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.7 | +7.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.6 | +3.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +1.5 | +7.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +1.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +1.3 | +7.9 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.3 | +2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.1 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.7 | -3.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -2.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.7 | +1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | -1.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | +1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.6 | -0.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.0 | -0.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.0 | -1.7 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.0 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | general transcription factor IIH subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.2 — chr5:71,035,016-71,067,689 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BTF2, TFIIH, BTF2P44, T-BTF2P44, p44 |
| Gene groups (HGNC) | Nucleotide excision repair; General transcription factor IIH complex subunits; RING finger E3 ubiquitin protein ligases |
| Reactome | 42 pathways, smallest: RNA Pol II CTD phosphorylation and interaction with CE during HIV infection; RNA Pol II CTD phosphorylation and interaction with CE; mRNA Capping |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13888](https://www.uniprot.org/uniprotkb/Q13888) (General transcription factor IIH subunit 2):

> Component of the general transcription and DNA repair factor IIH (TFIIH) core complex, which is involved in general and transcription-coupled nucleotide excision repair (NER) of damaged DNA and, when complexed to CAK, in RNA transcription by RNA polymerase II. In NER, TFIIH acts by opening DNA around the lesion to allow the excision of the damaged oligonucleotide and its replacement by a new DNA fragment. In transcription, TFIIH has an essential role in transcription initiation. When the …

**Summary**, from NCBI Gene [2966](https://www.ncbi.nlm.nih.gov/gene/2966):

> This gene is part of a 500 kb inverted duplication on chromosome 5q13. This duplicated region contains at least four genes and repetitive elements which make it prone to rearrangements and deletions. The repetitiveness and complexity of the sequence have also caused difficulty in determining the organization of this genomic region. This gene is within the telomeric copy of the duplication. Deletion of this gene sometimes accompanies deletion of the neighboring SMN1 gene in spinal muscular …

**Accessions** — [HGNC:4656](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4656) · Entrez [2966](https://www.ncbi.nlm.nih.gov/gene/2966) · UniProt [Q13888](https://www.uniprot.org/uniprotkb/Q13888) · Ensembl [ENSG00000145736](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145736)

## Data

Gene col 7020: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7020); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7020, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7020]; `tensor/DDL_lfc|DDL_z.npy` [7020]; `embed/gene_vectors.npy` [7020]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7020 or target_col == 7020). Every well: [[GTF2H2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GTF2H2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
