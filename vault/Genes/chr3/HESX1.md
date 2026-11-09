---
symbol: "HESX1"
type: "gene"
col: 8749
ensembl_id: "ENSG00000163666"
name: "HESX homeobox 1"
location: "3p14.3"
module: 35
arm: "+"
pooled_cpm: 3.36
n_lines_expressing: 49
n_dd_up: 19
n_dd_down: 22
n_dd_up_clean: 16
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# HESX1

*HESX homeobox 1* — 3p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.32× (z +18.8, q 0e+00, up in 29 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.363× (z -11.2, q 2e-26, down in 31 of 45 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PJVK]] (+0.58, fdr 2e-05), [[DNAI1]] (+0.58, fdr 7e-06), [[PRRT1]] (+0.57, fdr 2e-05); moves opposite to [[CLEC16A]] (-0.43, fdr 0.007, ⚠ not reproduced), [[MRPL28]] (-0.43, fdr 3e-04).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC02609]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8749.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.32×** | +18.8 | 0e+00 | 29/35 (HEC-1-A, A-172, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.62×** | +10.7 | 3e-24 | 32/45 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.34×** | +9.5 | 6e-19 | 28/43 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.80×** | +9.2 | 5e-18 | 31/43 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.73×** | +8.7 | 6e-16 | 19/35 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.04×** | +7.9 | 2e-13 | 28/44 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.00×** | +7.7 | 9e-13 | 26/44 (HOP62, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.89×** | +6.6 | 3e-09 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.78×** | +6.4 | 8e-09 | 20/40 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.70×** | +5.9 | 2e-07 | 12/44 (KATO III, NCI-H1792, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.38×** | +5.1 | 2e-05 | 7/44 (SW48, C-33 A, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.49×** | +4.4 | 4e-04 | 6/40 (SW48, KATO III, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.45×** | +4.2 | 0.001 | 7/33 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.00×** | +4.0 | 0.002 | 6/39 (SW480, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.41×** | +3.8 | 0.005 | 9/41 (H4, NCI-H460, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | **1.36×** | +3.4 | 0.022 | 3/41 (COLO 205, LoVo, …) | all doses, flat |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.041 | 5/44 (SW480, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8749.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.363×** | -11.2 | 2e-26 | 31/45 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.434×** | -9.2 | 7e-18 | 31/43 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.496×** | -7.8 | 2e-12 | 21/40 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.595×** | -5.7 | 1e-06 | 13/43 (A498, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.603×** | -5.6 | 2e-06 | 14/30 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.604×** | -5.6 | 2e-06 | 17/44 (PANC-1, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.628×** | -5.1 | 2e-05 | 11/43 (A-172, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.630×** | -4.8 | 1e-04 | 12/21 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.677×** | -4.3 | 0.001 | 8/45 (HS-578T, SW480, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.694×** | -4.0 | 0.003 | 11/44 (A-427, RPMI-7951, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.513×** | -3.9 | 0.006 | 8/38 (A-172, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.699×** | -3.7 | 0.011 | 11/39 (PANC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.539×** | -3.6 | 0.015 | 8/40 (PANC-1, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.801×** | -3.5 | 0.022 | 9/43 (CFPAC-1, AN3 CA, …) | rises with dose |  |
| [[Clopidogrel (drug)]] 0.05 µM |  | **0.748×** | -3.2 | 0.049 | 3/43 (HOP62, A-172, …) | inconsistent across doses | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **0.738×** | -3.1 | 0.061 | 10/40 (SW1417, COLO 205, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.588×** | -3.1 | 0.071 | 10/30 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.749×** | -3.0 | 0.091 | 7/44 (AN3 CA, CHP-212, …) | top dose only | plate-row cell shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.767×** | -2.9 | 0.097 | 9/44 (A498, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8749. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 6.24 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0219× (z -22.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.115× (z -12.7) |
| [[HEC-1-A (line)]] | alt | 5.34 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.71× (z +12.8) | [[Clofarabine (drug)]] 5 µM 0.146× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 5.83 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0785× (z -10.2) |
| [[SW480 (line)]] | alt | 4.80 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.136× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.142× (z -10.6) |
| [[A-427 (line)]] | wt | 5.98 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.137× (z -8.6) ⚠ cell-cycle shift, explains ~42% of this change |
| [[HCT15 (line)]] | alt | 3.72 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.8× (z +8.5) | — |
| [[LoVo (line)]] | wt | 2.58 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +11.8) | — |
| [[NCI-H460 (line)]] | wt | 2.23 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.90× (z +9.0) | — |
| [[A-172 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.744 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.964 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.90 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.42 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8749), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PJVK]] | +0.58 | +0.75 / +0.48 | both halves | 2e-05 |  |
| [[DNAI1]] | +0.58 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[PRRT1]] | +0.57 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[ASB14]] | +0.54 | +0.68 / +0.42 | both halves | 4e-05 | ⚠ same locus (40.7 kb, same strand: neighbours can correlate without regulation) |
| [[RYR1]] | +0.54 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[GAPLINC]] | +0.54 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[MEIOC]] | +0.54 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[C2CD5-AS1]] | +0.53 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[DEPDC4]] | +0.53 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[LRRC36]] | +0.52 | +0.46 / +0.50 | both halves | 2e-05 |  |
| [[EFHD1]] | +0.52 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[PPEF1]] | +0.52 | +0.62 / +0.44 | both halves | 3e-05 |  |
| [[GPLD1]] | +0.51 | +0.61 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLEC16A]] | -0.43 | -0.02 / -0.32 | ⚠ not reproduced | 0.007 |  |
| [[MRPL28]] | -0.43 | -0.28 / -0.47 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02609]] | B | LINC02609 activity raises HESX1's level | lines that do not express LINC02609 (6) vs lines expressing it (44) | 1.48× lower at baseline in the lines without LINC02609 | 0.085 | ⚠ within organs, on part of the lines; also absent: TPST1, HLTF, FERMT2; maybe low, not absent |
| [[TLCD3B]] | B | TLCD3B activity raises HESX1's level | lines that do not express TLCD3B (5) vs lines expressing it (45) | 1.66× lower at baseline in the lines without TLCD3B | 0.097 | ⚠ within organs, on part of the lines; also absent: NECAB2, SHMT1, TMCC1-DT; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.447). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (11.0, 31.6); signed map (24.8, 16.1). **Vector** length 43.3, 4.89% of its response variance represented; |z| ≥ 3 in 1,057 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.7 | +8.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +18.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.8 | +6.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.2 | +3.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.3 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.1 | +2.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.9 | +0.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +0.9 | +1.7 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.7 | -11.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | -9.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.2 | -4.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.1 | -5.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.9 | -7.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.7 | -3.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.1 | -3.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.0 | -2.7 |
|  | [[Malotilate (drug)]] 0.05 µM |  | -1.0 | -2.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.0 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | HESX homeobox 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p14.3 — chr3:57,197,838-57,227,606 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RPX, ANF |
| Gene groups (HGNC) | PRD class homeoboxes and pseudogenes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBX0](https://www.uniprot.org/uniprotkb/Q9UBX0) (Homeobox expressed in ES cells 1):

> Required for the normal development of the forebrain, eyes and other anterior structures such as the olfactory placodes and pituitary gland. Possible transcriptional repressor. Binds to the palindromic PIII sequence, 5'-AGCTTGAGTCTAATTGAATTAACTGTAC-3'. HESX1 and PROP1 bind as heterodimers on this palindromic site, and, in vitro, HESX1 can antagonize PROP1 activation.

**Summary**, from NCBI Gene [8820](https://www.ncbi.nlm.nih.gov/gene/8820):

> This gene encodes a conserved homeobox protein that is a transcriptional repressor in the developing forebrain and pituitary gland. Mutations in this gene are associated with septooptic dysplasia, HESX1-related growth hormone deficiency, and combined pituitary hormone deficiency. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4877](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4877) · Entrez [8820](https://www.ncbi.nlm.nih.gov/gene/8820) · UniProt [Q9UBX0](https://www.uniprot.org/uniprotkb/Q9UBX0) · Ensembl [ENSG00000163666](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163666)

## Data

Gene col 8749: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8749); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8749, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8749]; `tensor/DDL_lfc|DDL_z.npy` [8749]; `embed/gene_vectors.npy` [8749]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8749 or target_col == 8749). Every well: [[HESX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HESX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
