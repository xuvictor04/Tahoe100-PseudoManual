---
symbol: "LAMB2"
type: "gene"
col: 10202
ensembl_id: "ENSG00000172037"
name: "laminin subunit beta 2"
location: "3p21.31"
module: 50
arm: "+"
pooled_cpm: 28.7
n_lines_expressing: 48
n_dd_up: 5
n_dd_down: 17
n_dd_up_clean: 1
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# LAMB2

*laminin subunit beta 2* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.03× (z +8.4, q 9e-15, up in 27 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 1.57× (z +3.9, q 0.009, up in 23 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HEC-1-A 3.86×, HS-578T 2.82×, LoVo 3.82×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 3.96×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HEC-1-A 3.58×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.438× (z -14.5, q 7e-45, down in 41 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRKCSH]] (+0.74, fdr 7e-06), [[ATP6AP1]] (+0.66, fdr 1e-05), [[TLE5]] (+0.64, fdr 7e-06); moves opposite to [[FBXO45]] (-0.53, fdr 3e-05), [[CCDC137]] (-0.50, fdr 2e-05), [[MRPL36]] (-0.49, fdr 4e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MYL9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10202.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HEC-1-A 3.86×, HS-578T 2.82×, LoVo 3.82×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 3.96×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HEC-1-A 3.58×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.03×** | +8.4 | 9e-15 | 27/35 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.98×** | +8.4 | 9e-15 | 38/43 (HEC-1-A, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.73×** | +5.8 | 1e-06 | 26/40 (HEC-1-A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.36×** | +5.3 | 2e-05 | 31/46 (C32, BT-474, …) | rises with dose | low cells (technical?); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.57×** | +3.9 | 0.009 | 23/44 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | 1.44× | +3.2 | 0.11 | 17/46 (HOP62, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | 1.32× | +3.2 | 0.11 | 12/46 (HEC-1-A, A498, …) | inconsistent across doses | position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 1.62× | +3.1 | 0.14 | 14/40 (J82, A498, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10202.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.438×** | -14.5 | 7e-45 | 41/45 (SNU-423, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.382×** | -11.9 | 2e-30 | 39/45 (hTERT-HPNE, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.431×** | -10.0 | 2e-21 | 39/46 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.537×** | -7.7 | 2e-12 | 43/46 (HOP62, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.607×** | -6.0 | 3e-07 | 31/46 (HS-578T, HepG2/C3A, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.676×** | -4.9 | 1e-04 | 25/46 (NCI-H1792, SNU-423, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.681×** | -4.8 | 1e-04 | 28/46 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.687×** | -4.7 | 2e-04 | 24/46 (LOX-IMVI, SK-MEL-2, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.498×** | -4.5 | 4e-04 | 26/41 (SW1417, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.783×** | -4.3 | 9e-04 | 25/46 (SNU-1, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.725×** | -4.0 | 0.003 | 25/46 (NCI-H460, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~95% of this change | **0.754×** | -3.5 | 0.021 | 22/46 (SNU-423, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.727×** | -3.4 | 0.032 | 21/45 (SNU-1, HS-578T, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **0.766×** | -3.3 | 0.037 | 20/46 (NCI-H1792, A-172, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.774×** | -3.2 | 0.053 | 19/46 (SW 900, SNU-1, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.778×** | -3.1 | 0.058 | 17/46 (SW480, HEC-1-A, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10202. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 21.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -16.4) |
| [[HEC-1-A (line)]] | alt | 40.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +11.4) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 34.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -13.3) |
| [[HS-578T (line)]] | alt | 50.8 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +9.1) ⚠ toxic; transcription drop | [[Verteporfin (drug)]] 5 µM 0.339× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 67.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.182× (z -13.0) |
| [[J82 (line)]] | alt | 45.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -14.2) |
| [[NCI-H2030 (line)]] | alt | 38.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -15.8) |
| [[NCI-H2347 (line)]] | alt | 43.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -11.9) |
| [[NCI-H460 (line)]] | wt | 24.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -13.9) |
| [[A-172 (line)]] | wt | 53.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.280× (z -10.9) |
| [[LoVo (line)]] | wt | 17.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.82× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 22.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -9.4) |
| [[LS 180 (line)]] | wt | 21.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -16.0) |
| [[RPMI-7951 (line)]] | alt | 75.2 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.290× (z -9.4) |
| [[SNU-1 (line)]] | wt | 77.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -10.8) |
| [[SNU-423 (line)]] | alt | 28.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -18.1) |
| [[A-427 (line)]] | wt | 33.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -16.2) |
| [[A549 (line)]] | wt | 16.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -10.6) |
| [[AsPC-1 (line)]] | alt | 13.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -10.0) |
| [[CHP-212 (line)]] | wt | 29.1 | 0 | 1 | — | [[Almonertinib (hydrochloride) (drug)]] 0.5 µM 0.100× (z -8.5) |
| [[H4 (line)]] | wt | 25.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.167× (z -8.5) |
| [[Hs 766T (line)]] | wt | 29.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -11.4) |
| [[NCI-H1792 (line)]] | alt | 28.6 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.245× (z -9.2) |
| [[NCI-H661 (line)]] | alt | 40.6 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.05 µM 0.0751× (z -9.6) |
| [[SHP-77 (line)]] | alt | 14.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -11.5) |
| [[SW 900 (line)]] | alt | 22.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -11.7) |
| [[A498 (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.61 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.65 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 26.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10202), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKCSH]] | +0.74 | +0.77 / +0.70 | both halves | 7e-06 | pathway: Post-translational protein phosphorylation |
| [[ATP6AP1]] | +0.66 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[TLE5]] | +0.64 | +0.58 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[LENG8]] | +0.64 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[SELENON]] | +0.64 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[PSAP]] | +0.64 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[PNPLA6]] | +0.63 | +0.52 / +0.68 | both halves | 1e-05 | **novel candidate** |
| [[GAA]] | +0.63 | +0.63 / +0.53 | both halves | 1e-05 | **novel candidate** |
| [[GANAB]] | +0.61 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[LAMP1]] | +0.61 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[PLBD2]] | +0.61 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[OS9]] | +0.61 | +0.56 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO45]] | -0.53 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[CCDC137]] | -0.50 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[MRPL36]] | -0.49 | -0.40 / -0.53 | both halves | 4e-05 |  |
| [[NIFK]] | -0.49 | -0.42 / -0.50 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYL9]] | B | MYL9 activity raises LAMB2's level | lines that do not express MYL9 (22) vs lines expressing it (28) | 1.68× lower at baseline in the lines without MYL9 | 0.004 | ⚠ within organs, on part of the lines; also absent: CCBE1, EFEMP1, SEC14L4 |
| [[COL3A1]] | B | COL3A1 activity raises LAMB2's level | lines that do not express COL3A1 (35) vs lines expressing it (15) | 1.64× lower at baseline in the lines without COL3A1 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, PDGFRB, ZNF677 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.685). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-19.5, -21.8); signed map (-25.6, -36.5). **Vector** length 102, 26.1% of its response variance represented; |z| ≥ 3 in 952 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +5.9 | +5.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +5.5 | -1.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +5.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +8.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +3.3 | +3.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +2.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.8 | +2.3 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.8 | +1.2 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.6 | +3.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -6.6 | -7.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.6 | -10.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.6 | -11.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.3 | -4.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.8 | -6.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.4 | -3.4 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -2.2 | -1.1 |
|  | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | -2.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | laminin subunit beta 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:49,121,114-49,133,118 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NPHS5; previously LAMS |
| Gene groups (HGNC) | Laminin subunits |
| Reactome | 20 pathways, smallest: Attachment of bacteria to epithelial cells; Biofilm formation; Developmental Lineage of Pancreatic Ductal Cells |
| Matched by | ensembl_id |

