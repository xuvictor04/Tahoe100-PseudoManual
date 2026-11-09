---
symbol: "GET3"
type: "gene"
col: 12577
ensembl_id: "ENSG00000198356"
name: "guided entry of tail-anchored proteins factor 3, ATPase"
location: "19p13.13"
module: 122
arm: "+"
pooled_cpm: 12.79
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 2
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/122"]
generated_by: "tahoemap"
---

# GET3

*guided entry of tail-anchored proteins factor 3, ATPase* — 19p13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (22 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.17× (z +12.9, q 3e-35, up in 34 of 37 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.78× (z +9.1, q 2e-17, up in 36 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.687× (z -6.0, q 1e-06, down in 37 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0692×); [[Pimozide (drug)]] 0.5 µM in 1 line (KATO III 0.157×; ⚠ transcription drop); [[Sodium Salicylate (drug)]] 0.5 µM in 1 line (HCT15 0.122×); [[Pyridoxine (drug)]] 0.5 µM in 1 line (SW48 0.0980×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPNS1]] (+0.70, fdr 7e-06), [[MCOLN1]] (+0.67, fdr 1e-05), [[VPS11]] (+0.66, fdr 7e-06); moves opposite to [[ESYT3]] (-0.49, fdr 5e-05), [[FLNB-AS1]] (-0.44, fdr 7e-04).
> It is in [[Module 122]], a single-armed module (Transferrin endocytosis and recycling).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 22 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12577.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **3.17×** | +12.9 | 3e-35 | 34/37 (A498, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **2.42×** | +9.5 | 6e-19 | 21/23 (A498, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +9.1 | 2e-17 | 36/46 (HS-578T, A-172, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.11×** | +7.7 | 2e-12 | 24/30 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.93×** | +7.3 | 3e-11 | 38/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +6.4 | 2e-08 | 32/41 (SW480, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **1.72×** | +6.0 | 1e-07 | 29/46 (NCI-H460, PANC-1, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.69×** | +5.8 | 4e-07 | 29/48 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **1.65×** | +5.6 | 1e-06 | 28/43 (SW1417, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +5.2 | 1e-05 | 24/47 (A-427, SNU-423, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.56×** | +4.9 | 4e-05 | 25/47 (LS 180, SW480, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.47×** | +4.3 | 8e-04 | 19/47 (NCI-H460, PANC-1, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.47×** | +4.3 | 8e-04 | 23/47 (COLO 205, RKO, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.48×** | +4.2 | 0.001 | 21/47 (HEC-1-A, SNU-423, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~53% of this change | **1.47×** | +4.1 | 0.001 | 19/41 (NCI-H23, J82, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.40×** | +3.7 | 0.007 | 14/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.39×** | +3.6 | 0.009 | 18/47 (PANC-1, NCI-H2030, …) | rises with dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.009 | 19/48 (BT-474, A-172, …) | top dose only | position effect removed |
| [[Arbutin (drug)]] 5 µM |  | **1.40×** | +3.6 | 0.009 | 15/46 (J82, HS-578T, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.51×** | +3.2 | 0.030 | 14/43 (MIA PaCa-2, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.75×** | +3.0 | 0.047 | 2/47 (NCI-H460, NCI-H2347) | top dose only | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.43×** | +2.8 | 0.092 | 8/45 (LoVo, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12577.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0692×); [[Pimozide (drug)]] 0.5 µM in 1 line (KATO III 0.157×; ⚠ transcription drop); [[Sodium Salicylate (drug)]] 0.5 µM in 1 line (HCT15 0.122×); [[Pyridoxine (drug)]] 0.5 µM in 1 line (SW48 0.0980×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.687×** | -6.0 | 1e-06 | 37/48 (MIA PaCa-2, BT-474, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.634×** | -5.1 | 8e-05 | 25/47 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~17% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12577. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 21.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H460 (line)]] | wt | 10.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.38× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[A-172 (line)]] | wt | 18.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.11× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[HCT15 (line)]] | alt | 15.0 | 0 | 1 | — | [[Sodium Salicylate (drug)]] 0.5 µM 0.122× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 14.0 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0692× (z -10.9) |
| [[KATO III (line)]] | alt | 9.03 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.157× (z -9.5) ⚠ transcription drop |
| [[NCI-H1573 (line)]] | alt | 9.41 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.81× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[PANC-1 (line)]] | alt | 9.84 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.61× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[SW48 (line)]] | wt | 12.3 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0980× (z -8.8) |
| [[SW480 (line)]] | alt | 10.7 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.62× (z +8.6) ⚠ toxic | — |
| [[A-427 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.12 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.19 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.13 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.77 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.16 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12577), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPNS1]] | +0.70 | +0.60 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[MCOLN1]] | +0.67 | +0.61 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[VPS11]] | +0.66 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[TRAPPC2L]] | +0.64 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[ZFYVE26]] | +0.63 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[UROD]] | +0.61 | +0.40 / +0.70 | both halves | 5e-05 |  |
| [[APH1A]] | +0.61 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[TMUB2]] | +0.58 | +0.37 / +0.56 | both halves | 7e-05 |  |
| [[HEXA]] | +0.58 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[CSNK2B]] | +0.57 | +0.28 / +0.66 | both halves | 3e-04 |  |
| [[MED25]] | +0.56 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[COMMD9]] | +0.56 | +0.47 / +0.66 | both halves | 2e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ESYT3]] | -0.49 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[FLNB-AS1]] | -0.44 | -0.54 / -0.21 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GET3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[EFCAB6]] | B | EFCAB6 activity raises GET3's level | lines that do not express EFCAB6 (5) vs lines expressing it (45) | 1.53× lower at baseline in the lines without EFCAB6 | 0.088 | ⚠ within organs, on part of the lines; also absent: ITGA2B, THBS3-AS1, CYP46A1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 122]] — Transferrin endocytosis and recycling; 40 genes; every member is in the + arm (projection on the module's main direction 0.674). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-16.4, -17.2); signed map (-9.8, -21.0). **Vector** length 53.1, 8.28% of its response variance represented; |z| ≥ 3 in 752 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +9.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +3.0 | +7.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +1.9 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +3.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | +1.9 | +12.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +5.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.4 | +1.7 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | +1.3 | +2.5 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.3 | +2.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.1 | -6.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.2 | -5.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.1 | -0.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -0.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.3 | -0.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.0 | -1.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -0.9 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | guided entry of tail-anchored proteins factor 3, ATPase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.13 — chr19:12,737,139-12,748,323 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ARSA-I, TRC40; previously ASNA1 |
| Gene groups (HGNC) | Guided entry of tail-anchored proteins complex subunits; GET4-GET5 transmembrane domain recognition complex subunits |
| Reactome | 2 pathways, smallest: Insertion of tail-anchored proteins into the endoplasmic reticulum membrane; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [O43681](https://www.uniprot.org/uniprotkb/O43681) (ATPase GET3):

> ATPase required for the post-translational delivery of tail-anchored (TA) proteins to the endoplasmic reticulum. Recognizes and selectively binds the transmembrane domain of TA proteins in the cytosol. This complex then targets to the endoplasmic reticulum by membrane-bound receptors GET1/WRB and CAMLG/GET2, where the tail-anchored protein is released for insertion. This process is regulated by ATP binding and hydrolysis. ATP binding drives the homodimer towards the closed dimer state, …

**Summary**, from NCBI Gene [439](https://www.ncbi.nlm.nih.gov/gene/439):

> This gene represents the human homolog of the bacterial arsA gene, encoding the arsenite-stimulated ATPase component of the arsenite transporter responsible for resistance to arsenicals. This protein is also a central component of a transmembrane domain (TMD) recognition complex (TRC) that is involved in the post-translational delivery of tail-anchored (TA) proteins from the cytosol to the endoplasmic reticulum (ER). It recognizes and selectively binds the TMD of TA proteins in the cytosol, and …

**Accessions** — [HGNC:752](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:752) · Entrez [439](https://www.ncbi.nlm.nih.gov/gene/439) · UniProt [O43681](https://www.uniprot.org/uniprotkb/O43681) · Ensembl [ENSG00000198356](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198356)

## Data

Gene col 12577: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12577); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12577, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12577]; `tensor/DDL_lfc|DDL_z.npy` [12577]; `embed/gene_vectors.npy` [12577]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12577 or target_col == 12577). Every well: [[GET3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GET3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
