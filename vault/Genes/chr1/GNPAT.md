---
symbol: "GNPAT"
type: "gene"
col: 3855
ensembl_id: "ENSG00000116906"
name: "glyceronephosphate O-acyltransferase"
location: "1q42.2"
module: 198
arm: "+"
pooled_cpm: 46.28
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 3
n_dd_up_clean: 3
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/198"]
generated_by: "tahoemap"
---

# GNPAT

*glyceronephosphate O-acyltransferase* — 1q42.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.36× (z +7.1, q 8e-10, up in 25 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Palmatine (chloride) (drug)]] 0.5 µM: 1.19× (z +4.1, q 0.006, up in 15 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.740× (z -10.3, q 4e-22, down in 29 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CIAO3]] (+0.58, fdr 1e-05), [[TAB1]] (+0.57, fdr 1e-05), [[FBXO9]] (+0.56, fdr 1e-05); moves opposite to [[SLC8A2]] (-0.55, fdr 2e-05), [[FSCN2]] (-0.53, fdr 3e-05), [[PDE2A]] (-0.46, fdr 8e-05).
> It is in [[Module 198]], a single-armed module (Antigen processing: Ubiquitination & Proteasome degradation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[WNT7B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3855.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +7.1 | 8e-10 | 25/41 (A-172, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.25×** | +5.3 | 4e-05 | 23/46 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | 1.19× | +4.1 | 0.006 | 15/48 (SW48, MIA PaCa-2, …) | two highest doses | position effect removed |
| [[Alpelisib (drug)]] 5 µM |  | **1.37×** | +4.0 | 0.008 | 14/46 (SW480, LoVo, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Alpelisib (drug)]] 0.05 µM |  | 1.19× | +4.0 | 0.008 | 15/48 (PANC-1, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.17× | +3.8 | 0.014 | 15/47 (A-172, A498, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **1.33×** | +3.6 | 0.028 | 12/47 (KATO III, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +3.5 | 0.039 | 10/42 (HepG2/C3A, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 1.15× | +3.4 | 0.042 | 10/48 (LoVo, A498, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.3 | 0.054 | 11/47 (SW 900, LS 180, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.20×** | +3.2 | 0.083 | 10/47 (RKO, BT-474, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3855.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.740×** | -10.3 | 4e-22 | 29/47 (A-172, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.740×** | -7.3 | 9e-11 | 31/48 (A-172, NCI-H460, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.837× | -4.3 | 0.003 | 19/48 (NCI-H460, KATO III, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.853× | -3.9 | 0.016 | 16/48 (NCI-H460, SW480, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.902× | -3.5 | 0.046 | 20/48 (NCI-H1573, HOP62, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 0.869× | -3.4 | 0.065 | 18/48 (SW480, SW1417, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.768×** | -3.3 | 0.067 | 17/49 (A-427, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.881× | -3.1 | 0.15 | 13/48 (Panc 03.27, SW480, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3855. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 64.9 | 0 | 5 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.460× (z -11.9) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.617× (z -10.4) |
| [[A-172 (line)]] | wt | 58.3 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.12× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -18.2) |
| [[A-427 (line)]] | wt | 61.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.127× (z -22.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.496× (z -11.4) |
| [[HOP62 (line)]] | alt | 48.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.502× (z -11.7) |
| [[A549 (line)]] | wt | 51.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.415× (z -8.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 26.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.314× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[C-33 A (line)]] | alt | 58.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.251× (z -11.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 32.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -9.9) |
| [[COLO 205 (line)]] | alt | 57.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.131× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 69.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.333× (z -9.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 42.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -12.1) |
| [[J82 (line)]] | alt | 34.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.512× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 42.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.556× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 43.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -9.3) ⚠ cell-cycle shift, explains ~16% of this change |
| [[NCI-H1792 (line)]] | alt | 44.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.501× (z -9.3) |
| [[NCI-H661 (line)]] | alt | 62.3 | 0 | 1 | — | [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.0724× (z -11.9) |
| [[SK-MEL-2 (line)]] | alt | 38.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 37.3 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.347× (z -9.7) |
| [[SNU-423 (line)]] | alt | 39.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -11.0) |
| [[SW480 (line)]] | alt | 63.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.598× (z -8.7) ⚠ cell-cycle shift, explains ~14% of this change |
| [[A498 (line)]] | wt | 38.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 59.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 47.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 64.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 62.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 43.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3855), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIAO3]] | +0.58 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[TAB1]] | +0.57 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[FBXO9]] | +0.56 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[MRPS5]] | +0.55 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[MTFMT]] | +0.55 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[DTWD1]] | +0.55 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[GTF2H2B]] | +0.55 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[ZNF224]] | +0.54 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[PHC3]] | +0.54 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[NTPCR]] | +0.53 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[MRPL1]] | +0.52 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[GTF2H2]] | +0.52 | +0.59 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC8A2]] | -0.55 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[FSCN2]] | -0.53 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[PDE2A]] | -0.46 | -0.49 / -0.37 | both halves | 8e-05 |  |
| [[ALPK3]] | -0.46 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[TMPRSS9]] | -0.45 | -0.37 / -0.39 | both halves | 9e-05 |  |
| [[LINC00243]] | -0.45 | -0.40 / -0.43 | both halves | 4e-05 |  |
| [[RCOR1]] | -0.44 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[RELT]] | -0.44 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[EFCAB8]] | -0.43 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[SNAP25-AS1]] | -0.43 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[WNT7B]] | -0.43 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[ITPR2-AS1]] | -0.43 | -0.34 / -0.48 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WNT7B]] | B | WNT7B activity lowers GNPAT's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 1.22× higher at baseline in the lines without WNT7B | 0.039 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG |
| [[EPHA1-AS1]] | B | EPHA1-AS1 activity lowers GNPAT's level | lines that do not express EPHA1-AS1 (6) vs lines expressing it (44) | 1.27× higher at baseline in the lines without EPHA1-AS1 | 0.091 | ⚠ within organs, on part of the lines; also absent: GNA14, RIPOR2, SSUH2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 198]] — Antigen processing: Ubiquitination & Proteasome degradation; 16 genes; every member is in the + arm (projection on the module's main direction 0.608). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-19.1, -0.6); signed map (-16.9, -14.1). **Vector** length 74.8, 13.3% of its response variance represented; |z| ≥ 3 in 762 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.8 |
|  | [[NG25 (drug)]] 5 µM |  | +3.0 | +3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.8 | +5.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.6 | +3.3 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.0 | +2.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.0 | +2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | +0.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.9 | +1.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.3 | -7.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.0 | -10.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -2.8 | -3.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | -1.9 | -1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -2.1 |
|  | [[9-ING-41 (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Auranofin (drug)]] 0.5 µM |  | -1.2 | -1.4 |
|  | [[Cinacalcet (drug)]] 5 µM |  | -1.2 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | glyceronephosphate O-acyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.2 — chr1:231,241,207-231,277,973 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DHAPAT, DAPAT, DAP-AT |
| Gene groups (HGNC) | Acyltransferases |
| Hallmark sets | BILE_ACID_METABOLISM, PEROXISOME |
| Reactome | 8 pathways, smallest: Plasmalogen biosynthesis; Wax and plasmalogen biosynthesis; Synthesis of PA |
| Matched by | ensembl_id |

**Function**, from UniProt [O15228](https://www.uniprot.org/uniprotkb/O15228) (Dihydroxyacetone phosphate acyltransferase):

> Dihydroxyacetonephosphate acyltransferase catalyzing the first step in the biosynthesis of plasmalogens, a subset of phospholipids that differ from other glycerolipids by having an alkyl chain attached through a vinyl ether linkage at the sn-1 position of the glycerol backbone, and which unique physical properties have an impact on various aspects of cell signaling and membrane biology.

**Summary**, from NCBI Gene [8443](https://www.ncbi.nlm.nih.gov/gene/8443):

> This gene encodes an enzyme located in the peroxisomal membrane which is essential to the synthesis of ether phospholipids. Mutations in this gene are associated with rhizomelic chondrodysplasia punctata. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct 2015]

**Accessions** — [HGNC:4416](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4416) · Entrez [8443](https://www.ncbi.nlm.nih.gov/gene/8443) · UniProt [O15228](https://www.uniprot.org/uniprotkb/O15228) · Ensembl [ENSG00000116906](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116906)

## Data

Gene col 3855: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3855); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3855, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3855]; `tensor/DDL_lfc|DDL_z.npy` [3855]; `embed/gene_vectors.npy` [3855]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3855 or target_col == 3855). Every well: [[GNPAT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GNPAT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