**Function**, from UniProt [P55268](https://www.uniprot.org/uniprotkb/P55268) (Laminin subunit beta-2):

> Binding to cells via a high affinity receptor, laminin is thought to mediate the attachment, migration and organization of cells into tissues during embryonic development by interacting with other extracellular matrix components.

**Summary**, from NCBI Gene [3913](https://www.ncbi.nlm.nih.gov/gene/3913):

> Laminins, a family of extracellular matrix glycoproteins, are the major noncollagenous constituent of basement membranes. They have been implicated in a wide variety of biological processes including cell adhesion, differentiation, migration, signaling, neurite outgrowth and metastasis. Laminins, composed of 3 non identical chains: laminin alpha, beta and gamma (formerly A, B1, and B2, respectively), form a cruciform structure consisting of 3 short arms, each formed by a different chain, and a …

**Accessions** — [HGNC:6487](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6487) · Entrez [3913](https://www.ncbi.nlm.nih.gov/gene/3913) · UniProt [P55268](https://www.uniprot.org/uniprotkb/P55268) · Ensembl [ENSG00000172037](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172037)

## Data

Gene col 10202: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10202); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10202, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10202]; `tensor/DDL_lfc|DDL_z.npy` [10202]; `embed/gene_vectors.npy` [10202]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10202 or target_col == 10202). Every well: [[LAMB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LAMB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
