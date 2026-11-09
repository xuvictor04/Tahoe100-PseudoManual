---
symbol: "TSPAN4"
type: "gene"
col: 13169
ensembl_id: "ENSG00000214063"
name: "tetraspanin 4"
location: "11p15.5"
module: 78
arm: "+"
pooled_cpm: 26.19
n_lines_expressing: 43
n_dd_up: 6
n_dd_down: 24
n_dd_up_clean: 2
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 7
direction_downstream: 6
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# TSPAN4

*tetraspanin 4* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.28× (z +9.9, q 2e-20, up in 28 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[vincristine (drug)]] 0.5 µM: 1.67× (z +3.8, q 0.019, up in 16 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1792 3.43×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A498 3.01×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (SNU-423 3.14×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (5 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.423× (z -9.8, q 4e-20, down in 34 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STMN3]] (+0.70, fdr 7e-06), [[ITGA3]] (+0.60, fdr 1e-05), [[RASA3]] (+0.58, fdr 1e-05); moves opposite to [[PSMA3]] (-0.53, fdr 3e-05), [[PSMA4]] (-0.49, fdr 3e-05), [[KEAP1]] (-0.48, fdr 1e-04).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 6 go from it, the strongest it → [[VIM]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13169.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1792 3.43×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A498 3.01×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (SNU-423 3.14×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.28×** | +9.9 | 2e-20 | 28/35 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.02×** | +8.2 | 1e-13 | 18/26 (SNU-423, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.86×** | +6.6 | 8e-09 | 19/29 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.38×** | +3.9 | 0.013 | 14/40 (Hs 766T, NCI-H2347, …) | top dose only | position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **1.67×** | +3.8 | 0.019 | 16/40 (NCI-H1792, HT-29, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.63×** | +3.6 | 0.032 | 14/38 (RKO, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.55× | +3.2 | 0.11 | 5/38 (HS-578T, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13169.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.423×** | -9.8 | 4e-20 | 34/40 (HOP62, J82, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.535×** | -7.6 | 1e-11 | 28/41 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.608×** | -6.0 | 3e-07 | 27/41 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.609×** | -6.0 | 3e-07 | 26/41 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.611×** | -6.0 | 3e-07 | 29/41 (HOP62, SK-MEL-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.358×** | -5.6 | 2e-06 | 21/33 (A-172, HOP62, …) | all doses, flat | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.647×** | -5.3 | 1e-05 | 24/40 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.751×** | -4.9 | 6e-05 | 23/41 (CFPAC-1, Hs 766T, …) | rises with dose | low cells (technical?) |
| [[Trametinib (drug)]] 5 µM |  | **0.658×** | -4.7 | 1e-04 | 27/41 (HEC-1-A, A549, …) | all doses, flat | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.641×** | -4.7 | 1e-04 | 22/41 (HEC-1-A, Hs 766T, …) | all doses, flat | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.680×** | -4.7 | 2e-04 | 23/41 (SK-MEL-2, HOP62, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.684×** | -4.4 | 4e-04 | 24/40 (HEC-1-A, NCI-H1792, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.698×** | -4.4 | 6e-04 | 18/40 (HEC-1-A, CFPAC-1, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.690×** | -4.3 | 6e-04 | 16/40 (CFPAC-1, SW 900, …) | all doses, flat | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.712×** | -4.1 | 0.001 | 23/41 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.792×** | -3.9 | 0.003 | 17/41 (NCI-H1792, SW480, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.754×** | -3.4 | 0.019 | 17/41 (HOP62, SNU-423, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.759×** | -3.3 | 0.024 | 15/41 (HEC-1-A, SNU-1, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.791×** | -3.3 | 0.033 | 15/41 (HEC-1-A, LoVo, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13169. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 82.7 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -15.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.166× (z -13.8) |
| [[MIA PaCa-2 (line)]] | alt | 31.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.187× (z -10.5) |
| [[SNU-423 (line)]] | alt | 52.2 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.14× (z +8.5) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 0.05 µM 0.293× (z -8.9) |
| [[A-172 (line)]] | wt | 67.3 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.389× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 16.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 48.7 | 0 | 2 | — | [[Bortezomib (drug)]] 0.05 µM 0.264× (z -9.9) |
| [[SK-MEL-2 (line)]] | alt | 38.6 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.238× (z -9.2) |
| [[SNU-1 (line)]] | wt | 38.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.222× (z -8.7) |
| [[A498 (line)]] | wt | 55.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.01× (z +8.6) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 16.1 | 0 | 1 | — | [[Dihydroartemisinin (drug)]] 5 µM 0.0528× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 13.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[RKO (line)]] | wt | 15.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.144× (z -10.3) |
| [[A-427 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 56.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.22 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 9.48 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.14 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.08 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.65 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.49 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.98 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 18.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13169), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STMN3]] | +0.70 | +0.67 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[ITGA3]] | +0.60 | +0.61 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_APICAL_JUNCTION; STRING 482 |
| [[RASA3]] | +0.58 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[LAPTM5]] | +0.57 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[FMNL1-DT]] | +0.57 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[FMNL1]] | +0.57 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[SPRY4]] | +0.56 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[RPSAP52]] | +0.54 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[MAP2K3]] | +0.53 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[SLCO4A1]] | +0.53 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[CMTM3]] | +0.53 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[HMGA2-AS1]] | +0.53 | +0.48 / +0.51 | both halves | 2e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMA3]] | -0.53 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[PSMA4]] | -0.49 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[KEAP1]] | -0.48 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[CYP4F3]] | -0.47 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[PIR]] | -0.46 | -0.54 / -0.39 | both halves | 5e-05 |  |
| [[GTF3C3]] | -0.46 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[PSMA1]] | -0.45 | -0.40 / -0.44 | both halves | 4e-05 |  |
| [[SPR]] | -0.44 | -0.50 / -0.25 | both halves | 4e-04 |  |
| [[AKR1C1]] | -0.44 | -0.47 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TSPAN4's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[AXL]] | B | AXL activity raises TSPAN4's level | lines that do not express AXL (14) vs lines expressing it (36) | 2.59× lower at baseline in the lines without AXL | 0.041 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: LGALS1, ENSG00000289526, LTBP2 |
| [[C13orf46]] | B | C13orf46 activity raises TSPAN4's level | lines that do not express C13orf46 (11) vs lines expressing it (39) | 2.15× lower at baseline in the lines without C13orf46 | 0.043 | ⚠ within organs, on part of the lines; also absent: RASA3, COL27A1, PRR5L |
| [[GYPC]] | B | GYPC activity raises TSPAN4's level | lines that do not express GYPC (35) vs lines expressing it (15) | 2.38× lower at baseline in the lines without GYPC | 0.051 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PHACTR1, ANKRD30B, PLPP4 |
| [[CYP4F3]] | B | CYP4F3 activity lowers TSPAN4's level | lines that do not express CYP4F3 (29) vs lines expressing it (21) | 1.72× higher at baseline in the lines without CYP4F3 | 0.077 | ⚠ within organs, on part of the lines; also absent: P2RY2, CYP3A5, ITGB6 |
| [[LINC02813]] | B | LINC02813 activity raises TSPAN4's level | lines that do not express LINC02813 (26) vs lines expressing it (24) | 1.84× lower at baseline in the lines without LINC02813 | 0.078 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, ENSG00000260517, CUBN |
| [[VIM]] | B | VIM activity raises TSPAN4's level | lines that do not express VIM (18) vs lines expressing it (32) | 2.42× lower at baseline in the lines without VIM | 0.094 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: LOXL2, ADAMTS18, MAP1B |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VIM]] | B | TSPAN4 activity raises VIM's level | lines that do not express TSPAN4 (7) vs lines expressing it (43) | 10.90× lower at baseline in the lines without TSPAN4 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: TRPC1, EMP3, PXDC1; maybe low, not absent |
| [[CYP4F3]] | B | TSPAN4 activity lowers CYP4F3's level | lines that do not express TSPAN4 (7) vs lines expressing it (43) | 5.32× higher at baseline in the lines without TSPAN4 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: TRPC1, EMP3, PXDC1; maybe low, not absent |
| [[TGFB1]] | B | TSPAN4 activity raises TGFB1's level | lines that do not express TSPAN4 (7) vs lines expressing it (43) | 2.79× lower at baseline in the lines without TSPAN4 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: TRPC1, EMP3, PXDC1; maybe low, not absent |
| [[MFSD10]] | B | TSPAN4 activity raises MFSD10's level | lines that do not express TSPAN4 (7) vs lines expressing it (43) | 1.41× lower at baseline in the lines without TSPAN4 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: TRPC1, EMP3, PXDC1; maybe low, not absent |
| [[PLXNA1]] | B | TSPAN4 activity raises PLXNA1's level | lines that do not express TSPAN4 (7) vs lines expressing it (43) | 1.66× lower at baseline in the lines without TSPAN4 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: TRPC1, EMP3, PXDC1; maybe low, not absent |
| [[CMTM3]] | C | TSPAN4 activity raises CMTM3's level | lines that do not express TSPAN4 (7) vs lines expressing it (43) | 4.65× lower at baseline in the lines without TSPAN4 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: TRPC1, EMP3, PXDC1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.499). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (51.7, 1.5); signed map (6.2, 51.8). **Vector** length 83.0, 19.3% of its response variance represented; |z| ≥ 3 in 880 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.4 | -0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +3.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +1.8 | -2.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +1.7 | +3.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | +1.5 | +2.3 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.4 | +3.0 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.3 | +0.7 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -4.9 | -9.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.5 | -7.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.0 | -6.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -3.9 | -5.6 |
|  | [[Trametinib (drug)]] 5 µM |  | -3.7 | -4.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.7 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.6 | -4.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.4 | -4.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.3 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | tetraspanin 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:842,812-867,116 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NAG-2, TSPAN-4, TETRASPAN; previously TM4SF7 |
| Gene groups (HGNC) | Tetraspanin family |
| Hallmark sets | APICAL_JUNCTION |
| Matched by | ensembl_id |

