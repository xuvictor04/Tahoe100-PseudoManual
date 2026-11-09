---
symbol: "TAF9B"
type: "gene"
col: 11910
ensembl_id: "ENSG00000187325"
name: "TATA-box binding protein associated factor 9b"
location: "Xq21.1"
module: 77
arm: "-"
pooled_cpm: 5.95
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 2
n_dd_up_clean: 13
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# TAF9B

*TATA-box binding protein associated factor 9b* — Xq21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.84× (z +21.3, q 0e+00, up in 23 of 24 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.76× (z +19.4, q 0e+00, up in 36 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.706× (z -4.7, q 0.001, down in 14 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Saquinavir (drug)]] 0.5 µM in 1 line (SW480 0.214×); [[Pravastatin (sodium) (drug)]] 0.05 µM in 1 line (RKO 0.0840×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (A549 0.107×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZBED5-AS1]] (+0.73, fdr 1e-05), [[CYB5D2]] (+0.72, fdr 2e-05), [[MED12]] (+0.70, fdr 1e-05); moves opposite to [[SDHAF1]] (-0.68, fdr 1e-05), [[TRIM11]] (-0.64, fdr 3e-05), [[SMYD4]] (-0.64, fdr 2e-05).
> It sits in the **-** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MYEF2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11910.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.84×** | +21.3 | 0e+00 | 23/24 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.86×** | +20.5 | 0e+00 | 11/12 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.76×** | +19.4 | 0e+00 | 36/41 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.19×** | +14.5 | 3e-45 | 16/16 (J82, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.61×** | +12.9 | 3e-36 | 29/37 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.08×** | +9.5 | 2e-19 | 29/44 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +8.5 | 2e-15 | 23/41 (NCI-H2347, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +8.2 | 2e-14 | 18/30 (NCI-H2030, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.77×** | +7.7 | 1e-12 | 22/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +7.6 | 2e-12 | 21/40 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.71×** | +7.2 | 3e-11 | 15/30 (HOP62, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +6.6 | 2e-09 | 19/34 (J82, A-427, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.59×** | +6.3 | 2e-08 | 17/45 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.38×** | +6.1 | 4e-08 | 5/15 (NCI-H2347, A549, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +5.8 | 2e-07 | 18/45 (SW480, A-172, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.6 | 1e-04 | 13/41 (A-172, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.38×** | +4.4 | 4e-04 | 8/45 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.37×** | +4.3 | 6e-04 | 10/44 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.33×** | +3.7 | 0.006 | 12/46 (PANC-1, LoVo, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.55×** | +3.1 | 0.058 | 1/43 (MIA PaCa-2) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Nevirapine (drug)]] 0.05 µM |  | **1.28×** | +3.0 | 0.063 | 2/43 (LS 180, SNU-423) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11910.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Saquinavir (drug)]] 0.5 µM in 1 line (SW480 0.214×); [[Pravastatin (sodium) (drug)]] 0.05 µM in 1 line (RKO 0.0840×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (A549 0.107×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.706×** | -4.7 | 0.001 | 14/46 (LOX-IMVI, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.758×** | -3.7 | 0.050 | 5/46 (NCI-H2030, CFPAC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | 0.782× | -3.3 | 0.16 | 7/46 (A-427, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~3% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11910. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 7.59 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +12.3) | — |
| [[SW480 (line)]] | alt | 6.94 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +10.2) | [[Saquinavir (drug)]] 0.5 µM 0.214× (z -9.5) |
| [[A498 (line)]] | wt | 6.04 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.95× (z +9.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.38× (z +9.0) | — |
| [[A549 (line)]] | wt | 4.59 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 9.34× (z +8.9) ⚠ toxic; transcription drop | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.107× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 5.12 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.51× (z +10.4) | — |
| [[NCI-H460 (line)]] | wt | 6.12 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.53× (z +9.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 5.12× (z +8.6) | — |
| [[SNU-423 (line)]] | alt | 14.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.28× (z +9.8) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 5.49 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.57× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 5.94 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 7.92× (z +8.9) ⚠ toxic | — |
| [[RKO (line)]] | wt | 6.53 | 0 | 1 | — | [[Pravastatin (sodium) (drug)]] 0.05 µM 0.0840× (z -9.1) |
| [[A-172 (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.84 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.20 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.93 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.39 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.13 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11910), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBED5-AS1]] | +0.73 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[CYB5D2]] | +0.72 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[MED12]] | +0.70 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[CGGBP1]] | +0.70 | +0.71 / +0.44 | both halves | 3e-05 |  |
| [[ARMT1]] | +0.68 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[RAP2C-AS1]] | +0.67 | +0.73 / +0.47 | both halves | 2e-05 |  |
| [[DDX6]] | +0.67 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[UFL1-AS1]] | +0.67 | +0.69 / +0.31 | both halves | 2e-04 |  |
| [[TMEM202-AS1]] | +0.66 | +0.67 / +0.38 | both halves | 6e-05 |  |
| [[TIA1]] | +0.66 | +0.68 / +0.33 | both halves | 1e-04 |  |
| [[AHI1-DT]] | +0.66 | +0.60 / +0.34 | both halves | 1e-04 |  |
| [[IQCH-AS1]] | +0.65 | +0.62 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAF1]] | -0.68 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[TRIM11]] | -0.64 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[SMYD4]] | -0.64 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[DRD4]] | -0.62 | -0.59 / -0.58 | both halves | 8e-06 |  |
| [[GPR89B]] | -0.62 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[TECPR1]] | -0.61 | -0.59 / -0.28 | both halves | 3e-04 |  |
| [[PHKA2]] | -0.61 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[TMEM120B]] | -0.61 | -0.57 / -0.33 | both halves | 1e-04 |  |
| [[LCMT1]] | -0.61 | -0.54 / -0.36 | both halves | 9e-05 |  |
| [[PBX4]] | -0.61 | -0.60 / -0.33 | both halves | 1e-04 |  |
| [[SS18L1]] | -0.61 | -0.66 / -0.36 | both halves | 1e-04 | pathway: Affinity selection of immunoglobulins |
| [[GPR89A]] | -0.61 | -0.56 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYEF2]] | B | MYEF2 activity raises TAF9B's level | lines that do not express MYEF2 (16) vs lines expressing it (34) | 1.31× lower at baseline in the lines without MYEF2 | 0.0998 | ⚠ within organs, on part of the lines; also absent: SDK2, MAP6, RBM20 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **-** arm (projection on the module's main direction -0.718). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (5.0, 18.4); signed map (20.3, -19.3). **Vector** length 62.5, 8.98% of its response variance represented; |z| ≥ 3 in 963 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.1 | +21.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.1 | +14.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.8 | +20.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.2 | +19.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.3 | +9.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.7 | +3.7 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -2.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.3 | -4.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -0.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -1.9 | -3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | +0.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -0.4 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.0 | -1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.0 | +1.2 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.0 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | TATA-box binding protein associated factor 9b |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq21.1 — chrX:78,129,748-78,139,650 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TAFII31L, DN-7, DN7, TFIID-31; previously TAF9L |
| Reactome | 21 pathways, smallest: HIV Transcription Initiation; RNA Polymerase II HIV Promoter Escape; RNA Polymerase II Promoter Escape |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HBM6](https://www.uniprot.org/uniprotkb/Q9HBM6) (Transcription initiation factor TFIID subunit 9B):

> Essential for cell viability. TAF9 and TAF9B are involved in transcriptional activation as well as repression of distinct but overlapping sets of genes. May have a role in gene regulation associated with apoptosis. TAFs are components of the transcription factor IID (TFIID) complex, the TBP-free TAFII complex (TFTC), the PCAF histone acetylase complex and the STAGA transcription coactivator-HAT complex. TFIID or TFTC are essential for the regulation of RNA polymerase II-mediated transcription.

**Summary**, from NCBI Gene [51616](https://www.ncbi.nlm.nih.gov/gene/51616):

> Initiation of transcription by RNA polymerase II requires the activities of more than 70 polypeptides. The protein that coordinates these activities is transcription factor IID (TFIID), which binds to the core promoter to position the polymerase properly, serves as the scaffold for assembly of the remainder of the transcription complex, and acts as a channel for regulatory signals. TFIID is composed of the TATA-binding protein (TBP) and a group of evolutionarily conserved proteins known as …

**Accessions** — [HGNC:17306](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17306) · Entrez [51616](https://www.ncbi.nlm.nih.gov/gene/51616) · UniProt [Q9HBM6](https://www.uniprot.org/uniprotkb/Q9HBM6) · Ensembl [ENSG00000187325](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187325)

## Data

Gene col 11910: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11910); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11910, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11910]; `tensor/DDL_lfc|DDL_z.npy` [11910]; `embed/gene_vectors.npy` [11910]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11910 or target_col == 11910). Every well: [[TAF9B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAF9B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
