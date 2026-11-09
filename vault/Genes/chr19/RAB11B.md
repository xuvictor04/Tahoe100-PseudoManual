---
symbol: "RAB11B"
type: "gene"
col: 11643
ensembl_id: "ENSG00000185236"
name: "RAB11B, member RAS oncogene family"
location: "19p13.2"
module: 153
arm: "+"
pooled_cpm: 24.68
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 29
n_dd_up_clean: 1
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/153"]
generated_by: "tahoemap"
---

# RAB11B

*RAB11B, member RAS oncogene family* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.58× (z +7.4, q 1e-10, up in 33 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 1.51× (z +3.5, q 0.050, up in 18 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (Panc 03.27 3.90×, LS 180 3.68×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2030 2.31×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW480 2.72×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.392× (z -15.2, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BAG6]] (+0.77, fdr 7e-06), [[RAB1B]] (+0.69, fdr 7e-06), [[PPP2R1A]] (+0.68, fdr 7e-06); moves opposite to [[PDCD5]] (-0.57, fdr 4e-05), [[NOL7]] (-0.53, fdr 1e-04, ⚠ NOL7 in the vector space only through flagged drug-doses), [[NACA4P]] (-0.48, fdr 1e-04, ⚠ NACA4P in the vector space only through flagged drug-doses).
> It is in [[Module 153]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11643.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (Panc 03.27 3.90×, LS 180 3.68×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2030 2.31×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW480 2.72×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.58×** | +7.4 | 1e-10 | 33/42 (SW480, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.56×** | +6.7 | 5e-09 | 27/40 (HT-29, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +6.6 | 8e-09 | 24/35 (Panc 03.27, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **1.29×** | +4.2 | 0.004 | 20/46 (MIA PaCa-2, A549, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **1.51×** | +3.5 | 0.050 | 18/48 (COLO 205, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.31× | +3.2 | 0.14 | 10/48 (HCT15, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.14× | +3.1 | 0.16 | 7/48 (Panc 03.27, C32, …) | inconsistent across doses | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | 1.21× | +3.0 | 0.16 | 12/48 (HOP62, KATO III, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.30× | +3.0 | 0.16 | 9/48 (Hs 766T, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11643.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.392×** | -15.2 | 0e+00 | 45/48 (PANC-1, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~8% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.397×** | -15.0 | 0e+00 | 44/48 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.450×** | -12.9 | 5e-36 | 47/48 (HS-578T, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~2% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.464×** | -12.4 | 3e-33 | 39/48 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~11% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.605×** | -11.5 | 2e-28 | 40/47 (SHP-77, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.653×** | -9.7 | 2e-20 | 34/47 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.558×** | -9.4 | 3e-19 | 39/47 (KATO III, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.560×** | -9.4 | 5e-19 | 35/47 (HS-578T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.380×** | -8.2 | 2e-14 | 41/48 (PANC-1, Hs 766T, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.721×** | -7.5 | 4e-12 | 38/48 (LoVo, A-427, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.622×** | -7.4 | 8e-12 | 34/47 (LS 180, SW480, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.682×** | -5.9 | 1e-07 | 30/47 (RKO, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.719×** | -5.1 | 1e-05 | 22/47 (A498, J82, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.728×** | -5.1 | 1e-05 | 23/48 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.732×** | -4.8 | 5e-05 | 25/45 (SW480, A-172, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.745×** | -4.7 | 7e-05 | 26/48 (SW 900, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.752×** | -4.6 | 1e-04 | 21/48 (HOP62, HCT15, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11643. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 31.2 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.272× (z -14.4) |
| [[HS-578T (line)]] | alt | 35.8 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.231× (z -11.8) |
| [[NCI-H1573 (line)]] | alt | 24.2 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -14.1) |
| [[LS 180 (line)]] | wt | 25.8 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.68× (z +9.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -8.9) |
| [[A-427 (line)]] | wt | 32.6 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.284× (z -10.4) |
| [[NCI-H2347 (line)]] | alt | 31.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -13.8) |
| [[AsPC-1 (line)]] | alt | 24.4 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.300× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 16.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -9.1) |
| [[COLO 205 (line)]] | alt | 21.7 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.114× (z -12.1) |
| [[HepG2_C3A (line)]] | wt | 20.9 | 0 | 2 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.0817× (z -13.6) ⚠ toxic; unreliable plate only · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.177× (z -9.4) |
| [[LoVo (line)]] | wt | 20.2 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.335× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 19.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 28.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.90× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -12.2) |
| [[A-172 (line)]] | wt | 28.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.330× (z -8.6) |
| [[BT-474 (line)]] | alt | 25.2 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.226× (z -9.4) |
| [[C-33 A (line)]] | alt | 31.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.163× (z -10.9) ⚠ toxic |
| [[H4 (line)]] | wt | 42.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.124× (z -12.2) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 36.4 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.263× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 21.3 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.204× (z -8.7) |
| [[KATO III (line)]] | alt | 16.3 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.224× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 16.6 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.139× (z -11.0) |
| [[NCI-H2030 (line)]] | alt | 35.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +10.2) | — |
| [[NCI-H23 (line)]] | alt | 27.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -9.1) |
| [[SHP-77 (line)]] | alt | 30.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -15.3) |
| [[SK-MEL-2 (line)]] | alt | 22.9 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.273× (z -8.6) |
| [[SNU-423 (line)]] | alt | 23.1 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.279× (z -8.7) |
| [[SW480 (line)]] | alt | 21.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.72× (z +9.8) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11643), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAG6]] | +0.77 | +0.70 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[RAB1B]] | +0.69 | +0.58 / +0.72 | both halves | 7e-06 | same gene group; pathway: RAB geranylgeranylation; STRING 916 |
| [[PPP2R1A]] | +0.68 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[CDK16]] | +0.66 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[ATP13A1]] | +0.66 | +0.46 / +0.67 | both halves | 3e-05 |  |
| [[ANAPC2]] | +0.65 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[PCIF1]] | +0.64 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[PRPF8]] | +0.64 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[MED16]] | +0.64 | +0.64 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[ARAF]] | +0.64 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[SNRNP200]] | +0.63 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[NCSTN]] | +0.63 | +0.67 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDCD5]] | -0.57 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[NOL7]] ⚠ | -0.53 | -0.35 / -0.55 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[NACA4P]] ⚠ | -0.48 | -0.35 / -0.50 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 153]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.728). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-20.5, -23.8); signed map (-14.6, -34.4). **Vector** length 76.5, 15.5% of its response variance represented; |z| ≥ 3 in 1,072 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.9 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.1 | +6.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.8 | -12.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.6 | -15.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.5 | +3.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | +1.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.2 | +0.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.2 | +2.6 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.0 | +1.7 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -3.3 | -9.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.2 | -5.1 |
|  | [[EX229 (drug)]] 5 µM |  | -3.0 | -2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.9 | -2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -7.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.7 | -5.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.4 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | RAB11B, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:8,389,981-8,404,434 (+) |
| Ensembl biotype | protein_coding |
| Also known as | H-YPT3 |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Reactome | 5 pathways, smallest: TBC/RABGAPs; RAB geranylgeranylation; Rab regulation of trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15907](https://www.uniprot.org/uniprotkb/Q15907) (Ras-related protein Rab-11B):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different set of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion. RAB11B plays a role in endocytic recycling, regulating apical recycling of several transmembrane proteins including …

**Summary**, from NCBI Gene [9230](https://www.ncbi.nlm.nih.gov/gene/9230):

> The Ras superfamily of small GTP-binding proteins, which includes the Ras (see MIM 190020), Ral (see MIM 179550), Rho (see MIM 165390), Rap (see MIM 179520), and Rab (see MIM 179508) families, is involved in controlling a diverse set of essential cellular functions. The Rab family, including RAB11B, appears to play a critical role in regulating exocytotic and endocytotic pathways (summary by Zhu et al., 1994 [PubMed 7811277]).[supplied by OMIM, Nov 2010]

**Accessions** — [HGNC:9761](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9761) · Entrez [9230](https://www.ncbi.nlm.nih.gov/gene/9230) · UniProt [Q15907](https://www.uniprot.org/uniprotkb/Q15907) · Ensembl [ENSG00000185236](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185236)

## Data

Gene col 11643: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11643); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11643, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11643]; `tensor/DDL_lfc|DDL_z.npy` [11643]; `embed/gene_vectors.npy` [11643]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11643 or target_col == 11643). Every well: [[RAB11B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB11B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
