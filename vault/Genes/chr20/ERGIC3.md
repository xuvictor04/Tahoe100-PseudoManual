---
symbol: "ERGIC3"
type: "gene"
col: 4704
ensembl_id: "ENSG00000125991"
name: "ERGIC and golgi 3"
location: "20q11.22"
module: 30
arm: "+"
pooled_cpm: 72.27
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 10
n_dd_up_clean: 4
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# ERGIC3

*ERGIC and golgi 3* — 20q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.81× (z +10.5, q 8e-23, up in 40 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.25× (z +4.0, q 0.004, up in 26 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.670× (z -10.0, q 6e-21, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATPAF2]] (+0.61, fdr 2e-05), [[PFDN5]] (+0.61, fdr 7e-06), [[CTSD]] (+0.60, fdr 2e-05); moves opposite to [[SPDL1]] (-0.55, fdr 1e-05), [[TASOR]] (-0.54, fdr 2e-05), [[EPOP]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4704.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.81×** | +10.5 | 8e-23 | 40/48 (A549, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +8.9 | 1e-16 | 30/43 (KATO III, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +7.7 | 2e-12 | 36/47 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.38×** | +5.7 | 1e-06 | 33/47 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.36×** | +4.9 | 1e-04 | 30/44 (A549, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **1.31×** | +4.8 | 2e-04 | 29/47 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.27×** | +4.2 | 0.002 | 24/47 (NCI-H1573, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.25×** | +4.0 | 0.004 | 26/47 (HT-29, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.59×** | +3.9 | 0.005 | 23/46 (SW480, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.25×** | +3.8 | 0.008 | 23/46 (CFPAC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.50×** | +3.4 | 0.032 | 15/47 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.20×** | +3.3 | 0.051 | 19/47 (A-172, CHP-212, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.19× | +3.1 | 0.096 | 17/47 (PANC-1, NCI-H1573, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4704.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.670×** | -10.0 | 6e-21 | 39/47 (NCI-H460, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.728×** | -5.6 | 5e-06 | 31/47 (NCI-H1573, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.737×** | -5.4 | 1e-05 | 30/47 (HT-29, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.750×** | -5.1 | 5e-05 | 32/47 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.765×** | -4.8 | 2e-04 | 29/47 (AsPC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.772×** | -4.4 | 1e-03 | 25/47 (LS 180, SW480, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.812×** | -3.6 | 0.031 | 22/47 (NCI-H2347, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.828×** | -3.3 | 0.057 | 19/48 (SW480, A-427, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.830×** | -3.3 | 0.059 | 20/48 (NCI-H460, AsPC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | **0.833×** | -3.2 | 0.066 | 19/47 (AsPC-1, A498, …) | all doses, flat | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | 0.679× | -3.1 | 0.11 | 14/48 (NCI-H2347, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4704. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 92.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.53× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 70.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -15.8) |
| [[SW480 (line)]] | alt | 72.7 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 1.95× (z +9.2) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 88.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.16× (z +9.4) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 51.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +10.2) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 69.0 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +9.3) ⚠ cell-cycle shift, explains ~24% of this change | — |
| [[C32 (line)]] | wt | 51.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +8.9) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 78.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -8.9) |
| [[HOP62 (line)]] | alt | 66.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +9.5) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 103 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.543× (z -8.8) |
| [[HS-578T (line)]] | alt | 79.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -9.0) |
| [[J82 (line)]] | alt | 71.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.500× (z -11.0) |
| [[LoVo (line)]] | wt | 47.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +9.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 65.9 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +9.7) ⚠ cell-cycle shift, explains ~24% of this change | — |
| [[NCI-H1792 (line)]] | alt | 102 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.517× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 124 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.420× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 71.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.611× (z -8.9) |
| [[PANC-1 (line)]] | alt | 66.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.03× (z +8.7) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 101 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -12.2) |
| [[SNU-423 (line)]] | alt | 79.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +8.6) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 55.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 75.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 72.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.8 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 72.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 51.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 53.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 80.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 96.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 58.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 63.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 64.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 69.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 66.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 90.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 65.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 71.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 92.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 58.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4704), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATPAF2]] | +0.61 | +0.68 / +0.47 | both halves | 2e-05 |  |
| [[PFDN5]] | +0.61 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[CTSD]] | +0.60 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[GNPTG]] | +0.58 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[TMEM259]] | +0.57 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[NENF]] | +0.57 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[ATF6B]] | +0.57 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[MTCH1]] | +0.57 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[UBXN6]] | +0.56 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[ASAH1]] | +0.56 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[MAN2B2]] | +0.55 | +0.63 / +0.46 | both halves | 2e-05 |  |
| [[ADIPOR1]] | +0.55 | +0.63 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPDL1]] | -0.55 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[TASOR]] | -0.54 | -0.65 / -0.47 | both halves | 2e-05 |  |
| [[EPOP]] | -0.54 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[FBXO41]] | -0.53 | -0.65 / -0.25 | both halves | 4e-04 |  |
| [[IFRD2]] | -0.52 | -0.55 / -0.35 | both halves | 1e-04 |  |
| [[FJX1]] | -0.52 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[FOSL1]] | -0.50 | -0.46 / -0.36 | both halves | 9e-05 |  |
| [[BRCA2]] | -0.50 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[KIAA0586]] | -0.50 | -0.60 / -0.37 | both halves | 7e-05 |  |
| [[ETS1]] | -0.49 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[NSUN6]] | -0.48 | -0.56 / -0.36 | both halves | 9e-05 |  |
| [[CYREN]] | -0.48 | -0.59 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises ERGIC3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.476). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-43.0, -32.3); signed map (-50.7, -9.5). **Vector** length 75.0, 18.1% of its response variance represented; |z| ≥ 3 in 673 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +7.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +3.9 | +5.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +0.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +8.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | +2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +0.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.1 | +0.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.1 | +0.7 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.7 | -3.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.3 | -5.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.1 | -10.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.5 | -4.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.8 | +1.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -0.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.7 | +0.3 |
|  | [[vincristine (drug)]] 0.05 µM |  | -1.5 | -0.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | ERGIC and golgi 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.22 — chr20:35,542,038-35,557,634 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-54, PRO0989, NY-BR-84, Erv46; previously SDBCAG84, C20orf47 |
| Hallmark sets | PROTEIN_SECRETION |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y282](https://www.uniprot.org/uniprotkb/Q9Y282) (Endoplasmic reticulum-Golgi intermediate compartment protein 3):

> Possible role in transport between endoplasmic reticulum and Golgi. Positively regulates trafficking of the secretory proteins SERPINA1/alpha1-antitrypsin and HP/haptoglobin.

**Summary**, from NCBI Gene [51614](https://www.ncbi.nlm.nih.gov/gene/51614):

> Involved in endoplasmic reticulum to Golgi vesicle-mediated transport and positive regulation of intracellular protein transport. Located in membrane. Biomarker of lung adenocarcinoma. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:15927](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15927) · Entrez [51614](https://www.ncbi.nlm.nih.gov/gene/51614) · UniProt [Q9Y282](https://www.uniprot.org/uniprotkb/Q9Y282) · Ensembl [ENSG00000125991](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125991)

## Data

Gene col 4704: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4704); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4704, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4704]; `tensor/DDL_lfc|DDL_z.npy` [4704]; `embed/gene_vectors.npy` [4704]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4704 or target_col == 4704). Every well: [[ERGIC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERGIC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
