---
symbol: "SMARCAD1"
type: "gene"
col: 8633
ensembl_id: "ENSG00000163104"
name: "SNF2 related chromatin remodeling ATPase with DExD box 1"
location: "4q22.3"
module: 1
arm: "+"
pooled_cpm: 82.28
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 21
n_dd_up_clean: 2
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# SMARCAD1

*SNF2 related chromatin remodeling ATPase with DExD box 1* — 4q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 1.49× (z +4.5, q 0.005, up in 24 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.471× (z -23.5, q 0e+00, down in 46 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOL11]] (+0.77, fdr 7e-06), [[MAK16]] (+0.69, fdr 7e-06), [[NUBPL]] (+0.68, fdr 8e-06).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8633.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.49×** | +4.5 | 0.005 | 24/49 (LoVo, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.43×** | +4.0 | 0.018 | 23/48 (LoVo, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.16× | +3.0 | 0.48 | 16/47 (Panc 03.27, BT-474, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8633.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.471×** | -23.5 | 0e+00 | 46/49 (A498, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.548×** | -13.2 | 1e-37 | 42/49 (C-33 A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.553×** | -12.5 | 9e-34 | 37/44 (A-427, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.598×** | -11.3 | 1e-27 | 45/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.599×** | -11.3 | 1e-27 | 45/48 (H4, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.607×** | -11.0 | 4e-26 | 44/48 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.611×** | -10.4 | 1e-23 | 41/50 (NCI-H23, HOP62, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.614×** | -10.3 | 4e-23 | 37/48 (LOX-IMVI, H4, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.561×** | -9.7 | 1e-20 | 34/45 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.772×** | -8.1 | 4e-14 | 36/48 (HOP62, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.696×** | -8.0 | 7e-14 | 31/48 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.725×** | -7.1 | 7e-11 | 39/48 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.834× | -5.7 | 7e-07 | 23/48 (A-172, HOP62, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.787×** | -5.3 | 5e-06 | 27/48 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.795×** | -4.9 | 4e-05 | 24/47 (NCI-H460, KATO III, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.822×** | -4.3 | 5e-04 | 23/49 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.709×** | -3.8 | 0.004 | 21/48 (PANC-1, A498, …) | rises with dose | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.821×** | -2.9 | 0.088 | 17/47 (LoVo, AN3 CA, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.877× | -2.9 | 0.088 | 11/49 (HOP62, A498, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.825×** | -2.8 | 0.098 | 9/48 (A498, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8633. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 74.2 | 0 | 12 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -15.8) |
| [[HOP62 (line)]] | alt | 75.7 | 0 | 9 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -18.4) |
| [[MIA PaCa-2 (line)]] | alt | 89.2 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.267× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -10.8) |
| [[PANC-1 (line)]] | alt | 94.1 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -17.2) |
| [[H4 (line)]] | wt | 137 | 0 | 8 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.254× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.283× (z -11.9) |
| [[SW480 (line)]] | alt | 97.4 | 0 | 8 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -14.1) |
| [[LOX-IMVI (line)]] | wt | 75.8 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -21.7) |
| [[HEC-1-A (line)]] | alt | 84.3 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.116× (z -28.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.596× (z -10.0) |
| [[SW 900 (line)]] | alt | 83.8 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -14.8) |
| [[A498 (line)]] | wt | 105 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -22.9) |
| [[AN3 CA (line)]] | alt | 137 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -13.5) |
| [[C32 (line)]] | wt | 87.9 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -12.5) |
| [[HS-578T (line)]] | alt | 65.5 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -16.7) |
| [[LoVo (line)]] | wt | 87.8 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.227× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -12.6) |
| [[NCI-H1792 (line)]] | alt | 92.8 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -11.9) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.429× (z -10.0) |
| [[A-427 (line)]] | wt | 118 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0890× (z -31.1) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -11.2) |
| [[KATO III (line)]] | alt | 49.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0779× (z -19.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 114 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -17.5) |
| [[RPMI-7951 (line)]] | alt | 99.2 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.297× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -10.5) |
| [[SW48 (line)]] | wt | 106 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.271× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -10.5) |
| [[A-172 (line)]] | wt | 69.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -21.4) |
| [[AsPC-1 (line)]] | alt | 55.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -14.8) |
| [[CFPAC-1 (line)]] | alt | 73.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -15.9) |
| [[HCT15 (line)]] | alt | 130 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -12.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 80.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -12.8) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -12.2) |
| [[NCI-H2030 (line)]] | alt | 84.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -15.1) |
| [[Panc 03.27 (line)]] | alt | 67.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -16.1) |
| [[RKO (line)]] | wt | 68.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -12.2) |
| [[SK-MEL-2 (line)]] | alt | 102 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -11.0) |
| [[SNU-1 (line)]] | wt | 138 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -20.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -14.1) |
| [[A549 (line)]] | wt | 66.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -15.0) |
| [[BT-474 (line)]] | alt | 63.5 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.414× (z -8.6) ⚠ cell-cycle shift, explains ~48% of this change |
| [[C-33 A (line)]] | alt | 145 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -15.7) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 70.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -12.9) |
| [[Hs 766T (line)]] | wt | 77.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -12.6) |
| [[hTERT-HPNE (line)]] | wt | 77.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -10.4) |
| [[NCI-H1573 (line)]] | alt | 77.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.118× (z -23.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 67.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.550× (z -10.5) |
| [[SHP-77 (line)]] | alt | 68.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -9.6) |
| [[SNU-423 (line)]] | alt | 37.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -9.2) |
| [[CHP-212 (line)]] | wt | 127 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 79.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 66.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 82.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 77.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 78.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 46.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8633), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOL11]] | +0.77 | +0.62 / +0.78 | both halves | 7e-06 |  |
| [[MAK16]] | +0.69 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[NUBPL]] | +0.68 | +0.58 / +0.73 | both halves | 8e-06 |  |
| [[SF3A3]] | +0.68 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[GAR1]] | +0.67 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[PRMT5]] | +0.66 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[ICE2]] | +0.65 | +0.45 / +0.70 | both halves | 3e-05 |  |
| [[QTRT2]] | +0.65 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[FASTKD2]] | +0.65 | +0.51 / +0.70 | both halves | 1e-05 |  |
| [[RBM28]] | +0.64 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[BRIX1]] | +0.64 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[MRPL15]] | +0.64 | +0.50 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.710). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-21.0, -40.2); signed map (-3.4, -41.8). **Vector** length 94.3, 26.0% of its response variance represented; |z| ≥ 3 in 1,138 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA processing* (reactome, mean cos +0.54 to 28); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.54 to 24); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.54 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +6.8 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.6 | -0.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~11% of this change | +4.4 | -3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.0 | +4.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.9 | +4.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.5 | +0.0 |
|  | [[EX229 (drug)]] 5 µM |  | +2.4 | +1.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.3 | +0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | -1.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.9 | -8.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.0 | -4.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.8 | -23.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.5 | -10.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -1.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.9 | -1.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.1 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.0 | -2.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.0 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | SNF2 related chromatin remodeling ATPase with DExD box 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q22.3 — chr4:94,207,611-94,291,292 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ETL1, DKFZP762K2015, KIAA1122, DKFZp762K2015; previously HPGDS-AS1 |
| Gene groups (HGNC) | SNF2 related family; CUE domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H4L7](https://www.uniprot.org/uniprotkb/Q9H4L7) (SWI/SNF-related matrix-associated actin-dependent regulator of chromatin subfamily A containing DEAD/H box 1):

> Protein that possesses intrinsic ATP-dependent nucleosome-remodeling activity and is both required for DNA repair and heterochromatin organization. Combines the ATP-dependent ability to exchange histones, with the chaperone-like ATP-independent activity to deposit histones and assemble nucleosomes. Promotes DNA end resection of double-strand breaks (DSBs) following DNA damage: probably acts by weakening histone DNA interactions in nucleosomes flanking DSBs. Required for the restoration of …

**Summary**, from NCBI Gene [56916](https://www.ncbi.nlm.nih.gov/gene/56916):

> This gene encodes a member of the SNF subfamily of helicase proteins. The encoded protein plays a critical role in the restoration of heterochromatin organization and propagation of epigenetic patterns following DNA replication by mediating histone H3/H4 deacetylation. Mutations in this gene are associated with adermatoglyphia. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Dec 2011]

**Accessions** — [HGNC:18398](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18398) · Entrez [56916](https://www.ncbi.nlm.nih.gov/gene/56916) · UniProt [Q9H4L7](https://www.uniprot.org/uniprotkb/Q9H4L7) · Ensembl [ENSG00000163104](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163104)

## Data

Gene col 8633: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8633); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8633, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8633]; `tensor/DDL_lfc|DDL_z.npy` [8633]; `embed/gene_vectors.npy` [8633]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8633 or target_col == 8633). Every well: [[SMARCAD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMARCAD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
