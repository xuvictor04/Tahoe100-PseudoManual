---
symbol: "C2orf74-DT"
type: "gene"
col: 13072
ensembl_id: "ENSG00000212978"
name: "C2orf74 antisense RNA 1"
location: "2p15"
module: 16
arm: "+"
pooled_cpm: 3.13
n_lines_expressing: 35
n_dd_up: 5
n_dd_down: 16
n_dd_up_clean: 4
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# C2orf74-DT

*C2orf74 antisense RNA 1* — 2p15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.61× (z +5.7, q 8e-06, up in 7 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.369× (z -8.3, q 4e-14, down in 23 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C2orf74]] (+0.68, fdr 7e-06, ⚠ same locus), [[ZNF287]] (+0.61, fdr 1e-05), [[ZMAT1]] (+0.60, fdr 1e-05), [[TTC30A]] (+0.58, fdr 9e-06); moves opposite to [[TMEM181]] (-0.59, fdr 1e-05), [[BDH1]] (-0.58, fdr 1e-05), [[GPC4]] (-0.50, fdr 3e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[BOLA3-DT]] → it (grade B ⚠); 1 goes from it, the strongest it → [[C2orf74]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13072.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.61×** | +5.7 | 8e-06 | 7/31 (A-172, BT-474, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.61×** | +4.0 | 0.015 | 8/31 (A498, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.60×** | +3.9 | 0.015 | 6/15 (PANC-1, SNU-423, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Bendamustine (drug)]] 5 µM |  | **1.60×** | +3.8 | 0.019 | 8/23 (HEC-1-A, A-427, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.53×** | +3.5 | 0.044 | 10/29 (A-172, PANC-1, …) | two highest doses | position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | 1.46× | +3.2 | 0.13 | 4/32 (MIA PaCa-2, A-427, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 1.29× | +3.1 | 0.16 | 4/31 (A498, MIA PaCa-2, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.44× | +3.0 | 0.16 | 5/32 (C32, H4, …) | two highest doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13072.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.369×** | -8.3 | 4e-14 | 23/30 (SHP-77, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.435×** | -7.0 | 7e-10 | 24/32 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.436×** | -6.9 | 7e-10 | 18/32 (PANC-1, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.482×** | -6.1 | 1e-07 | 14/24 (SNU-423, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.608×** | -5.9 | 5e-07 | 16/24 (RPMI-7951, A549, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.510×** | -5.6 | 2e-06 | 15/29 (PANC-1, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.279×** | -5.6 | 2e-06 | 14/29 (A498, SHP-77, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.350×** | -4.6 | 3e-04 | 12/25 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.582×** | -4.3 | 0.001 | 14/29 (PANC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.634×** | -3.8 | 0.008 | 8/30 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.732×** | -3.7 | 0.012 | 13/25 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[EX229 (drug)]] 5 µM |  | **0.454×** | -3.5 | 0.026 | 9/19 (A-427, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.667×** | -3.4 | 0.032 | 9/32 (SK-MEL-2, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.686×** | -3.1 | 0.066 | 9/32 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.687×** | -3.1 | 0.066 | 7/26 (BT-474, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Pimozide (drug)]] 5 µM |  | **0.695×** | -3.0 | 0.085 | 7/32 (C32, J82, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13072. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 3.86 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0917× (z -9.9) |
| [[PANC-1 (line)]] | alt | 6.15 | 0 | 2 | — | [[Bortezomib (drug)]] 0.05 µM 0.132× (z -9.4) |
| [[A-172 (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.65 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.94 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.409 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.260 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.202 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.20 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.258 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.253 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.218 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.204 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.00 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.207 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.233 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.668 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.233 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.230 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.197 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.231 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.203 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13072), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C2orf74]] | +0.68 | +0.71 / +0.63 | both halves | 7e-06 | ⚠ same locus (0.1 kb: neighbours can correlate without regulation) |
| [[ZNF287]] | +0.61 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[ZMAT1]] | +0.60 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[TTC30A]] | +0.58 | +0.57 / +0.57 | both halves | 9e-06 |  |
| [[ID3]] | +0.58 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[DUSP19]] | +0.56 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[ASF1A]] | +0.56 | +0.41 / +0.68 | both halves | 4e-05 |  |
| [[GSPT2]] | +0.56 | +0.42 / +0.73 | both halves | 4e-05 |  |
| [[LINC02211]] | +0.55 | +0.58 / +0.46 | both halves | 2e-05 |  |
| [[PABIR1]] | +0.55 | +0.38 / +0.64 | both halves | 6e-05 |  |
| [[MIR3171HG]] | +0.55 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[CCDC102B]] | +0.53 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[CEP19]] | +0.53 | +0.43 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM181]] | -0.59 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[BDH1]] | -0.58 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[GPC4]] | -0.50 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[SFXN2]] | -0.49 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[PRR5-ARHGAP8]] | -0.47 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[CALML4]] | -0.46 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[TMPRSS5]] | -0.46 | -0.30 / -0.47 | both halves | 2e-04 |  |
| [[ELMO3]] | -0.46 | -0.51 / -0.30 | both halves | 2e-04 |  |
| [[SNRPA]] | -0.45 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[TSPAN3]] | -0.45 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[SCLY]] | -0.45 | -0.27 / -0.43 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BOLA3-DT]] | B | BOLA3-DT activity raises C2orf74-DT's level | lines that do not express BOLA3-DT (10) vs lines expressing it (40) | 2.23× lower at baseline in the lines without BOLA3-DT | 0.051 | ⚠ within organs, on part of the lines; also absent: GIHCG, KATNAL1, LIX1L |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C2orf74]] | C | C2orf74-DT activity raises C2orf74's level | lines that do not express C2orf74-DT (15) vs lines expressing it (35) | 4.72× lower at baseline in the lines without C2orf74-DT | 0.060 | ⚠ within organs, on part of the lines; also absent: C2orf74, NR3C1, FIGN; co-absent with the target; its own permutation p |

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.529). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-8.8, 40.5); signed map (-3.5, -30.3). **Vector** length 42.3, 6.56% of its response variance represented; |z| ≥ 3 in 653 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +2.6 | +5.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +1.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | +0.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.6 | +3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.0 | -0.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.0 | +2.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +0.9 | +4.0 |
|  | [[Docetaxel (drug)]] 5 µM |  | +0.9 | +1.7 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -1.6 | -6.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.4 | -3.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -1.3 | -5.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -1.3 | -4.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.3 | -8.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.8 | -2.0 |
|  | [[EX229 (drug)]] 5 µM |  | -0.8 | -3.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -0.8 | -2.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -0.7 | -1.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.7 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | C2orf74 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2p15 — chr2:61,141,592-61,144,969 (-) |
| Ensembl biotype | lncRNA |
| Also known as | AC016747.2; previously C2orf74-DT |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | prev_symbol |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:56377](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:56377) · Entrez [105374758](https://www.ncbi.nlm.nih.gov/gene/105374758) · Ensembl [ENSG00000212978](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000212978)

## Data

Gene col 13072: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13072); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13072, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13072]; `tensor/DDL_lfc|DDL_z.npy` [13072]; `embed/gene_vectors.npy` [13072]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13072 or target_col == 13072). Every well: [[C2orf74-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C2orf74-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
