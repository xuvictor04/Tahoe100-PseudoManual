---
symbol: "KMT2E-AS1"
type: "gene"
col: 14200
ensembl_id: "ENSG00000239569"
name: "KMT2E antisense RNA 1"
location: "7q22.3"
module: 23
arm: "+"
pooled_cpm: 5.41
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 9
n_dd_up_clean: 13
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# KMT2E-AS1

*KMT2E antisense RNA 1* — 7q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.54× (z +11.8, q 2e-29, up in 37 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.206× (z -15.3, q 0e+00, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01004]] (+0.81, fdr 1e-05, ⚠ same locus), [[LINC01090]] (+0.80, fdr 1e-05), [[SPEN-AS1]] (+0.78, fdr 1e-05), [[TMEM202-AS1]] (+0.76, fdr 3e-05); moves opposite to [[RRP1B]] (-0.66, fdr 1e-05), [[STUB1]] (-0.66, fdr 0.002, ⚠ not reproduced), [[WRAP73]] (-0.65, fdr 2e-04).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14200.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.54×** | +11.8 | 2e-29 | 37/40 (AsPC-1, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.33×** | +10.6 | 5e-24 | 32/38 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.84×** | +10.1 | 7e-22 | 25/27 (NCI-H460, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.00×** | +9.9 | 9e-21 | 15/17 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.44×** | +8.7 | 5e-16 | 27/38 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.37×** | +8.0 | 8e-14 | 8/11 (HS-578T, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.02×** | +6.8 | 7e-10 | 29/47 (KATO III, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.03×** | +6.6 | 3e-09 | 19/31 (SW1417, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.56×** | +5.7 | 1e-06 | 20/46 (PANC-1, HEC-1-A, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +5.4 | 3e-06 | 17/36 (MIA PaCa-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.71×** | +5.2 | 1e-05 | 19/45 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.52×** | +4.9 | 5e-05 | 15/47 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +4.8 | 7e-05 | 18/38 (RKO, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.59×** | +4.5 | 2e-04 | 17/46 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.54×** | +3.9 | 0.004 | 8/34 (RKO, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +3.8 | 0.004 | 14/38 (A498, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +3.5 | 0.015 | 16/44 (NCI-H23, A-427, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.36×** | +3.0 | 0.083 | 8/42 (C32, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14200.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.206×** | -15.3 | 0e+00 | 42/47 (C32, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.279×** | -12.4 | 1e-32 | 40/47 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.729×** | -10.7 | 2e-24 | 44/48 (NCI-H1792, SW480, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.366×** | -9.7 | 3e-20 | 35/45 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.395×** | -9.0 | 3e-17 | 38/47 (C32, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.493×** | -6.8 | 8e-10 | 26/39 (LOX-IMVI, A-427, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.400×** | -4.6 | 3e-04 | 13/42 (AsPC-1, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **0.666×** | -3.9 | 0.006 | 12/35 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.749×** | -3.8 | 0.009 | 10/46 (SW 900, SW480, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14200. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 5.28 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 8.88× (z +10.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 4.51× (z +9.2) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.122× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 8.09 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0389× (z -14.0) |
| [[LoVo (line)]] | wt | 6.37 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.52× (z +10.3) | [[Belinostat (drug)]] 5 µM 0.105× (z -10.1) |
| [[AsPC-1 (line)]] | alt | 3.83 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.40× (z +9.3) | — |
| [[C32 (line)]] | wt | 16.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0993× (z -11.2) |
| [[COLO 205 (line)]] | alt | 5.72 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0597× (z -8.5) |
| [[HCT15 (line)]] | alt | 5.62 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0421× (z -9.1) |
| [[HS-578T (line)]] | alt | 4.27 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0559× (z -8.9) |
| [[KATO III (line)]] | alt | 9.81 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 8.90× (z +9.8) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 4.54 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0744× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 6.66 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0411× (z -12.5) |
| [[NCI-H2030 (line)]] | alt | 4.88 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0342× (z -11.8) |
| [[PANC-1 (line)]] | alt | 4.15 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.144× (z -8.9) |
| [[RKO (line)]] | wt | 6.94 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0675× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 5.09 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0634× (z -8.8) |
| [[SW1417 (line)]] | alt | 10.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.147× (z -8.7) |
| [[SW480 (line)]] | alt | 7.83 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.109× (z -12.1) |
| [[A-172 (line)]] | wt | 4.52 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.89 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.45 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.56 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.52 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.05 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14200), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 7 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01004]] | +0.81 | +0.72 / +0.56 | both halves | 1e-05 | ⚠ same locus (0.2 kb, same strand: neighbours can correlate without regulation) |
| [[LINC01090]] | +0.80 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[SPEN-AS1]] | +0.78 | +0.65 / +0.53 | both halves | 1e-05 | same gene group |
| [[TMEM202-AS1]] | +0.76 | +0.62 / +0.45 | both halves | 3e-05 | same gene group |
| [[USP34-DT]] | +0.76 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[STX17-DT]] | +0.76 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[CYB5D2]] | +0.74 | +0.70 / +0.45 | both halves | 3e-05 |  |
| [[LRP2BP]] | +0.74 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[UBE2D3-AS1]] | +0.74 | +0.63 / +0.56 | both halves | 1e-05 | same gene group |
| [[TBCE-1]] | +0.74 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[PPP1R12A-AS2]] | +0.73 | +0.63 / +0.31 | both halves | 2e-04 | same gene group |
| [[EFCAB5]] | +0.73 | +0.56 / +0.31 | both halves | 2e-04 |  |
| [[NUTM2E]] | +0.73 | +0.67 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRP1B]] | -0.66 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[STUB1]] | -0.66 | -0.47 / -0.11 | ⚠ not reproduced | 0.002 |  |
| [[WRAP73]] | -0.65 | -0.45 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers KMT2E-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HOXC9]] | B | HOXC9 activity raises KMT2E-AS1's level | lines that do not express HOXC9 (10) vs lines expressing it (40) | 1.18× lower at baseline in the lines without HOXC9 | 0.044 | ⚠ within organs, on part of the lines; also absent: HOXC4, LINC01013, SOCS2 |
| [[SIM2]] | B | SIM2 activity raises KMT2E-AS1's level | lines that do not express SIM2 (9) vs lines expressing it (41) | 1.31× lower at baseline in the lines without SIM2 | 0.064 | ⚠ within organs, on part of the lines; also absent: SMC1B |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises KMT2E-AS1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises KMT2E-AS1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.793). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (9.8, 21.6); signed map (28.8, -2.2). **Vector** length 82.8, 15.9% of its response variance represented; |z| ≥ 3 in 998 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.5 | +11.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.7 | +10.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.6 | +5.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +9.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +3.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.5 | +2.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.4 | +1.6 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | +1.2 | +0.7 |
| fall | [[Belinostat (drug)]] 5 µM |  | -5.7 | -12.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.0 | -9.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.5 | -15.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.3 | -6.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.9 | -9.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.0 | -4.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -0.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.7 | -1.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.5 | -1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | +1.3 |

## What is on record

|  |  |
|---|---|
| Name | KMT2E antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 7q22.3 — chr7:105,013,277-105,014,321 (-) |
| Ensembl biotype | lncRNA |
| Also known as | lncPENG, LOC100216545, RP11-325F22.5.1; previously LINC01004, LHFPL3-AS2 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40845](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40845) · Entrez [100216545](https://www.ncbi.nlm.nih.gov/gene/100216545) · Ensembl [ENSG00000239569](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000239569)

## Data

Gene col 14200: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14200); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14200, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14200]; `tensor/DDL_lfc|DDL_z.npy` [14200]; `embed/gene_vectors.npy` [14200]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14200 or target_col == 14200). Every well: [[KMT2E-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KMT2E-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
