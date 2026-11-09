---
symbol: "STK16"
type: "gene"
col: 3708
ensembl_id: "ENSG00000115661"
name: "serine/threonine kinase 16"
location: "2q35"
module: 12
arm: "+"
pooled_cpm: 8.53
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 5
n_dd_up_clean: 6
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# STK16

*serine/threonine kinase 16* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.80× (z +9.3, q 7e-18, up in 34 of 44 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 2.04× (z +7.6, q 4e-12, up in 34 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.491× (z -7.9, q 1e-12, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNHG11]] (+0.78, fdr 7e-06), [[AMZ2P1-1]] (+0.78, fdr 7e-06), [[PEX12]] (+0.75, fdr 7e-06); moves opposite to [[HACD3]] (-0.64, fdr 1e-05), [[TUFM]] (-0.62, fdr 9e-05), [[FANCA]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[ZNF570]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3708.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.80×** | +9.3 | 7e-18 | 34/44 (SW1417, SW480, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.99×** | +7.7 | 4e-12 | 22/34 (C32, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.04×** | +7.6 | 4e-12 | 34/46 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.89×** | +6.8 | 1e-09 | 11/16 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.50×** | +6.4 | 2e-08 | 26/47 (A-427, LoVo, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.76×** | +6.3 | 2e-08 | 24/41 (Panc 03.27, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.70×** | +5.9 | 2e-07 | 21/43 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.86×** | +4.0 | 0.004 | 9/43 (A498, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.44×** | +3.5 | 0.029 | 7/43 (A-172, HT-29, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.36×** | +3.4 | 0.032 | 9/47 (HS-578T, RKO, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.39×** | +3.4 | 0.032 | 11/26 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.63×** | +3.1 | 0.077 | 8/39 (PANC-1, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3708.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.491×** | -7.9 | 1e-12 | 36/47 (H4, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.556×** | -6.5 | 1e-08 | 30/47 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.558×** | -6.5 | 1e-08 | 34/46 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.612×** | -5.5 | 6e-06 | 24/43 (NCI-H1792, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.678×** | -4.3 | 0.002 | 16/46 (LOX-IMVI, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.898× | -3.8 | 0.012 | 8/48 (LoVo, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3708. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 14.4 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0813× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 9.88 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.34× (z +8.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 6.64 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0739× (z -10.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 10.2 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.287× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 9.78 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0896× (z -10.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 7.30 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.103× (z -8.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 11.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +9.5) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[A-172 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.20 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.26 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.43 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.57 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.04 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.45 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.19 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.87 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.74 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.49 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.17 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.79 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.52 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.96 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3708), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG11]] | +0.78 | +0.83 / +0.71 | both halves | 7e-06 |  |
| [[AMZ2P1-1]] | +0.78 | +0.84 / +0.68 | both halves | 7e-06 |  |
| [[PEX12]] | +0.75 | +0.79 / +0.68 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.74 | +0.77 / +0.70 | both halves | 7e-06 |  |
| [[DXO]] | +0.73 | +0.77 / +0.55 | both halves | 1e-05 |  |
| [[CREB3]] | +0.72 | +0.76 / +0.64 | both halves | 7e-06 |  |
| [[NFKBIL1]] | +0.72 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[WASHC1]] | +0.71 | +0.77 / +0.64 | both halves | 7e-06 |  |
| [[METTL25B]] | +0.71 | +0.76 / +0.62 | both halves | 7e-06 |  |
| [[DNAL4]] | +0.70 | +0.73 / +0.73 | both halves | 7e-06 |  |
| [[C1orf131]] | +0.70 | +0.78 / +0.60 | both halves | 7e-06 |  |
| [[TMEM42]] | +0.70 | +0.74 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HACD3]] | -0.64 | -0.63 / -0.57 | both halves | 1e-05 |  |
| [[TUFM]] | -0.62 | -0.68 / -0.36 | both halves | 9e-05 |  |
| [[FANCA]] | -0.61 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[FAM20B]] | -0.61 | -0.67 / -0.60 | both halves | 7e-06 |  |
| [[CDK2]] | -0.59 | -0.68 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF570]] | C | STK16's natural level weakens ZNF570's drug response | STK16's natural level across 33 lines (lineage-adjusted; a glimpse) | r -0.77, reverse -0.42; direction not clear | 0.082 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.771). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-33.1, 1.7); signed map (5.2, -20.7). **Vector** length 61.8, 10.2% of its response variance represented; |z| ≥ 3 in 740 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +7.5 | +9.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.5 | +7.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.2 | +5.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.6 | +6.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +2.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.8 | +4.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +1.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.3 | +2.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.3 | +3.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -4.3 | -7.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.7 | -5.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.6 | -6.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.1 | -6.5 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.1 | -4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -0.9 | +0.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.9 | -0.4 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -0.9 | -1.5 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.8 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | serine/threonine kinase 16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:219,245,455-219,250,337 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MPSK1, PKL12, MPSK |
| Gene groups (HGNC) | Numb-associated kinase family |
| Matched by | ensembl_id |

**Function**, from UniProt [O75716](https://www.uniprot.org/uniprotkb/O75716) (Serine/threonine-protein kinase 16):

> Membrane-associated protein kinase that phosphorylates on serine and threonine residues. In vitro substrates include DRG1, ENO1 and EIF4EBP1. Also autophosphorylates. May be involved in secretory vesicle trafficking or intracellular signaling. May have a role in regulating stromal-epithelial interactions that occur during ductal morphogenesis in the mammary gland. May be involved in TGF-beta signaling. Able to autophosphorylate on Tyr residue; it is however unclear whether it has …

**Summary**, from NCBI Gene [8576](https://www.ncbi.nlm.nih.gov/gene/8576):

> Predicted to enable protein serine/threonine kinase activity. Involved in protein autophosphorylation. Located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:11394](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11394) · Entrez [8576](https://www.ncbi.nlm.nih.gov/gene/8576) · UniProt [O75716](https://www.uniprot.org/uniprotkb/O75716) · Ensembl [ENSG00000115661](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115661)

## Data

Gene col 3708: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3708); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3708, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3708]; `tensor/DDL_lfc|DDL_z.npy` [3708]; `embed/gene_vectors.npy` [3708]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3708 or target_col == 3708). Every well: [[STK16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STK16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
