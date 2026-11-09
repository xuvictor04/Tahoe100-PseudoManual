---
symbol: "WDR45"
type: "gene"
col: 12317
ensembl_id: "ENSG00000196998"
name: "WD repeat domain 45"
location: "Xp11.23"
module: 35
arm: "+"
pooled_cpm: 12.62
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 12
n_dd_up_clean: 18
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# WDR45

*WD repeat domain 45* — Xp11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.16× (z +18.1, q 0e+00, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.524× (z -10.7, q 4e-24, down in 38 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Abemaciclib (drug)]] 5 µM: 0.539× (z -5.4, q 2e-05, down in 15 of 44 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATXN1L]] (+0.73, fdr 1e-05), [[TRIM8]] (+0.70, fdr 3e-05), [[ZFHX2-AS1]] (+0.67, fdr 2e-05); moves opposite to [[L2HGDH]] (-0.67, fdr 1e-05), [[MRPS34]] (-0.64, fdr 8e-05), [[ATG4C]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12317.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.16×** | +18.1 | 0e+00 | 42/47 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.46×** | +15.0 | 0e+00 | 31/36 (J82, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.17×** | +12.4 | 8e-33 | 20/24 (A549, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.16×** | +11.8 | 5e-30 | 23/31 (KATO III, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.00×** | +11.5 | 2e-28 | 34/46 (SW480, LoVo, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.55×** | +10.2 | 1e-22 | 34/48 (SW480, NCI-H2347, …) | rises with dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +5.9 | 3e-07 | 22/46 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +5.6 | 2e-06 | 19/46 (SW480, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +4.9 | 5e-05 | 14/40 (A-172, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.34×** | +4.8 | 9e-05 | 20/46 (NCI-H1573, HS-578T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.29×** | +4.2 | 0.001 | 10/47 (A498, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.28×** | +4.1 | 0.002 | 11/47 (KATO III, HT-29, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.40×** | +4.0 | 0.003 | 10/42 (NCI-H1792, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.27×** | +3.8 | 0.005 | 10/45 (LoVo, LS 180, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.24×** | +3.6 | 0.011 | 4/45 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[4EGI-1 (drug)]] 5 µM |  | **1.50×** | +3.5 | 0.014 | 3/42 (SHP-77, HS-578T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.016 | 12/47 (KATO III, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.036 | 5/44 (LOX-IMVI, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.038 | 9/43 (A498, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12317.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.524×** | -10.7 | 4e-24 | 38/47 (KATO III, MIA PaCa-2, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.539×** | -5.4 | 2e-05 | 15/44 (SK-MEL-2, HT-29, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.643×** | -5.2 | 3e-05 | 16/48 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.576×** | -4.8 | 2e-04 | 18/43 (SW 900, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.828×** | -4.4 | 0.001 | 13/48 (KATO III, RKO, …) | rises with dose |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.758×** | -4.4 | 0.001 | 10/46 (PANC-1, NCI-H1792, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.780×** | -4.1 | 0.003 | 10/47 (KATO III, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~8% here); position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.635×** | -3.9 | 0.006 | 7/44 (HepG2/C3A, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.720×** | -3.9 | 0.006 | 10/46 (NCI-H1792, SW 900, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.814×** | -3.4 | 0.034 | 15/45 (KATO III, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.682×** | -3.3 | 0.045 | 9/43 (NCI-H23, A549, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.825×** | -3.2 | 0.067 | 7/47 (BT-474, KATO III, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12317. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 17.3 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.37× (z +12.1) | — |
| [[A498 (line)]] | wt | 6.55 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +8.5) | — |
| [[C-33 A (line)]] | alt | 9.98 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.102× (z -8.7) ⚠ toxic; unreliable plate only |
| [[HCT15 (line)]] | alt | 15.8 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.146× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 10.5 | 0 | 1 | — | [[Thymopentin (drug)]] 0.05 µM 0.0969× (z -8.6) |
| [[J82 (line)]] | alt | 14.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +8.8) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 14.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.99× (z +10.3) | — |
| [[NCI-H2347 (line)]] | alt | 12.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +10.2) | — |
| [[NCI-H460 (line)]] | wt | 11.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +8.5) | — |
| [[A-172 (line)]] | wt | 9.70 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.86 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.77 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.48 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.43 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12317), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATXN1L]] | +0.73 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[TRIM8]] | +0.70 | +0.45 / +0.67 | both halves | 3e-05 |  |
| [[ZFHX2-AS1]] | +0.67 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[CPEB2-DT]] | +0.67 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[QRICH2]] | +0.66 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[PPP1R12A-AS2]] | +0.66 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[SIAH2-AS1]] | +0.66 | +0.60 / +0.42 | both halves | 4e-05 |  |
| [[BCL10-AS1]] | +0.65 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[LINC01090]] | +0.65 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[INTS6-AS1]] | +0.65 | +0.64 / +0.39 | both halves | 5e-05 |  |
| [[TMEM202-AS1]] | +0.65 | +0.64 / +0.44 | both halves | 3e-05 |  |
| [[FAM174B]] | +0.65 | +0.53 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[L2HGDH]] | -0.67 | -0.64 / -0.54 | both halves | 1e-05 |  |
| [[MRPS34]] | -0.64 | -0.61 / -0.37 | both halves | 8e-05 |  |
| [[ATG4C]] | -0.63 | -0.53 / -0.52 | both halves | 1e-05 | pathway: Autophagy; STRING 414 |
| [[SYBU]] | -0.60 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[ATP5MC3]] ⚠ | -0.58 | -0.33 / -0.57 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[POT1]] | -0.57 | -0.55 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers WDR45's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises WDR45's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.637). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (9.6, 11.3); signed map (19.6, -8.1). **Vector** length 78.2, 13.9% of its response variance represented; |z| ≥ 3 in 824 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +18.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.6 | +12.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.4 | +15.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.3 | +11.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.0 | +11.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.2 | +10.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.3 | +4.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.2 | +4.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.8 | +3.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.9 | -10.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.7 | -3.9 |
|  | [[EX229 (drug)]] 5 µM |  | -3.6 | -4.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.4 | -3.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.4 | -5.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.4 | -5.4 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 45 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.23 — chrX:49,074,433-49,101,170 (-) |
| Ensembl biotype | protein_coding |
| Also known as | JM5, WIPI4, NBIA5; previously WDRX1 |
| Gene groups (HGNC) | WD repeat domain containing; WIPI family |
| Reactome | 2 pathways, smallest: Macroautophagy; Autophagy |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y484](https://www.uniprot.org/uniprotkb/Q9Y484) (WD repeat domain phosphoinositide-interacting protein 4):

> Component of the autophagy machinery that controls the major intracellular degradation process by which cytoplasmic materials are packaged into autophagosomes and delivered to lysosomes for degradation. Binds phosphatidylinositol 3-phosphate (PtdIns3P). Activated by the STK11/AMPK signaling pathway upon starvation, WDR45 is involved in autophagosome assembly downstream of WIPI2, regulating the size of forming autophagosomes. Together with WIPI1, promotes ATG2 (ATG2A or ATG2B)-mediated lipid …

**Summary**, from NCBI Gene [11152](https://www.ncbi.nlm.nih.gov/gene/11152):

> This gene encodes a member of the WD repeat protein family. WD repeats are minimally conserved regions of approximately 40 amino acids typically bracketed by gly-his and trp-asp (GH-WD), which may facilitate formation of heterotrimeric or multiprotein complexes. Members of this family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis, and gene regulation. This gene has a pseudogene at chromosome 4q31.3. Multiple alternatively …

**Accessions** — [HGNC:28912](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28912) · Entrez [11152](https://www.ncbi.nlm.nih.gov/gene/11152) · UniProt [Q9Y484](https://www.uniprot.org/uniprotkb/Q9Y484) · Ensembl [ENSG00000196998](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196998)

## Data

Gene col 12317: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12317); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12317, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12317]; `tensor/DDL_lfc|DDL_z.npy` [12317]; `embed/gene_vectors.npy` [12317]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12317 or target_col == 12317). Every well: [[WDR45 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR45.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
