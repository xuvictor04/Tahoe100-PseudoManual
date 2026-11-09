---
symbol: "PRKAB2"
type: "gene"
col: 5248
ensembl_id: "ENSG00000131791"
name: "protein kinase AMP-activated non-catalytic subunit beta 2"
location: "1q21.1"
module: 30
arm: "+"
pooled_cpm: 47.07
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 22
n_dd_up_clean: 3
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# PRKAB2

*protein kinase AMP-activated non-catalytic subunit beta 2* — 1q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Radotinib (drug)]] 5 µM: 1.27× (z +5.6, q 2e-05, up in 27 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.687× (z -6.2, q 3e-07, down in 26 of 48 measured lines) ⚠ cell-cycle shift, explains ~44% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.704× (z -5.8, q 1e-06, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VPS37D]] (+0.67, fdr 7e-06), [[CGRRF1]] (+0.65, fdr 7e-06), [[CAT]] (+0.62, fdr 7e-06); moves opposite to [[SNRPB]] (-0.67, fdr 1e-05), [[SLC20A2]] (-0.63, fdr 1e-05), [[GNL3L]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5248.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Radotinib (drug)]] 5 µM |  | **1.27×** | +5.6 | 2e-05 | 27/48 (AsPC-1, PANC-1, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.23×** | +4.8 | 4e-04 | 25/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.32×** | +4.6 | 8e-04 | 28/48 (SW480, H4, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **1.66×** | +4.4 | 0.002 | 26/47 (LoVo, AsPC-1, …) | top dose only | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.24×** | +3.5 | 0.057 | 19/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +3.1 | 0.17 | 3/49 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.21× | +3.0 | 0.17 | 8/47 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.20× | +3.0 | 0.17 | 11/48 (SW480, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5248.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.687×** | -6.2 | 3e-07 | 26/48 (A-172, AsPC-1, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.686×** | -6.0 | 5e-07 | 23/40 (NCI-H460, KATO III, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.704×** | -5.8 | 1e-06 | 26/48 (HOP62, A549, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.792×** | -5.5 | 7e-06 | 30/48 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.736×** | -5.1 | 4e-05 | 25/48 (HOP62, HS-578T, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **0.740×** | -5.0 | 6e-05 | 24/47 (NCI-H2347, NCI-H460, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.741×** | -5.0 | 6e-05 | 26/48 (HOP62, SNU-1, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.815×** | -4.8 | 1e-04 | 26/49 (HOP62, HS-578T, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.762×** | -4.5 | 4e-04 | 25/48 (RPMI-7951, HOP62, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.758×** | -4.3 | 8e-04 | 21/47 (NCI-H2347, SW1417, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.767×** | -4.2 | 0.001 | 24/48 (HS-578T, HOP62, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.778×** | -4.2 | 0.001 | 22/47 (A549, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.782×** | -3.9 | 0.004 | 20/48 (RKO, NCI-H2347, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.791×** | -3.9 | 0.004 | 20/49 (NCI-H460, BT-474, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.797×** | -3.8 | 0.006 | 19/48 (AsPC-1, SW1417, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.798×** | -3.7 | 0.006 | 19/48 (COLO 205, A549, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.814×** | -3.4 | 0.022 | 17/48 (LS 180, SHP-77, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.824×** | -3.2 | 0.036 | 16/49 (LS 180, SW 900, …) | inconsistent across doses |  |
| [[(S)-Crizotinib (drug)]] 0.5 µM |  | **0.824×** | -3.2 | 0.036 | 13/48 (HEC-1-A, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.872× | -3.2 | 0.036 | 12/48 (COLO 205, KATO III, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.825×** | -3.2 | 0.036 | 14/49 (H4, KATO III, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.832×** | -3.1 | 0.056 | 13/49 (CFPAC-1, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5248. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 63.3 | 0 | 8 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -12.0) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.370× (z -9.8) |
| [[HS-578T (line)]] | alt | 51.5 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.253× (z -12.9) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 84.2 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.124× (z -19.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[A-172 (line)]] | wt | 55.1 | 0 | 3 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -10.3) ⚠ cell-cycle shift, explains ~55% of this change |
| [[C32 (line)]] | wt | 37.5 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -13.0) ⚠ cell-cycle shift, explains ~8% of this change |
| [[PANC-1 (line)]] | alt | 40.3 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +12.9) ⚠ cell-cycle shift, explains ~8% of this change | — |
| [[SW480 (line)]] | alt | 38.0 | 2 (2 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.51× (z +9.4) ⚠ toxic | [[Dinaciclib (drug)]] 5 µM 0.353× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[AsPC-1 (line)]] | alt | 79.0 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.374× (z -8.8) ⚠ cell-cycle shift, explains ~44% of this change |
| [[hTERT-HPNE (line)]] | wt | 60.0 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -10.1) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H2347 (line)]] | alt | 55.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.379× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[RPMI-7951 (line)]] | alt | 66.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.235× (z -11.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 38.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +8.8) ⚠ cell-cycle shift, explains ~8% of this change | — |
| [[A498 (line)]] | wt | 34.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +9.4) ⚠ cell-cycle shift, explains ~8% of this change | — |
| [[A549 (line)]] | wt | 46.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.268× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[HepG2_C3A (line)]] | wt | 92.5 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.309× (z -9.4) ⚠ cell-cycle shift, explains ~64% of this change |
| [[KATO III (line)]] | alt | 22.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[NCI-H1792 (line)]] | alt | 71.8 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.406× (z -9.0) ⚠ cell-cycle shift, explains ~41% of this change |
| [[NCI-H596 (line)]] | alt | 58.3 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.05 µM 0.196× (z -9.8) |
| [[SHP-77 (line)]] | alt | 76.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.328× (z -9.7) ⚠ toxic |
| [[SW 1271 (line)]] | alt | 34.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0749× (z -10.6) ⚠ cell-cycle shift, explains ~38% of this change |
| [[SW 900 (line)]] | alt | 65.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -10.8) ⚠ cell-cycle shift, explains ~8% of this change |
| [[AN3 CA (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 43.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 65.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 64.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 44.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 70.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 43.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 36.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5248), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS37D]] | +0.67 | +0.67 / +0.59 | both halves | 7e-06 | pathway: Autophagy |
| [[CGRRF1]] | +0.65 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[CAT]] | +0.62 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[NBPF1]] | +0.61 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[LCA5]] | +0.60 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[ANKMY2]] | +0.60 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[ANG]] | +0.60 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[FAM229B]] | +0.59 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[SPOPL]] | +0.59 | +0.66 / +0.43 | both halves | 3e-05 |  |
| [[SCPEP1]] | +0.59 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[MTIF3]] | +0.59 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[KBTBD3]] | +0.58 | +0.51 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNRPB]] | -0.67 | -0.71 / -0.56 | both halves | 1e-05 |  |
| [[SLC20A2]] | -0.63 | -0.72 / -0.51 | both halves | 1e-05 |  |
| [[GNL3L]] | -0.63 | -0.66 / -0.55 | both halves | 1e-05 |  |
| [[MBD3]] | -0.62 | -0.65 / -0.56 | both halves | 1e-05 | pathway: Regulation of TP53 Activity |
| [[HNRNPAB]] | -0.61 | -0.59 / -0.58 | both halves | 8e-06 |  |
| [[DOCK1]] | -0.58 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[ZNF407]] | -0.58 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[REXO1]] | -0.58 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[SMC1A]] | -0.57 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[OPA3]] | -0.57 | -0.64 / -0.43 | both halves | 3e-05 |  |
| [[PKP4]] | -0.57 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[LARP4B]] | -0.57 | -0.50 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PRKAB2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ABL1]] | B | ABL1 activity lowers PRKAB2's level | compounds that target ABL1: 3 of 6 raise it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.4% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HOXA9]] | B | HOXA9 activity raises PRKAB2's level | lines that do not express HOXA9 (31) vs lines expressing it (19) | 1.05× lower at baseline in the lines without HOXA9 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HOXA11, IGFL2-AS1, GPA33 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.585). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (3.0, -8.9); signed map (-26.5, -6.9). **Vector** length 115, 30.2% of its response variance represented; |z| ≥ 3 in 1,043 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Radotinib (drug)]] 5 µM |  | +5.2 | +5.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.7 | +4.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | +1.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +1.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.5 | +1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.4 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.9 | +2.2 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -6.1 | -5.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -5.7 | -5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.7 | -5.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -2.6 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -3.8 | -4.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.6 | -4.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.7 | -3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -1.8 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.5 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | protein kinase AMP-activated non-catalytic subunit beta 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.1 — chr1:147,155,106-147,172,550 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Protein kinase AMP-activated non-catalytic subunit beta family |
| Reactome | 36 pathways, smallest: AMPK inhibits chREBP transcriptional activation activity; Lipophagy; Activation of PPARGC1A (PGC-1alpha) by phosphorylation |
| Matched by | ensembl_id |

