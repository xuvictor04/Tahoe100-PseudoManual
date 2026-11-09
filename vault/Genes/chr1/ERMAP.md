---
symbol: "ERMAP"
type: "gene"
col: 8832
ensembl_id: "ENSG00000164010"
name: "erythroblast membrane associated protein (Scianna blood group)"
location: "1p34.2"
module: 23
arm: "+"
pooled_cpm: 6.67
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 12
n_dd_up_clean: 5
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# ERMAP

*erythroblast membrane associated protein (Scianna blood group)* — 1p34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.72× (z +7.0, q 1e-09, up in 23 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.362× (z -9.2, q 2e-17, down in 38 of 46 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 0.376× (z -8.9, q 2e-16, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP3CB-AS1]] (+0.80, fdr 2e-05), [[PPP1R3F]] (+0.77, fdr 1e-05), [[RFX3-DT]] (+0.76, fdr 4e-05); moves opposite to [[TSPAN33]] (-0.69, fdr 3e-05), [[UBE2O]] (-0.67, fdr 5e-05), [[YIF1B]] (-0.64, fdr 1e-04).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[WASF3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8832.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.72×** | +7.0 | 1e-09 | 23/41 (C32, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.98×** | +6.0 | 6e-07 | 3/9 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +5.6 | 3e-06 | 22/42 (LOX-IMVI, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +4.6 | 7e-04 | 6/16 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **1.60×** | +4.3 | 0.002 | 22/48 (LoVo, PANC-1, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **2.20×** | +3.8 | 0.016 | 10/46 (SW480, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Demeclocycline (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.076 | 9/46 (AsPC-1, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8832.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.362×** | -9.2 | 2e-17 | 38/46 (hTERT-HPNE, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.376×** | -8.9 | 2e-16 | 36/47 (SW480, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.415×** | -8.0 | 2e-13 | 36/46 (SW480, HT-29, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.450×** | -7.3 | 5e-11 | 30/42 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.450×** | -7.3 | 5e-11 | 34/47 (SW480, PANC-1, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.600×** | -4.6 | 3e-04 | 22/47 (HS-578T, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.615×** | -4.4 | 7e-04 | 19/47 (PANC-1, H4, …) | rises with dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.396×** | -4.4 | 7e-04 | 21/44 (NCI-H1573, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | **0.648×** | -3.9 | 0.005 | 17/44 (SW480, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **0.652×** | -3.9 | 0.006 | 19/42 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.664×** | -3.7 | 0.010 | 12/43 (PANC-1, SNU-423, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.473×** | -3.6 | 0.018 | 15/43 (Hs 766T, LS 180, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8832. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 11.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0623× (z -19.4) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 0.5 µM 0.258× (z -9.5) |
| [[LoVo (line)]] | wt | 5.53 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +8.9) | [[Belinostat (drug)]] 0.5 µM 0.0867× (z -11.3) |
| [[A-427 (line)]] | wt | 6.71 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.126× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 4.37 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.14× (z +9.0) | — |
| [[Hs 766T (line)]] | wt | 6.84 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0572× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[HT-29 (line)]] | alt | 8.20 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.115× (z -9.3) ⚠ cell-cycle shift, explains ~30% of this change |
| [[hTERT-HPNE (line)]] | wt | 6.97 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0295× (z -10.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[KATO III (line)]] | alt | 6.28 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0803× (z -9.6) ⚠ toxic |
| [[LS 180 (line)]] | wt | 7.02 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0845× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[NCI-H1573 (line)]] | alt | 4.91 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0974× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[NCI-H1792 (line)]] | alt | 6.86 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0837× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 5.61 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.5 µM 0.0897× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 8.68 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0881× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[NCI-H460 (line)]] | wt | 6.80 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0887× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[PANC-1 (line)]] | alt | 10.7 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.166× (z -8.9) ⚠ cell-cycle shift, explains ~63% of this change |
| [[RPMI-7951 (line)]] | alt | 8.34 | 0 | 1 | — | [[Flumatinib (mesylate) (drug)]] 5 µM 0.0489× (z -10.1) |
| [[SW 900 (line)]] | alt | 4.86 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 14.0× (z +8.6) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 8.06 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.31 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.85 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.50 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.97 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.81 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.37 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8832), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP3CB-AS1]] | +0.80 | +0.82 / +0.47 | both halves | 2e-05 |  |
| [[PPP1R3F]] | +0.77 | +0.72 / +0.51 | both halves | 1e-05 |  |
| [[RFX3-DT]] | +0.76 | +0.73 / +0.41 | both halves | 4e-05 |  |
| [[PBLD]] | +0.76 | +0.71 / +0.44 | both halves | 3e-05 |  |
| [[PCNX4-DT]] | +0.75 | +0.72 / +0.32 | both halves | 2e-04 |  |
| [[WARS2-AS1]] | +0.73 | +0.73 / +0.29 | both halves | 3e-04 |  |
| [[PMF1]] | +0.73 | +0.70 / +0.46 | both halves | 3e-05 |  |
| [[EFCAB2]] | +0.72 | +0.64 / +0.38 | both halves | 6e-05 |  |
| [[ERCC6L2-AS1]] | +0.72 | +0.71 / +0.29 | both halves | 2e-04 |  |
| [[FIZ1]] | +0.71 | +0.67 / +0.41 | both halves | 4e-05 |  |
| [[LRRC37A3]] | +0.71 | +0.72 / +0.22 | both halves | 6e-04 |  |
| [[CHMP3]] | +0.71 | +0.68 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSPAN33]] | -0.69 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[UBE2O]] | -0.67 | -0.66 / -0.40 | both halves | 5e-05 |  |
| [[YIF1B]] | -0.64 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[TMEM120B]] | -0.64 | -0.57 / -0.28 | both halves | 3e-04 |  |
| [[GMCL1]] | -0.64 | -0.61 / -0.36 | both halves | 9e-05 |  |
| [[TMEM256]] | -0.64 | -0.52 / -0.37 | both halves | 8e-05 |  |
| [[ECI2]] | -0.64 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[ATG4C]] | -0.64 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[CARHSP1]] | -0.63 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[ARL6]] | -0.63 | -0.55 / -0.36 | both halves | 1e-04 |  |
| [[HEBP1]] | -0.63 | -0.56 / -0.41 | both halves | 4e-05 | pathway: HALLMARK_HEME_METABOLISM |
| [[ANKRD27]] | -0.63 | -0.55 / -0.18 | ⚠ one half (not replicated) | 1e-03 |  |
| [[WASF3]] | -0.63 | -0.56 / -0.24 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WASF3]] | B | WASF3 activity raises ERMAP's level | lines that do not express WASF3 (21) vs lines expressing it (29) | 1.17× lower at baseline in the lines without WASF3 | 0.048 | ⚠ within organs, on part of the lines; also absent: SDC2, COL4A4, IGF2BP1 |
| [[HDAC6]] | B | HDAC6 activity raises ERMAP's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.675). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (6.2, 10.4); signed map (25.5, -9.7). **Vector** length 81.1, 15.1% of its response variance represented; |z| ≥ 3 in 1,045 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.4 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.9 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.8 | +2.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +6.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +1.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.1 | +4.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.4 | +3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | -0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +0.6 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -7.3 | -7.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -6.3 | -8.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -4.9 | -9.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.1 | -4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -2.8 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.6 | -3.9 |
|  | [[Brivudine (drug)]] 0.5 µM |  | -1.9 | -1.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | erythroblast membrane associated protein (Scianna blood group) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.2 — chr1:42,817,122-42,844,991 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BTN5; previously RD, SC |
| Gene groups (HGNC) | Blood group antigens; Butyrophilins; V-set domain containing |
| Hallmark sets | HEME_METABOLISM |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96PL5](https://www.uniprot.org/uniprotkb/Q96PL5) (Erythroid membrane-associated protein):

> Possible role as a cell-adhesion or receptor molecule of erythroid cells.

**Summary**, from NCBI Gene [114625](https://www.ncbi.nlm.nih.gov/gene/114625):

> The protein encoded by this gene is a cell surface transmembrane protein that may act as an erythroid cell receptor, possibly as a mediator of cell adhesion. Polymorphisms in this gene are responsible for the Scianna/Radin blood group system. Two transcript variants encoding the same protein have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:15743](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15743) · Entrez [114625](https://www.ncbi.nlm.nih.gov/gene/114625) · UniProt [Q96PL5](https://www.uniprot.org/uniprotkb/Q96PL5) · Ensembl [ENSG00000164010](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164010)

## Data

Gene col 8832: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8832); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8832, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8832]; `tensor/DDL_lfc|DDL_z.npy` [8832]; `embed/gene_vectors.npy` [8832]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8832 or target_col == 8832). Every well: [[ERMAP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERMAP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
