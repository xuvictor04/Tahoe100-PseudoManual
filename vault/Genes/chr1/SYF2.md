---
symbol: "SYF2"
type: "gene"
col: 3932
ensembl_id: "ENSG00000117614"
name: "SYF2 pre-mRNA splicing factor"
location: "1p36.11"
module: 74
arm: "+"
pooled_cpm: 78.24
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 1
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# SYF2

*SYF2 pre-mRNA splicing factor* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.53× (z +5.5, q 2e-05, up in 41 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.390× (z -9.1, q 8e-17, down in 48 of 48 measured lines) ⚠ unreliable plate only.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[c-Kit-IN-1 (drug)]] 0.05 µM in 10 lines (AsPC-1 0.242×, HT-29 0.316×, H4 0.201×, PANC-1 0.327×, …; ⚠ unreliable plate only); [[Dinaciclib (drug)]] 5 µM in 1 line (SNU-1 0.178×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CIR1]] (+0.86, fdr 7e-06), [[SLU7]] (+0.81, fdr 7e-06), [[EAPP]] (+0.81, fdr 7e-06); moves opposite to [[NUP188]] (-0.73, fdr 7e-06), [[TFDP1]] (-0.70, fdr 7e-06), [[SIGMAR1]] (-0.70, fdr 7e-06).
> It is in [[Module 074]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HOXA5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3932.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +5.5 | 2e-05 | 41/49 (NCI-H2347, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.42×** | +4.5 | 0.002 | 38/49 (NCI-H23, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **1.55×** | +4.3 | 0.004 | 42/48 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +4.2 | 0.004 | 34/48 (SK-MEL-2, C32, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.35×** | +3.9 | 0.011 | 29/48 (C32, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +3.4 | 0.062 | 29/47 (HEC-1-A, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | 1.84× | +3.1 | 0.16 | 29/48 (LS 180, C-33 A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 1.37× | +3.0 | 0.17 | 25/48 (C32, HS-578T, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3932.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[c-Kit-IN-1 (drug)]] 0.05 µM in 10 lines (AsPC-1 0.242×, HT-29 0.316×, H4 0.201×, PANC-1 0.327×, …; ⚠ unreliable plate only); [[Dinaciclib (drug)]] 5 µM in 1 line (SNU-1 0.178×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.390×** | -9.1 | 8e-17 | 48/48 (AsPC-1, HT-29, …) | all doses, flat |  |
| [[TAK-733 (drug)]] 5 µM |  | 0.527× | -3.2 | 0.36 | 36/48 (COLO 205, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | 0.541× | -3.1 | 0.38 | 33/48 (KATO III, COLO 205, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | 0.550× | -3.0 | 0.38 | 29/48 (SHP-77, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3932. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 76.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.323× (z -8.8) ⚠ unreliable plate only |
| [[AsPC-1 (line)]] | alt | 83.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.242× (z -12.2) ⚠ unreliable plate only |
| [[C32 (line)]] | wt | 61.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +12.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[COLO 205 (line)]] | alt | 115 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.306× (z -8.6) ⚠ unreliable plate only |
| [[H4 (line)]] | wt | 66.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.201× (z -9.9) ⚠ unreliable plate only |
| [[HT-29 (line)]] | alt | 92.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.316× (z -10.7) ⚠ unreliable plate only |
| [[KATO III (line)]] | alt | 90.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.336× (z -8.8) ⚠ unreliable plate only |
| [[LoVo (line)]] | wt | 71.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.313× (z -9.0) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 70.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +11.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H460 (line)]] | wt | 61.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.332× (z -9.0) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 70.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.327× (z -9.7) ⚠ unreliable plate only |
| [[SK-MEL-2 (line)]] | alt | 76.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SNU-1 (line)]] | wt | 96.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.178× (z -11.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 83.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.354× (z -9.2) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 51.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 74.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 65.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 96.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 104 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 53.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 127 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 70.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 92.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 80.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 87.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 72.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 92.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 87.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 63.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 75.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 78.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 79.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 83.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 76.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 69.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 92.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 90.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 66.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 77.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 69.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 92.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 75.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 82.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3932), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIR1]] | +0.86 | +0.82 / +0.87 | both halves | 7e-06 | STRING 626 |
| [[SLU7]] | +0.81 | +0.73 / +0.85 | both halves | 7e-06 | same gene group; pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 995 |
| [[EAPP]] | +0.81 | +0.72 / +0.86 | both halves | 7e-06 |  |
| [[UBXN1]] | +0.76 | +0.72 / +0.81 | both halves | 7e-06 |  |
| [[UBXN7]] | +0.74 | +0.55 / +0.77 | both halves | 1e-05 |  |
| [[RB1CC1]] | +0.73 | +0.62 / +0.75 | both halves | 7e-06 |  |
| [[TERF2IP]] | +0.73 | +0.66 / +0.78 | both halves | 7e-06 |  |
| [[FRG1]] | +0.73 | +0.63 / +0.75 | both halves | 7e-06 | STRING 829 |
| [[GCC2]] | +0.73 | +0.62 / +0.76 | both halves | 7e-06 |  |
| [[TRIM23]] | +0.73 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[MPHOSPH8]] | +0.71 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[WDR83OS]] ⚠ | +0.71 | +0.59 / +0.74 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[CWC15]] | +0.71 | +0.65 / +0.71 | both halves | 7e-06 | same gene group; pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 998 |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP188]] | -0.73 | -0.60 / -0.74 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[TFDP1]] | -0.70 | -0.70 / -0.68 | both halves | 7e-06 |  |
| [[SIGMAR1]] | -0.70 | -0.69 / -0.64 | both halves | 7e-06 |  |
| [[MACROH2A1]] | -0.68 | -0.67 / -0.63 | both halves | 7e-06 |  |
| [[VMA21]] | -0.66 | -0.61 / -0.66 | both halves | 7e-06 |  |
| [[WDR77]] | -0.66 | -0.55 / -0.66 | both halves | 1e-05 |  |
| [[MTHFD1]] | -0.65 | -0.59 / -0.67 | both halves | 7e-06 |  |
| [[ICMT]] | -0.64 | -0.69 / -0.60 | both halves | 7e-06 |  |
| [[VARS1]] | -0.63 | -0.39 / -0.73 | both halves | 6e-05 |  |
| [[LMNB2]] | -0.63 | -0.51 / -0.66 | both halves | 1e-05 |  |
| [[PRKDC]] | -0.62 | -0.59 / -0.63 | both halves | 7e-06 |  |
| [[PAICS]] | -0.62 | -0.56 / -0.65 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXA5]] | B | HOXA5 activity raises SYF2's level | lines that do not express HOXA5 (9) vs lines expressing it (41) | 1.29× lower at baseline in the lines without HOXA5 | 0.094 | ⚠ within organs, on part of the lines; also absent: HOXA3, HOXA6, HOTAIRM1 |
| [[ARID4B]] | C | ARID4B's natural level weakens SYF2's drug response | ARID4B's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.66, reverse +0.33; direction not clear | 0.034 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.846). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-1.5, -45.7); signed map (-13.6, 6.8). **Vector** length 115, 46.2% of its response variance represented; |z| ≥ 3 in 498 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.4 | +4.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +5.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.0 | +3.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.8 | +3.9 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +3.6 | +2.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.4 | +2.3 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | +2.8 | +1.2 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.7 | +1.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -11.5 | -9.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -6.6 | -3.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -6.0 | -3.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -6.0 | -2.4 |
|  | [[venetoclax (drug)]] 5 µM |  | -5.7 | -3.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -5.2 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | SYF2 pre-mRNA splicing factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:25,222,276-25,232,502 (-) |
| Ensembl biotype | protein_coding |
| Also known as | p29, DKFZp564O2082, NTC31, fSAP29; previously CBPIN |
| Gene groups (HGNC) | Spliceosomal C complex; Spliceosomal P complex |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [O95926](https://www.uniprot.org/uniprotkb/O95926) (Pre-mRNA-splicing factor SYF2):

> Involved in pre-mRNA splicing as component of the spliceosome.

**Summary**, from NCBI Gene [25949](https://www.ncbi.nlm.nih.gov/gene/25949):

> This gene encodes a nuclear protein that interacts with cyclin D-type binding-protein 1, which is thought to be a cell cycle regulator at the G1/S transition. Alternate transcriptional splice variants, encoding different isoforms, have been characterized. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:19824](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19824) · Entrez [25949](https://www.ncbi.nlm.nih.gov/gene/25949) · UniProt [O95926](https://www.uniprot.org/uniprotkb/O95926) · Ensembl [ENSG00000117614](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117614)

## Data

Gene col 3932: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3932); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3932, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3932]; `tensor/DDL_lfc|DDL_z.npy` [3932]; `embed/gene_vectors.npy` [3932]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3932 or target_col == 3932). Every well: [[SYF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