**Function**, from UniProt [O43741](https://www.uniprot.org/uniprotkb/O43741) (5'-AMP-activated protein kinase subunit beta-2):

> Non-catalytic subunit of AMP-activated protein kinase (AMPK), an energy sensor protein kinase that plays a key role in regulating cellular energy metabolism. In response to reduction of intracellular ATP levels, AMPK activates energy-producing pathways and inhibits energy-consuming processes: inhibits protein, carbohydrate and lipid biosynthesis, as well as cell growth and proliferation. AMPK acts via direct phosphorylation of metabolic enzymes, and by longer-term effects via phosphorylation of …

**Summary**, from NCBI Gene [5565](https://www.ncbi.nlm.nih.gov/gene/5565):

> The protein encoded by this gene is a regulatory subunit of the AMP-activated protein kinase (AMPK). AMPK is a heterotrimer consisting of an alpha catalytic subunit, and non-catalytic beta and gamma subunits. AMPK is an important energy-sensing enzyme that monitors cellular energy status. In response to cellular metabolic stresses, AMPK is activated, and thus phosphorylates and inactivates acetyl-CoA carboxylase (ACC) and beta-hydroxy beta-methylglutaryl-CoA reductase (HMGCR), key enzymes …

**Accessions** — [HGNC:9379](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9379) · Entrez [5565](https://www.ncbi.nlm.nih.gov/gene/5565) · UniProt [O43741](https://www.uniprot.org/uniprotkb/O43741) · Ensembl [ENSG00000131791](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131791)

## Data

Gene col 5248: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5248); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5248, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5248]; `tensor/DDL_lfc|DDL_z.npy` [5248]; `embed/gene_vectors.npy` [5248]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5248 or target_col == 5248). Every well: [[PRKAB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRKAB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
