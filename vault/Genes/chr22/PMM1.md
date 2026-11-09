---
symbol: "PMM1"
type: "gene"
col: 1956
ensembl_id: "ENSG00000100417"
name: "phosphomannomutase 1"
location: "22q13.2"
module: 3
arm: "+"
pooled_cpm: 13.71
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 10
n_dd_up_clean: 6
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# PMM1

*phosphomannomutase 1* — 22q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.59× (z +9.0, q 9e-17, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.492× (z -6.7, q 1e-08, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INAFM1]] (+0.75, fdr 7e-06), [[TULP3]] (+0.73, fdr 1e-05), [[GOLGA2]] (+0.73, fdr 7e-06); moves opposite to [[VMA21]] (-0.74, fdr 7e-06), [[PTGR2]] (-0.66, fdr 8e-06), [[TMEM33]] (-0.66, fdr 7e-06).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[APPAT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1956.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.59×** | +9.0 | 9e-17 | 43/48 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.19×** | +7.5 | 2e-11 | 39/48 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.01×** | +6.6 | 6e-09 | 36/48 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +6.3 | 6e-08 | 29/45 (SW480, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.57×** | +4.3 | 0.002 | 25/44 (NCI-H23, A-427, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.90×** | +3.5 | 0.037 | 13/45 (LS 180, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **1.41×** | +3.3 | 0.092 | 16/44 (CFPAC-1, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.78× | +3.2 | 0.10 | 14/43 (SHP-77, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1956.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.492×** | -6.7 | 1e-08 | 36/47 (HOP62, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.547×** | -5.7 | 3e-06 | 29/48 (AsPC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.253×** | -5.6 | 3e-06 | 34/44 (C32, Hs 766T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.255×** | -5.6 | 3e-06 | 35/47 (HOP62, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.566×** | -5.4 | 8e-06 | 27/46 (HOP62, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.649×** | -4.1 | 0.004 | 24/44 (SW 900, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.663×** | -3.9 | 0.008 | 24/46 (HOP62, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.676×** | -3.7 | 0.016 | 22/48 (A498, HT-29, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.663×** | -3.7 | 0.016 | 20/46 (HEC-1-A, SW480, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.699×** | -3.4 | 0.041 | 18/46 (hTERT-HPNE, HOP62, …) | rises with dose | cell-cycle shift (explains ~9% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1956. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 26.2 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.169× (z -12.7) |
| [[SK-MEL-2 (line)]] | alt | 52.4 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.57× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.263× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 8.90 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.40× (z +9.6) | — |
| [[KATO III (line)]] | alt | 15.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.146× (z -8.9) |
| [[PANC-1 (line)]] | alt | 12.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 8.87 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0836× (z -9.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.89 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.83 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.81 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.65 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.86 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.90 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.39 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1956), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INAFM1]] | +0.75 | +0.59 / +0.79 | both halves | 7e-06 |  |
| [[TULP3]] | +0.73 | +0.54 / +0.76 | both halves | 1e-05 |  |
| [[GOLGA2]] | +0.73 | +0.71 / +0.69 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[MRPL55]] | +0.70 | +0.39 / +0.77 | both halves | 5e-05 |  |
| [[ZFAND2B]] | +0.70 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[RNF181]] | +0.69 | +0.46 / +0.75 | both halves | 3e-05 |  |
| [[ING2]] | +0.69 | +0.57 / +0.75 | both halves | 1e-05 |  |
| [[RAB40C]] | +0.69 | +0.41 / +0.71 | both halves | 4e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[LIN7B]] | +0.69 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[CARD19]] | +0.68 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[MIGA2]] | +0.68 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[LCMT1]] | +0.68 | +0.43 / +0.61 | both halves | 3e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VMA21]] | -0.74 | -0.72 / -0.78 | both halves | 7e-06 |  |
| [[PTGR2]] | -0.66 | -0.62 / -0.58 | both halves | 8e-06 |  |
| [[TMEM33]] | -0.66 | -0.66 / -0.70 | both halves | 7e-06 |  |
| [[EWSR1]] | -0.65 | -0.29 / -0.74 | both halves | 3e-04 |  |
| [[SRSF1]] | -0.65 | -0.38 / -0.65 | both halves | 7e-05 |  |
| [[BTBD1]] | -0.64 | -0.50 / -0.66 | both halves | 1e-05 |  |
| [[DARS2]] | -0.64 | -0.43 / -0.63 | both halves | 3e-05 |  |
| [[ATIC]] | -0.63 | -0.57 / -0.69 | both halves | 9e-06 |  |
| [[MRPL42]] | -0.63 | -0.59 / -0.77 | both halves | 7e-06 |  |
| [[WDR77]] | -0.62 | -0.61 / -0.63 | both halves | 7e-06 |  |
| [[HNRNPA3]] | -0.62 | -0.54 / -0.66 | both halves | 1e-05 |  |
| [[ZC3HAV1L]] | -0.62 | -0.55 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APPAT]] | B | APPAT activity lowers PMM1's level | lines that do not express APPAT (7) vs lines expressing it (43) | 1.73× higher at baseline in the lines without APPAT | 0.062 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers PMM1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.758). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-29.6, -29.0); signed map (-25.6, 12.1). **Vector** length 89.6, 22.6% of its response variance represented; |z| ≥ 3 in 730 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +3.3 | +9.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.2 | +7.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.1 | +6.6 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +2.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.4 | +3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +3.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.0 | +0.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.8 | +3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.5 | +0.6 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.4 | -2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.7 | -3.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.2 | -0.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.1 | +1.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.1 | -3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -2.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.4 | -3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | -5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | phosphomannomutase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.2 — chr22:41,576,900-41,589,871 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Sec53 |
| Gene groups (HGNC) | HAD Asp-based non-protein phosphatases |
| Hallmark sets | XENOBIOTIC_METABOLISM, P53_PATHWAY |
| Reactome | 4 pathways, smallest: Synthesis of GDP-mannose; Synthesis of substrates in N-glycan biosythesis; Biosynthesis of the N-glycan precursor (dolichol lipid-linked oligosaccharide, LLO) and transfer to a nascent protein |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92871](https://www.uniprot.org/uniprotkb/Q92871) (Phosphomannomutase 1):

> Involved in the synthesis of the GDP-mannose and dolichol-phosphate-mannose required for a number of critical mannosyl transfer reactions. In addition, may be responsible for the degradation of glucose-1,6-bisphosphate in ischemic brain.

**Summary**, from NCBI Gene [5372](https://www.ncbi.nlm.nih.gov/gene/5372):

> Phosphomannomutase catalyzes the conversion between D-mannose 6-phosphate and D-mannose 1-phosphate which is a substrate for GDP-mannose synthesis. GDP-mannose is used for synthesis of dolichol-phosphate-mannose, which is essential for N-linked glycosylation and thus the secretion of several glycoproteins as well as for the synthesis of glycosyl-phosphatidyl-inositol (GPI) anchored proteins. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9114](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9114) · Entrez [5372](https://www.ncbi.nlm.nih.gov/gene/5372) · UniProt [Q92871](https://www.uniprot.org/uniprotkb/Q92871) · Ensembl [ENSG00000100417](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100417)

## Data

Gene col 1956: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1956); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1956, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1956]; `tensor/DDL_lfc|DDL_z.npy` [1956]; `embed/gene_vectors.npy` [1956]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1956 or target_col == 1956). Every well: [[PMM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PMM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
