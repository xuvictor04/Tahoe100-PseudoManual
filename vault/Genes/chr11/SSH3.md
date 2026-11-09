---
symbol: "SSH3"
type: "gene"
col: 10303
ensembl_id: "ENSG00000172830"
name: "slingshot protein phosphatase 3"
location: "11q13.2"
module: 126
arm: "+"
pooled_cpm: 8.76
n_lines_expressing: 49
n_dd_up: 3
n_dd_down: 30
n_dd_up_clean: 0
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/126"]
generated_by: "tahoemap"
---

# SSH3

*slingshot protein phosphatase 3* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.74× (z +7.2, q 4e-10, up in 13 of 17 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (15 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.347× (z -14.3, q 9e-44, down in 42 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INPPL1]] (+0.60, fdr 7e-06), [[EPS8L2]] (+0.59, fdr 1e-05), [[STK36]] (+0.59, fdr 1e-05); moves opposite to [[MIF]] (-0.48, fdr 9e-05), [[PHF20]] (-0.47, fdr 5e-05), [[SLC25A5]] (-0.47, fdr 6e-05).
> It is in [[Module 126]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[ARHGEF5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10303.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.74×** | +7.2 | 4e-10 | 13/17 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.51×** | +5.5 | 9e-06 | 12/28 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.49×** | +4.9 | 1e-04 | 13/25 (HEC-1-A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 15 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10303.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.347×** | -14.3 | 9e-44 | 42/46 (COLO 205, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.423×** | -11.6 | 7e-29 | 33/42 (SHP-77, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.433×** | -11.3 | 2e-27 | 31/45 (KATO III, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.566×** | -10.9 | 2e-25 | 27/41 (KATO III, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.454×** | -10.7 | 1e-24 | 37/44 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.501×** | -9.4 | 7e-19 | 30/44 (BT-474, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.502×** | -9.3 | 8e-19 | 33/46 (SW480, NCI-H1792, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.547×** | -8.2 | 2e-14 | 32/44 (BT-474, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.548×** | -8.1 | 2e-14 | 26/40 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.637×** | -6.1 | 6e-08 | 23/46 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.663×** | -5.6 | 1e-06 | 19/46 (HT-29, NCI-H1792, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.669×** | -5.5 | 2e-06 | 20/44 (RPMI-7951, HT-29, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.665×** | -5.3 | 5e-06 | 18/44 (J82, NCI-H1792, …) | rises with dose | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.774×** | -4.9 | 4e-05 | 16/41 (AsPC-1, HT-29, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.722×** | -4.4 | 4e-04 | 17/46 (HepG2/C3A, H4, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.806×** | -4.1 | 0.001 | 16/45 (LoVo, HT-29, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.759×** | -3.7 | 0.006 | 17/44 (SHP-77, Panc 03.27, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.763×** | -3.7 | 0.007 | 12/45 (Panc 03.27, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.781×** | -3.2 | 0.039 | 11/43 (HT-29, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.794×** | -3.1 | 0.043 | 7/46 (NCI-H460, HT-29, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.805×** | -2.9 | 0.073 | 11/43 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.747×** | -2.8 | 0.092 | 3/46 (SNU-1, Hs 766T, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.672×** | -2.8 | 0.092 | 7/39 (HT-29, HCT15, …) | rises with dose | noisy plate (z scaled) |
| [[Almonertinib (hydrochloride) (drug)]] 0.05 µM |  | **0.812×** | -2.8 | 0.092 | 10/44 (HepG2/C3A, J82, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10303. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 24.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -12.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.180× (z -10.2) |
| [[COLO 205 (line)]] | alt | 12.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0370× (z -13.3) |
| [[LoVo (line)]] | wt | 10.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.119× (z -13.0) |
| [[NCI-H1573 (line)]] | alt | 10.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0635× (z -14.5) |
| [[Hs 766T (line)]] | wt | 7.55 | 0 | 2 (1 ⚠) | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.126× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 4.45 | 0 | 2 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0829× (z -9.3) |
| [[PANC-1 (line)]] | alt | 7.26 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.207× (z -9.9) |
| [[SW 900 (line)]] | alt | 6.51 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0575× (z -10.2) ⚠ cell-cycle shift, explains ~49% of this change |
| [[SW480 (line)]] | alt | 8.36 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.269× (z -9.1) ⚠ cell-cycle shift, explains ~34% of this change |
| [[A549 (line)]] | wt | 6.89 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.116× (z -9.8) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -9.2) ⚠ cell-cycle shift, explains ~29% of this change |
| [[HS-578T (line)]] | alt | 4.64 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0818× (z -8.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 7.06 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -10.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[KATO III (line)]] | alt | 14.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -12.2) ⚠ cell-cycle shift, explains ~29% of this change |
| [[MIA PaCa-2 (line)]] | alt | 5.72 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.121× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.109× (z -12.3) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 5.96 | 0 | 1 | — | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM 0.0578× (z -9.2) |
| [[SHP-77 (line)]] | alt | 8.61 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0937× (z -10.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 6.65 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.125× (z -9.1) |
| [[SW48 (line)]] | wt | 9.65 | 0 | 1 | — | [[Decitabine (drug)]] 0.5 µM 0.0640× (z -9.0) |
| [[A-172 (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.20 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.09 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.20 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.66 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.52 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.55 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10303), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INPPL1]] | +0.60 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[EPS8L2]] | +0.59 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[STK36]] | +0.59 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[EVPL]] | +0.57 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[SCRIB]] | +0.56 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[PLXNB1]] | +0.56 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[CTBP1]] | +0.55 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[CRTC2]] | +0.55 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[ATP13A1]] | +0.55 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[CAPN1]] | +0.54 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[LAD1]] | +0.54 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[PRR36]] | +0.53 | +0.50 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIF]] | -0.48 | -0.36 / -0.39 | both halves | 9e-05 |  |
| [[PHF20]] | -0.47 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[SLC25A5]] | -0.47 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[ST3GAL3]] | -0.47 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[TMEM14B]] | -0.47 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[HILPDA]] | -0.46 | -0.27 / -0.50 | both halves | 3e-04 |  |
| [[KATNBL1]] | -0.46 | -0.38 / -0.42 | both halves | 7e-05 |  |
| [[FUT11]] | -0.45 | -0.30 / -0.37 | both halves | 2e-04 |  |
| [[SEC61G]] | -0.45 | -0.24 / -0.44 | both halves | 4e-04 |  |
| [[PRDX4]] | -0.45 | -0.40 / -0.37 | both halves | 8e-05 |  |
| [[VIM]] | -0.44 | -0.36 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGEF5]] | B | ARHGEF5 activity raises SSH3's level | lines that do not express ARHGEF5 (19) vs lines expressing it (31) | 1.79× lower at baseline in the lines without ARHGEF5 | 0.007 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ENSG00000284644, ESRP2, GOLT1A |
| [[ESRP2]] | B | ESRP2 activity raises SSH3's level | lines that do not express ESRP2 (26) vs lines expressing it (24) | 1.82× lower at baseline in the lines without ESRP2 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS22, MARVELD3, CRB3 |
| [[TP53I11]] | B | TP53I11 activity raises SSH3's level | lines that do not express TP53I11 (7) vs lines expressing it (43) | 1.48× lower at baseline in the lines without TP53I11 | 0.036 | ⚠ within organs, on part of the lines |
| [[PROM2]] | B | PROM2 activity raises SSH3's level | lines that do not express PROM2 (21) vs lines expressing it (29) | 1.41× lower at baseline in the lines without PROM2 | 0.050 | ⚠ within organs, on part of the lines; also absent: FAM83B, GRHL2, ANKRD22; maybe low, not absent |
| [[TNNT2]] | B | TNNT2 activity raises SSH3's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 1.58× lower at baseline in the lines without TNNT2 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14 |
| [[LAD1]] | B | LAD1 activity raises SSH3's level | lines that do not express LAD1 (30) vs lines expressing it (20) | 1.66× lower at baseline in the lines without LAD1 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ST14, KDF1 |
| [[TMEM30B]] | B | TMEM30B activity raises SSH3's level | lines that do not express TMEM30B (35) vs lines expressing it (15) | 1.80× lower at baseline in the lines without TMEM30B | 0.091 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 126]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.559). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (5.9, 56.0); signed map (-11.8, -33.0). **Vector** length 63.8, 10.1% of its response variance represented; |z| ≥ 3 in 1,054 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.1 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.0 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.5 | +4.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.8 | +0.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +1.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +2.9 |
|  | [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | +1.4 | +2.1 |
|  | [[Saquinavir (drug)]] 0.5 µM |  | +1.3 | +2.2 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.2 | +0.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -4.2 | -10.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.1 | -9.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.7 | -14.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.2 | -11.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -2.2 | -6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -4.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -1.4 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.5 | -1.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.5 | -1.2 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.4 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | slingshot protein phosphatase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:67,303,478-67,312,607 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20515, FLJ10928 |
| Gene groups (HGNC) | Slingshot protein phosphatases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TE77](https://www.uniprot.org/uniprotkb/Q8TE77) (Protein phosphatase Slingshot homolog 3):

> Protein phosphatase which may play a role in the regulation of actin filament dynamics. Can dephosphorylate and activate the actin binding/depolymerizing factor cofilin, which subsequently binds to actin filaments and stimulates their disassembly (By similarity).

**Summary**, from NCBI Gene [54961](https://www.ncbi.nlm.nih.gov/gene/54961):

> The ADF (actin-depolymerizing factor)/cofilin family (see MIM 601442) is composed of stimulus-responsive mediators of actin dynamics. ADF/cofilin proteins are inactivated by kinases such as LIM domain kinase-1 (LIMK1; MIM 601329). The SSH family appears to play a role in actin dynamics by reactivating ADF/cofilin proteins in vivo (Niwa et al., 2002 [PubMed 11832213]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:30581](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30581) · Entrez [54961](https://www.ncbi.nlm.nih.gov/gene/54961) · UniProt [Q8TE77](https://www.uniprot.org/uniprotkb/Q8TE77) · Ensembl [ENSG00000172830](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172830)

## Data

Gene col 10303: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10303); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10303, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10303]; `tensor/DDL_lfc|DDL_z.npy` [10303]; `embed/gene_vectors.npy` [10303]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10303 or target_col == 10303). Every well: [[SSH3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SSH3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
