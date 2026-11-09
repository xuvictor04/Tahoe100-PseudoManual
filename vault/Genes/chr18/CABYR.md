---
symbol: "CABYR"
type: "gene"
col: 7763
ensembl_id: "ENSG00000154040"
name: "calcium binding tyrosine phosphorylation regulated"
location: "18q11.2"
module: 80
arm: "+"
pooled_cpm: 10.6
n_lines_expressing: 44
n_dd_up: 22
n_dd_down: 9
n_dd_up_clean: 18
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# CABYR

*calcium binding tyrosine phosphorylation regulated* — 18q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.20× (z +29.1, q 0e+00, up in 37 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.565× (z -8.2, q 2e-13, down in 25 of 41 measured lines).
> Its strongest partners by |cos| (58 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 42 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF341-AS1]] (+0.70, fdr 3e-05), [[LINC00863]] (+0.67, fdr 5e-05), [[EFCAB5]] (+0.66, fdr 4e-05); moves opposite to [[C20orf27]] (-0.60, fdr 0.002, ⚠ one half only (not replicated)), [[SMYD3]] (-0.59, fdr 6e-04), [[ELP1]] (-0.58, fdr 3e-04), [[MRPL4]] (-0.57, fdr 2e-04).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[DNAJC6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7763.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.20×** | +29.1 | 0e+00 | 37/37 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.82×** | +21.0 | 0e+00 | 31/38 (NCI-H1792, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.00×** | +14.0 | 2e-42 | 29/40 (A-172, A549, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.13×** | +12.5 | 8e-34 | 24/34 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.18×** | +11.2 | 5e-27 | 25/37 (MIA PaCa-2, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.76×** | +11.1 | 7e-27 | 28/38 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.58×** | +9.2 | 2e-18 | 24/41 (HS-578T, A-172, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.11×** | +8.2 | 1e-14 | 20/31 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.66×** | +7.3 | 2e-11 | 21/39 (A-172, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.55×** | +6.2 | 2e-08 | 16/38 (BT-474, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +6.0 | 1e-07 | 14/39 (SW480, HCT15, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.46×** | +5.5 | 2e-06 | 15/41 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.45×** | +5.3 | 4e-06 | 16/41 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.33×** | +4.1 | 0.002 | 16/39 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +4.0 | 0.002 | 12/40 (SW1417, BT-474, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.31×** | +3.9 | 0.003 | 12/39 (A549, A-172, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7763.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.565×** | -8.2 | 2e-13 | 25/41 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.599×** | -7.3 | 8e-11 | 20/35 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.625×** | -6.7 | 4e-09 | 22/40 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.490×** | -5.3 | 1e-05 | 16/39 (PANC-1, C-33 A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.522×** | -4.9 | 1e-04 | 17/35 (RPMI-7951, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.778×** | -3.6 | 0.029 | 8/41 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.779×** | -3.6 | 0.029 | 11/40 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.724×** | -3.5 | 0.029 | 14/32 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Menadione (drug)]] 0.05 µM |  | **0.781×** | -3.3 | 0.069 | 8/35 (C32, RKO, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.803× | -3.1 | 0.10 | 7/41 (SW480, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7763. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 24.0 | 4 | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.44× (z +20.7) | [[Digitoxin (drug)]] 5 µM 0.0772× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.296× (z -9.6) |
| [[PANC-1 (line)]] | alt | 20.2 | 1 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +11.1) | [[Digitoxin (drug)]] 5 µM 0.202× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.232× (z -12.4) |
| [[HOP62 (line)]] | alt | 4.24 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 9.41× (z +12.3) | [[Temsirolimus (drug)]] 0.5 µM 0.106× (z -8.8) |
| [[LoVo (line)]] | wt | 8.25 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.61× (z +13.7) | [[Belinostat (drug)]] 0.5 µM 0.130× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 11.5 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.58× (z +12.7) | [[Digitoxin (drug)]] 5 µM 0.125× (z -10.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 19.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.28× (z +18.2) | — |
| [[A549 (line)]] | wt | 15.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.78× (z +17.2) | — |
| [[AsPC-1 (line)]] | alt | 4.64 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.21× (z +11.5) | — |
| [[C32 (line)]] | wt | 9.25 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.93× (z +9.3) | [[Imiquimod (maleate) (drug)]] 0.05 µM 0.0817× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 5.06 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.0× (z +12.8) | — |
| [[HS-578T (line)]] | alt | 8.70 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.10× (z +9.9) | — |
| [[J82 (line)]] | alt | 8.28 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.34× (z +12.6) | — |
| [[LS 180 (line)]] | wt | 3.93 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.94× (z +10.2) | [[Medroxyprogesterone acetate (drug)]] 0.05 µM 0.0773× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 36.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.85× (z +18.6) | — |
| [[NCI-H2347 (line)]] | alt | 8.73 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +10.8) | [[Digitoxin (drug)]] 5 µM 0.185× (z -8.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 4.40 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.48× (z +9.2) | — |
| [[SW480 (line)]] | alt | 11.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.87× (z +11.9) | — |
| [[A-427 (line)]] | wt | 37.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.248× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~6% of this change |
| [[BT-474 (line)]] | alt | 6.96 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.46× (z +9.9) | — |
| [[HEC-1-A (line)]] | alt | 4.60 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.100× (z -9.4) ⚠ toxic; unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 12.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.98× (z +10.1) | — |
| [[RPMI-7951 (line)]] | alt | 10.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.67× (z +9.1) | — |
| [[A498 (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.43 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.62 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.26 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.37 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.45 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.11 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7763), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 38 of them with an alert (⚠; 38 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF341-AS1]] | +0.70 | +0.64 / +0.43 | both halves | 3e-05 |  |
| [[LINC00863]] | +0.67 | +0.71 / +0.39 | both halves | 5e-05 |  |
| [[EFCAB5]] | +0.66 | +0.67 / +0.41 | both halves | 4e-05 |  |
| [[GCNT4]] | +0.66 | +0.60 / +0.35 | both halves | 1e-04 |  |
| [[PPP1R12A-AS2]] | +0.64 | +0.68 / +0.28 | both halves | 3e-04 |  |
| [[LINC00944]] | +0.64 | +0.57 / +0.36 | both halves | 1e-04 |  |
| [[KRBOX5]] | +0.64 | +0.69 / +0.35 | both halves | 1e-04 |  |
| [[LACC1]] | +0.64 | +0.74 / +0.35 | both halves | 1e-04 |  |
| [[TYMSOS]] | +0.63 | +0.67 / +0.40 | both halves | 5e-05 |  |
| [[PBLD]] | +0.63 | +0.70 / +0.04 | ⚠ one half (not replicated) | 0.006 |  |
| [[DENND5B-AS1]] | +0.63 | +0.56 / +0.35 | both halves | 1e-04 |  |
| [[LINC02955]] | +0.62 | +0.63 / +0.27 | both halves | 3e-04 |  |
| [[LINC02542]] | +0.62 | +0.68 / +0.20 | both halves | 7e-04 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C20orf27]] | -0.60 | -0.57 / -0.11 | ⚠ one half (not replicated) | 0.002 |  |
| [[SMYD3]] | -0.59 | -0.50 / -0.21 | both halves | 6e-04 |  |
| [[ELP1]] | -0.58 | -0.49 / -0.26 | both halves | 3e-04 |  |
| [[STUB1]] | -0.58 | -0.44 / -0.01 | ⚠ not reproduced | 0.008 |  |
| [[MRPL4]] | -0.57 | -0.38 / -0.30 | both halves | 2e-04 |  |
| [[RSU1]] | -0.57 | -0.50 / -0.27 | both halves | 3e-04 |  |
| [[PCMT1]] | -0.56 | -0.62 / +0.03 | ⚠ one half (not replicated) | 1.00 |  |
| [[NUDT21]] | -0.56 | -0.62 / -0.31 | both halves | 2e-04 |  |
| [[WDR5]] | -0.55 | -0.58 / -0.31 | both halves | 2e-04 |  |
| [[PAFAH1B3]] | -0.55 | -0.48 / +0.06 | ⚠ not reproduced | 1.00 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CABYR's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.9% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TP53]] | C | TP53 activity strengthens CABYR's drug response | recorded loss-of-function mutation of TP53 in 27 lines vs 14 not recorded | the TP53-altered lines respond 1.04× as strongly (z diff -0.09); strongest at Topotecan (hydrochloride) 5 µM: 1.56x vs 2.77x (z diff +2.7) | 0.907 over the table, 0.086 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DNAJC6]] | B | CABYR activity raises DNAJC6's level | lines that do not express CABYR (6) vs lines expressing it (44) | 2.09× lower at baseline in the lines without CABYR | 0.012 | ⚠ within organs, on part of the lines; also absent: SUGCT, GABBR1, CLTCL1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.696). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.6, 10.5); signed map (23.1, -5.7). **Vector** length 74.0, 13.7% of its response variance represented; |z| ≥ 3 in 1,007 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.8 | +29.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.2 | +21.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.0 | +14.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +4.9 | +7.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +12.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +6.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.7 | +1.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.6 | +3.9 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | +0.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.2 | +4.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.9 | +5.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.7 | -6.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.5 | +0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -4.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.7 | -2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | +0.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | -2.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.2 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | calcium binding tyrosine phosphorylation regulated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q11.2 — chr18:24,138,987-24,161,600 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FSP-2, CBP86, CT88 |
| Matched by | ensembl_id |

**Function**, from UniProt [O75952](https://www.uniprot.org/uniprotkb/O75952) (Calcium-binding tyrosine phosphorylation-regulated protein):

> May function as a regulator of both motility- and head-associated functions such as capacitation and the acrosome reaction. Isoform 1 binds calcium in vitro. Isoform 2 and isoform 6 probably bind calcium. Isoform 3 and isoform 5 do not bind calcium in vitro. Isoform 4 probably does not bind calcium.

**Summary**, from NCBI Gene [26256](https://www.ncbi.nlm.nih.gov/gene/26256):

> To reach fertilization competence, spermatozoa undergo a series of morphological and molecular maturational processes, termed capacitation, involving protein tyrosine phosphorylation and increased intracellular calcium. The protein encoded by this gene localizes to the principal piece of the sperm flagellum in association with the fibrous sheath and exhibits calcium-binding when phosphorylated during capacitation. A pseudogene on chromosome 3 has been identified for this gene. Alternatively …

**Accessions** — [HGNC:15569](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15569) · Entrez [26256](https://www.ncbi.nlm.nih.gov/gene/26256) · UniProt [O75952](https://www.uniprot.org/uniprotkb/O75952) · Ensembl [ENSG00000154040](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154040)

## Data

Gene col 7763: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7763); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7763, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7763]; `tensor/DDL_lfc|DDL_z.npy` [7763]; `embed/gene_vectors.npy` [7763]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7763 or target_col == 7763). Every well: [[CABYR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CABYR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
