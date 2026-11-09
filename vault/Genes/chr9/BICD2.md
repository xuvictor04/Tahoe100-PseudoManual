---
symbol: "BICD2"
type: "gene"
col: 11760
ensembl_id: "ENSG00000185963"
name: "BICD cargo adaptor 2"
location: "9q22.31"
module: 77
arm: "+"
pooled_cpm: 47.45
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 3
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# BICD2

*BICD cargo adaptor 2* — 9q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.02× (z +9.5, q 1e-18, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.633× (z -8.5, q 1e-14, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD27]] (+0.74, fdr 7e-06), [[LPCAT4]] (+0.68, fdr 1e-05), [[RBAK-RBAKDN]] (+0.66, fdr 1e-05); moves opposite to [[TIA1]] (-0.68, fdr 1e-05), [[CGGBP1]] (-0.66, fdr 2e-05), [[CASC9]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ANKRD13B]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11760.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.02×** | +9.5 | 1e-18 | 44/48 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.96×** | +9.1 | 3e-17 | 47/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.92×** | +8.8 | 2e-16 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.80×** | +7.9 | 3e-13 | 33/47 (A498, SNU-423, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.61×** | +6.2 | 6e-08 | 31/40 (C32, SNU-423, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.54×** | +5.8 | 5e-07 | 42/48 (J82, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.46×** | +5.1 | 3e-05 | 36/48 (SNU-423, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +4.8 | 1e-04 | 31/48 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.44×** | +4.7 | 1e-04 | 30/47 (J82, Hs 766T, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.36×** | +4.1 | 0.002 | 28/48 (SW480, KATO III, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.35×** | +3.8 | 0.007 | 27/48 (SNU-423, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.31×** | +3.7 | 0.011 | 25/48 (H4, SW480, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.22×** | +3.6 | 0.014 | 21/48 (A498, HT-29, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **1.33×** | +3.5 | 0.017 | 25/44 (SNU-423, HOP62, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.54×** | +3.1 | 0.086 | 20/43 (J82, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11760.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.633×** | -8.5 | 1e-14 | 36/48 (RKO, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.716×** | -4.3 | 0.004 | 28/48 (AsPC-1, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.917× | -3.7 | 0.034 | 2/49 (NCI-H23, HT-29) | inconsistent across doses |  |
| [[Folic acid (drug)]] 5 µM |  | **0.823×** | -3.5 | 0.057 | 23/48 (MIA PaCa-2, HS-578T, …) | top dose only |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.793× | -3.1 | 0.19 | 14/48 (NCI-H460, RPMI-7951, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11760. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 48.5 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.65× (z +9.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.60× (z +9.1) | — |
| [[A498 (line)]] | wt | 52.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[AsPC-1 (line)]] | alt | 32.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -13.6) |
| [[NCI-H2347 (line)]] | alt | 42.6 | 1 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.58× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -8.5) |
| [[SNU-423 (line)]] | alt | 57.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[A-172 (line)]] | wt | 57.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -10.2) |
| [[AN3 CA (line)]] | alt | 56.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -11.6) |
| [[C32 (line)]] | wt | 41.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.87× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[HEC-1-A (line)]] | alt | 105 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -11.4) |
| [[HOP62 (line)]] | alt | 49.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -11.6) |
| [[Hs 766T (line)]] | wt | 52.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -9.8) |
| [[J82 (line)]] | alt | 90.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -13.8) |
| [[LOX-IMVI (line)]] | wt | 62.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -13.3) |
| [[MIA PaCa-2 (line)]] | alt | 49.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 31.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 53.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 61.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -13.5) |
| [[RKO (line)]] | wt | 93.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -24.9) |
| [[RPMI-7951 (line)]] | alt | 44.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[A-427 (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 48.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 56.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 49.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 58.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 37.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 45.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 46.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 95.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 67.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11760), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD27]] | +0.74 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[LPCAT4]] | +0.68 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[RBAK-RBAKDN]] | +0.66 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[ST6GALNAC6]] | +0.66 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[CYTH3]] | +0.65 | +0.56 / +0.53 | both halves | 1e-05 | pathway: Intra-Golgi and retrograde Golgi-to-ER traffic |
| [[DIP2A]] | +0.65 | +0.66 / +0.44 | both halves | 3e-05 |  |
| [[PWWP3A]] | +0.64 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[CORO7]] | +0.64 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[RGS10]] | +0.64 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[TSEN54]] | +0.64 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[PACC1]] | +0.64 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[AP2A2]] | +0.63 | +0.67 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIA1]] | -0.68 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[CGGBP1]] | -0.66 | -0.59 / -0.46 | both halves | 2e-05 |  |
| [[CASC9]] | -0.65 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[HCP5]] | -0.64 | -0.65 / -0.42 | both halves | 4e-05 |  |
| [[FAM111A]] | -0.64 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[THAP9]] | -0.64 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[TAPBPL]] | -0.63 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[DCAF8]] | -0.62 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[MED12]] | -0.61 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[PATL2]] | -0.60 | -0.50 / -0.37 | both halves | 7e-05 |  |
| [[PNRC2]] | -0.59 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[RIPK2-DT]] | -0.59 | -0.50 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKRD13B]] | C | ANKRD13B activity raises BICD2's level | lines that do not express ANKRD13B (3) vs lines expressing it (47) | 1.87× lower at baseline in the lines without ANKRD13B | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **+** arm (projection on the module's main direction 0.747). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (-0.6, 0.8); signed map (-42.7, -4.8). **Vector** length 95.7, 25.9% of its response variance represented; |z| ≥ 3 in 790 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +5.7 | +5.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.1 | +9.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.4 | +5.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | +4.2 | +3.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +4.2 | +8.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.3 | +2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.6 | +2.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.5 | +2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +4.1 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -8.6 | -4.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.5 | -8.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.9 | -0.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | +0.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | +0.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.1 | -2.8 |
|  | [[Folic acid (drug)]] 5 µM |  | -1.8 | -3.5 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -1.6 | -2.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.5 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | BICD cargo adaptor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.31 — chr9:92,711,363-92,764,833 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0699 |
| Gene groups (HGNC) | Centriolar satellite proteins; BICD family cargo adaptors |
| Reactome | 5 pathways, smallest: COPI-independent Golgi-to-ER retrograde traffic; Golgi-to-ER retrograde transport; Intra-Golgi and retrograde Golgi-to-ER traffic |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TD16](https://www.uniprot.org/uniprotkb/Q8TD16) (Protein bicaudal D homolog 2):

> Acts as an adapter protein linking the dynein motor complex to various cargos and converts dynein from a non-processive to a highly processive motor in the presence of dynactin. Facilitates and stabilizes the interaction between dynein and dynactin and activates dynein processivity (the ability to move along a microtubule for a long distance without falling off the track). Facilitates the binding of RAB6A to the Golgi by stabilizing its GTP-bound form. Regulates coat complex coatomer protein I …

**Summary**, from NCBI Gene [23299](https://www.ncbi.nlm.nih.gov/gene/23299):

> This gene is one of two human homologs of Drosophila bicaudal-D and a member of the Bicoid family. It has been implicated in dynein-mediated, minus end-directed motility along microtubules. It has also been reported to be a phosphorylation target of NIMA related kinase 8. Two alternative splice variants have been described. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17208](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17208) · Entrez [23299](https://www.ncbi.nlm.nih.gov/gene/23299) · UniProt [Q8TD16](https://www.uniprot.org/uniprotkb/Q8TD16) · Ensembl [ENSG00000185963](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185963)

## Data

Gene col 11760: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11760); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11760, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11760]; `tensor/DDL_lfc|DDL_z.npy` [11760]; `embed/gene_vectors.npy` [11760]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11760 or target_col == 11760). Every well: [[BICD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BICD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
