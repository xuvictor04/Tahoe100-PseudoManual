---
symbol: "SLC2A4RG"
type: "gene"
col: 4628
ensembl_id: "ENSG00000125520"
name: "SLC2A4 regulator"
location: "20q13.33"
module: 94
arm: "+"
pooled_cpm: 23.01
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 13
n_dd_up_clean: 9
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/094"]
generated_by: "tahoemap"
---

# SLC2A4RG

*SLC2A4 regulator* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.03× (z +12.1, q 6e-31, up in 39 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.53× (z +6.6, q 6e-09, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.557× (z -6.0, q 1e-06, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC44A2]] (+0.68, fdr 1e-05), [[TRPM4]] (+0.67, fdr 7e-06), [[DUSP15]] (+0.59, fdr 3e-05); moves opposite to [[TXN]] (-0.49, fdr 3e-05), [[CCT6A]] (-0.48, fdr 9e-05), [[PRDX1]] (-0.46, fdr 6e-05).
> It is in [[Module 094]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NGFR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4628.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.03×** | +12.1 | 6e-31 | 39/39 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.88×** | +11.1 | 4e-26 | 26/30 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.02×** | +7.1 | 3e-10 | 26/34 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.53×** | +6.6 | 6e-09 | 34/48 (NCI-H2030, LoVo, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.70×** | +5.8 | 7e-07 | 34/45 (SW1417, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.70×** | +5.8 | 7e-07 | 37/48 (NCI-H1792, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.60×** | +5.1 | 3e-05 | 34/47 (LoVo, C-33 A, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.58×** | +5.0 | 4e-05 | 27/48 (SHP-77, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.83×** | +4.5 | 4e-04 | 31/45 (Panc 03.27, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.64×** | +3.7 | 0.012 | 21/48 (PANC-1, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.62×** | +3.6 | 0.017 | 20/48 (SW1417, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.37×** | +3.4 | 0.029 | 18/45 (Hs 766T, CFPAC-1, …) | two highest doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.54×** | +3.2 | 0.060 | 18/44 (J82, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +3.1 | 0.092 | 4/48 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4628.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.557×** | -6.0 | 1e-06 | 30/48 (HT-29, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.638×** | -4.9 | 3e-04 | 29/48 (J82, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.672×** | -4.3 | 0.002 | 26/48 (Hs 766T, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.674×** | -4.3 | 0.002 | 26/47 (BT-474, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.681×** | -4.2 | 0.003 | 23/47 (NCI-H2030, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.683×** | -4.1 | 0.003 | 24/47 (H4, HT-29, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.685×** | -4.1 | 0.003 | 23/48 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.709×** | -3.7 | 0.013 | 23/47 (NCI-H2030, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.796×** | -3.5 | 0.027 | 21/47 (Panc 03.27, J82, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.727×** | -3.5 | 0.029 | 18/48 (C-33 A, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.746×** | -3.2 | 0.072 | 18/48 (J82, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.736×** | -3.1 | 0.096 | 14/47 (NCI-H23, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.755×** | -3.1 | 0.096 | 19/47 (BT-474, SW48, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4628. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 34.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +12.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A498 (line)]] | wt | 35.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +10.3) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 25.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.20× (z +10.4) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 31.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +11.1) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 16.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.64× (z +11.6) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 18.0 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.118× (z -8.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HOP62 (line)]] | alt | 24.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +8.7) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 34.8 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.257× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 18.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.44× (z +12.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H1573 (line)]] | alt | 11.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.63× (z +10.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 23.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H661 (line)]] | alt | 60.0 | 0 | 1 | — | [[Doxycycline (monohydrate) (drug)]] 0.05 µM 0.0885× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 47.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -9.0) ⚠ cell-cycle shift, explains ~20% of this change |
| [[A-427 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 45.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.15 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4628), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC44A2]] | +0.68 | +0.53 / +0.71 | both halves | 1e-05 |  |
| [[TRPM4]] | +0.67 | +0.58 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[DUSP15]] | +0.59 | +0.45 / +0.69 | both halves | 3e-05 |  |
| [[PCCA]] | +0.58 | +0.26 / +0.66 | both halves | 4e-04 |  |
| [[NUDT16]] | +0.55 | +0.38 / +0.68 | both halves | 6e-05 |  |
| [[DCXR]] | +0.54 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[ZNF44]] | +0.54 | +0.44 / +0.71 | both halves | 3e-05 | same gene group |
| [[GALT]] | +0.53 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[CCDC24]] | +0.52 | +0.59 / +0.46 | both halves | 2e-05 |  |
| [[ANKRD54]] | +0.52 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[PER1]] | +0.52 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[OGA]] | +0.52 | +0.27 / +0.64 | both halves | 3e-04 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXN]] | -0.49 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[CCT6A]] | -0.48 | -0.36 / -0.54 | both halves | 9e-05 |  |
| [[PRDX1]] | -0.46 | -0.53 / -0.38 | both halves | 6e-05 |  |
| [[TMEM11-DT]] | -0.44 | -0.32 / -0.42 | both halves | 2e-04 |  |
| [[PRMT3]] | -0.44 | -0.38 / -0.43 | both halves | 7e-05 | same gene group |
| [[CCT3]] | -0.43 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[HSPA8]] | -0.42 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[AP4B1]] | -0.41 | -0.36 / -0.50 | both halves | 1e-04 |  |
| [[MCM9]] | -0.41 | -0.39 / -0.36 | both halves | 1e-04 |  |
| [[L3HYPDH]] | -0.41 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[ADORA2B]] | -0.41 | -0.30 / -0.39 | both halves | 2e-04 |  |
| [[CCT4]] | -0.41 | -0.43 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NGFR]] | B | NGFR activity raises SLC2A4RG's level | lines that do not express NGFR (19) vs lines expressing it (31) | 1.52× lower at baseline in the lines without NGFR | 0.072 | ⚠ within organs, on part of the lines; also absent: ZNF829, ZNF568, GNG11 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 094]]; 49 genes; every member is in the + arm (projection on the module's main direction 0.525). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-23.3, 25.2); signed map (14.8, -16.0). **Vector** length 82.4, 19.8% of its response variance represented; |z| ≥ 3 in 786 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.5 | +6.6 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +5.7 | +5.0 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +4.5 | +5.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +1.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.6 | +0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +4.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.8 | +5.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.7 | +2.8 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.2 | +2.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.8 | +0.6 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -3.5 | -6.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -2.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -3.4 | -3.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.1 | -3.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.1 | -1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -3.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.6 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | SLC2A4 regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:63,739,776-63,744,050 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GLUT4EF, GEF, HDBP1, Si-1-2, Si-1-2-19 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NR83](https://www.uniprot.org/uniprotkb/Q9NR83) (SLC2A4 regulator):

> Transcription factor involved in SLC2A4 and HD gene transactivation. Binds to the consensus sequence 5'-GCCGGCG-3'.

**Summary**, from NCBI Gene [56731](https://www.ncbi.nlm.nih.gov/gene/56731):

> The protein encoded by this gene is a nuclear transcription factor involved in the activation of the solute carrier family 2 member 4 gene. The encoded protein interacts with another transcription factor, myocyte enhancer factor 2, to activate transcription of this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:15930](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15930) · Entrez [56731](https://www.ncbi.nlm.nih.gov/gene/56731) · UniProt [Q9NR83](https://www.uniprot.org/uniprotkb/Q9NR83) · Ensembl [ENSG00000125520](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125520)

## Data

Gene col 4628: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4628); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4628, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4628]; `tensor/DDL_lfc|DDL_z.npy` [4628]; `embed/gene_vectors.npy` [4628]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4628 or target_col == 4628). Every well: [[SLC2A4RG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC2A4RG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
