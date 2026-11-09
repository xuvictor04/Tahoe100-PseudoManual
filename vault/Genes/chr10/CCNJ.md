---
symbol: "CCNJ"
type: "gene"
col: 2852
ensembl_id: "ENSG00000107443"
name: "cyclin J"
location: "10q24.1"
module: 5
arm: "+"
pooled_cpm: 10.84
n_lines_expressing: 50
n_dd_up: 35
n_dd_down: 4
n_dd_up_clean: 27
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# CCNJ

*cyclin J* — 10q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.51× (z +21.1, q 0e+00, up in 42 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.809× (z -4.9, q 5e-04, down in 19 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRM1]] (+0.72, fdr 1e-05), [[PIGW]] (+0.70, fdr 1e-05), [[ZNF142]] (+0.67, fdr 7e-06); moves opposite to [[SPAG9]] (-0.61, fdr 2e-05), [[GNG7]] (-0.59, fdr 4e-05), [[ALAD]] (-0.58, fdr 5e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2852.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.51×** | +21.1 | 0e+00 | 42/43 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.83×** | +9.8 | 3e-20 | 39/47 (NCI-H460, NCI-H1792, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +8.8 | 2e-16 | 27/44 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +7.9 | 3e-13 | 25/40 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.57×** | +7.3 | 4e-11 | 24/46 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.54×** | +7.0 | 3e-10 | 24/47 (SW480, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.26×** | +6.9 | 3e-10 | 20/43 (C32, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.50×** | +6.6 | 3e-09 | 21/43 (CFPAC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.52×** | +6.5 | 4e-09 | 20/45 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.49×** | +6.4 | 7e-09 | 21/47 (CFPAC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +6.4 | 7e-09 | 23/46 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.49×** | +6.4 | 7e-09 | 22/47 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +6.2 | 2e-08 | 20/40 (HepG2/C3A, RKO, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.02×** | +6.0 | 9e-08 | 20/46 (SW480, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.29×** | +5.8 | 2e-07 | 19/46 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.46×** | +5.8 | 3e-07 | 16/45 (SW48, SW480, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.41×** | +5.3 | 5e-06 | 14/44 (SNU-423, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.79×** | +4.9 | 2e-05 | 9/40 (MIA PaCa-2, A-427, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2852.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.809×** | -4.9 | 5e-04 | 19/47 (SHP-77, C-33 A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.748×** | -4.8 | 5e-04 | 16/47 (RKO, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.771×** | -4.3 | 0.004 | 16/36 (LoVo, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **0.663×** | -3.5 | 0.061 | 8/47 (AN3 CA, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Furosemide (drug)]] 0.5 µM |  | 0.818× | -3.3 | 0.11 | 9/46 (NCI-H661, SW 900, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.869× | -3.2 | 0.14 | 10/47 (SW480, SW48, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.828× | -3.1 | 0.15 | 13/45 (SW480, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.834× | -3.0 | 0.19 | 15/47 (C-33 A, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2852. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 13.8 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.173× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 15.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +8.6) | — |
| [[RKO (line)]] | wt | 31.8 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.194× (z -11.6) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.307× (z -8.7) |
| [[SW480 (line)]] | alt | 13.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.171× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 13.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -11.0) |
| [[AN3 CA (line)]] | alt | 46.6 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0917× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 5.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.51× (z +9.1) | — |
| [[HOP62 (line)]] | alt | 8.47 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +9.4) | — |
| [[Hs 766T (line)]] | wt | 6.10 | 0 | 1 | — | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM 0.0837× (z -9.2) |
| [[HS-578T (line)]] | alt | 5.81 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0849× (z -9.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 4.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.35× (z +9.8) | — |
| [[LoVo (line)]] | wt | 12.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -12.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 11.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.82× (z +11.4) | — |
| [[NCI-H1792 (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.176× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 16.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +9.3) | — |
| [[A-427 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.32 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.45 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.75 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2852), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRM1]] | +0.72 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[PIGW]] | +0.70 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[ZNF142]] | +0.67 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[ZNF746]] | +0.67 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[TLCD3A]] | +0.66 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[KLHL42]] | +0.65 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[UBTF]] | +0.64 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[JADE3]] | +0.64 | +0.64 / +0.45 | both halves | 3e-05 |  |
| [[E2F3]] | +0.64 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[TOR1A]] | +0.63 | +0.59 / +0.42 | both halves | 4e-05 |  |
| [[PTPN9]] | +0.63 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[BEND3]] | +0.63 | +0.63 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPAG9]] | -0.61 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[GNG7]] | -0.59 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[ALAD]] | -0.58 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[MOSPD2]] | -0.58 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[EFHC1]] | -0.57 | -0.55 / -0.31 | both halves | 2e-04 |  |
| [[TBC1D17]] | -0.56 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[IFT172]] | -0.56 | -0.51 / -0.28 | both halves | 3e-04 |  |
| [[MAP3K13]] | -0.55 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[NBEAL1]] | -0.55 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[HDAC5]] | -0.55 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[LMTK3]] | -0.54 | -0.36 / -0.38 | both halves | 1e-04 |  |
| [[UBE2B]] | -0.54 | -0.49 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises CCNJ's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[KCTD15]] | B | KCTD15 activity raises CCNJ's level | lines that do not express KCTD15 (7) vs lines expressing it (43) | 1.58× lower at baseline in the lines without KCTD15 | 0.087 | ⚠ within organs, on part of the lines; also absent: EGFL7, SEPTIN3, EEF1A2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.644). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-5.8, 10.7); signed map (24.3, -29.3). **Vector** length 80.8, 14.8% of its response variance represented; |z| ≥ 3 in 939 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.6 | +21.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.1 | +9.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.1 | +7.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +8.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +4.1 | +6.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.2 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +2.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.2 | +5.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.2 | +4.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.1 | +3.8 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.3 | -3.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.3 | -4.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | -2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.5 | -1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | cyclin J |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.1 — chr10:96,043,394-96,060,870 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10895, bA690P14.1 |
| Gene groups (HGNC) | Cyclins |
| Matched by | ensembl_id |

UniProt [Q5T5M9](https://www.uniprot.org/uniprotkb/Q5T5M9) carries no function annotation.

**Summary**, from NCBI Gene [54619](https://www.ncbi.nlm.nih.gov/gene/54619):

> Predicted to enable cyclin-dependent protein serine/threonine kinase regulator activity. Predicted to be involved in G1/S transition of mitotic cell cycle. Predicted to be part of cyclin-dependent protein kinase holoenzyme complex. Predicted to be active in cytoplasm; microtubule organizing center; and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23434](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23434) · Entrez [54619](https://www.ncbi.nlm.nih.gov/gene/54619) · UniProt [Q5T5M9](https://www.uniprot.org/uniprotkb/Q5T5M9) · Ensembl [ENSG00000107443](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107443)

## Data

Gene col 2852: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2852); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2852, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2852]; `tensor/DDL_lfc|DDL_z.npy` [2852]; `embed/gene_vectors.npy` [2852]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2852 or target_col == 2852). Every well: [[CCNJ — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCNJ.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
