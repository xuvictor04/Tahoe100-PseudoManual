---
symbol: "ANKRD9"
type: "gene"
col: 7973
ensembl_id: "ENSG00000156381"
name: "ankyrin repeat domain 9"
location: "14q32.31"
module: 88
arm: "-"
pooled_cpm: 3.82
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 7
n_dd_up_clean: 3
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# ANKRD9

*ankyrin repeat domain 9* — 14q32.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.62× (z +9.9, q 3e-20, up in 4 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.49× (z +4.5, q 0.001, up in 13 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.364× (z -8.1, q 3e-13, down in 26 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IGSF8]] (+0.70, fdr 8e-06), [[TRIM62]] (+0.70, fdr 1e-05), [[MOSPD3]] (+0.67, fdr 1e-05); moves opposite to [[TRMT13]] (-0.67, fdr 2e-05), [[ST7L]] (-0.67, fdr 8e-06), [[USP40]] (-0.66, fdr 9e-06).
> It sits in the **-** arm of [[Module 088]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MNX1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7973.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.62×** | +9.9 | 3e-20 | 4/4 (NCI-H2030, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.53×** | +7.4 | 4e-11 | 17/23 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.89×** | +4.9 | 2e-04 | 7/22 (HEC-1-A, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +4.5 | 0.001 | 13/37 (A549, PANC-1, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.70×** | +4.2 | 0.003 | 15/43 (SW1417, C-33 A, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.60×** | +3.7 | 0.018 | 11/36 (LS 180, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~12% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.85×** | +3.6 | 0.027 | 2/9 (NCI-H2347, NCI-H2030) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 1.49× | +3.2 | 0.10 | 8/43 (SW480, HOP62, …) | two highest doses | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.90× | +3.1 | 0.10 | 3/29 (LoVo, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.47× | +3.0 | 0.13 | 7/33 (PANC-1, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Bendamustine (drug)]] 5 µM |  | 1.49× | +3.0 | 0.13 | 11/36 (CFPAC-1, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7973.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.364×** | -8.1 | 3e-13 | 26/35 (NCI-H460, LoVo, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.526×** | -7.3 | 1e-10 | 25/34 (SW48, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.518×** | -5.1 | 7e-05 | 19/40 (HCT15, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.369×** | -4.2 | 0.004 | 18/34 (J82, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.601×** | -4.1 | 0.005 | 13/45 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.644×** | -3.5 | 0.039 | 14/42 (NCI-H23, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.652×** | -3.4 | 0.048 | 16/43 (RKO, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | 0.486× | -3.0 | 0.17 | 9/38 (LoVo, J82, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7973. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 5.09 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -9.6) |
| [[HCT15 (line)]] | alt | 9.04 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0360× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 3.59 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0373× (z -13.9) |
| [[SW48 (line)]] | wt | 11.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -10.5) |
| [[C32 (line)]] | wt | 6.57 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -9.7) |
| [[J82 (line)]] | alt | 7.28 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0714× (z -11.1) |
| [[LoVo (line)]] | wt | 6.53 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0896× (z -11.5) |
| [[NCI-H2030 (line)]] | alt | 7.33 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -10.3) |
| [[PANC-1 (line)]] | alt | 1.34 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0457× (z -10.2) |
| [[A-427 (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.36 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.972 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.57 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.43 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7973), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IGSF8]] | +0.70 | +0.58 / +0.64 | both halves | 8e-06 |  |
| [[TRIM62]] | +0.70 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[MOSPD3]] | +0.67 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[CARHSP1]] | +0.66 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[CNOT8]] | +0.66 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[RALGDS]] | +0.65 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[NENF]] | +0.64 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[RAB6A]] | +0.64 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[DOK4]] | +0.63 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[MPST]] | +0.63 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[STK32C]] | +0.63 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[NR2F6]] | +0.62 | +0.51 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRMT13]] | -0.67 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[ST7L]] | -0.67 | -0.58 / -0.59 | both halves | 8e-06 |  |
| [[USP40]] | -0.66 | -0.57 / -0.58 | both halves | 9e-06 |  |
| [[NEK9]] | -0.65 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[ZNF507]] | -0.64 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[TASOR]] | -0.63 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[KICS2]] | -0.62 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[MCTS1]] | -0.61 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[TRIM44]] | -0.61 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[NEPRO-AS1]] | -0.60 | -0.57 / -0.38 | both halves | 6e-05 |  |
| [[DDX6]] | -0.60 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[GTF2H3]] | -0.60 | -0.52 / -0.59 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MNX1]] | B | MNX1 activity raises ANKRD9's level | lines that do not express MNX1 (11) vs lines expressing it (39) | 1.72× lower at baseline in the lines without MNX1 | 0.050 | ⚠ within organs, on part of the lines; also absent: ABLIM2, CAMSAP3, GRTP1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **-** arm (projection on the module's main direction -0.681). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (3.6, -3.9); signed map (-31.5, 17.0). **Vector** length 50.7, 7.46% of its response variance represented; |z| ≥ 3 in 676 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.5 | +4.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +3.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +2.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.0 | +3.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +1.9 | +3.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.7 | +4.2 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.5 | +2.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.4 | +2.3 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.4 | +1.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.1 | -8.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.5 | -3.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.2 | -5.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.7 | -7.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.4 | -4.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -2.0 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.4 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.31 — chr14:102,501,767-102,509,799 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Reactome | 1 pathways, smallest: Neddylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96BM1](https://www.uniprot.org/uniprotkb/Q96BM1) (Ankyrin repeat domain-containing protein 9):

> Substrate receptor subunit of a cullin-RING superfamily E3 ligase complex (CUL5-based E3 ubiquitin ligase complex) which mediates the ubiquitination and subsequent proteasomal degradation of target proteins. Depending of the metabolic state of the cell, promotes the proteasomal degradation of IMPDH2, the rate-limiting enzyme in GTP biosynthesis or protects IMPDH2 by stabilizing IMPDH2 filaments assembly. Implicated in different cellular processes, like copper homeostasis and cell proliferation.

**Summary**, from NCBI Gene [122416](https://www.ncbi.nlm.nih.gov/gene/122416):

> Enables ubiquitin-like ligase-substrate adaptor activity. Involved in intracellular copper ion homeostasis; proteasome-mediated ubiquitin-dependent protein catabolic process; and protein ubiquitination. Located in cytoplasmic vesicle and cytosol. Part of Cul5-RING ubiquitin ligase complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20096](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20096) · Entrez [122416](https://www.ncbi.nlm.nih.gov/gene/122416) · UniProt [Q96BM1](https://www.uniprot.org/uniprotkb/Q96BM1) · Ensembl [ENSG00000156381](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156381)

## Data

Gene col 7973: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7973); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7973, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7973]; `tensor/DDL_lfc|DDL_z.npy` [7973]; `embed/gene_vectors.npy` [7973]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7973 or target_col == 7973). Every well: [[ANKRD9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
