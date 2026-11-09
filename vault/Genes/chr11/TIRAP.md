---
symbol: "TIRAP"
type: "gene"
col: 7434
ensembl_id: "ENSG00000150455"
name: "TIR domain containing adaptor protein"
location: "11q24.2"
module: 64
arm: "+"
pooled_cpm: 10.61
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 19
n_dd_up_clean: 4
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# TIRAP

*TIR domain containing adaptor protein* — 11q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.01× (z +14.9, q 0e+00, up in 35 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.379× (z -12.8, q 7e-35, down in 34 of 46 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMB5]] (+0.71, fdr 1e-05), [[RHBDD3]] (+0.67, fdr 3e-05), [[PPP1R26-AS1]] (+0.67, fdr 5e-05); moves opposite to [[ZMIZ2]] (-0.63, fdr 3e-05), [[PAFAH1B3]] (-0.62, fdr 4e-04), [[KCTD17]] (-0.60, fdr 3e-04).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[AMOT]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Erythromycin (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7434.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +14.9 | 0e+00 | 35/42 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.49×** | +5.7 | 4e-06 | 19/44 (COLO 205, HT-29, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +5.5 | 8e-06 | 23/46 (HEC-1-A, LoVo, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.25×** | +4.7 | 3e-04 | 17/47 (LoVo, J82, …) | top dose only | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.1 | 0.005 | 16/42 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +4.0 | 0.006 | 8/46 (KATO III, PANC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.23× | +3.1 | 0.15 | 8/46 (HT-29, AsPC-1, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.26× | +3.1 | 0.15 | 11/46 (A498, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7434.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.379×** | -12.8 | 7e-35 | 34/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.482×** | -9.7 | 1e-19 | 26/43 (AsPC-1, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.546×** | -8.0 | 2e-13 | 27/46 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.364×** | -8.0 | 2e-13 | 31/46 (KATO III, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.584×** | -7.8 | 6e-13 | 21/37 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.612×** | -7.1 | 9e-11 | 26/45 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.585×** | -7.1 | 1e-10 | 26/46 (KATO III, A-427, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.411×** | -7.0 | 2e-10 | 23/42 (Panc 03.27, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.572×** | -6.3 | 1e-08 | 24/46 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.690×** | -5.6 | 1e-06 | 24/45 (RKO, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.698×** | -5.4 | 3e-06 | 21/46 (NCI-H1792, Panc 03.27, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.640×** | -5.1 | 2e-05 | 18/45 (NCI-H460, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.650×** | -4.9 | 5e-05 | 20/46 (HOP62, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.729×** | -4.3 | 8e-04 | 14/47 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change | **0.791×** | -3.6 | 0.014 | 15/33 (LS 180, PANC-1, …) | inconsistent across doses | composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.780×** | -3.5 | 0.017 | 12/42 (SNU-423, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Mebendazole (drug)]] 5 µM |  | **0.792×** | -3.4 | 0.021 | 13/47 (NCI-H460, NCI-H661, …) | top dose only |  |
| [[Folic acid (drug)]] 5 µM |  | 0.854× | -3.4 | 0.022 | 6/47 (MIA PaCa-2, A-427, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.807×** | -3.3 | 0.033 | 4/46 (NCI-H2030, SNU-423, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7434. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 10.6 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.119× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.132× (z -12.4) |
| [[KATO III (line)]] | alt | 31.1 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.254× (z -10.2) |
| [[PANC-1 (line)]] | alt | 16.2 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.269× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.260× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 11.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.19× (z +10.5) | [[Dinaciclib (drug)]] 0.05 µM 0.210× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change |
| [[J82 (line)]] | alt | 6.28 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 10.9 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.182× (z -9.2) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 12.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0430× (z -9.1) |
| [[RKO (line)]] | wt | 11.3 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.103× (z -11.3) |
| [[A498 (line)]] | wt | 7.22 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.192× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 8.41 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0917× (z -10.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0818× (z -9.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 10.3 | 0 | 1 | — | [[Menadione (drug)]] 0.5 µM 0.0528× (z -11.3) |
| [[HOP62 (line)]] | alt | 7.02 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.100× (z -8.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[LS 180 (line)]] | wt | 15.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0938× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change |
| [[NCI-H23 (line)]] | alt | 6.30 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.16× (z +10.2) | — |
| [[NCI-H2347 (line)]] | alt | 4.93 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.138× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 8.69 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0610× (z -9.8) |
| [[SW 900 (line)]] | alt | 9.55 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 14.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +10.3) | — |
| [[A-172 (line)]] | wt | 6.41 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.72 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.29 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.45 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.26 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.48 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.56 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.75 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7434), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMB5]] | +0.71 | +0.55 / +0.68 | both halves | 1e-05 | pathway: Antigen processing-Cross presentation |
| [[RHBDD3]] | +0.67 | +0.65 / +0.43 | both halves | 3e-05 |  |
| [[PPP1R26-AS1]] | +0.67 | +0.40 / +0.67 | both halves | 5e-05 |  |
| [[RCC1L]] | +0.66 | +0.60 / +0.36 | both halves | 1e-04 |  |
| [[PEX6]] | +0.65 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[SPAG7]] | +0.64 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[TMEM79]] | +0.64 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[PTOV1-AS1]] | +0.64 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[METTL4]] | +0.63 | +0.38 / +0.48 | both halves | 6e-05 |  |
| [[DNAJB14]] | +0.63 | +0.67 / +0.34 | both halves | 1e-04 |  |
| [[CCDC117]] | +0.63 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[LRRC41]] | +0.63 | +0.21 / +0.57 | both halves | 7e-04 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMIZ2]] | -0.63 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[PAFAH1B3]] | -0.62 | -0.54 / -0.25 | both halves | 4e-04 |  |
| [[KCTD17]] | -0.60 | -0.53 / -0.27 | both halves | 3e-04 |  |
| [[ARRB2]] | -0.60 | -0.56 / -0.20 | ⚠ one half (not replicated) | 7e-04 |  |
| [[STUB1]] | -0.57 | -0.52 / -0.04 | ⚠ one half (not replicated) | 0.006 |  |
| [[VWA1]] | -0.56 | -0.41 / -0.29 | both halves | 2e-04 |  |
| [[TTLL12]] | -0.56 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[PICALM]] | -0.55 | -0.46 / -0.56 | both halves | 2e-05 |  |
| [[PADI2]] | -0.54 | -0.44 / -0.30 | both halves | 2e-04 |  |
| [[FOXO6]] | -0.53 | -0.43 / -0.19 | ⚠ not reproduced | 8e-04 |  |
| [[HPSE]] | -0.53 | -0.45 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AMOT]] | B | AMOT activity raises TIRAP's level | lines that do not express AMOT (12) vs lines expressing it (38) | 1.37× lower at baseline in the lines without AMOT | 0.040 | ⚠ within organs, on part of the lines; also absent: SYCP2, ENSG00000289956, ENSG00000132832 |
| [[NMRAL2P]] | B | NMRAL2P activity raises TIRAP's level | lines that do not express NMRAL2P (18) vs lines expressing it (32) | 1.16× lower at baseline in the lines without NMRAL2P | 0.082 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, SERPINE2, APOL1 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Erythromycin (drug)]] 0.5 µM | C | TIRAP's natural level lowers the cells' numbers under Erythromycin 0.5 µM (makes them more sensitive) | TIRAP's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.69 | 0.285 over the table, 0.083 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.429). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-10.2, 21.4); signed map (4.4, -1.2). **Vector** length 68.9, 11.8% of its response variance represented; |z| ≥ 3 in 824 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +14.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | +4.9 | +5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +5.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.6 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +0.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.0 | +0.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +4.0 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -4.1 | -6.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.1 | -8.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.9 | -7.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -2.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.8 | -2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -1.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.5 | +0.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.1 | -3.5 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | TIR domain containing adaptor protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q24.2 — chr11:126,282,497-126,298,845 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Mal, wyatt |
| Gene groups (HGNC) | TIR domain containing |
| Reactome | 15 pathways, smallest: MyD88 deficiency (TLR2/4); IRAK4 deficiency (TLR2/4); Diseases associated with the TLR signaling cascade |
| Matched by | ensembl_id |

