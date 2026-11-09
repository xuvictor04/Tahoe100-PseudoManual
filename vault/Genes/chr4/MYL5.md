---
symbol: "MYL5"
type: "gene"
col: 13260
ensembl_id: "ENSG00000215375"
name: "myosin light chain 5"
location: "4p16.3"
module: 10
arm: "+"
pooled_cpm: 2.02
n_lines_expressing: 49
n_dd_up: 10
n_dd_down: 2
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# MYL5

*myosin light chain 5* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.41× (z +9.0, q 2e-16, up in 6 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.11× (z +7.7, q 3e-12, up in 15 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.569× (z -4.1, q 0.022, down in 17 of 44 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Dexmedetomidine (drug)]] 5 µM in 1 line (A-172 0.0590×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0668×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00240]] (+0.71, fdr 2e-05), [[TIGD6]] (+0.71, fdr 7e-06), [[DEDD]] (+0.71, fdr 7e-06); moves opposite to [[L2HGDH]] (-0.62, fdr 1e-04), [[GGCT]] (-0.59, fdr 4e-05), [[CCDC134]] (-0.59, fdr 4e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ZMAT1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13260.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.41×** | +9.0 | 2e-16 | 6/9 (HEC-1-A, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.11×** | +7.7 | 3e-12 | 15/27 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.05×** | +7.5 | 9e-12 | 3/3 (A498, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.44×** | +6.3 | 5e-08 | 2/2 (A498, NCI-H2347) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.89×** | +4.3 | 0.002 | 10/27 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.74×** | +4.1 | 0.004 | 3/7 (A498, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **2.10×** | +3.9 | 0.008 | 3/21 (MIA PaCa-2, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +3.6 | 0.022 | 5/26 (NCI-H2347, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.59×** | +3.4 | 0.039 | 4/36 (A-427, A-172, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.61×** | +3.3 | 0.046 | 4/27 (Hs 766T, MIA PaCa-2, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 1.34× | +3.0 | 0.12 | 2/43 (SW480, LoVo) | top dose only | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13260.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Dexmedetomidine (drug)]] 5 µM in 1 line (A-172 0.0590×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0668×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.569×** | -4.1 | 0.022 | 17/44 (A-172, Panc 03.27, …) | inconsistent across doses | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.610×** | -3.6 | 0.088 | 11/39 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.654× | -3.1 | 0.37 | 9/39 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13260. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 3.38 | 0 | 1 | — | [[Dexmedetomidine (drug)]] 5 µM 0.0590× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 3.24 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0668× (z -8.5) |
| [[A-427 (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.804 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.802 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.958 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.644 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.629 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.851 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.443 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.999 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.31 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13260), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00240]] | +0.71 | +0.79 / +0.46 | both halves | 2e-05 |  |
| [[TIGD6]] | +0.71 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[DEDD]] | +0.71 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[ZNF747]] | +0.70 | +0.73 / +0.55 | both halves | 1e-05 |  |
| [[LINC01569]] | +0.68 | +0.71 / +0.53 | both halves | 1e-05 |  |
| [[PPP3CB-AS1]] | +0.68 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[BCDIN3D]] | +0.67 | +0.72 / +0.50 | both halves | 1e-05 |  |
| [[RBM26-AS1]] | +0.67 | +0.74 / +0.44 | both halves | 3e-05 |  |
| [[DXO]] | +0.67 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[IDNK]] | +0.67 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[PATL2]] | +0.66 | +0.73 / +0.48 | both halves | 2e-05 |  |
| [[ZNF554]] | +0.66 | +0.73 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[L2HGDH]] | -0.62 | -0.68 / -0.35 | both halves | 1e-04 |  |
| [[GGCT]] | -0.59 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[CCDC134]] | -0.59 | -0.52 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZMAT1]] | B | ZMAT1 activity raises MYL5's level | lines that do not express ZMAT1 (18) vs lines expressing it (32) | 1.29× lower at baseline in the lines without ZMAT1 | 0.030 | ⚠ within organs, on part of the lines; also absent: NTN1, C19orf81, LMX1B |
| [[FRG1-DT]] | B | FRG1-DT activity raises MYL5's level | lines that do not express FRG1-DT (7) vs lines expressing it (43) | 1.32× lower at baseline in the lines without FRG1-DT | 0.057 | ⚠ within organs, on part of the lines; also absent: GALNT16, ENSG00000272438, PRKAR2B; maybe low, not absent |
| [[KDM5D]] | B | KDM5D activity weakens MYL5's drug response | lines that do not express KDM5D (28) vs lines expressing it (16) | the lines without KDM5D respond 1.58× as strongly (z diff -0.50); strongest at Homoharringtonine 5 µM: 2.37x vs 1.00x (z diff -2.8) | 0.063 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P; target measured in part of the lines; artifact flags |
| [[KDM5D]] | B | KDM5D activity raises MYL5's level | lines that do not express KDM5D (30) vs lines expressing it (20) | 1.11× lower at baseline in the lines without KDM5D | 0.090 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P |
| [[DPH6-DT]] | C | DPH6-DT activity raises MYL5's level | lines that do not express DPH6-DT (3) vs lines expressing it (47) | 1.73× lower at baseline in the lines without DPH6-DT | 0.064 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, MYO10, SPDL1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.731). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (3.4, 13.9); signed map (38.9, -7.0). **Vector** length 41.7, 4.96% of its response variance represented; |z| ≥ 3 in 917 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +6.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.1 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +9.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.9 | +4.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.7 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +1.7 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.6 | +2.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.6 | +3.9 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -2.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -1.7 | -3.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | -1.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.5 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.2 | -1.5 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.1 | -0.7 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | -1.0 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | myosin light chain 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.3 — chr4:673,580-682,028 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Myosin light chains, class 2 |
| Reactome | 2 pathways, smallest: Smooth Muscle Contraction; Muscle contraction |
| Matched by | ensembl_id |

UniProt [Q02045](https://www.uniprot.org/uniprotkb/Q02045) carries no function annotation.

**Summary**, from NCBI Gene [4636](https://www.ncbi.nlm.nih.gov/gene/4636):

> This gene encodes one of the myosin light chains, a component of the hexameric ATPase cellular motor protein myosin. Myosin is composed of two heavy chains, two nonphosphorylatable alkali light chains, and two phosphorylatable regulatory light chains. This gene product, one of the regulatory light chains, is expressed in fetal muscle and in adult retina, cerebellum, and basal ganglia. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7586](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7586) · Entrez [4636](https://www.ncbi.nlm.nih.gov/gene/4636) · UniProt [Q02045](https://www.uniprot.org/uniprotkb/Q02045) · Ensembl [ENSG00000215375](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000215375)

## Data

Gene col 13260: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13260); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13260, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13260]; `tensor/DDL_lfc|DDL_z.npy` [13260]; `embed/gene_vectors.npy` [13260]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13260 or target_col == 13260). Every well: [[MYL5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYL5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
