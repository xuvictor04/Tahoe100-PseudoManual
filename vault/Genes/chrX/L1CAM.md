---
symbol: "L1CAM"
type: "gene"
col: 12731
ensembl_id: "ENSG00000198910"
name: "L1 cell adhesion molecule"
location: "Xq28"
module: 2
arm: "+"
pooled_cpm: 46.53
n_lines_expressing: 28
n_dd_up: 10
n_dd_down: 34
n_dd_up_clean: 6
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 8
direction_downstream: 13
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# L1CAM

*L1 cell adhesion molecule* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.06× (z +9.6, q 4e-19, up in 20 of 25 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 1.78× (z +7.7, q 3e-12, up in 10 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.306× (z -22.3, q 0e+00, down in 24 of 26 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CERCAM]] (+0.65, fdr 1e-05), [[CD151]] (+0.63, fdr 1e-05), [[RHOA]] (+0.61, fdr 2e-05); moves opposite to [[ATXN7L1]] (-0.49, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[CYS1]] → it (grade B ⚠); 13 go from it, the strongest it → [[YWHAQ]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12731.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.06×** | +9.6 | 4e-19 | 20/25 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.01×** | +9.0 | 8e-17 | 14/20 (J82, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.78×** | +7.7 | 3e-12 | 10/26 (KATO III, SNU-423, …) | two highest doses | cell-cycle shift (explains ~12% here); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.77×** | +7.3 | 4e-11 | 17/24 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.66×** | +6.8 | 1e-09 | 15/25 (NCI-H460, SW480, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +6.6 | 3e-09 | 14/26 (KATO III, SNU-423, …) | two highest doses | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.64×** | +6.1 | 9e-08 | 11/23 (SW1417, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.40×** | +4.5 | 5e-04 | 14/25 (NCI-H460, SW480, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.24×** | +4.1 | 0.003 | 11/26 (A498, SW480, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.28×** | +3.3 | 0.055 | 13/25 (SW480, KATO III, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12731.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.306×** | -22.3 | 0e+00 | 24/26 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.176×** | -22.2 | 0e+00 | 24/26 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.356×** | -13.7 | 1e-40 | 23/26 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.417×** | -11.6 | 4e-29 | 23/25 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.421×** | -11.5 | 2e-28 | 21/26 (HOP62, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.496×** | -9.3 | 1e-18 | 21/26 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.504×** | -9.1 | 6e-18 | 22/26 (PANC-1, SW1417, …) | two highest doses | cell-cycle shift (explains ~8% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.662×** | -7.7 | 7e-13 | 19/26 (SK-MEL-2, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.571×** | -7.4 | 7e-12 | 21/26 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.701×** | -6.7 | 2e-09 | 20/26 (MIA PaCa-2, SW480, …) | two highest doses | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.609×** | -6.6 | 2e-09 | 20/26 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.611×** | -6.5 | 3e-09 | 18/26 (HOP62, NCI-H23, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.635×** | -5.8 | 3e-07 | 19/25 (PANC-1, SK-MEL-2, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.696×** | -4.8 | 6e-05 | 14/26 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.709×** | -4.6 | 2e-04 | 9/24 (A549, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.712×** | -4.5 | 2e-04 | 14/26 (SK-MEL-2, MIA PaCa-2, …) | two highest doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.724×** | -4.3 | 5e-04 | 10/26 (HS-578T, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Amsacrine (drug)]] 5 µM |  | **0.800×** | -4.2 | 8e-04 | 14/26 (PANC-1, J82, …) | rises with dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.737×** | -4.1 | 0.001 | 10/26 (C32, SNU-423, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.44 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12731. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 188 | 1 (1 ⚠) | 12 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.0808× (z -36.5) |
| [[A-172 (line)]] | wt | 277 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0706× (z -44.0) |
| [[NCI-H460 (line)]] | wt | 45.0 | 8 (1 ⚠) | 3 | [[Pitavastatin (Calcium) (drug)]] 5 µM 4.65× (z +11.6) | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -13.5) |
| [[HOP62 (line)]] | alt | 156 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0709× (z -35.1) |
| [[J82 (line)]] | alt | 196 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 3.10× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -29.7) |
| [[A-427 (line)]] | wt | 29.0 | 0 | 5 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0792× (z -16.1) |
| [[A549 (line)]] | wt | 20.5 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -16.3) |
| [[HS-578T (line)]] | alt | 45.8 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -12.9) |
| [[MIA PaCa-2 (line)]] | alt | 34.9 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0841× (z -21.9) |
| [[C32 (line)]] | wt | 31.2 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.0896× (z -14.1) |
| [[H4 (line)]] | wt | 43.7 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.0394× (z -16.7) |
| [[SW1417 (line)]] | alt | 85.1 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -13.4) |
| [[CHP-212 (line)]] | wt | 80.3 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.110× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Saquinavir (drug)]] 0.05 µM 0.180× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 47.9 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.0540× (z -21.4) |
| [[RPMI-7951 (line)]] | alt | 74.0 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.122× (z -15.5) |
| [[SK-MEL-2 (line)]] | alt | 45.9 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.276× (z -11.9) |
| [[SNU-423 (line)]] | alt | 33.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -15.2) |
| [[SW 1088 (line)]] | alt | 155 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -11.9) |
| [[SW480 (line)]] | alt | 38.6 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.127× (z -18.4) |
| [[KATO III (line)]] | alt | 14.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0858× (z -16.9) |
| [[Panc 03.27 (line)]] | alt | 33.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -18.5) |
| [[A498 (line)]] | wt | 26.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -11.0) |
| [[AN3 CA (line)]] | alt | 6.11 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.53 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.26 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.15 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.60 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.48 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.96 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.92 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.97 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 9.34 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.54 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.24 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.90 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.23 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.31 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.42 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.15 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 7.86 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12731), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CERCAM]] | +0.65 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[CD151]] | +0.63 | +0.54 / +0.58 | both halves | 1e-05 | same gene group; STRING 630 |
| [[RHOA]] | +0.61 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[FGFRL1]] | +0.61 | +0.40 / +0.61 | both halves | 5e-05 | same gene group |
| [[STX2]] | +0.57 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[TNNT1]] | +0.57 | +0.59 / +0.37 | both halves | 8e-05 |  |
| [[DKK3]] | +0.56 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[SEPTIN5]] | +0.55 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[IDS]] | +0.55 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[GNAI2]] | +0.55 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[COL18A1]] | +0.55 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[SUN1]] | +0.54 | +0.41 / +0.54 | both halves | 4e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATXN7L1]] | -0.49 | -0.49 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYS1]] | B | CYS1 activity raises L1CAM's level | lines that do not express CYS1 (22) vs lines expressing it (28) | 2.46× lower at baseline in the lines without CYS1 | 0.013 | ⚠ within organs, on part of the lines; also absent: MT1A, FMNL1-DT, SEC14L4 |
| [[TOP2A]] | B | TOP2A activity raises L1CAM's level | compounds that target TOP2A: 4 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SPEG]] | B | SPEG activity raises L1CAM's level | lines that do not express SPEG (16) vs lines expressing it (34) | 3.08× lower at baseline in the lines without SPEG | 0.053 | ⚠ within organs, on part of the lines; also absent: APBA2, FBXO17, GJC1 |
| [[GNAZ]] | B | GNAZ activity raises L1CAM's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 3.12× lower at baseline in the lines without GNAZ | 0.059 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[RIMS3]] | B | RIMS3 activity raises L1CAM's level | lines that do not express RIMS3 (9) vs lines expressing it (41) | 2.98× lower at baseline in the lines without RIMS3 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: STOX1, ZFP69B, LINC02456; maybe low, not absent |
| [[MEGF6]] | B | MEGF6 activity raises L1CAM's level | lines that do not express MEGF6 (11) vs lines expressing it (39) | 1.67× lower at baseline in the lines without MEGF6 | 0.083 | ⚠ within organs, on part of the lines; also absent: SQOR; maybe low, not absent |
| [[COL18A1]] | B | COL18A1 activity raises L1CAM's level | lines that do not express COL18A1 (18) vs lines expressing it (32) | 2.56× lower at baseline in the lines without COL18A1 | 0.092 | ⚠ within organs, on part of the lines; also absent: NGFR, CX3CL1, PPP2R2B |
| [[PDZD4]] | C | PDZD4 activity raises L1CAM's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 5.31× lower at baseline in the lines without PDZD4 | 3e-04 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 12, C 1. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[YWHAQ]] | B | L1CAM activity raises YWHAQ's level | lines that do not express L1CAM (22) vs lines expressing it (28) | 1.39× lower at baseline in the lines without L1CAM | 0.032 | ⚠ within organs, on part of the lines; also absent: ELFN1, PDZD4, ARHGAP28 |
| [[CYS1]] | B | L1CAM activity raises CYS1's level | lines that do not express L1CAM (22) vs lines expressing it (28) | 1.63× lower at baseline in the lines without L1CAM | 0.033 | ⚠ within organs, on part of the lines; also absent: ELFN1, PDZD4, ARHGAP28 |
| [[KIF3C]] | B | L1CAM activity raises KIF3C's level | lines that do not express L1CAM (22) vs lines expressing it (28) | 1.91× lower at baseline in the lines without L1CAM | 0.042 | ⚠ within organs, on part of the lines; also absent: ELFN1, PDZD4, ARHGAP28 |
| [[KREMEN1]] | B | L1CAM activity raises KREMEN1's level | lines that do not express L1CAM (22) vs lines expressing it (28) | 1.21× lower at baseline in the lines without L1CAM | 0.055 | ⚠ within organs, on part of the lines; also absent: ELFN1, PDZD4, ARHGAP28 |
| [[BSG]] | B | L1CAM activity raises BSG's level | lines that do not express L1CAM (22) vs lines expressing it (28) | 1.38× lower at baseline in the lines without L1CAM | 0.058 | ⚠ within organs, on part of the lines; also absent: ELFN1, PDZD4, ARHGAP28 |
| [[CRMP1]] | B | L1CAM activity raises CRMP1's level | lines that do not express L1CAM (22) vs lines expressing it (28) | 2.06× lower at baseline in the lines without L1CAM | 0.070 | ⚠ within organs, on part of the lines; also absent: ELFN1, PDZD4, ARHGAP28 |
| [[COL18A1]] | B | L1CAM activity raises COL18A1's level | lines that do not express L1CAM (22) vs lines expressing it (28) | 2.23× lower at baseline in the lines without L1CAM | 0.074 | ⚠ within organs, on part of the lines; also absent: ELFN1, PDZD4, ARHGAP28 |
| [[THRB]] | B | L1CAM activity lowers THRB's level | lines that do not express L1CAM (22) vs lines expressing it (28) | 2.13× higher at baseline in the lines without L1CAM | 0.075 | ⚠ within organs, on part of the lines; also absent: ELFN1, PDZD4, ARHGAP28 |
| [[DAG1]] | B | L1CAM activity raises DAG1's level | lines that do not express L1CAM (22) vs lines expressing it (28) | 1.16× lower at baseline in the lines without L1CAM | 0.080 | ⚠ within organs, on part of the lines; also absent: ELFN1, PDZD4, ARHGAP28 |
| [[TUBA1A]] | B | L1CAM activity raises TUBA1A's level | lines that do not express L1CAM (22) vs lines expressing it (28) | 2.60× lower at baseline in the lines without L1CAM | 0.080 | ⚠ within organs, on part of the lines; also absent: ELFN1, PDZD4, ARHGAP28 |
| [[ZFP28]] | B | L1CAM activity raises ZFP28's level | lines that do not express L1CAM (22) vs lines expressing it (28) | 2.53× lower at baseline in the lines without L1CAM | 0.093 | ⚠ within organs, on part of the lines; also absent: ELFN1, PDZD4, ARHGAP28 |
| [[AKTIP]] | B | L1CAM activity raises AKTIP's level | lines that do not express L1CAM (22) vs lines expressing it (28) | 1.13× lower at baseline in the lines without L1CAM | 0.0997 | ⚠ within organs, on part of the lines; also absent: ELFN1, PDZD4, ARHGAP28 |

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.545). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (16.7, -3.3); signed map (-12.2, 34.6). **Vector** length 97.0, 28.8% of its response variance represented; |z| ≥ 3 in 860 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.0 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +6.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +3.7 | +7.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.6 | +6.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.7 | +4.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.6 | +4.1 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.1 | +2.4 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.8 | -22.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.8 | -9.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.1 | -7.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.9 | -6.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.8 | -13.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.4 | -4.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.3 | -3.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.1 | -3.7 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.5 | -0.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.5 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | L1 cell adhesion molecule |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:153,861,514-153,886,173 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CD171, NCAM-L1, CAML1; previously HSAS1, SPG1, HSAS, MASA, MIC5 |
| Gene groups (HGNC) | CD molecules; Fibronectin type III domain containing; I-set domain containing; Ig-like cell adhesion molecule family |
| Hallmark sets | HEDGEHOG_SIGNALING |
| Reactome | 9 pathways, smallest: Basigin interactions; Signal transduction by L1; Interaction between L1 and Ankyrins |
| Matched by | ensembl_id |

