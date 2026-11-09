---
symbol: "ALKBH1"
type: "gene"
col: 1998
ensembl_id: "ENSG00000100601"
name: "alkB homolog 1, histone H2A dioxygenase"
location: "14q24.3"
module: 114
arm: "+"
pooled_cpm: 30.61
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 5
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/114"]
generated_by: "tahoemap"
---

# ALKBH1

*alkB homolog 1, histone H2A dioxygenase* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.64× (z +11.7, q 1e-28, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.511× (z -15.8, q 0e+00, down in 31 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.809× (z -7.0, q 2e-10, down in 19 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (NCI-H2030 0.166×, CFPAC-1 0.200×, Panc 03.27 0.202×, NCI-H23 0.206×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (SHP-77 0.0853×, PANC-1 0.268×, C32 0.112×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (LoVo 0.137×, C32 0.113×; ⚠ toxic; transcription drop); [[Trimetrexate (drug)]] 0.5 µM in 1 line (CHP-212 0.0534×); [[Cyclosporin A (drug)]] 0.5 µM in 1 line (SW 1271 0.0673×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF3]] (+0.82, fdr 7e-06), [[FBXO28]] (+0.81, fdr 7e-06), [[BRAP]] (+0.80, fdr 7e-06); moves opposite to [[ELOVL5]] (-0.61, fdr 7e-06).
> It is in [[Module 114]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1998.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.64×** | +11.7 | 1e-28 | 36/47 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.57×** | +11.6 | 2e-28 | 38/48 (MIA PaCa-2, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.35×** | +10.0 | 4e-21 | 28/47 (NCI-H1573, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.97×** | +8.3 | 1e-14 | 28/48 (MIA PaCa-2, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.28×** | +8.2 | 4e-14 | 27/48 (Hs 766T, J82, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM |  | **1.42×** | +8.0 | 2e-13 | 33/48 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.35×** | +7.0 | 1e-10 | 26/48 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +6.9 | 3e-10 | 24/48 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +6.1 | 6e-08 | 22/47 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.30×** | +6.1 | 6e-08 | 24/48 (A-427, A549, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.26×** | +5.5 | 2e-06 | 17/47 (NCI-H2347, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +5.1 | 2e-05 | 21/48 (MIA PaCa-2, HEC-1-A, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +4.1 | 0.002 | 10/48 (HEC-1-A, SW1417, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.23×** | +3.5 | 0.020 | 6/48 (PANC-1, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.16× | +3.4 | 0.021 | 13/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.15× | +3.3 | 0.036 | 11/47 (SW 900, A-172, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.054 | 4/48 (HEC-1-A, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1998.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (NCI-H2030 0.166×, CFPAC-1 0.200×, Panc 03.27 0.202×, NCI-H23 0.206×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (SHP-77 0.0853×, PANC-1 0.268×, C32 0.112×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (LoVo 0.137×, C32 0.113×; ⚠ toxic; transcription drop); [[Trimetrexate (drug)]] 0.5 µM in 1 line (CHP-212 0.0534×); [[Cyclosporin A (drug)]] 0.5 µM in 1 line (SW 1271 0.0673×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.511×** | -15.8 | 0e+00 | 31/44 (NCI-H2030, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.572×** | -12.6 | 6e-34 | 38/47 (SHP-77, J82, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.603×** | -11.4 | 8e-28 | 28/38 (LoVo, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.668×** | -8.7 | 3e-16 | 25/41 (SHP-77, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.809×** | -7.0 | 2e-10 | 19/48 (SW480, SNU-423, …) | rises with dose |  |
| [[Gefitinib (drug)]] 5 µM |  | 0.864× | -3.4 | 0.058 | 7/48 (NCI-H460, SW480, …) | top dose only |  |
| [[Cyclosporin A (drug)]] 0.05 µM |  | 0.869× | -3.3 | 0.085 | 7/48 (A-172, J82, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.873× | -3.1 | 0.15 | 13/48 (PANC-1, A549, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1998. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 29.7 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.06× (z +9.9) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -13.2) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 27.8 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.268× (z -14.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 40.0 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0853× (z -20.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 42.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -16.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 24.7 | 2 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.99× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.137× (z -16.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 37.2 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.79× (z +9.0) | [[Niclosamide (olamine) (drug)]] 5 µM 0.353× (z -9.0) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 36.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -11.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 25.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -13.4) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 34.4 | 0 | 2 (1 ⚠) | — | [[Trimetrexate (drug)]] 0.5 µM 0.0534× (z -12.3) |
| [[NCI-H1792 (line)]] | alt | 39.4 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.37× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -14.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 46.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.166× (z -17.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 39.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.206× (z -15.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 30.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -12.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 32.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.343× (z -9.2) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 41.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -12.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 27.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.228× (z -13.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 35.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.363× (z -9.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 20.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.200× (z -9.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 28.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.257× (z -11.8) ⚠ toxic |
| [[KATO III (line)]] | alt | 30.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.339× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 30.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +10.5) | — |
| [[Panc 03.27 (line)]] | alt | 44.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -15.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 32.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -14.4) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 46.3 | 0 | 1 | — | [[Cyclosporin A (drug)]] 0.5 µM 0.0673× (z -8.8) |
| [[SW480 (line)]] | alt | 41.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.466× (z -10.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1998), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF3]] | +0.82 | +0.83 / +0.76 | both halves | 7e-06 |  |
| [[FBXO28]] | +0.81 | +0.76 / +0.75 | both halves | 7e-06 |  |
| [[BRAP]] | +0.80 | +0.81 / +0.71 | both halves | 7e-06 |  |
| [[TTF1]] | +0.79 | +0.84 / +0.76 | both halves | 7e-06 |  |
| [[ZC3HC1]] | +0.77 | +0.73 / +0.79 | both halves | 7e-06 |  |
| [[TEFM]] | +0.76 | +0.73 / +0.73 | both halves | 7e-06 |  |
| [[ABRAXAS2]] | +0.75 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[ALKBH4]] | +0.74 | +0.74 / +0.69 | both halves | 7e-06 | same gene group; STRING 955 |
| [[ZNF791]] | +0.74 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[MAU2]] | +0.73 | +0.76 / +0.69 | both halves | 7e-06 |  |
| [[ZNF721]] | +0.73 | +0.76 / +0.66 | both halves | 7e-06 |  |
| [[TRIM4]] | +0.73 | +0.75 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELOVL5]] | -0.61 | -0.61 / -0.58 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 114]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.873). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-41.6, 5.5); signed map (-4.6, -14.4). **Vector** length 96.1, 21.0% of its response variance represented; |z| ≥ 3 in 894 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.4 | +11.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | +5.3 | +8.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.0 | +11.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.9 | +6.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.7 | +8.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +3.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.1 | +3.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | +2.0 | +2.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.9 | +2.0 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -8.0 | -12.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.1 | -15.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.0 | -8.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.8 | -11.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | -7.0 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.5 | -3.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.5 | -0.9 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.9 | -1.8 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -1.7 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | alkB homolog 1, histone H2A dioxygenase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:77,672,404-77,708,023 (-) |
| Ensembl biotype | protein_coding |
| Also known as | hABH, alkB, ABH; previously ALKBH |
| Gene groups (HGNC) | Alkylation repair homologs; DNA-(apurinic or apyrimidinic site) lyases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13686](https://www.uniprot.org/uniprotkb/Q13686) (Nucleic acid dioxygenase ALKBH1):

> Dioxygenase that acts on nucleic acids, such as DNA and tRNA. Requires molecular oxygen, alpha-ketoglutarate and iron. A number of activities have been described for this dioxygenase, but recent results suggest that it mainly acts on tRNAs and mediates their demethylation or oxidation depending on the context and subcellular compartment. Mainly acts as a tRNA demethylase by removing N(1)-methyladenine from various tRNAs, with a preference for N(1)-methyladenine at position 58 (m1A58) present on …

**Summary**, from NCBI Gene [8846](https://www.ncbi.nlm.nih.gov/gene/8846):

> This gene encodes a homolog to the E. coli alkB gene product. The E. coli alkB protein is part of the adaptive response mechanism of DNA alkylation damage repair. It is involved in damage reversal by oxidative demethylation of 1-methyladenine and 3-methylcytosine. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17911](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17911) · Entrez [8846](https://www.ncbi.nlm.nih.gov/gene/8846) · UniProt [Q13686](https://www.uniprot.org/uniprotkb/Q13686) · Ensembl [ENSG00000100601](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100601)

## Data

Gene col 1998: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1998); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1998, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1998]; `tensor/DDL_lfc|DDL_z.npy` [1998]; `embed/gene_vectors.npy` [1998]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1998 or target_col == 1998). Every well: [[ALKBH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALKBH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
