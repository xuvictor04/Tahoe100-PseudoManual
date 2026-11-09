---
symbol: "PPIL3"
type: "gene"
col: 14233
ensembl_id: "ENSG00000240344"
name: "peptidylprolyl isomerase like 3"
location: "2q33.1"
module: 216
arm: "+"
pooled_cpm: 26.81
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 24
n_dd_up_clean: 1
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/216"]
generated_by: "tahoemap"
---

# PPIL3

*peptidylprolyl isomerase like 3* — 2q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.31× (z +6.8, q 5e-09, up in 23 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (4 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.491× (z -12.2, q 2e-31, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ESCO1]] (+0.61, fdr 7e-06), [[CRLS1]] (+0.61, fdr 1e-05), [[TRMU]] (+0.59, fdr 1e-05); moves opposite to [[PTPRK]] (-0.63, fdr 7e-06), [[LPP]] (-0.58, fdr 4e-05), [[COBL]] (-0.57, fdr 1e-05).
> It is in [[Module 216]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14233.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +6.8 | 5e-09 | 23/47 (NCI-H1573, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.17× | +3.9 | 0.025 | 16/48 (C32, NCI-H2347, …) | top dose only | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | 1.18× | +3.0 | 0.37 | 11/48 (C32, KATO III, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 1.12× | +3.0 | 0.37 | 13/48 (J82, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14233.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.491×** | -12.2 | 2e-31 | 35/47 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.635×** | -11.4 | 8e-28 | 33/47 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.567×** | -10.1 | 8e-22 | 34/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.601×** | -8.8 | 1e-16 | 34/48 (SW 900, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.645×** | -7.8 | 6e-13 | 31/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.635×** | -7.8 | 6e-13 | 31/45 (H4, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.662×** | -7.3 | 2e-11 | 29/47 (A-172, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.681×** | -6.7 | 2e-09 | 27/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.690×** | -6.4 | 8e-09 | 30/48 (SW 900, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.701×** | -6.3 | 1e-08 | 28/48 (CFPAC-1, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.688×** | -6.2 | 4e-08 | 20/38 (RPMI-7951, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.744×** | -5.3 | 7e-06 | 22/47 (hTERT-HPNE, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.750×** | -5.1 | 1e-05 | 24/47 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.814×** | -4.9 | 3e-05 | 20/48 (MIA PaCa-2, NCI-H460, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.768×** | -4.7 | 1e-04 | 18/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.773×** | -4.6 | 2e-04 | 21/48 (NCI-H1573, NCI-H460, …) | all doses, flat | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.811×** | -4.5 | 2e-04 | 16/48 (NCI-H460, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.789×** | -3.9 | 0.003 | 13/48 (NCI-H460, MIA PaCa-2, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14233. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 29.0 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -17.3) |
| [[A498 (line)]] | wt | 29.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -15.4) |
| [[NCI-H1573 (line)]] | alt | 41.2 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.324× (z -14.1) |
| [[MIA PaCa-2 (line)]] | alt | 56.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -14.6) |
| [[NCI-H460 (line)]] | wt | 31.3 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.352× (z -9.1) |
| [[PANC-1 (line)]] | alt | 21.0 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.282× (z -11.8) |
| [[AsPC-1 (line)]] | alt | 24.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -12.6) |
| [[H4 (line)]] | wt | 40.8 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0880× (z -14.0) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.308× (z -10.0) |
| [[J82 (line)]] | alt | 36.4 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.290× (z -10.9) |
| [[LOX-IMVI (line)]] | wt | 37.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.242× (z -10.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 38.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.166× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.256× (z -9.3) |
| [[SW 900 (line)]] | alt | 35.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.298× (z -9.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.291× (z -8.9) |
| [[A549 (line)]] | wt | 25.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -10.9) |
| [[AN3 CA (line)]] | alt | 17.4 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM 0.0617× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 42.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -13.4) |
| [[hTERT-HPNE (line)]] | wt | 23.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.178× (z -10.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 25.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.338× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 23.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -10.6) |
| [[SNU-423 (line)]] | alt | 18.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.198× (z -10.5) |
| [[SW1417 (line)]] | alt | 22.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SW480 (line)]] | alt | 21.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.263× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[A-427 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14233), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ESCO1]] | +0.61 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[CRLS1]] | +0.61 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[TRMU]] | +0.59 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[ECD]] | +0.59 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[SMAP2]] | +0.59 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[NUDT22]] | +0.58 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[TNFRSF10D]] | +0.58 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[ISY1]] | +0.57 | +0.51 / +0.55 | both halves | 1e-05 | same gene group; pathway: Dengue Virus-Host Interactions |
| [[INTS4]] | +0.57 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[POM121]] | +0.56 | +0.53 / +0.58 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[YIPF5]] | +0.56 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[SPICE1]] | +0.56 | +0.51 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPRK]] | -0.63 | -0.66 / -0.65 | both halves | 7e-06 |  |
| [[LPP]] | -0.58 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[COBL]] | -0.57 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[ENAH]] | -0.55 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[NUTM2B-AS1]] | -0.55 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[NPIPB4]] | -0.54 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[STK3]] | -0.53 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[LINC00342]] | -0.52 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[CUEDC1]] | -0.52 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[USP25]] | -0.52 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[TENM3]] | -0.52 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[ALCAM]] | -0.51 | -0.42 / -0.56 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 216]]; 12 genes; every member is in the + arm (projection on the module's main direction -0.743). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (6.9, -32.6); signed map (-41.0, 20.5). **Vector** length 102, 23.7% of its response variance represented; |z| ≥ 3 in 993 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +6.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | +1.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | +3.9 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +1.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +2.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.2 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +1.9 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.8 | -7.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.5 | -8.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.5 | -4.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.1 | -10.1 |
|  | [[Trametinib (drug)]] 5 µM |  | -4.0 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.9 | -3.3 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.8 | -4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.6 | -4.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.5 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | peptidylprolyl isomerase like 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.1 — chr2:200,870,907-200,889,303 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CyPJ |
| Gene groups (HGNC) | Cyclophilin peptidylprolyl isomerases; Spliceosomal C complex; Spliceosomal P complex |
| Reactome | 7 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Dengue Virus-Host Interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H2H8](https://www.uniprot.org/uniprotkb/Q9H2H8) (Peptidyl-prolyl cis-trans isomerase-like 3):

> PPIases accelerate the folding of proteins. It catalyzes the cis-trans isomerization of proline imidic peptide bonds in oligopeptides. May be involved in pre-mRNA splicing.

**Summary**, from NCBI Gene [53938](https://www.ncbi.nlm.nih.gov/gene/53938):

> This gene encodes a member of the cyclophilin family. Cyclophilins catalyze the cis-trans isomerization of peptidylprolyl imide bonds in oligopeptides. They have been proposed to act either as catalysts or as molecular chaperones in protein-folding events. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Sep 2008]

**Accessions** — [HGNC:9262](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9262) · Entrez [53938](https://www.ncbi.nlm.nih.gov/gene/53938) · UniProt [Q9H2H8](https://www.uniprot.org/uniprotkb/Q9H2H8) · Ensembl [ENSG00000240344](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000240344)

## Data

Gene col 14233: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14233); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14233, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14233]; `tensor/DDL_lfc|DDL_z.npy` [14233]; `embed/gene_vectors.npy` [14233]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14233 or target_col == 14233). Every well: [[PPIL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPIL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
