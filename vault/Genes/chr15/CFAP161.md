---
symbol: "CFAP161"
type: "gene"
col: 7957
ensembl_id: "ENSG00000156206"
name: "cilia and flagella associated protein 161"
location: "15q25.1"
module: 47
arm: "+"
pooled_cpm: 21.32
n_lines_expressing: 44
n_dd_up: 9
n_dd_down: 23
n_dd_up_clean: 7
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 5
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# CFAP161

*cilia and flagella associated protein 161* — 15q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.64× (z +10.9, q 7e-25, up in 21 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (13 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.336× (z -8.6, q 3e-15, down in 34 of 42 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.485× (z -8.1, q 8e-14, down in 33 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC2A9]] (+0.73, fdr 7e-06), [[STAC3]] (+0.72, fdr 7e-06), [[MYH3]] (+0.71, fdr 7e-06); moves opposite to [[TMEM9]] (-0.65, fdr 7e-06), [[PEX3]] (-0.65, fdr 7e-06), [[SPATA7]] (-0.61, fdr 1e-05).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MTNR1A]] → it (grade B ⚠); 5 go from it, the strongest it → [[AHRR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7957.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.64×** | +10.9 | 7e-25 | 21/38 (LoVo, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **2.88×** | +7.9 | 6e-13 | 34/40 (LoVo, C32, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.49×** | +7.2 | 1e-10 | 18/36 (C32, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **2.26×** | +6.5 | 1e-08 | 37/42 (LoVo, C32, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **2.14×** | +5.8 | 8e-07 | 28/39 (NCI-H23, HS-578T, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.62×** | +3.5 | 0.039 | 10/30 (SW 900, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **2.28×** | +3.4 | 0.053 | 13/42 (LoVo, C32, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dapagliflozin (drug)]] 0.05 µM |  | **1.51×** | +3.3 | 0.073 | 18/42 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +3.2 | 0.084 | 9/27 (SW 900, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.51× | +3.1 | 0.10 | 19/39 (NCI-H460, RPMI-7951, …) | rises with dose |  |
| [[crizotinib (drug)]] 5 µM |  | 1.49× | +3.0 | 0.13 | 13/41 (J82, H4, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7957.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.336×** | -8.6 | 3e-15 | 34/42 (SW480, BT-474, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.353×** | -8.2 | 5e-14 | 31/42 (NCI-H1573, KATO III, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.359×** | -8.1 | 8e-14 | 33/41 (SW480, KATO III, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.485×** | -8.1 | 8e-14 | 33/42 (KATO III, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.383×** | -7.6 | 3e-12 | 33/39 (KATO III, AsPC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.430×** | -6.7 | 2e-09 | 32/40 (BT-474, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.466×** | -6.0 | 1e-07 | 28/42 (SW480, KATO III, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.470×** | -6.0 | 2e-07 | 27/40 (KATO III, SW480, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.540×** | -4.9 | 6e-05 | 27/40 (KATO III, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.527×** | -4.9 | 6e-05 | 26/36 (HT-29, H4, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.334×** | -4.5 | 3e-04 | 22/41 (KATO III, H4, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.574×** | -4.4 | 5e-04 | 25/41 (KATO III, SW48, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.701×** | -4.0 | 0.003 | 24/42 (CFPAC-1, COLO 205, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.618×** | -3.8 | 0.006 | 21/39 (SW48, BT-474, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.608×** | -3.7 | 0.007 | 21/40 (PANC-1, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.637×** | -3.4 | 0.020 | 20/39 (HCT15, RPMI-7951, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.651×** | -3.4 | 0.021 | 19/40 (KATO III, SW480, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.492×** | -2.9 | 0.084 | 10/37 (LS 180, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.493×** | -2.9 | 0.085 | 9/42 (SW480, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.68 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7957. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 59.2 | 0 | 11 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0587× (z -17.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.274× (z -11.1) |
| [[SW480 (line)]] | alt | 33.9 | 0 | 10 (9 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.139× (z -11.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.275× (z -10.8) |
| [[BT-474 (line)]] | alt | 41.4 | 0 | 7 (5 ⚠) | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0499× (z -14.2) |
| [[HT-29 (line)]] | alt | 37.0 | 0 | 6 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0367× (z -16.6) ⚠ toxic; cell-cycle shift, explains ~28% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.246× (z -10.4) |
| [[AsPC-1 (line)]] | alt | 58.2 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0647× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[PANC-1 (line)]] | alt | 33.0 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.112× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.321× (z -8.7) |
| [[H4 (line)]] | wt | 43.9 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0794× (z -10.2) ⚠ toxic; cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0202× (z -8.5) |
| [[LoVo (line)]] | wt | 46.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.34× (z +14.3) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.176× (z -8.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H1573 (line)]] | alt | 17.4 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +10.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0561× (z -12.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW1417 (line)]] | alt | 54.5 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.187× (z -9.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[C32 (line)]] | wt | 14.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +12.1) | — |
| [[LS 180 (line)]] | wt | 20.5 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.106× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 6.58 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 10.4× (z +8.7) | [[Digitoxin (drug)]] 5 µM 0.0755× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[NCI-H23 (line)]] | alt | 10.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 9.04× (z +8.7) | [[Digitoxin (drug)]] 5 µM 0.0863× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[A-172 (line)]] | wt | 6.33 | 0 | 1 | — | [[5-Azacytidine (drug)]] 0.5 µM 0.0803× (z -8.6) |
| [[A-427 (line)]] | wt | 11.3 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0644× (z -10.6) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A549 (line)]] | wt | 21.8 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.213× (z -8.5) |
| [[C-33 A (line)]] | alt | 19.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0963× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[COLO 205 (line)]] | alt | 22.7 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.103× (z -8.9) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HCT15 (line)]] | alt | 12.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.14× (z +9.4) | — |
| [[HEC-1-A (line)]] | alt | 24.9 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.218× (z -8.5) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HOP62 (line)]] | alt | 10.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.70× (z +10.5) | — |
| [[Hs 766T (line)]] | wt | 23.2 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.130× (z -9.1) ⚠ cell-cycle shift, explains ~29% of this change |
| [[hTERT-HPNE (line)]] | wt | 10.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.95× (z +9.2) | — |
| [[LOX-IMVI (line)]] | wt | 7.73 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +8.6) | — |
| [[NCI-H460 (line)]] | wt | 12.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +9.5) | — |
| [[RPMI-7951 (line)]] | alt | 25.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.27× (z +10.4) | — |
| [[SW48 (line)]] | wt | 54.1 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0842× (z -9.3) |
| [[A498 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.90 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.45 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.39 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.97 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 9.47 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.08 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.52 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.93 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7957), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC2A9]] | +0.73 | +0.81 / +0.60 | both halves | 7e-06 |  |
| [[STAC3]] | +0.72 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[MYH3]] | +0.71 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[RNF32-AS1]] | +0.70 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[ZDHHC11]] | +0.69 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[C3orf20]] | +0.67 | +0.74 / +0.51 | both halves | 1e-05 |  |
| [[TMEM236]] | +0.67 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[FBXW10B]] | +0.65 | +0.71 / +0.50 | both halves | 1e-05 |  |
| [[MMP25]] | +0.65 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[EFCAB8]] | +0.65 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[LINC02803]] | +0.64 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[SEMA6A-AS1]] | +0.64 | +0.66 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM9]] | -0.65 | -0.68 / -0.61 | both halves | 7e-06 |  |
| [[PEX3]] | -0.65 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[SPATA7]] | -0.61 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[ECI2]] | -0.61 | -0.65 / -0.55 | both halves | 1e-05 |  |
| [[VDAC3]] | -0.58 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[USP30]] | -0.58 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[PGAP1]] | -0.57 | -0.58 / -0.49 | both halves | 2e-05 |  |
| [[ABCD4]] | -0.57 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[WDR54]] | -0.57 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[SCPEP1]] | -0.56 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[PRKRA]] | -0.55 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[LMBR1L]] | -0.55 | -0.60 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTNR1A]] | B | MTNR1A activity raises CFAP161's level | lines that do not express MTNR1A (7) vs lines expressing it (43) | 2.09× lower at baseline in the lines without MTNR1A | 0.077 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ZDHHC11]] | C | ZDHHC11 activity raises CFAP161's level | lines that do not express ZDHHC11 (4) vs lines expressing it (46) | 2.69× lower at baseline in the lines without ZDHHC11 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent; its own permutation p |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AHRR]] | B | CFAP161 activity raises AHRR's level | lines that do not express CFAP161 (6) vs lines expressing it (44) | 2.15× lower at baseline in the lines without CFAP161 | 0.060 | ⚠ within organs, on part of the lines; also absent: CRB1; maybe low, not absent; its own permutation p |
| [[FLACC1]] | B | CFAP161 activity raises FLACC1's level | lines that do not express CFAP161 (6) vs lines expressing it (44) | 1.72× lower at baseline in the lines without CFAP161 | 0.060 | ⚠ within organs, on part of the lines; also absent: CRB1; maybe low, not absent; its own permutation p |
| [[SCUBE2]] | B | CFAP161 activity raises SCUBE2's level | lines that do not express CFAP161 (6) vs lines expressing it (44) | 1.52× lower at baseline in the lines without CFAP161 | 0.074 | ⚠ within organs, on part of the lines; also absent: CRB1; maybe low, not absent |
| [[ZDHHC11]] | B | CFAP161 activity raises ZDHHC11's level | lines that do not express CFAP161 (6) vs lines expressing it (44) | 2.05× lower at baseline in the lines without CFAP161 | 0.089 | ⚠ within organs, on part of the lines; also absent: CRB1; maybe low, not absent; its own permutation p |
| [[BTBD16]] | B | CFAP161 activity raises BTBD16's level | lines that do not express CFAP161 (6) vs lines expressing it (44) | 1.42× lower at baseline in the lines without CFAP161 | 0.089 | ⚠ within organs, on part of the lines; also absent: CRB1; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.681). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.8, -10.9); signed map (19.5, 6.8). **Vector** length 114, 30.9% of its response variance represented; |z| ≥ 3 in 1,107 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +12.8 | +10.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +11.2 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.7 | +3.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.3 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.5 | +1.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +5.0 | +7.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +5.0 | +6.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +1.2 |
|  | [[EX229 (drug)]] 5 µM |  | +3.0 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | -1.9 |
| fall | [[Selinexor (drug)]] 5 µM |  | -5.0 | -8.1 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -4.7 | -4.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -4.1 | -8.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.9 | -4.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -2.4 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -3.1 | -1.1 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.6 | -2.3 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | -2.5 | -1.6 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -2.4 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | cilia and flagella associated protein 161 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.1 — chr15:81,007,033-81,149,179 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ38615; previously C15orf26 |
| Gene groups (HGNC) | Cilia and flagella associated |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P656](https://www.uniprot.org/uniprotkb/Q6P656) (Cilia- and flagella-associated protein 161):

> Microtubule inner protein (MIP) part of the dynein-decorated doublet microtubules (DMTs) in cilia axoneme, which is required for motile cilia beating.

**Summary**, from NCBI Gene [161502](https://www.ncbi.nlm.nih.gov/gene/161502):

> Predicted to be involved in cilium assembly and flagellated sperm motility. Predicted to act upstream of or within gene expression; mRNA stabilization; and motile cilium assembly. Located in axonemal microtubule. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26782](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26782) · Entrez [161502](https://www.ncbi.nlm.nih.gov/gene/161502) · UniProt [Q6P656](https://www.uniprot.org/uniprotkb/Q6P656) · Ensembl [ENSG00000156206](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156206)

## Data

Gene col 7957: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7957); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7957, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7957]; `tensor/DDL_lfc|DDL_z.npy` [7957]; `embed/gene_vectors.npy` [7957]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7957 or target_col == 7957). Every well: [[CFAP161 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CFAP161.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
