---
symbol: "GATD1"
type: "gene"
col: 10804
ensembl_id: "ENSG00000177225"
name: "glutamine amidotransferase class 1 domain containing 1"
location: "11p15.5"
module: 18
arm: "+"
pooled_cpm: 15.19
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 5
n_dd_up_clean: 6
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# GATD1

*glutamine amidotransferase class 1 domain containing 1* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.00× (z +10.0, q 7e-21, up in 26 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.63× (z +7.0, q 2e-10, up in 31 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.834× (z -8.8, q 6e-16, down in 31 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.472× (z -5.6, q 5e-06, down in 24 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPS25]] (+0.63, fdr 1e-05), [[VHL]] (+0.60, fdr 2e-05), [[PRELID3A]] (+0.59, fdr 1e-05); moves opposite to [[MDH1]] (-0.53, fdr 1e-05), [[COPB2]] (-0.48, fdr 4e-05), [[ZNF184]] (-0.47, fdr 3e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ADCY3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10804.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.00×** | +10.0 | 7e-21 | 26/37 (Hs 766T, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.99×** | +9.6 | 4e-19 | 32/41 (NCI-H1573, KATO III, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.96×** | +9.3 | 2e-18 | 22/25 (PANC-1, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.92×** | +8.7 | 4e-16 | 24/29 (SW480, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.63×** | +7.0 | 2e-10 | 31/47 (NCI-H2347, SW480, …) | top dose only | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.47×** | +5.3 | 1e-05 | 20/46 (RKO, NCI-H23, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.22×** | +4.1 | 0.003 | 18/47 (A498, HT-29, …) | rises with dose | low cells (technical?) |
| [[Thymol (drug)]] 0.5 µM |  | **1.31×** | +3.9 | 0.007 | 15/44 (A-172, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +3.7 | 0.011 | 15/47 (NCI-H1792, A498, …) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.41×** | +3.5 | 0.026 | 7/44 (Hs 766T, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.38×** | +3.3 | 0.046 | 9/43 (SW480, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.24×** | +3.1 | 0.078 | 12/47 (LoVo, A498, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | 1.49× | +3.0 | 0.11 | 5/41 (CFPAC-1, A498, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10804.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.834× | -8.8 | 6e-16 | 31/48 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.472×** | -5.6 | 5e-06 | 24/47 (PANC-1, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.781×** | -5.0 | 9e-05 | 23/46 (MIA PaCa-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.545×** | -4.6 | 7e-04 | 19/43 (LOX-IMVI, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.747×** | -4.2 | 0.003 | 17/47 (SK-MEL-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.772×** | -3.7 | 0.020 | 17/47 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.798× | -3.1 | 0.14 | 15/47 (NCI-H23, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10804. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 17.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.05× (z +10.0) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 28.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.180× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 19.4 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.144× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 16.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 11.0 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0993× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 10.5 | 0 | 1 | — | [[Erlotinib (drug)]] 5 µM 0.0892× (z -9.4) |
| [[J82 (line)]] | alt | 30.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.346× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change |
| [[LOX-IMVI (line)]] | wt | 17.5 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0708× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 19.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -11.0) |
| [[NCI-H1792 (line)]] | alt | 7.30 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.05× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 16.2 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.193× (z -9.5) ⚠ cell-cycle shift, explains ~39% of this change |
| [[PANC-1 (line)]] | alt | 33.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.74× (z +10.4) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 19.4 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0751× (z -11.2) |
| [[A-172 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.49 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 19.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10804), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS25]] | +0.63 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[VHL]] | +0.60 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[PRELID3A]] | +0.59 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[CTTN-DT]] | +0.57 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[METTL8]] | +0.56 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[LINC00106]] | +0.55 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[C1orf159]] | +0.55 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[TCFL5]] | +0.55 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[MBD3]] | +0.55 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[MCM3AP-AS1]] | +0.55 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[TANGO6]] | +0.55 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[ITPA]] | +0.54 | +0.53 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MDH1]] | -0.53 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[COPB2]] | -0.48 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[ZNF184]] | -0.47 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[ADD3]] | -0.47 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[SUCO]] | -0.47 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[GBF1]] | -0.47 | -0.46 / -0.39 | both halves | 6e-05 |  |
| [[BTN3A1]] | -0.47 | -0.51 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADCY3]] | B | ADCY3 activity raises GATD1's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.49× lower at baseline in the lines without ADCY3 | 0.025 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[ZP3]] | B | ZP3 activity raises GATD1's level | lines that do not express ZP3 (11) vs lines expressing it (39) | 1.38× lower at baseline in the lines without ZP3 | 0.083 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[NCS1]] | B | NCS1 activity raises GATD1's level | lines that do not express NCS1 (6) vs lines expressing it (44) | 1.42× lower at baseline in the lines without NCS1 | 0.094 | ⚠ within organs, on part of the lines; also absent: SH3BP5, ZNF618, PBK; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.567). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-12.7, -29.5); signed map (6.3, -53.9). **Vector** length 74.8, 13.3% of its response variance represented; |z| ≥ 3 in 844 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.2 | +9.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.0 | +3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +7.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +5.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.1 | +3.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.1 | +1.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.7 | -5.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.2 | -5.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -0.9 |
|  | [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | -2.2 | -1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.6 | -1.8 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -1.6 | -0.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.5 | -2.4 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | -1.4 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | glutamine amidotransferase class 1 domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:767,220-777,488 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ34283, Fy-5, FERRY5; previously PDDC1 |
| Gene groups (HGNC) | Glutamine amidotransferase class 1 domain containing; FERRY complex subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NB37](https://www.uniprot.org/uniprotkb/Q8NB37) (Glutamine amidotransferase-like class 1 domain-containing protein 1):

> Component of the FERRY complex (Five-subunit Endosomal Rab5 and RNA/ribosome intermediary). The FERRY complex directly interacts with mRNAs and RAB5A, and functions as a RAB5A effector involved in the localization and the distribution of specific mRNAs most likely by mediating their endosomal transport. The complex recruits mRNAs and ribosomes to early endosomes through direct mRNA-interaction.

**Summary**, from NCBI Gene [347862](https://www.ncbi.nlm.nih.gov/gene/347862):

> Predicted to enable glyoxalase III activity. Predicted to be involved in obsolete methylglyoxal catabolic process to pyruvate via (R)-S-lactoyl-glutathione. Located in extracellular exosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26616](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26616) · Entrez [347862](https://www.ncbi.nlm.nih.gov/gene/347862) · UniProt [Q8NB37](https://www.uniprot.org/uniprotkb/Q8NB37) · Ensembl [ENSG00000177225](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177225)

## Data

Gene col 10804: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10804); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10804, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10804]; `tensor/DDL_lfc|DDL_z.npy` [10804]; `embed/gene_vectors.npy` [10804]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10804 or target_col == 10804). Every well: [[GATD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GATD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
