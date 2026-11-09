---
symbol: "METTL21EP-1"
type: "gene"
col: 16526
ensembl_id: "ENSG00000290918"
name: ""
location: ""
module: 37
arm: "+"
pooled_cpm: 2.36
n_lines_expressing: 46
n_dd_up: 4
n_dd_down: 19
n_dd_up_clean: 3
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# METTL21EP-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.06× (z +11.0, q 2e-25, up in 24 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.191× (z -11.6, q 3e-28, down in 30 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF547]] (+0.72, fdr 7e-06), [[RNF139-DT]] (+0.70, fdr 7e-06), [[GABRR2]] (+0.70, fdr 7e-06); moves opposite to [[MRTFB]] (-0.53, fdr 3e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[C9]] → it (grade B ⚠); 2 go from it, the strongest it → [[FLJ46284]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16526.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.06×** | +11.0 | 2e-25 | 24/28 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.92×** | +4.5 | 0.002 | 10/41 (SW480, A498, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +4.3 | 0.004 | 0/2 | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.73×** | +3.8 | 0.021 | 10/37 (KATO III, NCI-H1573, …) | rises with dose | position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.57× | +3.1 | 0.21 | 5/32 (hTERT-HPNE, RPMI-7951, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16526.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.191×** | -11.6 | 3e-28 | 30/40 (LS 180, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.258×** | -9.5 | 9e-19 | 26/35 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.324×** | -7.9 | 6e-13 | 25/32 (LS 180, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.332×** | -7.4 | 2e-11 | 23/34 (COLO 205, A498, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.353×** | -7.3 | 4e-11 | 26/39 (CFPAC-1, BT-474, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.367×** | -7.0 | 2e-10 | 25/38 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.382×** | -6.7 | 1e-09 | 23/37 (NCI-H460, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **0.494×** | -4.9 | 6e-05 | 16/19 (Hs 766T, COLO 205, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.547×** | -4.2 | 0.001 | 19/38 (COLO 205, hTERT-HPNE, …) | two highest doses | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.571×** | -3.9 | 0.005 | 19/34 (CFPAC-1, A-172, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.585×** | -3.8 | 0.009 | 15/38 (BT-474, H4, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.590×** | -3.7 | 0.010 | 11/39 (LOX-IMVI, H4, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.704×** | -3.5 | 0.021 | 18/31 (A-172, HEC-1-A, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.618×** | -3.4 | 0.030 | 15/39 (LoVo, COLO 205, …) | two highest doses | position effect removed |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.413×** | -3.2 | 0.046 | 11/34 (COLO 205, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.418×** | -3.2 | 0.050 | 9/28 (A-172, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | **0.743×** | -2.9 | 0.095 | 6/36 (PANC-1, SW 900, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.45 per unit of S-phase module lfc, -0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16526. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 7.69 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0401× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0811× (z -8.8) |
| [[COLO 205 (line)]] | alt | 18.2 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0176× (z -14.8) ⚠ cell-cycle shift, explains ~35% of this change |
| [[CFPAC-1 (line)]] | alt | 3.75 | 0 | 2 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0510× (z -9.7) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.0661× (z -8.8) |
| [[LS 180 (line)]] | wt | 3.34 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0281× (z -11.1) |
| [[A-172 (line)]] | wt | 6.16 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0603× (z -10.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 4.55 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0259× (z -11.2) ⚠ cell-cycle shift, explains ~35% of this change |
| [[H4 (line)]] | wt | 5.80 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.0293× (z -8.5) ⚠ cell-cycle shift, explains ~44% of this change |
| [[HEC-1-A (line)]] | alt | 3.50 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0600× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[LOX-IMVI (line)]] | wt | 2.36 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.0382× (z -8.7) ⚠ cell-cycle shift, explains ~44% of this change |
| [[SW480 (line)]] | alt | 1.88 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0455× (z -9.8) |
| [[A-427 (line)]] | wt | 0.497 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.575 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.464 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.494 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.844 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.768 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.727 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.661 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16526), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF547]] | +0.72 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[RNF139-DT]] | +0.70 | +0.60 / +0.75 | both halves | 7e-06 |  |
| [[GABRR2]] | +0.70 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[LINC00672]] | +0.68 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[RRH]] | +0.67 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[GET1-SH3BGR]] | +0.67 | +0.60 / +0.76 | both halves | 7e-06 |  |
| [[LINC01772]] | +0.66 | +0.57 / +0.72 | both halves | 1e-05 |  |
| [[FLJ46284]] | +0.66 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[TEX29]] | +0.65 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[KLRA1P]] | +0.64 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[HAVCR2]] | +0.64 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[FAM209A]] | +0.64 | +0.54 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRTFB]] | -0.53 | -0.49 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C9]] | B | C9 activity raises METTL21EP-1's level | lines that do not express C9 (21) vs lines expressing it (29) | 1.44× lower at baseline in the lines without C9 | 0.043 | ⚠ within organs, on part of the lines; also absent: DAB2, ENSG00000253891, PTGFR |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FLJ46284]] | C | METTL21EP-1 activity raises FLJ46284's level | lines that do not express METTL21EP-1 (4) vs lines expressing it (46) | 2.66× lower at baseline in the lines without METTL21EP-1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CEMIP2, SMAD7, CASP4; maybe low, not absent; its own permutation p |
| [[ATP2A1]] | C | METTL21EP-1 activity lowers ATP2A1's level | lines that do not express METTL21EP-1 (4) vs lines expressing it (46) | 1.45× higher at baseline in the lines without METTL21EP-1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CEMIP2, SMAD7, CASP4; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.646). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.8, -18.2); signed map (12.5, 7.1). **Vector** length 65.3, 12.1% of its response variance represented; |z| ≥ 3 in 1,016 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.6 | +1.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.2 | +2.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +4.3 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +3.1 | +1.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.9 | +1.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.8 | +0.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.8 | +0.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | -0.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +4.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.7 | -7.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.6 | -2.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.6 | -11.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -9.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -0.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.6 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -3.9 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.5 | -1.0 |

## What is on record

> [!warning] No registry record
> METTL21EP-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16526: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16526); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16526, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16526]; `tensor/DDL_lfc|DDL_z.npy` [16526]; `embed/gene_vectors.npy` [16526]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16526 or target_col == 16526). Every well: [[METTL21EP-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/METTL21EP-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
