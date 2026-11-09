---
symbol: "RNASEH2C"
type: "gene"
col: 10315
ensembl_id: "ENSG00000172922"
name: "ribonuclease H2 subunit C"
location: "11q13.1"
module: 48
arm: "+"
pooled_cpm: 10.74
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 1
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# RNASEH2C

*ribonuclease H2 subunit C* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.03× (z +10.7, q 9e-24, up in 27 of 32 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.37× (z +3.8, q 0.006, up in 16 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.661× (z -4.0, q 0.042, down in 21 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Penfluridol (drug)]] 5 µM in 1 line (C-33 A 0.0795×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARSA]] (+0.67, fdr 1e-05), [[SNRNP25]] (+0.58, fdr 1e-05), [[ZDHHC12]] (+0.57, fdr 1e-05); moves opposite to [[CPSF2]] (-0.49, fdr 6e-05), [[DNAJC2]] (-0.49, fdr 2e-04), [[IDE]] (-0.49, fdr 3e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 14 with an alert ⚠. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10315.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **3.03×** | +10.7 | 9e-24 | 27/32 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **2.61×** | +8.9 | 2e-16 | 19/20 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **2.04×** | +6.9 | 9e-10 | 31/47 (LoVo, HT-29, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.04×** | +6.8 | 9e-10 | 29/42 (SW1417, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **2.04×** | +6.8 | 9e-10 | 35/47 (HT-29, SW1417, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.98×** | +6.3 | 2e-08 | 32/41 (HT-29, SW 900, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **2.04×** | +6.0 | 1e-07 | 23/26 (HS-578T, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.61×** | +4.6 | 4e-04 | 24/47 (HT-29, LoVo, …) | top dose only | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.61×** | +4.4 | 7e-04 | 20/45 (HS-578T, RKO, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.38×** | +4.1 | 0.002 | 19/46 (Hs 766T, A549, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.37×** | +3.8 | 0.006 | 16/48 (J82, A498, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~55% of this change | **1.50×** | +3.8 | 0.008 | 13/38 (HS-578T, NCI-H460, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.36×** | +3.6 | 0.014 | 12/48 (A-427, SW480, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.47×** | +3.6 | 0.014 | 18/45 (NCI-H23, HS-578T, …) | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +3.5 | 0.020 | 16/44 (NCI-H2030, LoVo, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.87×** | +3.5 | 0.020 | 16/41 (SNU-1, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +3.2 | 0.050 | 19/47 (NCI-H460, LoVo, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.37×** | +3.0 | 0.080 | 8/47 (HT-29, SW480, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +2.9 | 0.095 | 11/48 (HS-578T, A-427, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10315.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Penfluridol (drug)]] 5 µM in 1 line (C-33 A 0.0795×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.661×** | -4.0 | 0.042 | 21/45 (SW480, H4, …) | two highest doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.58 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10315. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 11.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.25× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[C-33 A (line)]] | alt | 7.86 | 0 | 1 | — | [[Penfluridol (drug)]] 5 µM 0.0795× (z -8.8) |
| [[A-172 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.13 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.92 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.34 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.84 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.26 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.76 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.49 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.37 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.67 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.72 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.29 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.90 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10315), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARSA]] | +0.67 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[SNRNP25]] | +0.58 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[ZDHHC12]] | +0.57 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[NUDT1]] | +0.56 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[CENPW]] | +0.54 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[DGAT1]] | +0.53 | +0.37 / +0.56 | both halves | 8e-05 |  |
| [[CTXN1]] | +0.53 | +0.44 / +0.31 | both halves | 2e-04 |  |
| [[NPTN]] | +0.52 | +0.43 / +0.36 | both halves | 1e-04 |  |
| [[BLOC1S1]] | +0.51 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[JMJD8]] | +0.50 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[C1QL1]] | +0.50 | +0.30 / +0.52 | both halves | 2e-04 |  |
| [[SKIC2]] | +0.49 | +0.50 / +0.37 | both halves | 8e-05 | STRING 518 |

## Genes that move opposite

*25 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPSF2]] | -0.49 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[DNAJC2]] | -0.49 | -0.55 / -0.32 | both halves | 2e-04 |  |
| [[IDE]] | -0.49 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[USP7]] | -0.49 | -0.40 / -0.37 | both halves | 8e-05 |  |
| [[MTIF2]] | -0.49 | -0.37 / -0.38 | both halves | 8e-05 |  |
| [[CDKL1]] | -0.48 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[DDX21]] | -0.47 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[CCT6P3]] | -0.47 | -0.32 / -0.44 | both halves | 2e-04 |  |
| [[RSL1D1]] | -0.47 | -0.37 / -0.38 | both halves | 8e-05 |  |
| [[NPIPB5]] | -0.47 | -0.16 / -0.61 | ⚠ one half (not replicated) | 0.001 |  |
| [[TCERG1]] | -0.46 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[NOP14]] | -0.46 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[ZFR]] | -0.46 | -0.43 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RNASEH2C's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.394). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-50.3, -14.4); signed map (-37.3, 14.7). **Vector** length 50.4, 8.14% of its response variance represented; |z| ≥ 3 in 647 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +2.0 | +6.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.0 | +3.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +1.9 | +6.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | +1.6 | +4.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.5 | +2.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.3 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +2.7 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +1.1 | -0.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.0 | -4.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -2.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.7 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -1.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -1.6 | +4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.2 | -0.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.2 | -1.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -1.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -1.1 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | ribonuclease H2 subunit C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:65,714,005-65,720,818 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AYP1, AGS3 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TDP1](https://www.uniprot.org/uniprotkb/Q8TDP1) (Ribonuclease H2 subunit C):

> Non catalytic subunit of RNase H2, an endonuclease that specifically degrades the RNA of RNA:DNA hybrids. Participates in DNA replication, possibly by mediating the removal of lagging-strand Okazaki fragment RNA primers during DNA replication. Mediates the excision of single ribonucleotides from DNA:RNA duplexes.

**Summary**, from NCBI Gene [84153](https://www.ncbi.nlm.nih.gov/gene/84153):

> This gene encodes a ribonuclease H subunit that can cleave ribonucleotides from RNA:DNA duplexes. Mutations in this gene cause Aicardi-Goutieres syndrome-3, a disease that causes severe neurologic dysfunction. A pseudogene for this gene has been identified on chromosome Y, near the sex determining region Y (SRY) gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:24116](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24116) · Entrez [84153](https://www.ncbi.nlm.nih.gov/gene/84153) · UniProt [Q8TDP1](https://www.uniprot.org/uniprotkb/Q8TDP1) · Ensembl [ENSG00000172922](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172922)

## Data

Gene col 10315: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10315); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10315, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10315]; `tensor/DDL_lfc|DDL_z.npy` [10315]; `embed/gene_vectors.npy` [10315]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10315 or target_col == 10315). Every well: [[RNASEH2C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNASEH2C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
