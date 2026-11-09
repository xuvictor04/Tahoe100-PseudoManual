---
symbol: "COX14"
type: "gene"
col: 10930
ensembl_id: "ENSG00000178449"
name: "cytochrome c oxidase assembly factor COX14"
location: "12q13.12"
module: 3
arm: "+"
pooled_cpm: 10.94
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 1
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# COX14

*cytochrome c oxidase assembly factor COX14* — 12q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 2.03× (z +5.6, q 1e-05, up in 31 of 41 measured lines) ⚠ transcription drop. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.67× (z +4.0, q 0.005, up in 28 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.476× (z -5.8, q 4e-06, down in 36 of 47 measured lines) ⚠ unreliable plate only.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (KATO III 0.133×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (SW48 0.0678×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALKBH7]] (+0.80, fdr 7e-06), [[NME3]] (+0.74, fdr 3e-05), [[WDR83OS]] (+0.73, fdr 1e-05, ⚠ WDR83OS in the vector space only through flagged drug-doses), [[LAMTOR2]] (+0.73, fdr 1e-05); moves opposite to [[MAPRE1]] (-0.67, fdr 4e-05), [[PDAP1]] (-0.62, fdr 2e-05), [[ZNF655]] (-0.62, fdr 7e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10930.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.03×** | +5.6 | 1e-05 | 31/41 (KATO III, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **1.88×** | +4.9 | 2e-04 | 21/35 (A-172, SHP-77, …) | two highest doses | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.83×** | +4.7 | 4e-04 | 32/47 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.77×** | +4.5 | 1e-03 | 31/47 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.71×** | +4.2 | 0.003 | 27/47 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.67×** | +4.0 | 0.005 | 28/45 (NCI-H1573, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.78× | +3.1 | 0.14 | 12/41 (NCI-H460, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Arbutin (drug)]] 5 µM |  | 1.51× | +3.1 | 0.14 | 13/45 (PANC-1, NCI-H2030, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | 1.47× | +3.0 | 0.15 | 17/47 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10930.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (KATO III 0.133×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (SW48 0.0678×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.476×** | -5.8 | 4e-06 | 36/47 (A498, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10930. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 20.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.133× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 8.54 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0678× (z -8.5) |
| [[A-172 (line)]] | wt | 8.86 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.04 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.11 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.94 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.90 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.14 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.00 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.87 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.82 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10930), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 8 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALKBH7]] | +0.80 | +0.59 / +0.81 | both halves | 7e-06 |  |
| [[NME3]] | +0.74 | +0.46 / +0.72 | both halves | 3e-05 |  |
| [[WDR83OS]] ⚠ | +0.73 | +0.56 / +0.76 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[LAMTOR2]] | +0.73 | +0.53 / +0.76 | both halves | 1e-05 | STRING 469 |
| [[MALSU1]] | +0.73 | +0.51 / +0.71 | both halves | 1e-05 |  |
| [[LAMTOR5]] | +0.73 | +0.46 / +0.73 | both halves | 2e-05 |  |
| [[C15orf61]] ⚠ | +0.72 | +0.57 / +0.72 | both halves | 9e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[NDUFA2]] | +0.72 | +0.49 / +0.73 | both halves | 1e-05 | pathway: Aerobic respiration and respiratory electron transport; STRING 611 |
| [[MRPL43]] | +0.71 | +0.43 / +0.74 | both halves | 3e-05 |  |
| [[MRPL55]] | +0.71 | +0.47 / +0.74 | both halves | 2e-05 | STRING 480 |
| [[GLRX5]] | +0.71 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[ATP5MJ]] | +0.71 | +0.45 / +0.71 | both halves | 3e-05 | pathway: Aerobic respiration and respiratory electron transport; STRING 435 |
| [[SIVA1]] | +0.70 | +0.48 / +0.70 | both halves | 2e-05 |  |
| [[COX5B]] | +0.70 | +0.44 / +0.72 | both halves | 3e-05 | pathway: Aerobic respiration and respiratory electron transport; STRING 868 |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPRE1]] | -0.67 | -0.42 / -0.70 | both halves | 4e-05 |  |
| [[PDAP1]] | -0.62 | -0.47 / -0.67 | both halves | 2e-05 |  |
| [[ZNF655]] | -0.62 | -0.37 / -0.62 | both halves | 7e-05 |  |
| [[PIEZO1]] | -0.62 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[THOC6]] | -0.61 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[ELK4]] | -0.61 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[KRT8P12]] | -0.61 | -0.56 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers COX14's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[BTBD6]] | B | BTBD6 activity lowers COX14's level | lines that do not express BTBD6 (8) vs lines expressing it (42) | 1.08× higher at baseline in the lines without BTBD6 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000225647, ENSG00000254394, RPL23AP49 |
| [[C19orf53]] | C | C19orf53's natural level weakens COX14's drug response | C19orf53's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.65, reverse +0.27; direction not clear | 0.052 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.670). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-44.8, -20.0); signed map (-35.2, 5.0). **Vector** length 72.2, 16.3% of its response variance represented; |z| ≥ 3 in 550 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +2.5 | +4.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.5 | +4.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +1.9 | +4.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +1.9 | +4.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.8 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +3.1 |
|  | [[Terfenadine (drug)]] 5 µM |  | +1.5 | +1.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.3 | +2.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.3 | +1.8 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.3 | +3.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.8 | -2.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -4.0 | +0.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.0 | -5.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.0 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | -3.1 | +4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -1.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.1 | -1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.0 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome c oxidase assembly factor COX14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.12 — chr12:50,112,082-50,120,457 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC14288; previously C12orf62 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors |
| Reactome | 3 pathways, smallest: Complex IV assembly; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96I36](https://www.uniprot.org/uniprotkb/Q96I36) (Cytochrome c oxidase assembly protein COX14):

> Core component of the MITRAC (mitochondrial translation regulation assembly intermediate of cytochrome c oxidase complex) complex, that regulates cytochrome c oxidase assembly. Requires for coordination of the early steps of cytochrome c oxidase assembly with the synthesis of MT-CO1.

**Summary**, from NCBI Gene [84987](https://www.ncbi.nlm.nih.gov/gene/84987):

> This gene encodes a small single-pass transmembrane protein that localizes to mitochondria. This protein may play a role in coordinating the early steps of cytochrome c oxidase (COX; also known as complex IV) subunit assembly and, in particular, the synthesis and assembly of the COX I subunit of the holoenzyme. Mutations in this gene have been associated with mitochondrial complex IV deficiency. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Nov 2012]

**Accessions** — [HGNC:28216](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28216) · Entrez [84987](https://www.ncbi.nlm.nih.gov/gene/84987) · UniProt [Q96I36](https://www.uniprot.org/uniprotkb/Q96I36) · Ensembl [ENSG00000178449](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178449)

## Data

Gene col 10930: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10930); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10930, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10930]; `tensor/DDL_lfc|DDL_z.npy` [10930]; `embed/gene_vectors.npy` [10930]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10930 or target_col == 10930). Every well: [[COX14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COX14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
