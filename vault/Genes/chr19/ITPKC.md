---
symbol: "ITPKC"
type: "gene"
col: 1462
ensembl_id: "ENSG00000086544"
name: "inositol-trisphosphate 3-kinase C"
location: "19q13.2"
module: 31
arm: "+"
pooled_cpm: 54.67
n_lines_expressing: 48
n_dd_up: 10
n_dd_down: 24
n_dd_up_clean: 9
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 33
direction_downstream: 0
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# ITPKC

*inositol-trisphosphate 3-kinase C* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.60× (z +10.0, q 7e-21, up in 26 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.472× (z -11.3, q 5e-27, down in 37 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COQ8B]] (+0.70, fdr 7e-06, ⚠ same locus), [[PLK3]] (+0.63, fdr 7e-06), [[TICAM1]] (+0.63, fdr 1e-05), [[C6orf132]] (+0.61, fdr 7e-06); moves opposite to [[COPS7B]] (-0.46, fdr 2e-04), [[ANKRD52]] (-0.46, fdr 5e-05), [[PPT1]] (-0.44, fdr 6e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 33 arrows point to it, the strongest [[TMPRSS4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1462.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.60×** | +10.0 | 7e-21 | 26/45 (A498, AsPC-1, …) | top dose only | cell-cycle shift (explains ~5% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.39×** | +9.6 | 1e-19 | 32/47 (NCI-H1573, A549, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.93×** | +9.6 | 2e-19 | 29/45 (A549, HS-578T, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.47×** | +5.5 | 5e-06 | 18/45 (A498, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.86×** | +4.9 | 1e-04 | 21/43 (HS-578T, BT-474, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +4.1 | 0.004 | 21/46 (C-33 A, C32, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.31×** | +4.1 | 0.004 | 16/45 (C32, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.31×** | +4.0 | 0.004 | 16/44 (BT-474, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.29×** | +3.9 | 0.006 | 17/46 (A549, SNU-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.59×** | +3.7 | 0.013 | 16/44 (HEC-1-A, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1462.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.472×** | -11.3 | 5e-27 | 37/46 (SW48, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.525×** | -9.8 | 5e-20 | 29/42 (HT-29, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.532×** | -9.5 | 3e-19 | 33/46 (HT-29, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.527×** | -9.3 | 2e-18 | 24/35 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.574×** | -8.4 | 6e-15 | 27/45 (SW48, HT-29, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[NG25 (drug)]] 5 µM |  | **0.400×** | -7.2 | 4e-11 | 29/43 (SW48, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.731×** | -6.7 | 2e-09 | 27/46 (SW48, NCI-H1573, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.662×** | -6.2 | 3e-08 | 25/46 (HT-29, MIA PaCa-2, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **0.788×** | -5.1 | 2e-05 | 25/46 (LoVo, Panc 03.27, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.924× | -4.5 | 4e-04 | 6/47 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.746×** | -4.3 | 0.001 | 17/44 (SNU-423, A-427, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM |  | **0.820×** | -4.2 | 0.001 | 18/46 (C32, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.750×** | -4.2 | 0.001 | 19/45 (SW48, NCI-H1573, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.752×** | -4.1 | 0.001 | 22/44 (SW48, HT-29, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.744×** | -4.1 | 0.001 | 16/45 (SW48, LoVo, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.761×** | -4.1 | 0.001 | 22/45 (SW48, HT-29, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.763×** | -4.1 | 0.002 | 17/45 (LoVo, NCI-H1573, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.599×** | -4.1 | 0.002 | 22/47 (HT-29, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1462. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 370 | 0 | 16 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.114× (z -17.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.156× (z -14.9) |
| [[HT-29 (line)]] | alt | 418 | 0 | 12 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0318× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0573× (z -14.8) |
| [[A549 (line)]] | wt | 42.7 | 4 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 5.54× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.293× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 114 | 1 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.32× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.0883× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.290× (z -12.9) |
| [[Panc 03.27 (line)]] | alt | 115 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.196× (z -11.3) |
| [[HEC-1-A (line)]] | alt | 70.3 | 1 (1 ⚠) | 2 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.98× (z +8.8) ⚠ toxic; cell-cycle shift, explains ~18% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.323× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 63.2 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.307× (z -9.8) |
| [[SW1417 (line)]] | alt | 90.7 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.214× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.252× (z -9.5) |
| [[A-172 (line)]] | wt | 25.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.133× (z -14.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 21.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +13.8) | — |
| [[AsPC-1 (line)]] | alt | 55.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +12.0) | [[Panobinostat (drug)]] 5 µM 0.271× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 15.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +9.1) | [[5-Azacytidine (drug)]] 0.05 µM 0.139× (z -8.7) |
| [[LoVo (line)]] | wt | 62.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.296× (z -8.5) |
| [[A-427 (line)]] | wt | 45.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.229× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change |
| [[CFPAC-1 (line)]] | alt | 108 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.254× (z -8.9) |
| [[COLO 205 (line)]] | alt | 124 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0831× (z -9.0) |
| [[Hs 766T (line)]] | wt | 36.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.101× (z -13.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 33.8 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 3.35× (z +9.4) | — |
| [[hTERT-HPNE (line)]] | wt | 19.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.162× (z -9.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 45.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.126× (z -13.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 22.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 70.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 84.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.8 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 46.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1462), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COQ8B]] | +0.70 | +0.70 / +0.66 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[PLK3]] | +0.63 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[TICAM1]] | +0.63 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[C6orf132]] | +0.61 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[RDH13]] | +0.58 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[SLC52A3]] | +0.56 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[BCL2L1-AS1]] | +0.56 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[SGPP2]] | +0.55 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[EPHA2-AS1]] | +0.54 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[EPS8L1]] | +0.54 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[EFNB2]] | +0.54 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[ABHD11]] | +0.53 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[SH2D3A]] | +0.53 | +0.50 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPS7B]] | -0.46 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[ANKRD52]] | -0.46 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[PPT1]] | -0.44 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[WHAMMP1]] | -0.44 | -0.37 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*33 arrows, 33 of them with an alert ⚠; grade A 0, B 32, C 1. Shown: the 12 strongest; 21 more arrows (21 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMPRSS4]] | B | TMPRSS4 activity raises ITPKC's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 3.77× lower at baseline in the lines without TMPRSS4 | 6e-05 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[GJB3]] | B | GJB3 activity raises ITPKC's level | lines that do not express GJB3 (31) vs lines expressing it (19) | 3.71× lower at baseline in the lines without GJB3 | 3e-04 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10 |
| [[INAVA]], [[MROH3P]] | B | INAVA, MROH3P activity raises ITPKC's level | lines that do not express INAVA, MROH3P (29) vs lines expressing them (21) | 2.96× lower at baseline in the lines without INAVA, MROH3P | 3e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, MAL2, B3GNT3; co-absent genes |
| [[C1orf116]] | B | C1orf116 activity raises ITPKC's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 3.59× lower at baseline in the lines without C1orf116 | 1e-03 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[SGPP2]] | B | SGPP2 activity raises ITPKC's level | lines that do not express SGPP2 (32) vs lines expressing it (18) | 3.47× lower at baseline in the lines without SGPP2 | 1e-03 | ⚠ within organs, on part of the lines; also absent: ST14, CATSPERB, TMPRSS4 |
| [[C6orf132]] | B | C6orf132 activity raises ITPKC's level | lines that do not express C6orf132 (27) vs lines expressing it (23) | 2.66× lower at baseline in the lines without C6orf132 | 0.002 | ⚠ within organs, on part of the lines; also absent: PCSK9, RNF223, CDH1 |
| [[TRIM15]] | B | TRIM15 activity raises ITPKC's level | lines that do not express TRIM15 (34) vs lines expressing it (16) | 3.33× lower at baseline in the lines without TRIM15 | 0.002 | ⚠ within organs, on part of the lines; also absent: TMEM45B, EPS8L3, ENSG00000225680 |
| [[HSH2D]] | B | HSH2D activity raises ITPKC's level | lines that do not express HSH2D (27) vs lines expressing it (23) | 2.81× lower at baseline in the lines without HSH2D | 0.004 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM; maybe low, not absent |
| [[B3GNT3]] | B | B3GNT3 activity raises ITPKC's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 2.70× lower at baseline in the lines without B3GNT3 | 0.006 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[KIAA0040]] | B | KIAA0040 activity raises ITPKC's level | lines that do not express KIAA0040 (24) vs lines expressing it (26) | 2.50× lower at baseline in the lines without KIAA0040 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000226281, CLDN3, ESRP1 |
| [[LSMEM2]] | B | LSMEM2 activity raises ITPKC's level | lines that do not express LSMEM2 (8) vs lines expressing it (42) | 1.98× lower at baseline in the lines without LSMEM2 | 0.013 | ⚠ within organs, on part of the lines; also absent: PLEKHA2, ATL1, ENSG00000283573; maybe low, not absent |
| [[FOXQ1]] | B | FOXQ1 activity raises ITPKC's level | lines that do not express FOXQ1 (30) vs lines expressing it (20) | 2.58× lower at baseline in the lines without FOXQ1 | 0.018 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TTC22, COL17A1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.533). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.9, 47.3); signed map (7.1, 32.7). **Vector** length 117, 31.4% of its response variance represented; |z| ≥ 3 in 1,194 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +6.1 | +9.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.7 | +9.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.1 | +1.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.8 | +10.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.1 | +3.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.7 | +3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +4.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.2 | +0.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +2.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.9 | +3.0 |
| fall | [[NG25 (drug)]] 5 µM |  | -5.0 | -7.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | +0.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.3 | -9.3 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.2 | -6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | -4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.3 | -6.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.8 | -4.1 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -2.4 | -2.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.4 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | inositol-trisphosphate 3-kinase C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:40,717,112-40,740,860 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IP3KC, IP3-3KC |
| Gene groups (HGNC) | Inositol-trisphosphate 3-kinase family |
| Reactome | 2 pathways, smallest: Synthesis of IP3 and IP4 in the cytosol; Inositol phosphate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96DU7](https://www.uniprot.org/uniprotkb/Q96DU7) (Inositol-trisphosphate 3-kinase C):

> Catalyzes the phosphorylation of 1D-myo-inositol 1,4,5-trisphosphate (InsP3) into 1D-myo-inositol 1,3,4,5-tetrakisphosphate and participates to the regulation of calcium homeostasis. Can phosphorylate inositol 2,4,5-triphosphate to inositol 2,4,5,6-tetraphosphate (By similarity).

**Summary**, from NCBI Gene [80271](https://www.ncbi.nlm.nih.gov/gene/80271):

> This gene encodes a member of the inositol 1,4,5-trisphosphate [Ins(1,4,5)P(3)] 3-kinase family of enzymes that catalyze the phosphorylation of inositol 1,4,5-trisphosphate to 1,3,4,5-tetrakisphosphate. The encoded protein is localized to the nucleus and cytoplasm and has both nuclear import and nuclear export activity. Single nucleotide polymorphisms in this gene are associated with Kawasaki disease.[provided by RefSeq, Sep 2009]

**Accessions** — [HGNC:14897](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14897) · Entrez [80271](https://www.ncbi.nlm.nih.gov/gene/80271) · UniProt [Q96DU7](https://www.uniprot.org/uniprotkb/Q96DU7) · Ensembl [ENSG00000086544](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000086544)

## Data

Gene col 1462: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1462); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1462, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1462]; `tensor/DDL_lfc|DDL_z.npy` [1462]; `embed/gene_vectors.npy` [1462]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1462 or target_col == 1462). Every well: [[ITPKC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITPKC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
