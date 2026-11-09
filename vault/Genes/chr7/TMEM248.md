---
symbol: "TMEM248"
type: "gene"
col: 2782
ensembl_id: "ENSG00000106609"
name: "transmembrane protein 248"
location: "7q11.21"
module: 42
arm: "+"
pooled_cpm: 70.03
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 8
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# TMEM248

*transmembrane protein 248* — 7q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.51× (z +9.8, q 5e-20, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.528× (z -14.7, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELAVL1]] (+0.70, fdr 7e-06), [[NIPA2]] (+0.69, fdr 7e-06), [[PMPCA]] (+0.67, fdr 7e-06); moves opposite to [[NOTCH2NLB]] (-0.62, fdr 7e-06), [[NBPF10]] (-0.62, fdr 7e-06), [[ATF4]] (-0.61, fdr 7e-06).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2782.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.51×** | +9.8 | 5e-20 | 40/48 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.12×** | +9.4 | 2e-18 | 40/49 (KATO III, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.92×** | +8.1 | 1e-13 | 30/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +6.1 | 2e-07 | 32/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.47×** | +4.7 | 2e-04 | 20/38 (NCI-H1573, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.22×** | +4.6 | 3e-04 | 22/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.18× | +4.0 | 0.005 | 16/48 (NCI-H1792, PANC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.9 | 0.006 | 17/48 (SW480, HOP62, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.17× | +3.8 | 0.008 | 20/49 (SNU-423, NCI-H1792, …) | inconsistent across doses | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.8 | 0.008 | 18/48 (SW480, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2782.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.528×** | -14.7 | 0e+00 | 44/48 (PANC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.669×** | -13.6 | 1e-39 | 33/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.669×** | -9.6 | 1e-19 | 36/48 (C-33 A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.697×** | -8.6 | 8e-16 | 33/48 (MIA PaCa-2, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.738×** | -7.3 | 4e-11 | 35/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.810×** | -7.2 | 8e-11 | 29/48 (NCI-H2347, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.776×** | -6.1 | 1e-07 | 29/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.807×** | -5.2 | 2e-05 | 23/48 (C32, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.870× | -4.7 | 1e-04 | 21/49 (AsPC-1, A498, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.855× | -3.8 | 0.010 | 21/48 (KATO III, PANC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.861× | -3.6 | 0.016 | 16/48 (C-33 A, C32, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.963× | -3.3 | 0.054 | 0/50 | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.889× | -3.2 | 0.060 | 11/48 (NCI-H2347, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.915× | -3.0 | 0.10 | 9/48 (A498, J82, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2782. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 88.3 | 6 (3 ⚠) | 2 | [[Digitoxin (drug)]] 5 µM 2.40× (z +13.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.26× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -14.1) |
| [[AsPC-1 (line)]] | alt | 116 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -18.4) |
| [[PANC-1 (line)]] | alt | 85.8 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.552× (z -11.8) |
| [[A498 (line)]] | wt | 123 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.544× (z -13.4) |
| [[C-33 A (line)]] | alt | 95.7 | 0 | 4 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.227× (z -12.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.261× (z -11.5) |
| [[KATO III (line)]] | alt | 97.5 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 3.90× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.449× (z -10.8) |
| [[A-427 (line)]] | wt | 58.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.58× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Harringtonine (drug)]] 5 µM 0.438× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 70.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.558× (z -11.2) |
| [[LS 180 (line)]] | wt | 56.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.379× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 72.2 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.49× (z +10.2) | [[Homoharringtonine (drug)]] 0.5 µM 0.315× (z -12.9) |
| [[NCI-H1573 (line)]] | alt | 54.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -19.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.405× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 80.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 66.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -13.6) |
| [[RKO (line)]] | wt | 56.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.205× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 1088 (line)]] | alt | 81.2 | 0 | 2 | — | [[Fenofibrate (drug)]] 0.5 µM 0.0835× (z -10.1) |
| [[SW1417 (line)]] | alt | 93.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.517× (z -12.0) |
| [[A-172 (line)]] | wt | 60.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.77× (z +11.9) | — |
| [[C32 (line)]] | wt | 80.4 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.359× (z -9.5) |
| [[HOP62 (line)]] | alt | 45.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.392× (z -10.2) |
| [[HS-578T (line)]] | alt | 65.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -11.0) |
| [[HT-29 (line)]] | alt | 62.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.533× (z -9.8) |
| [[Panc 03.27 (line)]] | alt | 62.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.543× (z -9.3) |
| [[SNU-423 (line)]] | alt | 44.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.62× (z +10.0) | — |
| [[SW 900 (line)]] | alt | 72.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.435× (z -8.6) |
| [[A549 (line)]] | wt | 60.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 96.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 68.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 56.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 81.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 48.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 56.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 50.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 65.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 66.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 53.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 75.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 52.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 75.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 65.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 71.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 77.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2782), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELAVL1]] | +0.70 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[NIPA2]] | +0.69 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[PMPCA]] | +0.67 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[TM9SF2]] | +0.67 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[SENP3]] | +0.66 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[RNF4]] | +0.64 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[SNHG30]] | +0.63 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[FBXW2]] | +0.63 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[ADPGK]] | +0.62 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[STX16-NPEPL1]] | +0.62 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[FUBP3]] | +0.62 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[SMPD4]] | +0.62 | +0.67 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOTCH2NLB]] | -0.62 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[NBPF10]] | -0.62 | -0.59 / -0.66 | both halves | 7e-06 |  |
| [[ATF4]] | -0.61 | -0.67 / -0.58 | both halves | 7e-06 |  |
| [[NBPF26]] | -0.59 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[ZC3H6]] | -0.59 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[UPF3B]] | -0.59 | -0.66 / -0.56 | both halves | 1e-05 |  |
| [[DYNLL1]] | -0.58 | -0.64 / -0.54 | both halves | 1e-05 |  |
| [[MARCKS]] | -0.58 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[BTG1]] | -0.58 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[PPP1R15A]] | -0.57 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[KLF6]] | -0.57 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[NBPF19]] | -0.57 | -0.51 / -0.64 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises TMEM248's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.547). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.8, -28.1); signed map (-45.1, -20.5). **Vector** length 106, 26.9% of its response variance represented; |z| ≥ 3 in 972 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.9 | +9.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | +1.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.8 | +9.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +8.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.0 | +1.3 |
|  | [[EX229 (drug)]] 5 µM |  | +1.7 | +2.8 |
|  | [[Gallic acid (drug)]] 0.05 µM |  | +1.6 | +1.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.5 | +1.0 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -10.8 | -14.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.9 | -9.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.6 | -13.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.2 | -8.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.2 | -3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.9 | -7.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.1 | -2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.2 | -2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.1 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 248 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.21 — chr7:66,921,225-66,958,551 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10099, FLJ13090; previously C7orf42 |
| Matched by | ensembl_id |

UniProt [Q9NWD8](https://www.uniprot.org/uniprotkb/Q9NWD8) carries no function annotation.

**Summary**, from NCBI Gene [55069](https://www.ncbi.nlm.nih.gov/gene/55069):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25476](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25476) · Entrez [55069](https://www.ncbi.nlm.nih.gov/gene/55069) · UniProt [Q9NWD8](https://www.uniprot.org/uniprotkb/Q9NWD8) · Ensembl [ENSG00000106609](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106609)

## Data

Gene col 2782: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2782); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2782, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2782]; `tensor/DDL_lfc|DDL_z.npy` [2782]; `embed/gene_vectors.npy` [2782]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2782 or target_col == 2782). Every well: [[TMEM248 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM248.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
