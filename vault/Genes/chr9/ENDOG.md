---
symbol: "ENDOG"
type: "gene"
col: 9425
ensembl_id: "ENSG00000167136"
name: "endonuclease G"
location: "9q34.11"
module: 11
arm: "+"
pooled_cpm: 2.79
n_lines_expressing: 48
n_dd_up: 8
n_dd_down: 7
n_dd_up_clean: 3
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# ENDOG

*endonuclease G* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.43× (z +11.1, q 8e-26, up in 29 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.604× (z -4.5, q 0.004, down in 18 of 30 measured lines).
> Its strongest partners by |cos| (81 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 20 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OXLD1]] (+0.66, fdr 1e-04), [[TMEM187]] (+0.65, fdr 1e-04), [[ACOT2]] (+0.64, fdr 2e-05); moves opposite to [[VAMP7]] (-0.58, fdr 3e-05), [[NDRG3]] (-0.55, fdr 7e-05), [[RPAP3]] (-0.55, fdr 5e-04).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9425.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.43×** | +11.1 | 8e-26 | 29/32 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.51×** | +5.6 | 5e-06 | 1/3 (A498) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.45×** | +5.5 | 8e-06 | 17/27 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **2.10×** | +4.7 | 3e-04 | 3/14 (A498, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.14×** | +4.7 | 4e-04 | 6/16 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **2.05×** | +4.6 | 5e-04 | 13/16 (PANC-1, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.48×** | +3.6 | 0.029 | 9/42 (PANC-1, SNU-423, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +3.3 | 0.059 | 11/30 (NCI-H460, RKO, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.41× | +3.1 | 0.12 | 11/42 (BT-474, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9425.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.604×** | -4.5 | 0.004 | 18/30 (BT-474, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.509×** | -4.3 | 0.006 | 20/41 (HEC-1-A, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.286×** | -4.1 | 0.007 | 17/29 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.549×** | -3.8 | 0.017 | 10/29 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.551×** | -3.8 | 0.017 | 18/40 (SNU-423, HT-29, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.552×** | -3.7 | 0.017 | 10/43 (C-33 A, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **0.375×** | -3.2 | 0.097 | 11/36 (SW1417, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | 0.390× | -3.1 | 0.13 | 11/36 (SW480, SHP-77, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.707× | -3.1 | 0.13 | 16/42 (MIA PaCa-2, HS-578T, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.620× | -3.0 | 0.15 | 14/39 (LS 180, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9425. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 3.95 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.99× (z +8.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.0724× (z -10.1) |
| [[BT-474 (line)]] | alt | 5.39 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -9.1) |
| [[NCI-H661 (line)]] | alt | 1.65 | 0 | 1 | — | [[Uridine (drug)]] 5 µM 0.317× (z -15.2) |
| [[SW480 (line)]] | alt | 2.92 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.72× (z +8.5) | — |
| [[A-172 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.927 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.578 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.86 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.629 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.37 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9425), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 17 of them with an alert (⚠; 16 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OXLD1]] | +0.66 | +0.33 / +0.74 | both halves | 1e-04 |  |
| [[TMEM187]] | +0.65 | +0.35 / +0.71 | both halves | 1e-04 |  |
| [[ACOT2]] | +0.64 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[ABHD15]] | +0.63 | +0.37 / +0.64 | both halves | 8e-05 |  |
| [[LEMD3]] | +0.61 | +0.36 / +0.46 | both halves | 1e-04 |  |
| [[PDCD7]] | +0.60 | +0.37 / +0.73 | both halves | 8e-05 |  |
| [[RBX1]] | +0.60 | +0.37 / +0.70 | both halves | 9e-05 |  |
| [[EMSY-DT]] | +0.60 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[ABHD14A]] | +0.59 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[SMIM27]] | +0.58 | +0.16 / +0.68 | ⚠ one half (not replicated) | 0.001 |  |
| [[INAFM2]] | +0.58 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[ATAD2B]] | +0.58 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[SCGB2B2]] | +0.58 | +0.40 / +0.51 | both halves | 5e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VAMP7]] | -0.58 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[NDRG3]] | -0.55 | -0.38 / -0.55 | both halves | 7e-05 |  |
| [[RPAP3]] | -0.55 | -0.23 / -0.52 | both halves | 5e-04 |  |
| [[MORF4L1]] | -0.54 | -0.37 / -0.62 | both halves | 8e-05 |  |
| [[AGO1]] | -0.54 | -0.20 / -0.63 | both halves | 7e-04 |  |
| [[NBDY]] | -0.54 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[CDA]] | -0.54 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[STARD3NL]] | -0.53 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[PRKCI]] | -0.53 | -0.36 / -0.53 | both halves | 9e-05 |  |
| [[CTC1]] | -0.52 | -0.33 / -0.59 | both halves | 1e-04 |  |
| [[MOCS2]] | -0.52 | -0.19 / -0.52 | ⚠ one half (not replicated) | 8e-04 |  |
| [[DYNC1LI2]] | -0.52 | -0.36 / -0.54 | both halves | 9e-05 |  |
| [[DLD]] | -0.51 | -0.20 / -0.57 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ENDOG's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PAQR7]] | B | PAQR7 activity raises ENDOG's level | lines that do not express PAQR7 (5) vs lines expressing it (45) | 1.27× lower at baseline in the lines without PAQR7 | 0.085 | ⚠ within organs, on part of the lines; also absent: DBN1, VASN, LTBP3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.381). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-3.6, 18.8); signed map (17.8, -6.9). **Vector** length 49.2, 7.30% of its response variance represented; |z| ≥ 3 in 778 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +11.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +5.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.7 | +4.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.3 | +1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.0 | +1.0 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +0.8 | +2.4 |
|  | [[vincristine (drug)]] 0.5 µM |  | +0.8 | +1.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -3.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -2.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | -1.8 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | -1.7 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.7 | +2.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.5 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -2.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.2 | -1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | endonuclease G |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:128,818,500-128,822,676 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14249](https://www.uniprot.org/uniprotkb/Q14249) (Endonuclease G, mitochondrial):

> Endonuclease that preferentially catalyzes the cleavage of double-stranded 5-hydroxymethylcytosine (5hmC)-modified DNA. The 5hmC-modified nucleotide does not increase the binding affinity, but instead increases the efficiency of cutting and specifies the site of cleavage for the modified DNAs (By similarity). Shows significantly higher affinity for four-stranded Holliday junction over duplex and single-stranded DNAs (By similarity). Promotes conservative recombination when the DNA is …

**Summary**, from NCBI Gene [2021](https://www.ncbi.nlm.nih.gov/gene/2021):

> The protein encoded by this gene is a nuclear encoded endonuclease that is localized in the mitochondrion. The encoded protein is widely distributed among animals and cleaves DNA at GC tracts. This protein is capable of generating the RNA primers required by DNA polymerase gamma to initiate replication of mitochondrial DNA. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3346](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3346) · Entrez [2021](https://www.ncbi.nlm.nih.gov/gene/2021) · UniProt [Q14249](https://www.uniprot.org/uniprotkb/Q14249) · Ensembl [ENSG00000167136](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167136)

## Data

Gene col 9425: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9425); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9425, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9425]; `tensor/DDL_lfc|DDL_z.npy` [9425]; `embed/gene_vectors.npy` [9425]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9425 or target_col == 9425). Every well: [[ENDOG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ENDOG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
