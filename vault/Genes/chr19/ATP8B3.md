---
symbol: "ATP8B3"
type: "gene"
col: 5042
ensembl_id: "ENSG00000130270"
name: "ATPase phospholipid transporting 8B3"
location: "19p13.3"
module: 67
arm: "+"
pooled_cpm: 6.7
n_lines_expressing: 45
n_dd_up: 6
n_dd_down: 22
n_dd_up_clean: 2
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 6
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# ATP8B3

*ATPase phospholipid transporting 8B3* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.45× (z +6.2, q 3e-07, up in 19 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H23 5.66×, NCI-H2030 3.86×; ⚠ cell-cycle shift, explains ~47% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H2030 4.33×; ⚠ cell-cycle shift, would explain all of this change); [[Tucidinostat (drug)]] 5 µM in 1 line (SW480 3.09×).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.369× (z -11.9, q 9e-30, down in 31 of 42 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYLK2]] (+0.58, fdr 1e-05), [[LOXL2]] (+0.57, fdr 3e-05), [[SLX4]] (+0.53, fdr 2e-05); moves opposite to [[SLC49A4]] (-0.55, fdr 9e-05), [[ORMDL1]] (-0.51, fdr 4e-05), [[HSPBAP1]] (-0.51, fdr 6e-05).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); 6 go from it, the strongest it → [[CHD1L]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5042.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H23 5.66×, NCI-H2030 3.86×; ⚠ cell-cycle shift, explains ~47% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H2030 4.33×; ⚠ cell-cycle shift, would explain all of this change); [[Tucidinostat (drug)]] 5 µM in 1 line (SW480 3.09×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +6.2 | 3e-07 | 19/42 (SW480, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +5.6 | 6e-06 | 1/12 (A498) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.45×** | +4.4 | 0.003 | 15/42 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.42×** | +4.1 | 0.005 | 8/27 (HS-578T, A549, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.27×** | +4.0 | 0.006 | 15/36 (NCI-H23, NCI-H2030, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.33×** | +3.4 | 0.073 | 3/24 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5042.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.369×** | -11.9 | 9e-30 | 31/42 (RPMI-7951, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.475×** | -8.5 | 4e-15 | 22/32 (A549, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.511×** | -8.0 | 2e-13 | 26/40 (HS-578T, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.519×** | -7.8 | 8e-13 | 24/37 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.549×** | -7.1 | 1e-10 | 23/38 (SW480, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.551×** | -7.1 | 1e-10 | 24/33 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.612×** | -5.8 | 4e-07 | 20/39 (MIA PaCa-2, A498, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.644×** | -5.2 | 1e-05 | 17/38 (LOX-IMVI, HS-578T, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.650×** | -5.1 | 2e-05 | 17/38 (H4, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.739×** | -5.1 | 2e-05 | 19/40 (hTERT-HPNE, A549, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.654×** | -4.9 | 6e-05 | 17/39 (C32, SW 900, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.678×** | -4.5 | 4e-04 | 15/29 (NCI-H2030, A-427, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.733×** | -3.7 | 0.009 | 13/42 (NCI-H1792, C32, …) | inconsistent across doses |  |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **0.735×** | -3.5 | 0.017 | 10/33 (J82, NCI-H2030, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.829×** | -3.2 | 0.054 | 11/40 (hTERT-HPNE, PANC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.767×** | -3.2 | 0.054 | 10/37 (LOX-IMVI, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.769×** | -3.1 | 0.055 | 9/42 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **0.771×** | -3.0 | 0.083 | 12/37 (C32, NCI-H23, …) | top dose only |  |
| [[Silodosin (drug)]] 5 µM |  | **0.773×** | -3.0 | 0.083 | 8/33 (NCI-H2347, CFPAC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5042. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 9.86 | 2 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +11.2) ⚠ cell-cycle shift, explains ~47% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.116× (z -12.1) ⚠ toxic |
| [[HOP62 (line)]] | alt | 8.13 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0312× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.171× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 8.79 | 0 | 3 | — | [[Auranofin (drug)]] 5 µM 0.145× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 7.54 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0620× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.132× (z -8.5) |
| [[SW480 (line)]] | alt | 6.07 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.09× (z +8.5) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.154× (z -10.0) |
| [[A549 (line)]] | wt | 6.53 | 0 | 2 (1 ⚠) | — | [[Temsirolimus (drug)]] 0.5 µM 0.0615× (z -11.8) |
| [[PANC-1 (line)]] | alt | 16.4 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 7.45 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0622× (z -9.8) |
| [[A498 (line)]] | wt | 10.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.208× (z -9.8) |
| [[C32 (line)]] | wt | 6.52 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.101× (z -8.6) ⚠ toxic |
| [[H4 (line)]] | wt | 17.1 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.102× (z -8.8) ⚠ cell-cycle shift, explains ~14% of this change |
| [[Hs 766T (line)]] | wt | 7.76 | 0 | 1 | — | [[Gemfibrozil (drug)]] 0.05 µM 0.0746× (z -10.3) |
| [[HS-578T (line)]] | alt | 9.13 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.110× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 22.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0845× (z -13.5) |
| [[NCI-H1573 (line)]] | alt | 3.20 | 0 | 1 | — | [[Bestatin (hydrochloride) (drug)]] 0.05 µM 0.0631× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 12.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.66× (z +12.5) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[NCI-H460 (line)]] | wt | 4.74 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.136× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 3.28 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0665× (z -8.5) ⚠ unreliable plate only |
| [[SW 900 (line)]] | alt | 9.75 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -8.7) ⚠ cell-cycle shift, explains ~47% of this change |
| [[A-172 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.16 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.848 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.17 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.740 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.21 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5042), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYLK2]] | +0.58 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[LOXL2]] | +0.57 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[SLX4]] | +0.53 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[ARHGAP33]] | +0.53 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[EFEMP2]] | +0.53 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[FAM83D]] | +0.52 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[AP1M1]] | +0.52 | +0.51 / +0.38 | both halves | 6e-05 |  |
| [[TMEM39B]] | +0.51 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[LAG3]] | +0.51 | +0.46 / +0.51 | both halves | 2e-05 |  |
| [[IQGAP3]] | +0.51 | +0.43 / +0.45 | both halves | 3e-05 |  |
| [[APC2]] | +0.51 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[DLG4]] | +0.51 | +0.60 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC49A4]] | -0.55 | -0.54 / -0.36 | both halves | 9e-05 |  |
| [[ORMDL1]] | -0.51 | -0.43 / -0.40 | both halves | 4e-05 |  |
| [[HSPBAP1]] | -0.51 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[HNF4G]] | -0.48 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[MFSD6]] | -0.47 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[NIPAL2]] | -0.46 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[ICA1]] | -0.46 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[AK3]] | -0.45 | -0.45 / -0.36 | both halves | 1e-04 |  |
| [[YBEY]] | -0.45 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[TMEM192]] | -0.45 | -0.27 / -0.41 | both halves | 3e-04 |  |
| [[VSIG10]] | -0.44 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[PHACTR2]] | -0.43 | -0.37 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers ATP8B3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHD1L]] | B | ATP8B3 activity raises CHD1L's level | lines that do not express ATP8B3 (5) vs lines expressing it (45) | 2.39× lower at baseline in the lines without ATP8B3 | 0.036 | ⚠ within organs, on part of the lines; also absent: CEP85L, PARP3, SOAT1; maybe low, not absent |
| [[MIER2]] | B | ATP8B3 activity raises MIER2's level | lines that do not express ATP8B3 (5) vs lines expressing it (45) | 1.36× lower at baseline in the lines without ATP8B3 | 0.066 | ⚠ within organs, on part of the lines; also absent: CEP85L, PARP3, SOAT1; maybe low, not absent |
| [[SESN1]] | B | ATP8B3 activity lowers SESN1's level | lines that do not express ATP8B3 (5) vs lines expressing it (45) | 1.65× higher at baseline in the lines without ATP8B3 | 0.079 | ⚠ within organs, on part of the lines; also absent: CEP85L, PARP3, SOAT1; maybe low, not absent |
| [[ZNF385A]] | B | ATP8B3 activity raises ZNF385A's level | lines that do not express ATP8B3 (5) vs lines expressing it (45) | 1.80× lower at baseline in the lines without ATP8B3 | 0.079 | ⚠ within organs, on part of the lines; also absent: CEP85L, PARP3, SOAT1; maybe low, not absent |
| [[POLG]] | B | ATP8B3 activity raises POLG's level | lines that do not express ATP8B3 (5) vs lines expressing it (45) | 1.19× lower at baseline in the lines without ATP8B3 | 0.088 | ⚠ within organs, on part of the lines; also absent: CEP85L, PARP3, SOAT1; maybe low, not absent |
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | ATP8B3's natural level lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | ATP8B3's natural level across 43 lines (lineage-adjusted; a glimpse) | r -0.68 | 0.390 over the table, 0.040 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.330). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-30.6, -57.8); signed map (-32.7, 35.4). **Vector** length 74.3, 13.7% of its response variance represented; |z| ≥ 3 in 971 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +5.3 | +4.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +5.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +6.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.4 | +4.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | -0.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.4 | +2.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.4 | +2.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.2 | +0.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.9 | -7.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.7 | -8.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.7 | -7.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.4 | -11.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -3.4 | -5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -5.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -3.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.0 | -3.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.6 | -2.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.6 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | ATPase phospholipid transporting 8B3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:1,782,075-1,812,276 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ATPIK |
| Gene groups (HGNC) | ATPase phospholipid transporting |
| Reactome | 3 pathways, smallest: Ion transport by P-type ATPases; Ion channel transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [O60423](https://www.uniprot.org/uniprotkb/O60423) (Phospholipid-transporting ATPase IK):

> P4-ATPase flippase which catalyzes the hydrolysis of ATP coupled to the transport of aminophospholipids from the outer to the inner leaflet of various membranes and ensures the maintenance of asymmetric distribution of phospholipids. Phospholipid translocation also seems to be implicated in vesicle formation and in uptake of lipid signaling molecules. May be responsible for the maintenance of asymmetric distribution of phosphatidylserine (PS) in spermatozoa membranes. Involved in acrosome …

**Summary**, from NCBI Gene [148229](https://www.ncbi.nlm.nih.gov/gene/148229):

> The protein encoded by this gene belongs to the family of P-type cation transport ATPases, and to the subfamily of aminophospholipid-transporting ATPases. The aminophospholipid translocases transport phosphatidylserine and phosphatidylethanolamine from one side of a bilayer to the other. This gene encodes member 3 of phospholipid-transporting ATPase 8B; other members of this protein family are located on chromosomes 1, 15 and 18. Alternatively spliced transcript variants encoding different …

**Accessions** — [HGNC:13535](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13535) · Entrez [148229](https://www.ncbi.nlm.nih.gov/gene/148229) · UniProt [O60423](https://www.uniprot.org/uniprotkb/O60423) · Ensembl [ENSG00000130270](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130270)

## Data

Gene col 5042: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5042); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5042, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5042]; `tensor/DDL_lfc|DDL_z.npy` [5042]; `embed/gene_vectors.npy` [5042]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5042 or target_col == 5042). Every well: [[ATP8B3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP8B3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
