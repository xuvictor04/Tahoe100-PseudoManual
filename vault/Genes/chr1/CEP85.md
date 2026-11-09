---
symbol: "CEP85"
type: "gene"
col: 5097
ensembl_id: "ENSG00000130695"
name: "centrosomal protein 85"
location: "1p36.11"
module: 67
arm: "+"
pooled_cpm: 28.45
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 13
n_dd_up_clean: 7
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# CEP85

*centrosomal protein 85* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (10 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 2.09× (z +14.0, q 1e-41, up in 39 of 47 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.05 µM: 1.54× (z +8.1, q 4e-14, up in 31 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.688× (z -10.0, q 7e-21, down in 34 of 48 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.740× (z -8.1, q 1e-13, down in 29 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCNF]] (+0.80, fdr 7e-06), [[CENPI]] (+0.79, fdr 7e-06), [[UBE2T]] (+0.77, fdr 7e-06); moves opposite to [[LINC00571]] (-0.63, fdr 1e-05), [[BCL10-AS1]] (-0.63, fdr 1e-05).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5097.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.09×** | +14.0 | 1e-41 | 39/47 (SW480, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.98×** | +12.9 | 7e-36 | 43/48 (SW480, Hs 766T, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.96×** | +12.7 | 9e-35 | 42/48 (SW480, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.66×** | +9.6 | 9e-20 | 30/47 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.62×** | +9.2 | 6e-18 | 28/48 (PANC-1, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.59×** | +8.8 | 1e-16 | 32/48 (PANC-1, LS 180, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.54×** | +8.1 | 4e-14 | 31/47 (PANC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.50×** | +7.6 | 2e-12 | 30/46 (PANC-1, NCI-H23, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +7.4 | 6e-12 | 28/48 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **1.49×** | +7.2 | 4e-11 | 25/46 (LoVo, NCI-H23, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +6.1 | 4e-08 | 24/46 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.37×** | +6.0 | 9e-08 | 23/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.53×** | +4.2 | 0.001 | 10/48 (SW480, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +4.1 | 0.002 | 16/48 (NCI-H2347, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.17× | +4.1 | 0.002 | 18/47 (CFPAC-1, NCI-H2347, …) | top dose only | composition shift |
| [[Riluzole hydrochloride (drug)]] 0.5 µM |  | **1.24×** | +4.0 | 0.002 | 11/48 (LOX-IMVI, LoVo, …) | inconsistent across doses | position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.50×** | +4.0 | 0.002 | 11/46 (HS-578T, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.43×** | +3.5 | 0.012 | 12/47 (SW1417, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5097.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.688×** | -10.0 | 7e-21 | 34/48 (HT-29, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.577×** | -9.6 | 2e-19 | 28/41 (NCI-H2030, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.648×** | -8.2 | 4e-14 | 31/47 (A498, KATO III, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.740×** | -8.1 | 1e-13 | 29/47 (A-427, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.688×** | -6.8 | 1e-09 | 20/38 (NCI-H2030, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.792×** | -6.3 | 4e-08 | 27/48 (A-172, HOP62, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.748×** | -5.3 | 1e-05 | 24/48 (HEC-1-A, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.764×** | -5.1 | 2e-05 | 22/48 (SNU-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.783×** | -4.6 | 2e-04 | 18/47 (C-33 A, A-427, …) | top dose only |  |
| [[Lactate (calcium) (drug)]] 5 µM |  | **0.786×** | -4.6 | 3e-04 | 12/48 (HepG2/C3A, NCI-H2030, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.784×** | -4.4 | 5e-04 | 20/46 (HEC-1-A, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.804×** | -4.1 | 0.002 | 19/43 (HOP62, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.877× | -3.5 | 0.019 | 5/48 (SHP-77, NCI-H2347, …) | top dose only | position effect removed |
| [[Larotrectinib sulfate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.844× | -3.2 | 0.052 | 6/48 (Panc 03.27, A-427, …) | inconsistent across doses | position effect removed |
| [[DTP3 (drug)]] 5 µM |  | **0.727×** | -3.2 | 0.060 | 11/45 (LS 180, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 0.852× | -3.0 | 0.088 | 15/47 (SW48, RKO, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5097. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 40.5 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.189× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -10.3) |
| [[PANC-1 (line)]] | alt | 55.3 | 3 (3 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +9.7) ⚠ cell-cycle shift, explains ~41% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.331× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.551× (z -9.4) |
| [[A498 (line)]] | wt | 27.5 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -9.7) |
| [[HOP62 (line)]] | alt | 32.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.262× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -9.2) |
| [[SW480 (line)]] | alt | 37.0 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.48× (z +10.1) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[LoVo (line)]] | wt | 22.5 | 2 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.68× (z +8.6) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H2030 (line)]] | alt | 55.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.172× (z -15.4) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 38.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.101× (z -14.3) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 13.7 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.308× (z -10.4) |
| [[C-33 A (line)]] | alt | 63.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -9.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 14.5 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0827× (z -11.4) |
| [[HEC-1-A (line)]] | alt | 25.6 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -10.5) |
| [[HT-29 (line)]] | alt | 26.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.353× (z -10.7) ⚠ cell-cycle shift, explains ~37% of this change |
| [[LOX-IMVI (line)]] | wt | 19.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.372× (z -9.6) ⚠ cell-cycle shift, explains ~37% of this change |
| [[LS 180 (line)]] | wt | 23.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.368× (z -10.4) ⚠ cell-cycle shift, explains ~37% of this change |
| [[NCI-H23 (line)]] | alt | 42.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -9.9) |
| [[SW 900 (line)]] | alt | 17.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -11.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.71 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5097), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNF]] | +0.80 | +0.72 / +0.75 | both halves | 7e-06 |  |
| [[CENPI]] | +0.79 | +0.71 / +0.76 | both halves | 7e-06 |  |
| [[UBE2T]] | +0.77 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[NEIL3]] | +0.77 | +0.69 / +0.79 | both halves | 7e-06 |  |
| [[NCAPH]] | +0.77 | +0.70 / +0.78 | both halves | 7e-06 |  |
| [[BUB1B]] | +0.77 | +0.79 / +0.73 | both halves | 7e-06 |  |
| [[KIF18B]] | +0.76 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[MPHOSPH9]] | +0.75 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[INCENP]] | +0.75 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[CEP57L1]] | +0.74 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[CIT]] | +0.74 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[CCDC150]] | +0.74 | +0.65 / +0.76 | both halves | 7e-06 | STRING 536 |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00571]] | -0.63 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[BCL10-AS1]] | -0.63 | -0.52 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises CEP85's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ANKRD20A1]] | B | ANKRD20A1 activity raises CEP85's level | lines that do not express ANKRD20A1 (20) vs lines expressing it (30) | 1.41× lower at baseline in the lines without ANKRD20A1 | 0.067 | ⚠ within organs, on part of the lines; also absent: ANKRD20A4P, CTNNA2, SCN8A |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.793). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-33.9, -53.6); signed map (-46.2, -40.3). **Vector** length 111, 28.5% of its response variance represented; |z| ≥ 3 in 1,132 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.68 to 12); *G2/M checkpoint* (hallmark, mean cos +0.66 to 9); *Mitotic Prometaphase* (reactome, mean cos +0.65 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +4.6 | +14.0 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | +4.5 | +8.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +4.0 | +12.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.0 | +7.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +3.8 | +12.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.2 | +4.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.4 | +4.0 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +2.4 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +4.1 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +1.5 | +2.3 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -9.0 | -10.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -7.3 | -8.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.0 | -8.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -5.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.6 | -4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.3 | -6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.8 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -2.8 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.2 | -2.2 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -2.2 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | centrosomal protein 85 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:26,234,200-26,278,808 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434L0117; previously CCDC21 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P2H3](https://www.uniprot.org/uniprotkb/Q6P2H3) (Centrosomal protein of 85 kDa):

> Acts as a regulator of centriole duplication through a direct interaction with STIL, a key factor involved in the early steps of centriole formation. The CEP85-STIL protein complex acts as a modulator of PLK4-driven cytoskeletal rearrangements and directional cell motility. Acts as a negative regulator of NEK2 to maintain the centrosome integrity in interphase. Suppresses centrosome disjunction by inhibiting NEK2 kinase activity.

**Summary**, from NCBI Gene [64793](https://www.ncbi.nlm.nih.gov/gene/64793):

> This gene encodes a protein that belongs to the centrosome-associated family of proteins. The centrosome is a subcellular organelle in the animal cell that functions as a microtubule organizing center and is involved in cell-cycle progression. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:25309](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25309) · Entrez [64793](https://www.ncbi.nlm.nih.gov/gene/64793) · UniProt [Q6P2H3](https://www.uniprot.org/uniprotkb/Q6P2H3) · Ensembl [ENSG00000130695](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130695)

## Data

Gene col 5097: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5097); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5097, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5097]; `tensor/DDL_lfc|DDL_z.npy` [5097]; `embed/gene_vectors.npy` [5097]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5097 or target_col == 5097). Every well: [[CEP85 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CEP85.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
