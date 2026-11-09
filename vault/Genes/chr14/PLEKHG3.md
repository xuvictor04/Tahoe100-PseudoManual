---
symbol: "PLEKHG3"
type: "gene"
col: 4772
ensembl_id: "ENSG00000126822"
name: "pleckstrin homology and RhoGEF domain containing G3"
location: "14q23.3"
module: 14
arm: "+"
pooled_cpm: 22.14
n_lines_expressing: 45
n_dd_up: 16
n_dd_down: 9
n_dd_up_clean: 11
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 17
direction_downstream: 3
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# PLEKHG3

*pleckstrin homology and RhoGEF domain containing G3* — 14q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.81× (z +14.8, q 0e+00, up in 24 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.409× (z -15.8, q 0e+00, down in 33 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP43]] (+0.59, fdr 2e-05), [[EHF]] (+0.55, fdr 4e-05), [[BCL9L]] (+0.55, fdr 1e-05); moves opposite to [[STRAP]] (-0.51, fdr 7e-05), [[CA5B]] (-0.47, fdr 1e-04), [[YIPF1]] (-0.45, fdr 1e-04).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[ANO9]] → it (grade B ⚠); 3 go from it, the strongest it → cells under [[Ixazomib citrate (drug)]] 5 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4772.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.81×** | +14.8 | 0e+00 | 24/42 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.17×** | +12.3 | 2e-32 | 27/42 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.56×** | +8.7 | 8e-16 | 28/43 (SW480, SW1417, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +7.3 | 4e-11 | 5/43 (MIA PaCa-2, HCT15, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.86×** | +5.7 | 1e-06 | 21/40 (SW480, SW1417, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +5.5 | 4e-06 | 20/39 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~23% of this change | **1.29×** | +4.5 | 6e-04 | 13/38 (HOP62, SHP-77, …) | inconsistent across doses | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.28×** | +4.3 | 0.001 | 14/42 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 1.18× | +4.2 | 0.002 | 12/43 (BT-474, A498, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.27×** | +4.1 | 0.002 | 14/41 (HOP62, PANC-1, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.24×** | +3.8 | 0.007 | 7/43 (HepG2/C3A, A498, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.23×** | +3.6 | 0.016 | 16/42 (A498, PANC-1, …) | rises with dose | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.32×** | +3.5 | 0.022 | 9/39 (SK-MEL-2, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.21×** | +3.4 | 0.027 | 14/42 (KATO III, SW480, …) | rises with dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.42×** | +3.2 | 0.051 | 4/38 (Hs 766T, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.21×** | +3.2 | 0.058 | 8/39 (SW480, LS 180, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.21×** | +3.1 | 0.059 | 7/39 (SW1417, SNU-423, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.28×** | +3.1 | 0.065 | 5/39 (HT-29, SW480, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4772.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.409×** | -15.8 | 0e+00 | 33/43 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.454×** | -14.0 | 6e-42 | 33/42 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.559×** | -10.3 | 1e-22 | 26/42 (LoVo, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.570×** | -10.0 | 3e-21 | 22/33 (CFPAC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.639×** | -7.1 | 1e-10 | 16/27 (LS 180, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.673×** | -7.0 | 2e-10 | 19/41 (HT-29, CFPAC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.710×** | -5.6 | 2e-06 | 16/29 (CFPAC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.773×** | -4.3 | 0.001 | 15/40 (SW1417, SNU-423, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.774×** | -4.1 | 0.003 | 16/36 (CFPAC-1, HT-29, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4772. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 63.4 | 1 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +18.7) | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.289× (z -11.9) |
| [[LoVo (line)]] | wt | 39.6 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.254× (z -13.7) |
| [[SW480 (line)]] | alt | 39.0 | 1 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.28× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.261× (z -13.8) |
| [[A498 (line)]] | wt | 22.4 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +20.0) | — |
| [[A549 (line)]] | wt | 25.4 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.122× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.282× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 27.5 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.0865× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.307× (z -10.9) |
| [[KATO III (line)]] | alt | 26.2 | 2 | 2 | [[Harringtonine (drug)]] 5 µM 4.46× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.195× (z -12.1) |
| [[LS 180 (line)]] | wt | 47.3 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0748× (z -20.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.154× (z -16.7) |
| [[PANC-1 (line)]] | alt | 13.3 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.90× (z +19.4) | — |
| [[AsPC-1 (line)]] | alt | 21.4 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +11.2) | [[Panobinostat (drug)]] 0.5 µM 0.195× (z -11.0) |
| [[HT-29 (line)]] | alt | 33.5 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.174× (z -13.1) |
| [[Panc 03.27 (line)]] | alt | 61.6 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.223× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.375× (z -8.5) |
| [[SNU-423 (line)]] | alt | 21.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +14.8) | [[Selinexor (drug)]] 5 µM 0.269× (z -12.2) ⚠ cell-cycle shift, explains ~57% of this change |
| [[BT-474 (line)]] | alt | 26.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +8.7) | [[Panobinostat (drug)]] 0.5 µM 0.209× (z -10.6) |
| [[SW1417 (line)]] | alt | 38.7 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +12.8) | [[Panobinostat (drug)]] 0.5 µM 0.327× (z -9.4) |
| [[A-172 (line)]] | wt | 17.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.48× (z +14.0) | — |
| [[A-427 (line)]] | wt | 9.05 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.151× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~4% of this change |
| [[C32 (line)]] | wt | 7.04 | 0 | 1 | — | [[Rifaximin (drug)]] 0.05 µM 0.0531× (z -10.5) |
| [[HCT15 (line)]] | alt | 53.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -13.7) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 13.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +13.9) | — |
| [[HOP62 (line)]] | alt | 6.21 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +9.0) | — |
| [[NCI-H2347 (line)]] | alt | 28.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +11.2) | — |
| [[AN3 CA (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.29 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.35 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.35 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.07 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.52 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4772), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP43]] | +0.59 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[EHF]] | +0.55 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[BCL9L]] | +0.55 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[SERTAD2]] | +0.55 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[RTKN]] | +0.54 | +0.46 / +0.53 | both halves | 2e-05 | same gene group; pathway: RHOA GTPase cycle |
| [[CDC42EP1]] | +0.54 | +0.46 / +0.54 | both halves | 3e-05 | pathway: CDC42 GTPase cycle; STRING 403 |
| [[NUAK1]] | +0.53 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[LAMB3]] | +0.53 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[CX3CL1]] | +0.52 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[NFKBIE]] | +0.52 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[BCL3]] | +0.51 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[SLCO3A1]] | +0.51 | +0.51 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STRAP]] | -0.51 | -0.38 / -0.53 | both halves | 7e-05 |  |
| [[CA5B]] | -0.47 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[YIPF1]] | -0.45 | -0.44 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 16, C 1. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANO9]] | B | ANO9 activity raises PLEKHG3's level | lines that do not express ANO9 (22) vs lines expressing it (28) | 2.33× lower at baseline in the lines without ANO9 | 0.002 | ⚠ within organs, on part of the lines; also absent: ELF3, PRAG1, TRIM29 |
| [[LRATD2]] | B | LRATD2 activity raises PLEKHG3's level | lines that do not express LRATD2 (16) vs lines expressing it (34) | 2.30× lower at baseline in the lines without LRATD2 | 0.002 | ⚠ within organs, on part of the lines; also absent: POU5F1B, PCAT1, ITGB8; maybe low, not absent |
| [[RASEF]] | B | RASEF activity raises PLEKHG3's level | lines that do not express RASEF (20) vs lines expressing it (30) | 1.68× lower at baseline in the lines without RASEF | 0.015 | ⚠ within organs, on part of the lines; also absent: LIPH, ENSG00000263325, DENND2D |
| [[FOXA1]] | B | FOXA1 activity raises PLEKHG3's level | lines that do not express FOXA1 (22) vs lines expressing it (28) | 2.21× lower at baseline in the lines without FOXA1 | 0.024 | ⚠ within organs, on part of the lines; also absent: MYO5C, SPINT1, COBL |
| [[EHF]] | B | EHF activity raises PLEKHG3's level | lines that do not express EHF (27) vs lines expressing it (23) | 2.10× lower at baseline in the lines without EHF | 0.039 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, IRF6, GJB3 |
| [[BARX2]] | B | BARX2 activity raises PLEKHG3's level | lines that do not express BARX2 (29) vs lines expressing it (21) | 2.04× lower at baseline in the lines without BARX2 | 0.041 | ⚠ within organs, on part of the lines; also absent: COL17A1, FXYD3, CEACAM6 |
| [[WNT7A]] | B | WNT7A activity raises PLEKHG3's level | lines that do not express WNT7A (39) vs lines expressing it (11) | 1.70× lower at baseline in the lines without WNT7A | 0.060 | ⚠ within organs, on part of the lines; also absent: KRT5, GSDMC, CST6 |
| [[RASEF]] | B | RASEF activity strengthens PLEKHG3's drug response | lines that do not express RASEF (17) vs lines expressing it (26) | the lines without RASEF respond 0.45× as strongly (z diff +2.06); rises at some drug-doses, falls at others (46% from rises): Homoharringtonine 5 µM: 1.16x vs 2.01x (z diff +4.1); Dinaciclib 5 µM: 0.72x vs 0.40x (z diff +3.3); Harringtonine 5 µM: 1.49x vs 2.47x (z diff +2.9) | 0.063 | ⚠ within organs, on part of the lines; also absent: LIPH, ENSG00000263325, DENND2D; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[ANO9]] | B | ANO9 activity strengthens PLEKHG3's drug response | lines that do not express ANO9 (18) vs lines expressing it (25) | the lines without ANO9 respond 0.33× as strongly (z diff +2.91); rises at some drug-doses, falls at others (32% from rises): Dinaciclib 5 µM: 0.93x vs 0.38x (z diff +4.9); Homoharringtonine 5 µM: 1.11x vs 2.11x (z diff +4.4); Panobinostat 0.5 µM: 0.65x vs 0.35x (z diff +4.2) | 0.068 | ⚠ within organs, on part of the lines; also absent: ELF3, PRAG1, TRIM29; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[CD22]] | B | CD22 activity strengthens PLEKHG3's drug response | lines that do not express CD22 (17) vs lines expressing it (26) | the lines without CD22 respond 0.47× as strongly (z diff +2.11); strongest at Homoharringtonine 5 µM: 0.84x vs 2.46x (z diff +7.8) | 0.080 | ⚠ within organs, on part of the lines; also absent: CX3CL1, SHROOM4, CFB; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises PLEKHG3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PRSS22]] | B | PRSS22 activity raises PLEKHG3's level | lines that do not express PRSS22 (28) vs lines expressing it (22) | 2.44× lower at baseline in the lines without PRSS22 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ESRP2, CDH1, ST14 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Ixazomib citrate (drug)]] 5 µM | B | PLEKHG3 activity raises the cells' numbers under Ixazomib citrate 5 µM (protects the cells) | lines that do not express PLEKHG3 (5) vs lines expressing it (43) | the lines without PLEKHG3: 0.57× the cells of the other lines | 0.028 | ⚠ across organs; also absent: ATP11A, SHC2, PPP1R26; maybe low, not absent |
| cells under [[Doxycycline (monohydrate) (drug)]] 5 µM | B | PLEKHG3 activity raises the cells' numbers under Doxycycline (monohydrate) 5 µM (protects the cells) | lines that do not express PLEKHG3 (5) vs lines expressing it (43) | the lines without PLEKHG3: 0.72× the cells of the other lines | 0.051 | ⚠ across organs; also absent: ATP11A, SHC2, PPP1R26; maybe low, not absent |
| [[LGALSL-DT]] | C | PLEKHG3 activity raises LGALSL-DT's level | lines that do not express PLEKHG3 (5) vs lines expressing it (45) | 3.03× lower at baseline in the lines without PLEKHG3 | 0.011 | ⚠ across organs; also absent: ATP11A, SHC2, PPP1R26; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.557). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.4, 7.6); signed map (43.6, 3.8). **Vector** length 98.6, 22.5% of its response variance represented; |z| ≥ 3 in 918 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +7.8 | +12.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | +5.5 | +3.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.5 | +14.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.8 | +5.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.9 | +8.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +1.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.7 | +4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +5.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +2.3 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.7 | -10.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.6 | -14.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.6 | -15.8 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.5 | -2.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.3 | -7.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -7.0 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.1 | -2.6 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.9 | -2.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.8 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | pleckstrin homology and RhoGEF domain containing G3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.3 — chr14:64,704,102-64,750,249 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ARHGEF43; previously KIAA0599 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Dbl family Rho GEFs |
| Reactome | 8 pathways, smallest: RHOQ GTPase cycle; RHOG GTPase cycle; RHOA GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [A1L390](https://www.uniprot.org/uniprotkb/A1L390) (Pleckstrin homology domain-containing family G member 3):

> Plays a role in controlling cell polarity and cell motility by selectively binding newly polymerized actin and activating RAC1 and CDC42 to enhance local actin polymerization.

**Summary**, from NCBI Gene [26030](https://www.ncbi.nlm.nih.gov/gene/26030):

> Enables actin binding activity. Involved in regulation of cell migration and regulation of establishment of cell polarity. Predicted to be located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20364](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20364) · Entrez [26030](https://www.ncbi.nlm.nih.gov/gene/26030) · UniProt [A1L390](https://www.uniprot.org/uniprotkb/A1L390) · Ensembl [ENSG00000126822](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126822)

## Data

Gene col 4772: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4772); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4772, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4772]; `tensor/DDL_lfc|DDL_z.npy` [4772]; `embed/gene_vectors.npy` [4772]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4772 or target_col == 4772). Every well: [[PLEKHG3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLEKHG3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
