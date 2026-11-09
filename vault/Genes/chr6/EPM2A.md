---
symbol: "EPM2A"
type: "gene"
col: 3371
ensembl_id: "ENSG00000112425"
name: "EPM2A glucan phosphatase, laforin"
location: "6q24.3"
module: 124
arm: "+"
pooled_cpm: 9.33
n_lines_expressing: 48
n_dd_up: 8
n_dd_down: 13
n_dd_up_clean: 6
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/124"]
generated_by: "tahoemap"
---

# EPM2A

*EPM2A glucan phosphatase, laforin* — 6q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.83× (z +15.2, q 0e+00, up in 37 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.427× (z -8.8, q 7e-16, down in 32 of 45 measured lines).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GABPB1-AS1]] (+0.77, fdr 1e-05), [[ADCK1]] (+0.77, fdr 2e-05), [[PIGW]] (+0.75, fdr 3e-05); moves opposite to [[GPATCH11]] (-0.70, fdr 2e-05), [[RAB3A]] (-0.69, fdr 4e-04), [[ALAD]] (-0.69, fdr 3e-05).
> It sits in the **+** arm of [[Module 124]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[SLC17A7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3371.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.83×** | +15.2 | 0e+00 | 37/42 (A498, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.39×** | +9.0 | 7e-17 | 29/43 (A-172, HOP62, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.94×** | +6.6 | 9e-09 | 26/43 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.55×** | +6.4 | 3e-08 | 25/45 (J82, A498, …) | rises with dose | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +5.9 | 4e-07 | 22/42 (HOP62, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.60×** | +4.4 | 9e-04 | 15/45 (C32, LS 180, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.44×** | +3.4 | 0.047 | 7/31 (Hs 766T, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.39×** | +3.4 | 0.056 | 6/44 (HEC-1-A, NCI-H460, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 1.36× | +3.1 | 0.10 | 9/44 (A498, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.24× | +3.1 | 0.12 | 11/46 (HOP62, A-172, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.34× | +3.0 | 0.13 | 7/43 (COLO 205, SNU-1, …) | inconsistent across doses |  |
| [[Benztropine (mesylate) (drug)]] 0.5 µM |  | 1.34× | +3.0 | 0.13 | 6/45 (NCI-H2030, HS-578T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3371.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.427×** | -8.8 | 7e-16 | 32/45 (SW480, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.438×** | -8.6 | 3e-15 | 32/45 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.531×** | -6.6 | 1e-08 | 27/45 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.550×** | -6.0 | 4e-07 | 24/44 (NCI-H2030, NCI-H460, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.684×** | -5.6 | 3e-06 | 21/42 (LOX-IMVI, HEC-1-A, …) | top dose only | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.619×** | -5.0 | 6e-05 | 23/42 (NCI-H23, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.673×** | -4.0 | 0.006 | 11/46 (SK-MEL-2, NCI-H460, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.484×** | -3.9 | 0.006 | 17/44 (NCI-H2030, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **0.688×** | -3.9 | 0.006 | 20/41 (SW480, PANC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.704×** | -3.6 | 0.015 | 16/45 (LoVo, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **0.705×** | -3.6 | 0.015 | 20/45 (SW480, PANC-1, …) | rises with dose | composition shift |
| [[Malotilate (drug)]] 0.05 µM |  | **0.718×** | -3.4 | 0.029 | 15/44 (C-33 A, H4, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.741×** | -3.1 | 0.081 | 13/45 (SW480, NCI-H2030, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3371. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 13.3 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.161× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.202× (z -10.1) |
| [[A-172 (line)]] | wt | 5.87 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.43× (z +10.7) | [[Belinostat (drug)]] 0.5 µM 0.110× (z -9.0) |
| [[HOP62 (line)]] | alt | 5.81 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.03× (z +9.7) | — |
| [[NCI-H2030 (line)]] | alt | 26.4 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.194× (z -9.1) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.231× (z -8.5) |
| [[HS-578T (line)]] | alt | 7.14 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.38× (z +9.5) | — |
| [[LoVo (line)]] | wt | 17.4 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.218× (z -10.9) |
| [[LOX-IMVI (line)]] | wt | 7.17 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.96× (z +11.0) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0671× (z -11.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 9.93 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.120× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Orlistat (drug)]] 0.05 µM 0.142× (z -8.5) |
| [[PANC-1 (line)]] | alt | 11.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.193× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[A498 (line)]] | wt | 4.48 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.15× (z +14.7) | — |
| [[AN3 CA (line)]] | alt | 21.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0629× (z -8.5) |
| [[C-33 A (line)]] | alt | 10.3 | 0 | 1 | — | [[Aspirin (drug)]] 0.5 µM 0.0638× (z -9.7) |
| [[HepG2_C3A (line)]] | wt | 9.93 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.73× (z +8.5) | — |
| [[NCI-H23 (line)]] | alt | 9.70 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0544× (z -13.7) |
| [[NCI-H460 (line)]] | wt | 16.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -11.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 9.05 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.59× (z +9.2) | — |
| [[A-427 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.02 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.43 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.29 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.72 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.35 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3371), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GABPB1-AS1]] | +0.77 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[ADCK1]] | +0.77 | +0.72 / +0.47 | both halves | 2e-05 |  |
| [[PIGW]] | +0.75 | +0.70 / +0.45 | both halves | 3e-05 |  |
| [[DPH5-DT]] | +0.75 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[CRPPA]] | +0.73 | +0.62 / +0.39 | both halves | 6e-05 |  |
| [[ZNF124]] | +0.73 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[AVEN]] | +0.72 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[ARSB]] | +0.72 | +0.64 / +0.39 | both halves | 5e-05 | pathway: Diseases of carbohydrate metabolism |
| [[PCBD2]] | +0.70 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[POU6F1]] | +0.69 | +0.50 / +0.39 | both halves | 5e-05 |  |
| [[MYLK4]] | +0.69 | +0.45 / +0.38 | both halves | 6e-05 |  |
| [[PBLD]] | +0.68 | +0.53 / +0.18 | ⚠ one half (not replicated) | 9e-04 |  |
| [[MSANTD2]] | +0.68 | +0.56 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPATCH11]] | -0.70 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[RAB3A]] | -0.69 | -0.62 / -0.26 | both halves | 4e-04 |  |
| [[ALAD]] | -0.69 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[PIGH]] | -0.68 | -0.63 / -0.28 | both halves | 3e-04 |  |
| [[CDKN2D]] | -0.66 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[GNAI2]] | -0.66 | -0.60 / -0.10 | ⚠ one half (not replicated) | 0.003 |  |
| [[IFT172]] | -0.65 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[ARL3]] | -0.65 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[SLC27A1]] | -0.63 | -0.55 / -0.10 | ⚠ one half (not replicated) | 0.003 |  |
| [[INIP]] | -0.63 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[NPHP1]] | -0.62 | -0.30 / -0.51 | both halves | 2e-04 |  |
| [[RNF24]] | -0.62 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[KLHL26]] | -0.62 | -0.46 / -0.30 | both halves | 2e-04 |  |
| [[RNF114]] | -0.61 | -0.37 / -0.54 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC17A7]] | B | SLC17A7 activity raises EPM2A's level | lines that do not express SLC17A7 (9) vs lines expressing it (41) | 2.05× lower at baseline in the lines without SLC17A7 | 0.007 | ⚠ within organs, on part of the lines; also absent: GXYLT2, ITGA10, NT5M; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers EPM2A's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TBX18]] | B | TBX18 activity raises EPM2A's level | lines that do not express TBX18 (27) vs lines expressing it (23) | 1.52× lower at baseline in the lines without TBX18 | 0.059 | ⚠ within organs, on part of the lines; also absent: SFRP1, LRRK2, ENSG00000286251 |
| [[ASB4]] | B | ASB4 activity raises EPM2A's level | lines that do not express ASB4 (31) vs lines expressing it (19) | 1.49× lower at baseline in the lines without ASB4 | 0.072 | ⚠ within organs, on part of the lines; also absent: ST18, PCK1, FAM3D |
| [[LLGL2]] | B | LLGL2 activity weakens EPM2A's drug response | lines that do not express LLGL2 (12) vs lines expressing it (34) | the lines without LLGL2 respond 1.26× as strongly (z diff -0.47); strongest at Auranofin 5 µM: 4.15x vs 1.81x (z diff -3.1) | 0.082 | ⚠ within organs, on part of the lines; also absent: GRTP1, FGFR4, LSR; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 124]]; 39 genes; this gene is in the **+** arm (projection on the module's main direction 0.829). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-4.1, 9.0); signed map (23.4, -28.7). **Vector** length 91.3, 18.8% of its response variance represented; |z| ≥ 3 in 1,037 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.5 | +15.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +6.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.7 | +9.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.9 | +3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.2 | +2.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.2 | +1.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +1.7 |
| fall | [[Belinostat (drug)]] 5 µM |  | -5.8 | -6.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.3 | -8.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.8 | -8.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.1 | -3.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.0 | -5.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | -1.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.1 | -2.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.6 | -2.7 |
|  | [[Fumaric acid (drug)]] 5 µM |  | -1.6 | -3.0 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | -1.5 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | EPM2A glucan phosphatase, laforin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q24.3 — chr6:145,382,535-145,736,023 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LDE, LD |
| Gene groups (HGNC) | Atypical dual specificity phosphatases; Laforin/Malin E3-ubiquitin ligase complex |
| Reactome | 7 pathways, smallest: Myoclonic epilepsy of Lafora; Glycogen synthesis; Glycogen storage diseases |
| Matched by | ensembl_id |

UniProt [B3EWF7](https://www.uniprot.org/uniprotkb/B3EWF7) carries no function annotation.

**Summary**, from NCBI Gene [7957](https://www.ncbi.nlm.nih.gov/gene/7957):

> This gene encodes a dual-specificity phosphatase and may be involved in the regulation of glycogen metabolism. The protein acts on complex carbohydrates to prevent glycogen hyperphosphorylation, thus avoiding the formation of insoluble aggregates. Loss-of-function mutations in this gene have been associated with Lafora disease, a rare, adult-onset recessive neurodegenerative disease, which results in myoclonus epilepsy and usually results in death several years after the onset of symptoms. The …

**Accessions** — [HGNC:3413](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3413) · Entrez [7957](https://www.ncbi.nlm.nih.gov/gene/7957) · UniProt [B3EWF7](https://www.uniprot.org/uniprotkb/B3EWF7) · Ensembl [ENSG00000112425](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112425)

## Data

Gene col 3371: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3371); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3371, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3371]; `tensor/DDL_lfc|DDL_z.npy` [3371]; `embed/gene_vectors.npy` [3371]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3371 or target_col == 3371). Every well: [[EPM2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPM2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
