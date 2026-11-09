---
symbol: "KCNN1"
type: "gene"
col: 2633
ensembl_id: "ENSG00000105642"
name: "potassium calcium-activated channel subfamily N member 1"
location: "19p13.11"
module: 181
arm: "+"
pooled_cpm: 3.85
n_lines_expressing: 49
n_dd_up: 27
n_dd_down: 2
n_dd_up_clean: 21
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/181"]
generated_by: "tahoemap"
---

# KCNN1

*potassium calcium-activated channel subfamily N member 1* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.73× (z +25.1, q 0e+00, up in 32 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Selinexor (drug)]] 5 µM: 0.623× (z -6.8, q 5e-09, down in 19 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Hydroxyurea (drug)]] 0.05 µM in 1 line (HEC-1-A 0.104×); [[9-ING-41 (drug)]] 0.05 µM in 1 line (SW1417 0.0347×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL11A2]] (+0.73, fdr 7e-06), [[NPHS1]] (+0.71, fdr 7e-06), [[ELAVL3]] (+0.70, fdr 7e-06); moves opposite to [[EEF1E1]] (-0.56, fdr 3e-05), [[ADPGK]] (-0.55, fdr 2e-05), [[RFT1]] (-0.54, fdr 1e-05).
> It is in [[Module 181]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NDUFA4L2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2633.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.73×** | +25.1 | 0e+00 | 32/36 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.81×** | +14.9 | 0e+00 | 29/36 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.62×** | +9.8 | 2e-20 | 21/37 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.55×** | +9.2 | 8e-18 | 1/2 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.38×** | +8.9 | 1e-16 | 23/43 (SW480, SK-MEL-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.22×** | +8.1 | 4e-14 | 9/18 (Hs 766T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.29×** | +8.1 | 4e-14 | 23/41 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.04×** | +7.3 | 2e-11 | 17/46 (NCI-H2030, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.86×** | +6.3 | 1e-08 | 19/41 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.53×** | +6.1 | 5e-08 | 16/44 (PANC-1, LS 180, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.80×** | +5.6 | 1e-06 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +5.3 | 4e-06 | 6/17 (A-427, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.62×** | +4.9 | 4e-05 | 15/45 (NCI-H2030, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.42×** | +4.7 | 1e-04 | 11/41 (NCI-H460, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.56×** | +4.5 | 2e-04 | 13/45 (NCI-H2030, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +4.3 | 6e-04 | 8/46 (A-172, A498, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.50×** | +3.9 | 0.003 | 9/41 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **2.08×** | +3.9 | 0.003 | 0/26 | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.86×** | +3.3 | 0.026 | 1/23 (NCI-H23) | top dose only | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.031 | 3/43 (NCI-H460, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2633.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Hydroxyurea (drug)]] 0.05 µM in 1 line (HEC-1-A 0.104×); [[9-ING-41 (drug)]] 0.05 µM in 1 line (SW1417 0.0347×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.623×** | -6.8 | 5e-09 | 19/45 (SW480, SW1417, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.703×** | -3.6 | 0.099 | 7/43 (Hs 766T, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.723× | -3.3 | 0.18 | 16/43 (AN3 CA, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2633. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 10.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.16× (z +11.9) | — |
| [[PANC-1 (line)]] | alt | 3.79 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.9× (z +16.5) | — |
| [[A-172 (line)]] | wt | 3.45 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.4× (z +12.9) | — |
| [[A549 (line)]] | wt | 2.61 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.4× (z +9.5) | — |
| [[CFPAC-1 (line)]] | alt | 2.39 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +9.2) | — |
| [[HEC-1-A (line)]] | alt | 7.10 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.104× (z -9.4) |
| [[J82 (line)]] | alt | 2.14 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +8.9) | — |
| [[LoVo (line)]] | wt | 4.04 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.9× (z +12.3) | — |
| [[NCI-H1573 (line)]] | alt | 4.31 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +8.5) | — |
| [[NCI-H23 (line)]] | alt | 7.07 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +8.6) | — |
| [[Panc 03.27 (line)]] | alt | 2.57 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +9.6) | — |
| [[SNU-423 (line)]] | alt | 2.18 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.0× (z +11.9) | — |
| [[SW1417 (line)]] | alt | 2.57 | 0 | 1 | — | [[9-ING-41 (drug)]] 0.05 µM 0.0347× (z -8.7) |
| [[A-427 (line)]] | wt | 9.32 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.26 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.96 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.909 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.19 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2633), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL11A2]] | +0.73 | +0.84 / +0.63 | both halves | 7e-06 |  |
| [[NPHS1]] | +0.71 | +0.67 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_DN |
| [[ELAVL3]] | +0.70 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[IL34]] | +0.66 | +0.75 / +0.58 | both halves | 8e-06 |  |
| [[TGIF2-RAB5IF]] | +0.64 | +0.74 / +0.52 | both halves | 1e-05 |  |
| [[PRRT3]] | +0.64 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[SEC1P]] | +0.64 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[TMPRSS9]] | +0.64 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[TTC36-AS1]] | +0.64 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[SPATC1]] | +0.63 | +0.73 / +0.54 | both halves | 1e-05 |  |
| [[PLA2G6]] | +0.63 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[DNAH12]] | +0.62 | +0.71 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EEF1E1]] | -0.56 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[ADPGK]] | -0.55 | -0.64 / -0.46 | both halves | 2e-05 |  |
| [[RFT1]] | -0.54 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[FBXW2]] | -0.54 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[MTERF3]] | -0.54 | -0.55 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NDUFA4L2]] | B | NDUFA4L2 activity raises KCNN1's level | lines that do not express NDUFA4L2 (16) vs lines expressing it (34) | 1.60× lower at baseline in the lines without NDUFA4L2 | 0.076 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[RRAD]] | B | RRAD activity lowers KCNN1's level | lines that do not express RRAD (31) vs lines expressing it (19) | 1.49× higher at baseline in the lines without RRAD | 0.096 | ⚠ within organs, on part of the lines; also absent: LOX, IL6, EDNRA |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 181]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.717). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.0, -6.6); signed map (23.8, 7.8). **Vector** length 68.3, 10.6% of its response variance represented; |z| ≥ 3 in 1,168 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.6 | +25.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +14.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +9.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.5 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +8.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +6.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +3.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.1 | +3.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.0 | +2.9 |
| fall | [[Selinexor (drug)]] 5 µM |  | -3.0 | -6.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.0 | -3.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | -2.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -1.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.5 | +0.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -2.3 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.4 | -2.2 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.4 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | potassium calcium-activated channel subfamily N member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:17,951,293-18,000,085 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KCa2.1, hSK1 |
| Gene groups (HGNC) | Potassium calcium-activated channels |
| Hallmark sets | KRAS_SIGNALING_DN |
| Reactome | 3 pathways, smallest: Ca2+ activated K+ channels; Potassium Channels; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92952](https://www.uniprot.org/uniprotkb/Q92952) (Small conductance calcium-activated potassium channel protein 1):

> Small conductance calcium-activated potassium channel that mediates the voltage-independent transmembrane transfer of potassium across the cell membrane through a constitutive interaction with calmodulin which binds the intracellular calcium allowing its opening. The current is characterized by a voltage-independent activation, an intracellular calcium concentration increase-dependent activation and a single-channel conductance of about 3 picosiemens. Also presents an inwardly rectifying …

**Summary**, from NCBI Gene [3780](https://www.ncbi.nlm.nih.gov/gene/3780):

> Action potentials in vertebrate neurons are followed by an afterhyperpolarization (AHP) that may persist for several seconds and may have profound consequences for the firing pattern of the neuron. Each component of the AHP is kinetically distinct and is mediated by different calcium-activated potassium channels. The protein encoded by this gene is activated before membrane hyperpolarization and is thought to regulate neuronal excitability by contributing to the slow component of synaptic AHP. …

**Accessions** — [HGNC:6290](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6290) · Entrez [3780](https://www.ncbi.nlm.nih.gov/gene/3780) · UniProt [Q92952](https://www.uniprot.org/uniprotkb/Q92952) · Ensembl [ENSG00000105642](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105642)

## Data

Gene col 2633: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2633); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2633, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2633]; `tensor/DDL_lfc|DDL_z.npy` [2633]; `embed/gene_vectors.npy` [2633]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2633 or target_col == 2633). Every well: [[KCNN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
