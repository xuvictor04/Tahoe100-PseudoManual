---
symbol: "ATPAF2"
type: "gene"
col: 10189
ensembl_id: "ENSG00000171953"
name: "ATP synthase mitochondrial F1 complex assembly factor 2"
location: "17p11.2"
module: 30
arm: "+"
pooled_cpm: 15.31
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 2
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# ATPAF2

*ATP synthase mitochondrial F1 complex assembly factor 2* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.71× (z +9.9, q 1e-20, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.800× (z -4.0, q 0.031, down in 15 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (C-33 A 0.130×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HS-578T 0.158×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A549 0.201×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (Hs 766T 0.130×); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (COLO 205 0.0752×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.106×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PMS2P3-1]] (+0.72, fdr 7e-06), [[NDUFAF7]] (+0.71, fdr 7e-06), [[PMS2P3]] (+0.71, fdr 7e-06); moves opposite to [[SKIL]] (-0.65, fdr 7e-06), [[HIVEP2]] (-0.61, fdr 2e-05), [[MIS12]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NRG1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10189.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.71×** | +9.9 | 1e-20 | 38/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.71×** | +9.9 | 1e-20 | 36/47 (LoVo, SHP-77, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.71×** | +9.9 | 1e-20 | 39/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +9.7 | 3e-20 | 33/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.63×** | +9.0 | 2e-17 | 38/47 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.67×** | +9.0 | 3e-17 | 31/48 (HOP62, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.59×** | +8.6 | 9e-16 | 30/48 (SHP-77, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.42×** | +8.5 | 9e-16 | 27/48 (KATO III, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +8.5 | 1e-15 | 26/43 (A498, SW 900, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.55×** | +8.1 | 2e-14 | 34/47 (PANC-1, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.49×** | +7.4 | 7e-12 | 22/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.31×** | +6.8 | 7e-10 | 22/47 (A549, A498, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.39×** | +6.1 | 4e-08 | 25/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.85×** | +5.9 | 1e-07 | 18/46 (PANC-1, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.48×** | +5.1 | 1e-05 | 7/48 (PANC-1, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.27×** | +4.3 | 5e-04 | 15/48 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.26×** | +3.0 | 0.056 | 8/45 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.12× | +2.8 | 0.099 | 3/48 (PANC-1, AsPC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10189.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (C-33 A 0.130×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HS-578T 0.158×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A549 0.201×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (Hs 766T 0.130×); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (COLO 205 0.0752×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.106×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.800×** | -4.0 | 0.031 | 15/47 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.814×** | -3.9 | 0.031 | 10/47 (HOP62, NCI-H2347, …) | rises with dose |  |
| [[(S)-Crizotinib (drug)]] 0.5 µM |  | 0.836× | -3.3 | 0.19 | 5/47 (KATO III, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10189. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 17.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +9.6) ⚠ cell-cycle shift, explains ~18% of this change | [[Dinaciclib (drug)]] 5 µM 0.201× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 20.1 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.78× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +9.3) | — |
| [[C-33 A (line)]] | alt | 36.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.130× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 10.6 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0752× (z -10.3) |
| [[Hs 766T (line)]] | wt | 12.3 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.130× (z -10.5) |
| [[HS-578T (line)]] | alt | 17.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.158× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[hTERT-HPNE (line)]] | wt | 11.8 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.106× (z -8.5) |
| [[KATO III (line)]] | alt | 19.0 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0832× (z -9.1) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 16.1 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.68× (z +9.2) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.62 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10189), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PMS2P3-1]] | +0.72 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[NDUFAF7]] | +0.71 | +0.72 / +0.66 | both halves | 7e-06 | same gene group |
| [[PMS2P3]] | +0.71 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[UNC45A]] | +0.70 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[ASB7]] | +0.70 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[C12orf76]] | +0.70 | +0.53 / +0.71 | both halves | 1e-05 |  |
| [[DHRS1]] | +0.70 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[CRYZL1]] | +0.68 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[KLHDC10]] | +0.67 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[TRIT1]] | +0.67 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[SNX1]] | +0.67 | +0.70 / +0.57 | both halves | 9e-06 |  |
| [[FBXO44]] | +0.67 | +0.68 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SKIL]] | -0.65 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[HIVEP2]] | -0.61 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[MIS12]] | -0.60 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[C21orf91]] | -0.59 | -0.64 / -0.44 | both halves | 3e-05 |  |
| [[NEPRO-AS1]] | -0.58 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[SFR1]] | -0.57 | -0.70 / -0.47 | both halves | 2e-05 |  |
| [[LACC1]] | -0.57 | -0.68 / -0.44 | both halves | 3e-05 |  |
| [[EEA1]] | -0.56 | -0.55 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRG1]] | B | NRG1 activity raises ATPAF2's level | lines that do not express NRG1 (19) vs lines expressing it (31) | 1.22× lower at baseline in the lines without NRG1 | 0.082 | ⚠ within organs, on part of the lines; also absent: TRIM9, DOCK2, ADAM23 |
| [[LACC1]] | B | LACC1 activity lowers ATPAF2's level | lines that do not express LACC1 (6) vs lines expressing it (44) | 1.73× higher at baseline in the lines without LACC1 | 0.084 | ⚠ within organs, on part of the lines; also absent: CCDC122, IL1RAP, NABP1 |
| [[SNTA1]] | B | SNTA1 activity raises ATPAF2's level | lines that do not express SNTA1 (5) vs lines expressing it (45) | 1.26× lower at baseline in the lines without SNTA1 | 0.088 | ⚠ within organs, on part of the lines; also absent: SACS, CLTCL1, MXRA7; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.721). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-3.0, -13.6); signed map (-34.2, -8.6). **Vector** length 66.4, 10.6% of its response variance represented; |z| ≥ 3 in 867 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.4 | +8.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.3 | +9.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +1.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.7 | +9.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +9.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.6 | +2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | +8.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +3.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.9 | +2.3 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.7 | -4.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | +0.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.1 | -0.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | -2.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -3.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.6 | -1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | +1.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.4 | -1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | ATP synthase mitochondrial F1 complex assembly factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p11.2 — chr17:17,977,409-18,039,209 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Atp12p, ATP12, LP3663, MGC29736 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N5M1](https://www.uniprot.org/uniprotkb/Q8N5M1) (ATP synthase mitochondrial F1 complex assembly factor 2):

> Plays a role in the assembly of the F1 component of the mitochondrial ATP synthase (ATPase).

**Summary**, from NCBI Gene [91647](https://www.ncbi.nlm.nih.gov/gene/91647):

> This gene encodes an assembly factor for the F(1) component of the mitochondrial ATP synthase. This protein binds specifically to the F1 alpha subunit and is thought to prevent this subunit from forming nonproductive homooligomers during enzyme assembly. This gene is located within the Smith-Magenis syndrome region on chromosome 17. An alternatively spliced transcript variant has been described, but its biological validity has not been determined. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:18802](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18802) · Entrez [91647](https://www.ncbi.nlm.nih.gov/gene/91647) · UniProt [Q8N5M1](https://www.uniprot.org/uniprotkb/Q8N5M1) · Ensembl [ENSG00000171953](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171953)

## Data

Gene col 10189: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10189); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10189, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10189]; `tensor/DDL_lfc|DDL_z.npy` [10189]; `embed/gene_vectors.npy` [10189]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10189 or target_col == 10189). Every well: [[ATPAF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATPAF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
