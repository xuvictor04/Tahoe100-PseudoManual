---
symbol: "PPP5D1P-1"
type: "gene"
col: 16605
ensembl_id: "ENSG00000291145"
name: ""
location: ""
module: 23
arm: "+"
pooled_cpm: 7.18
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 25
n_dd_up_clean: 14
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# PPP5D1P-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.75× (z +9.6, q 3e-19, up in 29 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (12 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.520× (z -8.0, q 9e-13, down in 31 of 46 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OXA1L-DT]] (+0.72, fdr 2e-05), [[ATE1OSP]] (+0.72, fdr 1e-05), [[FAM174B]] (+0.72, fdr 3e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16605.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +9.6 | 3e-19 | 29/42 (A498, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.88×** | +7.7 | 4e-12 | 29/45 (HT-29, A-427, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +5.9 | 7e-07 | 5/14 (J82, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +5.5 | 4e-06 | 18/47 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +5.5 | 4e-06 | 15/36 (A498, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.28×** | +4.1 | 0.003 | 11/47 (PANC-1, SW480, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.28×** | +4.1 | 0.004 | 13/48 (LoVo, RPMI-7951, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.35×** | +3.7 | 0.016 | 12/43 (KATO III, A-427, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.024 | 6/45 (NCI-H23, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.033 | 10/45 (SW480, HT-29, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.033 | 9/46 (KATO III, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.35×** | +3.4 | 0.033 | 4/18 (LoVo, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib (drug)]] 5 µM |  | **1.68×** | +3.3 | 0.040 | 3/40 (RPMI-7951, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.32×** | +3.3 | 0.040 | 6/48 (SW480, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.043 | 8/44 (A549, SW480, …) | all doses, flat |  |
| [[Ataluren (drug)]] 0.5 µM |  | **1.29×** | +3.1 | 0.059 | 3/45 (LoVo, SW48, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.070 | 12/38 (A498, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 1.19× | +3.0 | 0.088 | 4/46 (PANC-1, BT-474, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.28×** | +2.9 | 0.095 | 2/45 (hTERT-HPNE, NCI-H1792) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16605.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.520×** | -8.0 | 9e-13 | 31/46 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.526×** | -7.5 | 1e-11 | 22/36 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.577×** | -6.5 | 1e-08 | 27/47 (HEC-1-A, HT-29, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.598×** | -6.3 | 5e-08 | 23/47 (SW480, J82, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.608×** | -6.1 | 1e-07 | 22/45 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.614×** | -5.9 | 3e-07 | 23/42 (HOP62, LoVo, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.670×** | -4.9 | 8e-05 | 20/43 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.681×** | -4.7 | 2e-04 | 19/46 (HT-29, PANC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.493×** | -4.5 | 4e-04 | 13/44 (HOP62, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.698×** | -4.4 | 7e-04 | 19/45 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.704×** | -4.3 | 0.001 | 17/47 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.709×** | -4.2 | 0.001 | 14/45 (HT-29, J82, …) | rises with dose |  |
| [[Roxadustat (drug)]] 5 µM |  | **0.709×** | -4.0 | 0.003 | 11/44 (hTERT-HPNE, KATO III, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.723×** | -3.9 | 0.003 | 16/47 (HEC-1-A, PANC-1, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.715×** | -3.9 | 0.004 | 11/44 (HT-29, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.807×** | -3.7 | 0.007 | 12/46 (HT-29, MIA PaCa-2, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.561×** | -3.7 | 0.007 | 13/40 (HOP62, SW 900, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.561×** | -3.7 | 0.007 | 10/45 (SNU-1, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.775×** | -3.1 | 0.049 | 8/44 (MIA PaCa-2, A-427, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.623×** | -3.0 | 0.061 | 6/44 (NCI-H1792, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.843× | -2.9 | 0.073 | 10/47 (A498, NCI-H2030, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16605. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 9.29 | 0 | 4 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.135× (z -12.6) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 3.46 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 6.31× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.30× (z +8.9) | [[Cyclosporin A (drug)]] 0.5 µM 0.0618× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 21.4 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.224× (z -10.5) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.251× (z -9.7) |
| [[A-172 (line)]] | wt | 5.55 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.0968× (z -8.9) |
| [[A498 (line)]] | wt | 4.68 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.51× (z +10.2) | — |
| [[BT-474 (line)]] | alt | 10.9 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 0.05 µM 0.0743× (z -9.9) |
| [[HCT15 (line)]] | alt | 13.3 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.104× (z -8.7) |
| [[HOP62 (line)]] | alt | 5.65 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.115× (z -9.3) |
| [[HS-578T (line)]] | alt | 8.97 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0952× (z -9.4) ⚠ toxic |
| [[HT-29 (line)]] | alt | 10.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0903× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.101× (z -11.6) ⚠ toxic |
| [[KATO III (line)]] | alt | 6.47 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0720× (z -10.4) ⚠ toxic |
| [[LoVo (line)]] | wt | 6.72 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.182× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 8.35 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.118× (z -9.7) ⚠ transcription drop; cell-cycle shift, explains ~83% of this change |
| [[NCI-H1792 (line)]] | alt | 6.15 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0824× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[RPMI-7951 (line)]] | alt | 9.14 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0813× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 9.28 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.221× (z -9.3) ⚠ cell-cycle shift, explains ~33% of this change |
| [[A-427 (line)]] | wt | 6.18 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.14 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.30 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.32 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.01 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.36 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16605), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OXA1L-DT]] | +0.72 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[ATE1OSP]] | +0.72 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[FAM174B]] | +0.72 | +0.65 / +0.45 | both halves | 3e-05 |  |
| [[LINC02951]] | +0.71 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[ITFG2-AS1]] | +0.71 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[HEXIM2-AS1]] | +0.71 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[GTF2IRD2]] | +0.70 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[MFF-DT]] | +0.70 | +0.62 / +0.42 | both halves | 4e-05 |  |
| [[ANKHD1-DT]] | +0.70 | +0.64 / +0.42 | both halves | 4e-05 |  |
| [[C2orf49-DT]] | +0.69 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[GTF2IRD2B]] | +0.69 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[ANKRD17-DT]] | +0.69 | +0.63 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers PPP5D1P-1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.745). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (4.2, 16.3); signed map (25.2, -8.2). **Vector** length 70.5, 11.4% of its response variance represented; |z| ≥ 3 in 970 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.5 | +7.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +9.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.6 | +2.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.6 | +5.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +1.5 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.0 | +4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +3.4 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -5.6 | -5.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.0 | -6.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.0 | -8.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.1 | -3.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.1 | -7.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -2.9 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.7 | -1.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.6 | -3.0 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.5 | -1.8 |

## What is on record

> [!warning] No registry record
> PPP5D1P-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16605: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16605); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16605, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16605]; `tensor/DDL_lfc|DDL_z.npy` [16605]; `embed/gene_vectors.npy` [16605]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16605 or target_col == 16605). Every well: [[PPP5D1P-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP5D1P-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
