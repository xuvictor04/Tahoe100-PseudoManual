---
symbol: "NEK8"
type: "gene"
col: 8360
ensembl_id: "ENSG00000160602"
name: "NIMA related kinase 8"
location: "17q11.2"
module: 80
arm: "+"
pooled_cpm: 5.55
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 5
n_dd_up_clean: 20
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# NEK8

*NIMA related kinase 8* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.42× (z +24.4, q 0e+00, up in 37 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.502× (z -6.4, q 7e-08, down in 29 of 45 measured lines).
> Its strongest partners by |cos| (83 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 17 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MZF1-AS1]] (+0.81, fdr 2e-05), [[ZNF341-AS1]] (+0.79, fdr 1e-05), [[GPR137]] (+0.78, fdr 1e-05); moves opposite to [[NDRG3]] (-0.67, fdr 3e-05).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8360.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.42×** | +24.4 | 0e+00 | 37/37 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.14×** | +15.0 | 0e+00 | 32/37 (LoVo, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.63×** | +11.5 | 2e-28 | 27/34 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.89×** | +9.5 | 4e-19 | 32/42 (LoVo, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.78×** | +9.1 | 9e-18 | 31/40 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.56×** | +8.4 | 6e-15 | 8/11 (HEC-1-A, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.47×** | +8.1 | 7e-14 | 25/32 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.35×** | +7.9 | 2e-13 | 15/22 (J82, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.32×** | +7.8 | 5e-13 | 25/37 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.75×** | +7.3 | 2e-11 | 29/45 (HOP62, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.10×** | +6.4 | 1e-08 | 9/15 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.43×** | +4.7 | 1e-04 | 16/45 (HT-29, SW1417, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.53×** | +3.9 | 0.004 | 13/45 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.50×** | +3.7 | 0.008 | 11/44 (PANC-1, C-33 A, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.53×** | +3.6 | 0.011 | 12/35 (PANC-1, LS 180, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.48×** | +3.6 | 0.011 | 8/43 (HCT15, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.028 | 9/44 (A498, HOP62, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.97×** | +3.3 | 0.033 | 4/37 (LOX-IMVI, C32, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.39×** | +3.0 | 0.066 | 16/44 (A-427, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8360.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.502×** | -6.4 | 7e-08 | 29/45 (hTERT-HPNE, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.559×** | -5.4 | 2e-05 | 22/44 (KATO III, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.571×** | -5.2 | 3e-05 | 21/46 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.641×** | -4.2 | 0.004 | 16/43 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.673×** | -3.7 | 0.024 | 11/45 (PANC-1, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.712× | -3.2 | 0.13 | 6/45 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.789× | -3.2 | 0.13 | 12/44 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.722× | -3.1 | 0.16 | 14/43 (PANC-1, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8360. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 11.0 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.66× (z +13.7) | [[Digitoxin (drug)]] 0.5 µM 0.165× (z -11.4) |
| [[HOP62 (line)]] | alt | 3.41 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.7× (z +12.6) | [[Phenytoin (sodium) (drug)]] 0.05 µM 0.0531× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 2.92 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.6× (z +14.7) | — |
| [[A498 (line)]] | wt | 4.84 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.75× (z +12.9) | — |
| [[C32 (line)]] | wt | 3.84 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.2× (z +11.0) | — |
| [[HS-578T (line)]] | alt | 3.19 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +9.9) | — |
| [[LoVo (line)]] | wt | 6.29 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.48× (z +13.0) | — |
| [[SW480 (line)]] | alt | 5.14 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.64× (z +11.0) | — |
| [[A-172 (line)]] | wt | 3.51 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.3× (z +10.8) | — |
| [[A549 (line)]] | wt | 4.79 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.88× (z +10.3) | — |
| [[AsPC-1 (line)]] | alt | 2.97 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.71× (z +8.9) | — |
| [[BT-474 (line)]] | alt | 10.4 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0976× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 4.96 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.70× (z +9.7) | — |
| [[COLO 205 (line)]] | alt | 13.2 | 0 | 1 | — | [[Menadione (drug)]] 0.05 µM 0.0784× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 9.62 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.92× (z +10.1) | — |
| [[KATO III (line)]] | alt | 10.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.48× (z +9.0) | — |
| [[LOX-IMVI (line)]] | wt | 5.71 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.09× (z +9.5) | — |
| [[LS 180 (line)]] | wt | 4.19 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.24× (z +9.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 4.41 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.68× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 6.51 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.40× (z +9.8) | — |
| [[NCI-H2030 (line)]] | alt | 8.11 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.71× (z +11.3) | — |
| [[NCI-H23 (line)]] | alt | 8.13 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.72× (z +9.4) | — |
| [[NCI-H2347 (line)]] | alt | 3.46 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.57× (z +11.0) | — |
| [[Panc 03.27 (line)]] | alt | 6.39 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.25× (z +8.9) | — |
| [[SNU-423 (line)]] | alt | 4.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.79× (z +8.9) | — |
| [[SW1417 (line)]] | alt | 7.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.51× (z +9.0) | — |
| [[A-427 (line)]] | wt | 7.20 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.78 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8360), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 17 of them with an alert (⚠; 17 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MZF1-AS1]] | +0.81 | +0.86 / +0.47 | both halves | 2e-05 |  |
| [[ZNF341-AS1]] | +0.79 | +0.73 / +0.52 | both halves | 1e-05 |  |
| [[GPR137]] | +0.78 | +0.79 / +0.55 | both halves | 1e-05 |  |
| [[ENO3]] | +0.78 | +0.78 / +0.64 | both halves | 7e-06 |  |
| [[BOLA1]] | +0.77 | +0.82 / +0.60 | both halves | 7e-06 |  |
| [[RAD9B]] | +0.75 | +0.75 / +0.37 | both halves | 8e-05 |  |
| [[PPP1R12A-AS2]] | +0.75 | +0.80 / +0.18 | ⚠ one half (not replicated) | 1e-03 |  |
| [[TMEM202-AS1]] | +0.75 | +0.78 / +0.26 | both halves | 4e-04 |  |
| [[THAP2]] | +0.74 | +0.78 / +0.28 | both halves | 3e-04 |  |
| [[IL34]] | +0.74 | +0.77 / +0.43 | both halves | 3e-05 |  |
| [[CCT6B]] | +0.74 | +0.77 / +0.33 | both halves | 1e-04 |  |
| [[PCBP1-AS1]] | +0.74 | +0.77 / +0.24 | both halves | 4e-04 |  |
| [[PBLD]] | +0.74 | +0.74 / +0.23 | both halves | 5e-04 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDRG3]] | -0.67 | -0.62 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NEK8's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises NEK8's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PTPN6]] | B | PTPN6 activity raises NEK8's level | lines that do not express PTPN6 (8) vs lines expressing it (42) | 1.50× lower at baseline in the lines without PTPN6 | 0.067 | ⚠ within organs, on part of the lines; also absent: LMTK3, ENSG00000257252; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.860). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.1, 10.6); signed map (21.7, -5.9). **Vector** length 92.2, 19.4% of its response variance represented; |z| ≥ 3 in 1,044 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.5 | +24.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.5 | +15.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +11.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.0 | +7.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.8 | +7.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +2.6 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +2.3 | +2.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.0 | +2.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.9 | +3.3 |
| fall | [[Belinostat (drug)]] 5 µM |  | -5.4 | -6.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.9 | -5.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.3 | -3.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.2 | -5.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.6 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | -3.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.5 | -1.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | NIMA related kinase 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:28,725,897-28,743,455 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NPHP9 |
| Gene groups (HGNC) | NIMA related kinase family; Inversin complex subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86SG6](https://www.uniprot.org/uniprotkb/Q86SG6) (Serine/threonine-protein kinase Nek8):

> Required for renal tubular integrity. May regulate local cytoskeletal structure in kidney tubule epithelial cells. May regulate ciliary biogenesis through targeting of proteins to the cilia. Plays a role in organogenesis, and is involved in the regulation of the Hippo signaling pathway.

**Summary**, from NCBI Gene [284086](https://www.ncbi.nlm.nih.gov/gene/284086):

> This gene encodes a member of the serine/threionine protein kinase family related to NIMA (never in mitosis, gene A) of Aspergillus nidulans. The encoded protein may play a role in cell cycle progression from G2 to M phase. Mutations in the related mouse gene are associated with a disease phenotype that closely parallels the juvenile autosomal recessive form of polycystic kidney disease in humans. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:13387](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13387) · Entrez [284086](https://www.ncbi.nlm.nih.gov/gene/284086) · UniProt [Q86SG6](https://www.uniprot.org/uniprotkb/Q86SG6) · Ensembl [ENSG00000160602](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160602)

## Data

Gene col 8360: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8360); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8360, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8360]; `tensor/DDL_lfc|DDL_z.npy` [8360]; `embed/gene_vectors.npy` [8360]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8360 or target_col == 8360). Every well: [[NEK8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NEK8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