**Function**, from UniProt [O14817](https://www.uniprot.org/uniprotkb/O14817) (Tetraspanin-4):

> Structural component of specialized membrane microdomains known as tetraspanin-enriched microdomains (TERMs), which act as platforms for receptor clustering and signaling. Plays an essential role in migrasome formation and migration on retracting fibers at the rear end of migrating cells. Migrasomes are cellular organelles that form as large vesicle-like structures on retraction fibers of migrating cells. Mechanistically, acts as a membrane curvature sensor and participates in stabilizing the …

**Summary**, from NCBI Gene [7106](https://www.ncbi.nlm.nih.gov/gene/7106):

> The protein encoded by this gene is a member of the transmembrane 4 superfamily, also known as the tetraspanin family. Most of these members are cell-surface proteins that are characterized by the presence of four hydrophobic domains. The proteins mediate signal transduction events that play a role in the regulation of cell development, activation, growth and motility. This encoded protein is a cell surface glycoprotein and is similar in sequence to its family member CD53 antigen. It is known …

**Accessions** — [HGNC:11859](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11859) · Entrez [7106](https://www.ncbi.nlm.nih.gov/gene/7106) · UniProt [O14817](https://www.uniprot.org/uniprotkb/O14817) · Ensembl [ENSG00000214063](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214063)

## Data

Gene col 13169: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13169); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13169, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13169]; `tensor/DDL_lfc|DDL_z.npy` [13169]; `embed/gene_vectors.npy` [13169]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13169 or target_col == 13169). Every well: [[TSPAN4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSPAN4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
