---
symbol: "ORMDL1"
type: "gene"
col: 4914
ensembl_id: "ENSG00000128699"
name: "ORMDL sphingolipid biosynthesis regulator 1"
location: "2q32.2"
module: 15
arm: "+"
pooled_cpm: 35.5
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 3
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# ORMDL1

*ORMDL sphingolipid biosynthesis regulator 1* — 2q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.40× (z +12.1, q 5e-31, up in 41 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.57× (z +8.8, q 2e-16, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.697× (z -7.1, q 6e-10, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MFSD8]] (+0.64, fdr 1e-05), [[PLPP5]] (+0.63, fdr 1e-05), [[C14orf28]] (+0.61, fdr 2e-05); moves opposite to [[C15orf39]] (-0.56, fdr 3e-05), [[MAP3K14]] (-0.55, fdr 6e-05), [[CCDC57]] (-0.54, fdr 5e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4914.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.40×** | +12.1 | 5e-31 | 41/45 (HOP62, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.39×** | +11.6 | 1e-28 | 33/35 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +8.8 | 2e-16 | 42/48 (HS-578T, A-172, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.93×** | +8.4 | 6e-15 | 34/42 (A-172, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +6.4 | 1e-08 | 39/47 (HepG2/C3A, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +5.1 | 3e-05 | 35/47 (RKO, HOP62, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +5.0 | 4e-05 | 34/48 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +3.8 | 0.011 | 24/48 (NCI-H23, NCI-H2030, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~24% of this change | **1.30×** | +3.6 | 0.019 | 21/46 (HOP62, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.27×** | +3.3 | 0.061 | 19/47 (C32, J82, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4914.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.697×** | -7.1 | 6e-10 | 36/47 (A-427, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.362×** | -6.2 | 2e-07 | 40/47 (C32, SW 900, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.899× | -5.0 | 1e-04 | 6/48 (NCI-H2347, SNU-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.482×** | -4.4 | 0.001 | 26/48 (SNU-1, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.788× | -3.1 | 0.19 | 17/47 (HEC-1-A, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4914. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 37.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.79× (z +12.5) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 49.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.206× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.428× (z -9.6) |
| [[A498 (line)]] | wt | 51.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +9.5) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 34.7 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -9.6) |
| [[PANC-1 (line)]] | alt | 34.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.34× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.548× (z -8.6) |
| [[SNU-1 (line)]] | wt | 44.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0662× (z -19.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0594× (z -8.8) |
| [[SNU-423 (line)]] | alt | 25.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.95× (z +10.2) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 44.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.20× (z +12.8) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 32.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -14.3) |
| [[CFPAC-1 (line)]] | alt | 28.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +8.9) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 31.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +8.9) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 36.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.76× (z +11.1) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 32.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.30× (z +8.5) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 43.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.91× (z +8.8) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 27.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 26.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.04× (z +10.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 38.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 40.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -9.3) |
| [[A549 (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4914), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFSD8]] | +0.64 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[PLPP5]] | +0.63 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[C14orf28]] | +0.61 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[LSM8]] | +0.59 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[TAF12]] | +0.58 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[CLCC1]] | +0.58 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[BCL2L2-PABPN1]] | +0.57 | +0.49 / +0.41 | both halves | 4e-05 |  |
| [[CIAO2A]] | +0.57 | +0.44 / +0.41 | both halves | 4e-05 |  |
| [[SLC49A4]] | +0.56 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[VPS13B-DT]] | +0.56 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[EEF1AKMT3]] | +0.55 | +0.48 / +0.37 | both halves | 7e-05 |  |
| [[ISCU]] | +0.55 | +0.47 / +0.54 | both halves | 2e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C15orf39]] | -0.56 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[MAP3K14]] | -0.55 | -0.45 / -0.39 | both halves | 6e-05 |  |
| [[CCDC57]] | -0.54 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[ZKSCAN2]] | -0.53 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[H2AX]] | -0.53 | -0.39 / -0.56 | both halves | 6e-05 |  |
| [[RALY]] | -0.53 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[EPPK1]] | -0.53 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[NR4A1]] | -0.52 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[ATP8B3]] | -0.51 | -0.43 / -0.40 | both halves | 4e-05 |  |
| [[ZNF628]] | -0.51 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[SERBP1]] | -0.51 | -0.31 / -0.48 | both halves | 2e-04 |  |
| [[TAF1B]] | -0.50 | -0.32 / -0.46 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ORMDL1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[FSD1]] | B | FSD1 activity raises ORMDL1's level | lines that do not express FSD1 (17) vs lines expressing it (33) | 1.17× lower at baseline in the lines without FSD1 | 0.077 | ⚠ within organs, on part of the lines; also absent: RFLNB, B4GALNT1, NTNG2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.586). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-14.0, 21.5); signed map (0.1, 2.1). **Vector** length 61.8, 12.7% of its response variance represented; |z| ≥ 3 in 610 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +5.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +8.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +5.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | +2.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.6 | +1.4 |
|  | [[Terfenadine (drug)]] 5 µM |  | +1.6 | +1.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.5 | +1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | +1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.3 | +1.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.3 | +0.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.7 | -7.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -0.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.9 | -4.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -1.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -0.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.7 | -1.0 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -1.3 | -0.5 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -1.3 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | ORMDL sphingolipid biosynthesis regulator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q32.2 — chr2:189,770,267-189,784,364 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | ORMDL sphingolipid biosynthesis regulators |
| Reactome | 3 pathways, smallest: Sphingolipid de novo biosynthesis; Sphingolipid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P0S3](https://www.uniprot.org/uniprotkb/Q9P0S3) (ORM1-like protein 1):

> Plays an essential role in the homeostatic regulation of sphingolipid de novo biosynthesis by modulating the activity of the serine palmitoyltransferase (SPT) in response to ceramide levels. When complexed to SPT, the binding of ceramides to its N-terminus stabilizes a conformation that block SPT substrate entry, hence preventing SPT catalytic activity. Through this mechanism, maintains ceramide levels at sufficient concentrations for the production of complex sphingolipids, but which prevents …

**Summary**, from NCBI Gene [94101](https://www.ncbi.nlm.nih.gov/gene/94101):

> Involved in ceramide metabolic process. Acts upstream of or within negative regulation of ceramide biosynthetic process. Located in endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16036](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16036) · Entrez [94101](https://www.ncbi.nlm.nih.gov/gene/94101) · UniProt [Q9P0S3](https://www.uniprot.org/uniprotkb/Q9P0S3) · Ensembl [ENSG00000128699](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128699)

## Data

Gene col 4914: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4914); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4914, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4914]; `tensor/DDL_lfc|DDL_z.npy` [4914]; `embed/gene_vectors.npy` [4914]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4914 or target_col == 4914). Every well: [[ORMDL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ORMDL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
