---
symbol: "SLC2A10"
type: "gene"
col: 12406
ensembl_id: "ENSG00000197496"
name: "solute carrier family 2 member 10"
location: "20q13.12"
module: 19
arm: "+"
pooled_cpm: 9.3
n_lines_expressing: 32
n_dd_up: 0
n_dd_down: 49
n_dd_up_clean: 0
n_dd_down_clean: 36
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# SLC2A10

*solute carrier family 2 member 10* — 20q13.12

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 49 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.219× (z -23.9, q 0e+00, down in 27 of 28 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM98A]] (+0.46, fdr 5e-05), [[RBM10]] (+0.45, fdr 6e-05), [[FBLN7]] (+0.44, fdr 1e-04); moves opposite to [[MEIOB]] (-0.44, fdr 1e-04), [[LINC02945]] (-0.43, fdr 3e-04), [[PGBD5]] (-0.41, fdr 5e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TBX18]] → it (grade B ⚠); 2 go from it, the strongest it → [[NFXL1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12406.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | 1.44× | +3.6 | 0.21 | 3/29 (HT-29, SW 1088, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.34× | +3.2 | 0.21 | 6/29 (CFPAC-1, BT-474, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.33× | +3.2 | 0.21 | 7/30 (KATO III, MIA PaCa-2, …) | rises with dose |  |
| [[Larotrectinib (drug)]] 5 µM |  | 1.22× | +3.2 | 0.21 | 4/29 (Hs 766T, HS-578T, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 49 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12406.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.219×** | -23.9 | 0e+00 | 27/28 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.124×** | -23.2 | 0e+00 | 28/30 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.151×** | -21.1 | 0e+00 | 25/25 (HS-578T, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.164×** | -20.0 | 0e+00 | 27/30 (KATO III, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.208×** | -17.3 | 0e+00 | 28/29 (HOP62, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.214×** | -17.2 | 0e+00 | 28/30 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.216×** | -17.0 | 0e+00 | 28/30 (HCT15, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.267×** | -14.6 | 0e+00 | 25/28 (KATO III, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.281×** | -14.1 | 2e-43 | 25/29 (KATO III, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.311×** | -12.9 | 3e-36 | 25/29 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.325×** | -12.5 | 4e-34 | 24/27 (A498, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.321×** | -12.1 | 3e-32 | 22/28 (RPMI-7951, A498, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.364×** | -10.8 | 2e-25 | 21/24 (KATO III, HCT15, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.508×** | -10.6 | 9e-25 | 22/28 (HOP62, Hs 766T, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.197×** | -9.5 | 1e-19 | 25/30 (KATO III, SW 900, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.408×** | -9.4 | 2e-19 | 22/28 (KATO III, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.512×** | -7.4 | 6e-12 | 20/26 (J82, SNU-423, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.488×** | -6.9 | 2e-10 | 23/30 (hTERT-HPNE, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12406. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 46.7 | 0 | 13 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0943× (z -18.5) |
| [[Hs 766T (line)]] | wt | 22.3 | 0 | 12 (4 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0590× (z -13.9) |
| [[NCI-H1573 (line)]] | alt | 19.2 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0763× (z -21.4) |
| [[CFPAC-1 (line)]] | alt | 20.9 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -16.9) |
| [[SNU-1 (line)]] | wt | 25.4 | 0 | 10 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0449× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0707× (z -10.9) |
| [[BT-474 (line)]] | alt | 47.7 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -18.5) |
| [[RPMI-7951 (line)]] | alt | 18.4 | 0 | 8 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0605× (z -13.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0948× (z -11.3) |
| [[SW 900 (line)]] | alt | 15.3 | 0 | 8 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0618× (z -13.5) |
| [[HOP62 (line)]] | alt | 13.5 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0600× (z -15.1) |
| [[J82 (line)]] | alt | 8.54 | 0 | 7 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0906× (z -11.2) |
| [[A498 (line)]] | wt | 19.4 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -17.5) |
| [[HCT15 (line)]] | alt | 24.8 | 0 | 6 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0531× (z -14.7) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0709× (z -13.7) |
| [[HS-578T (line)]] | alt | 15.5 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0214× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.177× (z -11.4) |
| [[HT-29 (line)]] | alt | 9.37 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0407× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.118× (z -13.7) |
| [[MIA PaCa-2 (line)]] | alt | 8.53 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0567× (z -11.6) |
| [[Panc 03.27 (line)]] | alt | 13.9 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.155× (z -12.4) |
| [[A-172 (line)]] | wt | 16.8 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -13.1) |
| [[HepG2_C3A (line)]] | wt | 23.4 | 0 | 5 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0671× (z -11.9) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0858× (z -11.2) |
| [[RKO (line)]] | wt | 14.5 | 0 | 5 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.101× (z -10.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.160× (z -9.1) |
| [[SW480 (line)]] | alt | 5.39 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.100× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.114× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 6.62 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0261× (z -14.0) |
| [[SNU-423 (line)]] | alt | 8.26 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0292× (z -13.8) |
| [[hTERT-HPNE (line)]] | wt | 6.08 | 0 | 2 | — | [[Panobinostat (drug)]] 0.05 µM 0.0328× (z -9.7) |
| [[SK-MEL-2 (line)]] | alt | 11.3 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.108× (z -9.5) |
| [[A-427 (line)]] | wt | 0.543 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.591 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.880 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.894 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.721 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.28 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.756 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.718 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.888 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.60 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.877 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.599 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.997 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.662 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 7.72 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12406), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM98A]] | +0.46 | +0.40 / +0.57 | both halves | 5e-05 |  |
| [[RBM10]] | +0.45 | +0.38 / +0.46 | both halves | 6e-05 |  |
| [[FBLN7]] | +0.44 | +0.43 / +0.34 | both halves | 1e-04 |  |
| [[CADPS2]] | +0.42 | +0.29 / +0.45 | both halves | 3e-04 |  |
| [[GABRR2]] | +0.41 | +0.31 / +0.42 | both halves | 2e-04 |  |
| [[ZNF417]] | +0.40 | +0.23 / +0.55 | both halves | 5e-04 |  |
| [[RAD1]] | +0.40 | +0.36 / +0.33 | both halves | 1e-04 |  |
| [[METTL21EP-1]] | +0.39 | +0.31 / +0.36 | both halves | 2e-04 |  |
| [[LY6E-DT]] | +0.39 | +0.41 / +0.41 | both halves | 4e-05 |  |
| [[GPR173]] | +0.39 | +0.39 / +0.42 | both halves | 5e-05 |  |
| [[ATM]] | +0.39 | +0.37 / +0.38 | both halves | 8e-05 |  |
| [[PDXDC2P]] | +0.39 | +0.38 / +0.47 | both halves | 6e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MEIOB]] | -0.44 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[LINC02945]] | -0.43 | -0.28 / -0.32 | both halves | 3e-04 |  |
| [[PGBD5]] | -0.41 | -0.34 / -0.24 | both halves | 5e-04 |  |
| [[FAM110B]] | -0.41 | -0.36 / -0.27 | both halves | 3e-04 |  |
| [[FMNL2]] | -0.41 | -0.20 / -0.56 | both halves | 7e-04 |  |
| [[PDE1A]] | -0.40 | -0.38 / -0.29 | both halves | 2e-04 |  |
| [[MAP7]] | -0.39 | -0.39 / -0.32 | both halves | 2e-04 |  |
| [[MTM1]] | -0.39 | -0.30 / -0.30 | both halves | 2e-04 |  |
| [[CPS1]] | -0.38 | -0.33 / -0.29 | both halves | 2e-04 |  |
| [[CLSTN2]] | -0.38 | -0.46 / -0.30 | both halves | 2e-04 |  |
| [[ARHGEF18]] | -0.38 | -0.33 / -0.26 | both halves | 3e-04 |  |
| [[LINC02864]] | -0.37 | -0.39 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TBX18]] | B | TBX18 activity lowers SLC2A10's level | lines that do not express TBX18 (27) vs lines expressing it (23) | 2.65× higher at baseline in the lines without TBX18 | 0.036 | ⚠ within organs, on part of the lines; also absent: SFRP1, LRRK2, ENSG00000286251 |
| [[TOP2A]] | B | TOP2A activity raises SLC2A10's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.7% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC02864]] | B | LINC02864 activity lowers SLC2A10's level | lines that do not express LINC02864 (36) vs lines expressing it (14) | 2.89× higher at baseline in the lines without LINC02864 | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, LINC00824, LINC01205 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NFXL1]] | B | SLC2A10 activity raises NFXL1's level | lines that do not express SLC2A10 (18) vs lines expressing it (32) | 1.22× lower at baseline in the lines without SLC2A10 | 0.009 | ⚠ within organs, on part of the lines; also absent: SARDH, CSF1 |
| [[TBX18]] | B | SLC2A10 activity lowers TBX18's level | lines that do not express SLC2A10 (18) vs lines expressing it (32) | 2.95× higher at baseline in the lines without SLC2A10 | 0.069 | ⚠ within organs, on part of the lines; also absent: SARDH, CSF1 |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction -0.292). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.2, 35.6); signed map (4.3, 6.8). **Vector** length 66.9, 14.5% of its response variance represented; |z| ≥ 3 in 926 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +1.8 | -12.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +1.8 | +1.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | +1.7 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.5 | +1.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +1.2 | -6.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.2 | -0.7 |
|  | [[(S)-Crizotinib (drug)]] 5 µM |  | +1.1 | +2.2 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | +1.0 | +0.1 |
|  | [[Larotrectinib (drug)]] 5 µM |  | +1.0 | +3.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.6 | -10.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -1.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -1.8 | -2.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -0.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.7 | -0.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | -5.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.5 | -3.4 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.3 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 2 member 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:46,709,649-46,736,347 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GLUT10, GLUT-10 |
| Gene groups (HGNC) | Solute carrier family 2 |
| Reactome | 5 pathways, smallest: Cellular hexose transport; SLC transporter disorders; Disorders of transmembrane transporters |
| Matched by | ensembl_id |

**Function**, from UniProt [O95528](https://www.uniprot.org/uniprotkb/O95528) (Solute carrier family 2, facilitated glucose transporter member 10):

> Facilitative glucose transporter required for the development of the cardiovascular system.

**Summary**, from NCBI Gene [81031](https://www.ncbi.nlm.nih.gov/gene/81031):

> This gene encodes a member of the class III facilitative glucose transporter family. The encoded protein plays a role in regulation of glucose homeostasis. Mutations in this gene have been associated with arterial tortuosity syndrome.[provided by RefSeq, Dec 2009]

**Accessions** — [HGNC:13444](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13444) · Entrez [81031](https://www.ncbi.nlm.nih.gov/gene/81031) · UniProt [O95528](https://www.uniprot.org/uniprotkb/O95528) · Ensembl [ENSG00000197496](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197496)

## Data

Gene col 12406: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12406); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12406, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12406]; `tensor/DDL_lfc|DDL_z.npy` [12406]; `embed/gene_vectors.npy` [12406]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12406 or target_col == 12406). Every well: [[SLC2A10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC2A10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
