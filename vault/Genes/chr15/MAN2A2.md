---
symbol: "MAN2A2"
type: "gene"
col: 12233
ensembl_id: "ENSG00000196547"
name: "mannosidase alpha class 2A member 2"
location: "15q25"
module: 126
arm: "+"
pooled_cpm: 12.19
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 4
n_dd_up_clean: 1
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/126"]
generated_by: "tahoemap"
---

# MAN2A2

*mannosidase alpha class 2A member 2* — 15q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.46× (z +14.8, q 0e+00, up in 28 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.45× (z +8.7, q 7e-16, up in 24 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (PANC-1 3.30×, SW480 3.44×, KATO III 3.65×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 3.65×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.733× (z -5.1, q 2e-04, down in 23 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INPPL1]] (+0.70, fdr 1e-05), [[CERS2]] (+0.66, fdr 1e-05), [[SORBS3]] (+0.62, fdr 2e-05); moves opposite to [[SMIM30]] (-0.57, fdr 1e-04), [[NOL7]] (-0.52, fdr 4e-04, ⚠ NOL7 in the vector space only through flagged drug-doses), [[RPL36AL]] (-0.52, fdr 6e-05, ⚠ RPL36AL in the vector space only through flagged drug-doses), [[SF3B6]] (-0.51, fdr 1e-04), [[ATP5MJ]] (-0.49, fdr 1e-04).
> It is in [[Module 126]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NUP210]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12233.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (PANC-1 3.30×, SW480 3.44×, KATO III 3.65×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 3.65×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.46×** | +14.8 | 0e+00 | 28/36 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.42×** | +13.9 | 1e-41 | 19/22 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.27×** | +12.4 | 4e-33 | 26/30 (NCI-H1792, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +8.7 | 7e-16 | 24/44 (A549, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~2% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.34×** | +4.7 | 3e-04 | 15/39 (HOP62, LoVo, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +4.2 | 0.002 | 5/29 (NCI-H460, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 1.22× | +3.1 | 0.14 | 16/43 (hTERT-HPNE, LS 180, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.22× | +3.1 | 0.15 | 11/45 (NCI-H2347, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12233.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.733×** | -5.1 | 2e-04 | 23/46 (SW480, SW48, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.770×** | -4.3 | 0.004 | 20/46 (HepG2/C3A, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.775×** | -4.2 | 0.004 | 21/46 (SW480, HT-29, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.928× | -4.2 | 0.004 | 5/47 (BT-474, CFPAC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.666×** | -3.5 | 0.053 | 8/46 (NCI-H460, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | 0.825× | -3.2 | 0.13 | 9/46 (LS 180, LoVo, …) | inconsistent across doses | position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | 0.828× | -3.1 | 0.13 | 3/47 (NCI-H2030, CHP-212, …) | inconsistent across doses |  |
| [[Silodosin (drug)]] 5 µM |  | 0.822× | -3.1 | 0.13 | 13/45 (KATO III, C32, …) | top dose only |  |
| [[Clopidogrel (drug)]] 5 µM |  | 0.831× | -3.1 | 0.14 | 7/46 (CFPAC-1, A549, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12233. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 19.4 | 0 | 2 (1 ⚠) | — | [[Oxaprozin (drug)]] 0.5 µM 0.0573× (z -12.8) |
| [[SW480 (line)]] | alt | 12.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.65× (z +9.4) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 17.6 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.175× (z -10.5) |
| [[HepG2_C3A (line)]] | wt | 13.3 | 0 | 1 | — | [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.0708× (z -11.1) |
| [[Hs 766T (line)]] | wt | 5.22 | 0 | 1 | — | [[Fluvoxamine (maleate) (drug)]] 0.05 µM 0.0628× (z -10.5) |
| [[KATO III (line)]] | alt | 14.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 8.89 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.224× (z -10.5) |
| [[PANC-1 (line)]] | alt | 11.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +9.5) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 20.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0917× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change |
| [[SW 900 (line)]] | alt | 7.70 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 0.05 µM 0.0734× (z -9.9) |
| [[A-172 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.19 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.62 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.24 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.96 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.53 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12233), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INPPL1]] | +0.70 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[CERS2]] | +0.66 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[SORBS3]] | +0.62 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[ATP13A1]] | +0.62 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[ULK3]] | +0.62 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[SEPTIN8]] | +0.62 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[GRK2]] | +0.61 | +0.41 / +0.62 | both halves | 4e-05 |  |
| [[U2AF2]] | +0.61 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[UBQLN4]] | +0.61 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[PLXNB1]] | +0.60 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[MTA2]] | +0.60 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[STRN4]] | +0.59 | +0.58 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM30]] | -0.57 | -0.32 / -0.62 | both halves | 1e-04 |  |
| [[NOL7]] ⚠ | -0.52 | -0.25 / -0.53 | both halves | 4e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL36AL]] ⚠ | -0.52 | -0.38 / -0.48 | both halves | 6e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SF3B6]] | -0.51 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[ATP5MJ]] | -0.49 | -0.36 / -0.38 | both halves | 1e-04 |  |
| [[NBEAL1]] | -0.49 | -0.47 / -0.29 | both halves | 2e-04 |  |
| [[COX6A1]] | -0.49 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[RPL18]] ⚠ | -0.49 | -0.34 / -0.43 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[INIP]] | -0.49 | -0.43 / -0.36 | both halves | 9e-05 |  |
| [[ATP5PD]] | -0.48 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[EMC6]] | -0.48 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[TRAPPC2B]] | -0.48 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[ROMO1]] | -0.48 | -0.38 / -0.39 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NUP210]] | B | NUP210 activity raises MAN2A2's level | lines that do not express NUP210 (13) vs lines expressing it (37) | 1.72× lower at baseline in the lines without NUP210 | 0.023 | ⚠ within organs, on part of the lines; also absent: PRR36, NEBL, FAM169A |
| [[HDAC6]] | B | HDAC6 activity raises MAN2A2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 126]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.784). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.9, -23.7); signed map (-12.1, -35.5). **Vector** length 69.0, 11.0% of its response variance represented; |z| ≥ 3 in 806 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.3 | +13.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.6 | +14.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.1 | +12.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +8.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | +3.5 | +3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +0.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.1 | +1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +1.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.7 | +2.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.6 | +1.4 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -1.9 | -3.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.8 | -5.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.7 | -4.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.4 | -2.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -1.3 | -4.2 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.3 | -1.7 |
|  | [[Thymol (drug)]] 5 µM |  | -1.2 | -0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.2 | -1.6 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.2 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | mannosidase alpha class 2A member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25 — chr15:90,902,218-90,922,584 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MANA2X, HsT19662, alpha-MIIx |
| Gene groups (HGNC) | Mannosidases alpha class 2 |
| Reactome | 8 pathways, smallest: Reactions specific to the complex N-glycan synthesis pathway; N-glycan antennae elongation in the medial/trans-Golgi; Intra-Golgi traffic |
| Matched by | ensembl_id |

**Function**, from UniProt [P49641](https://www.uniprot.org/uniprotkb/P49641) (Alpha-mannosidase 2x):

> Catalyzes the first committed step in the biosynthesis of complex N-glycans. It controls conversion of high mannose to complex N-glycans; the final hydrolytic step in the N-glycan maturation pathway.

**Summary**, from NCBI Gene [4122](https://www.ncbi.nlm.nih.gov/gene/4122):

> Predicted to enable alpha-mannosidase activity. Predicted to be involved in N-glycan processing. Predicted to be active in Golgi membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:6825](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6825) · Entrez [4122](https://www.ncbi.nlm.nih.gov/gene/4122) · UniProt [P49641](https://www.uniprot.org/uniprotkb/P49641) · Ensembl [ENSG00000196547](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196547)

## Data

Gene col 12233: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12233); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12233, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12233]; `tensor/DDL_lfc|DDL_z.npy` [12233]; `embed/gene_vectors.npy` [12233]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12233 or target_col == 12233). Every well: [[MAN2A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAN2A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
