---
symbol: "MYOCOS"
type: "gene"
col: 16036
ensembl_id: "ENSG00000283683"
name: "myocilin opposite strand"
location: "1q24.3"
module: 39
arm: "+"
pooled_cpm: 6.02
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 15
n_dd_up_clean: 15
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# MYOCOS

*myocilin opposite strand* — 1q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.84× (z +16.9, q 0e+00, up in 39 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[HI-TOPK-032 (drug)]] 0.05 µM: 0.487× (z -5.1, q 2e-04, down in 22 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP50]] (+0.89, fdr 7e-06), [[FNDC7]] (+0.89, fdr 7e-06), [[SLC6A13]] (+0.88, fdr 7e-06).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16036.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.84×** | +16.9 | 0e+00 | 39/40 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.87×** | +14.5 | 3e-45 | 38/40 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.54×** | +9.6 | 2e-19 | 29/39 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.24×** | +8.7 | 7e-16 | 31/46 (HOP62, A498, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **2.14×** | +5.8 | 8e-07 | 30/47 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **2.00×** | +5.3 | 1e-05 | 19/43 (SW480, A-172, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.92×** | +4.7 | 3e-04 | 20/44 (A-172, A498, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +4.1 | 0.003 | 17/36 (MIA PaCa-2, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.79×** | +4.1 | 0.003 | 14/41 (NCI-H460, Hs 766T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.73×** | +4.0 | 0.003 | 17/44 (NCI-H1792, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +4.0 | 0.004 | 17/39 (BT-474, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.62×** | +3.7 | 0.011 | 16/44 (NCI-H1792, SW1417, …) | two highest doses | position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **2.47×** | +3.6 | 0.015 | 10/36 (NCI-H2347, SW480, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.62×** | +3.5 | 0.021 | 13/42 (HT-29, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.61×** | +3.3 | 0.032 | 2/18 (NCI-H2347, NCI-H460) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Pyridoxine (drug)]] 0.05 µM |  | **1.48×** | +3.0 | 0.089 | 8/44 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16036.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.487×** | -5.1 | 2e-04 | 22/44 (HEC-1-A, RKO, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.536×** | -4.7 | 7e-04 | 23/44 (A-427, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.544×** | -4.6 | 8e-04 | 19/46 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[NG25 (drug)]] 5 µM |  | **0.383×** | -3.8 | 0.021 | 10/35 (NCI-H1792, RKO, …) | top dose only | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Bexarotene (drug)]] 5 µM |  | **0.617×** | -3.7 | 0.029 | 15/46 (hTERT-HPNE, LOX-IMVI, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.627×** | -3.5 | 0.035 | 17/45 (COLO 205, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.628×** | -3.5 | 0.035 | 18/45 (NCI-H1573, A-427, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.631×** | -3.5 | 0.036 | 10/45 (BT-474, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.634×** | -3.3 | 0.054 | 12/45 (SNU-1, NCI-H2347, …) | top dose only | plate-row cell shift; position effect removed |
| [[Infigratinib (drug)]] 0.05 µM |  | **0.629×** | -3.3 | 0.054 | 12/43 (NCI-H1573, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.652×** | -3.2 | 0.059 | 10/46 (HT-29, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[LB-100 (drug)]] 0.05 µM |  | **0.636×** | -3.2 | 0.059 | 4/46 (NCI-H1573, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.743×** | -3.2 | 0.066 | 11/47 (NCI-H1573, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **0.652×** | -3.1 | 0.077 | 18/43 (NCI-H1573, J82, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.670×** | -3.0 | 0.095 | 17/37 (NCI-H1573, NCI-H2030, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16036. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 19.8 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0263× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0640× (z -11.9) |
| [[HOP62 (line)]] | alt | 4.47 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.90× (z +8.9) | [[Clobetasol propionate (drug)]] 0.05 µM 0.0575× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 7.96 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.90× (z +13.0) | — |
| [[SW 900 (line)]] | alt | 20.2 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0934× (z -10.1) ⚠ transcription drop; cell-cycle shift, explains ~62% of this change |
| [[AsPC-1 (line)]] | alt | 3.12 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.5× (z +9.0) | — |
| [[BT-474 (line)]] | alt | 10.5 | 0 | 1 | — | [[Flumatinib (mesylate) (drug)]] 5 µM 0.0687× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 4.55 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.03× (z +8.8) | — |
| [[HCT15 (line)]] | alt | 3.89 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.5× (z +9.0) | — |
| [[Hs 766T (line)]] | wt | 5.47 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.83× (z +9.8) | — |
| [[HS-578T (line)]] | alt | 3.76 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +8.8) | — |
| [[LoVo (line)]] | wt | 7.17 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.3× (z +14.5) | — |
| [[LOX-IMVI (line)]] | wt | 8.34 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.06× (z +9.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 3.51 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.2× (z +10.2) | — |
| [[NCI-H1792 (line)]] | alt | 12.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.05× (z +11.4) | — |
| [[NCI-H2030 (line)]] | alt | 10.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0623× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 7.46 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.75× (z +10.2) | — |
| [[Panc 03.27 (line)]] | alt | 3.50 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.18× (z +8.6) | — |
| [[PANC-1 (line)]] | alt | 2.21 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.01× (z +9.4) | — |
| [[SW480 (line)]] | alt | 2.80 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.00× (z +8.5) | — |
| [[A-172 (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.63 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.17 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.79 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.09 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.78 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16036), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP50]] | +0.89 | +0.89 / +0.82 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.89 | +0.90 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[SLC6A13]] | +0.88 | +0.88 / +0.80 | both halves | 7e-06 |  |
| [[ARL9]] | +0.88 | +0.89 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[GARIN1A]] | +0.88 | +0.87 / +0.81 | both halves | 7e-06 |  |
| [[IDI2-AS1]] | +0.88 | +0.90 / +0.76 | both halves | 7e-06 |  |
| [[CDKL4]] | +0.87 | +0.88 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[HCLS1]] | +0.87 | +0.85 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[OIT3]] | +0.87 | +0.86 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[ALDH8A1]] | +0.86 | +0.87 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[PILRA]] | +0.85 | +0.85 / +0.77 | both halves | 7e-06 |  |
| [[EPHX3]] | +0.85 | +0.86 / +0.78 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MYOCOS's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC01291]] | B | LINC01291 activity raises MYOCOS's level | lines that do not express LINC01291 (10) vs lines expressing it (40) | 1.66× lower at baseline in the lines without LINC01291 | 0.059 | ⚠ within organs, on part of the lines; also absent: ANTXR2, ENSG00000230479, PROCR; maybe low, not absent |
| [[AOX1]] | B | AOX1 activity raises MYOCOS's level | lines that do not express AOX1 (17) vs lines expressing it (33) | 1.64× lower at baseline in the lines without AOX1 | 0.067 | ⚠ within organs, on part of the lines; also absent: KCNG1, TTC28, ARHGEF6; maybe low, not absent |
| [[DYSF]] | B | DYSF activity raises MYOCOS's level | lines that do not express DYSF (11) vs lines expressing it (39) | 1.69× lower at baseline in the lines without DYSF | 0.072 | ⚠ within organs, on part of the lines; also absent: ISM2, IRX3, DNAAF9; maybe low, not absent |
| [[SMCO2]] | B | SMCO2 activity raises MYOCOS's level | lines that do not express SMCO2 (9) vs lines expressing it (41) | 1.33× lower at baseline in the lines without SMCO2 | 0.074 | ⚠ within organs, on part of the lines; also absent: BMAL2, MIR31HG, ITGA2; maybe low, not absent |
| [[LYG1]] | B | LYG1 activity raises MYOCOS's level | lines that do not express LYG1 (5) vs lines expressing it (45) | 1.73× lower at baseline in the lines without LYG1 | 0.098 | ⚠ within organs, on part of the lines; also absent: LINC02133, RBM44, DIRC3-AS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.945). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.2, -14.7); signed map (16.9, 9.3). **Vector** length 107, 24.7% of its response variance represented; |z| ≥ 3 in 1,277 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.8 | +14.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.2 | +16.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.7 | +9.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +5.9 | +4.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.9 | +5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.6 | +8.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +5.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.2 | +3.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -4.7 | -3.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | -2.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.2 | -3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.1 | -1.8 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -4.1 | -5.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.7 | -1.2 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -3.2 | -3.3 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.8 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | myocilin opposite strand |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q24.3 — chr1:171,600,621-171,638,799 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [A0A1B0GUC4](https://www.uniprot.org/uniprotkb/A0A1B0GUC4) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53429](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53429) · Entrez [110806290](https://www.ncbi.nlm.nih.gov/gene/110806290) · UniProt [A0A1B0GUC4](https://www.uniprot.org/uniprotkb/A0A1B0GUC4) · Ensembl [ENSG00000283683](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000283683)

## Data

Gene col 16036: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16036); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16036, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16036]; `tensor/DDL_lfc|DDL_z.npy` [16036]; `embed/gene_vectors.npy` [16036]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16036 or target_col == 16036). Every well: [[MYOCOS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYOCOS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
