---
symbol: "C2orf68"
type: "gene"
col: 9716
ensembl_id: "ENSG00000168887"
name: "chromosome 2 open reading frame 68"
location: "2p11.2"
module: 16
arm: "+"
pooled_cpm: 14.63
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 23
n_dd_up_clean: 2
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# C2orf68

*chromosome 2 open reading frame 68* — 2p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.59× (z +6.0, q 1e-06, up in 16 of 25 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.33× (z +5.5, q 1e-05, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.412× (z -16.7, q 0e+00, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIGM]] (+0.69, fdr 7e-06), [[TBC1D13]] (+0.56, fdr 1e-05), [[B3GALT9]] (+0.55, fdr 3e-05); moves opposite to [[INTS6L]] (-0.47, fdr 4e-05), [[LINC00910]] (-0.44, fdr 1e-04).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NUDT7]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9716.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +6.0 | 1e-06 | 16/25 (BT-474, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +5.5 | 1e-05 | 25/48 (LoVo, HT-29, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.45×** | +5.0 | 1e-04 | 21/37 (SNU-423, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.33×** | +3.8 | 0.022 | 16/42 (A-427, NCI-H1792, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.040 | 9/47 (SW480, NCI-H23, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.27× | +3.2 | 0.14 | 6/47 (LoVo, SW480, …) | rises with dose |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 1.25× | +3.0 | 0.19 | 8/47 (A549, HepG2/C3A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9716.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.412×** | -16.7 | 0e+00 | 41/47 (NCI-H460, COLO 205, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.381×** | -12.8 | 3e-35 | 44/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.422×** | -11.5 | 2e-28 | 36/46 (HT-29, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.483×** | -9.7 | 5e-20 | 38/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.489×** | -9.5 | 2e-19 | 32/47 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.678×** | -7.3 | 3e-11 | 30/46 (A-427, SHP-77, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.614×** | -6.5 | 7e-09 | 24/45 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.636×** | -6.0 | 1e-07 | 27/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.630×** | -5.8 | 4e-07 | 28/47 (SW480, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.655×** | -5.6 | 1e-06 | 24/47 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.649×** | -5.5 | 2e-06 | 23/46 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.666×** | -5.4 | 3e-06 | 21/47 (PANC-1, LS 180, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.673×** | -5.3 | 6e-06 | 22/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[EX229 (drug)]] 5 µM |  | **0.534×** | -4.4 | 5e-04 | 22/45 (RPMI-7951, HCT15, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.535×** | -4.4 | 5e-04 | 17/34 (PANC-1, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.745×** | -3.9 | 0.003 | 11/47 (LoVo, LOX-IMVI, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.652×** | -3.6 | 0.012 | 11/48 (A-427, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.769×** | -3.5 | 0.016 | 15/46 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9716. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 16.7 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -14.5) |
| [[SW480 (line)]] | alt | 21.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -12.0) |
| [[NCI-H1573 (line)]] | alt | 23.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -18.2) |
| [[NCI-H460 (line)]] | wt | 15.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -19.2) |
| [[LoVo (line)]] | wt | 8.36 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.172× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.289× (z -9.6) |
| [[HT-29 (line)]] | alt | 20.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.149× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.250× (z -9.0) |
| [[A-427 (line)]] | wt | 35.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.124× (z -16.2) |
| [[A549 (line)]] | wt | 17.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -8.6) |
| [[C-33 A (line)]] | alt | 15.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.108× (z -9.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 5.04 | 0 | 1 | — | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM 0.0564× (z -10.3) |
| [[COLO 205 (line)]] | alt | 17.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0861× (z -18.2) |
| [[H4 (line)]] | wt | 12.4 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0655× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 15.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -11.5) |
| [[Hs 766T (line)]] | wt | 7.47 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0528× (z -12.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 9.46 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 11.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0349× (z -17.5) |
| [[LS 180 (line)]] | wt | 14.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.192× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 17.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -11.3) |
| [[NCI-H2030 (line)]] | alt | 14.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -9.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 16.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -9.9) |
| [[SK-MEL-2 (line)]] | alt | 15.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -11.1) |
| [[A-172 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.69 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.91 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.10 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9716), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGM]] | +0.69 | +0.66 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[TBC1D13]] | +0.56 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[B3GALT9]] | +0.55 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[PLPP6]] | +0.54 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[COG2]] | +0.54 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[HARS2]] | +0.54 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[TTC30A]] | +0.54 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[CEBPZOS]] | +0.53 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[ZNF212]] | +0.53 | +0.33 / +0.60 | both halves | 1e-04 |  |
| [[HERPUD2-AS1]] | +0.53 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[ZNF839]] | +0.53 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[BRD3OS]] | +0.53 | +0.49 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INTS6L]] | -0.47 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[LINC00910]] | -0.44 | -0.39 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NUDT7]] | C | NUDT7 activity raises C2orf68's level | lines that do not express NUDT7 (3) vs lines expressing it (47) | 2.07× lower at baseline in the lines without NUDT7 | 0.047 | ⚠ few lines (3 vs 47); across organs; also absent: PKN3, EZR, CORO2A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.400). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-36.0, 18.0); signed map (-19.3, -20.4). **Vector** length 60.2, 9.74% of its response variance represented; |z| ≥ 3 in 836 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +6.0 | +0.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.1 | +1.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.8 | +5.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.2 | +3.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.0 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +0.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +3.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +2.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.4 | -7.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.8 | -16.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.7 | -5.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -1.4 |
|  | [[EX229 (drug)]] 5 µM |  | -2.3 | -4.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.9 | -2.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.6 | -3.6 |
|  | [[EX229 (drug)]] 0.05 µM |  | -1.6 | -2.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.5 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | chromosome 2 open reading frame 68 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p11.2 — chr2:85,605,254-85,612,066 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [Q2NKX9](https://www.uniprot.org/uniprotkb/Q2NKX9) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:34353](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34353) · Entrez [388969](https://www.ncbi.nlm.nih.gov/gene/388969) · UniProt [Q2NKX9](https://www.uniprot.org/uniprotkb/Q2NKX9) · Ensembl [ENSG00000168887](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168887)

## Data

Gene col 9716: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9716); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9716, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9716]; `tensor/DDL_lfc|DDL_z.npy` [9716]; `embed/gene_vectors.npy` [9716]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9716 or target_col == 9716). Every well: [[C2orf68 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C2orf68.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
