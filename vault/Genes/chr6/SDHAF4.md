---
symbol: "SDHAF4"
type: "gene"
col: 7766
ensembl_id: "ENSG00000154079"
name: "succinate dehydrogenase complex assembly factor 4"
location: "6q13"
module: 15
arm: "+"
pooled_cpm: 9.45
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 19
n_dd_up_clean: 10
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# SDHAF4

*succinate dehydrogenase complex assembly factor 4* — 6q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.10× (z +11.5, q 7e-28, up in 30 of 36 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.36× (z +7.1, q 3e-10, up in 21 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.512× (z -15.2, q 0e+00, down in 37 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GOT1-DT]] (+0.72, fdr 7e-06), [[TMEM68]] (+0.72, fdr 7e-06), [[RWDD3]] (+0.67, fdr 7e-06); moves opposite to [[KLF2]] (-0.55, fdr 6e-05), [[RMC1]] (-0.55, fdr 4e-05), [[RALY]] (-0.53, fdr 4e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7766.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.10×** | +11.5 | 7e-28 | 30/36 (NCI-H2347, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.41×** | +7.8 | 1e-12 | 26/48 (NCI-H2347, NCI-H1573, …) | rises with dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +7.1 | 3e-10 | 21/44 (AsPC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.54×** | +6.9 | 6e-10 | 21/47 (KATO III, NCI-H23, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.41×** | +5.5 | 4e-06 | 13/45 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.40×** | +5.4 | 7e-06 | 15/47 (HOP62, A-172, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +5.2 | 1e-05 | 19/48 (NCI-H2030, A549, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +5.0 | 5e-05 | 17/46 (NCI-H2030, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +4.5 | 4e-04 | 9/47 (NCI-H2347, LS 180, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.32×** | +4.5 | 4e-04 | 11/44 (SNU-423, NCI-H2030, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.32×** | +4.4 | 5e-04 | 8/46 (NCI-H2347, SW480, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.29×** | +4.1 | 0.002 | 11/34 (A498, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Triamcinolone (drug)]] 5 µM |  | 1.19× | +4.0 | 0.003 | 11/47 (NCI-H2030, A498, …) | rises with dose | position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.027 | 3/48 (HepG2/C3A, SW480, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.22×** | +3.2 | 0.047 | 5/44 (A-427, SW480, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.050 | 9/45 (KATO III, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +3.1 | 0.065 | 6/48 (NCI-H2347, NCI-H661, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7766.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.512×** | -15.2 | 0e+00 | 37/46 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.562×** | -9.2 | 7e-18 | 30/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.558×** | -9.0 | 4e-17 | 31/46 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.347×** | -8.9 | 7e-17 | 29/47 (LoVo, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.593×** | -8.4 | 5e-15 | 26/43 (NCI-H2347, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.411×** | -7.5 | 7e-12 | 25/43 (LS 180, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.654×** | -6.8 | 8e-10 | 19/47 (PANC-1, BT-474, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.660×** | -6.7 | 2e-09 | 20/47 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.648×** | -6.6 | 3e-09 | 19/44 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.677×** | -6.3 | 2e-08 | 23/46 (LS 180, SW480, …) | two highest doses | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.679×** | -6.2 | 3e-08 | 21/47 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.693×** | -5.9 | 2e-07 | 20/46 (BT-474, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.719×** | -5.3 | 5e-06 | 17/47 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.726×** | -5.1 | 1e-05 | 17/43 (PANC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.717×** | -5.1 | 1e-05 | 19/39 (NCI-H460, SNU-423, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.727×** | -5.1 | 1e-05 | 15/47 (C32, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.735×** | -4.9 | 3e-05 | 16/47 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7766. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 19.0 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -19.1) |
| [[NCI-H460 (line)]] | wt | 7.92 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.151× (z -11.8) |
| [[SNU-423 (line)]] | alt | 8.52 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -11.1) |
| [[NCI-H2347 (line)]] | alt | 8.94 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.135× (z -12.3) |
| [[A498 (line)]] | wt | 3.89 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -12.4) |
| [[A549 (line)]] | wt | 7.74 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -9.3) |
| [[H4 (line)]] | wt | 9.58 | 0 | 1 | — | [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM 0.0693× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 11.3 | 0 | 1 | — | [[Mebendazole (drug)]] 0.5 µM 0.0573× (z -10.0) |
| [[LoVo (line)]] | wt | 7.64 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -8.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 9.99 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.162× (z -9.9) |
| [[LS 180 (line)]] | wt | 11.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.144× (z -10.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 7.82 | 0 | 1 | — | [[Brivudine (drug)]] 0.05 µM 0.0813× (z -9.2) |
| [[SW48 (line)]] | wt | 10.2 | 0 | 1 | — | [[Almonertinib (hydrochloride) (drug)]] 0.5 µM 0.0759× (z -9.2) |
| [[SW480 (line)]] | alt | 10.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.254× (z -9.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 8.25 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.97 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.03 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.30 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.32 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.72 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.92 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.18 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7766), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOT1-DT]] | +0.72 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[TMEM68]] | +0.72 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[RWDD3]] | +0.67 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[VPS13B-DT]] | +0.65 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[ANGEL2]] | +0.63 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[TMED8]] | +0.63 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[DDX59]] | +0.63 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[C8orf76]] | +0.62 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[PIGC]] | +0.62 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[CMC1]] | +0.61 | +0.62 / +0.72 | both halves | 7e-06 | same gene group; pathway: Aerobic respiration and respiratory electron transport |
| [[TSTD3]] | +0.60 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[RAB11FIP2]] | +0.60 | +0.58 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLF2]] | -0.55 | -0.43 / -0.38 | both halves | 6e-05 |  |
| [[RMC1]] | -0.55 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[RALY]] | -0.53 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[CMIP]] | -0.53 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[ARHGAP39]] | -0.52 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[DNAJB1]] | -0.51 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[ABAT]] | -0.50 | -0.36 / -0.32 | both halves | 2e-04 |  |
| [[ZSWIM6]] | -0.50 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[SLC9A3R1]] | -0.49 | -0.44 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SDHAF4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[AMDHD2]] | C | AMDHD2's natural level weakens SDHAF4's drug response | AMDHD2's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.62, reverse -0.15; direction not clear | 0.092 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.657). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-14.7, 19.8); signed map (-30.5, -20.0). **Vector** length 67.8, 10.8% of its response variance represented; |z| ≥ 3 in 972 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +7.2 | +11.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +6.1 | +7.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +5.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +3.1 | +4.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +7.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +6.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +0.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.8 | +2.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.7 | +5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +5.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.6 | -9.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.4 | -15.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.3 | -5.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.6 | -2.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.3 | -5.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -6.7 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | -1.4 | -1.4 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -1.3 | -0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.3 | -5.1 |
|  | [[Apalutamide (drug)]] 0.5 µM |  | -1.3 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | succinate dehydrogenase complex assembly factor 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q13 — chr6:70,566,917-70,589,569 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Sdh8; previously C6orf57 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors |
| Reactome | 3 pathways, smallest: Maturation of TCA enzymes and regulation of TCA cycle; Citric acid cycle (TCA cycle); Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VUM1](https://www.uniprot.org/uniprotkb/Q5VUM1) (Succinate dehydrogenase assembly factor 4, mitochondrial):

> Plays an essential role in the assembly of succinate dehydrogenase (SDH), an enzyme complex (also referred to as respiratory complex II) that is a component of both the tricarboxylic acid (TCA) cycle and the mitochondrial electron transport chain, and which couples the oxidation of succinate to fumarate with the reduction of ubiquinone (coenzyme Q) to ubiquinol. Binds to the flavoprotein subunit SDHA in its FAD-bound form, blocking the generation of excess reactive oxygen species (ROS) and …

**Summary**, from NCBI Gene [135154](https://www.ncbi.nlm.nih.gov/gene/135154):

> Predicted to enable enzyme activator activity. Involved in cellular respiration and mitochondrial respiratory chain complex II assembly. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20957](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20957) · Entrez [135154](https://www.ncbi.nlm.nih.gov/gene/135154) · UniProt [Q5VUM1](https://www.uniprot.org/uniprotkb/Q5VUM1) · Ensembl [ENSG00000154079](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154079)

## Data

Gene col 7766: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7766); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7766, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7766]; `tensor/DDL_lfc|DDL_z.npy` [7766]; `embed/gene_vectors.npy` [7766]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7766 or target_col == 7766). Every well: [[SDHAF4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SDHAF4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
