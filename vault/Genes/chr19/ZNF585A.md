---
symbol: "ZNF585A"
type: "gene"
col: 12312
ensembl_id: "ENSG00000196967"
name: "zinc finger protein 585A"
location: "19q13.12"
module: 11
arm: "+"
pooled_cpm: 17.18
n_lines_expressing: 44
n_dd_up: 13
n_dd_down: 12
n_dd_up_clean: 12
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 7
direction_downstream: 2
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# ZNF585A

*zinc finger protein 585A* — 19q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.26× (z +22.4, q 0e+00, up in 38 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.575× (z -10.8, q 3e-24, down in 27 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM200A]] (+0.84, fdr 7e-06), [[PEX12]] (+0.79, fdr 7e-06), [[GIN1]] (+0.76, fdr 1e-05); moves opposite to [[TCF3]] (-0.69, fdr 7e-06), [[TBC1D24]] (-0.68, fdr 3e-05), [[NUTF2]] (-0.68, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[ZNF675]] → it (grade B ⚠); 2 go from it, the strongest it → [[ZNF585B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12312.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.26×** | +22.4 | 0e+00 | 38/40 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.62×** | +18.7 | 0e+00 | 37/40 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +12.7 | 2e-34 | 25/40 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.88×** | +11.8 | 4e-30 | 26/41 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.77×** | +11.1 | 2e-26 | 30/42 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.59×** | +9.0 | 1e-17 | 29/42 (RKO, A-427, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.36×** | +8.5 | 1e-15 | 21/42 (A-427, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +7.7 | 1e-12 | 21/42 (BT-474, PANC-1, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +6.2 | 3e-08 | 17/41 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +5.5 | 2e-06 | 11/41 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +4.2 | 0.001 | 1/42 (AN3 CA) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.22×** | +3.8 | 0.007 | 13/42 (A498, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | **1.20×** | +3.6 | 0.013 | 11/42 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.024 | 5/42 (RKO, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.21×** | +3.4 | 0.025 | 15/41 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | 1.19× | +3.3 | 0.035 | 14/41 (NCI-H460, A-427, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +3.2 | 0.042 | 8/42 (MIA PaCa-2, NCI-H1792, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12312.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.575×** | -10.8 | 3e-24 | 27/42 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.588×** | -10.3 | 1e-22 | 30/41 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.603×** | -9.8 | 2e-20 | 26/41 (HepG2/C3A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.726×** | -6.2 | 7e-08 | 21/41 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.737×** | -6.0 | 3e-07 | 20/41 (SW 900, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.743×** | -5.6 | 2e-06 | 18/38 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.760×** | -5.4 | 7e-06 | 14/42 (C32, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.758×** | -5.0 | 4e-05 | 14/30 (SW480, A-172, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.798×** | -4.4 | 7e-04 | 9/41 (BT-474, SK-MEL-2, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.803×** | -4.3 | 0.001 | 10/42 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.813×** | -4.0 | 0.003 | 13/41 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.818×** | -3.7 | 0.010 | 9/42 (CFPAC-1, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change | 0.834× | -3.4 | 0.029 | 11/23 (PANC-1, A-172, …) | all doses, flat | composition shift |
| [[Naproxen (drug)]] 0.05 µM |  | 0.846× | -3.0 | 0.10 | 7/41 (SW1417, A549, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12312. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 20.1 | 2 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.72× (z +11.0) | [[Digitoxin (drug)]] 5 µM 0.321× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.330× (z -9.3) |
| [[PANC-1 (line)]] | alt | 34.6 | 4 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +17.4) | [[Digitoxin (drug)]] 0.5 µM 0.481× (z -9.5) |
| [[SW480 (line)]] | alt | 17.1 | 3 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +17.6) | [[Digitoxin (drug)]] 0.5 µM 0.260× (z -11.8) |
| [[A-427 (line)]] | wt | 19.9 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 8.56× (z +15.4) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 37.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +9.8) | — |
| [[RPMI-7951 (line)]] | alt | 21.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +11.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.225× (z -8.5) ⚠ toxic |
| [[SW 900 (line)]] | alt | 25.3 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +8.9) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.190× (z -11.8) |
| [[A-172 (line)]] | wt | 14.8 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.228× (z -9.4) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 11.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0655× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Rifaximin (drug)]] 0.05 µM 0.0631× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 31.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +10.1) | — |
| [[NCI-H23 (line)]] | alt | 19.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.31× (z +15.9) | — |
| [[NCI-H460 (line)]] | wt | 57.6 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.15× (z +9.0) | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.213× (z -9.5) ⚠ toxic |
| [[BT-474 (line)]] | alt | 23.8 | 1 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.59× (z +8.8) | — |
| [[C32 (line)]] | wt | 12.4 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.184× (z -9.0) |
| [[HCT15 (line)]] | alt | 16.0 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.149× (z -8.5) |
| [[J82 (line)]] | alt | 20.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +9.1) | — |
| [[LOX-IMVI (line)]] | wt | 4.99 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0883× (z -8.8) |
| [[NCI-H661 (line)]] | alt | 44.9 | 0 | 1 | — | [[Ritonavir (drug)]] 0.5 µM 0.0430× (z -11.4) |
| [[SK-MEL-2 (line)]] | alt | 35.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +12.8) | — |
| [[A498 (line)]] | wt | 5.10 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.73 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.68 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.01 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.01 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12312), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM200A]] | +0.84 | +0.84 / +0.66 | both halves | 7e-06 |  |
| [[PEX12]] | +0.79 | +0.83 / +0.65 | both halves | 7e-06 |  |
| [[GIN1]] | +0.76 | +0.80 / +0.51 | both halves | 1e-05 |  |
| [[C1orf131]] | +0.76 | +0.84 / +0.59 | both halves | 7e-06 |  |
| [[MED18]] | +0.75 | +0.77 / +0.59 | both halves | 7e-06 |  |
| [[NAIF1]] | +0.74 | +0.78 / +0.53 | both halves | 1e-05 |  |
| [[CCDC174]] | +0.74 | +0.81 / +0.60 | both halves | 7e-06 |  |
| [[METTL25B]] | +0.72 | +0.79 / +0.54 | both halves | 1e-05 |  |
| [[MRPS31]] | +0.70 | +0.77 / +0.64 | both halves | 7e-06 |  |
| [[THAP2]] | +0.70 | +0.77 / +0.46 | both halves | 2e-05 |  |
| [[METTL18]] | +0.70 | +0.72 / +0.54 | both halves | 1e-05 |  |
| [[PPCS]] | +0.70 | +0.72 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCF3]] | -0.69 | -0.67 / -0.60 | both halves | 7e-06 |  |
| [[TBC1D24]] | -0.68 | -0.69 / -0.45 | both halves | 3e-05 |  |
| [[NUTF2]] | -0.68 | -0.70 / -0.57 | both halves | 1e-05 |  |
| [[FAM20B]] | -0.66 | -0.67 / -0.62 | both halves | 7e-06 |  |
| [[DCAF16]] | -0.66 | -0.72 / -0.42 | both halves | 4e-05 |  |
| [[TUFM]] | -0.64 | -0.62 / -0.30 | both halves | 2e-04 |  |
| [[INPP4A]] | -0.63 | -0.60 / -0.36 | both halves | 1e-04 |  |
| [[PIP4K2A]] | -0.63 | -0.71 / -0.37 | both halves | 8e-05 |  |
| [[MFSD14B]] | -0.63 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[MAPK9]] | -0.63 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[FAM118A]] | -0.62 | -0.68 / -0.24 | both halves | 5e-04 |  |
| [[CHID1]] | -0.62 | -0.61 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF675]] | B | ZNF675 activity raises ZNF585A's level | lines that do not express ZNF675 (5) vs lines expressing it (45) | 3.33× lower at baseline in the lines without ZNF675 | 0.019 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF573, ZNF420 |
| [[ZNF585B]] | B | ZNF585B activity raises ZNF585A's level | lines that do not express ZNF585B (12) vs lines expressing it (38) | 2.62× lower at baseline in the lines without ZNF585B | 0.025 | ⚠ within organs, on part of the lines; also absent: CYBRD1 |
| [[ZNF829]] | B | ZNF829 activity raises ZNF585A's level | lines that do not express ZNF829 (20) vs lines expressing it (30) | 2.14× lower at baseline in the lines without ZNF829 | 0.034 | ⚠ within organs, on part of the lines; also absent: ZNF568, ZNF880, ZNF625 |
| [[TOP2A]] | B | TOP2A activity lowers ZNF585A's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ZFP30]] | B | ZFP30 activity raises ZNF585A's level | lines that do not express ZFP30 (9) vs lines expressing it (41) | 2.55× lower at baseline in the lines without ZFP30 | 0.089 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF420, ZNF461 |
| [[PSMB5]] | B | PSMB5 activity raises ZNF585A's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZNF429]] | B | ZNF429 activity raises ZNF585A's level | lines that do not express ZNF429 (11) vs lines expressing it (39) | 2.17× lower at baseline in the lines without ZNF429 | 0.098 | ⚠ within organs, on part of the lines; also absent: ZNF724, ENSG00000283201, ZNF254 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF585B]] | B | ZNF585A activity raises ZNF585B's level | lines that do not express ZNF585A (6) vs lines expressing it (44) | 3.77× lower at baseline in the lines without ZNF585A | 0.076 | ⚠ within organs, on part of the lines; also absent: ZFP14, WWTR1, ZNF540 |
| [[RSPRY1]] | B | ZNF585A activity raises RSPRY1's level | lines that do not express ZNF585A (6) vs lines expressing it (44) | 1.37× lower at baseline in the lines without ZNF585A | 0.099 | ⚠ within organs, on part of the lines; also absent: ZFP14, WWTR1, ZNF540 |

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.746). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-33.3, 5.1); signed map (4.3, -20.2). **Vector** length 80.9, 15.2% of its response variance represented; |z| ≥ 3 in 884 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.4 | +22.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.7 | +18.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.6 | +11.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.7 | +11.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +9.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +7.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.1 | +3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.6 | -0.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -4.4 | -10.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -1.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | +0.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.3 | -5.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.2 | -6.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -5.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | +1.8 |
|  | [[Clonidine (hydrochloride) (drug)]] 5 µM |  | -1.1 | -0.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.0 | -2.4 |
|  | [[Folic acid (drug)]] 5 µM |  | -1.0 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 585A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.12 — chr19:37,106,734-37,172,741 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23765, Zfp27 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P3V2](https://www.uniprot.org/uniprotkb/Q6P3V2) (Zinc finger protein 585A):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [199704](https://www.ncbi.nlm.nih.gov/gene/199704):

> Predicted to enable transcription cis-regulatory region binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26305](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26305) · Entrez [199704](https://www.ncbi.nlm.nih.gov/gene/199704) · UniProt [Q6P3V2](https://www.uniprot.org/uniprotkb/Q6P3V2) · Ensembl [ENSG00000196967](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196967)

## Data

Gene col 12312: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12312); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12312, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12312]; `tensor/DDL_lfc|DDL_z.npy` [12312]; `embed/gene_vectors.npy` [12312]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12312 or target_col == 12312). Every well: [[ZNF585A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF585A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
