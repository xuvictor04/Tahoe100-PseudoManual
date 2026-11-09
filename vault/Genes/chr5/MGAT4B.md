---
symbol: "MGAT4B"
type: "gene"
col: 8409
ensembl_id: "ENSG00000161013"
name: "alpha-1,3-mannosyl-glycoprotein 4-beta-N-acetylglucosaminyltransferase B"
location: "5q35.3"
module: 138
arm: "+"
pooled_cpm: 25.55
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 18
n_dd_up_clean: 8
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/138"]
generated_by: "tahoemap"
---

# MGAT4B

*alpha-1,3-mannosyl-glycoprotein 4-beta-N-acetylglucosaminyltransferase B* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.97× (z +8.7, q 2e-15, up in 30 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.51× (z +5.3, q 1e-05, up in 27 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.461× (z -9.9, q 2e-20, down in 43 of 48 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.622× (z -6.1, q 2e-07, down in 31 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF103]] (+0.65, fdr 1e-05), [[RNPEPL1]] (+0.59, fdr 1e-05), [[SH2B1]] (+0.57, fdr 1e-05); moves opposite to [[ZNF215]] (-0.45, fdr 1e-04), [[PAG1]] (-0.43, fdr 2e-04), [[ATP5MC1]] (-0.42, fdr 4e-04).
> It is in [[Module 138]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GULP1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8409.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.97×** | +8.7 | 2e-15 | 30/39 (LoVo, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +6.2 | 1e-07 | 24/37 (LoVo, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.62×** | +6.2 | 1e-07 | 33/44 (CFPAC-1, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.51×** | +5.3 | 1e-05 | 27/47 (LoVo, Panc 03.27, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +5.3 | 1e-05 | 17/33 (PANC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +3.9 | 0.010 | 23/45 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.34×** | +3.8 | 0.012 | 20/47 (NCI-H1792, A498, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.70×** | +3.8 | 0.012 | 18/44 (LS 180, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.025 | 20/47 (AsPC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.61×** | +3.4 | 0.045 | 8/45 (LoVo, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.59×** | +3.3 | 0.050 | 12/46 (AsPC-1, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.56×** | +3.2 | 0.077 | 10/46 (HEC-1-A, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.54×** | +3.1 | 0.097 | 8/45 (HCT15, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8409.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.461×** | -9.9 | 2e-20 | 43/48 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.488×** | -9.2 | 1e-17 | 42/48 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.530×** | -8.1 | 8e-14 | 41/47 (HepG2/C3A, C-33 A, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.622×** | -6.1 | 2e-07 | 31/47 (HEC-1-A, A-172, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.745×** | -5.3 | 1e-05 | 23/47 (NCI-H23, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.669×** | -5.1 | 3e-05 | 25/48 (J82, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.686×** | -4.8 | 1e-04 | 22/48 (A-172, SW 900, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.704×** | -4.5 | 5e-04 | 24/48 (SK-MEL-2, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.705×** | -4.5 | 5e-04 | 26/48 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.696×** | -4.5 | 5e-04 | 23/47 (RPMI-7951, Panc 03.27, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.669×** | -4.2 | 0.001 | 23/47 (RKO, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.720×** | -4.2 | 0.001 | 25/47 (SNU-423, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.739×** | -3.7 | 0.008 | 21/48 (NCI-H1573, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.748×** | -3.7 | 0.008 | 20/48 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.741×** | -3.4 | 0.023 | 16/47 (SW 1271, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.781×** | -3.0 | 0.093 | 22/48 (SHP-77, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.848× | -3.0 | 0.093 | 19/48 (SK-MEL-2, SW 900, …) | top dose only | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.615×** | -3.0 | 0.093 | 17/44 (A-427, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.41 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8409. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 46.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -9.0) |
| [[LoVo (line)]] | wt | 35.4 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +9.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.252× (z -11.4) ⚠ cell-cycle shift, explains ~33% of this change |
| [[NCI-H23 (line)]] | alt | 13.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 47.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0711× (z -20.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 26.7 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.187× (z -8.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H1573 (line)]] | alt | 16.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -8.5) |
| [[RKO (line)]] | wt | 17.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0490× (z -13.7) |
| [[SK-MEL-2 (line)]] | alt | 31.5 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.279× (z -8.5) ⚠ cell-cycle shift, explains ~53% of this change |
| [[SNU-1 (line)]] | wt | 27.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -8.8) |
| [[SW 900 (line)]] | alt | 29.8 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.271× (z -8.6) ⚠ cell-cycle shift, explains ~33% of this change |
| [[A-427 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 18.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8409), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF103]] | +0.65 | +0.54 / +0.59 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation |
| [[RNPEPL1]] | +0.59 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[SH2B1]] | +0.57 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[ZFTA]] | +0.56 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[ZFTRAF1]] | +0.55 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[STX3]] | +0.55 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[INPPL1]] | +0.55 | +0.56 / +0.46 | both halves | 2e-05 |  |
| [[TEPSIN]] | +0.55 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[GET4]] | +0.53 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[EGLN2]] | +0.52 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[CRTC2]] | +0.52 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[NPIPA1]] | +0.52 | +0.48 / +0.52 | both halves | 2e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF215]] | -0.45 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[PAG1]] | -0.43 | -0.33 / -0.32 | both halves | 2e-04 |  |
| [[ATP5MC1]] | -0.42 | -0.50 / -0.25 | both halves | 4e-04 |  |
| [[FSBP]] | -0.41 | -0.35 / -0.44 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GULP1]] | C | GULP1 activity strengthens MGAT4B's drug response | lines that do not express GULP1 (4) vs lines expressing it (44) | the lines without GULP1 respond 0.79× as strongly (z diff +0.49); strongest at Dinaciclib 5 µM: 0.18x vs 1.47x (z diff +9.3) | 0.096 | ⚠ few lines (4 vs 46); across organs; also absent: RND3, SFXN3, LRRCC1; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 138]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.601). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.2, -21.3); signed map (3.3, -6.8). **Vector** length 79.6, 17.7% of its response variance represented; |z| ≥ 3 in 836 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | +1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +5.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.9 | +3.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.4 | +6.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +2.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.8 | +3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +3.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.7 | +1.4 |
|  | [[crizotinib (drug)]] 5 µM |  | +2.6 | +1.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.4 | -3.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.2 | -9.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.1 | -4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -3.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -1.8 | -9.2 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -1.8 | -1.9 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.6 | +0.4 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.5 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | alpha-1,3-mannosyl-glycoprotein 4-beta-N-acetylglucosaminyltransferase B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:179,797,597-179,806,952 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GnT-Ivb |
| Gene groups (HGNC) | Mannosyl-glycoprotein N-acetylglucosaminyltransferases; MicroRNA protein coding host genes |
| Reactome | 10 pathways, smallest: N-Glycan antennae elongation; N-glycan antennae elongation in the medial/trans-Golgi; Maturation of spike protein_9694548 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UQ53](https://www.uniprot.org/uniprotkb/Q9UQ53) (Alpha-1,3-mannosyl-glycoprotein 4-beta-N-acetylglucosaminyltransferase B):

> Glycosyltransferase that catalyzes the transfer of GlcNAc from UDP-GlcNAc to the GlcNAcbeta1-2Manalpha1-3 arm of the core structure of N-linked glycans through a beta1-4 linkage and participates in the production of tri- and tetra-antennary N-linked sugar chains. Prefers complex-type N-glycans over hybrid-types. Has lower affinities for donors or acceptors than MGAT4A, suggesting that, under physiological conditions, it is not the main contributor in N-glycan biosynthesis.

**Summary**, from NCBI Gene [11282](https://www.ncbi.nlm.nih.gov/gene/11282):

> This gene encodes a key glycosyltransferase that regulates the formation of tri- and multiantennary branching structures in the Golgi apparatus. The encoded protein, in addition to the related isoenzyme A, catalyzes the transfer of N-acetylglucosamine (GlcNAc) from UDP-GlcNAc in a beta-1,4 linkage to the Man-alpha-1,3-Man-beta-1,4-GlcNAc arm of R-Man-alpha-1,6(GlcNAc-beta-1,2-Man-alpha-1,3)Man-beta-1,4-GlcNAc-beta-1,4-GlcNAc-beta-1-Asn. The encoded protein may play a role in regulating the …

**Accessions** — [HGNC:7048](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7048) · Entrez [11282](https://www.ncbi.nlm.nih.gov/gene/11282) · UniProt [Q9UQ53](https://www.uniprot.org/uniprotkb/Q9UQ53) · Ensembl [ENSG00000161013](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161013)

## Data

Gene col 8409: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8409); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8409, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8409]; `tensor/DDL_lfc|DDL_z.npy` [8409]; `embed/gene_vectors.npy` [8409]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8409 or target_col == 8409). Every well: [[MGAT4B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MGAT4B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
