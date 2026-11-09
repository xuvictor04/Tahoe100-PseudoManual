---
symbol: "PRMT9"
type: "gene"
col: 8890
ensembl_id: "ENSG00000164169"
name: "protein arginine methyltransferase 9"
location: "4q31.23"
module: 65
arm: "+"
pooled_cpm: 28.02
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 13
n_dd_up_clean: 5
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# PRMT9

*protein arginine methyltransferase 9* — 4q31.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.25× (z +5.4, q 3e-05, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.330× (z -14.2, q 6e-43, down in 43 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.650× (z -7.8, q 1e-12, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALG9]] (+0.77, fdr 7e-06), [[COPS4]] (+0.71, fdr 7e-06), [[METTL14]] (+0.71, fdr 7e-06); moves opposite to [[RBM19]] (-0.65, fdr 9e-06), [[NPIPB4]] (-0.64, fdr 1e-05), [[DGKH]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8890.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.25×** | +5.4 | 3e-05 | 31/48 (SW480, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.94×** | +4.4 | 0.003 | 25/48 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.35×** | +3.9 | 0.021 | 21/48 (J82, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.34×** | +3.7 | 0.029 | 23/48 (A-172, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.33×** | +3.6 | 0.034 | 21/48 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +3.5 | 0.045 | 17/44 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | 1.59× | +3.1 | 0.15 | 11/48 (SHP-77, HepG2/C3A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8890.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.330×** | -14.2 | 6e-43 | 43/43 (NCI-H2347, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.378×** | -12.0 | 1e-30 | 37/41 (NCI-H2347, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.650×** | -7.8 | 1e-12 | 34/48 (NCI-H2347, HOP62, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.613×** | -5.8 | 1e-06 | 24/42 (NCI-H2347, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.655×** | -5.4 | 7e-06 | 30/48 (C32, SHP-77, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.761×** | -3.5 | 0.045 | 16/47 (SHP-77, A549, …) | two highest doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.827×** | -3.4 | 0.047 | 19/48 (H4, NCI-H23, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.763×** | -3.3 | 0.056 | 13/48 (NCI-H2347, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.832×** | -3.3 | 0.056 | 22/48 (NCI-H2347, SW1417, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 0.839× | -3.2 | 0.082 | 10/48 (Hs 766T, A498, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.784×** | -3.1 | 0.088 | 11/48 (AsPC-1, SW 1088, …) | inconsistent across doses |  |
| [[Mifepristone (drug)]] 0.5 µM |  | **0.785×** | -3.1 | 0.088 | 15/48 (LS 180, SNU-423, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.786×** | -3.1 | 0.088 | 14/48 (A498, NCI-H1573, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.788×** | -3.1 | 0.092 | 13/48 (A498, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8890. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 61.6 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.100× (z -21.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -16.2) |
| [[A-427 (line)]] | wt | 44.1 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.146× (z -14.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 17.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -11.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 37.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.271× (z -9.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 16.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0806× (z -14.0) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 48.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0780× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Temsirolimus (drug)]] 0.5 µM 0.0872× (z -9.3) |
| [[HOP62 (line)]] | alt | 25.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -10.6) |
| [[Hs 766T (line)]] | wt | 23.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -8.9) |
| [[LoVo (line)]] | wt | 25.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 41.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.229× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 21.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +12.1) ⚠ cell-cycle shift, explains ~0% of this change | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.103× (z -9.2) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 19.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.212× (z -12.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 40.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.188× (z -12.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 39.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.228× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -9.2) |
| [[SW1417 (line)]] | alt | 27.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.105× (z -14.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 42.0 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0921× (z -8.5) |
| [[C-33 A (line)]] | alt | 58.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -9.3) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 24.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.155× (z -10.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 34.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -9.7) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 44.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -9.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 18.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.263× (z -9.0) ⚠ transcription drop; cell-cycle shift, explains ~74% of this change |
| [[KATO III (line)]] | alt | 15.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0849× (z -14.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 38.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.247× (z -9.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 33.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -12.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 19.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -8.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 25.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.364× (z -8.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8890), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALG9]] | +0.77 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[COPS4]] | +0.71 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[METTL14]] | +0.71 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[PRPF39]] | +0.70 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[ABHD10]] | +0.70 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[TADA1]] | +0.70 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[REPS1]] | +0.69 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[DUSP11]] | +0.69 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[EID2B]] | +0.69 | +0.57 / +0.73 | both halves | 1e-05 |  |
| [[LRIG2]] | +0.69 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[NDUFV2]] | +0.68 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[ZNF14]] | +0.67 | +0.62 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM19]] | -0.65 | -0.65 / -0.57 | both halves | 9e-06 |  |
| [[NPIPB4]] | -0.64 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[DGKH]] | -0.64 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[ABR]] | -0.59 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[DDX5]] | -0.58 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[SUSD1]] | -0.57 | -0.53 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers PRMT9's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity raises PRMT9's level | compounds that target TOP2A: 3 of 5 lower it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.829). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-2.9, -10.1); signed map (-30.4, -10.8). **Vector** length 101, 24.7% of its response variance represented; |z| ≥ 3 in 875 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.2 | +3.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +1.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +2.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.3 | +2.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.1 | +0.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +3.1 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.3 | -2.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -7.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.0 | -5.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | -2.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -4.3 | -3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -2.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.4 | -2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | protein arginine methyltransferase 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.23 — chr4:147,637,785-147,684,163 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ46629; previously PRMT10 |
| Gene groups (HGNC) | 7BS protein arginine methyltranferases; Arginine methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P2P2](https://www.uniprot.org/uniprotkb/Q6P2P2) (Protein arginine N-methyltransferase 9):

> Arginine methyltransferase that can both catalyze the formation of omega-N monomethylarginine (MMA) and symmetrical dimethylarginine (sDMA). Specifically mediates the symmetrical dimethylation of SF3B2. Involved in the regulation of alternative splicing of pre-mRNA.

**Summary**, from NCBI Gene [90826](https://www.ncbi.nlm.nih.gov/gene/90826):

> This gene encodes a type II methyltransferase. Post-translational modification of target proteins by PRMTs plays an important regulatory role in many biological processes, whereby PRMTs methylate arginine residues by transferring methyl groups from S-adenosyl-L-methionine to the guanidino nitrogen atoms of arginine. The protein encoded by this gene methylates spliceosome associated protein 145 to regulate alternative splicing and acts as a modulator of small nuclear ribonucleoprotein …

**Accessions** — [HGNC:25099](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25099) · Entrez [90826](https://www.ncbi.nlm.nih.gov/gene/90826) · UniProt [Q6P2P2](https://www.uniprot.org/uniprotkb/Q6P2P2) · Ensembl [ENSG00000164169](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164169)

## Data

Gene col 8890: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8890); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8890, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8890]; `tensor/DDL_lfc|DDL_z.npy` [8890]; `embed/gene_vectors.npy` [8890]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8890 or target_col == 8890). Every well: [[PRMT9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRMT9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
