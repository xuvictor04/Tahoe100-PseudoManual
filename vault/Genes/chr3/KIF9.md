---
symbol: "KIF9"
type: "gene"
col: 1540
ensembl_id: "ENSG00000088727"
name: "kinesin family member 9"
location: "3p21.31"
module: 205
arm: "+"
pooled_cpm: 12.64
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 5
n_dd_up_clean: 4
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/205"]
generated_by: "tahoemap"
---

# KIF9

*kinesin family member 9* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.36× (z +12.7, q 2e-34, up in 34 of 35 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.21× (z +9.7, q 4e-20, up in 35 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.667× (z -4.9, q 5e-04, down in 30 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC40]] (+0.72, fdr 7e-06), [[CCDC157]] (+0.71, fdr 7e-06), [[CFAP210]] (+0.70, fdr 7e-06); moves opposite to [[EXO5-DT]] (-0.46, fdr 1e-04), [[NRBP1]] (-0.45, fdr 4e-05), [[CGRRF1]] (-0.44, fdr 1e-04).
> It is in [[Module 205]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CCDC120]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1540.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **4.36×** | +12.7 | 2e-34 | 34/35 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.80×** | +12.4 | 9e-33 | 20/21 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.21×** | +9.7 | 4e-20 | 35/43 (NCI-H1792, A549, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.33×** | +9.6 | 9e-20 | 27/28 (HEC-1-A, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.69×** | +6.4 | 2e-08 | 26/43 (Hs 766T, NCI-H2030, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.75×** | +4.8 | 1e-04 | 26/47 (HOP62, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.83×** | +4.8 | 1e-04 | 22/37 (NCI-H2030, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.70×** | +4.6 | 3e-04 | 21/47 (A-172, NCI-H460, …) | top dose only | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.19×** | +3.5 | 0.025 | 9/19 (HEC-1-A, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.33×** | +3.5 | 0.027 | 19/47 (NCI-H1573, A-172, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.57×** | +3.3 | 0.049 | 15/46 (HOP62, SNU-423, …) | two highest doses |  |
| [[Arbutin (drug)]] 5 µM |  | **1.51×** | +3.3 | 0.050 | 17/45 (NCI-H1573, SW480, …) | top dose only | position effect removed |
| [[Cyclosporin A (drug)]] 0.05 µM |  | **1.44×** | +3.2 | 0.069 | 11/47 (PANC-1, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1540.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.667×** | -4.9 | 5e-04 | 30/47 (SHP-77, SW1417, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.651×** | -3.7 | 0.056 | 21/44 (COLO 205, HS-578T, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Vortioxetine (drug)]] 0.5 µM |  | **0.608×** | -3.6 | 0.056 | 22/47 (HepG2/C3A, NCI-H2030, …) | inconsistent across doses |  |
| [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM |  | **0.626×** | -3.4 | 0.075 | 13/47 (SNU-423, NCI-H2347, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.626×** | -3.4 | 0.075 | 14/47 (HEC-1-A, CFPAC-1, …) | inconsistent across doses |  |
| [[LB-100 (drug)]] 0.05 µM |  | 0.671× | -3.2 | 0.12 | 11/48 (HOP62, SHP-77, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1540. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 19.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 20.4× (z +12.9) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 13.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.87× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SW 900 (line)]] | alt | 8.32 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 15.4× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[C-33 A (line)]] | alt | 13.8 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0627× (z -10.3) |
| [[KATO III (line)]] | alt | 22.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.83× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 7.15 | 0 | 1 | — | [[Cepharanthine (drug)]] 5 µM 0.193× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 7.03 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.1× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H2030 (line)]] | alt | 9.28 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.71× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[RKO (line)]] | wt | 13.9 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0491× (z -10.9) |
| [[RPMI-7951 (line)]] | alt | 16.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.99× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 4.86 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.24 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.26 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.64 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.84 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.13 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.98 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.48 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.22 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.89 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 27.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1540), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC40]] | +0.72 | +0.62 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[CCDC157]] | +0.71 | +0.75 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[CFAP210]] | +0.70 | +0.77 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[FOSB]] | +0.67 | +0.72 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[RNF213-AS1]] | +0.67 | +0.63 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[RRP12]] | +0.61 | +0.64 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[DRC3]] | +0.60 | +0.55 / +0.56 | both halves | 1e-05 | STRING 482 |
| [[FOS]] | +0.57 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[ANKRD42]] | +0.55 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[PRKCG]] | +0.54 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[MOK]] | +0.53 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[CFAP69]] | +0.52 | +0.41 / +0.57 | both halves | 4e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXO5-DT]] | -0.46 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[NRBP1]] | -0.45 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[CGRRF1]] | -0.44 | -0.32 / -0.48 | both halves | 1e-04 |  |
| [[UBA3]] | -0.42 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[TRIP4]] | -0.41 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[MFSD9]] | -0.41 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[FXR2]] | -0.40 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[GIPC1]] | -0.40 | -0.32 / -0.49 | both halves | 1e-04 |  |
| [[BLVRA]] | -0.40 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[CCDC120]] | -0.39 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[TRIM11]] | -0.39 | -0.31 / -0.40 | both halves | 2e-04 |  |
| [[YTHDF1]] | -0.39 | -0.29 / -0.44 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC120]] | B | CCDC120 activity raises KIF9's level | lines that do not express CCDC120 (11) vs lines expressing it (39) | 1.45× lower at baseline in the lines without CCDC120 | 0.022 | ⚠ within organs, on part of the lines; also absent: PARD6B, LMTK3, AP1G2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 205]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.738). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.5, -28.2); signed map (-1.5, 7.6). **Vector** length 93.2, 23.0% of its response variance represented; |z| ≥ 3 in 714 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.4 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +6.9 | +12.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +12.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +9.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.4 | +4.8 |
|  | [[Arbutin (drug)]] 5 µM |  | +2.2 | +3.3 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +2.2 | +1.5 |
|  | [[Sulfatinib (drug)]] 5 µM |  | +2.1 | +3.0 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +2.0 | +2.6 |
|  | [[Lactate (calcium) (drug)]] 0.05 µM |  | +2.0 | +0.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.8 | -4.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.7 | -3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.6 | -1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -1.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | +0.4 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -2.7 | -3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.7 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | kinesin family member 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:47,227,998-47,283,451 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC104186 |
| Gene groups (HGNC) | Kinesins; Centriolar satellite proteins |
| Reactome | 8 pathways, smallest: Kinesins; COPI-dependent Golgi-to-ER retrograde traffic; Golgi-to-ER retrograde transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HAQ2](https://www.uniprot.org/uniprotkb/Q9HAQ2) (Kinesin-like protein KIF9):

> Essential for normal male fertility and for progressive motility of spermatozoa.

**Summary**, from NCBI Gene [64147](https://www.ncbi.nlm.nih.gov/gene/64147):

> Enables identical protein binding activity. Involved in extracellular matrix disassembly; organelle disassembly; and regulation of podosome assembly. Located in microtubule; podosome; and vesicle. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16666](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16666) · Entrez [64147](https://www.ncbi.nlm.nih.gov/gene/64147) · UniProt [Q9HAQ2](https://www.uniprot.org/uniprotkb/Q9HAQ2) · Ensembl [ENSG00000088727](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000088727)

## Data

Gene col 1540: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1540); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1540, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1540]; `tensor/DDL_lfc|DDL_z.npy` [1540]; `embed/gene_vectors.npy` [1540]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1540 or target_col == 1540). Every well: [[KIF9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIF9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