**Function**, from UniProt [P32004](https://www.uniprot.org/uniprotkb/P32004) (Neural cell adhesion molecule L1):

> Neural cell adhesion molecule involved in the dynamics of cell adhesion and in the generation of transmembrane signals at tyrosine kinase receptors. During brain development, critical in multiple processes, including neuronal migration, axonal growth and fasciculation, and synaptogenesis. In the mature brain, plays a role in the dynamics of neuronal structure and function, including synaptic plasticity.

**Summary**, from NCBI Gene [3897](https://www.ncbi.nlm.nih.gov/gene/3897):

> The protein encoded by this gene is an axonal glycoprotein belonging to the immunoglobulin supergene family. The ectodomain, consisting of several immunoglobulin-like domains and fibronectin-like repeats (type III), is linked via a single transmembrane sequence to a conserved cytoplasmic domain. This cell adhesion molecule plays an important role in nervous system development, including neuronal migration and differentiation. Mutations in the gene cause X-linked neurological syndromes known as …

**Accessions** — [HGNC:6470](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6470) · Entrez [3897](https://www.ncbi.nlm.nih.gov/gene/3897) · UniProt [P32004](https://www.uniprot.org/uniprotkb/P32004) · Ensembl [ENSG00000198910](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198910)

## Data

Gene col 12731: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12731); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12731, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12731]; `tensor/DDL_lfc|DDL_z.npy` [12731]; `embed/gene_vectors.npy` [12731]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12731 or target_col == 12731). Every well: [[L1CAM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/L1CAM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
