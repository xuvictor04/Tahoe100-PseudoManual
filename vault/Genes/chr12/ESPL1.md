---
symbol: "ESPL1"
type: "gene"
col: 5712
ensembl_id: "ENSG00000135476"
name: "extra spindle pole bodies like 1, separase"
location: "12q13.13"
module: 91
arm: "+"
pooled_cpm: 19.03
n_lines_expressing: 49
n_dd_up: 15
n_dd_down: 21
n_dd_up_clean: 7
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/091"]
generated_by: "tahoemap"
---

# ESPL1

*extra spindle pole bodies like 1, separase* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.18× (z +31.5, q 0e+00, up in 43 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.552× (z -8.7, q 1e-15, down in 29 of 46 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.608× (z -7.7, q 3e-12, down in 29 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SGO1]] (+0.81, fdr 7e-06), [[REXO5]] (+0.79, fdr 7e-06), [[PHF19]] (+0.78, fdr 7e-06).
> It is in [[Module 091]], a single-armed module (HDR through Homologous Recombination (HRR)).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[DUBR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5712.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.18×** | +31.5 | 0e+00 | 43/46 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.44×** | +18.5 | 0e+00 | 39/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.86×** | +9.7 | 9e-20 | 25/46 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.69×** | +8.2 | 3e-14 | 28/47 (NCI-H460, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +6.4 | 2e-08 | 21/46 (A549, C32, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.45×** | +5.8 | 6e-07 | 21/46 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **1.44×** | +5.7 | 1e-06 | 23/45 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.43×** | +5.5 | 2e-06 | 20/47 (NCI-H460, A-172, …) | rises with dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +5.4 | 5e-06 | 18/45 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.34×** | +4.6 | 2e-04 | 20/46 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.34×** | +4.6 | 2e-04 | 18/46 (A549, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.29×** | +3.8 | 0.007 | 18/47 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.26×** | +3.3 | 0.035 | 11/46 (COLO 205, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **1.47×** | +3.1 | 0.069 | 9/44 (HOP62, RKO, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.22×** | +3.1 | 0.083 | 5/47 (AsPC-1, NCI-H2030, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5712.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.552×** | -8.7 | 1e-15 | 29/46 (HOP62, MIA PaCa-2, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.608×** | -7.7 | 3e-12 | 29/47 (SHP-77, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.740×** | -6.6 | 7e-09 | 23/47 (A-427, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.658×** | -6.5 | 1e-08 | 24/46 (A-427, BT-474, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.662×** | -6.4 | 2e-08 | 25/45 (NCI-H23, J82, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.704×** | -5.4 | 5e-06 | 23/47 (A-427, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.708×** | -5.4 | 6e-06 | 24/47 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.719×** | -5.1 | 2e-05 | 21/46 (A-427, NCI-H23, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.796×** | -5.0 | 3e-05 | 22/47 (SHP-77, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.747×** | -4.5 | 3e-04 | 19/41 (C-33 A, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **0.746×** | -4.4 | 6e-04 | 18/46 (NCI-H23, A498, …) | top dose only |  |
| [[palbociclib (drug)]] 5 µM |  | **0.592×** | -4.3 | 1e-03 | 15/44 (A-427, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.824×** | -4.2 | 1e-03 | 16/47 (Hs 766T, A-427, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **0.594×** | -4.2 | 1e-03 | 19/39 (A-427, BT-474, …) | all doses, flat | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.765×** | -4.2 | 0.001 | 19/46 (SHP-77, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.767×** | -4.0 | 0.003 | 12/46 (A-427, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.844× | -3.7 | 0.006 | 16/47 (A-427, H4, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.807×** | -3.3 | 0.024 | 17/47 (RPMI-7951, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.838× | -3.3 | 0.027 | 14/47 (C32, MIA PaCa-2, …) | two highest doses | noisy plate (z scaled) |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 0.866× | -3.1 | 0.042 | 10/47 (AN3 CA, A-427, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.817×** | -3.1 | 0.042 | 13/47 (LOX-IMVI, A-427, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5712. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 17.9 | 8 (5 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +25.5) | [[Selinexor (drug)]] 5 µM 0.295× (z -13.0) ⚠ cell-cycle shift, explains ~72% of this change |
| [[A-427 (line)]] | wt | 55.3 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.218× (z -16.1) ⚠ cell-cycle shift, explains ~72% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.386× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 15.1 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.161× (z -9.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.278× (z -9.4) |
| [[H4 (line)]] | wt | 18.6 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +9.2) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.238× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 20.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.109× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 17.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +14.3) | [[Bortezomib (drug)]] 0.05 µM 0.257× (z -8.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[LoVo (line)]] | wt | 11.5 | 3 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 6.15× (z +10.7) | — |
| [[NCI-H1573 (line)]] | alt | 9.04 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.17× (z +12.6) | [[Dinaciclib (drug)]] 0.05 µM 0.126× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 17.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.01× (z +21.2) | — |
| [[PANC-1 (line)]] | alt | 18.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.6× (z +29.3) | — |
| [[SW48 (line)]] | wt | 28.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +14.5) | — |
| [[A498 (line)]] | wt | 17.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +13.6) | — |
| [[A549 (line)]] | wt | 17.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.27× (z +19.5) | — |
| [[AsPC-1 (line)]] | alt | 8.14 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.4× (z +19.6) | — |
| [[CFPAC-1 (line)]] | alt | 18.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +19.4) | [[Selinexor (drug)]] 5 µM 0.302× (z -9.6) ⚠ cell-cycle shift, explains ~72% of this change |
| [[Hs 766T (line)]] | wt | 16.6 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.23× (z +13.3) | [[Clotrimazole (drug)]] 0.5 µM 0.157× (z -9.4) |
| [[J82 (line)]] | alt | 24.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +16.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 18.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +14.6) | [[Bortezomib (drug)]] 0.05 µM 0.209× (z -8.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H2030 (line)]] | alt | 23.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.22× (z +17.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.135× (z -13.2) ⚠ toxic; cell-cycle shift, explains ~7% of this change |
| [[Panc 03.27 (line)]] | alt | 21.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.84× (z +20.4) | — |
| [[SNU-1 (line)]] | wt | 23.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +9.8) | — |
| [[A-172 (line)]] | wt | 23.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +12.0) | — |
| [[AN3 CA (line)]] | alt | 31.5 | 0 | 1 | — | [[Flutamide (drug)]] 0.5 µM 0.100× (z -8.9) |
| [[C-33 A (line)]] | alt | 27.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -11.2) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 10.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.61× (z +13.8) | — |
| [[HT-29 (line)]] | alt | 8.94 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.15× (z +10.5) | — |
| [[hTERT-HPNE (line)]] | wt | 11.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.94× (z +11.6) | — |
| [[RKO (line)]] | wt | 29.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +11.7) | — |
| [[RPMI-7951 (line)]] | alt | 18.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +13.1) | — |
| [[SK-MEL-2 (line)]] | alt | 22.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.43× (z +13.4) | — |
| [[SNU-423 (line)]] | alt | 22.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.14× (z +14.4) | — |
| [[SW 900 (line)]] | alt | 11.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +16.6) | — |
| [[BT-474 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.09 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.14 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 30.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5712), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SGO1]] | +0.81 | +0.81 / +0.84 | both halves | 7e-06 | pathway: Mitotic Anaphase; STRING 976 |
| [[REXO5]] | +0.79 | +0.75 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[PHF19]] | +0.78 | +0.81 / +0.74 | both halves | 7e-06 |  |
| [[KIF24]] | +0.78 | +0.73 / +0.80 | both halves | 7e-06 |  |
| [[NCAPG]] | +0.77 | +0.74 / +0.81 | both halves | 7e-06 | STRING 730 |
| [[ESCO2]] | +0.75 | +0.74 / +0.74 | both halves | 7e-06 | STRING 874 |
| [[BRCA2]] | +0.75 | +0.73 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[MKI67]] | +0.75 | +0.73 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 856 |
| [[CIP2A]] | +0.75 | +0.75 / +0.76 | both halves | 7e-06 | STRING 402 |
| [[KIF2C]] | +0.75 | +0.70 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 939 |
| [[AURKB]] | +0.74 | +0.70 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 985 |
| [[SMC4]] | +0.74 | +0.77 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 710 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DUBR]] | B | DUBR activity raises ESPL1's level | lines that do not express DUBR (8) vs lines expressing it (42) | 1.98× lower at baseline in the lines without DUBR | 0.049 | ⚠ within organs, on part of the lines; also absent: ATP10D, LRP12, CYP46A1 |
| [[TOP2A]] | B | TOP2A activity lowers ESPL1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[E2F8]] | B | E2F8 activity raises ESPL1's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 1.99× lower at baseline in the lines without E2F8 | 0.084 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises ESPL1's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.22× lower at baseline in the lines without AURKB | 0.082 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 091]] — HDR through Homologous Recombination (HRR); 49 genes; every member is in the + arm (projection on the module's main direction 0.799). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-40.9, -48.9); signed map (-44.5, -47.6). **Vector** length 122, 33.3% of its response variance represented; |z| ≥ 3 in 1,168 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *HDR through Homologous Recombination (HRR)* (reactome, mean cos +0.66 to 5); *Resolution of D-loop Structures through Holliday Junction Intermediates* (reactome, mean cos +0.66 to 4); *Resolution of D-Loop Structures* (reactome, mean cos +0.66 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +11.4 | +31.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.2 | +18.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +6.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +4.5 | +2.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +5.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +2.6 |
|  | [[Docetaxel (drug)]] 5 µM |  | +2.2 | +2.9 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +2.2 | +1.9 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +1.8 | +1.3 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.7 | +3.3 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | -6.6 | -8.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.9 | -6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.7 | -5.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | -4.6 | -5.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.6 | -3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | +0.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.8 | -2.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.7 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | extra spindle pole bodies like 1, separase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:53,268,299-53,293,638 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0165, ESP1, SEPA |
| Gene groups (HGNC) | Cysteine endopeptidases |
| Hallmark sets | G2M_CHECKPOINT, MITOTIC_SPINDLE, E2F_TARGETS |
| Reactome | 6 pathways, smallest: Separation of Sister Chromatids; Mitotic Anaphase; Mitotic Metaphase and Anaphase |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14674](https://www.uniprot.org/uniprotkb/Q14674) (Separin):

> Caspase-like protease, which plays a central role in the chromosome segregation by cleaving the SCC1/RAD21 subunit of the cohesin complex at the onset of anaphase. During most of the cell cycle, it is inactivated by different mechanisms.

**Summary**, from NCBI Gene [9700](https://www.ncbi.nlm.nih.gov/gene/9700):

> Stable cohesion between sister chromatids before anaphase and their timely separation during anaphase are critical for chromosome inheritance. In vertebrates, sister chromatid cohesion is released in 2 steps via distinct mechanisms. The first step involves phosphorylation of STAG1 (MIM 604358) or STAG2 (MIM 300826) in the cohesin complex. The second step involves cleavage of the cohesin subunit SCC1 (RAD21; MIM 606462) by ESPL1, or separase, which initiates the final separation of sister …

**Accessions** — [HGNC:16856](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16856) · Entrez [9700](https://www.ncbi.nlm.nih.gov/gene/9700) · UniProt [Q14674](https://www.uniprot.org/uniprotkb/Q14674) · Ensembl [ENSG00000135476](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135476)

## Data

Gene col 5712: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5712); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5712, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5712]; `tensor/DDL_lfc|DDL_z.npy` [5712]; `embed/gene_vectors.npy` [5712]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5712 or target_col == 5712). Every well: [[ESPL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ESPL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