**Function**, from UniProt [P58753](https://www.uniprot.org/uniprotkb/P58753) (Toll/interleukin-1 receptor domain-containing adapter protein):

> Adapter involved in TLR2, TLR4 and RAGE signaling pathways in the innate immune response. Acts via IRAK2 and TRAF-6, leading to the activation of NF-kappa-B, MAPK1, MAPK3 and JNK, and resulting in cytokine secretion and the inflammatory response. Positively regulates the production of TNF (TNF) and interleukin-6 (IL6).

**Summary**, from NCBI Gene [114609](https://www.ncbi.nlm.nih.gov/gene/114609):

> The innate immune system recognizes microbial pathogens through Toll-like receptors (TLRs), which identify pathogen-associated molecular patterns. Different TLRs recognize different pathogen-associated molecular patterns and all TLRs have a Toll-interleukin 1 receptor (TIR) domain, which is responsible for signal transduction. The protein encoded by this gene is a TIR adaptor protein involved in the TLR4 signaling pathway of the immune system. It activates NF-kappa-B, MAPK1, MAPK3 and JNK, …

**Accessions** — [HGNC:17192](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17192) · Entrez [114609](https://www.ncbi.nlm.nih.gov/gene/114609) · UniProt [P58753](https://www.uniprot.org/uniprotkb/P58753) · Ensembl [ENSG00000150455](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150455)

## Data

Gene col 7434: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7434); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7434, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7434]; `tensor/DDL_lfc|DDL_z.npy` [7434]; `embed/gene_vectors.npy` [7434]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7434 or target_col == 7434). Every well: [[TIRAP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TIRAP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
